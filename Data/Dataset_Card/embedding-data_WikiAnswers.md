---
license: mit
language:
- en
paperswithcode_id: embedding-data/WikiAnswers
pretty_name: WikiAnswers
task_categories:
- sentence-similarity
- paraphrase-mining
task_ids:
- semantic-similarity-classification
---

# Dataset Card for "WikiAnswers"

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

- **Homepage:** [https://github.com/afader/oqa#wikianswers-corpus](https://github.com/afader/oqa#wikianswers-corpus)
- **Repository:** [More Information Needed](https://github.com/afader/oqa#wikianswers-corpus)
- **Paper:** [More Information Needed](https://doi.org/10.1145/2623330.2623677)
- **Point of Contact:** [Anthony Fader](https://dl.acm.org/profile/81324489111), [Luke Zettlemoyer](https://dl.acm.org/profile/81100527621), [Oren Etzioni](https://dl.acm.org/profile/99658633129)

### Dataset Summary
The WikiAnswers corpus contains clusters of questions tagged by WikiAnswers users as paraphrases. 
Each cluster optionally contains an answer provided by WikiAnswers users. There are 30,370,994 clusters containing an average of 25 questions per cluster. 3,386,256 (11%) of the clusters have an answer.

### Supported Tasks
- [Sentence Transformers](https://huggingface.co/sentence-transformers) training; useful for semantic search and sentence similarity. 
### Languages
- English.
## Dataset Structure
Each example in the dataset contains 25 equivalent sentences and is formatted as a dictionary with the key "set" and a list with the sentences as "value".
```
{"set": [sentence_1, sentence_2, ..., sentence_25]}
{"set": [sentence_1, sentence_2, ..., sentence_25]}
...
{"set": [sentence_1, sentence_2, ..., sentence_25]}
```
This dataset is useful for training Sentence Transformers models. Refer to the following post on how to train models using similar sentences.
### Usage Example
Install the 🤗 Datasets library with `pip install datasets` and load the dataset from the Hub with:
```python
from datasets import load_dataset
dataset = load_dataset("embedding-data/WikiAnswers")
```
The dataset is loaded as a `DatasetDict` and has the format for `N` examples:
```python
DatasetDict({
    train: Dataset({
        features: ['set'],
        num_rows: N
    })
})
```
Review an example `i` with:
```python
dataset["train"][i]["set"]
```

### Data Instances

### Data Fields

### Data Splits


## Dataset Creation

### Curation Rationale

[More Information Needed](https://github.com/afader/oqa#wikianswers-corpus)

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed](https://github.com/afader/oqa#wikianswers-corpus)

#### Who are the source language producers?

[More Information Needed](https://github.com/afader/oqa#wikianswers-corpus)

### Annotations

#### Annotation process

[More Information Needed](https://github.com/afader/oqa#wikianswers-corpus)

#### Who are the annotators?

[More Information Needed](https://github.com/afader/oqa#wikianswers-corpus)

### Personal and Sensitive Information

[More Information Needed](https://github.com/afader/oqa#wikianswers-corpus)

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed](https://github.com/afader/oqa#wikianswers-corpus)

### Discussion of Biases

[More Information Needed](https://github.com/afader/oqa#wikianswers-corpus)

### Other Known Limitations

[More Information Needed](https://github.com/afader/oqa#wikianswers-corpus)

## Additional Information

### Dataset Curators

[More Information Needed](https://github.com/afader/oqa#wikianswers-corpus)

### Licensing Information

[More Information Needed](https://github.com/afader/oqa#wikianswers-corpus)

### Citation Information

```
@inproceedings{Fader14,
    author    = {Anthony Fader and Luke Zettlemoyer and Oren Etzioni},
    title     = {{Open Question Answering Over Curated and Extracted
                Knowledge Bases}},
    booktitle = {KDD},
    year      = {2014}
}
```


### Contributions


