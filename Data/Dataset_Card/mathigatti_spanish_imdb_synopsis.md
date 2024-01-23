---
annotations_creators:
- no-annotation
language:
- es
license:
- apache-2.0
multilinguality:
- monolingual
task_categories:
- summarization
- text-generation
- text2text-generation
---
# Dataset Card for Spanish IMDb Synopsis
## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Fields](#data-fields)
- [Dataset Creation](#dataset-creation)

## Dataset Description

4969 movie synopsis from IMDb in spanish.

### Dataset Summary
[N/A]

### Languages

All descriptions are in spanish, the other fields have some mix of spanish and english.

## Dataset Structure
[N/A]

### Data Fields
- `description`: IMDb description for the movie (string), should be spanish
- `keywords`: IMDb keywords for the movie (string), mix of spanish and english
- `genre`: The genres of the movie (string), mix of spanish and english
- `year`: The year the movie was published (float)
- `name`: The name of the movie (string), mix of spanish and english
- `director`: The name of the main director in the movie, can be empty (string)

## Dataset Creation

[This kaggle dataset](https://www.kaggle.com/datasets/komalkhetlani/imdb-dataset) was used as a starting point. Then IMDb was scraped downloading the synopsis of the movies that have more than 5000 votes/reviews and those that did not have a synopsis available in Spanish were discarded.