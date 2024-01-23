---
license: mit
language:
- en
paperswithcode_id: embedding-data/PAQ_pairs
pretty_name: PAQ_pairs
task_categories:
- sentence-similarity
- paraphrase-mining
task_ids:
- semantic-similarity-classification

---

# Dataset Card for "PAQ_pairs"

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

- **Homepage:** [https://github.com/facebookresearch/PAQ](https://github.com/facebookresearch/PAQ)
- **Repository:** [More Information Needed](https://github.com/facebookresearch/PAQ)
- **Paper:** [More Information Needed](https://github.com/facebookresearch/PAQ)
- **Point of Contact:** [More Information Needed](https://github.com/facebookresearch/PAQ)
- **Size of downloaded dataset files:** 
- **Size of the generated dataset:** 
- **Total amount of disk used:** 21 Bytes

### Dataset Summary

Pairs questions and answers obtained from Wikipedia.

Disclaimer: The team releasing PAQ QA pairs did not upload the dataset to the Hub and did not write a dataset card. 
These steps were done by the Hugging Face team.

### Supported Tasks
- [Sentence Transformers](https://huggingface.co/sentence-transformers) training; useful for semantic search and sentence similarity. 
### Languages
- English.
## Dataset Structure
Each example in the dataset contains pairs of sentences and is formatted as a dictionary with the key "set" and a list with the sentences as "value". The first sentence is a question and the second an answer; thus, both sentences would be similar.

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
dataset = load_dataset("embedding-data/PAQ_pairs")
```
The dataset is loaded as a `DatasetDict` and has the format:
```python
DatasetDict({
    train: Dataset({
        features: ['set'],
        num_rows: 64371441
    })
})
```
Review an example `i` with:

```python
dataset["train"][i]["set"]
```



### Data Instances

[More Information Needed](https://github.com/facebookresearch/PAQ)

### Data Fields

[More Information Needed](https://github.com/facebookresearch/PAQ)

### Data Splits

[More Information Needed](https://github.com/facebookresearch/PAQ)

## Dataset Creation

[More Information Needed](https://github.com/facebookresearch/PAQ)

### Curation Rationale

[More Information Needed](https://github.com/facebookresearch/PAQ)

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed](https://github.com/facebookresearch/PAQ)

#### Who are the source language producers?

[More Information Needed](https://github.com/facebookresearch/PAQ)

### Annotations

#### Annotation process

[More Information Needed](https://github.com/facebookresearch/PAQ)

#### Who are the annotators?

[More Information Needed](https://github.com/facebookresearch/PAQ)

### Personal and Sensitive Information

[More Information Needed](https://github.com/facebookresearch/PAQ)

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed](https://github.com/facebookresearch/PAQ)

### Discussion of Biases

[More Information Needed](https://github.com/facebookresearch/PAQ)

### Other Known Limitations

[More Information Needed](https://github.com/facebookresearch/PAQ)

## Additional Information

### Dataset Curators

[More Information Needed](https://github.com/facebookresearch/PAQ)

### Licensing Information

The PAQ QA-pairs and metadata is licensed under [CC-BY-SA](https://creativecommons.org/licenses/by-sa/3.0/). 
Other data is licensed according to the accompanying license files.

### Citation Information

```
@article{lewis2021paq,
      title={PAQ: 65 Million Probably-Asked Questions and What You Can Do With Them}, 
      author={Patrick Lewis and Yuxiang Wu and Linqing Liu and Pasquale Minervini and Heinrich Küttler and Aleksandra Piktus and Pontus Stenetorp and Sebastian Riedel},
      year={2021},
      eprint={2102.07033},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}

```

### Contributions

Thanks to [@patrick-s-h-lewis](https://github.com/patrick-s-h-lewis) for adding this dataset.

