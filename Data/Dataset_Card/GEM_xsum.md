---
annotations_creators:
- none
language_creators:
- unknown
language:
- en
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
pretty_name: xsum
---

# Dataset Card for GEM/xsum

## Dataset Description

- **Homepage:** n/a
- **Repository:** https://github.com/EdinburghNLP/XSum
- **Paper:** https://www.aclweb.org/anthology/D18-1206
- **Leaderboard:** N/A
- **Point of Contact:** Shashi Narayan

### Link to Main Data Card

You can find the main data card on the [GEM Website](https://gem-benchmark.com/data_cards/xsum).

### Dataset Summary 

XSum is an English news summarization dataset where the task is to predict the first sentence of an article from the rest of it.

You can load the dataset via:
```
import datasets
data = datasets.load_dataset('GEM/xsum')
```
The data loader can be found [here](https://huggingface.co/datasets/GEM/xsum).

#### website
n/a

#### paper
[ACL Anthology](https://www.aclweb.org/anthology/D18-1206)

#### authors
Shashi Narayan, Shay B. Cohen, Mirella Lapata (all affiliated with University of Edinburgh at the time of dataset creation)

## Dataset Overview

### Where to find the Data and its Documentation

#### Download

<!-- info: What is the link to where the original dataset is hosted? -->
<!-- scope: telescope -->
[Github](https://github.com/EdinburghNLP/XSum)

#### Paper

<!-- info: What is the link to the paper describing the dataset (open access preferred)? -->
<!-- scope: telescope -->
[ACL Anthology](https://www.aclweb.org/anthology/D18-1206)

#### BibTex

<!-- info: Provide the BibTex-formatted reference for the dataset. Please use the correct published version (ACL anthology, etc.) instead of google scholar created Bibtex. -->
<!-- scope: microscope -->
```
@InProceedings{xsum-emnlp,
  author =      "Shashi Narayan and Shay B. Cohen and Mirella Lapata",
  title =       "Don't Give Me the Details, Just the Summary! {T}opic-Aware Convolutional Neural Networks for Extreme Summarization",
  booktitle =   "Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing ",
  year =        "2018",
  address =     "Brussels, Belgium",
}
```

#### Contact Name

<!-- quick -->
<!-- info: If known, provide the name of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
Shashi Narayan

#### Contact Email

<!-- info: If known, provide the email of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
shashinarayan@google.com

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
Since the source of the dataset are BBC articles, the language is in British English of the variation written by journalists.

#### Covered Languages

<!-- quick -->
<!-- info: What languages/dialects are covered in the dataset? -->
<!-- scope: telescope -->
`English`

#### Whose Language?

<!-- info: Whose language is in the dataset? -->
<!-- scope: periscope -->
Professional journalists

#### License

<!-- quick -->
<!-- info: What is the license of the dataset? -->
<!-- scope: telescope -->
cc-by-sa-4.0: Creative Commons Attribution Share Alike 4.0 International

#### Intended Use

<!-- info: What is the intended use of the dataset? -->
<!-- scope: microscope -->
The dataset is for the task of abstractive summarization in its extreme form, its about summarizing a document in a single sentence. The idea is to create a short, one-sentence news summary answering the question "What is the article about?".



#### Primary Task

<!-- info: What primary task does the dataset support? -->
<!-- scope: telescope -->
Summarization

#### Communicative Goal

<!-- quick -->
<!-- info: Provide a short description of the communicative goal of a model trained for this task on this dataset. -->
<!-- scope: periscope -->
Given a news article, produce a single sentence summary of the content of the article. 


### Credit

#### Curation Organization Type(s)

<!-- info: In what kind of organization did the dataset curation happen? -->
<!-- scope: telescope -->
`academic`

#### Curation Organization(s)

<!-- info: Name the organization(s). -->
<!-- scope: periscope -->
University of Edinburgh

#### Dataset Creators

<!-- info: Who created the original dataset? List the people involved in collecting the dataset and their affiliation(s). -->
<!-- scope: microscope -->
Shashi Narayan, Shay B. Cohen, Mirella Lapata (all affiliated with University of Edinburgh at the time of dataset creation)

#### Funding

<!-- info: Who funded the data creation? -->
<!-- scope: microscope -->
European Research Council (Lapata; award number 681760), the European Union under the Horizon 2020 SUMMA project (Narayan, Cohen; grant agreement 688139), and Huawei Technologies (Cohen).

#### Who added the Dataset to GEM?

<!-- info: Who contributed to the data card and adding the dataset to GEM? List the people+affiliations involved in creating this data card and who helped integrate this dataset into GEM. -->
<!-- scope: microscope -->
The original data card was written by Laura Perez-Beltrachini and the data loader by Yacine Jernite. Sebastian Gehrmann migrated the data card to the new format and extended it. The v2 data loader was migrated by  Abinaya Mahendiran


### Dataset Structure

#### Data Fields

<!-- info: List and describe the fields present in the dataset. -->
<!-- scope: telescope -->
- `Document`: Input news article.
- `Summary`: One sentence summary of the article.
- `Id`: BBC ID of the article.

#### Reason for Structure

<!-- info: How was the dataset structure determined? -->
<!-- scope: microscope -->
The Document/Summary format is standard for summarization datasets.

#### How were labels chosen?

<!-- info: How were the labels chosen? -->
<!-- scope: microscope -->
The labels are the first sentence of the source article. 

#### Example Instance

<!-- info: Provide a JSON formatted example of a typical instance in the dataset. -->
<!-- scope: periscope -->
```
{
  'document': 'The researchers have sequenced the genome of a strain of bacterium that causes the virulent infection.\nA survey in 2007 showed that bleeding canker had spread rapidly, with almost half of the two million horse chestnuts displaying symptoms of the disease.\nThe findings have been published in the journal PLoS One.\nA visible symptom of the disease is a lesion on the bark, which oozes a resin on to the trunk or sometimes the branches.\nThe bark underneath the canker is killed, and if cankers manage to go all the way around the trunk then the horse chestnut (Aesculus hippocastanum) will die because it cuts off the food supply. [...]',
  'target': "A team of UK scientists hopes to shed light on the mysteries of bleeding canker, a disease that is threatening the nation's horse chestnut trees.",
}
```

#### Data Splits

<!-- info: Describe and name the splits in the dataset if there are more than one. -->
<!-- scope: periscope -->
| Section   | Number of Documents          |
| ------------- |:-------------:|
| Training     | 204,045 |
| Validation     | 11,332      |
| Testing | 11,334    |
| Total | 226k |

| Section       |  number of words| number of sentences |
| ------------- |:-------------:| :-------------:|
| Documents      | 431.07     | 19.77 |
| Summary    | 23.26      | 1.00 |


#### Splitting Criteria

<!-- info: Describe any criteria for splitting the data, if used. If there are differences between the splits (e.g., if the training annotations are machine-generated and the dev and test ones are created by humans, or if different numbers of annotators contributed to each example), describe them here. -->
<!-- scope: microscope -->
The identifiers in the URLs were used to randomly split the dataset into training (90%, 204,045), validation (5%, 11,332), and test (5%, 11,334) sets.



## Dataset Curation

### Original Curation

#### Original Curation Rationale

<!-- info: Original curation rationale -->
<!-- scope: telescope -->
Comparable datasets are often very extractive which is not a strategy that works for one-sentence summaries. The dataset curators thus created this dataset as a way to evaluate truly abstractive models

#### Communicative Goal

<!-- info: What was the communicative goal? -->
<!-- scope: periscope -->
Same as the communicative goal in GEM: A model should summarize a news article in a single sentence

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

#### Language Producers

<!-- info: What further information do we have on the language producers? -->
<!-- scope: microscope -->
The data was collected from articles between 2010 and 2017. No other information 

#### Topics Covered

<!-- info: Does the language in the dataset focus on specific topics? How would you describe them? -->
<!-- scope: periscope -->
The collected articles included the following topics: News, Politics, Sports, Weather, Business, Technology, Science, Health, Family, Education, Entertainment and Arts 

The dataset curators also used LDA to gain insight into this question and found that the following were the top keywords associated with each topic:

- **T1**:  charge, court, murder, police, arrest, guilty, sentence, boy, bail, space, crown, trial
- **T2**:   church, abuse, bishop, child, catholic, gay, pope, school, christian, priest, cardinal
- **T3**:  council, people, government, local, housing, home, house, property, city, plan, authority
- **T4**:   clinton, party, trump, climate, poll, vote, plaid, election, debate, change, candidate, campaign
- **T5**:   country, growth, report, business, export, fall, bank, security, economy, rise, global, inflation
- **T6**:  hospital, patient, trust, nhs, people, care, health, service, staff, report, review, system, child

#### Data Validation

<!-- info: Was the text validated by a different worker or a data curator? -->
<!-- scope: telescope -->
not validated

#### Data Preprocessing

<!-- info: How was the text data pre-processed? (Enter N/A if the text was not pre-processed) -->
<!-- scope: microscope -->
The text was extracted from the HTML of the webpage. No further processing was done.

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
The copyright license of the data allows reusing it for this purpose. 


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

#### Are the Language Producers Representative of the Language?

<!-- info: Does the distribution of language producers in the dataset accurately represent the full distribution of speakers of the language world-wide? If not, how does it differ? -->
<!-- scope: periscope -->
The language and content of the data is focused on news and language in the UK and as such not representative of the speakers world-wide. Existing selection biases of the BBC exist in this dataset.


