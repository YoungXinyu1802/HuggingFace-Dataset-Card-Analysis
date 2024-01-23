---
annotations_creators:
- no-annotation
language:
- en
- code
language_creators:
- machine-generated
license:
- cc-by-nc-sa-3.0
multilinguality: []
pretty_name: Shadertoys-fine
size_categories:
- 100K<n<1M
source_datasets: []
tags:
- code
task_categories:
- text-generation
task_ids: []
dataset_info:
  features:
  - name: name
    dtype: string
  - name: code
    dtype: string
  - name: source
    dtype: string
  - name: author
    dtype: string
  splits:
  - name: train
    num_bytes: 95328576.47397786
    num_examples: 184946
  - name: test
    num_bytes: 16822932.526022132
    num_examples: 32638
  download_size: 54738148
  dataset_size: 112151509.0
---

# Dataset Card for Shadertoys-fine

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
  - [Source Data](#source-data)
- [Licensing Information](#licensing-information)

## Dataset Description

- **Repository:** https://github.com/Vipitis/project (private placeholder)

### Dataset Summary

fine variant of the Shadertoys dataset (still WIP), where individual functions are avaialable as Datapoints.

### Supported Tasks and Leaderboards

 `language-modeling`: The dataset can be used to train a model for modelling programming languages, which consists in building language models for programming languages.

### Languages

- English (names, comments)
- Shadercode **programming** language

## Dataset Structure

### Data Instances

A data point consists of the function string, it's name as well as a bit of metadata like the author and source URL. (in the future there might be a function string without comments)
```
{
  'name': '<type> <name>',
  'code': '<type> <name>(<inputs>) { <body> return <outputs>; }\n',
  'source': 'https://shadertoy.com/view/<shaderID>',
  'author': '<username>'
}
```

## #Data Fields

- 'name' funciton identifier composed of the type and the name of the function
- 'code' the raw code (including comments) of function.
- 'source' URL to the shader. It might be on a different renderpass
- 'author' username of the shader author

### Data Splits

Currently available (shuffled):
  - train (85.0%)
  - test (15.0%)

## Dataset Creation

Data retrieved starting 2022-07-20

### Source Data

#### Initial Data Collection and Normalization

All data was collected via the [Shadertoy.com API](https://www.shadertoy.com/howto#q2) and then by looking for keywords and counting curly brackets to figure out what is part of a function and what isn't.

#### Who are the source language producers?

Shadertoy.com contributers which publish shaders as 'public+API'

## Licensing Information

The Default [licnese for each Shader](https://www.shadertoy.com/terms) is CC BY-NC-SA 3.0. However, some Shaders might have a different license attached. The Dataset is currently not filtering for any licensis. 