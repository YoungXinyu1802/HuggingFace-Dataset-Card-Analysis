# Dataset Card for Fake-news-latam-omdena

## Table of Contents
- [Table of Contents](#table-of-contents)
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

- **Homepage:**[latam-chapters-news-detector](https://github.com/OmdenaAI/latam-chapters-news-detector)
- **Repository:**[latam-chapters-news-detector](https://github.com/OmdenaAI/latam-chapters-news-detector)
- **Paper:**
- **Leaderboard:**
- **Point of Contact:**

### Dataset Summary

Since the Cambridge Analytica scandal a pandora box has been opened around the world, bringing to light campaigns even involving our current Latinamerica leaders manipulating public opinion through social media to win an election. There is a common and simple pattern that includes platforms such as facebook and fake news, where the candidates are able to build a nefarious narrative for their own benefit. This fact is a growing concern for our democracies, as many of these practices have been widely spread across the region and more people are gaining access to the internet. Thus, it is a necessity to be able to advise the population, and for that we have to be able to quickly spot these plots on the net before the damage is irreversible.

Therefore, an initial effort was taken to collect this dataset which gathered news from different news sources in Mexico, Colombia and El Salvador. With the objective to train a classification model and deploy it as part of the Politics Fake News Detector in LATAM (Latin America) project [https://github.com/OmdenaAI/latam-chapters-news-detector].

Website articles and tweets were considered. 

### Supported Tasks and Leaderboards

Binary fake news classification [with classes "True" and "Fake"]

### Languages

Spanish only

## Dataset Structure

### Data Instances

* Train: 2782
* Test: 310

### Data Fields

[More Information Needed]

### Data Splits

Train and test. Each split was generated with a stratified procedure in order to have the same proportion of fake news in both train and test.

Around 1/3 of the observations in each split have the label 'Fake', while 2/3 have the label 'True'.

## Dataset Creation

### Curation Rationale

For a more specific flow of how the labeling was done, follow this link: https://github.com/OmdenaAI/latam-chapters-news-detector/blob/main/Fake-news_Flowchart.pdf

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

Once the capacity to somewhat detect irregularities in the news activity on the internet is developed, we might be able to counter the disinformation with the help of additional research. As we reduce the time spent in looking for those occurrences, more time can be used in validating the results and uncovering the truth; enabling researchers, journalists and organizations to help people make an informed decision whether the public opinion is true or not, so that they can identify on their own if someone is trying to manipulate them for a certain political benefit.
If this matter isn’t tackled with enough urgency, we might see the rise of a new dark era in latin america politics, where many unscrupulous parties and people will manage to gain power and control the lives of many people.

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

[More Information Needed]

### Licensing Information

[More Information Needed]

### Citation Information

[More Information Needed]

### Contributions

Thanks to the Omdena local chapter members from Mexico, Colombia and El Salvador for their amazing effort to collect and curate this dataset.