# Dataset Card for new_dataset

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-instances)
  - [Data Splits](#data-instances)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)

## Dataset Description

- **Homepage:** https://crisisnlp.qcri.org/humaid_dataset
- **Repository:** https://crisisnlp.qcri.org/data/humaid/humaid_data_all.zip
- **Paper:** https://ojs.aaai.org/index.php/ICWSM/article/view/18116/17919
<!-- - **Leaderboard:** [Needs More Information] -->
<!-- - **Point of Contact:** [Needs More Information] -->

### Dataset Summary

The HumAID Twitter dataset consists of several thousands of manually annotated tweets that has been collected during 19 major natural disaster events including earthquakes, hurricanes, wildfires, and floods, which happened from 2016 to 2019 across different parts of the World. The annotations in the provided datasets consists of following humanitarian categories. The dataset consists only english tweets and it is the largest dataset for crisis informatics so far.
** Humanitarian categories **
- Caution and advice
- Displaced people and evacuations
- Dont know cant judge
- Infrastructure and utility damage
- Injured or dead people
- Missing or found people
- Not humanitarian
- Other relevant information
- Requests or urgent needs
- Rescue volunteering or donation effort
- Sympathy and support

The resulting annotated dataset consists of 11 labels. 

### Supported Tasks and Benchmark
The dataset can be used to train a model for multiclass tweet classification for disaster response. The benchmark results can be found in https://ojs.aaai.org/index.php/ICWSM/article/view/18116/17919.

Dataset is also released with event-wise and JSON objects for further research.
Full set of the dataset can be found in https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/A7NVF7

### Languages

English

## Dataset Structure

### Data Instances

```
{

"tweet_text": "@RT_com: URGENT: Death toll in #Ecuador #quake rises to 233 \u2013 President #Correa #1 in #Pakistan", 

"class_label": "injured_or_dead_people"

}
```
### Data Fields

* tweet_text: corresponds to the tweet text.
* class_label: corresponds to a label assigned to a given tweet text


### Data Splits

* Train
* Development
* Test

## Dataset Creation

<!-- ### Curation Rationale -->

### Source Data

#### Initial Data Collection and Normalization

Tweets has been collected during several disaster events. 


### Annotations

#### Annotation process

AMT has been used to annotate the dataset. Please check the paper for a more detail. 

#### Who are the annotators?

- crowdsourced


<!-- ## Considerations for Using the Data -->

<!-- ### Social Impact of Dataset -->



<!-- ### Discussion of Biases -->

<!-- [Needs More Information] -->

<!-- ### Other Known Limitations -->

<!-- [Needs More Information] -->

## Additional Information

### Dataset Curators

Authors of the paper. 


### Licensing Information

- cc-by-nc-4.0

### Citation Information

```
@inproceedings{humaid2020,
Author = {Firoj Alam, Umair Qazi, Muhammad Imran, Ferda Ofli},
booktitle={Proceedings of the Fifteenth International AAAI Conference on Web and Social Media},
series={ICWSM~'21},
Keywords = {Social Media, Crisis Computing, Tweet Text Classification, Disaster Response},
Title = {HumAID: Human-Annotated Disaster Incidents Data from Twitter},
Year = {2021},
publisher={AAAI},
address={Online},
}
```