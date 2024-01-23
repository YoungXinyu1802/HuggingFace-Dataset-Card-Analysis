---
language:
- en
license:
- other
size_categories:
- 1K<n<10K
task_categories:
- text-classification
task_ids: []
tags:
- hate-speech-detection
- offensive-language
---

# Offensive language dataset of Croatian comments FRENK 1.0

English subset of the [FRENK dataset](http://hdl.handle.net/11356/1433). Also available on HuggingFace dataset hub: [Croatian subset](https://huggingface.co/datasets/5roop/FRENK-hate-hr),  [Slovenian subset](https://huggingface.co/datasets/5roop/FRENK-hate-sl).

## Dataset Description

- **Homepage:** http://hdl.handle.net/11356/1433

- **Repository:** http://hdl.handle.net/11356/1433

- **Paper:** https://arxiv.org/abs/1906.02045

- **Project page** https://nl.ijs.si/frenk/

## Description of the original dataset

The original FRENK dataset consists of comments to Facebook posts (news articles) of mainstream media outlets from Croatia, Great Britain, and Slovenia, on the topics of migrants and LGBT. The dataset contains whole discussion threads. Each comment is annotated by the type of socially unacceptable discourse (e.g., inappropriate, offensive, violent speech) and its target (e.g., migrants/LGBT, commenters, media). The annotation schema is described in detail in [https://arxiv.org/pdf/1906.02045.pdf]. Usernames in the metadata are pseudo-anonymised and removed from the comments.

The data in each language (Croatian (hr), English (en), Slovenian (sl), and topic (migrants, LGBT) is divided into a training and a testing portion. The training and testing data consist of separate discussion threads, i.e., there is no cross-discussion-thread contamination between training and testing data. The sizes of the splits are the following: Croatian, migrants: 4356 training comments, 978 testing comments; Croatian LGBT: 4494 training comments, 1142 comments; English, migrants: 4540 training comments, 1285 testing comments; English, LGBT: 4819 training comments, 1017 testing comments; Slovenian, migrants: 5145 training comments, 1277 testing comments; Slovenian, LGBT: 2842 training comments, 900 testing comments.

For this dataset only the English data was used. Training segment has been split into beginning 90% (published here as training split) and end 10% (published here as dev split).


## Usage in `Transformers`
```python
import datasets
ds = datasets.load_dataset("classla/FRENK-hate-en","binary") 
```

For binary classification the following encoding is used:


```python
_CLASS_MAP_BINARY = {
    'Acceptable': 0, 
    'Offensive': 1, 
}
```
The original labels are available if the dataset is loaded with the `multiclass` option:

```python
import datasets
ds = datasets.load_dataset("5roop/FRENK-hate-en","multiclass").
```

In this case the encoding used is:
```python
_CLASS_MAP_MULTICLASS = {
    'Acceptable speech': 0, 
    'Inappropriate': 1, 
    'Background offensive': 2,
    'Other offensive': 3, 
    'Background violence': 4,
    'Other violence': 5, 
}
```


The original labels are available if the dataset is loaded with the `multiclass` option:

```python
import datasets
ds = datasets.load_dataset("classla/FRENK-hate-en","multiclass").
```

In this case the encoding used is:
```python
_CLASS_MAP_MULTICLASS = {
    'Acceptable speech': 0, 
    'Inappropriate': 1, 
    'Background offensive': 2,
    'Other offensive': 3, 
    'Background violence': 4,
    'Other violence': 5, 
}
```


## Data structure

* `text`: text
* `target`: who is the target of the hate-speech text ("no target", "commenter", "target" (migrants or LGBT, depending on the topic), or "related to" (again, the topic))
* `topic`: whether the text relates to lgbt or migrants hate-speech domains
* `label`: label of the text instance, see above.

## Data instance

```
{'text': "Not everyone has the option of a rainbow reaction; I don't but wish I did.",
 'target': 'No target',
 'topic': 'lgbt',
 'label': 0}
 ```

## Licensing information

CLARIN.SI Licence ACA ID-BY-NC-INF-NORED 1.0

## Citation information

When using this dataset please cite the following paper:

```
@misc{ljubešić2019frenk,
      title={The FRENK Datasets of Socially Unacceptable Discourse in Slovene and English}, 
      author={Nikola Ljubešić and Darja Fišer and Tomaž Erjavec},
      year={2019},
      eprint={1906.02045},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/1906.02045}
}
```

The original dataset can be cited as
 ```
@misc{11356/1433,
 title = {Offensive language dataset of Croatian, English and Slovenian comments {FRENK} 1.0},
 author = {Ljube{\v s}i{\'c}, Nikola and Fi{\v s}er, Darja and Erjavec, Toma{\v z}},
 url = {http://hdl.handle.net/11356/1433},
 note = {Slovenian language resource repository {CLARIN}.{SI}},
 copyright = {{CLARIN}.{SI} Licence {ACA} {ID}-{BY}-{NC}-{INF}-{NORED} 1.0},
 year = {2021} }
 ```
