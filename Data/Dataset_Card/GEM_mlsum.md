---
annotations_creators:
- none
language_creators:
- unknown
language:
- de
- es
license:
- other
multilinguality:
- unknown
size_categories:
- unknown
source_datasets:
- original
task_categories:
- summarization
task_ids: []
pretty_name: mlsum
---

# Dataset Card for GEM/mlsum

## Dataset Description

- **Homepage:** N/A
- **Repository:** https://gitlab.lip6.fr/scialom/mlsum_data/-/tree/master/MLSUM
- **Paper:** https://aclanthology.org/2020.emnlp-main.647/
- **Leaderboard:** N/A
- **Point of Contact:** Thomas Scialom

### Link to Main Data Card

You can find the main data card on the [GEM Website](https://gem-benchmark.com/data_cards/mlsum).

### Dataset Summary 

MLSum is a multilingual summarization dataset crawled from different news websites. The GEM version supports the German and Spanish subset alongside specifically collected challenge sets for COVID-related articles to test out-of-domain generalization.

You can load the dataset via:
```
import datasets
data = datasets.load_dataset('GEM/mlsum')
```
The data loader can be found [here](https://huggingface.co/datasets/GEM/mlsum).

#### website
N/A

#### paper
[ACL Anthology](https://aclanthology.org/2020.emnlp-main.647/)

#### authors
Thomas Scialom, Paul-Alexis Dray, Sylvain Lamprier, Benjamin Piwowarski, Jacopo Staiano

## Dataset Overview

### Where to find the Data and its Documentation

#### Download

<!-- info: What is the link to where the original dataset is hosted? -->
<!-- scope: telescope -->
[Gitlab](https://gitlab.lip6.fr/scialom/mlsum_data/-/tree/master/MLSUM)

#### Paper

<!-- info: What is the link to the paper describing the dataset (open access preferred)? -->
<!-- scope: telescope -->
[ACL Anthology](https://aclanthology.org/2020.emnlp-main.647/)

#### BibTex

<!-- info: Provide the BibTex-formatted reference for the dataset. Please use the correct published version (ACL anthology, etc.) instead of google scholar created Bibtex. -->
<!-- scope: microscope -->
```
@inproceedings{scialom-etal-2020-mlsum,
    title = "{MLSUM}: The Multilingual Summarization Corpus",
    author = "Scialom, Thomas  and
      Dray, Paul-Alexis  and
      Lamprier, Sylvain  and
      Piwowarski, Benjamin  and
      Staiano, Jacopo",
    booktitle = "Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.emnlp-main.647",
    doi = "10.18653/v1/2020.emnlp-main.647",
    pages = "8051--8067",
    abstract = "We present MLSUM, the first large-scale MultiLingual SUMmarization dataset. Obtained from online newspapers, it contains 1.5M+ article/summary pairs in five different languages {--} namely, French, German, Spanish, Russian, Turkish. Together with English news articles from the popular CNN/Daily mail dataset, the collected data form a large scale multilingual dataset which can enable new research directions for the text summarization community. We report cross-lingual comparative analyses based on state-of-the-art systems. These highlight existing biases which motivate the use of a multi-lingual dataset.",
}
```

#### Contact Name

<!-- quick -->
<!-- info: If known, provide the name of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
Thomas Scialom

#### Contact Email

<!-- info: If known, provide the email of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
{thomas,paul-alexis,jacopo}@recital.ai, {sylvain.lamprier,benjamin.piwowarski}@lip6.fr

#### Has a Leaderboard?

<!-- info: Does the dataset have an active leaderboard? -->
<!-- scope: telescope -->
no


### Languages and Intended Use

#### Multilingual?

<!-- quick -->
<!-- info: Is the dataset multilingual? -->
<!-- scope: telescope -->
yes

#### Covered Dialects

<!-- info: What dialects are covered? Are there multiple dialects per language? -->
<!-- scope: periscope -->
There is only one dialect per language, Hochdeutsch for German and Castilian Spanish for Spanish. 

#### Covered Languages

<!-- quick -->
<!-- info: What languages/dialects are covered in the dataset? -->
<!-- scope: telescope -->
`German`, `Spanish, Castilian`

#### Whose Language?

<!-- info: Whose language is in the dataset? -->
<!-- scope: periscope -->
The German articles are crawled from Süddeutsche Zeitung and the Spanish ones from El Pais.

#### License

<!-- quick -->
<!-- info: What is the license of the dataset? -->
<!-- scope: telescope -->
other: Other license

#### Intended Use

<!-- info: What is the intended use of the dataset? -->
<!-- scope: microscope -->
The intended use of this dataset is to augment existing datasets for English news summarization with additional languages. 

#### Add. License Info

<!-- info: What is the 'other' license of the dataset? -->
<!-- scope: periscope -->
Restricted to non-commercial research purposes.

#### Primary Task

<!-- info: What primary task does the dataset support? -->
<!-- scope: telescope -->
Summarization

#### Communicative Goal

<!-- quick -->
<!-- info: Provide a short description of the communicative goal of a model trained for this task on this dataset. -->
<!-- scope: periscope -->
The speaker is required to produce a high quality summary of news articles in the same language as the input article.


### Credit

#### Curation Organization Type(s)

<!-- info: In what kind of organization did the dataset curation happen? -->
<!-- scope: telescope -->
`other`

#### Curation Organization(s)

<!-- info: Name the organization(s). -->
<!-- scope: periscope -->
CNRS, Sorbonne Université, reciTAL

#### Dataset Creators

<!-- info: Who created the original dataset? List the people involved in collecting the dataset and their affiliation(s). -->
<!-- scope: microscope -->
Thomas Scialom, Paul-Alexis Dray, Sylvain Lamprier, Benjamin Piwowarski, Jacopo Staiano

#### Funding

<!-- info: Who funded the data creation? -->
<!-- scope: microscope -->
Funding information is not specified.

#### Who added the Dataset to GEM?

<!-- info: Who contributed to the data card and adding the dataset to GEM? List the people+affiliations involved in creating this data card and who helped integrate this dataset into GEM. -->
<!-- scope: microscope -->
The original data card was written by Pedro Henrique Martins (Instituto de Telecomunicações) and Sebastian Gehrmann (Google Research) extended and updated it to the v2 format. The COVID challenge set was created by Laura Perez-Beltrachini (University of Edinburgh).  Data cleaning was done by Juan Diego Rodriguez (UT  Austin).


### Dataset Structure

#### Data Fields

<!-- info: List and describe the fields present in the dataset. -->
<!-- scope: telescope -->
The data fields are:

- `text`: the source article (`string`).
- `summary`: the output summary (`string`).
- `topic`: the topic of the article (`string`).
- `url`: the article's url (`string`).
- `title`: the article's title (`string`).
- `date`: the article's date (`string`).

#### Reason for Structure

<!-- info: How was the dataset structure determined? -->
<!-- scope: microscope -->
The structure follows previously released datasets. The `topic` and `title` fields were added to enable additional tasks like title generation and topic detection.

#### How were labels chosen?

<!-- info: How were the labels chosen? -->
<!-- scope: microscope -->
They are human written highlights or summaries scraped from the same website. 

#### Example Instance

<!-- info: Provide a JSON formatted example of a typical instance in the dataset. -->
<!-- scope: periscope -->
```
{
 'date': '00/01/2010',
 'gem_id': 'mlsum_de-train-2',
 'gem_parent_id': 'mlsum_de-train-2',
 'references': [],
 'target': 'Oskar Lafontaine gibt den Parteivorsitz der Linken ab - und seine Kollegen streiten, wer ihn beerben soll. sueddeutsche.de stellt die derzeit aussichtsreichsten Anwärter für Führungsaufgaben vor. Mit Vote.',
 'text': 'Wenn an diesem Montag die Landesvorsitzenden der Linken über die Nachfolger der derzeitigen Chefs Lothar Bisky und Oskar Lafontaine sowie des Bundesgeschäftsführers Dietmar Bartsch beraten, geht es nicht nur darum, wer die Partei führen soll. Es geht auch um die künftige Ausrichtung und Stärke einer Partei, die vor allem von Lafontaine zusammengehalten worden war. Ihm war es schließlich vor fünf Jahren gelungen, aus der ostdeutschen PDS und der westedeutschen WASG eine Partei zu formen. Eine Partei allerdings, die zerrissen ist in Ost und West, in Regierungswillige und ewige Oppositionelle, in Realos und Ideologen, in gemäßigte und radikale Linke. Wir stellen mögliche Kandidaten vor. Stimmen Sie ab: Wen halten Sie für geeignet und wen für unfähig? Kampf um Lafontaines Erbe: Gregor Gysi Sollte überhaupt jemand die Partei alleine führen, wie es sich viele Ostdeutsche wünschen, käme dafür wohl nur der 62-jährige Gregor Gysi in Betracht. Er ist nach Lafontaine einer der bekanntesten Politiker der Linken und derzeit Fraktionsvorsitzender der Partei im Bundestag. Allerdings ist der ehemalige PDS-Vorsitzende und Rechtsanwalt nach drei Herzinfarkten gesundheitlich angeschlagen. Wahrscheinlich wäre deshalb, dass er die zerstrittene Partei nur übergangsweise führt. Doch noch ist nicht klar, ob eine Person allein die Partei führen soll oder eine Doppelspitze. Viele Linke wünschen sich ein Duo aus einem westdeutschen und einem ostdeutschen Politiker, Mann und Frau. Foto: Getty Images',
 'title': 'Personaldebatte bei der Linken - Wer kommt nach Lafontaine?',
 'topic': 'politik',
 'url': 'https://www.sueddeutsche.de/politik/personaldebatte-bei-der-linken-wer-kommt-nach-lafontaine-1.70041'
}
```

#### Data Splits

<!-- info: Describe and name the splits in the dataset if there are more than one. -->
<!-- scope: periscope -->
The statistics of the original dataset are:

|	               |  Dataset  | Train   | Validation  |  Test  | Mean article length | Mean summary length |  
| :---        	   | :----:   | :---:   |   :---:      |  :---:  |       :---:          |      :---:           |
| German      	   | 242,982  | 220,887 |11,394     |10,701 |570.6 (words)  | 30.36 (words)  |
| Spanish          | 290,645  | 266,367 |10,358     |13,920 |800.5 (words)  |20.71 (words)  |

The statistics of the cleaned version of the dataset are:

|	               |  Dataset  | Train   | Validation  |  Test  |
| :---        	   | :----:   | :---:   |   :---:      |  :---:  |
| German      	   | 242,835  | 220,887 |11,392     |10,695 |
| Spanish          | 283,228  |259,886  |9,977     |13,365 |

The COVID challenge sets have 5058 (de) and 1938 (es) examples. 

#### Splitting Criteria

<!-- info: Describe any criteria for splitting the data, if used. If there are differences between the splits (e.g., if the training annotations are machine-generated and the dev and test ones are created by humans, or if different numbers of annotators contributed to each example), describe them here. -->
<!-- scope: microscope -->
The training set contains data from 2010 to 2018. Data from 2019 (~10% of the dataset) is used for validation (up to May) and testing(May-December 2019). 

#### 

<!-- info: What does an outlier of the dataset in terms of length/perplexity/embedding look like? -->
<!-- scope: microscope -->
Some topics are less represented within the dataset (e.g., Financial news in German and Television in Spanish). 




## Dataset in GEM

### Rationale for Inclusion in GEM

#### Why is the Dataset in GEM?

<!-- info: What does this dataset contribute toward better generation evaluation and why is it part of GEM? -->
<!-- scope: microscope -->
As the first large-scale multilingual summarization dataset, it enables evaluation of summarization models beyond English. 

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
In our configuration, the dataset is fully non-English. 

#### Ability that the Dataset measures

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: periscope -->
Content Selection, Content Planning, Realization


### GEM-Specific Curation

#### Modificatied for GEM?

<!-- info: Has the GEM version of the dataset been modified in any way (data, processing, splits) from the original curated data? -->
<!-- scope: telescope -->
yes

#### GEM Modifications

<!-- info: What changes have been made to he original dataset? -->
<!-- scope: periscope -->
`data points removed`, `data points added`

#### Modification Details

<!-- info: For each of these changes, described them in more details and provided the intended purpose of the modification -->
<!-- scope: microscope -->
The modifications done to the original dataset are the following:

- Selection of 2 languages (Spanish and German) out of the dataset 5 languages due to copyright restrictions.
- Removal of duplicate articles.
- Manually removal of article-summary pairs for which the summary is not related to the article.
- Removal of article-summary pairs written in a different language (detected using the [langdetect](https://pypi.org/project/langdetect/) library).

#### Additional Splits?

<!-- info: Does GEM provide additional splits to the dataset? -->
<!-- scope: telescope -->
yes

#### Split Information

<!-- info: Describe how the new splits were created -->
<!-- scope: periscope -->
For both selected languages (German and Spanish), we compiled time-shifted test data in the form of new articles for the second semester of 2020 with Covid19-related keywords. We collected articles from the same German and Spanish outlets as the original MLSUM datasets (El Pais and Süddeutsche Zeitung). We used the scripts provided for the re-creation of the [MLSUM datasets](https://github.com/recitalAI/MLSUM). The new challenge test set for German contains 5058 instances and the Spanish one contains 1938.

We additionally sample 500 training and validation points as additional challenge sets to measure overfitting. 

#### Split Motivation

<!-- info: What aspects of the model's generation capacities were the splits created to test? -->
<!-- scope: periscope -->
Generalization to unseen topics. 


### Getting Started with the Task




## Previous Results

### Previous Results

#### Measured Model Abilities

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: telescope -->
Content Selection, Content Planning, Realization

#### Metrics

<!-- info: What metrics are typically used for this task? -->
<!-- scope: periscope -->
`METEOR`, `ROUGE`, `Other: Other Metrics`

#### Other Metrics

<!-- info: Definitions of other metrics -->
<!-- scope: periscope -->
Novelty: Number of generated n-grams not included in the source articles.

#### Proposed Evaluation

<!-- info: List and describe the purpose of the metrics and evaluation methodology (including human evaluation) that the dataset creators used when introducing this task. -->
<!-- scope: microscope -->
ROUGE and METEOR both measure n-gram overlap with a focus on recall and are standard summarization metrics. Novelty is often reported alongside them to characterize how much a model diverges from its inputs. 

#### Previous results available?

<!-- info: Are previous results available? -->
<!-- scope: telescope -->
yes

#### Other Evaluation Approaches

<!-- info: What evaluation approaches have others used? -->
<!-- scope: periscope -->
The GEM benchmark results (https://gem-benchmark.com/results) report a wide range of metrics include lexical overlap metrics but also semantic ones like BLEURT and BERT-Score.



## Dataset Curation

### Original Curation

#### Original Curation Rationale

<!-- info: Original curation rationale -->
<!-- scope: telescope -->
The rationale was to create a multilingual news summarization dataset that mirrors the format of popular English datasets like XSum or CNN/DM. 

#### Communicative Goal

<!-- info: What was the communicative goal? -->
<!-- scope: periscope -->
The speaker is required to produce a high quality summary of news articles in the same language as the input article.

#### Sourced from Different Sources

<!-- info: Is the dataset aggregated from different data sources? -->
<!-- scope: telescope -->
yes

#### Source Details

<!-- info: List the sources (one per line) -->
<!-- scope: periscope -->
www.lemonde.fr
www.sueddeutsche.de
www.elpais.com
www.mk.ru
www.internethaber.com


### Language Data

#### How was Language Data Obtained?

<!-- info: How was the language data obtained? -->
<!-- scope: telescope -->
`Found`

#### Where was it found?

<!-- info: If found, where from? -->
<!-- scope: telescope -->
`Multiple websites`

#### Language Producers

<!-- info: What further information do we have on the language producers? -->
<!-- scope: microscope -->
The language producers are professional journalists. 

#### Topics Covered

<!-- info: Does the language in the dataset focus on specific topics? How would you describe them? -->
<!-- scope: periscope -->
4/5 of the original languages report their topics (except Turkish) and the distributions differ between sources. The dominant topics in German are Politik, Sport, Wirtschaft (economy). The dominant topics in Spanish are actualidad (current news) and opinion. French and Russian are different as well but we omit these languages in the GEM version. 

#### Data Validation

<!-- info: Was the text validated by a different worker or a data curator? -->
<!-- scope: telescope -->
not validated

#### Was Data Filtered?

<!-- info: Were text instances selected or filtered? -->
<!-- scope: telescope -->
algorithmically

#### Filter Criteria

<!-- info: What were the selection criteria? -->
<!-- scope: microscope -->
In the original dataset, only one filter was applied: all the articles shorter than 50 words or summaries shorter than 10 words are discarded. 

The GEM version additionally applies langID filter to ensure that articles are in the correct language. 


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
The copyright remains with the original data creators and the usage permission is restricted to non-commercial uses. 


### Private Identifying Information (PII)

#### Contains PII?

<!-- quick -->
<!-- info: Does the source language data likely contain Personal Identifying Information about the data creators or subjects? -->
<!-- scope: telescope -->
yes/very likely

#### Categories of PII

<!-- info: What categories of PII are present or suspected in the data? -->
<!-- scope: periscope -->
`sensitive information`, `generic PII`

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


