---
annotations_creators:
- automatically-created
language_creators:
- unknown
language:
- en
license:
- cc-by-sa-3.0
multilinguality:
- unknown
size_categories:
- unknown
source_datasets:
- original
task_categories:
- summarization
task_ids: []
pretty_name: wiki_cat_sum
---

# Dataset Card for GEM/wiki_cat_sum

## Dataset Description

- **Homepage:** https://github.com/lauhaide/WikiCatSum
- **Repository:** https://datashare.ed.ac.uk/handle/10283/3368
- **Paper:** https://arxiv.org/abs/1906.04687
- **Leaderboard:** N/A
- **Point of Contact:** Laura Perez-Beltrachini

### Link to Main Data Card

You can find the main data card on the [GEM Website](https://gem-benchmark.com/data_cards/wiki_cat_sum).

### Dataset Summary 

WikiCatSum is an English summarization dataset in three domains: animals, companies, and film. It provides multiple paragraphs of text paired with a summary of the paragraphs.

You can load the dataset via:
```
import datasets
data = datasets.load_dataset('GEM/wiki_cat_sum')
```
The data loader can be found [here](https://huggingface.co/datasets/GEM/wiki_cat_sum).

#### website
[Github](https://github.com/lauhaide/WikiCatSum)

#### paper
[Arxiv](https://arxiv.org/abs/1906.04687)

#### authors
Laura Perez-Beltrachini, Yang Liu, Mirella Lapata (University of Edinburgh) Peter J. Liu, Mohammad Saleh, Etienne Pot, Ben Goodrich, Ryan Sepassi, Lukasz Kaiser, Noam Shazeer (GoogleBrain)

## Dataset Overview

### Where to find the Data and its Documentation

#### Webpage

<!-- info: What is the webpage for the dataset (if it exists)? -->
<!-- scope: telescope -->
[Github](https://github.com/lauhaide/WikiCatSum)

#### Download

<!-- info: What is the link to where the original dataset is hosted? -->
<!-- scope: telescope -->
[Website](https://datashare.ed.ac.uk/handle/10283/3368)

#### Paper

<!-- info: What is the link to the paper describing the dataset (open access preferred)? -->
<!-- scope: telescope -->
[Arxiv](https://arxiv.org/abs/1906.04687)

#### BibTex

<!-- info: Provide the BibTex-formatted reference for the dataset. Please use the correct published version (ACL anthology, etc.) instead of google scholar created Bibtex. -->
<!-- scope: microscope -->
```
@inproceedings{perez-beltrachini-etal-2019-generating,
    title = "Generating Summaries with Topic Templates and Structured Convolutional Decoders",
    author = "Perez-Beltrachini, Laura  and
      Liu, Yang  and
      Lapata, Mirella",
    booktitle = "Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics",
    month = jul,
    year = "2019",
    address = "Florence, Italy",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/P19-1504",
    doi = "10.18653/v1/P19-1504",
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
cc-by-sa-3.0: Creative Commons Attribution Share Alike 3.0 Unported

#### Intended Use

<!-- info: What is the intended use of the dataset? -->
<!-- scope: microscope -->
Research on multi-document abstractive summarisation.

#### Primary Task

<!-- info: What primary task does the dataset support? -->
<!-- scope: telescope -->
Summarization

#### Communicative Goal

<!-- quick -->
<!-- info: Provide a short description of the communicative goal of a model trained for this task on this dataset. -->
<!-- scope: periscope -->
Summarise the most important facts of a given entity in the Film, Company, and Animal domains from a cluster of related documents. 


### Credit

#### Curation Organization Type(s)

<!-- info: In what kind of organization did the dataset curation happen? -->
<!-- scope: telescope -->
`industry`, `academic`

#### Curation Organization(s)

<!-- info: Name the organization(s). -->
<!-- scope: periscope -->
Google Cloud Platform, University of Edinburgh

#### Dataset Creators

<!-- info: Who created the original dataset? List the people involved in collecting the dataset and their affiliation(s). -->
<!-- scope: microscope -->
Laura Perez-Beltrachini, Yang Liu, Mirella Lapata (University of Edinburgh) Peter J. Liu, Mohammad Saleh, Etienne Pot, Ben Goodrich, Ryan Sepassi, Lukasz Kaiser, Noam Shazeer (GoogleBrain)

#### Funding

<!-- info: Who funded the data creation? -->
<!-- scope: microscope -->
Google Cloud Platform, European Research Council

#### Who added the Dataset to GEM?

<!-- info: Who contributed to the data card and adding the dataset to GEM? List the people+affiliations involved in creating this data card and who helped integrate this dataset into GEM. -->
<!-- scope: microscope -->
Ronald Cardenas (University of Edinburgh) Laura Perez-Beltrachini (University of Edinburgh) 


### Dataset Structure

#### Data Fields

<!-- info: List and describe the fields present in the dataset. -->
<!-- scope: telescope -->
- `id`: ID of the data example 
- `title`: Is the Wikipedia article's title
- `paragraphs`: Is the ranked list of paragraphs from the set of crawled texts
- `summary`: Is constituted by a list of sentences together with their corresponding topic label

#### Example Instance

<!-- info: Provide a JSON formatted example of a typical instance in the dataset. -->
<!-- scope: periscope -->
This is a truncated example from the animal setting: 

```
{'gem_id': 'animal-train-1',
 'gem_parent_id': 'animal-train-1',
 'id': '2652',
 'paragraphs': ["lytrosis (hulst) of louisiana vernon antoine brou jr. 2005. southern lepidopterists' news, 27: 7 ., ..."],
 'references': ['lytrosis unitaria , the common lytrosis moth, is a species of moth of the geometridae family. it is found in north america, including arkansas, georgia, iowa , massachusetts, and wisconsin. the wingspan is about 50 mm. the larvae feed on rosa, crataegus, amelanchier, acer, quercus and viburnum species.'],
 'summary': {'text': ['lytrosis unitaria , the common lytrosis moth , is a species of moth of the geometridae family .',
   'it is found in north america , including arkansas , georgia , iowa , massachusetts , new hampshire , new jersey , new york , north carolina , ohio , oklahoma , ontario , pennsylvania , south carolina , tennessee , texas , virginia , west virginia and wisconsin .',
   'the wingspan is about 50 mm .',
   'the larvae feed on rosa , crataegus , amelanchier , acer , quercus and viburnum species . '],
  'topic': [29, 20, 9, 8]},
 'target': 'lytrosis unitaria , the common lytrosis moth, is a species of moth of the geometridae family. it is found in north america, including arkansas, georgia, iowa , massachusetts, and wisconsin. the wingspan is about 50 mm. the larvae feed on rosa, crataegus, amelanchier, acer, quercus and viburnum species.',
 'title': 'lytrosis unitaria'}
```

#### Data Splits

<!-- info: Describe and name the splits in the dataset if there are more than one. -->
<!-- scope: periscope -->
Nb of instances in train/valid/test are 50,938/2,855/2,831

#### Splitting Criteria

<!-- info: Describe any criteria for splitting the data, if used. If there are differences between the splits (e.g., if the training annotations are machine-generated and the dev and test ones are created by humans, or if different numbers of annotators contributed to each example), describe them here. -->
<!-- scope: microscope -->
The data was split i.i.d., i.e. uniformly split into training, validation, and test datasets.



## Dataset in GEM

### Rationale for Inclusion in GEM

#### Why is the Dataset in GEM?

<!-- info: What does this dataset contribute toward better generation evaluation and why is it part of GEM? -->
<!-- scope: microscope -->
Evaluation of models' performance on noisy (document, summary) pairs and long inputs.
Evaluate models' capabilities to generalise and mitigate biases.  

#### Similar Datasets

<!-- info: Do other datasets for the high level task exist? -->
<!-- scope: telescope -->
no

#### Unique Language Coverage

<!-- info: Does this dataset cover other languages than other datasets for the same task? -->
<!-- scope: periscope -->
no

#### Ability that the Dataset measures

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: periscope -->
Capabilities to generalise, mitigate biases, factual correctness.  


### GEM-Specific Curation

#### Modificatied for GEM?

<!-- info: Has the GEM version of the dataset been modified in any way (data, processing, splits) from the original curated data? -->
<!-- scope: telescope -->
yes

#### GEM Modifications

<!-- info: What changes have been made to he original dataset? -->
<!-- scope: periscope -->
`annotations added`

#### Modification Details

<!-- info: For each of these changes, described them in more details and provided the intended purpose of the modification -->
<!-- scope: microscope -->
We provide topic labels for summary sentences.

#### Additional Splits?

<!-- info: Does GEM provide additional splits to the dataset? -->
<!-- scope: telescope -->
no


### Getting Started with the Task

#### Pointers to Resources

<!-- info: Getting started with in-depth research on the task. Add relevant pointers to resources that researchers can consult when they want to get started digging deeper into the task. -->
<!-- scope: microscope -->
- [Generating Wikipedia by Summarizing Long Sequences](https://arxiv.org/abs/1801.10198)
- [Generating Summaries with Topic Templates and Structured Convolutional Decoders](https://arxiv.org/abs/1906.04687)
- [Noisy Self-Knowledge Distillation for Text Summarization](https://arxiv.org/abs/2009.07032)

And all references in these papers.



## Previous Results

### Previous Results

#### Measured Model Abilities

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: telescope -->
Capabilities to generalise, mitigate biases, factual correctness.

#### Metrics

<!-- info: What metrics are typically used for this task? -->
<!-- scope: periscope -->
`ROUGE`, `BERT-Score`, `MoverScore`, `Other: Other Metrics`

#### Other Metrics

<!-- info: Definitions of other metrics -->
<!-- scope: periscope -->
- Abstract/Copy
- Factual accuracy based on the score of (Goodrich et al., 2019) and the relation extraction system of (Sorokin and Gurevych, 2017).

#### Proposed Evaluation

<!-- info: List and describe the purpose of the metrics and evaluation methodology (including human evaluation) that the dataset creators used when introducing this task. -->
<!-- scope: microscope -->
Human based are Question Answering and Ranking (Content, Fluency and  Repetition)

#### Previous results available?

<!-- info: Are previous results available? -->
<!-- scope: telescope -->
yes

#### Other Evaluation Approaches

<!-- info: What evaluation approaches have others used? -->
<!-- scope: periscope -->
Those listed above.

#### Relevant Previous Results

<!-- info: What are the most relevant previous results for this task/dataset? -->
<!-- scope: microscope -->
Generating Summaries with Topic Templates and Structured Convolutional Decoders
https://arxiv.org/abs/1906.04687

Noisy Self-Knowledge Distillation for Text Summarization
https://arxiv.org/abs/2009.07032




## Dataset Curation

### Original Curation

#### Original Curation Rationale

<!-- info: Original curation rationale -->
<!-- scope: telescope -->
The dataset is a subset of the WikiSum (Liu et al., 2018) dataset focusing on summaries of entities in three domains (Film, Company, and Animal). It is multi-document summarisation where input-output pairs for each example entity are created as follows. The input is a set of paragraphs collected from i) documents in the Reference section of the entity's Wikipedia page plus ii) documents collected from the top ten search results after querying Google search engine with the entity name. The output summary is the Wikipedia abstract for the entity.

#### Communicative Goal

<!-- info: What was the communicative goal? -->
<!-- scope: periscope -->
Generate descriptive summaries with specific domains, where certain topics are discussed and generally in specific orders.

#### Sourced from Different Sources

<!-- info: Is the dataset aggregated from different data sources? -->
<!-- scope: telescope -->
yes

#### Source Details

<!-- info: List the sources (one per line) -->
<!-- scope: periscope -->
WikiSum (Liu et al., 2018)


### Language Data

#### How was Language Data Obtained?

<!-- info: How was the language data obtained? -->
<!-- scope: telescope -->
`Other`

#### Topics Covered

<!-- info: Does the language in the dataset focus on specific topics? How would you describe them? -->
<!-- scope: periscope -->
The dataset and task focuses on summaries for entities in three domains:  Company, Film, and Animal.

#### Data Validation

<!-- info: Was the text validated by a different worker or a data curator? -->
<!-- scope: telescope -->
not validated

#### Data Preprocessing

<!-- info: How was the text data pre-processed? (Enter N/A if the text was not pre-processed) -->
<!-- scope: microscope -->
Summary sentences are associated with a topic label. There is a topic model for each domain. 

#### Was Data Filtered?

<!-- info: Were text instances selected or filtered? -->
<!-- scope: telescope -->
not filtered


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
Each summary sentences was annotated with a topic label. There is a topic model for each of the three domains. This was used to guide a hierarchical decoder. 

#### Any Quality Control?

<!-- info: Quality control measures? -->
<!-- scope: telescope -->
validated by data curators

#### Quality Control Details

<!-- info: Describe the quality control measures that were taken. -->
<!-- scope: microscope -->
Manual inspection of a sample of topics assigned to sentences. The number of topics was selected based on the  performance of the summarisation model.


### Consent

#### Any Consent Policy?

<!-- info: Was there a consent policy involved when gathering the data? -->
<!-- scope: telescope -->
no

#### Justification for Using the Data

<!-- info: If not, what is the justification for reusing the data? -->
<!-- scope: microscope -->
The dataset is base on Wikipedia and referenced and retrieved documents crawled from the Web.


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

#### Links and Summaries of Analysis Work

<!-- info: Provide links to and summaries of works analyzing these biases. -->
<!-- scope: microscope -->
This dataset is based on Wikipedia and thus biases analysis on other Wikipedia-based datasets are potentially true for  WikiCatSum.  For instance, see analysis for the ToTTo dataset here [1].

[1] Automatic Construction of Evaluation Suites for Natural Language Generation Datasets
https://openreview.net/forum?id=CSi1eu_2q96





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



