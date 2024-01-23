---
license: mit
---

# Dataset Card for CICERO

## Description

- **Homepage:** https://declare-lab.net/CICERO/
- **Repository:** https://github.com/declare-lab/CICERO
- **Paper:** https://aclanthology.org/2022.acl-long.344/
- **arXiv:** https://arxiv.org/abs/2203.13926

### Summary

CICERO is a new dataset for dialogue reasoning with contextualized commonsense inference. It contains 53K inferences for five commonsense dimensions – cause, subsequent event, prerequisite, motivation, and emotional reaction collected from 5.6K dialogues. We design several generative and multi-choice answer selection tasks to show the usefulness of CICERO in dialogue reasoning.

### Supported Tasks

Inference generation (NLG) and multi-choice answer selection (QA).

### Languages

The text in the dataset is in English. The associated BCP-47 code is en.

## Dataset Structure

### Data Fields

- **ID:** Dialogue ID with dataset indicator.
- **Dialogue:** Utterances of the dialogue in a list.
- **Target:** Target utterance.
- **Question:** One of the five questions (inference types).
- **Choices:** Five possible answer choices in a list. One of the answers is human written. The other four answers are machine-generated and selected through the Adversarial Filtering (AF) algorithm.
- **Human Written Answer:** Index of the human written answer in a single element list. Index starts from 0.
- **Correct Answers:** List of all correct answers indicated as plausible or speculatively correct by the human annotators. Includes the index of the human written answer.

### Data Instances

An instance of the dataset is as the following:

```
{
    "ID": "daily-dialogue-1291",
    "Dialogue": [
        "A: Hello , is there anything I can do for you ?",
        "B: Yes . I would like to check in .",
        "A: Have you made a reservation ?",
        "B: Yes . I am Belen .",
        "A: So your room number is 201 . Are you a member of our hotel ?",
        "B: No , what's the difference ?",
        "A: Well , we offer a 10 % charge for our members ."
    ],
    "Target": "Well , we offer a 10 % charge for our members .",
    "Question": "What subsequent event happens or could happen following the target?",
    "Choices": [
        "For future discounts at the hotel, the listener takes a credit card at the hotel.",
        "The listener is not enrolled in a hotel membership.",
        "For future discounts at the airport, the listener takes a membership at the airport.",
        "For future discounts at the hotel, the listener takes a membership at the hotel.",
        "The listener doesn't have a membership to the hotel."
    ],
    "Human Written Answer": [
        3
    ],
    "Correct Answers": [
        3
    ]
}
 ```

### Data Splits

The dataset contains 31,418 instances for training, 10,888 instances for validation and 10,898 instances for testing.

## Dataset Creation

### Curation Rationale

The annotation process of CICERO can be found in the paper.

### Source Data

The dialogues in CICERO are collected from three datasets - [DailyDialog](https://arxiv.org/abs/1710.03957), [DREAM](https://arxiv.org/abs/1902.00164), and [MuTual](https://arxiv.org/abs/2004.04494)

## Citation Information

```
@inproceedings{ghosal2022cicero,
  title={CICERO: A Dataset for Contextualized Commonsense Inference in Dialogues},
  author={Ghosal, Deepanway and Shen, Siqi and Majumder, Navonil and Mihalcea, Rada and Poria, Soujanya},
  booktitle={Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  pages={5010--5028},
  year={2022}
}
```
