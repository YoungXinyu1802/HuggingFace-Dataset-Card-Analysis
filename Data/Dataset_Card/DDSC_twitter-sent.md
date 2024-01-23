---
annotations_creators:
- expert-generated
language_creators:
- found
language:
- da
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: TwitterSent
size_categories:
- 1K<n<10K
source_datasets:
- original
task_categories:
- text-classification
task_ids:
- sentiment-classification
---

# Dataset Card for DKHate

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Direct Download**: https://danlp.alexandra.dk/304bd159d5de/datasets/twitter.sentiment.zip

### Dataset Summary

This dataset consists of anonymised Danish Twitter data that has been annotated for sentiment analysis by the [Alexandra Institute](https://github.com/alexandrainst) - all credits go to them.

### Supported Tasks and Leaderboards

This dataset is suitable for sentiment analysis.

### Languages

This dataset is in Danish.

## Dataset Structure

### Data Instances

Every entry in the dataset has a tweet and an associated label.

### Data Fields

An entry in the dataset consists of the following fields:
- `text` (`str`): The tweet content.
- `label` (`str`): The label of the `text`. Can be "positiv", "neutral" or "negativ" for positive, neutral and negative sentiment, respectively.

### Data Splits

A `train` and `test` split is available, being identical to the original splits. There are 1,007 tweets in the training split and 431 in the test split.

## Additional Information

### Dataset Curators

The collection and annotation of the dataset is solely due to the [Alexandra Institute](https://github.com/alexandrainst). The tweets have been anonymised by [@saattrupdan](https://github.com/saattrupdan).

### Licensing Information

The dataset is released under the CC BY 4.0 license.

### Citation Information

```
@misc{twittersent,
  title={TwitterSent},
  author={Alexandra Institute},
  year={2020},
  note={\url{https://danlp-alexandra.readthedocs.io/en/latest/docs/datasets.html#twitsent}}
}
```

### Contributions

Thanks to [@saattrupdan](https://github.com/saattrupdan) for adding this dataset to the Hugging Face Hub.