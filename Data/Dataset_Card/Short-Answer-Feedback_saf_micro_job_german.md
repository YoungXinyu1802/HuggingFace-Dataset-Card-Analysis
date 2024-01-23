---
pretty_name: SAF - Micro Job - German
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
- micro job
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
  - name: score
    dtype: float64
  splits:
  - name: train
    num_bytes: 885526
    num_examples: 1226
  - name: validation
    num_bytes: 217946
    num_examples: 308
  - name: test_unseen_answers
    num_bytes: 198832
    num_examples: 271
  - name: test_unseen_questions
    num_bytes: 545524
    num_examples: 602
  download_size: 274603
  dataset_size: 1847828
---
# Dataset Card for "saf_micro_job_german"

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Annotation process](#annotation-process) 
- [Additional Information](#additional-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Paper:** [Your Answer is Incorrect... Would you like to know why? Introducing a Bilingual Short Answer Feedback Dataset](https://aclanthology.org/2022.acl-long.587) (Filighera et al., ACL 2022)

### Dataset Summary

Short Answer Feedback (SAF) dataset is a short answer dataset introduced in [Your Answer is Incorrect... Would you like to know why? Introducing a Bilingual Short Answer Feedback Dataset](https://aclanthology.org/2022.acl-long.587) (Filighera et al., ACL 2022) as a way to remedy the lack of content-focused feedback datasets. This version of the dataset contains 8 German questions used in micro-job training on the crowd-worker platform appJobber - while the original dataset presented in the paper is comprised of an assortment of both English and German short answer questions (with reference answers). Please refer to the [saf_communication_networks_english](https://huggingface.co/datasets/Short-Answer-Feedback/saf_communication_networks_english) dataset to examine the English subset of the original dataset. Furthermore, a similarly constructed SAF dataset (covering the German legal domain) can be found at [saf_legal_domain_german](https://huggingface.co/datasets/Short-Answer-Feedback/saf_legal_domain_german). 

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
    "question": "Frage 1: Ist das eine Frage?",
    "reference_answer": "Ja, das ist eine Frage.",
    "provided_answer": "Ich bin mir sicher, dass das eine Frage ist.",
    "answer_feedback": "Korrekt!",
    "verification_feedback": "Correct",
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
- `score`: a `float64` feature (between 0 and 1) representing the score given to the provided answer.

### Data Splits

The dataset is comprised of four data splits.

- `train`: used for training, contains a set of questions and the provided answers to them.
- `validation`: used for validation, contains a set of questions and the provided answers to them (derived from the original training set defined in the paper).
- `test_unseen_answers`: used for testing, contains unseen answers to the questions present in the `train` split.
- `test_unseen_questions`: used for testing, contains unseen questions that do not appear in the `train` split.

|   Split           |train|validation|test_unseen_answers|test_unseen_questions|
|-------------------|----:|---------:|------------------:|--------------------:|
|Number of instances| 1226|       308|                271|                  602|

## Dataset Creation

### Annotation Process

Two experienced appJobber employees were selected to evaluate the crowd-worker platform’s answers, and both of them underwent a general annotation guideline training (supervised by a Psychology doctoral student with prior work in the field of feedback). After the training, the annotators individually provided feedback to the answers following an agreed upon scoring rubric and the general annotation guideline. The individually annotated answer files were then combined into a cohesive gold standard after discussing and solving possible disagreements.      

## Additional Information

### Citation Information

```
@inproceedings{filighera-etal-2022-answer,
    title = "Your Answer is Incorrect... Would you like to know why? Introducing a Bilingual Short Answer Feedback Dataset",
    author = "Filighera, Anna  and
      Parihar, Siddharth  and
      Steuer, Tim  and
      Meuser, Tobias  and
      Ochs, Sebastian",
    booktitle = "Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = may,
    year = "2022",
    address = "Dublin, Ireland",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.acl-long.587",
    doi = "10.18653/v1/2022.acl-long.587",
    pages = "8577--8591",
}
```

### Contributions

Thanks to [@JohnnyBoy2103](https://github.com/JohnnyBoy2103) for adding this dataset.