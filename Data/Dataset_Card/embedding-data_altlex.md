---
license: mit
language:
- en
paperswithcode_id: embedding-data/altlex
pretty_name: altlex
---

# Dataset Card for "altlex"

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

- **Homepage:** [https://github.com/chridey/altlex](https://github.com/chridey/altlex)
- **Repository:** [More Information Needed](https://github.com/chridey/altlex)
- **Paper:** [https://aclanthology.org/P16-1135.pdf](https://aclanthology.org/P16-1135.pdf)
- **Point of Contact:** [Christopher Hidey](ch3085@columbia.edu)

### Dataset Summary

Git repository for software associated with the 2016 ACL paper "Identifying Causal Relations Using Parallel Wikipedia Articles."

Disclaimer: The team releasing altlex did not upload the dataset to the Hub and did not write a dataset card.
These steps were done by the Hugging Face team.

### Supported Tasks

- [Sentence Transformers](https://huggingface.co/sentence-transformers) training; useful for semantic search and sentence similarity. 

### Languages

- English.

## Dataset Structure

Each example in the dataset contains a pair of similar sentences and is formatted as a dictionary with the key "set" and a list with the sentences as "value":

```
{"set": [sentence_1, sentence_2]}
{"set": [sentence_1, sentence_2]}
...
{"set": [sentence_1, sentence_2]}
```

This dataset is useful for training Sentence Transformers models. Refer to the following post on how to train models using similar pairs of sentences.

### Usage Example

Install the 🤗 Datasets library with `pip install datasets` and load the dataset from the Hub with:

```python
from datasets import load_dataset
dataset = load_dataset("embedding-data/altlex")
```
The dataset is loaded as a `DatasetDict` and has the format:

```python
DatasetDict({
    train: Dataset({
        features: ['set'],
        num_rows: 112696
    })
})
```

Review an example `i` with:

```python
dataset["train"][i]["set"]
```


### Source Data

#### Initial Data Collection and Normalization

[More Information Needed](https://github.com/chridey/altlex)

#### Who are the source language producers?

[More Information Needed](https://github.com/chridey/altlex)

### Annotations

#### Annotation process

[More Information Needed](https://github.com/chridey/altlex)

#### Who are the annotators?

[More Information Needed](https://github.com/chridey/altlex)

### Personal and Sensitive Information

[More Information Needed](https://github.com/chridey/altlex)

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed](https://github.com/chridey/altlex)

### Discussion of Biases

[More Information Needed](https://github.com/chridey/altlex)

### Other Known Limitations

[More Information Needed](https://github.com/chridey/altlex)

## Additional Information

### Dataset Curators

[More Information Needed](https://github.com/chridey/altlex)

### Licensing Information

[More Information Needed](https://github.com/chridey/altlex)

### Citation Information

### Contributions

- [@chridey](https://github.com/chridey/altlex/commits?author=chridey) for adding this dataset to Github.

---
