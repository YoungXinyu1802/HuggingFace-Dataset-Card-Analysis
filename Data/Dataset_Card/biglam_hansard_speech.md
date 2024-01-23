---
annotations_creators:
- no-annotation
language:
- 'en'
language_creators:
- expert-generated
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: Hansard Speeches
size_categories:
- 1M<n<10M
source_datasets:
- original
tags:
- speeches
- politics
- parliament
- British
task_categories:
- text-classification
- text-generation
task_ids:
- multi-class-classification
- language-modeling
- masked-language-modeling
---

# Dataset Card for Hansard speech

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

- **Homepage:** https://evanodell.com/projects/datasets/hansard-data/
- **Repository:** https://github.com/evanodell/hansard-data3
- **Paper:** [Needs More Information]
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [Evan Odell](https://github.com/evanodell)

### Dataset Summary

A dataset containing every speech in the House of Commons from May 1979-July 2020. Quoted from the dataset homepage

> Please contact me if you find any errors in the dataset. The integrity of the public Hansard record is questionable at times, and while I have improved it, the data is presented "as is".

### Supported Tasks and Leaderboards

- `text-classification`: This dataset can be used to classify various texts (transcribed from speeches) as different time periods or as different types
- `language-modeling`: This dataset can contribute to the training or the evaluation of language models for historical texts.

### Languages

`en:GB`

## Dataset Structure

### Data Instances

```
{
  'id': 'uk.org.publicwhip/debate/1979-05-17a.390.0', 
  'speech': "Since the Minister for Consumer Affairs said earlier that the bread price rise would be allowed, in view of developing unemployment in the baking industry, and since the Mother's Pride bakery in my constituency is about to close, will the right hon. Gentleman give us a firm assurance that there will be an early debate on the future of the industry, so that the Government may announce that, thanks to the price rise, those workers will not now be put out of work?", 
  'display_as': 'Eric Heffer', 
  'party': 'Labour', 
  'constituency': 'Liverpool, Walton', 
  'mnis_id': '725', 
  'date': '1979-05-17', 
  'time': '', 
  'colnum': '390', 
  'speech_class': 'Speech', 
  'major_heading': 'BUSINESS OF THE HOUSE', 
  'minor_heading': '', 
  'oral_heading': '', 
  'year': '1979', 
  'hansard_membership_id': '5612', 
  'speakerid': 'uk.org.publicwhip/member/11615', 
  'person_id': '', 
  'speakername': 'Mr. Heffer', 
  'url': '', 
  'government_posts': [], 
  'opposition_posts': [], 
  'parliamentary_posts': ['Member, Labour Party National Executive Committee']
}
```

### Data Fields

|Variable|Description|
|---|---|
|id|The ID as assigned by mysociety|
|speech|The text of the speech|
|display_as|	The standardised name of the MP.|
|party|The party an MP is member of at time of speech|
|constituency|	Constituency represented by MP at time of speech|
|mnis_id|	The MP's Members Name Information Service number|
|date|Date of speech|
|time|Time of speech|
|colnum	|Column number in hansard record|
|speech_class	|Type of speech|
|major_heading|	Major debate heading|
|minor_heading|	Minor debate heading|
|oral_heading|	Oral debate heading|
|year	|Year of speech|
|hansard_membership_id|	ID used by mysociety|
|speakerid	|ID used by mysociety|
|person_id	|ID used by mysociety|
|speakername|	MP name as appeared in Hansard record for speech|
|url| link to speech|
|government_posts|	Government posts held by MP (list)|
|opposition_posts	|Opposition posts held by MP (list)|
|parliamentary_posts|	Parliamentary posts held by MP (list)|

### Data Splits

Train: 2694375

## Dataset Creation

### Curation Rationale

This dataset contains all the speeches made in the House of Commons and can be used for a number of deep learning tasks like detecting how language and societal views have changed over the >40 years. The dataset also provides language closer to the spoken language used in an elite British institution. 

### Source Data

#### Initial Data Collection and Normalization

The dataset is created by getting the data from [data.parliament.uk](http://data.parliament.uk/membersdataplatform/memberquery.aspx). There is no normalization.

#### Who are the source language producers?

[N/A]

### Annotations

#### Annotation process

None

#### Who are the annotators?

[N/A]

### Personal and Sensitive Information

This is public information, so there should not be any personal and sensitive information

## Considerations for Using the Data

### Social Impact of Dataset

The purpose of this dataset is to understand how language use and society's views have changed over time. 

### Discussion of Biases

Because of the long time period this dataset spans, it might contain language and opinions that are unacceptable in modern society. 

### Other Known Limitations

[Needs More Information]

## Additional Information

### Dataset Curators

This dataset was built on top of [parlparse](https://github.com/mysociety/parlparse) by [Evan Odell](https://github.com/evanodell)

### Licensing Information

Creative Commons Attribution 4.0 International License

### Citation Information

```
@misc{odell, evan_2021, 
title={Hansard Speeches 1979-2021: Version 3.1.0}, 
DOI={10.5281/zenodo.4843485}, 
abstractNote={<p>Full details are available at <a href="https://evanodell.com/projects/datasets/hansard-data">https://evanodell.com/projects/datasets/hansard-data</a></p> <p><strong>Version 3.1.0 contains the following changes:</strong></p> <p>- Coverage up to the end of April 2021</p>}, 
note={This release is an update of previously released datasets. See full documentation for details.}, 
publisher={Zenodo}, 
author={Odell, Evan}, 
year={2021}, 
month={May} }
```

Thanks to [@shamikbose](https://github.com/shamikbose) for adding this dataset.