---
annotations_creators:
- no-annotation
language_creators:
- found
language:
- da
license:
- mit
multilinguality:
- monolingual
size_categories:
- 1M<n<10M
source_datasets:
- original
task_categories:
- text-generation
task_ids:
- language-modeling
pretty_name: Reddit-da
---

# Dataset Card for SQuAD-da

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Contributions](#contributions)

### Dataset Summary

This dataset consists of 1,908,887 Danish posts from Reddit. These are from [this Reddit dump](https://files.pushshift.io/reddit/) and have been filtered using [this script](https://github.com/NBAiLab/notram/blob/master/corpus_generation_scripts/lang_detect_reddit.py), which uses FastText to detect the Danish posts. 

### Supported Tasks and Leaderboards

This dataset is suitable for language modelling.

### Languages

This dataset is in Danish.

## Dataset Structure

### Data Instances

Every entry in the dataset contains short Reddit comments in Danish, along with a unique ID.

### Data Fields

An entry in the dataset consists of the following fields:
- `id` (`str`): A unique identifier.
- `text` (`str`): A short Reddit comment.


## Additional Information

### Licensing Information

The dataset is released under the MIT license.

### Contributions

Thanks to [@saattrupdan](https://github.com/saattrupdan) for adding this dataset to the Hugging Face Hub.