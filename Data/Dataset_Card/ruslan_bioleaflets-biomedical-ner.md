---
annotations_creators:
- machine-generated
language:
- en
language_creators:
- expert-generated
license:
- apache-2.0
multilinguality:
- monolingual
pretty_name: bioleaflets-biomedical-ner
size_categories:
- 1K<n<10K
source_datasets:
- original
tags:
- bio
- medical
- biomedical
- bioleaflets
- medicine
- data2text
- data-to-text
task_categories:
- text-generation
- text2text-generation
task_ids:
- language-modeling
---

# Dataset Card for *BioLeaflets* Dataset

## Table of Contents
- [Table of Contents](#table-of-contents)
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

- **Homepage:**
- **Repository:** [GitHub link](https://github.com/bayer-science-for-a-better-life/data2text-bioleaflets)
- **Paper:** [ACL Anthology](https://aclanthology.org/2021.inlg-1.40/)
- **Leaderboard:** [Papers with Code leaderboard for BioLeaflets Dataset](https://paperswithcode.com/dataset/bioleaflets)
- **Point of Contact:** [Ruslan Yermakov](https://github.com/wingedRuslan)

### Dataset Summary

*BioLeaflets* is a biomedical dataset for Data2Text generation. It is a corpus of 1,336 package leaflets of medicines authorised in Europe, which were obtained by scraping the European Medicines Agency (EMA) website. 
Package leaflets are included in the packaging of medicinal products and contain information to help patients use the product safely and appropriately. 
This dataset comprises the large majority (∼ 90%) of medicinal products authorised through the centralised procedure in Europe as of January 2021. 
For more detailed information, please read the paper at [ACL Anthology](https://aclanthology.org/2021.inlg-1.40/). 

### Supported Tasks and Leaderboards

BioLeaflets proposes a **conditional generation task** (data-to-text) in the biomedical domain: given an ordered set of entities as source, the *goal* is to produce a multi-sentence section. 
Successful generation thus requires the model to learn specific syntax, terminology, and writing style from the corpus. Alternatively, the dataset might be used for **named-entity recognition task**: given text, detect medical entities. 
The dataset provides an extensive description of medicinal products and thus supports a plain **language modeling task** focused on biomedical data.

### Languages

Monolingual - en.

## Dataset Structure

### Data Instances

For each instance (leaflet), there is a unique ID, URL, Product_Name, and textual information clearly describing the medicine. 
The content of each section is not standardized (NO template), yet it is still well-structured. 
Each document contains six sections: 
1) What is the product and what is it used for
2) What you need to know before you take the product
3) Product usage instructions
4) possible side effects
5) product storage conditions
6) other information

Every section is represented as a dictionary with the 'Title', 'Section_Content', and 'Entity_Recognition' as keys. 
The content of each section is lower-cased and tokenized by treating all special characters as separate tokens. 

### Data Fields

- `ID`: a string representing a unique ID assigned to a leaflet
- `URL`: a string containing the link to the article on the European Medicines Agency (EMA) website  
- `Product Name`: a string, the name of the medicine
- `Full Content`: a string covering the full content of the article available at URL
- `Section 1`: a dictionary including section 1 content and associated medical entities
- `Section 2`: a dictionary including section 2 content and associated medical entities
- `Section 3`: a dictionary including section 3 content and associated medical entities
- `Section 4`: a dictionary including section 4 content and associated medical entities
- `Section 5`: a dictionary including section 5 content and associated medical entities
- `Section 6`: a dictionary including section 6 content and associated medical entities

### Data Splits

We randomly split the dataset into training (80%), development (10%), and test (10%) set. Duplicates are removed.

## Dataset Creation

### Curation Rationale

Introduce a new biomedical dataset (BioLeaflets), which could serve as a benchmark for biomedical text generation models. 
BioLeaflets proposes a conditional generation task: given an ordered set of entities as source, the goal is to produce a multi-sentence section.

### Source Data

#### Initial Data Collection and Normalization

The dataset was obtained by scraping the European Medicines Agency (EMA) website. 
Each leaflet has an URL associated with it to the article on the EMA website.  

#### Who are the source language producers?

Labeling experts with domain knowledge produced factual information.

### Annotations

#### Annotation process

To create the required input for data-to-text generation, we augment each document by leveraging named entity recognition (NER). 
We combine two NER frameworks: Amazon Comprehend Medical (commercial) and Stanford Stanza (open-sourced). 
Additionally, we treat all digits as entities and add the medicine name as the first entity

#### Who are the annotators?

Machine-generated: ensemble of state-of-the-art named entity recognition (NER) models. 

### Personal and Sensitive Information

[Not included / Not present]

## Considerations for Using the Data

### Social Impact of Dataset

The purpose of this dataset is to help develop models that can automatically generate long paragraphs of text as well as to facilitate the development of NLP models in the biomedical domain. 
The main challenges of this dataset for D2T generation are multi-sentence and multi-section target text, small sample size, specialized medical vocabulary, and syntax. 

### Discussion of Biases

Package leaflets are published for medicinal products approved in the European Union (EU). 
They are included in the packaging of medicinal products and contain information to help patients use the product safely and appropriately. 
The dataset represents factual information produced by labeling experts and validated before publishing. Hence, biases of any kind are not present in the dataset. 
Package leaflets are required to be written in a way that is clear and understandable. 

### Other Known Limitations

[N/A]

## Additional Information

### Dataset Curators

The data was originally collected by Ruslan Yermakov<sup>*</sup>, Nicholas Drago, and Angelo Ziletti at Bayer AG (Decision Science & Advanced Analytics unit). The code is made publicly available at [github link](https://github.com/bayer-science-for-a-better-life/data2text-bioleaflets)

<sup>*</sup> Work done during internship.

### Licensing Information

The *BioLeaflets* dataset is released under the [Apache-2.0 License](http://www.apache.org/licenses/LICENSE-2.0). 

### Citation Information

    @inproceedings{yermakov-etal-2021-biomedical,
    title = "Biomedical Data-to-Text Generation via Fine-Tuning Transformers",
    author = "Yermakov, Ruslan  and
      Drago, Nicholas  and
      Ziletti, Angelo",
    booktitle = "Proceedings of the 14th International Conference on Natural Language Generation",
    month = aug,
    year = "2021",
    address = "Aberdeen, Scotland, UK",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.inlg-1.40",
    pages = "364--370",
    abstract = "Data-to-text (D2T) generation in the biomedical domain is a promising - yet mostly unexplored - field of research. Here, we apply neural models for   D2T generation to a real-world dataset consisting of package leaflets of European medicines. We show that fine-tuned transformers are able to generate realistic, multi-sentence text from data in the biomedical domain, yet have important limitations. We also release a new dataset (BioLeaflets) for benchmarking D2T generation models in the biomedical domain.",
    }

### Contributions

Thanks to [@wingedRuslan](https://github.com/wingedRuslan) for adding this dataset.

