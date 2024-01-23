---
annotations_creators:
- expert-generated
language_creators:
- found
language:
- en
license: []
multilinguality:
- monolingual
size_categories:
- unknown
source_datasets:
- original
task_categories:
- token-classification
task_ids:
- parsing
pretty_name: Scientific Dependency Tree Bank
language_bcp47:
- en-US
---

# Dataset Card for SciDTB

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-instances)
  - [Data Splits](#data-instances)
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

## Dataset Description

- **Homepage:** https://github.com/PKU-TANGENT/SciDTB
- **Repository:** https://github.com/PKU-TANGENT/SciDTB
- **Paper:** https://aclanthology.org/P18-2071/
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [Needs More Information]

### Dataset Summary

SciDTB is a domain-specific discourse treebank annotated on scientific articles written in English-language. Different from widely-used RST-DT and PDTB, SciDTB uses dependency trees to represent discourse structure, which is flexible and simplified to some extent but do not sacrifice structural integrity. Furthermore, this treebank is made as a benchmark for evaluating discourse dependency parsers. This dataset can benefit many downstream NLP tasks such as machine translation and automatic summarization. 

### Supported Tasks and Leaderboards

[Needs More Information]

### Languages

English.

## Dataset Structure

### Data Instances

A typical data point consist of `root` which is a list of nodes in dependency tree. Each node in the list has four fields: `id` containing id for the node, `parent` contains id of the parent node, `text` refers to the span that is part of the current node and finally `relation` represents relation between current node and parent node.

An example from SciDTB train set is given below:  

```
{
	"root": [
		{
			"id": 0,
			"parent": -1,
			"text": "ROOT",
			"relation": "null"
		},
		{
			"id": 1,
			"parent": 0,
			"text": "We propose a neural network approach ",
			"relation": "ROOT"
		},
		{
			"id": 2,
			"parent": 1,
			"text": "to benefit from the non-linearity of corpus-wide statistics for part-of-speech ( POS ) tagging . <S>",
			"relation": "enablement"
		},
		{
			"id": 3,
			"parent": 1,
			"text": "We investigated several types of corpus-wide information for the words , such as word embeddings and POS tag distributions . <S>",
			"relation": "elab-aspect"
		},
		{
			"id": 4,
			"parent": 5,
			"text": "Since these statistics are encoded as dense continuous features , ",
			"relation": "cause"
		},
		{
			"id": 5,
			"parent": 3,
			"text": "it is not trivial to combine these features ",
			"relation": "elab-addition"
		},
		{
			"id": 6,
			"parent": 5,
			"text": "comparing with sparse discrete features . <S>",
			"relation": "comparison"
		},
		{
			"id": 7,
			"parent": 1,
			"text": "Our tagger is designed as a combination of a linear model for discrete features and a feed-forward neural network ",
			"relation": "elab-aspect"
		},
		{
			"id": 8,
			"parent": 7,
			"text": "that captures the non-linear interactions among the continuous features . <S>",
			"relation": "elab-addition"
		},
		{
			"id": 9,
			"parent": 10,
			"text": "By using several recent advances in the activation functions for neural networks , ",
			"relation": "manner-means"
		},
		{
			"id": 10,
			"parent": 1,
			"text": "the proposed method marks new state-of-the-art accuracies for English POS tagging tasks . <S>",
			"relation": "evaluation"
		}
	]
}
```

More such raw data instance can be found [here](https://github.com/PKU-TANGENT/SciDTB/tree/master/dataset)

### Data Fields

- id: an integer identifier for the node
- parent: an integer identifier for the parent node
- text: a string containing text for the current node
- relation: a string representing discourse relation between current node and parent node

### Data Splits

Dataset consists of three splits: `train`, `dev` and  `test`.  

| Train   | Valid | Test |
| ------ | ----- | ---- |
| 743 |  154 | 152|


## Dataset Creation

### Curation Rationale

[Needs More Information]

### Source Data

#### Initial Data Collection and Normalization

[Needs More Information]

#### Who are the source language producers?

[Needs More Information]

### Annotations

#### Annotation process

More information can be found [here](https://aclanthology.org/P18-2071/)

#### Who are the annotators?

[Needs More Information]

### Personal and Sensitive Information

[Needs More Information]

## Considerations for Using the Data

### Social Impact of Dataset

[Needs More Information]

### Discussion of Biases

[Needs More Information]

### Other Known Limitations

[Needs More Information]

## Additional Information

### Dataset Curators

[Needs More Information]

### Licensing Information

[Needs More Information]

### Citation Information

```
@inproceedings{yang-li-2018-scidtb,
    title = "{S}ci{DTB}: Discourse Dependency {T}ree{B}ank for Scientific Abstracts",
    author = "Yang, An  and
      Li, Sujian",
    booktitle = "Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)",
    month = jul,
    year = "2018",
    address = "Melbourne, Australia",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/P18-2071",
    doi = "10.18653/v1/P18-2071",
    pages = "444--449",
    abstract = "Annotation corpus for discourse relations benefits NLP tasks such as machine translation and question answering. In this paper, we present SciDTB, a domain-specific discourse treebank annotated on scientific articles. Different from widely-used RST-DT and PDTB, SciDTB uses dependency trees to represent discourse structure, which is flexible and simplified to some extent but do not sacrifice structural integrity. We discuss the labeling framework, annotation workflow and some statistics about SciDTB. Furthermore, our treebank is made as a benchmark for evaluating discourse dependency parsers, on which we provide several baselines as fundamental work.",
}
```