---
annotations_creators:
- expert-generated
language:
- en
license:
- cc-by-4.0
multilinguality:
- monolingual
task_categories:
- text-classification
task_ids: []
pretty_name: AMPERE
---

# Dataset Card for AMPERE

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
- [Dataset Structure](#dataset-structure)
- [Dataset Creation](#dataset-creation)

## Dataset Description

This dataset is released together with our NAACL 2019 Paper "[`Argument Mining for Understanding Peer Reviews`](https://aclanthology.org/N19-1219/)". If you find our work useful, please cite:

```
@inproceedings{hua-etal-2019-argument,
    title = "Argument Mining for Understanding Peer Reviews",
    author = "Hua, Xinyu  and
      Nikolov, Mitko  and
      Badugu, Nikhil  and
      Wang, Lu",
    booktitle = "Proceedings of the 2019 Conference of the North {A}merican Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers)",
    month = jun,
    year = "2019",
    address = "Minneapolis, Minnesota",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/N19-1219",
    doi = "10.18653/v1/N19-1219",
    pages = "2131--2137",
}
```

This dataset includes 400 scientific peer reviews collected from ICLR 2018 hosted at the Openreview platform. Each review is segmented into multiple propositions. We include the original untokenized text for each proposition. Each proposition is labeled as one of the following types:

- **evaluation**: a proposition that is not objectively verifiable and does not require any action to be performed, such as qualitative judgement and interpretation of the paper, e.g. "The paper shows nice results on a number of small tasks."
- **request**: a proposition that is not objectively verifiable and suggests a course of action to be taken, such as recommendation and suggestion for new experiments, e.g. "I would really like to see how the method performs without this hack."
- **fact**: a proposition that is verifiable with objective evidence, such as mathematical conclusion and common knowledge of the field, e.g. "This work proposes a dynamic weight update scheme."
- **quote**: a quote from the paper or another source, e.g. "The author wrote 'where r is lower bound of feature norm'."
- **reference**: a proposition that refers to an objective evidence, such as URL link and citation, e.g. "see MuseGAN (Dong et al), MidiNet (Yang et al), etc."
- **non-arg**: a non-argumentative discourse unit that does not contribute to the overall agenda of the review, such as greetings, metadata, and clarification questions, e.g. "Aha, now I understand."
 

## Dataset Structure

The dataset is partitioned into train/val/test sets. Each set is uploaded as a jsonl format. Each line contains the following elements:

- `doc_id` (str): a unique id for review document
- `text` (list[str]): a list of segmented propositions
- `labels` (list[str]): a list of labels corresponding to the propositions

An example looks as follows.
```
{
    "doc_id": "H1WORsdlG",
    "text": [
      "This paper addresses the important problem of understanding mathematically how GANs work.",
      "The approach taken here is to look at GAN through the lense of the scattering transform.",
      "Unfortunately the manuscrit submitted is very poorly written.",
      "Introduction and flow of thoughts is really hard to follow.",
      "In method sections, the text jumps from one concept to the next without proper definitions.",
      "Sorry I stopped reading on page 3.",
      "I suggest to rewrite this work before sending it to review.",
      "Among many things: - For citations use citep and not citet to have () at the right places.",
      "- Why does it seems -> Why does it seem etc.",
    ],
    "labels": [
      'fact',
      'fact',
      'evaluation',
      'evaluation',
      'evaluation',
      'evaluation',
      'request',
      'request',
      'request',
    ]
}
```

## Dataset Creation

For human annotators, they will be asked to first read the above definitions and controversial cases carefully. The dataset to be annotated consists of 400 reviews partitioned in 20 batches. Each annotator will follow the following steps for annotation:

- Step 1: Open a review file with a text editor. The unannotated review file contains only one line, please separate it into multiple lines with each line corresponding to one single proposition. Repeat the above actions on all 400 reviews.
- Step 2: Based on the segmented units, label the type for each proposition. Start labeling at the end of each file with the marker "## Labels:". Indicate the line number of the proposition first, then annotate the type, e.g. "1. evaluation" for the first proposition. Repeat the above actions on all 400 reviews.

 A third annotator then resolves the disagreements between the two annotators on both segmentation and proposition type.
