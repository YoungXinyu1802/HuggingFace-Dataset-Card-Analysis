---
license: cc-by-sa-4.0
task_categories:
- question-answering
language:
- en
pretty_name: H4 Stack Exchange Preferences Dataset
tags:
- RLHF
- preferences
- human-feedback
- Stack Exchange
download_size: 22132072448
size_categories:
- 10M<n<100M
---
# Dataset Card for H4 Stack Exchange Preferences Dataset

## Dataset Description

- **Homepage:** https://archive.org/details/stackexchange
- **Repository:** (private for now) https://github.com/huggingface/h4
- **Point of Contact:** Nathan Lambert, nathan@huggingface.co
- **Size of downloaded dataset:** 22.13 GB
- **Number of instructions:** 10,741,532

### Dataset Summary

This dataset contains questions and answers from the [Stack Overflow Data Dump](https://archive.org/details/stackexchange) for the purpose of **preference model training**. 
Importantly, the questions have been filtered to fit the following criteria for preference models (following closely from [Askell et al. 2021](https://arxiv.org/abs/2112.00861)): *have >=2 answers*. 
This data could also be used for instruction fine-tuning and language model training.

The questions are grouped with answers that are assigned a score corresponding to the Anthropic paper:
```
score = log2 (1 + upvotes) rounded to the nearest integer, plus 1 if the answer was accepted by the questioner (we assign a score of −1 if the number of upvotes is negative).
```

Some important notes when using this dataset for preference model pretraining (PMP), which can be ignored for other uses: 
* the data will likely need to be filtered more due to matching scores.
* see section 4.1 of Askel et al 2021 for instructions on using each pair of samples twice via the following `binarization` (for better pre-training initialization):

```
Subsequently, we created a binary dataset by applying a ‘binarization’ procedure to the ranked dataset. That
is, for every ranked pair A > B, we transform it into two independent binary comparisons:
GOOD:A > BAD:A
BAD:B > GOOD:B
```
To see all the stackexchanges used in this data, please see [this file](https://huggingface.co/datasets/HuggingFaceH4/pmp-stack-exchange/blob/main/stack_exchanges.json).

Unfortunately, sharing the binarized data directly without metadata violates the license, so we have shared a script for binarization.


### Using the data
Here is a script from our internal tooling used to create a binarized dataset:
```
# Copyright 2023 The HuggingFace Team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import random
from argparse import ArgumentParser
from pathlib import Path

import numpy as np
from datasets import Dataset, concatenate_datasets, load_dataset

from h4.data.utils import save_dataset_shards


H4_DIR = Path(__file__).resolve().parents[3]
DATA_DIR = H4_DIR / "data"

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--debug", action="store_true", help="Added print statements / limit data size for debugging")
    parser.add_argument(
        "--output_dir",
        default=f"{DATA_DIR}/pmp-binarized",
        type=str,
        help="Where to save the processed dataset",
    )
    parser.add_argument(
        "--exchange_name",
        type=str,
        default=None,
        help="Optional argument to specify a specific subsection of the dataset",
    )
    parser.add_argument(
        "--binary_score", type=int, default=8, help="Score assigned to binarized pairs for preference data."
    )
    parser.add_argument(
        "--stream_data", action="store_true", help="Optionally stream data, which can be useful with weaker computers"
    )
    parser.set_defaults(debug=False, stream_data=False)  # default will process full dataset

    args = parser.parse_args()
    specific_exchange = args.exchange_name
    stream_dataset = args.stream_data
    binary_score = args.binary_score

    if specific_exchange:
        data_dir = "data/" + args.exchange_name
    else:
        data_dir = None

    if args.debug:
        data_len_limit = 10000
    else:
        data_len_limit = np.inf

    dataset = load_dataset(
        "HuggingFaceH4/pmp-stack-exchange",
        data_dir=data_dir,
        split="train",
        streaming=stream_dataset,
    )

    pmp_data = []
    for i, d in enumerate(iter(dataset)):
        # check debug limit, quit if in debug mode (don't save)
        if i > data_len_limit:
            print("Early exit for debug mode!")
            print(pmp_data)
            break

        question = d["question"]
        answers = d["answers"]
        num_answers = len(answers)

        answer_scores = [a["pm_score"] for a in answers]
        if len(np.unique(answer_scores)) < 2:
            print(f"PM Scores are {answer_scores}, skipping this question {i}")
        else:
            # Sample 2 unique scores for binarization
            dif_scores = False
            while not dif_scores:
                # print("infinite loop...?")
                two_answers = random.sample(answers, 2)

                if two_answers[0]["pm_score"] != two_answers[1]["pm_score"]:
                    dif_scores = True

        answer_0 = two_answers[0]
        answer_1 = two_answers[1]
        text_0 = "Question: " + question + "\n" + "Answer: " + answer_0["text"]
        text_1 = "Question: " + question + "\n" + "Answer: " + answer_1["text"]
        score_0 = binary_score
        score_1 = binary_score

        pmp_data.append({"context": text_0, "score": score_0})
        pmp_data.append({"context": text_1, "score": score_1})

    # Save binarized data
    sublist_len = 100000

    print(f"Dataset length is {len(pmp_data)}")
    # bypass known issue in arrow https://issues.apache.org/jira/browse/ARROW-17137
    print(f"Processed dataset length > {sublist_len}, processing to HF dataset in chunks")
    chunks = [pmp_data[x : x + sublist_len] for x in range(0, len(pmp_data), sublist_len)]
    ds_chunks = [Dataset.from_list(ch) for ch in chunks]
    ds = concatenate_datasets(ds_chunks)

    save_dataset_shards(ds, args.output_dir, subset="stackexchange", shard_size="100MB")
```


### Languages

This is intended to be English only, thought other languages may be present. Some Stack Exchanges that are omitted include: 

```
spanish: es.meta.stackoverflow.com, es.stackoverflow.com
japanese: ja.meta.stackoverflow.com, ja.stackoverflow.com
portugese: pt.stackoverflow.com, pt.meta.stackoverflow.com
russian: ru.stackoverflow, ru.meta.stackoverflow
```

### Licensing Information

License:  https://creativecommons.org/licenses/by-sa/4.0/

The cc-by-sa 4.0 licensing, while intentionally permissive, does require attribution:

Attribution — You must attribute the work in the manner specified by the author or licensor (but not in any way that suggests that they endorse you or your use of the work).
Specifically the attribution requirements are as follows:
1. Visually display or otherwise indicate the source of the content as coming from the Stack Exchange Network. This requirement is satisfied with a discreet text blurb, or some other unobtrusive but clear visual indication.
2. Ensure that any Internet use of the content includes a hyperlink directly to the original question on the source site on the Network (e.g., http://stackoverflow.com/questions/12345)
3. Visually display or otherwise clearly indicate the author names for every question and answer used
4. Ensure that any Internet use of the content includes a hyperlink for each author name directly back to his or her user profile page on the source site on the Network (e.g., http://stackoverflow.com/users/12345/username), directly to the Stack Exchange domain, in standard HTML (i.e. not through a Tinyurl or other such indirect hyperlink, form of obfuscation or redirection), without any “nofollow” command or any other such means of avoiding detection by search engines, and visible even with JavaScript disabled.
For more information, see the Stack Exchange Terms of Service.

### Citation Information

```
@online{h4stackexchange,
  author = {Lambert, Nathan and Tunstall, Lewis and Rajani, Nazneen and Thrush, Tristan},
  title = {HuggingFace H4 Stack Exchange Preference Dataset},
  year = 2023,
  url = {https://huggingface.co/datasets/HuggingFaceH4/stack-exchange-preferences},
}
```