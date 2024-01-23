---
tags:
- future
language:
- en
multilinguality:
- monolingual
size_categories:
- 1K<n<10K
task_categories:
- text-classification
task_ids:
- multi-class-classification
pretty_name: Future Statements
---
# Dataset Card for Future Statements Dataset
## Table of Contents

- [Dataset Description](#dataset-description)
- [Dataset Motivation](#dataset-motivation)
- [Dataset Composition](#dataset-composition)
- [Dataset Collection Process](#dataset-collection-process)
- [Dataset Preprocessing](#dataset-preprocessing)
- [Dataset Uses](#dataset-uses)
- [Dataset Maintenance](#dataset-maintenance)

## Dataset Description

The Future Statements Dataset is an English language dataset containing 2500 statements, 50% of which relate to future events and 50% of which relate to non-future events. The statements were collected manually and programmatically from several websites and datasets. The labels were set manually or programmatically (including corresponding manual examination of the labels).

**The statements within the dataset do not reflect any personal opinion of the creators of the dataset.**

## Dataset Motivation

- The sole purpose of this dataset was to fine tune the [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) model into ourc[distilbert-base-future](https://huggingface.co/fidsinn/distilbert-base-future) model.
- The dataset was created by students from the University of Leipzig (Germany) in the Big Data and Language Technologies Module of the [Webis Group](https://huggingface.co/webis).

## Dataset Composition

- The instances represent single- or multi-sentence statements from following sources (unequally distributed):
  - http://www.kaggle.com/unitednations/un-general-debates
  - http://data.world/ian/united-nations-general-debate-corpus
  - http://gadebate.un.org/
  - http://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/0TJX8Y
  - http://www.wsj.com/
  - http://www.vox.com/
  - http://futechblog.com/
  - http://www.weforum.org/
  - http://wired.com/
  - http://openai.com/blog/
  - http://techcrunch.com/
  - http://futurism.com
  
- The dataset consists of 2500 statements in total, 50% of which relate to future events and 50% of which relate to non-future events.
- The label is represented by the 'future'-column:
  - 0: No future statement
  - 1: Future statement
  
- Noise, Biases and redundancies:
  - The main goal of the data collection process was to find future statements and general statements in equal amount. The thematic content within the statements can be redundant and some topics can be much more present. The dataset was not created to work with the thematic content while only fine-tune an already existing model into a model which is sensible for future and non-future statements.
  
- The data in the 'statement'-column is publicly available and does not contain confidential information.
- The data in the 'statement'-column can contain data that might be offensive, insulting, threatening, or might otherwise cause anxiety. This is because the data was collected from several online sources. However this is unlikely because the data was collected from reputable sites.

## Dataset Collection Process
- The data was directly observable on the websites mentioned in upper section.
- The data was collected manually and programmatically (using Pythons NLTK library for automatic sentence-extraction and Regex-filtering).
- The data was collected from graduate students [D. Baradari](https://huggingface.co/Dunya), [F. Bartels](https://huggingface.co/fidsinn), A. Dewald, [J. Peters](https://huggingface.co/jpeters92) as part of a data science module of the University of Leipzig.
- The data was collected in the months 06/2022-07/2022 but the content of the dataset is independent of the data collection period and can be from earlier periods.

## Dataset Preprocessing

## Dataset Uses

- The future-statements dataset has been used for the purpose of fine-tuning the [distilbert-base-future](https://huggingface.co/fidsinn/distilbert-base-future) model.
- Further uses were not intended and are not planned in the future.
- The dataset is not intended to be used for any kind of content analyses, because it is unequally distributed in topics and not designed and evaluated for such use. It was only predestined for fine-tuning purposes in natural language processing.

## Dataset Maintenance

- Curators of the dataset can be contacted via the [community tab](https://huggingface.co/datasets/fidsinn/future-statements/discussions)
- It is not planned to update the dataset for further work or investigations.