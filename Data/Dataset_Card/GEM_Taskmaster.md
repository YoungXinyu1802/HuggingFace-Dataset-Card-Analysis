---
annotations_creators:
- none
language_creators:
- unknown
language:
- en
license:
- cc-by-4.0
multilinguality:
- unknown
size_categories:
- unknown
source_datasets:
- original
task_categories:
- conversational
task_ids: []
pretty_name: Taskmaster
tags:
- dialog-response-generation
---

# Dataset Card for GEM/Taskmaster

## Dataset Description

- **Homepage:** https://github.com/google-research-datasets/Taskmaster/tree/master/TM-3-2020
- **Repository:** https://github.com/google-research-datasets/Taskmaster/tree/master/TM-3-2020
- **Paper:** https://arxiv.org/abs/2012.12458
- **Leaderboard:** N/A
- **Point of Contact:** Karthik Krishnamoorthi

### Link to Main Data Card

You can find the main data card on the [GEM Website](https://gem-benchmark.com/data_cards/Taskmaster).

### Dataset Summary 

This is a large task-oriented dialog dataset in which a model has to produce the response. The input contains the context and a structured representation of what the model is supposed to generate. The input is already pre-formatted as string, turning this into a pure text-to-text problem. 

You can load the dataset via:
```
import datasets
data = datasets.load_dataset('GEM/Taskmaster')
```
The data loader can be found [here](https://huggingface.co/datasets/GEM/Taskmaster).

#### website
[Github](https://github.com/google-research-datasets/Taskmaster/tree/master/TM-3-2020)

#### paper
[Arxiv](https://arxiv.org/abs/2012.12458)

#### authors
Google researchers

## Dataset Overview

### Where to find the Data and its Documentation

#### Webpage

<!-- info: What is the webpage for the dataset (if it exists)? -->
<!-- scope: telescope -->
[Github](https://github.com/google-research-datasets/Taskmaster/tree/master/TM-3-2020)

#### Download

<!-- info: What is the link to where the original dataset is hosted? -->
<!-- scope: telescope -->
[Github](https://github.com/google-research-datasets/Taskmaster/tree/master/TM-3-2020)

#### Paper

<!-- info: What is the link to the paper describing the dataset (open access preferred)? -->
<!-- scope: telescope -->
[Arxiv](https://arxiv.org/abs/2012.12458)

#### BibTex

<!-- info: Provide the BibTex-formatted reference for the dataset. Please use the correct published version (ACL anthology, etc.) instead of google scholar created Bibtex. -->
<!-- scope: microscope -->
```
@article{byrne2020tickettalk,
  title={TicketTalk: Toward human-level performance with end-to-end, transaction-based dialog systems},
  author={Byrne, Bill and Krishnamoorthi, Karthik and Ganesh, Saravanan and Kale, Mihir Sanjay},
  journal={arXiv preprint arXiv:2012.12458},
  year={2020}
}
```

#### Contact Name

<!-- quick -->
<!-- info: If known, provide the name of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
Karthik Krishnamoorthi

#### Contact Email

<!-- info: If known, provide the email of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
krishnamoorthi@google.com

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
NA

#### Covered Languages

<!-- quick -->
<!-- info: What languages/dialects are covered in the dataset? -->
<!-- scope: telescope -->
`English`

#### Whose Language?

<!-- info: Whose language is in the dataset? -->
<!-- scope: periscope -->
NA

#### License

<!-- quick -->
<!-- info: What is the license of the dataset? -->
<!-- scope: telescope -->
cc-by-4.0: Creative Commons Attribution 4.0 International

#### Intended Use

<!-- info: What is the intended use of the dataset? -->
<!-- scope: microscope -->
Dialogues

#### Primary Task

<!-- info: What primary task does the dataset support? -->
<!-- scope: telescope -->
Dialog Response Generation

#### Communicative Goal

<!-- quick -->
<!-- info: Provide a short description of the communicative goal of a model trained for this task on this dataset. -->
<!-- scope: periscope -->
a movie ticketing dialog dataset with 23,789 annotated conversations. 


### Credit

#### Curation Organization Type(s)

<!-- info: In what kind of organization did the dataset curation happen? -->
<!-- scope: telescope -->
`other`

#### Curation Organization(s)

<!-- info: Name the organization(s). -->
<!-- scope: periscope -->
NA

#### Dataset Creators

<!-- info: Who created the original dataset? List the people involved in collecting the dataset and their affiliation(s). -->
<!-- scope: microscope -->
Google researchers

#### Funding

<!-- info: Who funded the data creation? -->
<!-- scope: microscope -->
Google

#### Who added the Dataset to GEM?

<!-- info: Who contributed to the data card and adding the dataset to GEM? List the people+affiliations involved in creating this data card and who helped integrate this dataset into GEM. -->
<!-- scope: microscope -->
Tosin Adewumi (Luleå University of Technology)


### Dataset Structure

#### Data Fields

<!-- info: List and describe the fields present in the dataset. -->
<!-- scope: telescope -->
- `gem_id`: The unique example id
- `context`: The context of the conversation
- `target`: A string representing the target
-`references`: A List representing the target(s)
-`conversation_id`: A unique ID of the conversation

#### Reason for Structure

<!-- info: How was the dataset structure determined? -->
<!-- scope: microscope -->
NA

#### How were labels chosen?

<!-- info: How were the labels chosen? -->
<!-- scope: microscope -->
NA

#### Example Instance

<!-- info: Provide a JSON formatted example of a typical instance in the dataset. -->
<!-- scope: periscope -->
```
{'context': "<PR>get_movie_attribute<PRAN>rating.movie<PRAV>rated R<C><U>I wanna see a movie<A>where are you?<U>spring hills kansas<PN>find_theaters<PAN>location<PAV>spring hills kansas<PR>find_theaters<PRAN>name.theater<PRAV>AMC Holiday Theater<PRAV>Cinemark Downtown<A>there are 2 theaters near you, the AMC Holiday Theater and Cinemark Downtown. Did you know which movie you'd like to see?<U>funny one please<PN>find_movies<PAN>location<PAV>spring hills kansas<PR>find_movies<PRAN>name.movie<PRAV>Not My Problem<PRAV>Family Jewels<PN>get_movie_attribute<PAN>name.movie<PAV>Not My Problem<PAN>attribute<PAV>name.genre<PR>get_movie_attribute<PRAN>name.genre<PRAV>comedy<PN>get_movie_attribute<PAN>name.movie<PAV>Not My Problem<PAN>attribute<PAV>name.person<PR>get_movie_attribute<PRAN>name.person<PRAV>Matt Damon<PN>get_movie_attribute<PAN>name.movie<PAV>Not My Problem<PAN>attribute<PAV>name.person<PR>get_movie_attribute<PRAN>name.person<PRAV>Noah Schnapp<PN>get_movie_attribute<PAN>name.movie<PAV>Family Jewels<PAN>attribute<PAV>name.genre<PR>get_movie_attribute<PRAN>name.genre<PRAV>romantic comedy<PN>get_movie_attribute<PAN>name.movie<PAV>Family Jewels<PAN>attribute<PAV>name.person<PR>get_movie_attribute<PRAN>name.person<PRAV>Melissa McCarthy<PN>get_movie_attribute<PAN>name.movie<PAV>Family Jewels<PAN>attribute<PAV>name.person<PR>get_movie_attribute<PRAN>name.person<PRAV>Ryan Reynolds<A>There's the comedy film called Not My Problem starring Matt Damon and Noah Schnapp. There's also a romantic comedy called Family Jewels starring Melissa McCarthy and Ryan Reynolds.<U>what ratings are there?<PN>get_movie_attribute<PAN>name.movie<PAV>Not My Problem<PAN>attribute<PAV>rating.movie<PR>get_movie_attribute<PRAN>rating.movie<PRAV>rated PG-13<PN>get_movie_attribute<PAN>name.movie<PAV>Family Jewels<PAN>attribute<PAV>rating.movie",
 'conversation_id': 'dlg-d1f52e7e-c34c-4e85-b406-85ed138b5068',
 'gem_id': 'Taskmaster-train-0',
 'references': ['Not My Problem is rated PG-13 and Family Jewels is rated R.'],
 'target': 'Not My Problem is rated PG-13 and Family Jewels is rated R.'}
```

#### Data Splits

<!-- info: Describe and name the splits in the dataset if there are more than one. -->
<!-- scope: periscope -->
-`train`: 187182 examples
-`dev`: 23406 examples
-`test`: 23316 examples

#### Splitting Criteria

<!-- info: Describe any criteria for splitting the data, if used. If there are differences between the splits (e.g., if the training annotations are machine-generated and the dev and test ones are created by humans, or if different numbers of annotators contributed to each example), describe them here. -->
<!-- scope: microscope -->
NA

#### 

<!-- info: What does an outlier of the dataset in terms of length/perplexity/embedding look like? -->
<!-- scope: microscope -->
NA



## Dataset in GEM

### Rationale for Inclusion in GEM

#### Why is the Dataset in GEM?

<!-- info: What does this dataset contribute toward better generation evaluation and why is it part of GEM? -->
<!-- scope: microscope -->
Dialogue generation that makes sense

#### Similar Datasets

<!-- info: Do other datasets for the high level task exist? -->
<!-- scope: telescope -->
yes

#### Unique Language Coverage

<!-- info: Does this dataset cover other languages than other datasets for the same task? -->
<!-- scope: periscope -->
no

#### Difference from other GEM datasets

<!-- info: What else sets this dataset apart from other similar datasets in GEM? -->
<!-- scope: microscope -->
NA

#### Ability that the Dataset measures

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: periscope -->
NA


### GEM-Specific Curation

#### Modificatied for GEM?

<!-- info: Has the GEM version of the dataset been modified in any way (data, processing, splits) from the original curated data? -->
<!-- scope: telescope -->
yes

#### GEM Modifications

<!-- info: What changes have been made to he original dataset? -->
<!-- scope: periscope -->
`other`

#### Modification Details

<!-- info: For each of these changes, described them in more details and provided the intended purpose of the modification -->
<!-- scope: microscope -->
gem_id field was added to the 3 data splits

#### Additional Splits?

<!-- info: Does GEM provide additional splits to the dataset? -->
<!-- scope: telescope -->
no


### Getting Started with the Task

#### Pointers to Resources

<!-- info: Getting started with in-depth research on the task. Add relevant pointers to resources that researchers can consult when they want to get started digging deeper into the task. -->
<!-- scope: microscope -->
https://github.com/google-research-datasets/Taskmaster/tree/master/TM-3-2020

#### Technical Terms

<!-- info: Technical terms used in this card and the dataset and their definitions -->
<!-- scope: microscope -->
NA



## Previous Results

### Previous Results

#### Measured Model Abilities

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: telescope -->
BLEU: 60

#### Metrics

<!-- info: What metrics are typically used for this task? -->
<!-- scope: periscope -->
`BLEU`

#### Proposed Evaluation

<!-- info: List and describe the purpose of the metrics and evaluation methodology (including human evaluation) that the dataset creators used when introducing this task. -->
<!-- scope: microscope -->
automatic evaluation

#### Previous results available?

<!-- info: Are previous results available? -->
<!-- scope: telescope -->
yes

#### Other Evaluation Approaches

<!-- info: What evaluation approaches have others used? -->
<!-- scope: periscope -->
NA

#### Relevant Previous Results

<!-- info: What are the most relevant previous results for this task/dataset? -->
<!-- scope: microscope -->
NA



## Dataset Curation

### Original Curation

#### Original Curation Rationale

<!-- info: Original curation rationale -->
<!-- scope: telescope -->
NA

#### Communicative Goal

<!-- info: What was the communicative goal? -->
<!-- scope: periscope -->
a movie ticketing dialog dataset with 23,789 annotated conversations.

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

#### Language Producers

<!-- info: What further information do we have on the language producers? -->
<!-- scope: microscope -->
NA

#### Topics Covered

<!-- info: Does the language in the dataset focus on specific topics? How would you describe them? -->
<!-- scope: periscope -->
Ticketing

#### Data Validation

<!-- info: Was the text validated by a different worker or a data curator? -->
<!-- scope: telescope -->
not validated

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
NA


### Private Identifying Information (PII)

#### Contains PII?

<!-- quick -->
<!-- info: Does the source language data likely contain Personal Identifying Information about the data creators or subjects? -->
<!-- scope: telescope -->
no PII

#### Justification for no PII

<!-- info: Provide a justification for selecting `no PII` above. -->
<!-- scope: periscope -->
It's based on ticketing without personal information


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
NA



## Considerations for Using the Data

### PII Risks and Liability

#### Potential PII Risk

<!-- info: Considering your answers to the PII part of the Data Curation Section, describe any potential privacy to the data subjects and creators risks when using the dataset. -->
<!-- scope: microscope -->
NA


### Licenses

#### Copyright Restrictions on the Dataset

<!-- info: Based on your answers in the Intended Use part of the Data Overview Section, which of the following best describe the copyright and licensing status of the dataset? -->
<!-- scope: periscope -->
`open license - commercial use allowed`

#### Copyright Restrictions on the Language Data

<!-- info: Based on your answers in the Language part of the Data Curation Section, which of the following best describe the copyright and licensing status of the underlying language data? -->
<!-- scope: periscope -->
`public domain`


### Known Technical Limitations

#### Technical Limitations

<!-- info: Describe any known technical limitations, such as spurrious correlations, train/test overlap, annotation biases, or mis-annotations, and cite the works that first identified these limitations when possible. -->
<!-- scope: microscope -->
NA

#### Unsuited Applications

<!-- info: When using a model trained on this dataset in a setting where users or the public may interact with its predictions, what are some pitfalls to look out for? In particular, describe some applications of the general task featured in this dataset that its curation or properties make it less suitable for. -->
<!-- scope: microscope -->
NA

#### Discouraged Use Cases

<!-- info: What are some discouraged use cases of a model trained to maximize the proposed metrics on this dataset? In particular, think about settings where decisions made by a model that performs reasonably well on the metric my still have strong negative consequences for user or members of the public. -->
<!-- scope: microscope -->
NA


