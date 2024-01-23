---
TODO: Add YAML tags here. 
---
name: **TRBLLmaker** 

annotations_creators: found

language_creators: found

languages: en-US

licenses: Genius-Ventura-Toker

multilinguality: monolingual

source_datasets: original

task_categories: sequence-modeling

task_ids: sequence-modeling-seq2seq_generate


# Dataset Card for TRBLLmaker Dataset

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
    - [Split info](#Split-info)
- [Dataset Creation](#dataset-creation)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Contributions](#contributions)

## Dataset Description

- **Repository:** https://github.com/venturamor/TRBLLmaker-NLP
- **Paper:** in git

### Dataset Summary
TRBLLmaker - To Read Between Lyrics Lines.
Dataset used in order to train a model to get as an input - several lines of song's lyrics and generate optional interpretation / meaning of them or use the songs' metdata for various tasks such as classification.

This dataset is based on 'Genius' website's data, which contains global collection of songs lyrics and provides annotations and interpretations to songs lyrics and additional music knowledge.
We used 'Genius' API, created private client and extracted the relevant raw data from Genius servers.

We extracted the songs by the most popular songs in each genre - pop, rap, rock, country and r&b. Afterwards, we created a varied pool of 150 artists that associated with different music styles and periods, and extracted maximum of 100 samples from each.
We combined all the data, without repetitions, into one final database. After preforming a cleaning of non-English lyrics, we got our final corpus that contains 8,808 different songs with over all of 60,630 samples, while each sample is a specific sentence from the song's lyrics and its top rated annotation.

### Supported Tasks and Leaderboards

Seq2Seq

### Languages

[En] - English

## Dataset Structure

### Data Fields

We stored each sample in a 'SongInfo' structure with the following attributes: title, genre, annotations and song's meta data. 
The meta data contains the artist's name, song id in the server, lyrics and statistics such page views.

### Data Splits

train
train_songs

test
test_songs

validation
validation songs

## Split info
- songs
- samples

train [0.64 (0.8 * 0.8)], test[0.2], validation [0.16 (0.8 * 0.2)]

## Dataset Creation

### Source Data
Genius - https://genius.com/

### Annotations

#### Who are the annotators?

top-ranked annotations by users in Genoius websites / Official Genius annotations

## Considerations for Using the Data

### Social Impact of Dataset

We are excited about the future of applying attention-based models on task such as meaning generation. 
We hope this dataset will encourage more NLP researchers to improve the way we understand and enjoy songs, since
achieving artistic comprehension is another step that progress us to the goal of robust AI. 

### Other Known Limitations

The artists list can be found here.

## Additional Information

### Dataset Curators

This Dataset created by Mor Ventura and Michael Toker.

### Licensing Information

All source of data belongs to Genius.

### Contributions

Thanks to [@venturamor, @tokeron](https://github.com/venturamor/TRBLLmaker-NLP) for adding this dataset.