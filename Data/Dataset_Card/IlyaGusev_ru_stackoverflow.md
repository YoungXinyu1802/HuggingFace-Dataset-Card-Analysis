---
license: other
task_categories:
- text-generation
- question-answering
language:
- ru
size_categories:
- 100K<n<1M
dataset_info:
  features:
  - name: question_id
    dtype: uint32
  - name: url
    dtype: string
  - name: answer_count
    dtype: uint32
  - name: text_html
    dtype: string
  - name: text_markdown
    dtype: string
  - name: score
    dtype: int32
  - name: title
    dtype: string
  - name: tags
    sequence: string
  - name: views
    dtype: uint64
  - name: author
    dtype: string
  - name: timestamp
    dtype: uint64
  - name: comments
    sequence:
    - name: text
      dtype: string
    - name: author
      dtype: string
    - name: comment_id
      dtype: uint32
    - name: score
      dtype: int32
    - name: timestamp
      dtype: uint64
  - name: answers
    sequence:
    - name: answer_id
      dtype: uint32
    - name: is_accepted
      dtype: uint8
    - name: text_html
      dtype: string
    - name: text_markdown
      dtype: string
    - name: score
      dtype: int32
    - name: author
      dtype: string
    - name: timestamp
      dtype: uint64
    - name: comments
      sequence:
      - name: text
        dtype: string
      - name: author
        dtype: string
      - name: comment_id
        dtype: uint32
      - name: score
        dtype: int32
      - name: timestamp
        dtype: uint64
  splits:
  - name: train
    num_bytes: 3013377174
    num_examples: 437604
  download_size: 670468664
  dataset_size: 3013377174
---

# Russian StackOverflow dataset

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Description](#description)
- [Usage](#usage)
- [Data Instances](#data-instances)
- [Source Data](#source-data)
- [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Licensing Information](#licensing-information)

## Description

**Summary:** Dataset of questions, answers, and comments from [ru.stackoverflow.com](https://ru.stackoverflow.com/).

**Script:** [create_stackoverflow.py](https://github.com/IlyaGusev/rulm/blob/hf/data_processing/create_stackoverflow.py)

**Point of Contact:** [Ilya Gusev](ilya.gusev@phystech.edu)

**Languages:** The dataset is in Russian with some programming code.


## Usage

Prerequisites:
```bash
pip install datasets zstandard jsonlines pysimdjson
```

Loading:
```python
from datasets import load_dataset
dataset = load_dataset('IlyaGusev/ru_stackoverflow', split="train")
for example in dataset:
    print(example["text_markdown"])
    print()
```

## Data Instances

```
{
  "question_id": 11235,
  "answer_count": 1,
  "url": "https://ru.stackoverflow.com/questions/11235",
  "score": 2,
  "tags": ["c++", "сериализация"],
  "title": "Извлечение из файла, запись в файл",
  "views": 1309,
  "author": "...",
  "timestamp": 1303205289,
  "text_html": "...",
  "text_markdown": "...",
  "comments": {
    "text": ["...", "...",
    "author": ["...", "..."],
    "comment_id": [11236, 11237],
    "score": [0, 0],
    "timestamp": [1303205411, 1303205678]
  },
  "answers": {
    "answer_id": [11243, 11245],
    "timestamp": [1303207791, 1303207792],
    "is_accepted": [1, 0],
    "text_html": ["...", "..."],
    "text_markdown": ["...", "..."],
    "score": [3, 0],
    "author": ["...", "..."],
    "comments": {
      "text": ["...", "..."],
      "author": ["...", "..."],
      "comment_id": [11246, 11249],
      "score": [0, 0],
      "timestamp": [1303207961, 1303207800]
    }
  }
}
```

You can use this little helper to unflatten sequences:
```python
def revert_flattening(records):
    fixed_records = []
    for key, values in records.items():
        if not fixed_records:
            fixed_records = [{} for _ in range(len(values))]
        for i, value in enumerate(values):
            fixed_records[i][key] = value
    return fixed_records
```

The original JSONL is already unflattened.

## Source Data

* The data source is the [Russian StackOverflow](https://ru.stackoverflow.com/) website.
* Original XMLs: [ru.stackoverflow.com.7z](https://ia600107.us.archive.org/27/items/stackexchange/ru.stackoverflow.com.7z).
* Processing script is [here](https://github.com/IlyaGusev/rulm/blob/hf/data_processing/create_stackoverflow.py). 

## Personal and Sensitive Information

The dataset is not anonymized, so individuals' names can be found in the dataset. Information about the original authors is included in the dataset where possible.

## Licensing Information

According to the license of original data, this dataset is distributed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/).