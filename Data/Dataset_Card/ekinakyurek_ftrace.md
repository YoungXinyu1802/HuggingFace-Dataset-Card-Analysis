---
language:
- en
license:
- cc-by-sa-4.0
- cc-by-nc-4.0
multilinguality:
- monolingual
pretty_name: FTRACE
size_categories:
- 1M<n<10M
source_datasets:
- TRex
- Lama
task_categories:
- influence-attribution
- information-retrieval
- question-answering-retrieval
task_ids:
- influence-attribution
- masked-language-modeling
---
# Dataset Card for "FTRACE"
## Table of Contents
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

- **Homepage:** https://huggingface.co/datasets/ekinakyurek/ftrace
- **Repository:** https://github.com/ekinakyurek/influence
- **Paper:** https://arxiv.org/pdf/2205.11482.pdf
- **Point of Contact:** [Ekin Akyürek](mailto:akyurek@mit.edu)
- **Size of downloaded dataset files:** 113.7 MB
- **Size of the generated dataset:** 1006.6 MB 
- **Total amount of disk used:** 1120.3 MB 

### Dataset Summary
[PAPER]
FTRACE is a zero-shot infromation retrieval benchmark deviced for tracing a language model’s predictions back to training examples. In the accompanying paper, we evaluate commonly studied influence methods, including gradient-based (TracIn) and embedding-based approaches. The dataset contains two parts. First, factual queries for that we trace the knowledge are extracted from existing LAMA queries (Petroni et al., 2019). Second, Wikidata sentences are extracted from TREx corpus (Elsahar et al., 2018). We annotate the extracted sentences with their stated facts, and these facts can be mathed with the facts in query set. In both parts, we provide (input, target) pairs as a masked language modeling task -- see examples in the below. However, one can use the same data in other formalities for example auto-regressive completion via a processing of `input_pretokenized` and `targets_pretokenized` field.    
### Supported Tasks and Leaderboards
[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
### Languages
[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
## Dataset Structure
### Data Instances
#### Abstracts
- **Size of downloaded dataset files:** 112 MB
- **Size of the generated dataset:** 884 MB
- **Total amount of disk used:** 996 MB   

An example of 'abstract' looks as follows.   
```
{"inputs_pretokenized": "The name Austroasiatic comes from the Latin words for \"south\" and \"Asia\", hence \"<extra_id_0>\".", 
 "targets_pretokenized": "<extra_id_0> South Asia", 
 "page_uri": "Q33199", 
 "masked_uri": "Q771405", 
 "masked_type": "subject", 
 "example_uris": "Q33199-1-Q48-Q771405-1", 
 "facts": "P361,Q48,Q771405;P30,Q48,Q771405", 
 "id": 8}
```
#### Queries
- **Size of downloaded dataset files:** 1.7 MB
- **Size of the generated dataset:** 8.9 MB
- **Total amount of disk used:** 10.6 MB   

An example of 'query' looks as follows.   

```
{"inputs_pretokenized": "Paul Ehrlich used to work in <extra_id_0> .", 
"targets_pretokenized": "<extra_id_0> Frankfurt", 
"uuid": "5b063008-a8ba-4064-9f59-e70102bb8c50", 
"obj_uri": "Q1794", 
"sub_uri": "Q57089", 
"predicate_id": "P937",
"obj_surface": "Frankfurt", 
"sub_surface": "Paul Ehrlich"}
```

### Data Fields
The data fields are the same among all splits.   

#### Abstracts
- `inputs_pretokenized`: a `string` feature.
- `targets_pretokenized`: a `string` feature.
- `masked_uri`: a `string` feature.
- `masked_type`: a `string` feature.
- `facts`: a `string` feature.
- `id`: a `string` feature.
- `example_uris`: a `string` feature.
- `page_uri`: a `string` feature.

#### Queries
- `inputs_pretokenized`: a `string` feature.
- `targets_pretokenized`: a `string` feature.
- `obj_surface`: a `string` feature.
- `sub_surface`: a `string` feature.
- `obj_uri`: a `string` feature.
- `sub_uri`: a `string` feature.
- `predicate_id`: a `string` feature.
- `uuid`: a `string` feature.

### Data Splits
|   name    | train |
|-----------|------:|
|Abstracts  |1560453|
|Queries    |31479  |

## Dataset Creation
### Curation Rationale
[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
### Source Data
LAMA: https://github.com/facebookresearch/LAMA   
TRex: https://hadyelsahar.github.io/t-rex/
#### Initial Data Collection and Normalization
[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
#### Who are the source language producers?
[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
### Annotations
#### Annotation process
[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
#### Who are the annotators?
[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
### Personal and Sensitive Information
[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
## Considerations for Using the Data
### Social Impact of Dataset
[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
### Discussion of Biases
[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
### Other Known Limitations
[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
## Additional Information
### Dataset Curators
[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
### Licensing Information
The parts of this dataset are available under the [Creative Commons Attribution-ShareAlike License (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/) and [The Creative Commons Attribution-Noncommercial 4.0 International License](https://github.com/facebookresearch/LAMA/blob/master/LICENSE)
### Citation Information
The main paper should be cited as follow:
```
@misc{https://doi.org/10.48550/arxiv.2205.11482,
  doi = {10.48550/ARXIV.2205.11482},
  url = {https://arxiv.org/abs/2205.11482},
  author = {Akyürek, Ekin and Bolukbasi, Tolga and Liu, Frederick and Xiong, Binbin and Tenney, Ian and Andreas, Jacob and Guu, Kelvin},
  keywords = {Computation and Language (cs.CL), Information Retrieval (cs.IR), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {Tracing Knowledge in Language Models Back to the Training Data},
  publisher = {arXiv},
  year = {2022}, 
}
```

Please also cite Petroni et al., 2019 for the query set, and Elsahar et al., 2018 for the abstract set.

```
@inproceedings{petroni2019language,
  title={Language Models as Knowledge Bases?},
  author={F. Petroni, T. Rockt{\"{a}}schel, A. H. Miller, P. Lewis, A. Bakhtin, Y. Wu and S. Riedel},
  booktitle={In: Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing (EMNLP), 2019},
  year={2019}
}
```

```
@inproceedings{elsahar2018t,
  title={T-rex: A large scale alignment of natural language with knowledge base triples},
  author={Elsahar, Hady and Vougiouklis, Pavlos and Remaci, Arslen and Gravier, Christophe and Hare, Jonathon and Laforest, Frederique and Simperl, Elena},
  booktitle={Proceedings of the Eleventh International Conference on Language Resources and Evaluation (LREC 2018)},
  year={2018}
}
```


### Contributions