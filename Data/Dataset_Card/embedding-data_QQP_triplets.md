---
license: mit
language:
- en
paperswithcode_id: embedding-data/QQP_triplets
pretty_name: QQP_triplets
task_categories:
- sentence-similarity
- paraphrase-mining
task_ids:
- semantic-similarity-classification

---

# Dataset Card for "QQP_triplets"

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

- **Homepage:** [https://quoradata.quora.com/First-Quora-Dataset-Release-Question-Pairs](https://quoradata.quora.com/First-Quora-Dataset-Release-Question-Pairs)
- **Repository:** [More Information Needed](http://qim.fs.quoracdn.net/quora_duplicate_questions.tsv)
- **Paper:** [More Information Needed](https://quoradata.quora.com/First-Quora-Dataset-Release-Question-Pairs)
- **Point of Contact:** [Kornél Csernai](https://www.quora.com/profile/Korn%C3%A9l-Csernai), [Nikhil Dandekar](https://www.quora.com/profile/Nikhil-Dandekar), [Shankar Iyer](https://www.quora.com/profile/Shankar-Iyer-5)

### Dataset Summary

This dataset will give anyone the opportunity to train and test models of semantic equivalence, based on actual Quora data. The data is organized as triplets (anchor, positive, negative).

Disclaimer: The team releasing Quora data did not upload the dataset to the Hub and did not write a dataset card. 
These steps were done by the Hugging Face team.

### Supported Tasks
- [Sentence Transformers](https://huggingface.co/sentence-transformers) training; useful for semantic search and sentence similarity. 

### Languages
- English.

## Dataset Structure
Each example is a dictionary with three keys (query, pos, and neg) containing a list each (triplets). The first key contains an anchor sentence, the second a positive sentence, and the third a list of negative sentences. 
```
{"query": [anchor], "pos": [positive], "neg": [negative1, negative2, ..., negativeN]}
{"query": [anchor], "pos": [positive], "neg": [negative1, negative2, ..., negativeN]}
...
{"query": [anchor], "pos": [positive], "neg": [negative1, negative2, ..., negativeN]}
```
This dataset is useful for training Sentence Transformers models. Refer to the following post on how to train them.

### Usage Example
Install the 🤗 Datasets library with `pip install datasets` and load the dataset from the Hub with:
```python
from datasets import load_dataset
dataset = load_dataset("embedding-data/QQP_triplets")
```
The dataset is loaded as a `DatasetDict` and has the format:
```python
DatasetDict({
    train: Dataset({
        features: ['set'],
        num_rows: 101762
    })
})
```
Review an example `i` with:
```python
dataset["train"][i]["set"]
```

### Curation Rationale

[More Information Needed](https://quoradata.quora.com/First-Quora-Dataset-Release-Question-Pairs)

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed](https://quoradata.quora.com/First-Quora-Dataset-Release-Question-Pairs)

#### Who are the source language producers?

[More Information Needed](https://quoradata.quora.com/First-Quora-Dataset-Release-Question-Pairs)

### Annotations

#### Annotation process

[More Information Needed](https://quoradata.quora.com/First-Quora-Dataset-Release-Question-Pairs)

#### Who are the annotators?

[More Information Needed](https://quoradata.quora.com/First-Quora-Dataset-Release-Question-Pairs)

### Personal and Sensitive Information

[More Information Needed](https://quoradata.quora.com/First-Quora-Dataset-Release-Question-Pairs)

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed](https://quoradata.quora.com/First-Quora-Dataset-Release-Question-Pairs)

### Discussion of Biases

[More Information Needed](https://quoradata.quora.com/First-Quora-Dataset-Release-Question-Pairs)

### Other Known Limitations

Here are a few important things to keep in mind about this dataset:

- Our original sampling method returned an imbalanced dataset with many more true examples of duplicate pairs than non-duplicates. 
Therefore, we supplemented the dataset with negative examples. 
- One source of negative examples were pairs of “related questions” which, although pertaining to similar topics, 
are not truly semantically equivalent.
- The distribution of questions in the dataset should not be taken to be representative of the distribution of questions asked on Quora. This is, in part, because of the combination of sampling procedures and also due to some sanitization measures that
have been applied to the final dataset (e.g., removal of questions with extremely long question details).
- The ground-truth labels contain some amount of noise: they are not guaranteed to be perfect.

## Additional Information

### Dataset Curators

[More Information Needed](https://quoradata.quora.com/First-Quora-Dataset-Release-Question-Pairs)

### Licensing Information

[More Information Needed](https://quoradata.quora.com/First-Quora-Dataset-Release-Question-Pairs)

### Citation Information

[More Information Needed](https://quoradata.quora.com/First-Quora-Dataset-Release-Question-Pairs)

### Contributions

Thanks to [Kornél Csernai](https://www.quora.com/profile/Korn%C3%A9l-Csernai), [Nikhil Dandekar](https://www.quora.com/profile/Nikhil-Dandekar), [Shankar Iyer](https://www.quora.com/profile/Shankar-Iyer-5) for adding this dataset.

