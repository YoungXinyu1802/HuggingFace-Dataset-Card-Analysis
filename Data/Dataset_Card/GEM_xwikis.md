---
annotations_creators:
- found
language_creators:
- unknown
language:
- de
- en
- fr
- cs
license:
- cc-by-sa-4.0
multilinguality:
- unknown
size_categories:
- unknown
source_datasets:
- original
task_categories:
- summarization
task_ids: []
pretty_name: xwikis
---

# Dataset Card for GEM/xwikis

## Dataset Description

- **Homepage:** https://github.com/lauhaide/clads
- **Repository:** [Needs More Information]
- **Paper:** https://arxiv.org/abs/2202.09583
- **Leaderboard:** N/A
- **Point of Contact:** Laura Perez-Beltrachini

### Link to Main Data Card

You can find the main data card on the [GEM Website](https://gem-benchmark.com/data_cards/xwikis).

### Dataset Summary 

The XWikis Corpus provides datasets with different language pairs and directions for cross-lingual and multi-lingual abstractive document summarisation. 

You can load the dataset via:
```
import datasets
data = datasets.load_dataset('GEM/xwikis')
```
The data loader can be found [here](https://huggingface.co/datasets/GEM/xwikis).

#### website
[Github](https://github.com/lauhaide/clads)

#### paper
https://arxiv.org/abs/2202.09583

#### authors
Laura Perez-Beltrachini (University of Edinburgh)

## Dataset Overview

### Where to find the Data and its Documentation

#### Webpage

<!-- info: What is the webpage for the dataset (if it exists)? -->
<!-- scope: telescope -->
[Github](https://github.com/lauhaide/clads)

#### Paper

<!-- info: What is the link to the paper describing the dataset (open access preferred)? -->
<!-- scope: telescope -->
https://arxiv.org/abs/2202.09583

#### BibTex

<!-- info: Provide the BibTex-formatted reference for the dataset. Please use the correct published version (ACL anthology, etc.) instead of google scholar created Bibtex. -->
<!-- scope: microscope -->
```
@InProceedings{clads-emnlp,
  author =      "Laura Perez-Beltrachini and Mirella Lapata",
  title =       "Models and Datasets for Cross-Lingual Summarisation",
  booktitle =   "Proceedings of The 2021 Conference on Empirical Methods in Natural Language Processing ",
  year =        "2021",
  address =     "Punta Cana, Dominican Republic",
}
```

#### Contact Name

<!-- quick -->
<!-- info: If known, provide the name of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
Laura Perez-Beltrachini

#### Contact Email

<!-- info: If known, provide the email of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
lperez@ed.ac.uk

#### Has a Leaderboard?

<!-- info: Does the dataset have an active leaderboard? -->
<!-- scope: telescope -->
no


### Languages and Intended Use

#### Multilingual?

<!-- quick -->
<!-- info: Is the dataset multilingual? -->
<!-- scope: telescope -->
yes

#### Covered Languages

<!-- quick -->
<!-- info: What languages/dialects are covered in the dataset? -->
<!-- scope: telescope -->
`German`, `English`, `French`, `Czech`, `Chinese`

#### License

<!-- quick -->
<!-- info: What is the license of the dataset? -->
<!-- scope: telescope -->
cc-by-sa-4.0: Creative Commons Attribution Share Alike 4.0 International

#### Intended Use

<!-- info: What is the intended use of the dataset? -->
<!-- scope: microscope -->
Cross-lingual and Multi-lingual single long input document abstractive summarisation.

#### Primary Task

<!-- info: What primary task does the dataset support? -->
<!-- scope: telescope -->
Summarization

#### Communicative Goal

<!-- quick -->
<!-- info: Provide a short description of the communicative goal of a model trained for this task on this dataset. -->
<!-- scope: periscope -->
Entity descriptive summarisation, that is, generate a summary that conveys the most salient facts of a document related to a given entity.


### Credit

#### Curation Organization Type(s)

<!-- info: In what kind of organization did the dataset curation happen? -->
<!-- scope: telescope -->
`academic`

#### Dataset Creators

<!-- info: Who created the original dataset? List the people involved in collecting the dataset and their affiliation(s). -->
<!-- scope: microscope -->
Laura Perez-Beltrachini (University of Edinburgh)

#### Who added the Dataset to GEM?

<!-- info: Who contributed to the data card and adding the dataset to GEM? List the people+affiliations involved in creating this data card and who helped integrate this dataset into GEM. -->
<!-- scope: microscope -->
Laura Perez-Beltrachini (University of Edinburgh) and Ronald Cardenas (University of Edinburgh)


### Dataset Structure

#### Data Splits

<!-- info: Describe and name the splits in the dataset if there are more than one. -->
<!-- scope: periscope -->
For each language pair and direction there exists a train/valid/test split. 
The test split is a sample of size 7k from the intersection of titles existing in the four languages (cs,fr,en,de).
Train/valid are randomly split.



## Dataset in GEM

### Rationale for Inclusion in GEM

#### Similar Datasets

<!-- info: Do other datasets for the high level task exist? -->
<!-- scope: telescope -->
no


### GEM-Specific Curation

#### Modificatied for GEM?

<!-- info: Has the GEM version of the dataset been modified in any way (data, processing, splits) from the original curated data? -->
<!-- scope: telescope -->
no

#### Additional Splits?

<!-- info: Does GEM provide additional splits to the dataset? -->
<!-- scope: telescope -->
no


### Getting Started with the Task




## Previous Results

### Previous Results

#### Measured Model Abilities

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: telescope -->
- identification of entity salient information
- translation
- multi-linguality
- cross-lingual transfer, zero-shot, few-shot

#### Metrics

<!-- info: What metrics are typically used for this task? -->
<!-- scope: periscope -->
`ROUGE`

#### Previous results available?

<!-- info: Are previous results available? -->
<!-- scope: telescope -->
yes

#### Other Evaluation Approaches

<!-- info: What evaluation approaches have others used? -->
<!-- scope: periscope -->
ROUGE-1/2/L



## Dataset Curation

### Original Curation

#### Sourced from Different Sources

<!-- info: Is the dataset aggregated from different data sources? -->
<!-- scope: telescope -->
no


### Language Data

#### How was Language Data Obtained?

<!-- info: How was the language data obtained? -->
<!-- scope: telescope -->
`Found`

#### Where was it found?

<!-- info: If found, where from? -->
<!-- scope: telescope -->
`Single website`

#### Data Validation

<!-- info: Was the text validated by a different worker or a data curator? -->
<!-- scope: telescope -->
other

#### Was Data Filtered?

<!-- info: Were text instances selected or filtered? -->
<!-- scope: telescope -->
not filtered


### Structured Annotations

#### Additional Annotations?

<!-- quick -->
<!-- info: Does the dataset have additional annotations for each instance? -->
<!-- scope: telescope -->
found

#### Annotation Service?

<!-- info: Was an annotation service used? -->
<!-- scope: telescope -->
no

#### Annotation Values

<!-- info: Purpose and values for each annotation -->
<!-- scope: microscope -->
The input documents have section structure information.

#### Any Quality Control?

<!-- info: Quality control measures? -->
<!-- scope: telescope -->
validated by another rater

#### Quality Control Details

<!-- info: Describe the quality control measures that were taken. -->
<!-- scope: microscope -->
Bilingual annotators assessed the content overlap of source document and target summaries.


### Consent

#### Any Consent Policy?

<!-- info: Was there a consent policy involved when gathering the data? -->
<!-- scope: telescope -->
no


### Private Identifying Information (PII)

#### Contains PII?

<!-- quick -->
<!-- info: Does the source language data likely contain Personal Identifying Information about the data creators or subjects? -->
<!-- scope: telescope -->
no PII


### Maintenance

#### Any Maintenance Plan?

<!-- info: Does the original dataset have a maintenance plan? -->
<!-- scope: telescope -->
no



## Broader Social Context

### Previous Work on the Social Impact of the Dataset

#### Usage of Models based on the Data

<!-- info: Are you aware of cases where models trained on the task featured in this dataset ore related tasks have been used in automated systems? -->
<!-- scope: telescope -->
no


### Impact on Under-Served Communities

#### Addresses needs of underserved Communities?

<!-- info: Does this dataset address the needs of communities that are traditionally underserved in language technology, and particularly language generation technology? Communities may be underserved for exemple because their language, language variety, or social or geographical context is underepresented in NLP and NLG resources (datasets and models). -->
<!-- scope: telescope -->
no


### Discussion of Biases

#### Any Documented Social Biases?

<!-- info: Are there documented social biases in the dataset? Biases in this context are variations in the ways members of different social categories are represented that can have harmful downstream consequences for members of the more disadvantaged group. -->
<!-- scope: telescope -->
no



## Considerations for Using the Data

### PII Risks and Liability



### Licenses

#### Copyright Restrictions on the Dataset

<!-- info: Based on your answers in the Intended Use part of the Data Overview Section, which of the following best describe the copyright and licensing status of the dataset? -->
<!-- scope: periscope -->
`public domain`

#### Copyright Restrictions on the Language Data

<!-- info: Based on your answers in the Language part of the Data Curation Section, which of the following best describe the copyright and licensing status of the underlying language data? -->
<!-- scope: periscope -->
`public domain`


### Known Technical Limitations



