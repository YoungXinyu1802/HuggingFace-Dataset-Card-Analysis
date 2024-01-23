---
annotations_creators:
- other
language:
- bn
- en
language_creators:
- found
license:
- cc-by-nc-sa-4.0
multilinguality:
- translation
pretty_name: BanglaNMT
size_categories:
- 1M<n<10M
source_datasets: []
tags:
- bengali
- BanglaNMT
task_categories:
- translation
---

# Dataset Card for `BanglaNMT`

## Table of Contents
- [Dataset Card for `BanglaNMT`](#dataset-card-for-BanglaNMT)
  - [Table of Contents](#table-of-contents)
  - [Dataset Description](#dataset-description)
    - [Dataset Summary](#dataset-summary)
    - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
    - [Languages](#languages)
    - [Usage](#usage)
  - [Dataset Structure](#dataset-structure)
    - [Data Instances](#data-instances)
    - [Data Fields](#data-fields)
    - [Data Splits](#data-splits)
  - [Dataset Creation](#dataset-creation)
    - [Curation Rationale](#curation-rationale)
    - [Source Data](#source-data)
      - [Initial Data Collection and Normalization](#initial-data-collection-and-normalization)
      - [Who are the source language producers?](#who-are-the-source-language-producers)
    - [Annotations](#annotations)
      - [Annotation process](#annotation-process)
      - [Who are the annotators?](#who-are-the-annotators)
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

- **Repository:** [https://github.com/csebuetnlp/banglanmt](https://github.com/csebuetnlp/banglanmt)
- **Paper:** [**"Not Low-Resource Anymore: Aligner Ensembling, Batch Filtering, and New Datasets for Bengali-English Machine Translation"**](https://www.aclweb.org/anthology/2020.emnlp-main.207)
- **Point of Contact:** [Tahmid Hasan](mailto:tahmidhasan@cse.buet.ac.bd)

### Dataset Summary

This is the largest Machine Translation (MT) dataset for Bengali-English, curated using novel sentence alignment methods introduced **[here](https://aclanthology.org/2020.emnlp-main.207/).**

**Note:** This is a filtered version of the original dataset that the authors used for NMT training. For the complete set, refer to the offical [repository](https://github.com/csebuetnlp/banglanmt)


### Supported Tasks and Leaderboards

[More information needed](https://github.com/csebuetnlp/banglanmt)

### Languages

- `Bengali`
- `English`

### Usage
```python
from datasets import load_dataset
dataset = load_dataset("csebuetnlp/BanglaNMT")
```
## Dataset Structure

### Data Instances

One example from the dataset is given below in JSON format. 
  ```
  {
    'bn': 'বিমানবন্দরে যুক্তরাজ্যে নিযুক্ত বাংলাদেশ হাইকমিশনার সাঈদা মুনা তাসনীম ও লন্ডনে বাংলাদেশ মিশনের জ্যেষ্ঠ কর্মকর্তারা তাকে বিদায় জানান।',
    'en': 'Bangladesh High Commissioner to the United Kingdom Saida Muna Tasneen and senior officials of Bangladesh Mission in London saw him off at the airport.'
  }
  ```

### Data Fields

The data fields are as follows:

- `bn`: a `string` feature indicating the Bengali sentence.
- `en`: a `string` feature indicating the English translation.

### Data Splits
|   split   |count  |
|----------|--------|
|`train`|  2379749 |
|`validation`| 597  |
|`test`| 1000 |




## Dataset Creation

[More information needed](https://github.com/csebuetnlp/banglanmt)

### Curation Rationale

[More information needed](https://github.com/csebuetnlp/banglanmt)

### Source Data

[More information needed](https://github.com/csebuetnlp/banglanmt)

#### Initial Data Collection and Normalization

[More information needed](https://github.com/csebuetnlp/banglanmt)


#### Who are the source language producers?

[More information needed](https://github.com/csebuetnlp/banglanmt)


### Annotations

[More information needed](https://github.com/csebuetnlp/banglanmt)


#### Annotation process

[More information needed](https://github.com/csebuetnlp/banglanmt)

#### Who are the annotators?

[More information needed](https://github.com/csebuetnlp/banglanmt)

### Personal and Sensitive Information

[More information needed](https://github.com/csebuetnlp/banglanmt)

## Considerations for Using the Data

### Social Impact of Dataset

[More information needed](https://github.com/csebuetnlp/banglanmt)

### Discussion of Biases

[More information needed](https://github.com/csebuetnlp/banglanmt)

### Other Known Limitations

[More information needed](https://github.com/csebuetnlp/banglanmt)

## Additional Information

### Dataset Curators

[More information needed](https://github.com/csebuetnlp/banglanmt)

### Licensing Information

Contents of this repository are restricted to only non-commercial research purposes under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/). Copyright of the dataset contents belongs to the original copyright holders.
### Citation Information

If you use the dataset, please cite the following paper:
```
@inproceedings{hasan-etal-2020-low,
    title = "Not Low-Resource Anymore: Aligner Ensembling, Batch Filtering, and New Datasets for {B}engali-{E}nglish Machine Translation",
    author = "Hasan, Tahmid  and
      Bhattacharjee, Abhik  and
      Samin, Kazi  and
      Hasan, Masum  and
      Basak, Madhusudan  and
      Rahman, M. Sohel  and
      Shahriyar, Rifat",
    booktitle = "Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.emnlp-main.207",
    doi = "10.18653/v1/2020.emnlp-main.207",
    pages = "2612--2623",
    abstract = "Despite being the seventh most widely spoken language in the world, Bengali has received much less attention in machine translation literature due to being low in resources. Most publicly available parallel corpora for Bengali are not large enough; and have rather poor quality, mostly because of incorrect sentence alignments resulting from erroneous sentence segmentation, and also because of a high volume of noise present in them. In this work, we build a customized sentence segmenter for Bengali and propose two novel methods for parallel corpus creation on low-resource setups: aligner ensembling and batch filtering. With the segmenter and the two methods combined, we compile a high-quality Bengali-English parallel corpus comprising of 2.75 million sentence pairs, more than 2 million of which were not available before. Training on neural models, we achieve an improvement of more than 9 BLEU score over previous approaches to Bengali-English machine translation. We also evaluate on a new test set of 1000 pairs made with extensive quality control. We release the segmenter, parallel corpus, and the evaluation set, thus elevating Bengali from its low-resource status. To the best of our knowledge, this is the first ever large scale study on Bengali-English machine translation. We believe our study will pave the way for future research on Bengali-English machine translation as well as other low-resource languages. Our data and code are available at https://github.com/csebuetnlp/banglanmt.",
}
```


### Contributions

Thanks to [@abhik1505040](https://github.com/abhik1505040) and [@Tahmid](https://github.com/Tahmid04) for adding this dataset.