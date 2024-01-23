---
annotations_creators: []
language_creators: []
language:
- ar
- bg
- de
- el
- en
- es
- fr
- hi
- it
- ja
- nl
- pl
- pt
- ru
- sw
- th
- tr
- ur
- vi
- zh
license: []
multilinguality:
- multilingual
pretty_name: Language Identification dataset
size_categories:
- unknown
source_datasets:
- extended|amazon_reviews_multi
- extended|xnli
- extended|stsb_multi_mt
task_categories:
- text-classification
task_ids:
- multi-class-classification
---

# Dataset Card for Language Identification dataset

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

The Language Identification dataset is a collection of 90k samples consisting of text passages and corresponding language label. 
This dataset was created by collecting data from 3 sources: [Multilingual Amazon Reviews Corpus](https://huggingface.co/datasets/amazon_reviews_multi), [XNLI](https://huggingface.co/datasets/xnli), and [STSb Multi MT](https://huggingface.co/datasets/stsb_multi_mt).


### Supported Tasks and Leaderboards

The dataset can be used to train a model for language identification, which is a **multi-class text classification** task.
The model [papluca/xlm-roberta-base-language-detection](https://huggingface.co/papluca/xlm-roberta-base-language-detection), which is a fine-tuned version of [xlm-roberta-base](https://huggingface.co/xlm-roberta-base), was trained on this dataset and currently achieves 99.6% accuracy on the test set.

### Languages

The Language Identification dataset contains text in 20 languages, which are:

`arabic (ar), bulgarian (bg), german (de), modern greek (el), english (en), spanish (es), french (fr), hindi (hi), italian (it), japanese (ja), dutch (nl), polish (pl), portuguese (pt), russian (ru), swahili (sw), thai (th), turkish (tr), urdu (ur), vietnamese (vi), and chinese (zh)`

## Dataset Structure

### Data Instances

For each instance, there is a string for the text and a string for the label (the language tag). Here is an example:

`{'labels': 'fr', 'text': 'Conforme à la description, produit pratique.'}`


### Data Fields

- **labels:** a string indicating the language label.
- **text:** a string consisting of one or more sentences in one of the 20 languages listed above.

### Data Splits

The Language Identification dataset has 3 splits: *train*, *valid*, and *test*. 
The train set contains 70k samples, while the validation and test sets 10k each. 
All splits are perfectly balanced: the train set contains 3500 samples per language, while the validation and test sets 500. 

## Dataset Creation

### Curation Rationale

This dataset was built during *The Hugging Face Course Community Event*, which took place in November 2021, with the goal of collecting a dataset with enough samples for each language to train a robust language detection model.

### Source Data

The Language Identification dataset was created by collecting data from 3 sources: [Multilingual Amazon Reviews Corpus](https://huggingface.co/datasets/amazon_reviews_multi), [XNLI](https://huggingface.co/datasets/xnli), and [STSb Multi MT](https://huggingface.co/datasets/stsb_multi_mt).

### Personal and Sensitive Information

The dataset does not contain any personal information about the authors or the crowdworkers.

## Considerations for Using the Data

### Social Impact of Dataset

This dataset was developed as a benchmark for evaluating (balanced) multi-class text classification models.

### Discussion of Biases

The possible biases correspond to those of the 3 datasets on which this dataset is based.

## Additional Information

### Dataset Curators

[More Information Needed]

### Licensing Information

[More Information Needed]

### Citation Information

[More Information Needed]

### Contributions

Thanks to [@LucaPapariello](https://github.com/LucaPapariello) for adding this dataset.
