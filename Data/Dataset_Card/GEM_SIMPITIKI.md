---
annotations_creators:
- crowd-sourced
language_creators:
- unknown
language:
- it
license:
- cc-by-4.0
multilinguality:
- unknown
size_categories:
- unknown
source_datasets:
- original
task_categories:
- text2text-generation
task_ids:
- text-simplification
pretty_name: SIMPITIKI
---

# Dataset Card for GEM/SIMPITIKI

## Dataset Description

- **Homepage:** https://github.com/dhfbk/simpitiki
- **Repository:** https://github.com/dhfbk/simpitiki/tree/master/corpus
- **Paper:** http://ceur-ws.org/Vol-1749/paper52.pdf
- **Leaderboard:** N/A
- **Point of Contact:** Sara Tonelli

### Link to Main Data Card

You can find the main data card on the [GEM Website](https://gem-benchmark.com/data_cards/SIMPITIKI).

### Dataset Summary 

SIMPITIKI is an Italian Simplification dataset. Its examples were selected from Italian Wikipedia such that their editing tracking descriptions contain any of the words "Simplified"/"Simplify"/"Simplification". 

You can load the dataset via:
```
import datasets
data = datasets.load_dataset('GEM/SIMPITIKI')
```
The data loader can be found [here](https://huggingface.co/datasets/GEM/SIMPITIKI).

#### website
[Github](https://github.com/dhfbk/simpitiki)

#### paper
[Website](http://ceur-ws.org/Vol-1749/paper52.pdf)

#### authors
Sara Tonelli (Fondazione Bruno Kessler), Alessio Palmero Aprosio (Fondazione Bruno Kessler), Francesca Saltori (Fondazione Bruno Kessler)

## Dataset Overview

### Where to find the Data and its Documentation

#### Webpage

<!-- info: What is the webpage for the dataset (if it exists)? -->
<!-- scope: telescope -->
[Github](https://github.com/dhfbk/simpitiki)

#### Download

<!-- info: What is the link to where the original dataset is hosted? -->
<!-- scope: telescope -->
[Github](https://github.com/dhfbk/simpitiki/tree/master/corpus)

#### Paper

<!-- info: What is the link to the paper describing the dataset (open access preferred)? -->
<!-- scope: telescope -->
[Website](http://ceur-ws.org/Vol-1749/paper52.pdf)

#### BibTex

<!-- info: Provide the BibTex-formatted reference for the dataset. Please use the correct published version (ACL anthology, etc.) instead of google scholar created Bibtex. -->
<!-- scope: microscope -->
```
@article{tonelli2016simpitiki,
  title={SIMPITIKI: a Simplification corpus for Italian},
  author={Tonelli, Sara and Aprosio, Alessio Palmero and Saltori, Francesca},
  journal={Proceedings of CLiC-it},
  year={2016}
}
```

#### Contact Name

<!-- quick -->
<!-- info: If known, provide the name of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
Sara Tonelli

#### Contact Email

<!-- info: If known, provide the email of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
satonelli@fbk.eu

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
None

#### Covered Languages

<!-- quick -->
<!-- info: What languages/dialects are covered in the dataset? -->
<!-- scope: telescope -->
`Italian`

#### License

<!-- quick -->
<!-- info: What is the license of the dataset? -->
<!-- scope: telescope -->
cc-by-4.0: Creative Commons Attribution 4.0 International

#### Intended Use

<!-- info: What is the intended use of the dataset? -->
<!-- scope: microscope -->
The purpose of the dataset is to train NLG models to simplify complex text by learning different types of transformations (verb to noun, noun to verbs, deletion, insertion, etc)

#### Primary Task

<!-- info: What primary task does the dataset support? -->
<!-- scope: telescope -->
Simplification

#### Communicative Goal

<!-- quick -->
<!-- info: Provide a short description of the communicative goal of a model trained for this task on this dataset. -->
<!-- scope: periscope -->
This dataset aims to enhance research in text simplification in Italian language with different text transformations.


### Credit

#### Curation Organization Type(s)

<!-- info: In what kind of organization did the dataset curation happen? -->
<!-- scope: telescope -->
`academic`, `independent`

#### Curation Organization(s)

<!-- info: Name the organization(s). -->
<!-- scope: periscope -->
Fondazione Bruno Kessler (FBK)

#### Dataset Creators

<!-- info: Who created the original dataset? List the people involved in collecting the dataset and their affiliation(s). -->
<!-- scope: microscope -->
Sara Tonelli (Fondazione Bruno Kessler), Alessio Palmero Aprosio (Fondazione Bruno Kessler), Francesca Saltori (Fondazione Bruno Kessler)

#### Funding

<!-- info: Who funded the data creation? -->
<!-- scope: microscope -->
EU Horizon 2020 Programme via the SIMPATICO Project (H2020-EURO-6-2015, n. 692819)

#### Who added the Dataset to GEM?

<!-- info: Who contributed to the data card and adding the dataset to GEM? List the people+affiliations involved in creating this data card and who helped integrate this dataset into GEM. -->
<!-- scope: microscope -->
Sebastien Montella (Orange Labs), Vipul Raheja (Grammarly Inc.)


### Dataset Structure

#### Data Fields

<!-- info: List and describe the fields present in the dataset. -->
<!-- scope: telescope -->
Each sample comes with the following fields:

- `gem_id` (string): Unique sample ID
-`text` (string): The raw text to be simplified
-`simplified_text` (string): The simplified version of "text" field
-`transformation_type` (string): Nature of transformation applied to raw text in order to simplify it.
-`source_dataset` (string): Initial dataset source of sample. Values: 'itwiki' (for Italian Wikipedia) or 'tn' (manually annotated administrative documents from the Municipality of Trento, Italy)

#### Reason for Structure

<!-- info: How was the dataset structure determined? -->
<!-- scope: microscope -->
The dataset is organized as a pairs where the raw text (input) is associated with its simplified text (output). The editing transformation and the source dataset of each sample is also provided for advanced analysis.

#### How were labels chosen?

<!-- info: How were the labels chosen? -->
<!-- scope: microscope -->
SIMPITIKI dataset selects documents from Italian Wikipedia such that their editing tracking descriptions contain any of the words "Simplified"/"Simplify"/"Simplification".  For the Public Administration domain of the documents of the Municipality of Trento (Italy)

#### Example Instance

<!-- info: Provide a JSON formatted example of a typical instance in the dataset. -->
<!-- scope: periscope -->
```
{"transformation_id": 31, "transformation_type": "Transformation - Lexical Substitution (word level)", "source_dataset": "tn", "text": "- assenza per <del>e</del>si<del>genze</del> particolari attestate da relazione dei servizi sociali;", "simplified_text": "- assenza per <ins>bi</ins>s<ins>ogn</ins>i particolari attestati da relazione dei servizi sociali;"}
```

#### Data Splits

<!-- info: Describe and name the splits in the dataset if there are more than one. -->
<!-- scope: periscope -->
Several splits are proposed to train models on different configurations:

-"train": Training samples randomly selected from initial corpus. 816 training samples.
-"validation": Validating samples randomly selected from initial corpus. 174 validating samples.
-"test": Testing samples randomly selected from initial corpus. 176 validating samples.
-"challenge_seen_transformations_train": This training challenge split includes specific transformations to simplify the raw text. Precisely, transformations are "Split", "Merge", "Reordering", "Insert - Verb", "Insert - Other", "Delete - Verb", "Delete - Other", "Transformation - Lexical Substitution (word level)", "Transformation - Anaphoric replacement", "Transformation - Noun to Verb", "Transformation - Verbal Features". 562 training samples.
-"challenge_seen_transformations_val": This validating challenge split includes same transformations than the ones observed in training. Precisely, transformations are "Split", "Merge", "Reordering", "Insert - Verb", "Insert - Other", "Delete - Verb", "Delete - Other", "Transformation - Lexical Substitution (word level)", "Transformation - Anaphoric replacement", "Transformation - Noun to Verb", "Transformation - Verbal Features". 121 validating samples.
-"challenge_seen_transformations_test": This testing challenge split includes same transformations than the ones observed in training. Precisely, transformations are "Split", "Merge", "Reordering", "Insert - Verb", "Insert - Other", "Delete - Verb", "Delete - Other", "Transformation - Lexical Substitution (word level)", "Transformation - Anaphoric replacement", "Transformation - Noun to Verb", "Transformation - Verbal Features". 127 testing samples.
-"challenge_unseen_transformations_test" : "Insert - Subject", "Delete - Subject", "Transformation - Lexical Substitution (phrase level)", "Transformation - Verb to Noun (nominalization)", "Transformation - Verbal Voice". 356 testing samples.
-"challenge_itwiki_train": This challenge split includes random samples from the Italian Wikipedia as source dataset. 402 training samples.
-"challenge_itwiki_val": This validating challenge split includes random samples from the Italian Wikipedia as source dataset. 86 validating samples.
-"challenge_itwiki_test": This testing challenge split includes random samples from the Italian Wikipedia as source dataset. 87 testing samples.
-"challenge_tn_test": This testing challenge split includes all samples from the Municipality of Trento administrative documents ('tn') as source dataset. 591 testing samples.





#### Splitting Criteria

<!-- info: Describe any criteria for splitting the data, if used. If there are differences between the splits (e.g., if the training annotations are machine-generated and the dev and test ones are created by humans, or if different numbers of annotators contributed to each example), describe them here. -->
<!-- scope: microscope -->
The training ratio is set to 0.7. The validation and test somehow equally divide the remaining 30% of the dataset. 



## Dataset in GEM

### Rationale for Inclusion in GEM

#### Why is the Dataset in GEM?

<!-- info: What does this dataset contribute toward better generation evaluation and why is it part of GEM? -->
<!-- scope: microscope -->
This dataset promotes Simplification task for Italian language.

#### Similar Datasets

<!-- info: Do other datasets for the high level task exist? -->
<!-- scope: telescope -->
no

#### Ability that the Dataset measures

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: periscope -->
Models can be evaluated if they can simplify text regarding different simplification transformations.


### GEM-Specific Curation

#### Modificatied for GEM?

<!-- info: Has the GEM version of the dataset been modified in any way (data, processing, splits) from the original curated data? -->
<!-- scope: telescope -->
yes

#### Additional Splits?

<!-- info: Does GEM provide additional splits to the dataset? -->
<!-- scope: telescope -->
yes

#### Split Information

<!-- info: Describe how the new splits were created -->
<!-- scope: periscope -->
The SIMPITIKI dataset provides a single file. Several splits are proposed to train models on different configurations:
-"train": Training samples randomly selected from initial corpus. 816 training samples.
-"validation": Validating samples randomly selected from initial corpus. 174 validating samples.
-"test": Testing samples randomly selected from initial corpus. 176 validating samples.
-"challenge_seen_transformations_train": This training challenge split includes specific transformations to simplify the raw text. Precisely, transformations are "Split", "Merge", "Reordering", "Insert - Verb", "Insert - Other", "Delete - Verb", "Delete - Other", "Transformation - Lexical Substitution (word level)", "Transformation - Anaphoric replacement", "Transformation - Noun to Verb", "Transformation - Verbal Features". 562 training samples.
-"challenge_seen_transformations_val": This validating challenge split includes same transformations than the ones observed in training. Precisely, transformations are "Split", "Merge", "Reordering", "Insert - Verb", "Insert - Other", "Delete - Verb", "Delete - Other", "Transformation - Lexical Substitution (word level)", "Transformation - Anaphoric replacement", "Transformation - Noun to Verb", "Transformation - Verbal Features". 121 validating samples.
-"challenge_seen_transformations_test": This testing challenge split includes same transformations than the ones observed in training. Precisely, transformations are "Split", "Merge", "Reordering", "Insert - Verb", "Insert - Other", "Delete - Verb", "Delete - Other", "Transformation - Lexical Substitution (word level)", "Transformation - Anaphoric replacement", "Transformation - Noun to Verb", "Transformation - Verbal Features". 127 testing samples.
-"challenge_unseen_transformations_test" : "Insert - Subject", "Delete - Subject", "Transformation - Lexical Substitution (phrase level)", "Transformation - Verb to Noun (nominalization)", "Transformation - Verbal Voice". 356 testing samples.
-"challenge_itwiki_train": This challenge split includes random samples from the Italian Wikipedia as source dataset. 402 training samples.
-"challenge_itwiki_val": This validating challenge split includes random samples from the Italian Wikipedia as source dataset. 86 validating samples.
-"challenge_itwiki_test": This testing challenge split includes random samples from the Italian Wikipedia as source dataset. 87 testing samples.
-"challenge_tn_test": This testing challenge split includes all samples from the Municipality of Trento administrative documents ('tn') as source dataset. 591 testing samples.





#### Split Motivation

<!-- info: What aspects of the model's generation capacities were the splits created to test? -->
<!-- scope: periscope -->
The splits allows to investigate the generalization of models regarding editing/transformations ("challenge_seen_transformations_test" / "challenge_unseen_transformations_test") and for transfer learning to different domain ("challenge_tn_test")


### Getting Started with the Task

#### Pointers to Resources

<!-- info: Getting started with in-depth research on the task. Add relevant pointers to resources that researchers can consult when they want to get started digging deeper into the task. -->
<!-- scope: microscope -->
- Coster and Kauchak, Simple English Wikipedia: A New Text Simplification Task, Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics, pages 665–669, Portland, Oregon, June 19-24, 2011
- Xu et al, Optimizing Statistical Machine Translation for Text Simplification, Transactions of the Association for Computational Linguistics, vol. 4, pp. 401–415, 2016
- Aprosio et al, Neural Text Simplification in Low-Resource Conditions Using Weak Supervision, Proceedings of the Workshop on Methods for Optimizing and Evaluating Neural Language Generation (NeuralGen), pages 37–44, Minneapolis, Minnesota, USA, June 6, 2019


#### Technical Terms

<!-- info: Technical terms used in this card and the dataset and their definitions -->
<!-- scope: microscope -->
Simplification: Process that consists in transforming an input text to its simplified version.




## Previous Results

### Previous Results

#### Measured Model Abilities

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: telescope -->
The splits allows to investigate the generalization of models regarding editing/transformations ("challenge_seen_transformations_test" / "challenge_unseen_transformations_test") and for transfer learning to different domain ("challenge_tn_test")

#### Metrics

<!-- info: What metrics are typically used for this task? -->
<!-- scope: periscope -->
`BLEU`, `Other: Other Metrics`

#### Other Metrics

<!-- info: Definitions of other metrics -->
<!-- scope: periscope -->
FKBLEU (https://aclanthology.org/Q16-1029.pdf): Combines Flesch-Kincaid Index and iBLEU metrics.
SARI (https://aclanthology.org/Q16-1029.pdf): Compares system output against references and against the input sentence. It explicitly measures the goodness of words that are added, deleted and kept by the systems 
Word-level F1



#### Previous results available?

<!-- info: Are previous results available? -->
<!-- scope: telescope -->
no



## Dataset Curation

### Original Curation

#### Original Curation Rationale

<!-- info: Original curation rationale -->
<!-- scope: telescope -->
Most of the resources for Text Simplification are in English. To stimulate research to different languages, SIMPITIKI proposes an Italian corpus  with Complex-Simple sentence pairs. 

#### Communicative Goal

<!-- info: What was the communicative goal? -->
<!-- scope: periscope -->
Text simplification allows a smooth reading of text to enhance understanding.

#### Sourced from Different Sources

<!-- info: Is the dataset aggregated from different data sources? -->
<!-- scope: telescope -->
yes

#### Source Details

<!-- info: List the sources (one per line) -->
<!-- scope: periscope -->
Italian Wikipedia
(Manually) Annotated administrative documents from the Municipality of Trento, Italy


### Language Data

#### How was Language Data Obtained?

<!-- info: How was the language data obtained? -->
<!-- scope: telescope -->
`Found`

#### Where was it found?

<!-- info: If found, where from? -->
<!-- scope: telescope -->
`Single website`, `Offline media collection`

#### Language Producers

<!-- info: What further information do we have on the language producers? -->
<!-- scope: microscope -->
SIMPITIKI is a combination of documents from Italian Wikipedia and from the Municipality of Trento, Italy.


#### Topics Covered

<!-- info: Does the language in the dataset focus on specific topics? How would you describe them? -->
<!-- scope: periscope -->
Samples from documents from the Municipality of Trento corpus are in the administrative domain.

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
crowd-sourced

#### Number of Raters

<!-- info: What is the number of raters -->
<!-- scope: telescope -->
unknown

#### Rater Qualifications

<!-- info: Describe the qualifications required of an annotator. -->
<!-- scope: periscope -->
Native speaker

#### Raters per Training Example

<!-- info: How many annotators saw each training example? -->
<!-- scope: periscope -->
0

#### Raters per Test Example

<!-- info: How many annotators saw each test example? -->
<!-- scope: periscope -->
0

#### Annotation Service?

<!-- info: Was an annotation service used? -->
<!-- scope: telescope -->
unknown

#### Annotation Values

<!-- info: Purpose and values for each annotation -->
<!-- scope: microscope -->
Annotators specified any of the tags as designed by Brunato et al. (https://aclanthology.org/W15-1604/):
-Split: Splitting a clause into two clauses.
-Merge: Merge two or more clauses together.
-Reordering:  Word order changes.
-Insert: Insertion of words or phrases that provide supportive information to the original sentence
-Delete: dropping redundant information.
-Transformation: Modification which can affect the sentence at the lexical, morpho-syntactic and syntactic level: Lexical substitution (word level) / Lexical substitution (phrase level) / Anaphoric replacement / Noun to Verb / Verb to Noun / Verbal voice / Verbal features/ morpho–syntactic and syntactic level, also giving rise to overlapping phenomena



#### Any Quality Control?

<!-- info: Quality control measures? -->
<!-- scope: telescope -->
unknown


### Consent

#### Any Consent Policy?

<!-- info: Was there a consent policy involved when gathering the data? -->
<!-- scope: telescope -->
no

#### Justification for Using the Data

<!-- info: If not, what is the justification for reusing the data? -->
<!-- scope: microscope -->
The dataset is available online under the CC-BY 4.0 license.


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
yes

#### Details on how Dataset Addresses the Needs

<!-- info: Describe how this dataset addresses the needs of underserved communities. -->
<!-- scope: microscope -->
The creator of SIMPITIKI wants to promote text simplification for Italian because few resources are available in other languages than English.


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
`research use only`

#### Copyright Restrictions on the Language Data

<!-- info: Based on your answers in the Language part of the Data Curation Section, which of the following best describe the copyright and licensing status of the underlying language data? -->
<!-- scope: periscope -->
`research use only`


### Known Technical Limitations

#### Discouraged Use Cases

<!-- info: What are some discouraged use cases of a model trained to maximize the proposed metrics on this dataset? In particular, think about settings where decisions made by a model that performs reasonably well on the metric my still have strong negative consequences for user or members of the public. -->
<!-- scope: microscope -->
The risk of surface-based metrics (BLEU, chrf++, etc) for this task is that semantic adequacy is not respected when simplifying the input document.


