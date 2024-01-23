---
annotations_creators:
- found
language_creators:
- found
language:
- en
license:
- cc-by-nc-sa-4.0
multilinguality:
- multilingual
pretty_name: stackexchange
size_categories:
- unknown
source_datasets:
- original
task_categories:
- question-answering
task_ids:
- closed-domain-qa
---

# Dataset Card Creation Guide

## Table of Contents
- [Dataset Card Creation Guide](#dataset-card-creation-guide)
  - [Table of Contents](#table-of-contents)
  - [Dataset Description](#dataset-description)
    - [Dataset Summary](#dataset-summary)
    - [Languages](#languages)
  - [Dataset Structure](#dataset-structure)
    - [Data Instances](#data-instances)
    - [Data Fields](#data-fields)
    - [Data Splits](#data-splits)
  - [Dataset Creation](#dataset-creation)
    - [Curation Rationale](#curation-rationale)
    - [Source Data](#source-data)
      - [Initial Data Collection and Normalization](#initial-data-collection-and-normalization)
      - [Who are the source language producers?](#who-are-the-source-language-producers)s
  - [Additional Information](#additional-information)
    - [Licensing Information](#licensing-information)
    - [Citation Information](#citation-information)
    - [Contributions](#contributions)

## Dataset Description

- **Homepage:** [stackexchange](https://archive.org/details/stackexchange)
- **Repository:** [flax-sentence-embeddings](https://github.com/nreimers/flax-sentence-embeddings)

### Dataset Summary

We automatically extracted question and answer (Q&A) pairs from [Stack Exchange](https://stackexchange.com/) network. Stack Exchange gather many Q&A communities across 50 online plateform, including the well known Stack Overflow and other technical sites. 100 millon developpers consult Stack Exchange every month. The dataset is a parallel corpus with each question mapped to the top rated answer. The dataset is split given communities which cover a variety of domains from 3d printing, economics, raspberry pi or emacs. An exhaustive list of all communities is available [here](https://stackexchange.com/sites).

### Languages

Stack Exchange mainly consist of english language (en).

## Dataset Structure

### Data Instances

Each data samples is presented as follow:

```
{'title_body': 'How to determine if 3 points on a 3-D graph are collinear? Let the points $A, B$ and $C$ be $(x_1, y_1, z_1), (x_2, y_2, z_2)$ and $(x_3, y_3, z_3)$ respectively. How do I prove that the 3 points are collinear? What is the formula?',
 'upvoted_answer': 'From $A(x_1,y_1,z_1),B(x_2,y_2,z_2),C(x_3,y_3,z_3)$ we can get their position vectors.\n\n$\\vec{AB}=(x_2-x_1,y_2-y_1,z_2-z_1)$ and $\\vec{AC}=(x_3-x_1,y_3-y_1,z_3-z_1)$.\n\nThen $||\\vec{AB}\\times\\vec{AC}||=0\\implies A,B,C$ collinear.',
 'downvoted_answer': 'If the distance between |AB|+|BC|=|AC| then A,B,C are collinear.'}
```

This particular exampe corresponds to the [following page](https://math.stackexchange.com/questions/947555/how-to-determine-if-3-points-on-a-3-d-graph-are-collinear)

### Data Fields

The fields present in the dataset contain the following informations:

- `title_body`: This is the concatenation of the title and body from the question
- `upvoted_answer`: This is the body from the most upvoted answer
- `downvoted_answer`: This is the body from most downvoted answer
- `title`: This is the title from the question

### Data Splits

We provide three splits for this dataset, which only differs by the structure of the fieds which are retrieved:

- `titlebody_upvoted_downvoted_answer`: Includes title and body from the question as well as most upvoted and downvoted answer.
- `title_answer`: Includes title from the question as well as most upvoted answer.
- `titlebody_answer`: Includes title and body from the question as well as most upvoted answer.


|                            | Number of pairs   |
| -----                      | ------ | 
| `titlebody_upvoted_downvoted_answer`            |    17,083    |
| `title_answer`   |   1,100,953     |
| `titlebody_answer`   |     1,100,953     |

## Dataset Creation

### Curation Rationale

We primary designed this dataset for sentence embeddings training. Indeed sentence embeddings may be trained using a contrastive learning setup for which the model is trained to associate each sentence with its corresponding pair out of multiple proposition. Such models require many examples to be efficient and thus the dataset creation may be tedious. Community networks such as Stack Exchange allow us to build many examples semi-automatically.

### Source Data

The source data are dumps from [Stack Exchange](https://archive.org/details/stackexchange)

#### Initial Data Collection and Normalization

We collected the data from the math community. 

We filtered out questions which title or body length is bellow 20 characters and questions for which body length is above 4096 characters.
When extracting most upvoted answer, we filtered to pairs for which their is at least 100 votes gap between most upvoted and downvoted answers.

#### Who are the source language producers?

Questions and answers are written by the community developpers of Stack Exchange.

## Additional Information

### Licensing Information

Please see the license information at: https://archive.org/details/stackexchange

### Citation Information

```
@misc{StackExchangeDataset,
  author = {Flax Sentence Embeddings Team},
  title = {Stack Exchange question pairs},
  year = {2021},
  howpublished = {https://huggingface.co/datasets/flax-sentence-embeddings/},
}
```


### Contributions

Thanks to the Flax Sentence Embeddings team for adding this dataset.