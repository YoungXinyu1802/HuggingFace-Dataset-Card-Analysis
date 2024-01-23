---
license: cc-by-nc-4.0
task_categories:
- token-classification
language:
- en
pretty_name: FiNER
size_categories:
- 1K<n<10K
multilinguality:
- monolingual
task_ids:
- named-entity-recognition
---

# Dataset Card for "FiNER-ORD"

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation and Annotation](#dataset-creation)
- [Additional Information](#additional-information)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contact Information](#contact-information)

## Dataset Description

- **Homepage:** [https://github.com/gtfintechlab/FiNER](https://github.com/gtfintechlab/FiNER)
- **Repository:** [https://github.com/gtfintechlab/FiNER](https://github.com/gtfintechlab/FiNER)
- **Paper:** [Arxiv Link]()
- **Point of Contact:** [Agam A. Shah](https://shahagam4.github.io/)
- **Size of train dataset file:** 1.08 MB
- **Size of validation dataset file:** 135 KB  
- **Size of test dataset file:** 336 KB  

### Dataset Summary

The FiNER-Open Research Dataset (FiNER-ORD) consists of a manually annotated dataset of financial news articles (in English)
collected from [webz.io] (https://webz.io/free-datasets/financial-news-articles/).
In total, there are 47851 news articles available in this data at the point of writing this paper. 
Each news article is available in the form of a JSON document with various metadata information like
the source of the article, publication date, author of the article, and the title of the article. 
For the manual annotation of named entities in financial news, we randomly sampled 220 documents from the entire set of news articles. 
We observed that some articles were empty in our sample, so after filtering the empty documents, we were left with a total of 201 articles.  
We use [Doccano](https://github.com/doccano/doccano), an open-source annotation tool,
to ingest the raw dataset and manually label person (PER), location (LOC), and organization (ORG) entities.
For our experiments, we use the manually labeled FiNER-ORD to benchmark model performance. 
Thus, we make a train, validation, and test split of FiNER-ORD. 
To avoid biased results, manual annotation is performed by annotators who have no knowledge about the labeling functions for the weak supervision framework. 
The train and validation sets are annotated by two separate annotators and validated by a third annotator. 
The test dataset is annotated by another annotator. We present a manual annotation guide in the Appendix of the paper detailing the procedures used to create the manually annotated FiNER-ORD. 

After manual annotation, the news articles are split into sentences. 
We then tokenize each sentence, employing a script to tokenize multi-token entities into separate tokens (e.g. PER_B denotes the beginning token of a person (PER) entity
and PER_I represents intermediate PER tokens). We exclude white spaces when tokenizing multi-token entities.
The descriptive statistics on the resulting FiNER-ORD are available in the Table of [Data Splits](#data-splits) section.

For more details check [information in paper]()

### Supported Tasks and Leaderboards

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Languages

- It is a monolingual English dataset

## Dataset Structure

### Data Instances

#### FiNER-ORD

- **Size of train dataset file:** 1.08 MB
- **Size of validation dataset file:** 135 KB  
- **Size of test dataset file:** 336 KB   

### Data Fields

The data fields are the same among all splits.

#### conll2003
- `doc_idx`: Document ID (`int`)
- `sent_idx`: Sentence ID within each document (`int`)
- `gold_token`: Token (`string`)
- `gold_label`: a `list` of classification labels (`int`). Full tagset with indices:

```python
{'O': 0, 'PER_B': 1, 'PER_I': 2, 'LOC_B': 3, 'LOC_I': 4, 'ORG_B': 5, 'ORG_I': 6}
```

### Data Splits

| **FiNER-ORD** | **Train** | **Validation** | **Test** |
|------------------|----------------|---------------------|---------------|
| # Articles      | 135            | 24                  | 42            |
| # Tokens        | 80,531         | 10,233              | 25,957        |
| # LOC entities  | 1,255          | 267                 | 428           |
| # ORG entities  | 3,440          | 524                 | 933           |
| # PER entities  | 1,374          | 222                 | 466           |


## Dataset Creation and Annotation


[Information in paper ]()


## Additional Information


### Licensing Information

[Information in paper ]()

### Citation Information

```
@article{shah2023finer,
  title={FiNER: Financial Named Entity Recognition Dataset and Weak-supervision Model},
  author={Agam Shah and Ruchit Vithani and Abhinav Gullapalli and Sudheer Chava},
  journal={arXiv preprint arXiv:2302.11157},
  year={2023}
}

```


### Contact Information

Please contact Agam Shah (ashah482[at]gatech[dot]edu) or Ruchit Vithani (rvithani6[at]gatech[dot]edu) about any FiNER-related issues and questions.  
GitHub: [@shahagam4](https://github.com/shahagam4), [@ruchit2801](https://github.com/ruchit2801)
Website: [https://shahagam4.github.io/](https://shahagam4.github.io/)


