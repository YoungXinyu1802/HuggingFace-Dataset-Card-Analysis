---
annotations_creators:
- crowdsourced
- expert-generated
language:
- en
language_creators:
- found
license:
- other
multilinguality:
- monolingual
pretty_name: The TAC Relation Extraction Dataset and TACRED Revisited
size_categories:
- 100K<n<1M
source_datasets:
- extended|other
tags:
- relation extraction
task_categories:
- text-classification
task_ids:
- multi-class-classification
---
# Dataset Card for "tacred"
## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)
## Dataset Description
- **Homepage:** [https://nlp.stanford.edu/projects/tacred](https://nlp.stanford.edu/projects/tacred)
- **Paper:** [Position-aware Attention and Supervised Data Improve Slot Filling](https://aclanthology.org/D17-1004/)
- **Point of Contact:** See [https://nlp.stanford.edu/projects/tacred/](https://nlp.stanford.edu/projects/tacred/)
- **Size of downloaded dataset files:** 62.3 MB
- **Size of the generated dataset:** 139.2 MB
- **Total amount of disk used:** 201.5 MB
### Dataset Summary
The TAC Relation Extraction Dataset (TACRED) is a large-scale relation extraction dataset with 106,264 examples built over newswire and web text from the corpus used in the yearly TAC Knowledge Base Population (TAC KBP) challenges. Examples in TACRED cover 41 relation types as used in the TAC KBP challenges (e.g., per:schools_attended
and org:members) or are labeled as no_relation if no defined relation is held. These examples are created by combining available human annotations from the TAC
KBP challenges and crowdsourcing. Please see [Stanford's EMNLP paper](https://nlp.stanford.edu/pubs/zhang2017tacred.pdf), or their [EMNLP slides](https://nlp.stanford.edu/projects/tacred/files/position-emnlp2017.pdf) for full details.

Note: 
- There is currently a [label-corrected version](https://github.com/DFKI-NLP/tacrev) of the TACRED dataset, which you should consider using instead of
the original version released in 2017. For more details on this new version, see the [TACRED Revisited paper](https://aclanthology.org/2020.acl-main.142/)
published at ACL 2020.
- There is also a [relabeled and pruned version](https://github.com/gstoica27/Re-TACRED) of the TACRED dataset. 
For more details on this new version, see the [Re-TACRED paper](https://arxiv.org/abs/2104.08398)
published at ACL 2020.

This repository provides all three versions of the dataset as BuilderConfigs - `'original'`, `'revisited'` and `'re-tacred'`.
Simply set the `name` parameter in the `load_dataset` method in order to choose a specific version. The original TACRED is loaded per default.

### Supported Tasks and Leaderboards
- **Tasks:** Relation Classification
- **Leaderboards:** [https://paperswithcode.com/sota/relation-extraction-on-tacred](https://paperswithcode.com/sota/relation-extraction-on-tacred)
### Languages
The language in the dataset is English.
## Dataset Structure
### Data Instances
- **Size of downloaded dataset files:** 62.3 MB
- **Size of the generated dataset:** 139.2 MB
- **Total amount of disk used:** 201.5 MB

An example of 'train' looks as follows:
```json
{
  "id": "61b3a5c8c9a882dcfcd2",
  "docid": "AFP_ENG_20070218.0019.LDC2009T13",
  "relation": "org:founded_by",
  "token": ["Tom", "Thabane", "resigned", "in", "October", "last", "year", "to", "form", "the", "All", "Basotho", "Convention", "-LRB-", "ABC", "-RRB-", ",", "crossing", "the", "floor", "with", "17", "members", "of", "parliament", ",", "causing", "constitutional", "monarch", "King", "Letsie", "III", "to", "dissolve", "parliament", "and", "call", "the", "snap", "election", "."],
  "subj_start": 10,
  "subj_end": 13,
  "obj_start": 0,
  "obj_end": 2,
  "subj_type": "ORGANIZATION",
  "obj_type": "PERSON",
  "stanford_pos": ["NNP", "NNP", "VBD", "IN", "NNP", "JJ", "NN", "TO", "VB", "DT", "DT", "NNP", "NNP", "-LRB-", "NNP", "-RRB-", ",", "VBG", "DT", "NN", "IN", "CD", "NNS", "IN", "NN", ",", "VBG", "JJ", "NN", "NNP", "NNP", "NNP", "TO", "VB", "NN", "CC", "VB", "DT", "NN", "NN", "."],
  "stanford_ner": ["PERSON", "PERSON", "O", "O", "DATE", "DATE", "DATE", "O", "O", "O", "O", "O", "O", "O", "ORGANIZATION", "O", "O", "O", "O", "O", "O", "NUMBER", "O", "O", "O", "O", "O", "O", "O", "O", "PERSON", "PERSON", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
  "stanford_head": [2, 3, 0, 5, 3, 7, 3, 9, 3, 13, 13, 13, 9, 15, 13, 15, 3, 3, 20, 18, 23, 23, 18, 25, 23, 3, 3, 32, 32, 32, 32, 27, 34, 27, 34, 34, 34, 40, 40, 37, 3],
  "stanford_deprel": ["compound", "nsubj", "ROOT", "case", "nmod", "amod", "nmod:tmod", "mark", "xcomp", "det", "compound", "compound", "dobj", "punct", "appos", "punct", "punct", "xcomp", "det", "dobj", "case", "nummod", "nmod", "case", "nmod", "punct", "xcomp", "amod", "compound", "compound", "compound", "dobj", "mark", "xcomp", "dobj", "cc", "conj", "det", "compound", "dobj", "punct"]
}
```
### Data Fields
The data fields are the same among all splits.

- `id`: the instance id of this sentence, a `string` feature.
- `docid`: the TAC KBP document id of this sentence, a `string` feature.
- `token`: the list of tokens of this sentence, obtained with the StanfordNLP toolkit, a `list` of `string` features.
- `relation`: the relation label of this instance, a `string` classification label.
- `subj_start`: the 0-based index of the start token of the relation subject mention, an `ìnt` feature.
- `subj_end`: the 0-based index of the end token of the relation subject mention, exclusive, an `ìnt` feature.
- `subj_type`: the NER type of the subject mention, among 23 fine-grained types used in the [Stanford NER system](https://stanfordnlp.github.io/CoreNLP/ner.html), a `string` feature.
- `obj_start`: the 0-based index of the start token of the relation object mention, an `ìnt` feature.
- `obj_end`: the 0-based index of the end token of the relation object mention, exclusive, an `ìnt` feature.
- `obj_type`: the NER type of the object mention, among 23 fine-grained types used in the [Stanford NER system](https://stanfordnlp.github.io/CoreNLP/ner.html), a `string` feature.
- `stanford_pos`: the part-of-speech tag per token. the NER type of the subject mention, among 23 fine-grained types used in the [Stanford NER system](https://stanfordnlp.github.io/CoreNLP/ner.html), a `list` of `string` features.
- `stanford_ner`: the NER tags of tokens (IO-Scheme), among 23 fine-grained types used in the [Stanford NER system](https://stanfordnlp.github.io/CoreNLP/ner.html), a `list` of `string` features.
- `stanford_deprel`: the Stanford dependency relation tag per token, a `list` of `string` features.
- `stanford_head`: the head (source) token index (0-based) for the dependency relation per token. The root token has a head index of -1, a `list` of `int` features.
### Data Splits
To miminize dataset bias, TACRED is stratified across years in which the TAC KBP challenge was run:
|           | Train  |  Dev  | Test |
| -----     | ------ | ----- | ---- |
| TACRED     | 68,124 (TAC KBP 2009-2012) | 22,631 (TAC KBP 2013) | 15,509 (TAC KBP 2014) |
| Re-TACRED     | 58,465 (TAC KBP 2009-2012) | 19,584 (TAC KBP 2013) | 13,418 (TAC KBP 2014) |
## Dataset Creation
### Curation Rationale
[More Information Needed]
### Source Data
#### Initial Data Collection and Normalization
[More Information Needed]
#### Who are the source language producers?
[More Information Needed]
### Annotations
#### Annotation process
See the Stanford paper and the Tacred Revisited paper, plus their appendices.

To ensure that models trained on TACRED are not biased towards predicting false positives on real-world text,
all sampled sentences where no relation was found between the mention pairs were fully annotated to be negative examples. As a result, 79.5% of the examples
are labeled as no_relation.
#### Who are the annotators?
[More Information Needed]
### Personal and Sensitive Information
[More Information Needed]
## Considerations for Using the Data
### Social Impact of Dataset
[More Information Needed]
### Discussion of Biases
[More Information Needed]
### Other Known Limitations
[More Information Needed]
## Additional Information
### Dataset Curators
[More Information Needed]
### Licensing Information
To respect the copyright of the underlying TAC KBP corpus, TACRED is released via the
Linguistic Data Consortium ([LDC License](https://catalog.ldc.upenn.edu/license/ldc-non-members-agreement.pdf)).
You can download TACRED from the [LDC TACRED webpage](https://catalog.ldc.upenn.edu/LDC2018T24).
If you are an LDC member, the access will be free; otherwise, an access fee of $25 is needed.
### Citation Information
The original dataset:
```
@inproceedings{zhang2017tacred,
  author = {Zhang, Yuhao and Zhong, Victor and Chen, Danqi and Angeli, Gabor and Manning, Christopher D.},
  booktitle = {Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing (EMNLP 2017)},
  title = {Position-aware Attention and Supervised Data Improve Slot Filling},
  url = {https://nlp.stanford.edu/pubs/zhang2017tacred.pdf},
  pages = {35--45},
  year = {2017}
}
```

For the revised version (`"revisited"`), please also cite:
```
@inproceedings{alt-etal-2020-tacred,
    title = "{TACRED} Revisited: A Thorough Evaluation of the {TACRED} Relation Extraction Task",
    author = "Alt, Christoph  and
      Gabryszak, Aleksandra  and
      Hennig, Leonhard",
    booktitle = "Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics",
    month = jul,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.acl-main.142",
    doi = "10.18653/v1/2020.acl-main.142",
    pages = "1558--1569",
}
```

For the relabeled version (`"re-tacred"`), please also cite:
```
@article{stoica2021re,
  author    = {George Stoica and
               Emmanouil Antonios Platanios and
               Barnab{\'{a}}s P{\'{o}}czos},
  title     = {Re-TACRED: Addressing Shortcomings of the {TACRED} Dataset},
  journal   = {CoRR},
  volume    = {abs/2104.08398},
  year      = {2021},
  url       = {https://arxiv.org/abs/2104.08398},
  eprinttype = {arXiv},
  eprint    = {2104.08398},
  timestamp = {Mon, 26 Apr 2021 17:25:10 +0200},
  biburl    = {https://dblp.org/rec/journals/corr/abs-2104-08398.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```

### Contributions
Thanks to [@dfki-nlp](https://github.com/dfki-nlp) and [@phucdev](https://github.com/phucdev) for adding this dataset.
