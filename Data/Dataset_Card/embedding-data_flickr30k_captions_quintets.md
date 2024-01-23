---
license: mit
language:
- en
paperswithcode_id: embedding-data/flickr30k-captions
pretty_name: flickr30k-captions
---

# Dataset Card for "flickr30k-captions"

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Usage Example](#usage-example)
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

- **Homepage:** [https://shannon.cs.illinois.edu/DenotationGraph/](https://shannon.cs.illinois.edu/DenotationGraph/)
- **Repository:** [More Information Needed](https://shannon.cs.illinois.edu/DenotationGraph/)
- **Paper:** [https://transacl.org/ojs/index.php/tacl/article/view/229/33](https://transacl.org/ojs/index.php/tacl/article/view/229/33)
- **Point of Contact:** [Peter Young](pyoung2@illinois.edu), [Alice Lai](aylai2@illinois.edu), [Micah Hodosh](mhodosh2@illinois.edu), [Julia Hockenmaier](juliahmr@illinois.edu)   

### Dataset Summary

We propose to use the visual denotations of linguistic expressions (i.e. the set of images they describe) to define novel denotational similarity metrics, which we show to be at least as beneficial as distributional similarities for two tasks that require semantic inference. To compute these denotational similarities, we construct a denotation graph, i.e. a subsumption hierarchy over constituents and their denotations, based on a large corpus of 30K images and 150K descriptive captions.

Disclaimer: The team releasing Flickr30k did not upload the dataset to the Hub and did not write a dataset card. These steps were done by the Hugging Face team.

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

dataset = load_dataset("embedding-data/flickr30k-captions")
```
The dataset is loaded as a `DatasetDict` has the format:

```python
DatasetDict({
    train: Dataset({
        features: ['set'],
        num_rows: 31783
    })
})
```

Review an example `i` with:

```python
dataset["train"][i]["set"]
```


### Curation Rationale

[More Information Needed](https://shannon.cs.illinois.edu/DenotationGraph/)

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed](https://shannon.cs.illinois.edu/DenotationGraph/)

#### Who are the source language producers?

[More Information Needed](https://shannon.cs.illinois.edu/DenotationGraph/)

### Annotations

#### Annotation process

[More Information Needed](https://shannon.cs.illinois.edu/DenotationGraph/)

#### Who are the annotators?

[More Information Needed](https://shannon.cs.illinois.edu/DenotationGraph/)

### Personal and Sensitive Information

[More Information Needed](https://shannon.cs.illinois.edu/DenotationGraph/)

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed](https://shannon.cs.illinois.edu/DenotationGraph/)

### Discussion of Biases

[More Information Needed](https://shannon.cs.illinois.edu/DenotationGraph/)

### Other Known Limitations

[More Information Needed](https://shannon.cs.illinois.edu/DenotationGraph/)

## Additional Information

### Dataset Curators

[More Information Needed](https://shannon.cs.illinois.edu/DenotationGraph/)

### Licensing Information

[More Information Needed](https://shannon.cs.illinois.edu/DenotationGraph/)

### Citation Information

[More Information Needed](https://shannon.cs.illinois.edu/DenotationGraph/)

### Contributions

Thanks to [Peter Young](pyoung2@illinois.edu), [Alice Lai](aylai2@illinois.edu), [Micah Hodosh](mhodosh2@illinois.edu), [Julia Hockenmaier](juliahmr@illinois.edu) for adding this dataset.

