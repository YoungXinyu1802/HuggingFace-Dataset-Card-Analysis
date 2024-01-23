---
license: cc-by-4.0
source_datasets:
- extended|nlu_evaluation_data
multilinguality:
- multilingual
language:
- en
- de
size_categories:
- 10K<n<100K
task_categories:
- text-classification
task_ids:
- intent-classification
---

# NLU Evaluation Data - English and German
A labeled English **and German** language multi-domain dataset (21 domains) with 25K user utterances for human-robot interaction.

This dataset is collected and annotated for evaluating NLU services and platforms.
The detailed paper on this dataset can be found at arXiv.org:
[Benchmarking Natural Language Understanding Services for building Conversational Agents](https://arxiv.org/abs/1903.05566)

The dataset builds on the annotated data of the [xliuhw/NLU-Evaluation-Data](https://github.com/xliuhw/NLU-Evaluation-Data)
repository. We have added an additional column (`answer_de`)
by translating the texts in column `answer` into German.
The translation was made with [DeepL](https://www.deepl.com/translator).

## Labels
The columns `scenario` and `intent` can be used for classification tasks.
However, we recommend to use even more fine-grained labels.
For this purpose, a new label can be derived by concatenating `scenario` and `intent`.
For example, this would turn "alarm" and "set" into "alarm_set".

## Dataset Quirks
The original dataset contains some `NaN` values in the `answer` column.
This means that there are also `NaN` values in the translations (`answer_de` column).
These rows should be filtered.

The dataset also contains duplicate values.

## Copyright
Copyright (c) the authors of [xliuhw/NLU-Evaluation-Data](https://github.com/xliuhw/NLU-Evaluation-Data)\
Copyright (c) 2022 [Philip May](https://may.la/)

All data is released under the
[Creative Commons Attribution 4.0 International License (CC BY 4.0)](http://creativecommons.org/licenses/by/4.0/).
