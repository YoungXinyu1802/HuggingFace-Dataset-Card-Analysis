---
license: other
task_categories:
- sentence-similarity
language:
- en
tags:
- '#sentence-relatedness'
- '#semantic-similarity'
- '#semantic-relatedness'
pretty_name: str-2022
size_categories:
- 1K<n<10K
---

## STR-2022: Dataset Description

The dataset consists of 5500 English sentence pairs that are scored and ranked on a relatedness scale ranging from 0 (least related) to 1 (most related).

## Loading the Dataset
- The sentence pairs, and associated scores, are in the file sem_text_rel_ranked.csv in the root directory. The CSV file can be read using:

  ```python
  import pandas as pd
  
  str = pd.read_csv('sem_text_rel_ranked.csv')
  
  row = str.loc[0]
  sent1, sent2 = row['Text'].split("\n")
  score = row['Score']
  ```

- Relevant columns: 

  - Text: Sentence pair, separated by the newline character.
  - Score: The semantic relatedness score between 0 and 1. 

- Additionally:
  - the SourceID column indicates the source dataset from which the sentence pair was drawn (see Table 2 of our paper)
  - The SubsetID column indicates the sampling strategy used for the source dataset
  - and the PairID is a unique identifier for each pair that also indicates its Source and Subset.
 
## Why Semantic Relatedness?
Closeness of meaning can be of two kinds: semantic relatedness and semantic similarity. Two sentences are considered semantically similar when they have a paraphrasal or entailment relation, whereas relatedness accounts for all of the commonalities that can exist between two sentences. Semantic relatedness is central to textual coherence and narrative structure. Automatically determining semantic relatedness has many applications such as question answering, plagiarism detection, text generation (say in personal assistants and chat bots), and summarization. 

Prior NLP work has focused on semantic similarity (a small subset of semantic relatedness), largely because of a dearth of datasets. In this paper, we present the first manually annotated dataset of sentence--sentence semantic relatedness. It includes fine-grained scores of relatedness from 0 (least related) to 1 (most related) for 5,500 English sentence pairs. The sentences are taken from diverse sources and thus also have diverse sentence structures, varying amounts of lexical overlap, and varying formality.

## Comparative Annotations and Best-Worst Scaling 
Most existing sentence-sentence similarity datasets were annotated, one item at a time, using coarse rating labels such as integer values between 1 and 5\@ representing coarse degrees of closeness. It is well documented that such approaches suffer from inter- and intra-annotator inconsistency, scale region bias, and issues arising due to the fixed granularity.

The relatedness scores for our dataset were, instead, obtained using a __comparative__ annotation schema. In comparative annotations, two (or more) items are presented together and the annotator has to determine which is greater with respect to the metric of interest.

Specifically, we use Best-Worst Scaling, a comparative annotation method}, which has been shown  to produce reliable scores with fewer annotations in other NLP tasks. We use scripts from https://saifmohammad.com/WebPages/BestWorst.html to obtain relatedness scores from our annotations.
 
## Citing our work 
Please use the following BibTex entry to cite us if you use our dataset or any of the [associated analyses](https://arxiv.org/abs/2110.04845):

```
@inproceedings{abdalla2023makes,
      title={What Makes Sentences Semantically Related: A Textual Relatedness Dataset and Empirical Study},
      author={Abdalla, Mohamed and Vishnubhotla, Krishnapriya and Mohammad, Saif M.},
      year={2023},
      address = {Dubrovnik, Croatia},
      publisher = "Association for Computational Linguistics",
      booktitle = "Proceedings of the 17th Conference of the European Chapter of the Association for Computational Linguistics: Main Volume"
}
```

## Ethics Statement
Any dataset of semantic relatedness entails several ethical considerations. We talk about this in Section 10 of [our paper](https://arxiv.org/abs/2110.04845).

## Relevant Links
- [GitHub repository](https://github.com/Priya22/semantic-textual-relatedness)
- [Zenodo page](https://zenodo.org/record/7599667)

## Creators
- [Mohamed Abdalla](https://www.cs.toronto.edu/~msa/index_all.html) (University of Toronto)
- [Krishnapriya Vishnubhotla](https://priya22.github.io/) (University of Toronto)
- [Saif M. Mohammad](http://saifmohammad.com/) (National Research Council Canada)

**Contact**: msa@cs.toronto.edu, vkpriya@cs.toronto.edu, saif.mohammad@nrc-cnrc.gc.ca