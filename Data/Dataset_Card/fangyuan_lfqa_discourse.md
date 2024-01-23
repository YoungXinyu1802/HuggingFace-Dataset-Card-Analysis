---
annotations_creators:
- crowdsourced
- expert-generated
language_creators:
- machine-generated
- found
language:
- en-US
license:
- cc-by-sa-4.0
multilinguality:
- monolingual
pretty_name: lfqa_discourse
size_categories:
- unknown
source_datasets:
- extended|natural_questions
- extended|eli5
task_categories: []
task_ids: []
---

# Dataset Card for LFQA Discourse

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Repository:** [Repo](https://github.com/utcsnlp/lfqa_discourse)
- **Paper:** [How Do We Answer Complex Questions: Discourse Structure of Long-form Answers](https://arxiv.org/abs/2203.11048)
- **Point of Contact:** fangyuan[at]utexas.edu

### Dataset Summary

This dataset contains discourse annotation of long-form answers. There are two types of annotations:
* **Validity:** whether a <question, answer> pair is valid based on a set of invalid reasons defined.
* **Role:** sentence-level role annotation of functional roles for long-form answers.

### Languages

The dataset contains data in English.

## Dataset Structure

### Data Instances

Each instance is a (question, long-form answer) pair from one of the four data sources -- ELI5, WebGPT, NQ, and model-generated answers (denoted as ELI5-model), and our discourse annotation, which consists of QA-pair level validity label and sentence-level functional role label.

We provide all validity and role annotations here. For further train/val/test split, please refer to our [github repository](https://github.com/utcsnlp/lfqa_discourse).

### Data Fields

For validity annotations, each instance contains the following fields:
* `dataset`: The dataset this QA pair belongs to, one of [`NQ`, `ELI5`, `Web-GPT`]. Note that `ELI5` contains both human-written answers and model-generated answers, with model-generated answer distinguished with the `a_id` field mentioned below.
* `q_id`: The question id, same as the original NQ or ELI5 dataset.
* `a_id`: The answer id, same as the original ELI5 dataset. For NQ, we populate a dummy `a_id` (1). For machine generated answers, this field corresponds to the name of the model. 
* `question`: The question.
* `answer_paragraph`: The answer paragraph.
* `answer_sentences`: The list of answer sentences, tokenized from the answer paragraph.
* `is_valid`: A boolean value indicating whether the qa pair is valid, values: [`True`, `False`].
* `invalid_reason`: A list of list, each list contains the invalid reason the annotator selected. The invalid reason is one of [`no_valid_answer`, `nonsensical_question`, `assumptions_rejected`, `multiple_questions`].

For role annotations, each instance contains the following fields:
* 
* `dataset`: The dataset this QA pair belongs to, one of [`NQ`, `ELI5`, `Web-GPT`]. Note that `ELI5` contains both human-written answers and model-generated answers, with model-generated answer distinguished with the `a_id` field mentioned below.
* `q_id`: The question id, same as the original NQ or ELI5 dataset.
* `a_id`: The answer id, same as the original ELI5 dataset. For NQ, we populate a dummy `a_id` (1). For machine generated answers, this field corresponds to the name of the model. 
* `question`: The question.
* `answer_paragraph`: The answer paragraph.
* `answer_sentences`: The list of answer sentences, tokenized from the answer paragraph.
* `role_annotation`: The list of majority role (or adjudicated) role (if exists), for the sentences in `answer_sentences`. Each role is one of [`Answer`, `Answer - Example`, `Answer (Summary)`, `Auxiliary Information`, `Answer - Organizational sentence`, `Miscellaneous`]
* `raw_role_annotation`: A list of list, each list contains the raw role annotations for sentences in `answer_sentences`.


### Data Splits

For train/validation/test splits, please refer to our [repository]((https://github.com/utcsnlp/lfqa_discourse).

## Dataset Creation

Please refer to our [paper](https://arxiv.org/abs/2203.11048) and datasheet for details on dataset creation, annotation process and discussion on limitations.

## Additional Information


### Licensing Information

https://creativecommons.org/licenses/by-sa/4.0/legalcode

### Citation Information
```
@inproceedings{xu2022lfqadiscourse,
  title     = {How Do We Answer Complex Questions: Discourse Structure of Long-form Answers},
  author    = {Xu, Fangyuan and Li, Junyi Jessy and Choi, Eunsol},
  year      = 2022,
  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},
  note      = {Long paper}
}
```
### Contributions

Thanks to [@carriex](https://github.com/carriex) for adding this dataset.