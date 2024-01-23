---
annotations_creators:
- crowdsourced
language:
- sl
language_creators:
- found
license:
- cc-by-sa-4.0
multilinguality:
- monolingual
pretty_name: SentiNews
size_categories: []
source_datasets:
- original
tags:
- slovenian sentiment
- news articles
task_categories:
- text-classification
task_ids:
- sentiment-classification
---

# Dataset Card for SentiNews

## Dataset Description

- **Homepage:** https://github.com/19Joey85/Sentiment-annotated-news-corpus-and-sentiment-lexicon-in-Slovene  
- **Paper:** Bučar, J., Žnidaršič, M. & Povh, J. Annotated news corpora and a lexicon for sentiment analysis in Slovene. Lang Resources & Evaluation 52, 895–919 (2018). https://doi.org/10.1007/s10579-018-9413-3

### Dataset Summary

SentiNews is a Slovenian sentiment classification dataset, consisting of news articles manually annotated with their sentiment by between two and six annotators.
It is annotated at three granularities: 
- document-level (config `document_level`, 10 427 documents), 
- paragraph-level (config `paragraph_level`, 89 999 paragraphs), and 
- sentence-level (config `sentence_level`, 168 899 sentences).

### Supported Tasks and Leaderboards

Sentiment classification, three classes (negative, neutral, positive).

### Languages

Slovenian.

## Dataset Structure

### Data Instances

A sample instance from the sentence-level config:
```
{
  'nid': 2, 
  'content': 'Vilo Prešeren je na dražbi ministrstva za obrambo kupilo nepremičninsko podjetje Condor Real s sedežem v Lescah.', 
  'sentiment': 'neutral', 
  'pid': 1, 
  'sid': 1
}
```

### Data Fields

The data fields are similar among all three configs, with the only difference being the IDs.

- `nid`: a uint16 containing a unique ID of the news article (document). 
- `content`: a string containing the body of the news article 
- `sentiment`: the sentiment of the instance
- `pid`: a uint8 containing the consecutive number of the paragraph inside the current news article, **not unique** (present in the configs `paragraph_level` and `sentence_level`)
- `sid`: a uint8 containing the consecutive number of the sentence inside the current paragraph, **not unique** (present in the config `sentence_level`)

## Additional Information

### Dataset Curators

Jože Bučar, Martin Žnidaršič, Janez Povh.

### Licensing Information

CC BY-SA 4.0

### Citation Information

```
@article{buvcar2018annotated, 
  title={Annotated news corpora and a lexicon for sentiment analysis in Slovene}, 
  author={Bu{\v{c}}ar, Jo{\v{z}}e and {\v{Z}}nidar{\v{s}}i{\v{c}}, Martin and Povh, Janez}, 
  journal={Language Resources and Evaluation}, 
  volume={52}, 
  number={3}, 
  pages={895--919}, 
  year={2018}, 
  publisher={Springer}
}
```

### Contributions

Thanks to [@matejklemen](https://github.com/matejklemen) for adding this dataset.
