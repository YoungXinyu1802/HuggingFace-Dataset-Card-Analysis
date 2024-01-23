---
pretty_name: Wikipedia Arabic dumps dataset.
language:
- ar
license:
- unknown
multilinguality:
- monolingual
---

# Arabic Wiki Dataset

## Dataset Summary
This dataset is extracted using [`wikiextractor`](https://github.com/attardi/wikiextractor) tool, from [Wikipedia Arabic pages](https://dumps.wikimedia.org/arwiki/).

## Supported Tasks and Leaderboards
Intended to train **Arabic** language models on MSA (Modern Standard Arabic).

## Dataset Structure
The dataset is structured into 2 folders:
- `arwiki_20211213_txt`: dataset is divided into subfolders each of which contains no more than 100 documents.
- `arwiki_20211213_txt_single`: all documents merged together in a single txt file.

## Dataset Statistics

#### Extracts from **December 13, 2021**:

| documents | vocabulary | words |
| --- | --- | --- |
| 1,136,455 | 5,446,560 | 175,566,016 |

## Usage
Load all dataset from the single txt file:
```python
load_dataset('CALM/arwiki', 
              data_files='arwiki_2021_txt_single/arwiki_20211213.txt')

# OR with stream

load_dataset('CALM/arwiki', 
              data_files='arwiki_2021_txt_single/arwiki_20211213.txt', 
              streaming=True)
```
Load a smaller subset from the individual txt files:
```python
load_dataset('CALM/arwiki', 
              data_files='arwiki_2021_txt/AA/arwiki_20211213_1208.txt')

# OR with stream

load_dataset('CALM/arwiki', 
              data_files='arwiki_2021_txt/AA/arwiki_20211213_1208.txt', 
              streaming=True)
```