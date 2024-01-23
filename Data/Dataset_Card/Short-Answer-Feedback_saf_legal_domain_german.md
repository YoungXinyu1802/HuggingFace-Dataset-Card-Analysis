---
pretty_name: SAF - Legal Domain - German
annotations_creators:
- expert-generated
language:
- de
language_creators:
- other
multilinguality:
- monolingual
size_categories:
- 1K<n<10K
source_datasets:
- original
tags:
- short answer feedback
- legal domain
task_categories:
- text2text-generation
dataset_info:
  features:
  - name: id
    dtype: string
  - name: question
    dtype: string
  - name: reference_answer
    dtype: string
  - name: provided_answer
    dtype: string
  - name: answer_feedback
    dtype: string
  - name: verification_feedback
    dtype: string
  - name: error_class
    dtype: string
  - name: score
    dtype: float64
  splits:
  - name: train
    num_bytes: 2142112
    num_examples: 1596
  - name: validation
    num_bytes: 550206
    num_examples: 400
  - name: test_unseen_answers
    num_bytes: 301087
    num_examples: 221
  - name: test_unseen_questions
    num_bytes: 360616
    num_examples: 275
  download_size: 484808
  dataset_size: 3354021
---

# Dataset Card for "saf_legal_domain_german"

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Additional Information](#additional-information)
  - [Contributions](#contributions)

## Dataset Description

### Dataset Summary

This Short Answer Feedback (SAF) dataset contains 19 German questions in the domain of the German social law (with reference answers). The idea of constructing a bilingual (English and German) short answer dataset as a way to remedy the lack of content-focused feedback datasets was introduced in [Your Answer is Incorrect... Would you like to know why? Introducing a Bilingual Short Answer Feedback Dataset](https://aclanthology.org/2022.acl-long.587) (Filighera et al., ACL 2022). Please refer to [saf_micro_job_german](https://huggingface.co/datasets/Short-Answer-Feedback/saf_micro_job_german) and [saf_communication_networks_english](https://huggingface.co/datasets/Short-Answer-Feedback/saf_communication_networks_english) for similarly constructed datasets that can be used for SAF tasks.

### Supported Tasks and Leaderboards

- `short_answer_feedback`: The dataset can be used to train a Text2Text Generation model from HuggingFace transformers in order to generate automatic short answer feedback. 

### Languages

The questions, reference answers, provided answers and the answer feedback in the dataset are written in German.

## Dataset Structure

### Data Instances

An example of an entry of the training split looks as follows.

```
{
    "id": "1",
    "question": "Ist das eine Frage?",
    "reference_answer": "Ja, das ist eine Frage.",
    "provided_answer": "Ich bin mir sicher, dass das eine Frage ist.",
    "answer_feedback": "Korrekt.",
    "verification_feedback": "Correct",
    "error_class": "Keine",
    "score": 1
}
```

### Data Fields

The data fields are the same among all splits.

- `id`: a `string` feature (UUID4 in HEX format).
- `question`: a `string` feature representing a question.
- `reference_answer`: a `string` feature representing a reference answer to the question.
- `provided_answer`: a `string` feature representing an answer that was provided for a particular question.
- `answer_feedback`: a `string` feature representing the feedback given to the provided answers.
- `verification_feedback`: a `string` feature representing an automatic labeling of the score. It can be `Correct` (`score` = 1), `Incorrect` (`score` = 0) or `Partially correct` (all intermediate scores).
- `error_class`: a `string` feature representing the type of error identified in the case of a not completely correct answer.
- `score`: a `float64` feature (between 0 and 1) representing the score given to the provided answer.

### Data Splits

The dataset is comprised of four data splits.

- `train`: used for training, contains a set of questions and the provided answers to them.
- `validation`: used for validation, contains a set of questions and the provided answers to them (derived from the original training set from which the data came from).
- `test_unseen_answers`: used for testing, contains unseen answers to the questions present in the `train` split.
- `test_unseen_questions`: used for testing, contains unseen questions that do not appear in the `train` split.

|   Split           |train|validation|test_unseen_answers|test_unseen_questions|
|-------------------|----:|---------:|------------------:|--------------------:|
|Number of instances| 1596|       400|                221|                  275|

## Additional Information

### Contributions
Thanks to [@JohnnyBoy2103](https://github.com/JohnnyBoy2103) for adding this dataset.