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
pretty_name: Shadertoys
size_categories:
- 10K<n<100K
source_datasets: []
tags:
- code
task_categories:
- text-generation
- text-classification
- translation
task_ids: []
dataset_info:
  features:
  - name: name
    dtype: string
  - name: type
    dtype: string
  - name: code
    dtype: string
  - name: title
    dtype: string
  - name: description
    dtype: string
  - name: tags
    sequence: string
  - name: author
    dtype: string
  - name: license
    dtype: string
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 145303157.20526963
    num_examples: 34518
  - name: test
    num_bytes: 25644209.79473036
    num_examples: 6092
  download_size: 81378628
  dataset_size: 170947367.0
---

# Dataset Card for Shadertoys

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

Shadertoys in the medium grained variant. Datapoints are renderpasses.

### Supported Tasks and Leaderboards

 `language-modeling`: The dataset can be used to train a model for modelling programming languages, which consists in building language models for programming languages.
 
 `text-classification`: The dataset can be used to classify text(title, description, comments) or code into labels like type or tags.
 
 `translation`: The Dataset can be used to translate from natural language (English) to programming language, or back.

### Languages

- English (title, description, tags, comments)
- Shadercode **programming** language

## Dataset Structure

### Data Instances

A data point consists of the function string, it's name as well as a bit of metadata like the author and source URL. (in the future there might be a function string without comments)
```
{
 'name': 'Image',
 'type': 'image',
 'code': '<full code>',
 'title': '<title of the shader>',
 'description': '<description of the shader>',
 'tags': ['tag1','tag2','tag3', ... ],
 'license': 'unknown',
 'author': '<username>',
 'source': 'https://shadertoy.com/view/<shaderID>'
}
```

### Data Fields

- 'name' Name of the renderpass, usually Image, Buffer A, Common, etc
- 'type' type of the renderpass; one of `{'buffer', 'common', 'cubemap', 'image', 'sound'}`
- 'code' the raw code (including comments) the whole renderpass.
- 'title' Name of the Shader
- 'description' description given for the Shader
- 'tags' List of tags assigned to the Shader (by it's creator); there are more than 10000 unique tags.
- 'license' currently in development
- 'author' username of the shader author
- 'source' URL to the shader. Not to the specific renderpass.

### Data Splits

Currently available (shuffled):
  - train (85.0%)
  - test (15.0%)

## Dataset Creation

Data retrieved starting 2022-07-20

### Source Data

#### Initial Data Collection and Normalization

All data was collected via the [Shadertoy.com API](https://www.shadertoy.com/howto#q2) and then iterated over the items in 'renderpass' while adding some of the fields from 'info'. The code to generate these datasets will be publish on the GitHub repository in the near future. 

#### Who are the source language producers?

Shadertoy.com contributers which publish shaders as 'public+API'

## Licensing Information

The Default [license for each Shader](https://www.shadertoy.com/terms) is CC BY-NC-SA 3.0. However, some Shaders might have a different license attached. The Dataset is currently not filtering for any licenses. A new data field is currently being developed to annotate if any other license applies to a shader.