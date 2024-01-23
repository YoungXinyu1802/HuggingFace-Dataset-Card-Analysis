---
annotations_creators:
- none
language_creators:
- unknown
language:
- ar
- en
- fr
- ha
- ig
- pt
- ru
- sw
- yo
multilinguality:
- yes
size_categories:
- unknown
source_datasets:
- original
task_categories:
- table-to-text
task_ids: []
pretty_name: TaTA
tags:
- data-to-text
license: cc-by-sa-4.0
dataset_info:
  features:
  - name: gem_id
    dtype: string
  - name: example_id
    dtype: string
  - name: title
    dtype: string
  - name: unit_of_measure
    dtype: string
  - name: chart_type
    dtype: string
  - name: was_translated
    dtype: string
  - name: table_data
    dtype: string
  - name: linearized_input
    dtype: string
  - name: table_text
    sequence: string
  - name: target
    dtype: string
  splits:
  - name: ru
    num_bytes: 308435
    num_examples: 210
  - name: test
    num_bytes: 1691383
    num_examples: 763
  - name: train
    num_bytes: 10019272
    num_examples: 6962
  - name: validation
    num_bytes: 1598442
    num_examples: 754
  download_size: 18543506
  dataset_size: 13617532
---


# Dataset Card for GEM/TaTA

## Dataset Description

- **Homepage:** https://github.com/google-research/url-nlp
- **Repository:** https://github.com/google-research/url-nlp
- **Paper:** https://arxiv.org/abs/2211.00142
- **Leaderboard:** https://github.com/google-research/url-nlp
- **Point of Contact:** Sebastian Ruder

### Link to Main Data Card

You can find the main data card on the [GEM Website](https://gem-benchmark.com/data_cards/TaTA).

### Dataset Summary

Existing data-to-text generation datasets are mostly limited to English. Table-to-Text in African languages (TaTA) addresses this lack of data as the first large multilingual table-to-text dataset with a focus on African languages. TaTA was created by transcribing figures and accompanying text in bilingual reports by the Demographic and Health Surveys Program, followed by professional translation to make the dataset fully parallel. TaTA includes 8,700 examples in nine languages including four African languages (Hausa, Igbo, Swahili, and Yorùbá) and a zero-shot test language (Russian).

You can load the dataset via:
```
import datasets
data = datasets.load_dataset('GEM/TaTA')
```
The data loader can be found [here](https://huggingface.co/datasets/GEM/TaTA).

#### website
[Github](https://github.com/google-research/url-nlp)

#### paper
[ArXiv](https://arxiv.org/abs/2211.00142)

#### authors
Sebastian Gehrmann, Sebastian Ruder , Vitaly Nikolaev, Jan A. Botha, Michael Chavinda, Ankur Parikh, Clara Rivera

## Dataset Overview

### Where to find the Data and its Documentation

#### Webpage

<!-- info: What is the webpage for the dataset (if it exists)? -->
<!-- scope: telescope -->
[Github](https://github.com/google-research/url-nlp)

#### Download

<!-- info: What is the link to where the original dataset is hosted? -->
<!-- scope: telescope -->
[Github](https://github.com/google-research/url-nlp)

#### Paper

<!-- info: What is the link to the paper describing the dataset (open access preferred)? -->
<!-- scope: telescope -->
[ArXiv](https://arxiv.org/abs/2211.00142)

#### BibTex

<!-- info: Provide the BibTex-formatted reference for the dataset. Please use the correct published version (ACL anthology, etc.) instead of google scholar created Bibtex. -->
<!-- scope: microscope -->
```
@misc{gehrmann2022TaTA,
  Author = {Sebastian Gehrmann and Sebastian Ruder and Vitaly Nikolaev and Jan A. Botha and Michael Chavinda and Ankur Parikh and Clara Rivera},
  Title = {TaTa: A Multilingual Table-to-Text Dataset for African Languages},
  Year = {2022},
  Eprint = {arXiv:2211.00142},
}
```

#### Contact Name

<!-- quick -->
<!-- info: If known, provide the name of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
Sebastian Ruder

#### Contact Email

<!-- info: If known, provide the email of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
ruder@google.com

#### Has a Leaderboard?

<!-- info: Does the dataset have an active leaderboard? -->
<!-- scope: telescope -->
yes

#### Leaderboard Link

<!-- info: Provide a link to the leaderboard. -->
<!-- scope: periscope -->
[Github](https://github.com/google-research/url-nlp)

#### Leaderboard Details

<!-- info: Briefly describe how the leaderboard evaluates models. -->
<!-- scope: microscope -->
The paper introduces a metric StATA which is trained on human ratings and which is used to rank approaches submitted to the leaderboard.


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
`English`, `Portuguese`, `Arabic`, `French`, `Hausa`, `Swahili (macrolanguage)`, `Igbo`, `Yoruba`, `Russian`

#### Whose Language?

<!-- info: Whose language is in the dataset? -->
<!-- scope: periscope -->
The language is taken from reports by the demographic and health surveys program.

#### License

<!-- quick -->
<!-- info: What is the license of the dataset? -->
<!-- scope: telescope -->
cc-by-sa-4.0: Creative Commons Attribution Share Alike 4.0 International

#### Intended Use

<!-- info: What is the intended use of the dataset? -->
<!-- scope: microscope -->
The dataset poses significant reasoning challenges and is thus meant as a way to asses the verbalization and reasoning capabilities of structure-to-text models.

#### Primary Task

<!-- info: What primary task does the dataset support? -->
<!-- scope: telescope -->
Data-to-Text

#### Communicative Goal

<!-- quick -->
<!-- info: Provide a short description of the communicative goal of a model trained for this task on this dataset. -->
<!-- scope: periscope -->
Summarize key information from a table in a single sentence.



### Credit

#### Curation Organization Type(s)

<!-- info: In what kind of organization did the dataset curation happen? -->
<!-- scope: telescope -->
`industry`

#### Curation Organization(s)

<!-- info: Name the organization(s). -->
<!-- scope: periscope -->
Google Research

#### Dataset Creators

<!-- info: Who created the original dataset? List the people involved in collecting the dataset and their affiliation(s). -->
<!-- scope: microscope -->
Sebastian Gehrmann, Sebastian Ruder , Vitaly Nikolaev, Jan A. Botha, Michael Chavinda, Ankur Parikh, Clara Rivera

#### Funding

<!-- info: Who funded the data creation? -->
<!-- scope: microscope -->
Google Research

#### Who added the Dataset to GEM?

<!-- info: Who contributed to the data card and adding the dataset to GEM? List the people+affiliations involved in creating this data card and who helped integrate this dataset into GEM. -->
<!-- scope: microscope -->
Sebastian Gehrmann (Google Research)


### Dataset Structure

#### Data Fields

<!-- info: List and describe the fields present in the dataset. -->
<!-- scope: telescope -->
- `example_id`: The ID of the example. Each ID (e.g., `AB20-ar-1`) consists of three parts: the document ID, the language ISO 639-1 code, and the index of the table within the document.
- `title`: The title of the table.
- `unit_of_measure`: A description of the numerical value of the data. E.g., percentage of households with clean water.
- `chart_type`: The kind of chart associated with the data. We consider the following (normalized) types: horizontal bar chart, map chart, pie graph, tables, line chart, pie chart, vertical chart type, line graph, vertical bar chart, and other.
- `was_translated`: Whether the table was transcribed in the original language of the report or translated.
- `table_data`: The table content is a JSON-encoded string of a two-dimensional list, organized by row, from left to right, starting from the top of the table. Number of items varies per table. Empty cells are given as empty string values in the corresponding table cell.
- `table_text`: The sentences forming the description of each table are encoded as a JSON object. In the case of more than one sentence, these are separated by commas. Number of items varies per table.
- `linearized_input`:  A single string that contains the table content separated by vertical bars, i.e., |. Including title, unit of measurement, and the content of each cell including row and column headers in between brackets, i.e., (Medium Empowerment, Mali, 17.9).

#### Reason for Structure

<!-- info: How was the dataset structure determined? -->
<!-- scope: microscope -->
The structure includes all available information for the infographics on which the dataset is based.

#### How were labels chosen?

<!-- info: How were the labels chosen? -->
<!-- scope: microscope -->
Annotators looked through English text to identify sentences that describe an infographic. They then identified the corresponding location of the parallel non-English document. All sentences were extracted.

#### Example Instance

<!-- info: Provide a JSON formatted example of a typical instance in the dataset. -->
<!-- scope: periscope -->
```
{
    "example_id": "FR346-en-39",
    "title": "Trends in early childhood mortality rates",
    "unit_of_measure": "Deaths per 1,000 live births for the 5-year period before the survey",
    "chart_type": "Line chart",
    "was_translated": "False",
    "table_data": "[[\"\", \"Child mortality\", \"Neonatal mortality\", \"Infant mortality\", \"Under-5 mortality\"], [\"1990 JPFHS\", 5, 21, 34, 39], [\"1997 JPFHS\", 6, 19, 29, 34], [\"2002 JPFHS\", 5, 16, 22, 27], [\"2007 JPFHS\", 2, 14, 19, 21], [\"2009 JPFHS\", 5, 15, 23, 28], [\"2012 JPFHS\", 4, 14, 17, 21], [\"2017-18 JPFHS\", 3, 11, 17, 19]]",
    "table_text": [
      "neonatal, infant, child, and under-5 mortality rates for the 5 years preceding each of seven JPFHS surveys (1990 to 2017-18).",
      "Under-5 mortality declined by half over the period, from 39 to 19 deaths per 1,000 live births.",
      "The decline in mortality was much greater between the 1990 and 2007 surveys than in the most recent period.",
      "Between 2012 and 2017-18, under-5 mortality decreased only modestly, from 21 to 19 deaths per 1,000 live births, and infant mortality remained stable at 17 deaths per 1,000 births."
    ],
    "linearized_input": "Trends in early childhood mortality rates | Deaths per 1,000 live births for the 5-year period before the survey | (Child mortality, 1990 JPFHS, 5) (Neonatal mortality, 1990 JPFHS, 21) (Infant mortality, 1990 JPFHS, 34) (Under-5 mortality, 1990 JPFHS, 39) (Child mortality, 1997 JPFHS, 6) (Neonatal mortality, 1997 JPFHS, 19) (Infant mortality, 1997 JPFHS, 29) (Under-5 mortality, 1997 JPFHS, 34) (Child mortality, 2002 JPFHS, 5) (Neonatal mortality, 2002 JPFHS, 16) (Infant mortality, 2002 JPFHS, 22) (Under-5 mortality, 2002 JPFHS, 27) (Child mortality, 2007 JPFHS, 2) (Neonatal mortality, 2007 JPFHS, 14) (Infant mortality, 2007 JPFHS, 19) (Under-5 mortality, 2007 JPFHS, 21) (Child mortality, 2009 JPFHS, 5) (Neonatal mortality, 2009 JPFHS, 15) (Infant mortality, 2009 JPFHS, 23) (Under-5 mortality, 2009 JPFHS, 28) (Child mortality, 2012 JPFHS, 4) (Neonatal mortality, 2012 JPFHS, 14) (Infant mortality, 2012 JPFHS, 17) (Under-5 mortality, 2012 JPFHS, 21) (Child mortality, 2017-18 JPFHS, 3) (Neonatal mortality, 2017-18 JPFHS, 11) (Infant mortality, 2017-18 JPFHS, 17) (Under-5 mortality, 2017-18 JPFHS, 19)"
  }
```

#### Data Splits

<!-- info: Describe and name the splits in the dataset if there are more than one. -->
<!-- scope: periscope -->
- `Train`: Training set, includes examples with 0 or more references.
- `Validation`: Validation set, includes examples with 3 or more references.
- `Test`: Test set, includes examples with 3 or more references.
- `Ru`: Russian zero-shot set. Includes English and Russian examples (Russian is not includes in any of the other splits).

#### Splitting Criteria

<!-- info: Describe any criteria for splitting the data, if used. If there are differences between the splits (e.g., if the training annotations are machine-generated and the dev and test ones are created by humans, or if different numbers of annotators contributed to each example), describe them here. -->
<!-- scope: microscope -->
The same table across languages is always in the same split, i.e., if table X is in the test split in language A, it will also be in the test split in language B. In addition to filtering examples without transcribed table values, every example of the development and test splits has at least 3 references.
From the examples that fulfilled these criteria, 100 tables were sampled for both development and test for a total of 800 examples each. A manual review process excluded a few tables in each set, resulting in a training set of 6,962 tables, a development set of 752 tables, and a test set of 763 tables.


####

<!-- info: What does an outlier of the dataset in terms of length/perplexity/embedding look like? -->
<!-- scope: microscope -->
There are tables without references, without values, and others that are very large. The dataset is distributed as-is, but the paper describes multiple strategies to deal with data issues.



## Dataset in GEM

### Rationale for Inclusion in GEM

#### Why is the Dataset in GEM?

<!-- info: What does this dataset contribute toward better generation evaluation and why is it part of GEM? -->
<!-- scope: microscope -->
There is no other multilingual data-to-text dataset that is parallel over languages. Moreover, over 70% of references in the dataset require reasoning and it is thus of very high quality and challenging for models.

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
More languages, parallel across languages, grounded in infographics, not centered on Western entities or source documents

#### Ability that the Dataset measures

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: periscope -->
reasoning, verbalization, content planning


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
The background section of the [paper](https://arxiv.org/abs/2211.00142) provides a list of related datasets.

#### Technical Terms

<!-- info: Technical terms used in this card and the dataset and their definitions -->
<!-- scope: microscope -->
- `data-to-text`: Term that refers to NLP tasks in which the input is structured information and the output is natural language.




## Previous Results

### Previous Results

#### Metrics

<!-- info: What metrics are typically used for this task? -->
<!-- scope: periscope -->
`Other: Other Metrics`

#### Other Metrics

<!-- info: Definitions of other metrics -->
<!-- scope: periscope -->
`StATA`: A new metric associated with TaTA that is trained on human judgments and which has a much higher correlation with them.

#### Proposed Evaluation

<!-- info: List and describe the purpose of the metrics and evaluation methodology (including human evaluation) that the dataset creators used when introducing this task. -->
<!-- scope: microscope -->
The creators used a human evaluation that measured [attribution](https://arxiv.org/abs/2112.12870) and reasoning capabilities of various models. Based on these ratings, they trained a new metric and showed that existing metrics fail to measure attribution.

#### Previous results available?

<!-- info: Are previous results available? -->
<!-- scope: telescope -->
no



## Dataset Curation

### Original Curation

#### Original Curation Rationale

<!-- info: Original curation rationale -->
<!-- scope: telescope -->
The curation rationale is to create a multilingual data-to-text dataset that is high-quality and challenging.

#### Communicative Goal

<!-- info: What was the communicative goal? -->
<!-- scope: periscope -->
The communicative goal is to describe a table in a single sentence.

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
The language was produced by USAID as part of the Demographic and Health Surveys program (https://dhsprogram.com/).

#### Topics Covered

<!-- info: Does the language in the dataset focus on specific topics? How would you describe them? -->
<!-- scope: periscope -->
The topics are related to fertility, family planning, maternal and child health, gender, and nutrition.

#### Data Validation

<!-- info: Was the text validated by a different worker or a data curator? -->
<!-- scope: telescope -->
validated by crowdworker

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
11<n<50

#### Rater Qualifications

<!-- info: Describe the qualifications required of an annotator. -->
<!-- scope: periscope -->
Professional annotator who is a fluent speaker of the respective language

#### Raters per Training Example

<!-- info: How many annotators saw each training example? -->
<!-- scope: periscope -->
0

#### Raters per Test Example

<!-- info: How many annotators saw each test example? -->
<!-- scope: periscope -->
1

#### Annotation Service?

<!-- info: Was an annotation service used? -->
<!-- scope: telescope -->
yes

#### Which Annotation Service

<!-- info: Which annotation services were used? -->
<!-- scope: periscope -->
`other`

#### Annotation Values

<!-- info: Purpose and values for each annotation -->
<!-- scope: microscope -->
The additional annotations are for system outputs and references and serve to develop metrics for this task.

#### Any Quality Control?

<!-- info: Quality control measures? -->
<!-- scope: telescope -->
validated by data curators

#### Quality Control Details

<!-- info: Describe the quality control measures that were taken. -->
<!-- scope: microscope -->
Ratings were compared to a small (English) expert-curated set of ratings to ensure high agreement. There were additional rounds of training and feedback to annotators to ensure high quality judgments.


### Consent

#### Any Consent Policy?

<!-- info: Was there a consent policy involved when gathering the data? -->
<!-- scope: telescope -->
yes

#### Other Consented Downstream Use

<!-- info: What other downstream uses of the data did the original data creators and the data curators consent to? -->
<!-- scope: microscope -->
In addition to data-to-text generation, the dataset can be used for translation or multimodal research.


### Private Identifying Information (PII)

#### Contains PII?

<!-- quick -->
<!-- info: Does the source language data likely contain Personal Identifying Information about the data creators or subjects? -->
<!-- scope: telescope -->
no PII

#### Justification for no PII

<!-- info: Provide a justification for selecting `no PII` above. -->
<!-- scope: periscope -->
The DHS program only publishes aggregate survey information and thus, no personal information is included.


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
The dataset is focusing on data about African countries and the languages included in the dataset are spoken in Africa. It aims to improve the representation of African languages in the NLP and NLG communities.


### Discussion of Biases

#### Any Documented Social Biases?

<!-- info: Are there documented social biases in the dataset? Biases in this context are variations in the ways members of different social categories are represented that can have harmful downstream consequences for members of the more disadvantaged group. -->
<!-- scope: telescope -->
no

#### Are the Language Producers Representative of the Language?

<!-- info: Does the distribution of language producers in the dataset accurately represent the full distribution of speakers of the language world-wide? If not, how does it differ? -->
<!-- scope: periscope -->
The language producers for this dataset are those employed by the DHS program which is a US-funded program. While the data is focused on African countries, there may be implicit western biases in how the data is presented.



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
While tables were transcribed in the available languages, the majority of the tables were published in English as the first language. Professional translators were used to translate the data, which makes it plausible that some translationese exists in the data. Moreover, it was unavoidable to collect reference sentences that are only partially entailed by the source tables.

#### Unsuited Applications

<!-- info: When using a model trained on this dataset in a setting where users or the public may interact with its predictions, what are some pitfalls to look out for? In particular, describe some applications of the general task featured in this dataset that its curation or properties make it less suitable for. -->
<!-- scope: microscope -->
The domain of health reports includes potentially sensitive topics relating to reproduction, violence, sickness, and death. Perceived negative values could be used to amplify stereotypes about people from the respective regions or countries. The intended academic use of this dataset is to develop and evaluate models that neutrally report the content of these tables but not use the outputs to make value judgments, and these applications are thus discouraged.
