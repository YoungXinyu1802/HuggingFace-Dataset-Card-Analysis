---
annotations_creators:
- crowdsourced
language_creators:
- crowdsourced
language:
- en
license:
- unknown
multilinguality:
- monolingual
pretty_name: 20_Newsgroups_Fixed
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- text-classification
task_ids:
- multi-class-classification
- topic-classification
---

# Dataset Card for 20_Newsgroups_Fixed

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

- **Galileo Homepage:** [Galileo ML Data Intelligence Platform](https://www.rungalileo.io)
- **Repository:** [Needs More Information]
- **Dataset Blog:** [Improving Your ML Datasets With Galileo, Part 1](https://www.rungalileo.io/blog/)
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [Needs More Information]
- **Sklearn Dataset:** [sklearn](https://scikit-learn.org/0.19/datasets/twenty_newsgroups.html#the-20-newsgroups-text-dataset)
- **20 Newsgroups Homepage:** [newsgroups homepage](http://qwone.com/~jason/20Newsgroups/)

### Dataset Summary

This dataset is a version of the [**20 Newsgroups**](https://scikit-learn.org/0.19/datasets/twenty_newsgroups.html#the-20-newsgroups-text-dataset) dataset fixed with the help of the [**Galileo ML Data Intelligence Platform**](https://www.rungalileo.io/). In a matter of minutes, Galileo enabled us to uncover and fix a multitude of errors within the original dataset. In the end, we present this improved dataset as a new standard for natural language experimentation and benchmarking using the Newsgroups dataset. 

### Curation Rationale

This dataset was created to showcase the power of Galileo as a Data Intelligence Platform. Through Galileo, we identify critical error patterns within the original Newsgroups training dataset - garbage data that do not properly fit any newsgroup label category. Moreover, we observe that these errors permeate throughout the test dataset.  

As a result of our analysis, we propose the addition of a new class to properly categorize and fix the labeling of garbage data samples: a "None" class. Galileo further enables us to quickly make these data sample changes within the training set (changing garbage data labels to None) and helps guide human re-annotation of the test set. 

#### Total Dataset Errors Fixed: 1163 *(6.5% of the dataset)*
|Errors / Split.      |Overall|     Train|      Test|
|---------------------|------:|---------:|---------:|
|Garbage samples fixed|    718|       396|       322|
|Empty samples fixed  |    445|       254|       254|
|Total samples fixed  |   1163|       650|       650|

To learn more about the process of fixing this dataset, please refer to our [**Blog**](https://www.rungalileo.io/blog).


## Dataset Structure

### Data Instances

For each data sample, there is the text of the newsgroup post, the corresponding newsgroup forum where the message was posted (label), and a data sample id. 

An example from the dataset looks as follows:
```
{'id': 1,
'text': 'I have win 3.0 and downloaded several icons and BMP\'s but I can\'t figure out\nhow to change the "wallpaper" or use the icons.  Any help would be appreciated.\n\n\nThanx,\n\n-Brando'
'label': comp.os.ms-windows.misc}
```


### Data Fields

- id: the unique numerical id associated with a data sample
- text: a string containing the text of the newsgroups message
- label: a string indicating the newsgroup forum where the sample was posted

### Data Splits

The data is split into a training and test split. To reduce bias and test generalizability across time, data samples are split between train and test depending upon whether their message was posted before or after a specific date, respectively. 

### Data Classes

The fixed data is organized into 20 newsgroup topics + a catch all "None" class. Some of the newsgroups are very closely related to each other (e.g. comp.sys.ibm.pc.hardware / comp.sys.mac.hardware), while others are highly unrelated (e.g misc.forsale / soc.religion.christian). Here is a list of the 21 classes, partitioned according to subject matter:

| comp.graphics<br>comp.os.ms-windows.misc<br>comp.sys.ibm.pc.hardware<br>comp.sys.mac.hardware<br>comp.windows.x | rec.autos<br>rec.motorcycles<br>rec.sport.baseball<br>rec.sport.hockey | sci.crypt<br><sci.electronics<br>sci.med<br>sci.space |
|:---|:---:|---:|
| misc.forsale | talk.politics.misc<br>talk.politics.guns<br>talk.politics.mideast | talk.religion.misc<br>alt.atheism<br>soc.religion.christian |
| None |
