---
language: 
- om
- am
- rw
- rn
- ha
- ig
- pcm
- so
- sw
- ti
- yo
- multilingual
    
license: apache-2.0

task_categories:
- text-generation
task_ids:
- language-modeling
---

# Dataset Card for AfriBERTa's Corpus

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
  - [Loading Dataset](#loading-dataset)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Discussion of Biases](#discussion-of-biases)
- [Additional Information](#additional-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

### Dataset Summary
This is the corpus on which AfriBERTa was trained on.
The dataset is mostly from the BBC news website, but some languages also have data from Common Crawl. 

- **Homepage:** https://github.com/keleog/afriberta
- **Models:** 
    - https://huggingface.co/castorini/afriberta_small
    - https://huggingface.co/castorini/afriberta_base
    - https://huggingface.co/castorini/afriberta_large
- **Paper:** https://aclanthology.org/2021.mrl-1.11/
- **Point of Contact:** kelechi.ogueji@uwaterloo.ca


### Supported Tasks and Leaderboards
The AfriBERTa corpus was mostly intended to pre-train language models.

### Languages
```
afaanoromoo
amharic
gahuza
hausa
igbo
pidgin
somali
swahili
tigrinya
yoruba
```
### Loading Dataset
An example to load the train split of the Somali corpus:
```
dataset = load_dataset("castorini/afriberta-corpus", "somali", split="train")
```

An example to load the test split of the Pidgin corpus:
```
dataset = load_dataset("castorini/afriberta-corpus", "pidgin", split="test")
```

## Dataset Structure

### Data Instances
Each data point is a line of text. 
An example from the `igbo` dataset:
```
{"id": "6", "text": "Ngwá ọrụ na-echebe ma na-ebuli gị na kọmputa."}
```

### Data Fields

The data fields are:

- id: id of the example
- text: content as a string

### Data Splits
Each language has a train and test split, with varying sizes. 

## Considerations for Using the Data

### Discussion of Biases
Since majority of the data is obtained from the BBC's news website, models trained on this dataset are likely going to 
be biased towards the news domain.

Also, since some of the data is obtained from Common Crawl, care should be taken (especially for text generation models) since personal and sensitive information might be present.

## Additional Information
### Citation Information
```
@inproceedings{ogueji-etal-2021-small,
    title = "Small Data? No Problem! Exploring the Viability of Pretrained Multilingual Language Models for Low-resourced Languages",
    author = "Ogueji, Kelechi  and
      Zhu, Yuxin  and
      Lin, Jimmy",
    booktitle = "Proceedings of the 1st Workshop on Multilingual Representation Learning",
    month = nov,
    year = "2021",
    address = "Punta Cana, Dominican Republic",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.mrl-1.11",
    pages = "116--126",
}
```

### Contributions
Thanks to [Kelechi Ogueji](https://github.com/keleog) for adding this dataset.