---
language:
- en
paperswithcode_id: conll-2000-1
pretty_name: CoNLL-2000
dataset_info:
  features:
  - name: id
    dtype: string
  - name: tokens
    sequence: string
  - name: pos_tags
    sequence:
      class_label:
        names:
          '0': ''''''
          '1': '#'
          '2': $
          '3': (
          '4': )
          '5': ','
          '6': .
          '7': ':'
          '8': '``'
          '9': CC
          '10': CD
          '11': DT
          '12': EX
          '13': FW
          '14': IN
          '15': JJ
          '16': JJR
          '17': JJS
          '18': MD
          '19': NN
          '20': NNP
          '21': NNPS
          '22': NNS
          '23': PDT
          '24': POS
          '25': PRP
          '26': PRP$
          '27': RB
          '28': RBR
          '29': RBS
          '30': RP
          '31': SYM
          '32': TO
          '33': UH
          '34': VB
          '35': VBD
          '36': VBG
          '37': VBN
          '38': VBP
          '39': VBZ
          '40': WDT
          '41': WP
          '42': WP$
          '43': WRB
  - name: chunk_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-ADJP
          '2': I-ADJP
          '3': B-ADVP
          '4': I-ADVP
          '5': B-CONJP
          '6': I-CONJP
          '7': B-INTJ
          '8': I-INTJ
          '9': B-LST
          '10': I-LST
          '11': B-NP
          '12': I-NP
          '13': B-PP
          '14': I-PP
          '15': B-PRT
          '16': I-PRT
          '17': B-SBAR
          '18': I-SBAR
          '19': B-UCP
          '20': I-UCP
          '21': B-VP
          '22': I-VP
  splits:
  - name: train
    num_bytes: 5356965
    num_examples: 8937
  - name: test
    num_bytes: 1201151
    num_examples: 2013
  download_size: 3481560
  dataset_size: 6558116
---

# Dataset Card for "conll2000"

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

- **Homepage:** [https://www.clips.uantwerpen.be/conll2000/chunking/](https://www.clips.uantwerpen.be/conll2000/chunking/)
- **Repository:** [More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
- **Paper:** [More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
- **Point of Contact:** [More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
- **Size of downloaded dataset files:** 3.32 MB
- **Size of the generated dataset:** 6.25 MB
- **Total amount of disk used:** 9.57 MB

### Dataset Summary

 Text chunking consists of dividing a text in syntactically correlated parts of words. For example, the sentence
 He reckons the current account deficit will narrow to only # 1.8 billion in September . can be divided as follows:
[NP He ] [VP reckons ] [NP the current account deficit ] [VP will narrow ] [PP to ] [NP only # 1.8 billion ]
[PP in ] [NP September ] .

Text chunking is an intermediate step towards full parsing. It was the shared task for CoNLL-2000. Training and test
data for this task is available. This data consists of the same partitions of the Wall Street Journal corpus (WSJ)
as the widely used data for noun phrase chunking: sections 15-18 as training data (211727 tokens) and section 20 as
test data (47377 tokens). The annotation of the data has been derived from the WSJ corpus by a program written by
Sabine Buchholz from Tilburg University, The Netherlands.

### Supported Tasks and Leaderboards

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Languages

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

## Dataset Structure

### Data Instances

#### conll2000

- **Size of downloaded dataset files:** 3.32 MB
- **Size of the generated dataset:** 6.25 MB
- **Total amount of disk used:** 9.57 MB

An example of 'train' looks as follows.
```
This example was too long and was cropped:

{
    "chunk_tags": [11, 13, 11, 12, 21, 22, 22, 22, 22, 11, 12, 12, 17, 11, 12, 13, 11, 0, 1, 13, 11, 11, 0, 21, 22, 22, 11, 12, 12, 13, 11, 12, 12, 11, 12, 12, 0],
    "id": "0",
    "pos_tags": [19, 14, 11, 19, 39, 27, 37, 32, 34, 11, 15, 19, 14, 19, 22, 14, 20, 5, 15, 14, 19, 19, 5, 34, 32, 34, 11, 15, 19, 14, 20, 9, 20, 24, 15, 22, 6],
    "tokens": "[\"Confidence\", \"in\", \"the\", \"pound\", \"is\", \"widely\", \"expected\", \"to\", \"take\", \"another\", \"sharp\", \"dive\", \"if\", \"trade\", \"figur..."
}
```

### Data Fields

The data fields are the same among all splits.

#### conll2000
- `id`: a `string` feature.
- `tokens`: a `list` of `string` features.
- `pos_tags`: a `list` of classification labels, with possible values including `''` (0), `#` (1), `$` (2), `(` (3), `)` (4).
- `chunk_tags`: a `list` of classification labels, with possible values including `O` (0), `B-ADJP` (1), `I-ADJP` (2), `B-ADVP` (3), `I-ADVP` (4).

### Data Splits

|  name   |train|test|
|---------|----:|---:|
|conll2000| 8937|2013|

## Dataset Creation

### Curation Rationale

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

#### Who are the source language producers?

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Annotations

#### Annotation process

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

#### Who are the annotators?

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Personal and Sensitive Information

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Discussion of Biases

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Other Known Limitations

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

## Additional Information

### Dataset Curators

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Licensing Information

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Citation Information

```
@inproceedings{tksbuchholz2000conll,
   author     = "Tjong Kim Sang, Erik F. and Sabine Buchholz",
   title      = "Introduction to the CoNLL-2000 Shared Task: Chunking",
   editor     = "Claire Cardie and Walter Daelemans and Claire
                 Nedellec and Tjong Kim Sang, Erik",
   booktitle  = "Proceedings of CoNLL-2000 and LLL-2000",
   publisher  = "Lisbon, Portugal",
   pages      = "127--132",
   year       = "2000"
}

```


### Contributions

Thanks to [@vblagoje](https://github.com/vblagoje), [@jplu](https://github.com/jplu) for adding this dataset.