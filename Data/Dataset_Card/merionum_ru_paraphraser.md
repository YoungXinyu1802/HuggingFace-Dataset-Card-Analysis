---
annotations_creators:
- crowdsourced
- expert-generated
- machine-generated
language_creators:
- crowdsourced
language:
- ru
license:
- mit
multilinguality:
- monolingual
paperswithcode_id: null
pretty_name: ParaPhraser
size_categories:
- 1M<n<10M
source_datasets:
- original
task_categories:
- text-classification
- text-generation
- text2text-generation
- sentence-similarity
task_ids:
- semantic-similarity-scoring
---

# Dataset Card for ParaPhraser

### Dataset Summary

ParaPhraser is a news headlines corpus annotated according to the following schema:

```
1: precise paraphrases
0: near paraphrases
-1: non-paraphrases
```
The _Plus_ part is also available.
It contains clusters of news headline paraphrases labeled automatically by a fine-tuned paraphrase detection BERT model.  
In order to load it:
```python
from datasets import load_dataset

corpus = load_dataset('merionum/ru_paraphraser', data_files='plus.jsonl')
```
## Dataset Structure

```
train: 7,227 pairs
test: 1,924 pairs
plus: 1,725,393 clusters (total: ~7m texts)
```


### Citation Information

```
@inproceedings{pivovarova2017paraphraser,
  title={ParaPhraser: Russian paraphrase corpus and shared task},
  author={Pivovarova, Lidia and Pronoza, Ekaterina and Yagunova, Elena and Pronoza, Anton},
  booktitle={Conference on artificial intelligence and natural language},
  pages={211--225},
  year={2017},
  organization={Springer}
}
```


```
@inproceedings{gudkov-etal-2020-automatically,
    title = "Automatically Ranked {R}ussian Paraphrase Corpus for Text Generation",
    author = "Gudkov, Vadim  and
      Mitrofanova, Olga  and
      Filippskikh, Elizaveta",
    booktitle = "Proceedings of the Fourth Workshop on Neural Generation and Translation",
    month = jul,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.ngt-1.6",
    doi = "10.18653/v1/2020.ngt-1.6",
    pages = "54--59",
    abstract = "The article is focused on automatic development and ranking of a large corpus for Russian paraphrase generation which proves to be the first corpus of such type in Russian computational linguistics. Existing manually annotated paraphrase datasets for Russian are limited to small-sized ParaPhraser corpus and ParaPlag which are suitable for a set of NLP tasks, such as paraphrase and plagiarism detection, sentence similarity and relatedness estimation, etc. Due to size restrictions, these datasets can hardly be applied in end-to-end text generation solutions. Meanwhile, paraphrase generation requires a large amount of training data. In our study we propose a solution to the problem: we collect, rank and evaluate a new publicly available headline paraphrase corpus (ParaPhraser Plus), and then perform text generation experiments with manual evaluation on automatically ranked corpora using the Universal Transformer architecture.",
}
```


### Contributions

Dataset maintainer:
Vadim Gudkov: [@merionum](https://github.com/merionum)

