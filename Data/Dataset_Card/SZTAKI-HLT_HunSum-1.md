---
language:
- hu
multilinguality:
- monolingual
task_categories:
- summarization
task_ids:
- news-articles-summarization
pretty_name: HunSum-1
license: cc-by-nc-sa-4.0
---
# Dataset Card for HunSum-1

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
- [Dataset Structure](#dataset-structure)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
 
## Dataset Description

### Dataset Summary

The HunSum-1 Dataset is a Hungarian-language dataset containing over 1.1M unique news articles with lead and other metadata. The dataset contains articles from 9 major Hungarian news websites. 

### Supported Tasks and Leaderboards

- 'summarization'
- 'title generation' 

## Dataset Structure

### Data Fields

- `uuid`: a string containing the unique id
- `article`: a string containing the body of the news article 
- `lead`: a string containing the lead of the article
- `title`: a string containing the title of the article
- `url`: a string containing the URL for the article
- `domain`:  a string containing the domain of the url
- `date_of_creation`: a timestamp containing the date when the article was created
- `tags`: a sequence containing the tags of the article

### Data Splits

The HunSum-1 dataset has 3 splits: _train_, _validation_, and _test_.

| Dataset Split | Number of Instances in Split                |
| ------------- | ------------------------------------------- |
| Train         | 1,144,255                                   |
| Validation    | 1996                                        |
| Test          | 1996                                        |

## Citation

If you use our dataset, please cite the following paper:
```
@inproceedings {HunSum-1,
    title = {{HunSum-1: an Abstractive Summarization Dataset for Hungarian}},
	booktitle = {XIX. Magyar Számítógépes Nyelvészeti Konferencia (MSZNY 2023)},
	year = {2023},
	publisher = {Szegedi Tudományegyetem, Informatikai Intézet},
	address = {Szeged, Magyarország},
	author = {Barta, Botond and Lakatos, Dorina and Nagy, Attila and Nyist, Mil{\'{a}}n Konor and {\'{A}}cs, Judit},
	pages = {231--243}
}
```