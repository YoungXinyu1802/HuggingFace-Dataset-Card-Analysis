---
annotations_creators:
- crowdsourced
language_creators:
- found
language:
- he
license:
- other
multilinguality:
- monolingual
size_categories:
- 10K<n<100K
source_datasets:
- extended|other-reuters-corpus
task_categories:
- token-classification
task_ids:
- named-entity-recognition
train-eval-index:
- config: bmc
  task: token-classification
  task_id: entity_extraction
  splits:
    train_split: train
    eval_split: validation
    test_split: test
  col_mapping:
    tokens: tokens
    ner_tags: tags
  metrics:
    - type: seqeval
      name: seqeval
---


# NEMO-Corpus - The Hebrew Named Entities and Morphology Corpus

**Disclaimer**: It's just a huggingface datasets convenient interface for research purpose which is fetching the original data from [github](https://github.com/OnlpLab/NEMO-Corpus). I'm not an author of this work.


```python
from datasets import load_dataset

# the main corpus
ds = load_dataset('imvladikon/nemo_corpus')
for sample in ds["train"]:
    print(sample)

# the nested corpus
ds = load_dataset('imvladikon/nemo_corpus', "nested")
```

Getting classes and encoding/decoding could be done through these functions:
```
idx2label = dataset["train"].features["ner_tags"].feature.int2str
label2idx = dataset["train"].features["ner_tags"].feature.str2int
```
or just use raw_tags field.

## Fields 

available fields (flat): 
* "id"
* "sentence"
* "tokens"
* "raw_tags"
* "ner_tags"
* "spans"

Example of the one record for `flat`:
```json
{'id': '0', 'tokens': ['"', 'תהיה', 'נקמה', 'ו', 'בגדול', '.'], 'sentence': '" תהיה נקמה ו בגדול .', 'raw_tags': ['O', 'O', 'O', 'O', 'O', 'O'], 'ner_tags': [24, 24, 24, 24, 24, 24], 'spans': {'span': [], 'start': [], 'end': [], 'entity': [], 'start_char': [], 'end_char': []}}
```

Example of the one record for `nested`:
```json
{'id': '0', 'tokens': ['"', 'תהיה', 'נקמה', 'ו', 'בגדול', '.'], 'ner_tags': [24, 24, 24, 24, 24, 24], 'ner_tags_2': [24, 24, 24, 24, 24, 24], 'ner_tags_3': [24, 24, 24, 24, 24, 24], 'ner_tags_4': [24, 24, 24, 24, 24, 24]}
```

## Dataset Description 
it's README.md of the [original repository](https://github.com/OnlpLab/NEMO-Corpus)

Named Entity (NER) annotations of the Hebrew Treebank (Haaretz newspaper) corpus, including: morpheme and token level NER labels, nested mentions, and more.  
We publish the NEMO corpus in the TACL paper [*"Neural Modeling for Named Entities and Morphology (NEMO<sup>2</sup>)"*](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00404/107206/Neural-Modeling-for-Named-Entities-and-Morphology) [1], where we use it in extensive experiments and analyses, showing the importance of morphological boundaries for neural modeling of NER in morphologically rich languages. Code for these models and experiments can be found in the [NEMO code repo](https://github.com/OnlpLab/NEMO).

## Main features:
1. Morpheme, token-single and token-multi sequence labels. Morpheme labels provide exact boundaries, token-multi provide partial sub-word morphological but no exact boundaries, token-single provides only token-level information. 
1. All annotations are in `BIOSE` format (`B`=Begin, `I`=Inside, `O`=Outside, `S`=Singleton, `E`=End).
1. Widely-used OntoNotes entity category set: `GPE` (geo-political entity), `PER` (person), `LOC` (location), `ORG` (organization), `FAC` (facility), `EVE` (event), `WOA` (work-of-art), `ANG` (language), `DUC` (product).
1. NEMO includes NER annotations for the two major versions of the Hebrew Treebank, UD (Universal Dependency) and SPMRL. These can be aligned to the other morphosyntactic information layers of the treebank using [bclm](https://github.com/OnlpLab/bclm)
1. We provide nested mentions. Only the first, widest, layer is used in the NEMO<sup>2</sup> paper. We invite you to take on this challenge!
1. Guidelines used for annotation are provided [here](./guidelines/).
1. Corpus was annotated by two native Hebrew speakers of academic education, and curated by the project manager. We provide the original annotations made by the annotators as well to promote work on [learning with disagreements](https://sites.google.com/view/semeval2021-task12/home).
1. Annotation was performed using [WebAnno](https://webanno.github.io/webanno/) (version 3.4.5)


## Legend for Files and Folder Structure
1. The two main [data](./data/) folders are [ud](./data/ud/) and [spmrl](./data/spmrl/), corresponding to the relevant Hebrew Treebank corpus version. 
1. Both contain a `gold` folder ([spmrl/gold](./data/spmrl/gold/), [ud/gold](./data/ud/gold/)) of gold curated annotations. 
1. Each `gold` folder contains files of the three input-output variants (morph, token-multi, token-single), for each of the treebank splits (train,dev,test).
1. Each `gold` folder also contains a `nested`  subfolder ([spmrl/nested](./data/spmrl/gold/nested/), [ud/nested](./data/ud/gold/nested/)), which contains all layers of nested mentions (the first layer is the layer used in the non-nested files, and in the NEMO<sup>2</sup> paper [1])
1. The `ud` folder also contains an [ab_annotators](./data/ud/ab_annotators/) folder. This folder contains the original annotations made by each annotator (named `a`, `b`), including first-layer and nested annotatations.
1. *\*UPDATE 2021-09-06\** `ud` folder now contains a [pilot_annotations](./data/ud/pilot_annotations/) folder. This folder contains the original annotations made by each annotator in our two phase pilot (phase I - sentences 1-200 of dev; phase II - sentences 201-400 of dev).


## Basic Corpus Statistics

|                              | train        | dev          | test          |
|------------------------------|           --:|           --:|            --:|
|  Sentences                   |  4,937       |  500         |  706          |
|  Tokens                      |  93,504      |  8,531       |  12,619       |
|  Morphemes                   |  127,031     |  11,301      |  16,828       |
|  All mentions                |  6,282       |  499         |  932          |
|  Type: Person         (PER)  |  2,128       |  193         |  267          |
|  Type: Organization   (ORG)  |  2,043       |  119         |  408          |
|  Type: Geo-Political  (GPE)  |  1,377       |  121         |  195          |
|  Type: Location       (LOC)  |  331         |  28          |  41           |
|  Type: Facility       (FAC)  |  163         |  12          |  11           |
|  Type: Work-of-Art    (WOA)  |  114         |  9           |  6            |
|  Type: Event          (EVE)  |  57          |  12          |  0            |
|  Type: Product        (DUC)  |  36          |  2           |  3            |
|  Type: Language       (ANG)  |  33          |  3           |  1            |



## Aligned Treenbank Versions
 
The NEMO corpus matches the treebank version of [bclm v.1.0.0](https://github.com/OnlpLab/bclm/releases/tag/v1.0.0-alpha).
This version is based on the [HTB UD v2.2](https://github.com/UniversalDependencies/UD_Hebrew-HTB/releases/tag/r2.2) and the [latest SPMRL HTB version](https://github.com/OnlpLab/HebrewResources/tree/102674bb030f5836e1ab827feb63954ad7a6f8fe/HebrewTreebank/hebtb). 
The changes contain (but might not be limited to the following):
1. Flagged and dropped duplicate and leaking sentences (between train and test). In addition to the sentences already removed in the bclm v1.0.0 HTB version, the following duplicate sentences were dropped as well (SPMRL sentence IDs): 5438, 5444, 5445, 5446, 5448, 5449, 5450, 5451, 5453, 5459 (in the bclm dataframes, these are marked in the `duplicate_sent_id` column).
To read the treebank (UD/SPMRL) in a way that matches the NEMO corpus, you can use the following:
```python
import bclm
dropped = [5438, 5444, 5445, 5446, 5448, 5449, 5450, 5451, 5453, 5459]
spdf = bclm.read_dataframe('spmrl') # load SPMRL treebank dataframe
global_dropped = [spdf[spdf.sent_id==d].global_sent_id.iat[0] for d in dropped]
uddf = bclm.read_dataframe('ud')  # load UD treebank dataframe
uddf = uddf[(~uddf.global_sent_id.isin(global_dropped))] # remove extra duplicates 
spdf = spdf[(~spdf.sent_id.isin(dropped))] # remove extra duplicates
# The resulting dataframes contain gold morph NER labels in the `biose_layer0`, `biose_layer1`... columns.
```
2. The UD treebank contains many more duplicates. In this version: all sentences exist in both UD and SPMRL versions, and all sentences and tokens are aligned between UD and SPMRL.
2. Fixed numbers that were originally reversed.
2. Fixed mismatches between tokens and morphemes.
2. Added Binyan feature.
2. No individual morphemes or tokens were added or removed, only complete sentences.


## Evaluation
An evaluation script is provided in the [NEMO code repo](https://github.com/OnlpLab/NEMO#evaluation) along with evaluation instructions. 


## Citations

##### [1]
If you use the NEMO corpus in your research, please cite the NEMO<sup>2</sup> paper:
```bibtex
@article{10.1162/tacl_a_00404,
    author = {Bareket, Dan and Tsarfaty, Reut},
    title = "{Neural Modeling for Named Entities and Morphology (NEMO2)}",
    journal = {Transactions of the Association for Computational Linguistics},
    volume = {9},
    pages = {909-928},
    year = {2021},
    month = {09},
    abstract = "{Named Entity Recognition (NER) is a fundamental NLP task, commonly formulated as classification over a sequence of tokens. Morphologically rich languages (MRLs) pose a challenge to this basic formulation, as the boundaries of named entities do not necessarily coincide with token boundaries, rather, they respect morphological boundaries. To address NER in MRLs we then need to answer two fundamental questions, namely, what are the basic units to be labeled, and how can these units be detected and classified in realistic settings (i.e., where no gold morphology is available). We empirically investigate these questions on a novel NER benchmark, with parallel token- level and morpheme-level NER annotations, which we develop for Modern Hebrew, a morphologically rich-and-ambiguous language. Our results show that explicitly modeling morphological boundaries leads to improved NER performance, and that a novel hybrid architecture, in which NER precedes and prunes morphological decomposition, greatly outperforms the standard pipeline, where morphological decomposition strictly precedes NER, setting a new performance bar for both Hebrew NER and Hebrew morphological decomposition tasks.}",
    issn = {2307-387X},
    doi = {10.1162/tacl_a_00404},
    url = {https://doi.org/10.1162/tacl\_a\_00404},
    eprint = {https://direct.mit.edu/tacl/article-pdf/doi/10.1162/tacl\_a\_00404/1962472/tacl\_a\_00404.pdf},
}
```

##### [2]
Please cite the Hebrew Treebank as well, described the following paper:
```bibtex
@article{sima2001building,
  title={Building a tree-bank of modern Hebrew text},
  author={Sima’an, Khalil and Itai, Alon and Winter, Yoad and Altman, Alon and Nativ, Noa},
  journal={Traitement Automatique des Langues},
  volume={42},
  number={2},
  pages={247--380},
  year={2001},
  publisher={Citeseer}
}
``` 
##### [3]
The UD version of the Hebrew Treebank is described in:
```bibtex
@inproceedings{sade-etal-2018-hebrew,
    title = "The {H}ebrew {U}niversal {D}ependency Treebank: Past Present and Future",
    author = "Sade, Shoval  and
      Seker, Amit  and
      Tsarfaty, Reut",
    booktitle = "Proceedings of the Second Workshop on Universal Dependencies ({UDW} 2018)",
    month = nov,
    year = "2018",
    address = "Brussels, Belgium",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/W18-6016",
    doi = "10.18653/v1/W18-6016",
    pages = "133--143",
    abstract = "The Hebrew treebank (HTB), consisting of 6221 morpho-syntactically annotated newspaper sentences, has been the only resource for training and validating statistical parsers and taggers for Hebrew, for almost two decades now. During these decades, the HTB has gone through a trajectory of automatic and semi-automatic conversions, until arriving at its UDv2 form. In this work we manually validate the UDv2 version of the HTB, and, according to our findings, we apply scheme changes that bring the UD HTB to the same theoretical grounds as the rest of UD. Our experimental parsing results with UDv2New confirm that improving the coherence and internal consistency of the UD HTB indeed leads to improved parsing performance. At the same time, our analysis demonstrates that there is more to be done at the point of intersection of UD with other linguistic processing layers, in particular, at the points where UD interfaces external morphological and lexical resources.",
}
```