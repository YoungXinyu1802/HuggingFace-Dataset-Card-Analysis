---
annotations_creators:
- generated
language_creators:
- found
language:
- en
license: mit
multilinguality:
- monolingual
size_categories:
- 100K<n<1M
source_datasets:
- original
task_categories:
- question-answering
task_ids:
- extractive-qa
- open-domain-qa
pretty_name: synQA
---


# Dataset Card for synQA

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks](#supported-tasks)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Homepage:** [synQA homepage](https://github.com/maxbartolo/improving-qa-model-robustness)
- **Paper:** [Improving Question Answering Model Robustness with Synthetic Adversarial Data Generation](https://aclanthology.org/2021.emnlp-main.696/)
- **Point of Contact:** [Max Bartolo](max.bartolo@ucl.ac.uk)

### Dataset Summary

SynQA is a Reading Comprehension dataset created in the work "Improving Question Answering Model Robustness with Synthetic Adversarial Data Generation" (https://aclanthology.org/2021.emnlp-main.696/).
It consists of 314,811 synthetically generated questions on the passages in the SQuAD v1.1 (https://arxiv.org/abs/1606.05250) training set.

In this work, we use a synthetic adversarial data generation to make QA models more robust to human adversaries. We develop a data generation pipeline that selects source passages, identifies candidate answers, generates questions, then finally filters or re-labels them to improve quality. Using this approach, we amplify a smaller human-written adversarial dataset to a much larger set of synthetic question-answer pairs. By incorporating our synthetic data, we improve the state-of-the-art on the AdversarialQA (https://adversarialqa.github.io/) dataset by 3.7F1 and improve model generalisation on nine of the twelve MRQA datasets. We further conduct a novel human-in-the-loop evaluation to show that our models are considerably more robust to new human-written adversarial examples: crowdworkers can fool our model only 8.8% of the time on average, compared to 17.6% for a model trained without synthetic data.

For full details on how the dataset was created, kindly refer to the paper.

### Supported Tasks

`extractive-qa`: The dataset can be used to train a model for Extractive Question Answering, which consists in selecting the answer to a question from a passage. Success on this task is typically measured by achieving a high word-overlap [F1 score](https://huggingface.co/metrics/f1).ilable as round 1 of the QA task on [Dynabench](https://dynabench.org/tasks/2#overall) and ranks models based on F1 score.

### Languages

The text in the dataset is in English. The associated BCP-47 code is `en`.

## Dataset Structure

### Data Instances

Data is provided in the same format as SQuAD 1.1. An example is shown below:

```
{
  "data": [
    {
      "title": "None",
      "paragraphs": [
        {
          "context": "Architecturally, the school has a Catholic character. Atop the Main Building's gold dome is a golden statue of the Virgin Mary. Immediately in front of the Main Building and facing it, is a copper statue of Christ with arms upraised with the legend \"Venite Ad Me Omnes\". Next to the Main Building is the Basilica of the Sacred Heart. Immediately behind the basilica is the Grotto, a Marian place of prayer and reflection. It is a replica of the grotto at Lourdes, France where the Virgin Mary reputedly appeared to Saint Bernadette Soubirous in 1858. At the end of the main drive (and in a direct line that connects through 3 statues and the Gold Dome), is a simple, modern stone statue of Mary.",
          "qas": [
            {
              "id": "689f275aacba6c43ff112b2c7cb16129bfa934fa",
              "question": "What material is the statue of Christ made of?",
              "answers": [
                {
                  "answer_start": 190,
                  "text": "organic copper"
                }
              ]
            },
            {
              "id": "73bd3f52f5934e02332787898f6e568d04bc5403",
              "question": "Who is on the Main Building's gold dome?",
              "answers": [
                {
                  "answer_start": 111,
                  "text": "the Virgin Mary."
                }
              ]
            },
            {
              "id": "4d459d5b75fd8a6623446290c542f99f1538cf84",
              "question": "What kind of statue is at the end of the main drive?",
              "answers": [
                {
                  "answer_start": 667,
                  "text": "modern stone"
                }
              ]
            },
            {
              "id": "987a1e469c5b360f142b0a171e15cef17cd68ea6",
              "question": "What type of dome is on the Main Building at Notre Dame?",
              "answers": [
                {
                  "answer_start": 79,
                  "text": "gold"
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}
```

### Data Fields

- title: all "None" in this dataset
- context: the context/passage
- id: a string identifier for each question
- answers: a list of all provided answers (one per question in our case, but multiple may exist in SQuAD) with an `answer_start` field which is the character index of the start of the answer span, and a `text` field which is the answer text.

### Data Splits

The dataset is composed of a single split of 314,811 examples that we used in a two-stage fine-tuning process (refer to the paper for further details).

## Dataset Creation

### Curation Rationale

This dataset was created to investigate the effects of using synthetic adversarial data generation to improve robustness of state-of-the-art QA models.

### Source Data

#### Initial Data Collection and Normalization

The source passages are from Wikipedia and are the same as those used in [SQuAD v1.1](https://arxiv.org/abs/1606.05250).

#### Who are the source language producers?

The source language produces are Wikipedia editors for the passages, and a BART-Large generative model for the questions.

### Personal and Sensitive Information

No annotator identifying details are provided.

## Considerations for Using the Data

### Social Impact of Dataset

The purpose of this dataset is to help develop better question answering systems.

A system that succeeds at the supported task would be able to provide an accurate extractive answer from a short passage. This dataset is to be seen as a support resource for improve the ability of systems t handle questions that contemporary state-of-the-art models struggle to answer correctly, thus often requiring more complex comprehension abilities than say detecting phrases explicitly mentioned in the passage with high overlap to the question.

It should be noted, however, that the the source passages are both domain-restricted and linguistically specific, and that provided questions and answers do not constitute any particular social application.


### Discussion of Biases

The dataset may exhibit various biases in terms of the source passage selection, selected candidate answers, generated questions, quality re-labelling process, as well as any algorithmic biases that may be exacerbated from the adversarial annotation process used to collect the SQuAD and AdversarialQA data on which the generators were trained.

### Other Known Limitations

N/a

## Additional Information

### Dataset Curators

This dataset was initially created by Max Bartolo, Tristan Thrush, Robin Jia, Sebastian Riedel, Pontus Stenetorp, and Douwe Kiela during work carried out at University College London (UCL) and Facebook AI Research (FAIR).

### Licensing Information

This dataset is distributed under the [MIT License](https://opensource.org/licenses/MIT).

### Citation Information

```
@inproceedings{bartolo-etal-2021-improving,
    title = "Improving Question Answering Model Robustness with Synthetic Adversarial Data Generation",
    author = "Bartolo, Max  and
      Thrush, Tristan  and
      Jia, Robin  and
      Riedel, Sebastian  and
      Stenetorp, Pontus  and
      Kiela, Douwe",
    booktitle = "Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing",
    month = nov,
    year = "2021",
    address = "Online and Punta Cana, Dominican Republic",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.emnlp-main.696",
    doi = "10.18653/v1/2021.emnlp-main.696",
    pages = "8830--8848",
    abstract = "Despite recent progress, state-of-the-art question answering models remain vulnerable to a variety of adversarial attacks. While dynamic adversarial data collection, in which a human annotator tries to write examples that fool a model-in-the-loop, can improve model robustness, this process is expensive which limits the scale of the collected data. In this work, we are the first to use synthetic adversarial data generation to make question answering models more robust to human adversaries. We develop a data generation pipeline that selects source passages, identifies candidate answers, generates questions, then finally filters or re-labels them to improve quality. Using this approach, we amplify a smaller human-written adversarial dataset to a much larger set of synthetic question-answer pairs. By incorporating our synthetic data, we improve the state-of-the-art on the AdversarialQA dataset by 3.7F1 and improve model generalisation on nine of the twelve MRQA datasets. We further conduct a novel human-in-the-loop evaluation and show that our models are considerably more robust to new human-written adversarial examples: crowdworkers can fool our model only 8.8{\%} of the time on average, compared to 17.6{\%} for a model trained without synthetic data.",
}
```
### Contributions

Thanks to [@maxbartolo](https://github.com/maxbartolo) for adding this dataset.

