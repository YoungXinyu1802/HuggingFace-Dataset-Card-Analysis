---
annotations_creators:
- expert-generated
language_creators:
- expert-generated
language:
- en
license:
- apache-2.0
multilinguality:
- monolingual
pretty_name: TruthfulQA
size_categories:
- n<1K
source_datasets:
- original
task_categories:
- question-answering
task_ids:
- extractive-qa
- open-domain-qa
- closed-domain-qa
---

# Dataset Card for TruthfulQA

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
 - [Contributions](#contributions)

## Dataset Description

- **Homepage:** [https://github.com/sylinrl/TruthfulQA](https://github.com/sylinrl/TruthfulQA)
- **Repository:** [https://github.com/sylinrl/TruthfulQA](https://github.com/sylinrl/TruthfulQA)
- **Paper:** [https://arxiv.org/abs/2109.07958](https://arxiv.org/abs/2109.07958)

### Dataset Summary

TruthfulQA: Measuring How Models Mimic Human Falsehoods

We propose a benchmark to measure whether a language model is truthful in generating answers to questions. The benchmark comprises 817 questions that span 38 categories, including health, law, finance and politics. We crafted questions that some humans would answer falsely due to a false belief or misconception. To perform well, models must avoid generating false answers learned from imitating human texts. We tested GPT-3, GPT-Neo/J, GPT-2 and a T5-based model. The best model was truthful on 58% of questions, while human performance was 94%. Models generated many false answers that mimic popular misconceptions and have the potential to deceive humans. The largest models were generally the least truthful. This contrasts with other NLP tasks, where performance improves with model size. However, this result is expected if false answers are learned from the training distribution. We suggest that scaling up models alone is less promising for improving truthfulness than fine-tuning using training objectives other than imitation of text from the web.

### Supported Tasks and Leaderboards

See: [Tasks](https://github.com/sylinrl/TruthfulQA#tasks)

### Languages

English

## Dataset Structure

### Data Instances

The benchmark comprises 817 questions that span 38 categories, including health, law, finance and politics.

### Data Fields

1. **Type**: Adversarial v Non-Adversarial Questions
2. **Category**: Category of misleading question
3. **Question**: The question
4. **Best Answer**: The best correct answer
5. **Correct Answers**: A set of correct answers. Delimited by `;`.
6. **Incorrect Answers**: A set of incorrect answers. Delimited by `;`.
7. **Source**: A source that supports the correct answers.

### Data Splits

Due to constraints of huggingface the dataset is loaded into a "train" split.

### Contributions

Thanks to [@sylinrl](https://github.com/sylinrl) for adding this dataset.