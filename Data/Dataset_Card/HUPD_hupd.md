---
language:
- en
license:
- cc-by-sa-4.0
task_categories:
- fill-mask
- summarization
- text-classification
- token-classification
task_ids:
- masked-language-modeling
- multi-class-classification
- topic-classification
- named-entity-recognition
pretty_name: "HUPD"
tags:
- patents
---

# Dataset Card for The Harvard USPTO Patent Dataset (HUPD)

![HUPD-Diagram](https://huggingface.co/datasets/HUPD/hupd/resolve/main/HUPD-Logo.png)


## Dataset Description

- **Homepage:** [https://patentdataset.org/](https://patentdataset.org/)
- **Repository:** [HUPD GitHub repository](https://github.com/suzgunmirac/hupd)
- **Paper:** [HUPD arXiv Submission](https://arxiv.org/abs/2207.04043)
- **Point of Contact:** Mirac Suzgun

### Dataset Summary

The Harvard USPTO Dataset (HUPD) is a large-scale, well-structured, and multi-purpose corpus of English-language utility patent applications filed to the United States Patent and Trademark Office (USPTO) between January 2004 and December 2018.


### Experiments and Tasks Considered in the Paper

- **Patent Acceptance Prediction**: Given a section of a patent application (in particular, the abstract, claims, or description), predict whether the application will be accepted by the USPTO.
- **Automated Subject (IPC/CPC) Classification**: Predict the primary IPC or CPC code of a patent application given (some subset of) the text of the application.
- **Language Modeling**: Masked/autoregressive language modeling on the claims and description sections of patent applications.
- **Abstractive Summarization**: Given the claims or claims section of a patent application, generate the abstract. 

### Languages

The dataset contains English text only. 

### Domain
Patents (intellectual property).

### Dataset Curators
The dataset was created by Mirac Suzgun, Luke Melas-Kyriazi, Suproteem K. Sarkar, Scott Duke Kominers, and Stuart M. Shieber. 

## Dataset Structure

Each patent application is defined by a distinct JSON file, named after its application number, and includes information about 
the application and publication numbers, 
title, 
decision status, 
filing and publication dates, 
primary and secondary classification codes, 
inventor(s), 
examiner,
attorney,
abstract, 
claims, 
background, 
summary, and 
full description of the proposed invention, among other fields. There are also supplementary variables, such as the small-entity indicator (which denotes whether the applicant is considered to be a small entity by the USPTO) and the foreign-filing indicator (which denotes whether the application was originally filed in a foreign country).

In total, there are 34 data fields for each application. A full list of data fields used in the dataset is listed in the next section.

### Data Instances

Each patent application in our patent dataset is defined by a distinct JSON file (e.g., ``8914308.json``), named after its unique application number. The format of the JSON files is as follows:


```python
{
    "application_number": "...",
    "publication_number": "...",
    "title": "...",
    "decision": "...",
    "date_produced": "...",
    "date_published": "...",
    "main_cpc_label": "...",
    "cpc_labels": ["...", "...", "..."],
    "main_ipcr_label": "...",
    "ipcr_labels": ["...", "...", "..."],
    "patent_number": "...",
    "filing_date": "...",
    "patent_issue_date": "...",
    "abandon_date": "...",
    "uspc_class": "...",
    "uspc_subclass": "...",
    "examiner_id": "...",
    "examiner_name_last": "...",
    "examiner_name_first": "...",
    "examiner_name_middle": "...",
    "inventor_list": [
        {
            "inventor_name_last": "...",
            "inventor_name_first": "...",
            "inventor_city": "...",
            "inventor_state": "...",
            "inventor_country": "..."
        }
    ],
    "abstract": "...",
    "claims": "...",
    "background": "...",
    "summary": "...",
    "full_description": "..."
}
```

## Usage
### Loading the Dataset
#### Sample (January 2016 Subset) 
The following command can be used to load the `sample` version of the dataset, which contains all the patent applications that were filed to the USPTO during the month of January in 2016. This small subset of the dataset can be used for debugging and exploration purposes.

```python
from datasets import load_dataset

dataset_dict = load_dataset('HUPD/hupd',
    name='sample',
    data_files="https://huggingface.co/datasets/HUPD/hupd/blob/main/hupd_metadata_2022-02-22.feather", 
    icpr_label=None,
    train_filing_start_date='2016-01-01',
    train_filing_end_date='2016-01-21',
    val_filing_start_date='2016-01-22',
    val_filing_end_date='2016-01-31',
)
```

#### Full Dataset

If you would like to use the **full** version of the dataset, please make sure that change the `name` field from `sample` to `all`, specify the training and validation start and end dates carefully, and set `force_extract` to be `True` (so that you would only untar the files that you are interested in and not squander your disk storage space). In the following example, for instance, we set the training set year range to be [2011, 2016] (inclusive) and the validation set year range to be 2017.

```python
from datasets import load_dataset

dataset_dict = load_dataset('HUPD/hupd',
    name='all',
    data_files="https://huggingface.co/datasets/HUPD/hupd/blob/main/hupd_metadata_2022-02-22.feather", 
    icpr_label=None,
    force_extract=True,
    train_filing_start_date='2011-01-01',
    train_filing_end_date='2016-12-31',
    val_filing_start_date='2017-01-01',
    val_filing_end_date='2017-12-31',
)
```

### Google Colab Notebook
You can also use the following Google Colab notebooks to explore HUPD. 
- [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1_ZsI7WFTsEO0iu_0g3BLTkIkOUqPzCET?usp=sharing)[ HUPD Examples: Loading the Dataset](https://colab.research.google.com/drive/1_ZsI7WFTsEO0iu_0g3BLTkIkOUqPzCET?usp=sharing)
- [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1TzDDCDt368cUErH86Zc_P2aw9bXaaZy1?usp=sharing)[ HUPD Examples: Loading HUPD By Using HuggingFace's Libraries](https://colab.research.google.com/drive/1TzDDCDt368cUErH86Zc_P2aw9bXaaZy1?usp=sharing)
- [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1TzDDCDt368cUErH86Zc_P2aw9bXaaZy1?usp=sharing)[ HUPD Examples: Using the HUPD DistilRoBERTa Model](https://colab.research.google.com/drive/11t69BWcAVXndQxAOCpKaGkKkEYJSfydT?usp=sharing)
- [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1TzDDCDt368cUErH86Zc_P2aw9bXaaZy1?usp=sharing)[ HUPD Examples: Using the HUPD T5-Small Summarization Model](https://colab.research.google.com/drive/1VkCtrRIryzev_ixDjmJcfJNK-q6Vx24y?usp=sharing)

## Dataset Creation

### Source Data

HUPD synthesizes multiple data sources from the USPTO: While the full patent application texts were obtained from the USPTO Bulk Data Storage System (Patent Application Data/XML Versions 4.0, 4.1, 4.2, 4.3, 4.4 ICE, as well as Version 1.5) as XML files, the bibliographic filing metadata were obtained from the USPTO Patent Examination Research Dataset (in February, 2021).


### Annotations

Beyond our patent decision label, for which construction details are provided in the paper, the dataset does not contain any human-written or computer-generated annotations beyond those produced by patent applicants or the USPTO.

### Data Shift

A major feature of HUPD is its structure, which allows it to demonstrate the evolution of concepts over time. As we illustrate in the paper, the criteria for patent acceptance evolve over time at different rates, depending on category. We believe this is an important feature of the dataset, not only because of the social scientific questions it raises, but also because it facilitates research on models that can accommodate concept shift in a real-world setting. 


### Personal and Sensitive Information

The dataset contains information about the inventor(s) and examiner of each patent application. These details are, however, already in the public domain and available on the USPTO's Patent Application Information Retrieval (PAIR) system, as well as on Google Patents and PatentsView.

### Social Impact of the Dataset

The authors of the dataset hope that HUPD will have a positive social impact on the ML/NLP and Econ/IP communities. They discuss these considerations in more detail in [the paper](https://arxiv.org/abs/2207.04043).

### Impact on Underserved Communities and Discussion of Biases
The dataset contains patent applications in English, a language with heavy attention from the NLP community. However, innovation is spread across many languages, cultures, and communities that are not reflected in this dataset. HUPD is thus not representative of all kinds of innovation. Furthermore, patent applications require a fixed cost to draft and file and are not accessible to everyone. One goal of this dataset is to spur research that reduces the cost of drafting applications, potentially allowing for more people to seek intellectual property protection for their innovations.

### Discussion of Biases
Section 4 of [the HUPD paper](https://arxiv.org/abs/2207.04043) provides an examination of the dataset for potential biases. It shows, among other things, that female inventors are notably underrepresented in the U.S. patenting system, that small and micro entities (e.g., independent inventors, small companies, non-profit organizations) are less likely to have positive outcomes in patent obtaining than large entities (e.g., companies with more than 500 employees), and that patent filing and acceptance rates are not uniformly distributed across the US. Our empirical findings suggest that any study focusing on the acceptance prediction task, especially if it is using the inventor information or the small-entity indicator as part of the input, should be aware of the the potential biases present in the dataset and interpret their results carefully in light of those biases.

- Please refer to Section 4 and Section D for an in-depth discussion of potential biases embedded in the dataset.  


### Licensing Information

HUPD is released under the CreativeCommons Attribution-NonCommercial-ShareAlike 4.0 International.

### Citation Information

```
@article{suzgun2022hupd,
    title={The Harvard USPTO Patent Dataset: A Large-Scale, Well-Structured, and Multi-Purpose Corpus of Patent Applications},
    author={Suzgun, Mirac and Melas-Kyriazi, Luke and Sarkar, Suproteem K. and Kominers, Scott Duke and Shieber, Stuart M.},
    year={2022},
    publisher={arXiv preprint arXiv:2207.04043},
    url={https://arxiv.org/abs/2207.04043},
```