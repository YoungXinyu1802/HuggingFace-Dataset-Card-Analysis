---
license: mit
language:
- en
paperswithcode_id: embedding-data/simple-wiki
pretty_name: simple-wiki
task_categories:
- sentence-similarity
- paraphrase-mining
task_ids:
- semantic-similarity-classification
---

# Dataset Card for "simple-wiki"

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

- **Homepage:** [https://cs.pomona.edu/~dkauchak/simplification/](https://cs.pomona.edu/~dkauchak/simplification/)
- **Repository:** [More Information Needed](https://cs.pomona.edu/~dkauchak/simplification/)
- **Paper:** [https://aclanthology.org/P11-2117/](https://aclanthology.org/P11-2117/)
- **Point of Contact:** [David Kauchak](dkauchak@cs.pomona.edu)

### Dataset Summary
This dataset contains pairs of equivalent sentences obtained from Wikipedia.

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
This dataset is useful for training Sentence Transformers models. Refer to the following post on how to train models using similar sentences.
### Usage Example
Install the 🤗 Datasets library with `pip install datasets` and load the dataset from the Hub with:
```python
from datasets import load_dataset
dataset = load_dataset("embedding-data/simple-wiki")
```
The dataset is loaded as a `DatasetDict` and has the format:
```python
DatasetDict({
    train: Dataset({
        features: ['set'],
        num_rows: 102225
    })
})
```
Review an example `i` with:
```python
dataset["train"][i]["set"]
```

### Curation Rationale

[More Information Needed](https://cs.pomona.edu/~dkauchak/simplification/)

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed](https://cs.pomona.edu/~dkauchak/simplification/)

#### Who are the source language producers?

[More Information Needed](https://cs.pomona.edu/~dkauchak/simplification/)

### Annotations

#### Annotation process

[More Information Needed](https://cs.pomona.edu/~dkauchak/simplification/)

#### Who are the annotators?

[More Information Needed](https://cs.pomona.edu/~dkauchak/simplification/)

### Personal and Sensitive Information

[More Information Needed](https://cs.pomona.edu/~dkauchak/simplification/)

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed](https://cs.pomona.edu/~dkauchak/simplification/)

### Discussion of Biases

[More Information Needed](https://cs.pomona.edu/~dkauchak/simplification/)

### Other Known Limitations

[More Information Needed](https://cs.pomona.edu/~dkauchak/simplification/)

## Additional Information

### Dataset Curators

[More Information Needed](https://cs.pomona.edu/~dkauchak/simplification/)

### Licensing Information

[More Information Needed](https://cs.pomona.edu/~dkauchak/simplification/)

### Contributions
