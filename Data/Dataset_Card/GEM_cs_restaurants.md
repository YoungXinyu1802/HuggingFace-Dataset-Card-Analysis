---
annotations_creators:
- none
language_creators:
- unknown
language:
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
- conversational
task_ids: []
pretty_name: cs_restaurants
tags:
- dialog-response-generation
---

# Dataset Card for GEM/cs_restaurants

## Dataset Description

- **Homepage:** n/a
- **Repository:** https://github.com/UFAL-DSG/cs_restaurant_dataset
- **Paper:** https://aclanthology.org/W19-8670/
- **Leaderboard:** N/A
- **Point of Contact:** Ondrej Dusek

### Link to Main Data Card

You can find the main data card on the [GEM Website](https://gem-benchmark.com/data_cards/cs_restaurants).

### Dataset Summary 

The Czech Restaurants dataset is a task oriented dialog dataset in which a model needs to verbalize a response that a service agent could provide which is specified through a series of dialog acts. The dataset originated as a translation of an English dataset to test the generation capabilities of an NLG system on a highly morphologically rich language like Czech. 

You can load the dataset via:
```
import datasets
data = datasets.load_dataset('GEM/cs_restaurants')
```
The data loader can be found [here](https://huggingface.co/datasets/GEM/cs_restaurants).

#### website
n/a

#### paper
[Github](https://aclanthology.org/W19-8670/)

#### authors
Ondrej Dusek and Filip Jurcicek

## Dataset Overview

### Where to find the Data and its Documentation

#### Download

<!-- info: What is the link to where the original dataset is hosted? -->
<!-- scope: telescope -->
[Github](https://github.com/UFAL-DSG/cs_restaurant_dataset)

#### Paper

<!-- info: What is the link to the paper describing the dataset (open access preferred)? -->
<!-- scope: telescope -->
[Github](https://aclanthology.org/W19-8670/)

#### BibTex

<!-- info: Provide the BibTex-formatted reference for the dataset. Please use the correct published version (ACL anthology, etc.) instead of google scholar created Bibtex. -->
<!-- scope: microscope -->
```
@inproceedings{cs_restaurants,
	address = {Tokyo, Japan},
	title = {Neural {Generation} for {Czech}: {Data} and {Baselines}},
	shorttitle = {Neural {Generation} for {Czech}},
	url = {https://www.aclweb.org/anthology/W19-8670/},
	urldate = {2019-10-18},
	booktitle = {Proceedings of the 12th {International} {Conference} on {Natural} {Language} {Generation} ({INLG} 2019)},
	author = {Dušek, Ondřej and Jurčíček, Filip},
	month = oct,
	year = {2019},
	pages = {563--574},
}
```

#### Contact Name

<!-- quick -->
<!-- info: If known, provide the name of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
Ondrej Dusek

#### Contact Email

<!-- info: If known, provide the email of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
odusek@ufal.mff.cuni.cz

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
No breakdown of dialects is provided. 

#### Covered Languages

<!-- quick -->
<!-- info: What languages/dialects are covered in the dataset? -->
<!-- scope: telescope -->
`Czech`

#### Whose Language?

<!-- info: Whose language is in the dataset? -->
<!-- scope: periscope -->
Six professional translators produced the outputs

#### License

<!-- quick -->
<!-- info: What is the license of the dataset? -->
<!-- scope: telescope -->
cc-by-sa-4.0: Creative Commons Attribution Share Alike 4.0 International

#### Intended Use

<!-- info: What is the intended use of the dataset? -->
<!-- scope: microscope -->
The dataset was created to test neural NLG systems in Czech and their ability to deal with rich morphology.



#### Primary Task

<!-- info: What primary task does the dataset support? -->
<!-- scope: telescope -->
Dialog Response Generation

#### Communicative Goal

<!-- quick -->
<!-- info: Provide a short description of the communicative goal of a model trained for this task on this dataset. -->
<!-- scope: periscope -->
Producing a text expressing the given intent/dialogue act and all and only the attributes specified in the input meaning representation.




### Credit

#### Curation Organization Type(s)

<!-- info: In what kind of organization did the dataset curation happen? -->
<!-- scope: telescope -->
`academic`

#### Curation Organization(s)

<!-- info: Name the organization(s). -->
<!-- scope: periscope -->
Charles University, Prague

#### Dataset Creators

<!-- info: Who created the original dataset? List the people involved in collecting the dataset and their affiliation(s). -->
<!-- scope: microscope -->
Ondrej Dusek and Filip Jurcicek

#### Funding

<!-- info: Who funded the data creation? -->
<!-- scope: microscope -->
This research was supported by the Charles University project PRIMUS/19/SCI/10 and by the Ministry of Education, Youth and Sports of the Czech Republic under the grant agreement LK11221. This work used using language resources distributed by the LINDAT/CLARIN project of the Ministry of Education, Youth and Sports of the Czech Republic (project LM2015071).

#### Who added the Dataset to GEM?

<!-- info: Who contributed to the data card and adding the dataset to GEM? List the people+affiliations involved in creating this data card and who helped integrate this dataset into GEM. -->
<!-- scope: microscope -->
Simon Mille wrote the initial data card and Yacine Jernite the data loader. Sebastian Gehrmann migrated the data card and loader to the v2 format. 


### Dataset Structure

#### Data Fields

<!-- info: List and describe the fields present in the dataset. -->
<!-- scope: telescope -->
The data is stored in a JSON or CSV format, with identical contents. The data has 4 fields:
* `da`: the input meaning representation/dialogue act (MR)
* `delex_da`: the input MR, delexicalized -- all slot values are replaced with placeholders, such as `X-name`
* `text`: the corresponding target natural language text (reference)
* `delex_text`: the target text, delexicalized (delexicalization is applied regardless of inflection)

In addition, the data contains a JSON file with all possible inflected forms for all slot values in the dataset (`surface_forms.json`).
Each slot -> value entry contains a list of inflected forms for the given value, with the base form (lemma), the inflected form, and
a [morphological tag](https://ufal.mff.cuni.cz/pdt/Morphology_and_Tagging/Doc/hmptagqr.html).

The same MR is often repeated multiple times with different synonymous reference texts.


#### Reason for Structure

<!-- info: How was the dataset structure determined? -->
<!-- scope: microscope -->
The data originated as a translation and localization of [Wen et al.'s SF restaurant](https://www.aclweb.org/anthology/D15-1199/) NLG dataset.


#### How were labels chosen?

<!-- info: How were the labels chosen? -->
<!-- scope: microscope -->
The input MRs were collected from [Wen et al.'s SF restaurant](https://www.aclweb.org/anthology/D15-1199/) NLG data
and localized by randomly replacing slot values (using a list of Prague restaurant names, neighborhoods etc.).

The generated slot values were then automatically replaced in reference texts in the data.


#### Example Instance

<!-- info: Provide a JSON formatted example of a typical instance in the dataset. -->
<!-- scope: periscope -->
```
{
  "input": "inform_only_match(food=Turkish,name='Švejk Restaurant',near='Charles Bridge',price_range=cheap)",
  "target": "Našla jsem pouze jednu levnou restauraci poblíž Karlova mostu , kde podávají tureckou kuchyni , Švejk Restaurant ."
}
```

#### Data Splits

<!-- info: Describe and name the splits in the dataset if there are more than one. -->
<!-- scope: periscope -->
| Property                       | Value |
|--------------------------------|-------|
| Total instances                | 5,192 |
| Unique MRs                     | 2,417 |
| Unique delexicalized instances | 2,752 |
| Unique delexicalized MRs       |   248 |

The data is split in a roughly 3:1:1 proportion into training, development and test sections, making sure no delexicalized MR
appears in two different parts. On the other hand, most DA types/intents are represented in all data parts.



#### Splitting Criteria

<!-- info: Describe any criteria for splitting the data, if used. If there are differences between the splits (e.g., if the training annotations are machine-generated and the dev and test ones are created by humans, or if different numbers of annotators contributed to each example), describe them here. -->
<!-- scope: microscope -->
The creators ensured that after delexicalization of the meaning representation there was no overlap between training and test. 

The data is split at a 3:1:1 rate between training, validation, and test.



## Dataset in GEM

### Rationale for Inclusion in GEM

#### Why is the Dataset in GEM?

<!-- info: What does this dataset contribute toward better generation evaluation and why is it part of GEM? -->
<!-- scope: microscope -->
This is one of a few non-English data-to-text datasets, in a well-known domain, but covering a morphologically rich language that is harder to generate since named entities need to be inflected. This makes it harder to apply common techniques such as delexicalization or copy mechanisms.



#### Similar Datasets

<!-- info: Do other datasets for the high level task exist? -->
<!-- scope: telescope -->
yes

#### Unique Language Coverage

<!-- info: Does this dataset cover other languages than other datasets for the same task? -->
<!-- scope: periscope -->
yes

#### Difference from other GEM datasets

<!-- info: What else sets this dataset apart from other similar datasets in GEM? -->
<!-- scope: microscope -->
The dialog acts in this dataset are much more varied than the e2e dataset which is the closest in style. 

#### Ability that the Dataset measures

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: periscope -->
surface realization


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
5 challenge sets for the Czech Restaurants dataset were added to the GEM evaluation suite.

1. Data shift: We created subsets of the training and development sets of 500 randomly selected inputs each.
2. Scrambling: We applied input scrambling on a subset of 500 randomly selected test instances; the order of the input dialogue acts was randomly reassigned.
3. We identified different subsets of the test set that we could compare to each other so that we would have a better understanding of the results. There are currently two selections that we have made:

The first comparison is based on input size: the number of predicates differs between different inputs, ranging from 1 to 5.
The table below provides an indication of the distribution of inputs with a particular length.
It is clear from the table that this distribution is not balanced, and comparisions between items should be done with caution. 
Particularly for input size 4 and 5, there may not be enough data to draw reliable conclusions.

| Input length | Number of inputs |
|--------------|------------------|
| 1            |              183 |
| 2            |              267 |
| 3            |              297 |
| 4            |               86 |
| 5            |                9 |

The second comparison is based on the type of act. Again we caution against comparing the different groups that have relatively few items.
It is probably OK to compare `inform` and `?request`, but the other acts are all low-frequent.

| Act               | Frequency |
|-------------------|-----------|
| ?request          |       149 |
| inform            |       609 |
| ?confirm          |        22 |
| inform_only_match |        16 |
| inform_no_match   |        34 |
| ?select           |        12 |






#### Split Motivation

<!-- info: What aspects of the model's generation capacities were the splits created to test? -->
<!-- scope: periscope -->
Generalization and robustness.


### Getting Started with the Task

#### Technical Terms

<!-- info: Technical terms used in this card and the dataset and their definitions -->
<!-- scope: microscope -->
- utterance: something a system or user may say in a turn
- meaning representation: a representation of meaning that the system should be in accordance with. The specific type of MR in this dataset are dialog acts which describe what a dialog system should do, e.g., inform a user about a value. 




## Previous Results

### Previous Results

#### Measured Model Abilities

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: telescope -->
Surface realization

#### Metrics

<!-- info: What metrics are typically used for this task? -->
<!-- scope: periscope -->
`BLEU`, `ROUGE`, `METEOR`

#### Proposed Evaluation

<!-- info: List and describe the purpose of the metrics and evaluation methodology (including human evaluation) that the dataset creators used when introducing this task. -->
<!-- scope: microscope -->
This dataset uses the suite of word-overlap-based automatic metrics from the E2E NLG Challenge (BLEU, NIST, ROUGE-L, METEOR, and CIDEr). In addition, the slot error rate is measured. 

#### Previous results available?

<!-- info: Are previous results available? -->
<!-- scope: telescope -->
no



## Dataset Curation

### Original Curation

#### Original Curation Rationale

<!-- info: Original curation rationale -->
<!-- scope: telescope -->
The dataset was created to test neural NLG systems in Czech and their ability to deal with rich morphology.



#### Communicative Goal

<!-- info: What was the communicative goal? -->
<!-- scope: periscope -->
Producing a text expressing the given intent/dialogue act and all and only the attributes specified in the input MR.



#### Sourced from Different Sources

<!-- info: Is the dataset aggregated from different data sources? -->
<!-- scope: telescope -->
no


### Language Data

#### How was Language Data Obtained?

<!-- info: How was the language data obtained? -->
<!-- scope: telescope -->
`Created for the dataset`

#### Creation Process

<!-- info: If created for the dataset, describe the creation process. -->
<!-- scope: microscope -->
Six professional translators translated the underlying dataset with the following instructions: 

- Each utterance should be translated by itself
- fluent spoken-style Czech should be produced
- Facts should be preserved
- If possible, synonyms should be varied to create diverse utterances
- Entity names should be inflected as necessary
- the reader of the generated text should be addressed using formal form and self-references should use the female form.

The translators did not have access to the meaning representation.

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
no

#### Justification for Using the Data

<!-- info: If not, what is the justification for reusing the data? -->
<!-- scope: microscope -->
It was not explicitly stated but we can safely assume that the translators agreed to this use of their data. 


### Private Identifying Information (PII)

#### Contains PII?

<!-- quick -->
<!-- info: Does the source language data likely contain Personal Identifying Information about the data creators or subjects? -->
<!-- scope: telescope -->
no PII

#### Justification for no PII

<!-- info: Provide a justification for selecting `no PII` above. -->
<!-- scope: periscope -->
This dataset does not include any information about individuals.


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
The dataset may help improve NLG methods for morphologically rich languages beyond Czech.




### Discussion of Biases

#### Any Documented Social Biases?

<!-- info: Are there documented social biases in the dataset? Biases in this context are variations in the ways members of different social categories are represented that can have harmful downstream consequences for members of the more disadvantaged group. -->
<!-- scope: telescope -->
yes

#### Links and Summaries of Analysis Work

<!-- info: Provide links to and summaries of works analyzing these biases. -->
<!-- scope: microscope -->
To ensure consistency of translation, the data always uses formal/polite address for the user, and uses the female form for first-person self-references (as if the dialogue agent producing the sentences was female). This prevents data sparsity and ensures consistent results for systems trained on the dataset, but does not represent all potential situations arising in Czech.





## Considerations for Using the Data

### PII Risks and Liability



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

#### Technical Limitations

<!-- info: Describe any known technical limitations, such as spurrious correlations, train/test overlap, annotation biases, or mis-annotations, and cite the works that first identified these limitations when possible. -->
<!-- scope: microscope -->
The test set may lead users to over-estimate the performance of their NLG systems with respect to their generalisability, because there are no unseen restaurants or addresses in the test set. This is something we will look into for future editions of the GEM shared task.




