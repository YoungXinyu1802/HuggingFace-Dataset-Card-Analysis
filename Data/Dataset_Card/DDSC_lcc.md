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
- n<1K
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

- **Repository**: https://github.com/fnielsen/lcc-sentiment
- **Direct Download part 1**: https://raw.githubusercontent.com/fnielsen/lcc-sentiment/master/dan_mixed_2014_10K-sentences.csv
- **Direct Download part 2**: https://raw.githubusercontent.com/fnielsen/lcc-sentiment/master/dan_newscrawl_2011_10K-sentences.csv

### Dataset Summary

This dataset consists of Danish data from [the Leipzig Collection](https://www.aclweb.org/anthology/L06-1396/) that has been annotated for sentiment analysis by Finn Årup Nielsen.

### Supported Tasks and Leaderboards

This dataset is suitable for sentiment analysis.

### Languages

This dataset is in Danish.

## Dataset Structure

### Data Instances

Every entry in the dataset has a document and an associated label.

### Data Fields

An entry in the dataset consists of the following fields:
- `text` (`str`): The text content.
- `label` (`str`): The label of the `text`. Can be "positiv", "neutral" or "negativ" for positive, neutral and negative sentiment, respectively.

### Data Splits

A `train` and `test` split is available, with the test split being 30% of the dataset, randomly sampled in a stratified fashion. There are 349 documents in the training split and 150 in the test split.

## Additional Information

### Dataset Curators

The collection and annotation of the dataset is solely due to the Finn Årup Nielsen. It was originally annotated as a score between -5 and +5, but the labels in this version have been converted to a negative, neutral and positive label.

### Licensing Information

The dataset is released under the CC BY 4.0 license.

### Citation Information

```
@misc{lcc,
  title={LCC},
  author={Finn Årup Nielsen},
  year={2016},
  note={\url{https://github.com/fnielsen/lcc-sentiment}}
}
```

### Contributions

Thanks to [@saattrupdan](https://github.com/saattrupdan) for adding this dataset to the Hugging Face Hub.