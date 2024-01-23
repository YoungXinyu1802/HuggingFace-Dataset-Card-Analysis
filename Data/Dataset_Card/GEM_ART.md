---
annotations_creators:
- automatically-created
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
pretty_name: ART
tags:
- reasoning
---

# Dataset Card for GEM/ART

## Dataset Description

- **Homepage:** http://abductivecommonsense.xyz/
- **Repository:** https://storage.googleapis.com/ai2-mosaic/public/abductive-commonsense-reasoning-iclr2020/anlg.zip
- **Paper:** https://openreview.net/pdf?id=Byg1v1HKDB
- **Leaderboard:** N/A
- **Point of Contact:** Chandra Bhagavatulla

### Link to Main Data Card

You can find the main data card on the [GEM Website](https://gem-benchmark.com/data_cards/ART).

### Dataset Summary 

Abductive reasoning is inference to the most plausible explanation. For example, if Jenny finds her house in a mess when she returns from work, and remembers that she left a window open, she can hypothesize that a thief broke into her house and caused the mess, as the most plausible explanation.
This data loader focuses on abductive NLG: a conditional English generation task for explaining given observations in natural language. 

You can load the dataset via:
```
import datasets
data = datasets.load_dataset('GEM/ART')
```
The data loader can be found [here](https://huggingface.co/datasets/GEM/ART).

#### website
[Website](http://abductivecommonsense.xyz/)

#### paper
[OpenReview](https://openreview.net/pdf?id=Byg1v1HKDB)

#### authors
Chandra Bhagavatula (AI2), Ronan Le Bras (AI2), Chaitanya Malaviya (AI2), Keisuke Sakaguchi (AI2), Ari Holtzman (AI2, UW), Hannah Rashkin (AI2, UW), Doug Downey (AI2), Wen-tau Yih (AI2), Yejin Choi  (AI2, UW)

## Dataset Overview

### Where to find the Data and its Documentation

#### Webpage

<!-- info: What is the webpage for the dataset (if it exists)? -->
<!-- scope: telescope -->
[Website](http://abductivecommonsense.xyz/)

#### Download

<!-- info: What is the link to where the original dataset is hosted? -->
<!-- scope: telescope -->
[Google Storage](https://storage.googleapis.com/ai2-mosaic/public/abductive-commonsense-reasoning-iclr2020/anlg.zip)

#### Paper

<!-- info: What is the link to the paper describing the dataset (open access preferred)? -->
<!-- scope: telescope -->
[OpenReview](https://openreview.net/pdf?id=Byg1v1HKDB)

#### BibTex

<!-- info: Provide the BibTex-formatted reference for the dataset. Please use the correct published version (ACL anthology, etc.) instead of google scholar created Bibtex. -->
<!-- scope: microscope -->
```
@inproceedings{
Bhagavatula2020Abductive,
title={Abductive Commonsense Reasoning},
author={Chandra Bhagavatula and Ronan Le Bras and Chaitanya Malaviya and Keisuke Sakaguchi and Ari Holtzman and Hannah Rashkin and Doug Downey and Wen-tau Yih and Yejin Choi},
booktitle={International Conference on Learning Representations},
year={2020},
url={https://openreview.net/forum?id=Byg1v1HKDB}
}
```

#### Contact Name

<!-- quick -->
<!-- info: If known, provide the name of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
Chandra Bhagavatulla

#### Contact Email

<!-- info: If known, provide the email of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
chandrab@allenai.org

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

#### Whose Language?

<!-- info: Whose language is in the dataset? -->
<!-- scope: periscope -->
Crowdworkers on the Amazon Mechanical Turk platform based in the U.S, Canada, U.K and Australia. 

#### License

<!-- quick -->
<!-- info: What is the license of the dataset? -->
<!-- scope: telescope -->
apache-2.0: Apache License 2.0

#### Intended Use

<!-- info: What is the intended use of the dataset? -->
<!-- scope: microscope -->
To study the viability of language-based abductive reasoning. Training and evaluating models to generate a plausible hypothesis to explain two given observations.

#### Primary Task

<!-- info: What primary task does the dataset support? -->
<!-- scope: telescope -->
Reasoning


### Credit

#### Curation Organization Type(s)

<!-- info: In what kind of organization did the dataset curation happen? -->
<!-- scope: telescope -->
`industry`

#### Curation Organization(s)

<!-- info: Name the organization(s). -->
<!-- scope: periscope -->
Allen Institute for AI

#### Dataset Creators

<!-- info: Who created the original dataset? List the people involved in collecting the dataset and their affiliation(s). -->
<!-- scope: microscope -->
Chandra Bhagavatula (AI2), Ronan Le Bras (AI2), Chaitanya Malaviya (AI2), Keisuke Sakaguchi (AI2), Ari Holtzman (AI2, UW), Hannah Rashkin (AI2, UW), Doug Downey (AI2), Wen-tau Yih (AI2), Yejin Choi  (AI2, UW)

#### Funding

<!-- info: Who funded the data creation? -->
<!-- scope: microscope -->
Allen Institute for AI

#### Who added the Dataset to GEM?

<!-- info: Who contributed to the data card and adding the dataset to GEM? List the people+affiliations involved in creating this data card and who helped integrate this dataset into GEM. -->
<!-- scope: microscope -->
Chandra Bhagavatula (AI2), Ronan LeBras (AI2), Aman Madaan (CMU), Nico Daheim (RWTH Aachen University)


### Dataset Structure

#### Data Fields

<!-- info: List and describe the fields present in the dataset. -->
<!-- scope: telescope -->
- `observation_1`: A string describing an observation / event.
- `observation_2`: A string describing an observation / event.
- `label`: A string that plausibly explains why observation_1 and observation_2 might have happened.

#### How were labels chosen?

<!-- info: How were the labels chosen? -->
<!-- scope: microscope -->
Explanations were authored by crowdworkers on the Amazon Mechanical Turk platform using a custom template designed by the creators of the dataset.

#### Example Instance

<!-- info: Provide a JSON formatted example of a typical instance in the dataset. -->
<!-- scope: periscope -->
```
{
'gem_id': 'GEM-ART-validation-0',
'observation_1': 'Stephen was at a party.',
'observation_2': 'He checked it but it was completely broken.',
'label': 'Stephen knocked over a vase while drunk.'
}
```

#### Data Splits

<!-- info: Describe and name the splits in the dataset if there are more than one. -->
<!-- scope: periscope -->
- `train`: Consists of training instances. 
- `dev`: Consists of dev instances.
- `test`: Consists of test instances.




## Dataset in GEM

### Rationale for Inclusion in GEM

#### Why is the Dataset in GEM?

<!-- info: What does this dataset contribute toward better generation evaluation and why is it part of GEM? -->
<!-- scope: microscope -->
Abductive reasoning is a crucial capability of humans and ART is the first dataset curated to study language-based abductive reasoning.

#### Similar Datasets

<!-- info: Do other datasets for the high level task exist? -->
<!-- scope: telescope -->
no

#### Ability that the Dataset measures

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: periscope -->
Whether models can reason abductively about a given pair of observations.


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

#### Pointers to Resources

<!-- info: Getting started with in-depth research on the task. Add relevant pointers to resources that researchers can consult when they want to get started digging deeper into the task. -->
<!-- scope: microscope -->
- [Paper](https://arxiv.org/abs/1908.05739)
- [Code](https://github.com/allenai/abductive-commonsense-reasoning)



## Previous Results

### Previous Results

#### Measured Model Abilities

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: telescope -->
Whether models can reason abductively about a given pair of observations.

#### Metrics

<!-- info: What metrics are typically used for this task? -->
<!-- scope: periscope -->
`BLEU`, `BERT-Score`, `ROUGE`

#### Previous results available?

<!-- info: Are previous results available? -->
<!-- scope: telescope -->
no



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
`Amazon Mechanical Turk`

#### Language Producers

<!-- info: What further information do we have on the language producers? -->
<!-- scope: microscope -->
Language producers were English speakers in U.S., Canada, U.K and Australia.

#### Topics Covered

<!-- info: Does the language in the dataset focus on specific topics? How would you describe them? -->
<!-- scope: periscope -->
No

#### Data Validation

<!-- info: Was the text validated by a different worker or a data curator? -->
<!-- scope: telescope -->
validated by crowdworker

#### Was Data Filtered?

<!-- info: Were text instances selected or filtered? -->
<!-- scope: telescope -->
algorithmically

#### Filter Criteria

<!-- info: What were the selection criteria? -->
<!-- scope: microscope -->
Adversarial filtering algorithm as described in the [paper](https://arxiv.org/abs/1908.05739)


### Structured Annotations

#### Additional Annotations?

<!-- quick -->
<!-- info: Does the dataset have additional annotations for each instance? -->
<!-- scope: telescope -->
automatically created

#### Annotation Service?

<!-- info: Was an annotation service used? -->
<!-- scope: telescope -->
no

#### Annotation Values

<!-- info: Purpose and values for each annotation -->
<!-- scope: microscope -->
Each observation is associated with a list of COMET (https://arxiv.org/abs/1906.05317) inferences.

#### Any Quality Control?

<!-- info: Quality control measures? -->
<!-- scope: telescope -->
none


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

#### Justification for no PII

<!-- info: Provide a justification for selecting `no PII` above. -->
<!-- scope: periscope -->
The dataset contains day-to-day events. It does not contain names, emails, addresses etc. 


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
`public domain`

#### Copyright Restrictions on the Language Data

<!-- info: Based on your answers in the Language part of the Data Curation Section, which of the following best describe the copyright and licensing status of the underlying language data? -->
<!-- scope: periscope -->
`public domain`


### Known Technical Limitations



