---
annotations_creators:
- found
language_creators:
- found
language:
- en
license:
- unknown
multilinguality:
- monolingual
size_categories:
- n<1K
source_datasets:
- original
task_categories:
- text2text-generation
- text-generation
- fill-mask
- text-retrieval
- summarization
task_ids:
- document-retrieval
- entity-linking-retrieval
- explanation-generation
- language-modeling
- masked-language-modeling
pretty_name: Cocktail Recipes
dataset_info:
  features:
  - name: title
    dtype: string
  - name: ingredients
    sequence: string
  - name: directions
    sequence: string
  - name: misc
    sequence: string
  - name: source
    dtype: string
  - name: ner
    sequence: string
  splits:
  - name: train
    num_bytes: 301501
    num_examples: 875
  download_size: 96915
  dataset_size: 301501
---
# Dataset Card for Cocktail Recipes

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


## Dataset Description

### Dataset Summary

Cocktail Recipes Dataset for Semi-Structured Text Generation.

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

The dataset is in English.

## Dataset Structure

### Data Instances

```json
{"title": "Final Ward",
 "ingredients": ["0.75 oz. Rye Whiskey",
  "0.75 oz. Lemon Juice",
  "0.75 oz. Maraschino Liqueur",
  "0.75 oz. Green Chartreuse"],
 "directions": ["shake on ice and strain"],
 "misc":[],
 "source": "Death & Co.",
 "ner":["whiskey",
  "chartreuse",
  "maraschino liqueur"]}
```

### Data Fields

- `title` (`str`): Title of the recipe.
- `ingredients` (`list` of `str`): Ingredients.
- `directions` (`list` of `str`): Instruction steps.
- `source` (`str`): Origin of each recipe
- `ner` (`list` of `str`): NER entities.

### Data Splits

The dataset contains a single `train` split.

## Dataset Creation

[More Information Needed]
### Curation Rationale

[More Information Needed]

### Source Data

[More Information Needed]

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

[More Information Needed]

### Annotations

[More Information Needed]

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


