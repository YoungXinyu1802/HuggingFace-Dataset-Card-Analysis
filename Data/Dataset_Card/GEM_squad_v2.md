---
annotations_creators:
- crowd-sourced
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
- other
task_ids: []
pretty_name: squad_v2
tags:
- question-generation
---

# Dataset Card for GEM/squad_v2

## Dataset Description

- **Homepage:** https://rajpurkar.github.io/SQuAD-explorer/
- **Repository:** https://rajpurkar.github.io/SQuAD-explorer/
- **Paper:** https://arxiv.org/abs/1806.03822v1
- **Leaderboard:** https://rajpurkar.github.io/SQuAD-explorer/
- **Point of Contact:** Robin Jia

### Link to Main Data Card

You can find the main data card on the [GEM Website](https://gem-benchmark.com/data_cards/squad_v2).

### Dataset Summary 

SQuAD2.0 is a dataset that tests the ability of a system to not only answer reading comprehension questions, but also abstain when presented with a question that cannot be answered based on the provided paragraph.  F1 score is used to evaluate models on the leaderboard. In GEM, we are using this dataset for the question-generation task in which a model should generate squad-like questions from an input text.

You can load the dataset via:
```
import datasets
data = datasets.load_dataset('GEM/squad_v2')
```
The data loader can be found [here](https://huggingface.co/datasets/GEM/squad_v2).

#### website
[Website](https://rajpurkar.github.io/SQuAD-explorer/)

#### paper
[Arxiv](https://arxiv.org/abs/1806.03822v1)

#### authors
Pranav Rajpurkar,  Robin Jia and Percy Liang

## Dataset Overview

### Where to find the Data and its Documentation

#### Webpage

<!-- info: What is the webpage for the dataset (if it exists)? -->
<!-- scope: telescope -->
[Website](https://rajpurkar.github.io/SQuAD-explorer/)

#### Download

<!-- info: What is the link to where the original dataset is hosted? -->
<!-- scope: telescope -->
[Website](https://rajpurkar.github.io/SQuAD-explorer/)

#### Paper

<!-- info: What is the link to the paper describing the dataset (open access preferred)? -->
<!-- scope: telescope -->
[Arxiv](https://arxiv.org/abs/1806.03822v1)

#### BibTex

<!-- info: Provide the BibTex-formatted reference for the dataset. Please use the correct published version (ACL anthology, etc.) instead of google scholar created Bibtex. -->
<!-- scope: microscope -->
```
@inproceedings{Rajpurkar2018KnowWY,
  title={Know What You Don’t Know: Unanswerable Questions for SQuAD},
  author={Pranav Rajpurkar and Robin Jia and Percy Liang},
  booktitle={ACL},
  year={2018}
}
```

#### Contact Name

<!-- quick -->
<!-- info: If known, provide the name of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
Robin Jia

#### Contact Email

<!-- info: If known, provide the email of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
robinjia@stanford.edu

#### Has a Leaderboard?

<!-- info: Does the dataset have an active leaderboard? -->
<!-- scope: telescope -->
yes

#### Leaderboard Link

<!-- info: Provide a link to the leaderboard. -->
<!-- scope: periscope -->
[Website](https://rajpurkar.github.io/SQuAD-explorer/)

#### Leaderboard Details

<!-- info: Briefly describe how the leaderboard evaluates models. -->
<!-- scope: microscope -->
SQuAD2.0 tests the ability of a system to not only answer reading comprehension questions, but also abstain when presented with a question that cannot be answered based on the provided paragraph.  F1 score is used to evaluate models on the leaderboard.


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
cc-by-sa-4.0: Creative Commons Attribution Share Alike 4.0 International

#### Intended Use

<!-- info: What is the intended use of the dataset? -->
<!-- scope: microscope -->
The idea behind SQuAD2.0 dataset is to make the models understand when a question cannot be answered given a context. This will help in building models such that they know what they don't know, and therefore make the models understand language at a deeper level. The tasks that can be supported by the dataset are machine reading comprehension, extractive QA, and question generation.

#### Primary Task

<!-- info: What primary task does the dataset support? -->
<!-- scope: telescope -->
Question Generation

#### Communicative Goal

<!-- quick -->
<!-- info: Provide a short description of the communicative goal of a model trained for this task on this dataset. -->
<!-- scope: periscope -->
Given an input passage and an answer span, the  goal is to generate a question that asks for the answer.


### Credit

#### Curation Organization Type(s)

<!-- info: In what kind of organization did the dataset curation happen? -->
<!-- scope: telescope -->
`academic`

#### Curation Organization(s)

<!-- info: Name the organization(s). -->
<!-- scope: periscope -->
Stanford University

#### Dataset Creators

<!-- info: Who created the original dataset? List the people involved in collecting the dataset and their affiliation(s). -->
<!-- scope: microscope -->
Pranav Rajpurkar,  Robin Jia and Percy Liang

#### Funding

<!-- info: Who funded the data creation? -->
<!-- scope: microscope -->
Facebook and NSF Graduate Research Fellowship under Grant No. DGE-114747

#### Who added the Dataset to GEM?

<!-- info: Who contributed to the data card and adding the dataset to GEM? List the people+affiliations involved in creating this data card and who helped integrate this dataset into GEM. -->
<!-- scope: microscope -->
(Abinaya Mahendiran)[https://github.com/AbinayaM02], Manager Data Science, NEXT Labs,


### Dataset Structure

#### Data Fields

<!-- info: List and describe the fields present in the dataset. -->
<!-- scope: telescope -->
The data fields are the same among all splits.

#### squad_v2

- `id`: a `string` feature.
- `gem_id`: a `string` feature.
- `title`: a `string` feature.
- `context`: a `string` feature.
- `question`: a `string` feature.
- `answers`: a dictionary feature containing:
  - `text`: a `string` feature.
  - `answer_start`: a `int32` feature.

#### Example Instance

<!-- info: Provide a JSON formatted example of a typical instance in the dataset. -->
<!-- scope: periscope -->
Here is an example of a validation data point. This example was too long and was cropped:

```
{
    "gem_id": "gem-squad_v2-validation-1",
    "id": "56ddde6b9a695914005b9629",
    "answers": {
        "answer_start": [94, 87, 94, 94],
        "text": ["10th and 11th centuries", "in the 10th and 11th centuries", "10th and 11th centuries", "10th and 11th centuries"]
    },
    "context": "\"The Normans (Norman: Nourmands; French: Normands; Latin: Normanni) were the people who in the 10th and 11th centuries gave thei...",
    "question": "When were the Normans in Normandy?",
    "title": "Normans"
}
```

#### Data Splits

<!-- info: Describe and name the splits in the dataset if there are more than one. -->
<!-- scope: periscope -->
The original SQuAD2.0 dataset has only training and dev (validation) splits. The train split is further divided into test split and added as part of the GEM datasets.

| name           |  train    | validation | test     |
| -------------- | --------: | -------------: | -------: |
| squad_v2   | 90403  |          11873 | 39916 |



## Dataset in GEM

### Rationale for Inclusion in GEM

#### Why is the Dataset in GEM?

<!-- info: What does this dataset contribute toward better generation evaluation and why is it part of GEM? -->
<!-- scope: microscope -->
SQuAD2.0 will encourage the development of new reading comprehension models
that know what they don’t know, and therefore understand language at a deeper level. It can also help in building better models for answer-aware question generation .

#### Similar Datasets

<!-- info: Do other datasets for the high level task exist? -->
<!-- scope: telescope -->
no

#### Unique Language Coverage

<!-- info: Does this dataset cover other languages than other datasets for the same task? -->
<!-- scope: periscope -->
yes

#### Ability that the Dataset measures

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: periscope -->
Reasoning capability


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
yes

#### Split Information

<!-- info: Describe how the new splits were created -->
<!-- scope: periscope -->
The train(80%) and validation(10%) split of SQuAD2.0 are made available to public whereas the  test(10%) split is not available. 

As part of GEM, the train split, 80% of the original data is split into two train split (90%) and test split (remaining 10%). The idea is to provide all three splits for the users to use. 


### Getting Started with the Task




## Previous Results

### Previous Results

#### Measured Model Abilities

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: telescope -->
Extractive QA, Question Generation

#### Metrics

<!-- info: What metrics are typically used for this task? -->
<!-- scope: periscope -->
`Other: Other Metrics`, `METEOR`, `ROUGE`, `BLEU`

#### Other Metrics

<!-- info: Definitions of other metrics -->
<!-- scope: periscope -->
- Extractive QA  uses Exact Match and F1 Score
- Question generation users METEOR, ROUGE-L, BLEU-4

#### Previous results available?

<!-- info: Are previous results available? -->
<!-- scope: telescope -->
yes

#### Other Evaluation Approaches

<!-- info: What evaluation approaches have others used? -->
<!-- scope: periscope -->
Question generation users METEOR, ROUGE-L, BLEU-4

#### Relevant Previous Results

<!-- info: What are the most relevant previous results for this task/dataset? -->
<!-- scope: microscope -->
@article{Dong2019UnifiedLM,
  title={Unified Language Model Pre-training for Natural Language Understanding and Generation},
  author={Li Dong and Nan Yang and Wenhui Wang and Furu Wei and Xiaodong Liu and Yu Wang and Jianfeng Gao and M. Zhou and Hsiao-Wuen Hon},
  journal={ArXiv},
  year={2019},
  volume={abs/1905.03197}
}



## Dataset Curation

### Original Curation

#### Original Curation Rationale

<!-- info: Original curation rationale -->
<!-- scope: telescope -->
The dataset is curated in three stages: 
- Curating passages, 
- Crowdsourcing question-answers on those passages,
- Obtaining additional answers
As part of SQuAD1.1, 10000 high-quality articles from English Wikipedia is extracted using Project Nayuki’s Wikipedia’s internal PageRanks, from which 536 articles are sampled uniformly at random. From each of these articles, individual paragraphs are extracted, stripping away images, figures, tables, and discarding paragraphs shorter than 500 characters. 

SQuAD2.0 combines the 100,000 questions in SQuAD1.1 with over 50,000 unanswerable questions written adversarially by crowdworkers to look similar to answerable ones. 


#### Communicative Goal

<!-- info: What was the communicative goal? -->
<!-- scope: periscope -->
To build systems that not only answer questions when possible, but also determine when no
answer is supported by the paragraph and abstain from answering.

#### Sourced from Different Sources

<!-- info: Is the dataset aggregated from different data sources? -->
<!-- scope: telescope -->
yes

#### Source Details

<!-- info: List the sources (one per line) -->
<!-- scope: periscope -->
Wikipedia


### Language Data

#### How was Language Data Obtained?

<!-- info: How was the language data obtained? -->
<!-- scope: telescope -->
`Found`

#### Where was it found?

<!-- info: If found, where from? -->
<!-- scope: telescope -->
`Single website`

#### Topics Covered

<!-- info: Does the language in the dataset focus on specific topics? How would you describe them? -->
<!-- scope: periscope -->
The dataset contains 536 articles covering a wide range of topics, from musical celebrities to abstract concepts.

#### Data Validation

<!-- info: Was the text validated by a different worker or a data curator? -->
<!-- scope: telescope -->
validated by crowdworker

#### Data Preprocessing

<!-- info: How was the text data pre-processed? (Enter N/A if the text was not pre-processed) -->
<!-- scope: microscope -->
From the sampled articles from Wikipedia, individual paragraphs are extracted, stripping
away images, figures, tables, and discarding paragraphs shorter than 500 characters  and partitioned into training(80%),  development set(10%) and test set(10%).

#### Was Data Filtered?

<!-- info: Were text instances selected or filtered? -->
<!-- scope: telescope -->
algorithmically

#### Filter Criteria

<!-- info: What were the selection criteria? -->
<!-- scope: microscope -->
To retrieve high-quality articles, Project Nayuki’s Wikipedia’s internal PageRanks was used to obtain the top 10000 articles of English Wikipedia, from which 536 articles are sampled uniformly at random. 


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
Crowdworkers from the United States or Canada with a 97% HIT acceptance rate, a minimum of 1000 HITs, were employed to create questions. 

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
yes

#### Which Annotation Service

<!-- info: Which annotation services were used? -->
<!-- scope: periscope -->
`other`, `Amazon Mechanical Turk`

#### Annotation Values

<!-- info: Purpose and values for each annotation -->
<!-- scope: microscope -->
For SQuAD 1.1 ,  crowdworkers were tasked with asking and answering up to 5 questions on the
content of that paragraph. The questions had to be entered in a text field, and the answers had to be
highlighted in the paragraph.

For SQuAD2.0, each task consisted of an entire article from SQuAD 1.1. For each paragraph in the article, workers were asked to pose up to five questions that were impossible to answer
based on the paragraph alone, while referencing entities in the paragraph and ensuring that a plausible answer is present. 

#### Any Quality Control?

<!-- info: Quality control measures? -->
<!-- scope: telescope -->
validated by another rater

#### Quality Control Details

<!-- info: Describe the quality control measures that were taken. -->
<!-- scope: microscope -->
Questions from workers who wrote 25 or fewer questions on an article is removed; this filter
helped remove noise from workers who had trouble understanding the task, and therefore quit before completing the whole article. This filter to both SQuAD2.0 and the existing answerable questions from SQuAD 1.1.


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
unlikely

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
yes



## Considerations for Using the Data

### PII Risks and Liability



### Licenses



### Known Technical Limitations



