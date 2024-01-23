---
license: mit
language:
- en
paperswithcode_id: embedding-data/coco_captions
pretty_name: coco_captions
task_categories:
- sentence-similarity
- paraphrase-mining
task_ids:
- semantic-similarity-classification

---

# Dataset Card for "coco_captions"

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
- **Homepage:** [https://cocodataset.org/#home](https://cocodataset.org/#home)
- **Repository:** [https://github.com/cocodataset/cocodataset.github.io](https://github.com/cocodataset/cocodataset.github.io)
- **Paper:** [More Information Needed](https://arxiv.org/abs/1405.0312)
- **Point of Contact:** [info@cocodataset.org](info@cocodataset.org)
- **Size of downloaded dataset files:** 
- **Size of the generated dataset:** 
- **Total amount of disk used:** 6.32 MB

### Dataset Summary

COCO is a large-scale object detection, segmentation, and captioning dataset. This repo contains five captions per image; useful for sentence similarity tasks.

Disclaimer: The team releasing COCO did not upload the dataset to the Hub and did not write a dataset card. 
These steps were done by the Hugging Face team.

### Supported Tasks

- [Sentence Transformers](https://huggingface.co/sentence-transformers) training; useful for semantic search and sentence similarity. 

### Languages

- English.

## Dataset Structure

Each example in the dataset contains quintets of similar sentences and is formatted as a dictionary with the key "set" and a list with the sentences as "value":

```
{"set": [sentence_1, sentence_2, sentence3, sentence4, sentence5]}
{"set": [sentence_1, sentence_2, sentence3, sentence4, sentence5]}
...
{"set": [sentence_1, sentence_2, sentence3, sentence4, sentence5]}
```

This dataset is useful for training Sentence Transformers models. Refer to the following post on how to train models using similar pairs of sentences.

### Usage Example

Install the 🤗 Datasets library with `pip install datasets` and load the dataset from the Hub with:

```python
from datasets import load_dataset
dataset = load_dataset("embedding-data/coco_captions")
```
The dataset is loaded as a `DatasetDict` and has the format:

```python
DatasetDict({
    train: Dataset({
        features: ['set'],
        num_rows: 82783
    })
})
```

Review an example `i` with:

```python
dataset["train"][i]["set"]
```


### Data Instances

[More Information Needed](https://cocodataset.org/#format-data)

### Data Splits

[More Information Needed](https://cocodataset.org/#format-data)

## Dataset Creation

### Curation Rationale

[More Information Needed](https://cocodataset.org/#home)

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed](https://cocodataset.org/#home)

#### Who are the source language producers?

[More Information Needed](https://cocodataset.org/#home)

### Annotations

#### Annotation process

[More Information Needed](https://cocodataset.org/#home)

#### Who are the annotators?

[More Information Needed](https://cocodataset.org/#home)

### Personal and Sensitive Information

[More Information Needed](https://cocodataset.org/#home)

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed](https://cocodataset.org/#home)

### Discussion of Biases

[More Information Needed](https://cocodataset.org/#home)

### Other Known Limitations

[More Information Needed](https://cocodataset.org/#home)

## Additional Information

### Dataset Curators

[More Information Needed](https://cocodataset.org/#home)

### Licensing Information

The annotations in this dataset along with this website belong to the COCO Consortium 
and are licensed under a [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/legalcode)

### Citation Information

[More Information Needed](https://cocodataset.org/#home)

### Contributions

Thanks to:

- Tsung-Yi Lin - Google Brain
- Genevieve Patterson - MSR, Trash TV
- Matteo R. - Ronchi Caltech
- Yin Cui - Google
- Michael Maire - TTI-Chicago
- Serge Belongie - Cornell Tech
- Lubomir Bourdev - WaveOne, Inc.
- Ross Girshick - FAIR
- James Hays - Georgia Tech
- Pietro Perona - Caltech
- Deva Ramanan - CMU
- Larry Zitnick - FAIR
- Piotr Dollár - FAIR

for adding this dataset.
