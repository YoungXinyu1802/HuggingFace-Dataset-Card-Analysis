---
annotations_creators: []
language:
- en
language_creators:
- other
license:
- mit
multilinguality:
- monolingual
pretty_name: Blogspot_raw_texts
size_categories:
- 1M<n<10M
source_datasets:
- original
tags:
- blogspot
- blogger
- texts
task_categories:
- text-classification
- text-retrieval
- text-generation
- time-series-forecasting
task_ids: []
---

# Dataset Card for blogspot raw dataset

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

- **Homepage:**
- **Repository:**
- **Paper:**
- **Leaderboard:**
- **Point of Contact:**

### Dataset Summary

This dataset is a corpus of raw blogposts from [blogspot](https://blogger.com) mostly in the English language. It was obtained by scraping corpora of [webarchive](https://archive.org) and [commoncrawl](https://commoncrawl.org).

### Supported Tasks and Leaderboards

The dataset may be used for training language models or serve other research interests.

### Languages

Mostly English language, but some outliers may occur.

## Dataset Structure

[Distribution](https://huggingface.co/datasets/mschi/blogspot_raw/blob/main/blospot_comm_dist.png)

The distribution of the blog posts over time can be viewed at ./blogspot_dist_comm.png

### Data Instances

[More Information Needed]

### Data Fields

    text: string
    URL: string
    date: string
    comment: int

### Data Splits

[More Information Needed]

## Dataset Creation

### Curation Rationale

The dataset was constructed by utilizing the [WARC-dl pipeline](https://github.com/webis-de/web-archive-keras). It was executed on cluster architecture. The corpora of archive.org and commoncrawl.org contain WARC files that contain HTML which gets parsed by the pipeline. The pipeline extracts HTML from the WARC files and applies distributed filtering to efficiently filter for the desired content. 

### Source Data

#### Initial Data Collection and Normalization

The corpora "corpus-commoncrawl-main-2022-05" and "corpus-iwo-internet-archive-wide00001" have been searched for the content present in this dataset.
Search terms have been inserted into the preciously mentioned pipeline to filter URLs for "blogspot.com" and characteristic timestamp information contained in the URL (e.g. "/01/2007"). The HTML documents were parsed for specific tags to obtain the timestamps. Further, the data was labeled with the "comment" label if there were some comment markers in the URL, indicating that the retrieved text is from the main text of a blog post or from the comments section. The texts are stored raw and no further processing has been done.

#### Who are the source language producers?

Since [blogspot](https://blogger.com) provides a high-level framework to allow people everywhere in the world to set up and maintain a blog, the producers of the texts may not be further specified.

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

### Personal and Sensitive Information

Texts are raw and unfiltered, thus personal and sensitive information, as well as explicit language, may be present in the dataset.

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

The retrieval of the timestamps from the HTML documents was not 100% accurate, so a small proportion of wrong or nonsense timestamps can be present in the data. Also we can not guarantee the correctness of the timestamps as well as the "comment" labels.

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

The dataset was constructed during the course "Big Data and Language Technologies" of the Text Mining and Retrieval Group, Department of Computer Science at the University of Leipzig.

### Licensing Information

[More Information Needed]

### Citation Information

[More Information Needed]

### Contributions

Thanks to [@jonaskonig](https://github.com/jonaskonig), [@maschirmer](https://github.com/maschirmer) and [@1BlattPapier](https://github.com/1BlattPapier) for contributing.

