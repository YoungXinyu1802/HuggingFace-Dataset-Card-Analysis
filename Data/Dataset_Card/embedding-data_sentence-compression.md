---
license: mit
language:
- en
paperswithcode_id: embedding-data/sentence-compression
pretty_name: sentence-compression
task_categories:
- sentence-similarity
- paraphrase-mining
task_ids:
- semantic-similarity-classification
---

# Dataset Card for "sentence-compression"

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

- **Homepage:** [https://github.com/google-research-datasets/sentence-compression](https://github.com/google-research-datasets/sentence-compression)
- **Repository:** [More Information Needed](https://github.com/google-research-datasets/sentence-compression)
- **Paper:** [More Information Needed](https://www.aclweb.org/anthology/D13-1155/)
- **Point of Contact:** [Katja Filippova](altun@google.com)
- **Size of downloaded dataset files:** 
- **Size of the generated dataset:** 
- **Total amount of disk used:** 14.2 MB

### Dataset Summary
Dataset with pairs of equivalent sentences.
The dataset is provided "AS IS" without any warranty, express or implied. 
Google disclaims all liability for any damages, direct or indirect, resulting from using the dataset.

Disclaimer: The team releasing sentence-compression did not upload the dataset to the Hub and did not write a dataset card. These steps were done by the Hugging Face team.

### Supported Tasks
- [Sentence Transformers](https://huggingface.co/sentence-transformers) training; useful for semantic search and sentence similarity. 
### Languages
- English.
## Dataset Structure
Each example in the dataset contains pairs of equivalent sentences and is formatted as a dictionary with the key "set" and a list with the sentences as "value".
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
dataset = load_dataset("embedding-data/sentence-compression")
```
The dataset is loaded as a `DatasetDict` and has the format:
```python
DatasetDict({
    train: Dataset({
        features: ['set'],
        num_rows: 180000
    })
})
```
Review an example `i` with:
```python
dataset["train"][i]["set"]
```

### Curation Rationale

[More Information Needed](https://github.com/google-research-datasets/sentence-compression)

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed](https://github.com/google-research-datasets/sentence-compression)

#### Who are the source language producers?

[More Information Needed](https://github.com/google-research-datasets/sentence-compression)

### Annotations

#### Annotation process

[More Information Needed](https://github.com/google-research-datasets/sentence-compression)

#### Who are the annotators?

[More Information Needed](https://github.com/google-research-datasets/sentence-compression)

### Personal and Sensitive Information

[More Information Needed](https://github.com/google-research-datasets/sentence-compression)

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed](https://github.com/google-research-datasets/sentence-compression)

### Discussion of Biases

[More Information Needed](https://github.com/google-research-datasets/sentence-compression)

### Other Known Limitations

[More Information Needed](https://github.com/google-research-datasets/sentence-compression)

## Additional Information

### Dataset Curators

[More Information Needed](https://github.com/google-research-datasets/sentence-compression)

### Licensing Information

[More Information Needed](https://github.com/google-research-datasets/sentence-compression)

### Contributions




