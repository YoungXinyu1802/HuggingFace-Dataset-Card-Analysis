---
annotations_creators:
- crowdsourced
language_creators:
- found
language:
- da
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: AngryTweets
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

- **Paper:** https://aclanthology.org/2021.nodalida-main.53/
- **Direct Download**: https://danlp-downloads.alexandra.dk/datasets/game_tweets.zip

### Dataset Summary

This dataset consists of anonymised Danish Twitter data that has been annotated for sentiment analysis through crowd-sourcing. All credits go to the authors of the following paper, who created the dataset: 

[Pauli, Amalie Brogaard, et al. "DaNLP: An open-source toolkit for Danish Natural Language Processing." Proceedings of the 23rd Nordic Conference on Computational Linguistics (NoDaLiDa). 2021](https://aclanthology.org/2021.nodalida-main.53/)

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

A `train` and `test` split is available, with the test split being 30% of the dataset, randomly sampled in a stratified fashion. There are 2,437 tweets in the training split and 1,047 in the test split.

## Additional Information

### Dataset Curators

The collection and annotation of the dataset is solely due to the authors of [the original paper](https://aclanthology.org/2021.nodalida-main.53/): Amalie Brogaard Pauli, Maria Barrett, Ophélie Lacroix and Rasmus Hvingelby. The tweets have been anonymised by [@saattrupdan](https://github.com/saattrupdan).

### Licensing Information

The dataset is released under the CC BY 4.0 license.

### Citation Information

```
@inproceedings{pauli2021danlp,
  title={DaNLP: An open-source toolkit for Danish Natural Language Processing},
  author={Pauli, Amalie Brogaard and Barrett, Maria and Lacroix, Oph{\'e}lie and Hvingelby, Rasmus},
  booktitle={Proceedings of the 23rd Nordic Conference on Computational Linguistics (NoDaLiDa)},
  pages={460--466},
  year={2021}
}
```

### Contributions

Thanks to [@saattrupdan](https://github.com/saattrupdan) for adding this dataset to the Hugging Face Hub.