---
annotations_creators:
- other
language_creators:
- other
language:
- en
multilinguality:
- monolingual
pretty_name: tldr_news
size_categories:
- 1K<n<10K
source_datasets:
- original
task_categories:
- summarization
- text2text-generation
- text-generation
task_ids:
- news-articles-headline-generation
- text-simplification
- language-modeling
---

# Dataset Card for `tldr_news`

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

- **Homepage:** https://tldr.tech/newsletter

### Dataset Summary

The `tldr_news` dataset was constructed by collecting a daily tech newsletter (available
[here](https://tldr.tech/newsletter)). Then, for every piece of news, the `headline` and its corresponding `
content` were extracted.
Also, the newsletter contain different sections. We add this extra information to every piece of news.

Such a dataset can be used to train a model to generate a headline from a input piece of text.

### Supported Tasks and Leaderboards

There is no official supported tasks nor leaderboard for this dataset. However, it could be used for the following
tasks:

- summarization
- headline generation

### Languages

en

## Dataset Structure

### Data Instances

A data point comprises a "headline" and its corresponding "content".
An example is as follows:

```
{
  "headline": "Cana Unveils Molecular Beverage Printer, a ‘Netflix for Drinks’ That Can Make Nearly Any Type of Beverage ",
  "content": "Cana has unveiled a drink machine that can synthesize almost any drink. The machine uses a cartridge that contains flavor compounds that can be combined to create the flavor of nearly any type of drink. It is about the size of a toaster and could potentially save people from throwing hundreds of containers away every month by allowing people to create whatever drinks they want at home. Around $30 million was spent building Cana’s proprietary hardware platform and chemistry system. Cana plans to start full production of the device and will release pricing by the end of February.",
  "category": "Science and Futuristic Technology"
}
```

### Data Fields

- `headline (str)`: the piece of news' headline
- `content (str)`: the piece of news
- `category (str)`: newsletter section

### Data Splits

- `all`: all existing daily newsletters available [here](https://tldr.tech/newsletter).

## Dataset Creation

### Curation Rationale

This dataset was obtained by scrapping the collecting all the existing newsletter
available [here](https://tldr.tech/newsletter).

Every single newsletter was then processed to extract all the different pieces of news. Then for every collected piece
of news the headline and the news content were extracted.

### Source Data

#### Initial Data Collection and Normalization

The dataset was has been collected from https://tldr.tech/newsletter.

In order to clean up the samples and to construct a dataset better suited for headline generation we have applied a
couple of normalization steps:

1. The headlines initially contain an estimated read time in parentheses; we stripped this information from the
   headline.
2. Some news are sponsored and thus do not belong to any newsletter section. We create an additional category "Sponsor"
   for such samples.

#### Who are the source language producers?

The people (or person) behind the https://tldr.tech/ newsletter.

### Annotations

#### Annotation process

Disclaimers: The dataset was generated from a daily newsletter. The author had no intention for those newsletters to be
used as such.

#### Who are the annotators?

The newsletters were written by the people behind *TLDR tech*.

### Personal and Sensitive Information

[Needs More Information]

## Considerations for Using the Data

### Social Impact of Dataset

[Needs More Information]

### Discussion of Biases

This dataset only contains tech news. A model trained on such a dataset might not be able to generalize to other domain.

### Other Known Limitations

[Needs More Information]

## Additional Information

### Dataset Curators

The dataset was obtained by collecting newsletters from this website: https://tldr.tech/newsletter

### Contributions

Thanks to [@JulesBelveze](https://github.com/JulesBelveze) for adding this dataset.