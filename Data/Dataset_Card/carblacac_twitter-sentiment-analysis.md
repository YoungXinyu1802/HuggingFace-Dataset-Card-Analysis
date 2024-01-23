---
pretty_name: "TSATC: Twitter Sentiment Analysis Training Corpus"
annotations_creators:
- expert-generated
language_creators:
- other
language:
- en
license:
- apache-2.0
multilinguality:
- monolingual
size_categories:
- 100K<n<1M
source_datasets:
- original
task_categories:
- text-classification
task_ids:
- feeling-classification
paperswithcode_id: other
configs:
- None
---
# Dataset Card for TSATC: Twitter Sentiment Analysis Training Corpus
## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
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
  - [Contributions](#contributions)
## Dataset Description
- **Homepage:** [TSATC](https://github.com/cblancac/SentimentAnalysisBert/blob/main/data)
- **Repository:** [TSATC](https://github.com/cblancac/SentimentAnalysisBert/blob/main/data)
- **Paper:** [TSATC: Twitter Sentiment Analysis Training Corpus](http://thinknook.com/twitter-sentiment-analysis-training-corpus-dataset-2012-09-22/)
- **Point of Contact:** [Carlos Blanco](carblacac7@gmail.com)
### Dataset Summary
TSATC: Twitter Sentiment Analysis Training Corpus
The original Twitter Sentiment Analysis Dataset contains 1,578,627 classified tweets, each row is marked as 1 for positive sentiment and 0 for negative sentiment. It can be downloaded from http://thinknook.com/wp-content/uploads/2012/09/Sentiment-Analysis-Dataset.zip. 
The dataset is based on data from the following two sources:

University of Michigan Sentiment Analysis competition on Kaggle
Twitter Sentiment Corpus by Niek Sanders

This dataset has been transformed, selecting in a random way a subset of them, applying a cleaning process, and dividing them between the test and train subsets, keeping a balance between the number of positive and negative tweets within each of these subsets. These two files can be founded on https://github.com/cblancac/SentimentAnalysisBert/blob/main/data. 

Finally, the train subset has been divided in two smallest datasets, train (80%) and validation (20%). The final dataset has been created with these two new subdatasets plus the previous test dataset. 
### Supported Tasks and Leaderboards
[More Information Needed]
### Languages
The text in the dataset is in English.
## Dataset Structure
### Data Instances
Below are two examples from the dataset:




|     | Text                              | Feeling |
| :-- | :----------------------------     | :------ |
| (1) | blaaah. I don't feel good aagain. | 0       |
| (2) | My birthday is coming June 3.     | 1       |

### Data Fields
In the final dataset, all files are in the JSON format with f columns:

| Column Name   | Data                        |
| :------------ | :-------------------------- |
| text          | A sentence (or tweet)       |
| feeling       | The feeling of the sentence |

Each feeling has two possible values: `0` indicates the sentence has a negative sentiment, while `1` indicates a positive feeling.
### Data Splits
The number of examples and the proportion sentiments are shown below:

| Data                | Train   | Validation    | Test  |
| :------------------ | ------: | ------------: | ----: |
| Size                | 119.988 | 29.997      |  61.998 |
| Labeled positive    | 60.019  | 14.947      | 31029   |
| Labeled negative    | 59.969  | 15.050      | 30969   |
## Dataset Creation
### Curation Rationale
Existing paraphrase identification datasets lack sentence pairs that have high lexical overlap without being paraphrases. Models trained on such data fail to distinguish pairs like *flights from New York to Florida* and *flights from Florida to New York*.
### Source Data
#### Initial Data Collection and Normalization
[More Information Needed]
#### Who are the source language producers?
Mentioned above.
### Annotations
#### Annotation process
[More Information Needed]
#### Who are the annotators?
[More Information Needed]
### Personal and Sensitive Information
[More Information Needed]
## Considerations for Using the Data
### Social Impact of Dataset
[More Information Needed]
### Discussion of Biases
[More Information Needed]
### Other Known Limitations
[More Information Needed]
## Additional Information
### Dataset Curators
[More Information Needed]
### Citation Information
```
@InProceedings{paws2019naacl,
  title = {{TSATC: Twitter Sentiment Analysis Training Corpus}},
  author = {Ibrahim Naji},
  booktitle = {thinknook},
  year = {2012}
}
```
### Contributions
Thanks to myself [@carblacac](https://github.com/cblancac/) for adding this transformed dataset from the original one.