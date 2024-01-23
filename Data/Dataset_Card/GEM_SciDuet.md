---
annotations_creators:
- none
language_creators:
- unknown
language:
- en
license:
- apache-2.0
multilinguality:
- unknown
size_categories:
- unknown
source_datasets:
- original
task_categories:
- other
task_ids: []
pretty_name: SciDuet
tags:
- text-to-slide
---

# Dataset Card for GEM/SciDuet

## Dataset Description

- **Homepage:** https://huggingface.co/datasets/GEM/SciDuet
- **Repository:** https://github.com/IBM/document2slides/tree/main/SciDuet-ACL
- **Paper:** https://aclanthology.org/2021.naacl-main.111/
- **Leaderboard:** N/A
- **Point of Contact:** N/A

### Link to Main Data Card

You can find the main data card on the [GEM Website](https://gem-benchmark.com/data_cards/SciDuet).

### Dataset Summary 

This dataset supports the document-to-slide generation task where a model has to generate presentation slide content from the text of a document. 

You can load the dataset via:
```
import datasets
data = datasets.load_dataset('GEM/SciDuet')
```
The data loader can be found [here](https://huggingface.co/datasets/GEM/SciDuet).

#### website
[Huggingface](https://huggingface.co/datasets/GEM/SciDuet)

#### paper
[ACL Anthology](https://aclanthology.org/2021.naacl-main.111/)

#### authors
Edward Sun, Yufang Hou, Dakuo Wang, Yunfeng Zhang, Nancy Wang

## Dataset Overview

### Where to find the Data and its Documentation

#### Webpage

<!-- info: What is the webpage for the dataset (if it exists)? -->
<!-- scope: telescope -->
[Huggingface](https://huggingface.co/datasets/GEM/SciDuet)

#### Download

<!-- info: What is the link to where the original dataset is hosted? -->
<!-- scope: telescope -->
[Github](https://github.com/IBM/document2slides/tree/main/SciDuet-ACL)

#### Paper

<!-- info: What is the link to the paper describing the dataset (open access preferred)? -->
<!-- scope: telescope -->
[ACL Anthology](https://aclanthology.org/2021.naacl-main.111/)

#### BibTex

<!-- info: Provide the BibTex-formatted reference for the dataset. Please use the correct published version (ACL anthology, etc.) instead of google scholar created Bibtex. -->
<!-- scope: microscope -->
```
@inproceedings{sun-etal-2021-d2s,
    title = "{D}2{S}: Document-to-Slide Generation Via Query-Based Text Summarization",
    author = "Sun, Edward  and
      Hou, Yufang  and
      Wang, Dakuo  and
      Zhang, Yunfeng  and
      Wang, Nancy X. R.",
    booktitle = "Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies",
    month = jun,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.naacl-main.111",
    doi = "10.18653/v1/2021.naacl-main.111",
    pages = "1405--1418",
    abstract = "Presentations are critical for communication in all areas of our lives, yet the creation of slide decks is often tedious and time-consuming. There has been limited research aiming to automate the document-to-slides generation process and all face a critical challenge: no publicly available dataset for training and benchmarking. In this work, we first contribute a new dataset, SciDuet, consisting of pairs of papers and their corresponding slides decks from recent years{'} NLP and ML conferences (e.g., ACL). Secondly, we present D2S, a novel system that tackles the document-to-slides task with a two-step approach: 1) Use slide titles to retrieve relevant and engaging text, figures, and tables; 2) Summarize the retrieved context into bullet points with long-form question answering. Our evaluation suggests that long-form QA outperforms state-of-the-art summarization baselines on both automated ROUGE metrics and qualitative human evaluation.",
}
```

#### Has a Leaderboard?

<!-- info: Does the dataset have an active leaderboard? -->
<!-- scope: telescope -->
no


### Languages and Intended Use

#### Multilingual?

<!-- quick -->
<!-- info: Is the dataset multilingual? -->
<!-- scope: telescope -->
no

#### Covered Languages

<!-- quick -->
<!-- info: What languages/dialects are covered in the dataset? -->
<!-- scope: telescope -->
`English`

#### License

<!-- quick -->
<!-- info: What is the license of the dataset? -->
<!-- scope: telescope -->
apache-2.0: Apache License 2.0

#### Intended Use

<!-- info: What is the intended use of the dataset? -->
<!-- scope: microscope -->
Promote research on the task of document-to-slides generation

#### Primary Task

<!-- info: What primary task does the dataset support? -->
<!-- scope: telescope -->
Text-to-Slide


### Credit

#### Curation Organization Type(s)

<!-- info: In what kind of organization did the dataset curation happen? -->
<!-- scope: telescope -->
`industry`

#### Curation Organization(s)

<!-- info: Name the organization(s). -->
<!-- scope: periscope -->
IBM Research

#### Dataset Creators

<!-- info: Who created the original dataset? List the people involved in collecting the dataset and their affiliation(s). -->
<!-- scope: microscope -->
Edward Sun, Yufang Hou, Dakuo Wang, Yunfeng Zhang, Nancy Wang

#### Funding

<!-- info: Who funded the data creation? -->
<!-- scope: microscope -->
IBM Research

#### Who added the Dataset to GEM?

<!-- info: Who contributed to the data card and adding the dataset to GEM? List the people+affiliations involved in creating this data card and who helped integrate this dataset into GEM. -->
<!-- scope: microscope -->
Yufang Hou (IBM Research), Dakuo Wang (IBM Research)


### Dataset Structure

#### How were labels chosen?

<!-- info: How were the labels chosen? -->
<!-- scope: microscope -->
The original papers and slides (both are in PDF format) are carefully processed by a combination of PDF/Image processing tookits. The text contents from multiple slides that correspond to the same slide title are mreged.

#### Data Splits

<!-- info: Describe and name the splits in the dataset if there are more than one. -->
<!-- scope: periscope -->
Training, validation and testing data contain 136, 55, and 81 papers from ACL Anthology and their corresponding slides, respectively. 

#### Splitting Criteria

<!-- info: Describe any criteria for splitting the data, if used. If there are differences between the splits (e.g., if the training annotations are machine-generated and the dev and test ones are created by humans, or if different numbers of annotators contributed to each example), describe them here. -->
<!-- scope: microscope -->
The dataset integrated into GEM is the ACL portion of the whole dataset described in the [paper](https://aclanthology.org/2021.naacl-main.111), It contains the full Dev and Test sets, and a portion of the Train dataset. 
Note that although we cannot release the  whole training dataset due to copyright issues, researchers can still use our released data procurement code to generate the training dataset from the online ICML/NeurIPS anthologies.



## Dataset in GEM

### Rationale for Inclusion in GEM

#### Why is the Dataset in GEM?

<!-- info: What does this dataset contribute toward better generation evaluation and why is it part of GEM? -->
<!-- scope: microscope -->
SciDuet is the first publicaly available dataset for the challenging task of document2slides generation, which requires a model has a good ability to "understand" long-form text, choose appropriate content and generate key points.

#### Similar Datasets

<!-- info: Do other datasets for the high level task exist? -->
<!-- scope: telescope -->
no

#### Ability that the Dataset measures

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: periscope -->
content selection, long-form text undersanding and generation


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
content selection, long-form text undersanding and key points generation

#### Metrics

<!-- info: What metrics are typically used for this task? -->
<!-- scope: periscope -->
`ROUGE`

#### Proposed Evaluation

<!-- info: List and describe the purpose of the metrics and evaluation methodology (including human evaluation) that the dataset creators used when introducing this task. -->
<!-- scope: microscope -->
Automatical Evaluation Metric: ROUGE
Human Evaluation: (Readability, Informativeness, Consistency) 
1) Readability:  The generated slide content is coherent, concise, and grammatically correct;
2) Informativeness: The generated slide provides sufficient and necessary information that corresponds to the given slide title, regardless of its similarity to the original slide;
3) Consistency: The generated slide content is similar to the original author’s reference slide.

#### Previous results available?

<!-- info: Are previous results available? -->
<!-- scope: telescope -->
yes

#### Other Evaluation Approaches

<!-- info: What evaluation approaches have others used? -->
<!-- scope: periscope -->
ROUGE + Human Evaluation

#### Relevant Previous Results

<!-- info: What are the most relevant previous results for this task/dataset? -->
<!-- scope: microscope -->
Paper "D2S: Document-to-Slide Generation Via Query-Based
Text Summarization" reports 20.47, 5.26 and 19.08 for ROUGE-1, ROUGE-2 and ROUGE-L (f-score).



## Dataset Curation

### Original Curation

#### Original Curation Rationale

<!-- info: Original curation rationale -->
<!-- scope: telescope -->
Provide a benchmark dataset for the document-to-slides task.

#### Sourced from Different Sources

<!-- info: Is the dataset aggregated from different data sources? -->
<!-- scope: telescope -->
no


### Language Data

#### How was Language Data Obtained?

<!-- info: How was the language data obtained? -->
<!-- scope: telescope -->
`Other`

#### Data Validation

<!-- info: Was the text validated by a different worker or a data curator? -->
<!-- scope: telescope -->
not validated

#### Data Preprocessing

<!-- info: How was the text data pre-processed? (Enter N/A if the text was not pre-processed) -->
<!-- scope: microscope -->
Text on papers was extracted through Grobid. Figures andcaptions were extracted through pdffigures. Text on slides was extracted through IBM Watson Discovery package and OCR by pytesseract. Figures and tables that appear on slides and papers were linked through multiscale template matching by OpenCV. Further dataset
cleaning was performed with standard string-based
heuristics on sentence building, equation and floating caption removal, and duplicate line deletion.

#### Was Data Filtered?

<!-- info: Were text instances selected or filtered? -->
<!-- scope: telescope -->
algorithmically

#### Filter Criteria

<!-- info: What were the selection criteria? -->
<!-- scope: microscope -->
the slide context text shouldn't contain additional format information such as "*** University" 


### Structured Annotations

#### Additional Annotations?

<!-- quick -->
<!-- info: Does the dataset have additional annotations for each instance? -->
<!-- scope: telescope -->
none

#### Annotation Service?

<!-- info: Was an annotation service used? -->
<!-- scope: telescope -->
no


### Consent

#### Any Consent Policy?

<!-- info: Was there a consent policy involved when gathering the data? -->
<!-- scope: telescope -->
yes

#### Consent Policy Details

<!-- info: What was the consent policy? -->
<!-- scope: microscope -->
The original dataset was open-sourced under Apache-2.0.  
Some of the original dataset creators are part of the GEM v2 dataset infrastructure team and take care of integrating this dataset into GEM.


### Private Identifying Information (PII)

#### Contains PII?

<!-- quick -->
<!-- info: Does the source language data likely contain Personal Identifying Information about the data creators or subjects? -->
<!-- scope: telescope -->
yes/very likely

#### Categories of PII

<!-- info: What categories of PII are present or suspected in the data? -->
<!-- scope: periscope -->
`generic PII`

#### Any PII Identification?

<!-- info: Did the curators use any automatic/manual method to identify PII in the dataset? -->
<!-- scope: periscope -->
no identification


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
unsure



## Considerations for Using the Data

### PII Risks and Liability



### Licenses

#### Copyright Restrictions on the Dataset

<!-- info: Based on your answers in the Intended Use part of the Data Overview Section, which of the following best describe the copyright and licensing status of the dataset? -->
<!-- scope: periscope -->
`non-commercial use only`

#### Copyright Restrictions on the Language Data

<!-- info: Based on your answers in the Language part of the Data Curation Section, which of the following best describe the copyright and licensing status of the underlying language data? -->
<!-- scope: periscope -->
`research use only`


### Known Technical Limitations



