---
license: cc-by-4.0
language:
- en
- de
multilinguality:
- multilingual
source_datasets:
- extended|deutsche-telekom/NLU-Evaluation-Data-en-de
size_categories:
- 1K<n<10K
task_categories:
- text-classification
task_ids:
- intent-classification
---

# NLU Few-shot Benchmark - English and German
This is a few-shot training dataset from the domain of human-robot interaction.
It contains texts in German and English language with 64 different utterances (classes).
Each utterance (class) has exactly 20 samples in the training set.
This leads to a total of 1280 different training samples.

The dataset is intended to benchmark the intent classifiers of chat bots in English and especially in German language.
We are building on our
[deutsche-telekom/NLU-Evaluation-Data-en-de](https://huggingface.co/datasets/deutsche-telekom/NLU-Evaluation-Data-en-de)
data set.

## Processing Steps
- drop `NaN` values
- drop duplicates in `answer_de` and `answer`
- delete all rows where `answer_de` has more than 70 characters
- add column `label`: `df["label"] = df["scenario"] + "_" + df["intent"]`
- remove classes (`label`) with less than 25 samples:
  - `audio_volume_other`
  - `cooking_query`
  - `general_greet`
  - `music_dislikeness`
- random selection for train set - exactly 20 samples for each class (`label`)
- rest for test set

## Copyright
Copyright (c) the authors of [xliuhw/NLU-Evaluation-Data](https://github.com/xliuhw/NLU-Evaluation-Data)\
Copyright (c) 2022 [Philip May](https://may.la/), [Deutsche Telekom AG](https://www.telekom.com/)

All data is released under the
[Creative Commons Attribution 4.0 International License (CC BY 4.0)](http://creativecommons.org/licenses/by/4.0/).
