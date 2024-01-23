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
- table-to-text
task_ids: []
pretty_name: e2e_nlg
tags:
- data-to-text
---

# Dataset Card for GEM/e2e_nlg

## Dataset Description

- **Homepage:** http://www.macs.hw.ac.uk/InteractionLab/E2E/
- **Repository:** https://github.com/tuetschek/e2e-cleaning
- **Paper:** https://www.aclweb.org/anthology/W17-5525/,   [Detailed E2E Challenge writeup
- **Leaderboard:** N/A
- **Point of Contact:** Ondrej Dusek

### Link to Main Data Card

You can find the main data card on the [GEM Website](https://gem-benchmark.com/data_cards/e2e_nlg).

### Dataset Summary 

The E2E NLG dataset is an English benchmark dataset for data-to-text models that verbalize a set of 2-9 key-value attribute pairs in the restaurant domain. The version used for GEM is the cleaned E2E NLG dataset, which filters examples with hallucinations and outputs that don't fully cover all input attributes. 

You can load the dataset via:
```
import datasets
data = datasets.load_dataset('GEM/e2e_nlg')
```
The data loader can be found [here](https://huggingface.co/datasets/GEM/e2e_nlg).

#### website
[Website](http://www.macs.hw.ac.uk/InteractionLab/E2E/)

#### paper
[First data release](https://www.aclweb.org/anthology/W17-5525/),   [Detailed E2E Challenge writeup](https://doi.org/10.1016/j.csl.2019.06.009),   [Cleaned E2E version](https://www.aclweb.org/anthology/W19-8652/)

#### authors
Jekaterina Novikova, Ondrej Dusek and Verena Rieser

## Dataset Overview

### Where to find the Data and its Documentation

#### Webpage

<!-- info: What is the webpage for the dataset (if it exists)? -->
<!-- scope: telescope -->
[Website](http://www.macs.hw.ac.uk/InteractionLab/E2E/)

#### Download

<!-- info: What is the link to where the original dataset is hosted? -->
<!-- scope: telescope -->
[Github](https://github.com/tuetschek/e2e-cleaning)

#### Paper

<!-- info: What is the link to the paper describing the dataset (open access preferred)? -->
<!-- scope: telescope -->
[First data release](https://www.aclweb.org/anthology/W17-5525/),   [Detailed E2E Challenge writeup](https://doi.org/10.1016/j.csl.2019.06.009),   [Cleaned E2E version](https://www.aclweb.org/anthology/W19-8652/)

#### BibTex

<!-- info: Provide the BibTex-formatted reference for the dataset. Please use the correct published version (ACL anthology, etc.) instead of google scholar created Bibtex. -->
<!-- scope: microscope -->
```
@inproceedings{e2e_cleaned,
	address = {Tokyo, Japan},
	title = {Semantic {Noise} {Matters} for {Neural} {Natural} {Language} {Generation}},
	url = {https://www.aclweb.org/anthology/W19-8652/},
	booktitle = {Proceedings of the 12th {International} {Conference} on {Natural} {Language} {Generation} ({INLG} 2019)},
	author = {Dušek, Ondřej and Howcroft, David M and Rieser, Verena},
	year = {2019},
	pages = {421--426},
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
Dialect-specific data was not collected and the language is general British English. 

#### Covered Languages

<!-- quick -->
<!-- info: What languages/dialects are covered in the dataset? -->
<!-- scope: telescope -->
`English`

#### Whose Language?

<!-- info: Whose language is in the dataset? -->
<!-- scope: periscope -->
The original dataset was collected using the CrowdFlower (now Appen) platform using native English speakers (self-reported). No demographic information was provided, but the collection was geographically limited to English-speaking countries. 

#### License

<!-- quick -->
<!-- info: What is the license of the dataset? -->
<!-- scope: telescope -->
cc-by-sa-4.0: Creative Commons Attribution Share Alike 4.0 International

#### Intended Use

<!-- info: What is the intended use of the dataset? -->
<!-- scope: microscope -->
The dataset was collected to test neural model on a very well specified realization task. 

#### Primary Task

<!-- info: What primary task does the dataset support? -->
<!-- scope: telescope -->
Data-to-Text

#### Communicative Goal

<!-- quick -->
<!-- info: Provide a short description of the communicative goal of a model trained for this task on this dataset. -->
<!-- scope: periscope -->
Producing a text informing/recommending a restaurant, given all and only the attributes specified on the input.


### Credit

#### Curation Organization Type(s)

<!-- info: In what kind of organization did the dataset curation happen? -->
<!-- scope: telescope -->
`academic`

#### Curation Organization(s)

<!-- info: Name the organization(s). -->
<!-- scope: periscope -->
Heriot-Watt University

#### Dataset Creators

<!-- info: Who created the original dataset? List the people involved in collecting the dataset and their affiliation(s). -->
<!-- scope: microscope -->
Jekaterina Novikova, Ondrej Dusek and Verena Rieser

#### Funding

<!-- info: Who funded the data creation? -->
<!-- scope: microscope -->
This research received funding from the EPSRC projects DILiGENt (EP/M005429/1) and MaDrIgAL (EP/N017536/1).

#### Who added the Dataset to GEM?

<!-- info: Who contributed to the data card and adding the dataset to GEM? List the people+affiliations involved in creating this data card and who helped integrate this dataset into GEM. -->
<!-- scope: microscope -->
Simon Mille wrote the initial data card and Yacine Jernite the data loader. Sebastian Gehrmann migrated the data card to the v2 format and moved the data loader to the hub.


### Dataset Structure

#### Data Fields

<!-- info: List and describe the fields present in the dataset. -->
<!-- scope: telescope -->
The data is in a CSV format, with the following fields:

* `mr` -- the meaning representation (MR, input)
* `ref` -- reference, i.e. the corresponding natural-language description (output)

There are additional fields (`fixed`, `orig_mr`) indicating whether the data was modified in the
cleaning process and what was the original MR before cleaning, but these aren't used for NLG.

The MR has a flat structure -- attribute-value pairs are comma separated, with values
enclosed in brackets (see example above). There are 8 attributes:
* `name` -- restaurant name
* `near` -- a landmark close to the restaurant
* `area` -- location (riverside, city centre)
* `food` -- food type / cuisine (e.g. Japanese, Indian, English etc.)
* `eatType` -- restaurant type (restaurant, coffee shop, pub)
* `priceRange` -- price range (low, medium, high, <£20, £20-30, >£30)
* `rating` -- customer rating (low, medium, high, 1/5, 3/5, 5/5)
* `familyFriendly` -- is the restaurant family-friendly (yes/no)

The same MR is often repeated multiple times with different synonymous references.


#### How were labels chosen?

<!-- info: How were the labels chosen? -->
<!-- scope: microscope -->
The source MRs were generated automatically at random from a set of valid attribute values. The labels were crowdsourced and are natural language

#### Example Instance

<!-- info: Provide a JSON formatted example of a typical instance in the dataset. -->
<!-- scope: periscope -->
```
{
  "input":  "name[Alimentum], area[riverside], familyFriendly[yes], near[Burger King]",
  "target": "Alimentum is a kids friendly place in the riverside area near Burger King." 
}
```

#### Data Splits

<!-- info: Describe and name the splits in the dataset if there are more than one. -->
<!-- scope: periscope -->

|             | MRs  | Distinct MRs | References |
|-------------|------|--------------|------------|
| Training    |12,568|        8,362 |    33,525  |
| Development | 1,484|        1,132 |     4,299  |
| Test        | 1,847|        1,358 |     4,693  |
| Total       |15,899|       10,852 |    42,517  |


“Distinct MRs” are MRs that remain distinct even if restaurant/place names (attributes `name`, `near`)
are delexicalized, i.e., replaced with a placeholder.

#### Splitting Criteria

<!-- info: Describe any criteria for splitting the data, if used. If there are differences between the splits (e.g., if the training annotations are machine-generated and the dev and test ones are created by humans, or if different numbers of annotators contributed to each example), describe them here. -->
<!-- scope: microscope -->
The data are divided so that MRs in different splits do not overlap.




## Dataset in GEM

### Rationale for Inclusion in GEM

#### Why is the Dataset in GEM?

<!-- info: What does this dataset contribute toward better generation evaluation and why is it part of GEM? -->
<!-- scope: microscope -->
The E2E dataset is one of the largest limited-domain NLG datasets and is frequently used as a data-to-text generation benchmark. The E2E Challenge included 20 systems of very different architectures, with system outputs available for download.



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
The dataset is much cleaner than comparable datasets, and it is also a relatively easy task, making for a straightforward evaluation. 

#### Ability that the Dataset measures

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: periscope -->
surface realization.


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
4 special test sets for E2E were added to the GEM evaluation suite.

1. We created subsets of the training and development sets of ~500 randomly selected inputs each.
2. We applied input scrambling on a subset of 500 randomly selected test instances; the order of the input properties was randomly reassigned.
3. For the input size, we created subpopulations based on the number of restaurant properties in the input.

| Input length  | Frequency English |
|---------------|-------------------|
| 2             |                 5 |
| 3             |               120 |
| 4             |               389 |
| 5             |               737 |
| 6             |              1187 |
| 7             |              1406 |
| 8             |               774 |
| 9             |                73 |
| 10            |                 2 |

#### Split Motivation

<!-- info: What aspects of the model's generation capacities were the splits created to test? -->
<!-- scope: periscope -->
Generalization and robustness


### Getting Started with the Task




## Previous Results

### Previous Results

#### Measured Model Abilities

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: telescope -->
Surface realization.

#### Metrics

<!-- info: What metrics are typically used for this task? -->
<!-- scope: periscope -->
`BLEU`, `METEOR`, `ROUGE`

#### Proposed Evaluation

<!-- info: List and describe the purpose of the metrics and evaluation methodology (including human evaluation) that the dataset creators used when introducing this task. -->
<!-- scope: microscope -->
The official evaluation script combines the MT-Eval and COCO Captioning libraries with the following metrics.

- BLEU
- CIDEr
- NIST
- METEOR
- ROUGE-L

#### Previous results available?

<!-- info: Are previous results available? -->
<!-- scope: telescope -->
yes

#### Other Evaluation Approaches

<!-- info: What evaluation approaches have others used? -->
<!-- scope: periscope -->
Most previous results, including the shared task results, used the library provided by the dataset creators. The shared task also conducted a human evaluation using the following two criteria: 

- `Quality`: When collecting quality ratings, system outputs were presented to crowd workers together with the corresponding meaning representation, which implies that correctness of the NL utterance relative to the MR should also influence this ranking. The crowd workers were asked: “How do you judge the overall quality of the utterance in terms of its grammatical correctness, fluency, adequacy and other important factors?”
- `Naturalness`: When collecting naturalness ratings, system outputs were presented to crowd workers without the corresponding meaning representation. The crowd workers were asked: “Could the utterance have been produced by a native speaker?”

#### Relevant Previous Results

<!-- info: What are the most relevant previous results for this task/dataset? -->
<!-- scope: microscope -->
The shared task writeup has in-depth evaluations of systems (https://www.sciencedirect.com/science/article/pii/S0885230819300919) 



## Dataset Curation

### Original Curation

#### Original Curation Rationale

<!-- info: Original curation rationale -->
<!-- scope: telescope -->
The dataset was collected to showcase/test neural NLG models. It is larger and contains more lexical richness and syntactic variation than previous closed-domain NLG datasets.



#### Communicative Goal

<!-- info: What was the communicative goal? -->
<!-- scope: periscope -->
Producing a text informing/recommending a restaurant, given all and only the attributes specified on the input.

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
`Other crowdworker platform`

#### Language Producers

<!-- info: What further information do we have on the language producers? -->
<!-- scope: microscope -->
Human references describing the MRs were collected by crowdsourcing on the CrowdFlower (now Appen) platform,
with either textual or pictorial MRs as a baseline. 
The pictorial MRs were used in 20% of cases -- these yield higher lexical variation but introduce noise.

#### Topics Covered

<!-- info: Does the language in the dataset focus on specific topics? How would you describe them? -->
<!-- scope: periscope -->
The dataset is focused on descriptions of restaurants.

#### Data Validation

<!-- info: Was the text validated by a different worker or a data curator? -->
<!-- scope: telescope -->
validated by data curator

#### Data Preprocessing

<!-- info: How was the text data pre-processed? (Enter N/A if the text was not pre-processed) -->
<!-- scope: microscope -->
There were basic checks (length, valid characters, repetition).


#### Was Data Filtered?

<!-- info: Were text instances selected or filtered? -->
<!-- scope: telescope -->
algorithmically

#### Filter Criteria

<!-- info: What were the selection criteria? -->
<!-- scope: microscope -->
The cleaned version of the dataset which we are using in GEM was algorithmically filtered. They used regular expressions to match all human-generated references with a more accurate input when attributes were hallucinated or dropped. Additionally, train-test overlap stemming from the transformation was removed. As a result, this data is much cleaner than the original dataset but not perfect (about 20% of instances may have misaligned slots, compared to 40% of the original data. 


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
Since a crowdsourcing platform was used, the involved raters waived their rights to the data and are aware that the produced annotations can be publicly released. 


### Private Identifying Information (PII)

#### Contains PII?

<!-- quick -->
<!-- info: Does the source language data likely contain Personal Identifying Information about the data creators or subjects? -->
<!-- scope: telescope -->
no PII

#### Justification for no PII

<!-- info: Provide a justification for selecting `no PII` above. -->
<!-- scope: periscope -->
The dataset is artificial and does not contain any description of people.


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

#### Are the Language Producers Representative of the Language?

<!-- info: Does the distribution of language producers in the dataset accurately represent the full distribution of speakers of the language world-wide? If not, how does it differ? -->
<!-- scope: periscope -->
The source data is generated randomly, so it should not contain biases. The human references may be biased by the workers' demographic, but that was not investigated upon data collection.



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
The cleaned version still has data points with hallucinated or omitted attributes. 

#### Unsuited Applications

<!-- info: When using a model trained on this dataset in a setting where users or the public may interact with its predictions, what are some pitfalls to look out for? In particular, describe some applications of the general task featured in this dataset that its curation or properties make it less suitable for. -->
<!-- scope: microscope -->
The data only pertains to the restaurant domain and the included attributes. A model cannot be expected to handle other domains or attributes. 


