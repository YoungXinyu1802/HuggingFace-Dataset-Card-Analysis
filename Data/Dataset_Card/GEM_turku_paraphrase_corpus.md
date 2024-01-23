---
annotations_creators:
- expert-created
language_creators:
- unknown
language:
- fi
license:
- cc-by-sa-4.0
multilinguality:
- unknown
size_categories:
- unknown
source_datasets:
- original
task_categories:
- other
task_ids: []
pretty_name: turku_paraphrase_corpus
tags:
- paraphrasing
---

# Dataset Card for GEM/turku_paraphrase_corpus

## Dataset Description

- **Homepage:** https://turkunlp.org/paraphrase.html
- **Repository:** https://github.com/TurkuNLP/Turku-paraphrase-corpus
- **Paper:** https://aclanthology.org/2021.nodalida-main.29/
- **Leaderboard:** N/A
- **Point of Contact:** Jenna Kanerva, Filip Ginter

### Link to Main Data Card

You can find the main data card on the [GEM Website](https://gem-benchmark.com/data_cards/turku_paraphrase_corpus).

### Dataset Summary 

This is a Finnish paraphrase corpus which consists of pairs of text passages, where a typical passage is about a sentence long. It can be used to either identify or generate paraphrases.

You can load the dataset via:
```
import datasets
data = datasets.load_dataset('GEM/turku_paraphrase_corpus')
```
The data loader can be found [here](https://huggingface.co/datasets/GEM/turku_paraphrase_corpus).

#### website
[Website](https://turkunlp.org/paraphrase.html)

#### paper
[ACL Anthology](https://aclanthology.org/2021.nodalida-main.29/)

#### authors
Jenna Kanerva, Filip Ginter, Li-Hsin Chang, Iiro Rastas, Valtteri Skantsi, Jemina Kilpeläinen, Hanna-Mari Kupari, Aurora Piirto, Jenna Saarni, Maija Sevón, Otto Tarkka (TurkuNLP / University of Turku)

## Dataset Overview

### Where to find the Data and its Documentation

#### Webpage

<!-- info: What is the webpage for the dataset (if it exists)? -->
<!-- scope: telescope -->
[Website](https://turkunlp.org/paraphrase.html)

#### Download

<!-- info: What is the link to where the original dataset is hosted? -->
<!-- scope: telescope -->
[Github](https://github.com/TurkuNLP/Turku-paraphrase-corpus)

#### Paper

<!-- info: What is the link to the paper describing the dataset (open access preferred)? -->
<!-- scope: telescope -->
[ACL Anthology](https://aclanthology.org/2021.nodalida-main.29/)

#### BibTex

<!-- info: Provide the BibTex-formatted reference for the dataset. Please use the correct published version (ACL anthology, etc.) instead of google scholar created Bibtex. -->
<!-- scope: microscope -->
```
@inproceedings{kanerva-etal-2021-finnish,
    title = {Finnish Paraphrase Corpus},
    author = {Kanerva, Jenna and Ginter, Filip and Chang, Li-Hsin and Rastas, Iiro and Skantsi, Valtteri and Kilpel{\"a}inen, Jemina and Kupari, Hanna-Mari and Saarni, Jenna and Sev{\'o}n, Maija and Tarkka, Otto},
    booktitle = {Proceedings of the 23rd Nordic Conference on Computational Linguistics (NoDaLiDa'21)},
    year = {2021},
    publisher = {Link{\"o}ping University Electronic Press, Sweden},
    url = {https://aclanthology.org/2021.nodalida-main.29},
    pages = {288--298}
}
```

#### Contact Name

<!-- quick -->
<!-- info: If known, provide the name of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
Jenna Kanerva, Filip Ginter

#### Contact Email

<!-- info: If known, provide the email of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
jmnybl@utu.fi, figint@utu.fi

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

#### Covered Dialects

<!-- info: What dialects are covered? Are there multiple dialects per language? -->
<!-- scope: periscope -->
written standard language, spoken language

#### Covered Languages

<!-- quick -->
<!-- info: What languages/dialects are covered in the dataset? -->
<!-- scope: telescope -->
`Finnish`

#### License

<!-- quick -->
<!-- info: What is the license of the dataset? -->
<!-- scope: telescope -->
cc-by-sa-4.0: Creative Commons Attribution Share Alike 4.0 International

#### Intended Use

<!-- info: What is the intended use of the dataset? -->
<!-- scope: microscope -->
Paraphrase classification, paraphrase generation

#### Primary Task

<!-- info: What primary task does the dataset support? -->
<!-- scope: telescope -->
Paraphrasing

#### Communicative Goal

<!-- quick -->
<!-- info: Provide a short description of the communicative goal of a model trained for this task on this dataset. -->
<!-- scope: periscope -->
The corpus provides naturally occurring Finnish paraphrases striving for low lexical overlap, thus supporting many different downstream applications requiring language understanding. 


### Credit

#### Curation Organization Type(s)

<!-- info: In what kind of organization did the dataset curation happen? -->
<!-- scope: telescope -->
`academic`

#### Curation Organization(s)

<!-- info: Name the organization(s). -->
<!-- scope: periscope -->
University of Turku

#### Dataset Creators

<!-- info: Who created the original dataset? List the people involved in collecting the dataset and their affiliation(s). -->
<!-- scope: microscope -->
Jenna Kanerva, Filip Ginter, Li-Hsin Chang, Iiro Rastas, Valtteri Skantsi, Jemina Kilpeläinen, Hanna-Mari Kupari, Aurora Piirto, Jenna Saarni, Maija Sevón, Otto Tarkka (TurkuNLP / University of Turku)

#### Funding

<!-- info: Who funded the data creation? -->
<!-- scope: microscope -->
The Turku paraphrase corpus project was funded by the Academy of Finland, as well as the European Language Grid project through its open call for pilot projects. The European Language Grid project has received funding from the European Union’s Horizon 2020 Research and Innovation programme under Grant Agreement no. 825627 (ELG).

#### Who added the Dataset to GEM?

<!-- info: Who contributed to the data card and adding the dataset to GEM? List the people+affiliations involved in creating this data card and who helped integrate this dataset into GEM. -->
<!-- scope: microscope -->
Jenna Kanerva, Filip Ginter (TurkuNLP / University of Turku)


### Dataset Structure

#### Data Fields

<!-- info: List and describe the fields present in the dataset. -->
<!-- scope: telescope -->
The dataset consist of pairs of text passages, where a typical passage is about a sentence long, however, a passage may also be longer or shorter than a sentence. Thus, each example include two text passages (string), a manually annotated label to indicate the paraphrase type (string), and additional metadata.

The dataset include three different `modes`, plain, classification, and generation. The `plain` mode loads the original data without any additional preprocessing or transformations, while the `classification` mode directly builds the data in a form suitable for training a paraphrase classifier, where each example is doubled in the data with different directions (text1, text2, label) --> (text2, text1, label) taking care of the label flipping as well if needed (paraphrases with directionality flag < or >). In the `generation` mode, the examples are preprocessed to be directly suitable for paraphrase generation task. In here, paraphrases not suitable for generation are discarded (negative, and highly context-dependent paraphrases), and directional paraphrases are provided so that the generation goes from more detailed passage to the more general one in order to prevent model hallucination (i.e. model learning to introduce new information). The rest of the paraphrases are provided in both directions (text1, text2, label) --> (text2, text1, label).


Each pair in `plain` and `classification` mode will include fields:

`gem_id`: Identifier of the paraphrase pair (string)
`goeswith`: Identifier of the document from which the paraphrase was extracted, can be `not available` in case the source of the paraphrase is not from document-structured data (string)
`fold`: 0-99, data split into 100 parts respecting document boundaries, you can use this e.g. to implement crossvalidation safely as all paraphrases from one document are in one fold (int)
`text1`: First paraphrase passage (string)
`text2`: Second paraphrase passage (string)
`label`: Manually annotated labels (string)
`binary_label`: Label turned into binary with values `positive` (paraphrase) and `negative` (not-paraphrase) (string)
`is_rewrite`: Indicator whether the example is human produced rewrite or naturally occurring paraphrase (bool)

Each pair in `generation` mode will include the same fields expect `text1` and `text2` are renamed to `input` and `output` in order to indicate the generation direction. Thus the fields are:

`gem_id`: Identifier of the paraphrase pair (string)
`goeswith`: Identifier of the document from which the paraphrase was extracted, can be `not available` in case the source of the paraphrase is not from document-structured data (string)
`fold`: 0-99, data split into 100 parts respecting document boundaries, you can use this e.g. to implement crossvalidation safely as all paraphrases from one document are in one fold (int)
`input`: The input paraphrase passage for generation (string)
`output`: The output paraphrase passage for generation (string)
`label`: Manually annotated labels (string)
`binary_label`: Label turned into binary with values `positive` (paraphrase) and `negative` (not-paraphrase) (string)
`is_rewrite`: Indicator whether the example is human produced rewrite or naturally occurring paraphrase (bool)

#### Example Instance

<!-- info: Provide a JSON formatted example of a typical instance in the dataset. -->
<!-- scope: periscope -->
```
{
  'gem_id':  'gem-turku_paraphrase_corpus-train-15',
  'goeswith': 'episode-02243',
  'fold': 0,
  'text1': 'Mitä merkitystä sillä on?',
  'text2': 'Mitä väliä sillä edes on?',
  'label': '4',
  'binary_label': 'positive',
  'is_rewrite': False
}
```

#### Data Splits

<!-- info: Describe and name the splits in the dataset if there are more than one. -->
<!-- scope: periscope -->
The corpus include 3 splits: train, validation, and test.

#### Splitting Criteria

<!-- info: Describe any criteria for splitting the data, if used. If there are differences between the splits (e.g., if the training annotations are machine-generated and the dev and test ones are created by humans, or if different numbers of annotators contributed to each example), describe them here. -->
<!-- scope: microscope -->
The data is split randomly into the three section with a restriction of all paraphrases from the same document (movie, TV episode, news article, student translation, or exam question) being in the same section. All splits are manually annotated.



## Dataset in GEM

### Rationale for Inclusion in GEM

#### Why is the Dataset in GEM?

<!-- info: What does this dataset contribute toward better generation evaluation and why is it part of GEM? -->
<!-- scope: microscope -->
This dataset provides a large amount of high quality (manually collected and verified) paraphrases for Finnish.

#### Similar Datasets

<!-- info: Do other datasets for the high level task exist? -->
<!-- scope: telescope -->
yes

#### Unique Language Coverage

<!-- info: Does this dataset cover other languages than other datasets for the same task? -->
<!-- scope: periscope -->
no

#### Ability that the Dataset measures

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: periscope -->
natural language understanding, language variation


### GEM-Specific Curation

#### Modificatied for GEM?

<!-- info: Has the GEM version of the dataset been modified in any way (data, processing, splits) from the original curated data? -->
<!-- scope: telescope -->
yes

#### GEM Modifications

<!-- info: What changes have been made to he original dataset? -->
<!-- scope: periscope -->
`data points modified`

#### Modification Details

<!-- info: For each of these changes, described them in more details and provided the intended purpose of the modification -->
<!-- scope: microscope -->
Data structure is slightly simplified, and the release provides ready made transformations into two tasks (paraphrase classification and generation), where some data instances are doubled with different direction, and some are discarded as not being suitable for generation (e.g. negatives).

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
natural language understanding, language variation

#### Previous results available?

<!-- info: Are previous results available? -->
<!-- scope: telescope -->
yes

#### Other Evaluation Approaches

<!-- info: What evaluation approaches have others used? -->
<!-- scope: periscope -->
F-score in paraphrase classification



## Dataset Curation

### Original Curation

#### Original Curation Rationale

<!-- info: Original curation rationale -->
<!-- scope: telescope -->
The dataset is fully manually annotated. The dataset strives for interesting paraphrases with low lexical overlap, thus the annotation is two fold. First the paraphrases are manually extracted from two related documents, where the annotators are instructed to extract only interesting paraphrases. In the second phrase, all extracted paraphrases are manually labeled given the annotation scheme.

The annotation scheme is:
4 : paraphrase in all reasonably possible contexts
3 : paraphrase in the given document contexts, but not in general
2 : related but not paraphrase
During annotation also labels 1 (unrelated) and x (skip, e.g. wrong language) were used, however, the insignificant amount of examples annotated with these labels were discarded from the released corpus.

The following flags are annotated to label 4 paraphrases:
< : txt1 is more general than txt2; txt2 is more specific than txt1 (directional paraphrase where txt2 can be replaced with txt1 in all contexts but not to the other direction)
> : txt2 is more general than txt1; txt1 is more specific than txt2 (directional paraphrase where txt1 can be replaced with txt2 in all contexts but not to the other direction)
i : minor traceable difference (differing in terms of grammatical number or case, 'this' vs 'that', etc.)
s : style or strength difference (e.g. equivalent meaning, but one of the statements substantially more colloquial than the other)

For paraphrases where the annotated label was something else than label 4 without any flags, the annotators had an option to rewrite the text passages so that the rewritten paraphrase pair formed label 4 (universal) paraphrase. This was used for cases where simple edit would turn e.g. contextual or directional paraphrase into universal one. For the rewritten examples, both the original and the rewritten pairs are available with corresponding labels annotated.

#### Communicative Goal

<!-- info: What was the communicative goal? -->
<!-- scope: periscope -->
Representing text passages with identical meaning but different surface realization.

#### Sourced from Different Sources

<!-- info: Is the dataset aggregated from different data sources? -->
<!-- scope: telescope -->
yes

#### Source Details

<!-- info: List the sources (one per line) -->
<!-- scope: periscope -->
movie and TV series subtitles (82%)
news articles (9%)
discussion forum messages (8%)
university translation exercises  (1%)
university course essays and exams (<1%)


### Language Data

#### How was Language Data Obtained?

<!-- info: How was the language data obtained? -->
<!-- scope: telescope -->
`Found`, `Other`

#### Where was it found?

<!-- info: If found, where from? -->
<!-- scope: telescope -->
`Multiple websites`, `Offline media collection`, `Other`

#### Language Producers

<!-- info: What further information do we have on the language producers? -->
<!-- scope: microscope -->
The movie and TV series subtitles are extracted from OPUS OpenSubtitles2018 collection, which is based on data from [OpenSubtitles](http://www.opensubtitles.org/).
The news articles are collected from two Finnish news sites, YLE and HS, during years 2017-2020.
Discussion forum messages are obtained from the Finnish Suomi24 discussion forum released for academic use (http://urn.fi/urn:nbn:fi:lb-2020021801).
University translation exercises, essays and exams are collected during the project.

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
expert created

#### Number of Raters

<!-- info: What is the number of raters -->
<!-- scope: telescope -->
2<n<10

#### Rater Qualifications

<!-- info: Describe the qualifications required of an annotator. -->
<!-- scope: periscope -->
Members of the TurkuNLP research group, native speakers of Finnish, each annotator has a strong background in language studies by having an academic degree or ongoing studies in a field related to languages or linguistics.

#### Raters per Training Example

<!-- info: How many annotators saw each training example? -->
<!-- scope: periscope -->
1

#### Raters per Test Example

<!-- info: How many annotators saw each test example? -->
<!-- scope: periscope -->
1

#### Annotation Service?

<!-- info: Was an annotation service used? -->
<!-- scope: telescope -->
no

#### Annotation Values

<!-- info: Purpose and values for each annotation -->
<!-- scope: microscope -->
1. Manual extraction of interesting paraphrases from two related documents.
2. Manual labeling of each extracted paraphrase based on the given annotation scheme, e.g. distinguishing contextual and universal paraphrases, marking style or strength differences, etc.

#### Any Quality Control?

<!-- info: Quality control measures? -->
<!-- scope: telescope -->
validated by another rater

#### Quality Control Details

<!-- info: Describe the quality control measures that were taken. -->
<!-- scope: microscope -->
Partial double annotation, double annotation batches are assigned regularly in order to monitor annotation consistency. In double annotation, one annotator first extracts the candidate paraphrases, and these candidates are assigned to two different annotators, who does the label annotation independently from each other. Afterwards, the label annotations are merged, and conflicting labels are resolved together with the whole annotation team.


### Consent

#### Any Consent Policy?

<!-- info: Was there a consent policy involved when gathering the data? -->
<!-- scope: telescope -->
yes

#### Consent Policy Details

<!-- info: What was the consent policy? -->
<!-- scope: microscope -->
The corpus is mostly based on public/open data. For other data sources (student material), the licensing was agreed with the data providers during the collection.


### Private Identifying Information (PII)

#### Contains PII?

<!-- quick -->
<!-- info: Does the source language data likely contain Personal Identifying Information about the data creators or subjects? -->
<!-- scope: telescope -->
likely

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
no



## Considerations for Using the Data

### PII Risks and Liability

#### Potential PII Risk

<!-- info: Considering your answers to the PII part of the Data Curation Section, describe any potential privacy to the data subjects and creators risks when using the dataset. -->
<!-- scope: microscope -->
None


### Licenses

#### Copyright Restrictions on the Dataset

<!-- info: Based on your answers in the Intended Use part of the Data Overview Section, which of the following best describe the copyright and licensing status of the dataset? -->
<!-- scope: periscope -->
`open license - commercial use allowed`

#### Copyright Restrictions on the Language Data

<!-- info: Based on your answers in the Language part of the Data Curation Section, which of the following best describe the copyright and licensing status of the underlying language data? -->
<!-- scope: periscope -->
`open license - commercial use allowed`


### Known Technical Limitations



