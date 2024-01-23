annotations_creators:
- other
language:
- en
language_creators:
- found
license:
- gpl-3.0
multilinguality:
- monolingual
pretty_name: The World's Sentiment
size_categories:
- 1K<n<10K
source_datasets:
- original
task_categories:
- other
task_ids: []

# Dataset Card for The World's Sentiment

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

- **Homepage:** [TWS Homepage](the-worlds-sentiment.enzon3.repl.co)
- **Repository:** [GitHub](https://github.com/EnZon3/TWS-dataset_gen)
- **Paper:** [Needs More Information]
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [Needs More Information]

### Dataset Summary

The World's Sentiment is a dataset of news headlines' titles and their sentiment scores. This dataset was for a project of mine to see how positive or negative events in the world are. There are some use cases for this dataset, if you use only the headlines, you could train an AI to generate fake, but realistic headlines. But if you opt for what I did, which was to analyze the dataset, you'll find quite a bit of interesting stuff.

### Supported Tasks and Leaderboards

[Needs More Information]

### Languages

This dataset is in English, text is from news articles' titles, provided by [News API](https://newsapi.org)
The associated BCP-47 code is `en`.

## Dataset Structure

### Data Instances

A typical data point comprises of a title, and the title's sentiment score. The dataset is a CSV file, so I cannot provide JSON data, but I can provide an example of what it would look like in Excel.

| Headline | Sentiment score |
| ----- | ---- |
|  Russia Ukraine: Russian missile strike hits crowded shopping mall in Kremenchuk - 9News | -0.181818182 |

Here's what the example would look like in plain-text:

Russia Ukraine: Russian missile strike hits crowded shopping mall in Kremenchuk - 9News,-0.181818182

### Data Fields

Headline:

The title to a headline

Sentiment:

The sentiment score of the headline's title.

### Data Splits

[N/A]

## Dataset Creation

### Curation Rationale

I created the TWS dataset after a question popped up in my head on June 27th. It kind of went like this: 'How negative, or positive are news headlines?'

### Source Data

#### Initial Data Collection and Normalization

The data was collected by getting the top headlines in every English-speaking country that [News API](https://newsapi.org) supported and running through the responses and logging only the titles, while also simultaneously using Sentiment analysis to get the sentiment score (The sentiment dataset I used was afinn). The data was slightly modified in it's final form to correct any syntax errors in the CSV file using [CSVlint](https://csvlint.io/) to find them. The dataset is not tokenized.

#### Who are the source language producers?

The data was made by humans, and the news sources I used are located [here](https://newsapi.org/docs/endpoints/sources), because there are so many that I can't put them here.

### Annotations

#### Annotation process

[N/A]

#### Who are the annotators?

[N/A]

### Personal and Sensitive Information

Names might show up in the titles.

## Considerations for Using the Data

### Social Impact of Dataset

[Needs More Information]

### Discussion of Biases

[Needs More Information]

### Other Known Limitations

[Needs More Information]

## Additional Information

### Dataset Curators

[Needs More Information]

### Licensing Information

[Needs More Information]

### Citation Information

[Needs More Information]