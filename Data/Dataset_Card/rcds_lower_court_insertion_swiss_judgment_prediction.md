---
annotations_creators:
- expert-generated
language:
- de
- fr
- it
- en
language_creators:
- expert-generated
- found
license:
- cc-by-sa-4.0
multilinguality:
- multilingual
pretty_name: LowerCourtInsertionSwissJudgmentPrediction
size_categories:
- 1K<n<10K
source_datasets:
- extended|swiss_judgment_prediction
tags:
- explainability-judgment-prediction
task_categories:
- text-classification
- other
task_ids: []
---

# Dataset Card for "LowerCourtInsertionSwissJudgmentPrediction": An implementation of lower court insertion bias analysis for Swiss judgment prediction

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Summary](#dataset-summary)
  - [Documents](#documents)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset **str**ucture](#dataset-**str**ucture)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Summary

This dataset contains an implementation of lower-court-insertion for the SwissJudgmentPrediction task.
Note that this dataset only provides a test set and should be used in comination with the [Swiss-Judgment-Prediction](https://huggingface.co/datasets/swiss_judgment_prediction) dataset.


### Documents
Lower-Court-Insertion-Swiss-Judgment-Prediction is a subset of the [Swiss-Judgment-Prediction](https://huggingface.co/datasets/swiss_judgment_prediction) dataset.
The Swiss-Judgment-Prediction dataset is a multilingual, diachronic dataset of 85K Swiss Federal Supreme Court (FSCS) cases annotated with the respective binarized judgment outcome (approval/dismissal), the publication year, the legal area and the canton of origin per case. Lower-Court-Insertion-Swiss-Judgment-Prediction extends this dataset by adding lower court insertion.
### Supported Tasks and Leaderboards

LowerCourtInsertionSwissJudgmentPrediction can be used for performing the LowerCourtInsertion in the legal judgment prediction task.

### Languages

Switzerland has four official languages with 3 languages (German, French and Italian) being represented in more than 1000 Swiss Federal Supreme court decisions. The decisions are written by the judges and clerks in the language of the proceedings.

## Dataset structure

### Data Instances
#### Multilingual use of the dataset

When the dataset is used in a multilingual setting selecting the the 'all' flag:

```python
from datasets import load_dataset
dataset = load_dataset('rcds/lower_court_insertion_swiss_judgment_prediction', 'all')
```



#### Monolingual use of the dataset

When the dataset is used in a monolingual setting selecting the ISO language code for one of the 3 supported languages. For example:

```python
from datasets import load_dataset
dataset = load_dataset('rcds/lower-court-insertion_swiss_judgment_prediction', 'de')
```

### Data Fields

The following data fields are provided for documents (train, validation):

id: (**int**) a unique identifier of the for the document
year: (**int**) the publication year
text: (**str**) the facts of the case
label: (class label) the judgment outcome: 0 (dismissal) or 1 (approval)
language: (**str**) one of (de, fr, it)
region: (**str**) the region of the lower court
canton: (**str**) the canton of the lower court
legal area: (**str**) the legal area of the case


The following data fields are provided for documents (test):

id: (**int**) a unique identifier of the for the document
year: (**int**) the publication year
label: (**str**) the judgment outcome: dismissal or approval
language: (**str**) one of (de, fr, it)
region: (**str**) the region of the lower court
canton: (**str**) the canton of the lower court
legal area: (**str**) the legal area of the case
explainability_label: (**str**) the explainability label assigned to the occluded text: Lower court, Baseline
text: (**str**) the facts of the case w/o the occluded text except for cases w/ explainability label "Baseline" (contain entire facts)
lower_court: (**str**) the inserted lower_court (for Baseline there is no insertion)

### Data Splits (Including Swiss Judgment Prediction)

Language |	Subset |	Number of Documents (Training/Validation/Test)
|-----|-----|------|
German| 	de| 	35'452 / 4'705 / __378__
French |	fr|	21'179 / 3'095 / __414__
Italian |	it| 	3'072 / 408 / __335__
All |	all |	59'709 / 8'208 / __1127__


## Dataset Creation

### Curation Rationale

The dataset was curated by Niklaus et al. (2021) and Nina Baumgartner.

### Source Data

#### Initial Data Collection and Normalization

The original data are available at the Swiss Federal Supreme Court (https://www.bger.ch) in unprocessed formats (HTML). The documents were downloaded from the Entscheidsuche portal (https://entscheidsuche.ch) in HTML.

#### Who are the source language producers?

Switzerland has four official languages with 3 languages (German, French and Italian) being represented in more than 1000 Swiss Federal Supreme court decisions. The decisions are written by the judges and clerks in the language of the proceedings.

### Annotations

#### Annotation process

The decisions have been annotated with the binarized judgment outcome using parsers and regular expressions. In addition the a subset of the test set (27 cases in German, 24 in French and 23 in Italian spanning over the years 2017 an 20200) was annotated by legal experts with the lower court. These lower court annotations were then use the insert each lower court into each case once (instead of the original lower court). Allowing an analysis of the changes in the models performance for each inserted lower court, giving insight into a possible bias among them. The legal expert annotation were conducted from April 2020 to August 2020.

#### Who are the annotators?

Joel Niklaus and Adrian Jörg annotated the binarized judgment outcomes. Metadata is published by the Swiss Federal Supreme Court (https://www.bger.ch). The group of legal experts consists of Thomas Lüthi (lawyer), Lynn Grau (law student at master's level) and Angela Stefanelli (law student at master's level).

### Personal and Sensitive Information

The dataset contains publicly available court decisions from the Swiss Federal Supreme Court. Personal or sensitive information has been anonymized by the court before publication according to the following guidelines: https://www.bger.ch/home/juridiction/anonymisierungsregeln.html.

## Additional Information

### Dataset Curators

Niklaus et al. (2021) and Nina Baumgartner

### Licensing Information

We release the data under CC-BY-4.0 which complies with the court licensing (https://www.bger.ch/files/live/sites/bger/files/pdf/de/urteilsveroeffentlichung_d.pdf)

© Swiss Federal Supreme Court, 2000-2020

The copyright for the editorial content of this website and the consolidated texts, which is owned by the Swiss Federal Supreme Court, is licensed under the Creative Commons Attribution 4.0 International licence. This means that you can re-use the content provided you acknowledge the source and indicate any changes you have made.

Source: https://www.bger.ch/files/live/sites/bger/files/pdf/de/urteilsveroeffentlichung_d.pdf

### Citation Information

```
@misc{baumgartner_nina_occlusion_2019,
	title = {From Occlusion to Transparancy – An Occlusion-Based Explainability Approach for Legal Judgment Prediction in Switzerland},
	shorttitle = {From Occlusion to Transparancy},
	abstract = {Natural Language Processing ({NLP}) models have been used for more and more complex tasks such as Legal Judgment Prediction ({LJP}). A {LJP} model predicts the outcome of a legal case by utilizing its facts. This increasing deployment of Artificial Intelligence ({AI}) in high-stakes domains such as law and the involvement of sensitive data has increased the need for understanding such systems. We propose a multilingual occlusion-based explainability approach for {LJP} in Switzerland and conduct a study on the bias using Lower Court Insertion ({LCI}). We evaluate our results using different explainability metrics introduced in this thesis and by comparing them to high-quality Legal Expert Annotations using Inter Annotator Agreement. Our findings show that the model has a varying understanding of the semantic meaning and context of the facts section, and struggles to distinguish between legally relevant and irrelevant sentences. We also found that the insertion of a different lower court can have an effect on the prediction, but observed no distinct effects based on legal areas, cantons, or regions. However, we did identify a language disparity with Italian performing worse than the other languages due to representation inequality in the training data, which could lead to potential biases in the prediction in multilingual regions of Switzerland. Our results highlight the challenges and limitations of using {NLP} in the judicial field and the importance of addressing concerns about fairness, transparency, and potential bias in the development and use of {NLP} systems. The use of explainable artificial intelligence ({XAI}) techniques, such as occlusion and {LCI}, can help provide insight into the decision-making processes of {NLP} systems and identify areas for improvement. Finally, we identify areas for future research and development in this field in order to address the remaining limitations and challenges.},
	author = {{Baumgartner, Nina}},
	year = {2022},
	langid = {english}
	}
```

### Contributions

Thanks to [@ninabaumgartner](https://github.com/ninabaumgartner) for adding this dataset.
