---
annotations_creators:
- none
language_creators:
- unknown
languages:
- unknown
licenses:
- mit
multilinguality:
- unknown
pretty_name: indonlg
size_categories:
- unknown
source_datasets:
- original
task_categories:
- summarization
task_ids:
- unknown
---

# Dataset Card for GEM/indonlg

## Dataset Description

- **Homepage:** https://github.com/indobenchmark/indonlg
- **Repository:** https://github.com/indobenchmark/indonlg
- **Paper:** https://aclanthology.org/2021.emnlp-main.699
- **Leaderboard:** N/A
- **Point of Contact:** Genta Indra Winata

### Link to Main Data Card

You can find the main data card on the [GEM Website](https://gem-benchmark.com/data_cards/indonlg).

### Dataset Summary 

IndoNLG is a collection of various Indonesian, Javanese, and Sundanese NLG tasks including summarization, question answering, chit-chat, and three different pairs of machine translation (MT) tasks.

You can load the dataset via:
```
import datasets
data = datasets.load_dataset('GEM/indonlg')
```
The data loader can be found [here](https://huggingface.co/datasets/GEM/indonlg).

#### website
[Github](https://github.com/indobenchmark/indonlg)

#### paper
[ACL Anthology](https://aclanthology.org/2021.emnlp-main.699)

#### authors
Samuel Cahyawijaya, Genta Indra Winata, Bryan Wilie, Karissa Vincentio, Xiaohong Li, Adhiguna Kuncoro, Sebastian Ruder, Zhi Yuan Lim, Syafri Bahar, Masayu Leylia Khodra, Ayu Purwarianti, Pascale Fung

## Dataset Overview

### Where to find the Data and its Documentation

#### Webpage

<!-- info: What is the webpage for the dataset (if it exists)? -->
<!-- scope: telescope -->
[Github](https://github.com/indobenchmark/indonlg)

#### Download

<!-- info: What is the link to where the original dataset is hosted? -->
<!-- scope: telescope -->
[Github](https://github.com/indobenchmark/indonlg)

#### Paper

<!-- info: What is the link to the paper describing the dataset (open access preferred)? -->
<!-- scope: telescope -->
[ACL Anthology](https://aclanthology.org/2021.emnlp-main.699)

#### BibTex

<!-- info: Provide the BibTex-formatted reference for the dataset. Please use the correct published version (ACL anthology, etc.) instead of google scholar created Bibtex. -->
<!-- scope: microscope -->
```
@inproceedings{cahyawijaya-etal-2021-indonlg, title =  '{I}ndo{NLG}: Benchmark and Resources for Evaluating {I}ndonesian Natural Language Generation ', author =  'Cahyawijaya, Samuel and Winata, Genta Indra and Wilie, Bryan and Vincentio, Karissa and Li, Xiaohong and Kuncoro, Adhiguna and Ruder, Sebastian and Lim, Zhi Yuan and Bahar, Syafri and Khodra, Masayu and Purwarianti, Ayu and Fung, Pascale ', booktitle =  'Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing ', month = nov, year =  '2021 ', address =  'Online and Punta Cana, Dominican Republic ', publisher =  'Association for Computational Linguistics ', url =  'https://aclanthology.org/2021.emnlp-main.699 ', pages =  '8875--8898 ', abstract =  'Natural language generation (NLG) benchmarks provide an important avenue to measure progress and develop better NLG systems. Unfortunately, the lack of publicly available NLG benchmarks for low-resource languages poses a challenging barrier for building NLG systems that work well for languages with limited amounts of data. Here we introduce IndoNLG, the first benchmark to measure natural language generation (NLG) progress in three low-resource{---}yet widely spoken{---}languages of Indonesia: Indonesian, Javanese, and Sundanese. Altogether, these languages are spoken by more than 100 million native speakers, and hence constitute an important use case of NLG systems today. Concretely, IndoNLG covers six tasks: summarization, question answering, chit-chat, and three different pairs of machine translation (MT) tasks. We collate a clean pretraining corpus of Indonesian, Sundanese, and Javanese datasets, Indo4B-Plus, which is used to pretrain our models: IndoBART and IndoGPT. We show that IndoBART and IndoGPT achieve competitive performance on all tasks{---}despite using only one-fifth the parameters of a larger multilingual model, mBART-large (Liu et al., 2020). This finding emphasizes the importance of pretraining on closely related, localized languages to achieve more efficient learning and faster inference at very low-resource languages like Javanese and Sundanese. ',}
```

#### Contact Name

<!-- quick -->
<!-- info: If known, provide the name of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
Genta Indra Winata

#### Contact Email

<!-- info: If known, provide the email of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
gentaindrawinata@gmail.com

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
`Indonesian`, `Javanese`, `Sundanese`

#### License

<!-- quick -->
<!-- info: What is the license of the dataset? -->
<!-- scope: telescope -->
mit: MIT License

#### Intended Use

<!-- info: What is the intended use of the dataset? -->
<!-- scope: microscope -->
IndoNLG is a collection of Natural Language Generation (NLG) resources for Bahasa Indonesia with 10 downstream tasks.

#### Primary Task

<!-- info: What primary task does the dataset support? -->
<!-- scope: telescope -->
Summarization

#### Communicative Goal

<!-- quick -->
<!-- info: Provide a short description of the communicative goal of a model trained for this task on this dataset. -->
<!-- scope: periscope -->
Generate a response according to the context and text.


### Credit

#### Curation Organization Type(s)

<!-- info: In what kind of organization did the dataset curation happen? -->
<!-- scope: telescope -->
`academic`, `industry`

#### Curation Organization(s)

<!-- info: Name the organization(s). -->
<!-- scope: periscope -->
The Hong Kong University of Science and Technology, Gojek, Institut Teknologi Bandung, Universitas Multimedia Nusantara, DeepMind, Prosa.ai

#### Dataset Creators

<!-- info: Who created the original dataset? List the people involved in collecting the dataset and their affiliation(s). -->
<!-- scope: microscope -->
Samuel Cahyawijaya, Genta Indra Winata, Bryan Wilie, Karissa Vincentio, Xiaohong Li, Adhiguna Kuncoro, Sebastian Ruder, Zhi Yuan Lim, Syafri Bahar, Masayu Leylia Khodra, Ayu Purwarianti, Pascale Fung

#### Funding

<!-- info: Who funded the data creation? -->
<!-- scope: microscope -->
The Hong Kong University of Science and Technology, Gojek, Institut Teknologi Bandung, Universitas Multimedia Nusantara, DeepMind, Prosa.ai

#### Who added the Dataset to GEM?

<!-- info: Who contributed to the data card and adding the dataset to GEM? List the people+affiliations involved in creating this data card and who helped integrate this dataset into GEM. -->
<!-- scope: microscope -->
Genta Indra Winata (The Hong Kong University of Science and Technology)


### Dataset Structure




## Dataset in GEM

### Rationale for Inclusion in GEM

#### Similar Datasets

<!-- info: Do other datasets for the high level task exist? -->
<!-- scope: telescope -->
yes

#### Unique Language Coverage

<!-- info: Does this dataset cover other languages than other datasets for the same task? -->
<!-- scope: periscope -->
no


### GEM-Specific Curation

#### Modificatied for GEM?

<!-- info: Has the GEM version of the dataset been modified in any way (data, processing, splits) from the original curated data? -->
<!-- scope: telescope -->
yes

#### GEM Modifications

<!-- info: What changes have been made to he original dataset? -->
<!-- scope: periscope -->
`other`

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
Dialog understanding, summarization, translation

#### Metrics

<!-- info: What metrics are typically used for this task? -->
<!-- scope: periscope -->
`BLEU`

#### Proposed Evaluation

<!-- info: List and describe the purpose of the metrics and evaluation methodology (including human evaluation) that the dataset creators used when introducing this task. -->
<!-- scope: microscope -->
BLEU evaluates the generation quality.

#### Previous results available?

<!-- info: Are previous results available? -->
<!-- scope: telescope -->
yes

#### Other Evaluation Approaches

<!-- info: What evaluation approaches have others used? -->
<!-- scope: periscope -->
BLEU



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
`Crowdsourced`

#### Where was it crowdsourced?

<!-- info: If crowdsourced, where from? -->
<!-- scope: periscope -->
`Participatory experiment`

#### Data Validation

<!-- info: Was the text validated by a different worker or a data curator? -->
<!-- scope: telescope -->
validated by data curator

#### Was Data Filtered?

<!-- info: Were text instances selected or filtered? -->
<!-- scope: telescope -->
not filtered


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
Annotators agree using the dataset for research purpose.

#### Other Consented Downstream Use

<!-- info: What other downstream uses of the data did the original data creators and the data curators consent to? -->
<!-- scope: microscope -->
Any


### Private Identifying Information (PII)

#### Contains PII?

<!-- quick -->
<!-- info: Does the source language data likely contain Personal Identifying Information about the data creators or subjects? -->
<!-- scope: telescope -->
unlikely

#### Categories of PII

<!-- info: What categories of PII are present or suspected in the data? -->
<!-- scope: periscope -->
``


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
yes


### Discussion of Biases

#### Any Documented Social Biases?

<!-- info: Are there documented social biases in the dataset? Biases in this context are variations in the ways members of different social categories are represented that can have harmful downstream consequences for members of the more disadvantaged group. -->
<!-- scope: telescope -->
no



## Considerations for Using the Data

### PII Risks and Liability

#### Potential PII Risk

<!-- info: Considering your answers to the PII part of the Data Curation Section, describe any potential privacy to the data subjects and creators risks when using the dataset. -->
<!-- scope: microscope -->
No


### Licenses

#### Copyright Restrictions on the Dataset

<!-- info: Based on your answers in the Intended Use part of the Data Overview Section, which of the following best describe the copyright and licensing status of the dataset? -->
<!-- scope: periscope -->
`open license`

#### Copyright Restrictions on the Language Data

<!-- info: Based on your answers in the Language part of the Data Curation Section, which of the following best describe the copyright and licensing status of the underlying language data? -->
<!-- scope: periscope -->
`open license`


### Known Technical Limitations



