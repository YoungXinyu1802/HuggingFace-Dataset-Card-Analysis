---
annotations_creators:
- expert-generated
language_creators:
- found
- expert-generated
language:
- sl
license:
- cc-by-nc-sa-4.0
multilinguality:
- monolingual
size_categories:
- 1K<n<10K
- 10K<n<100K
source_datasets: []
task_categories:
- token-classification
task_ids:
- named-entity-recognition
- part-of-speech
- lemmatization
- parsing
pretty_name: ssj500k
tags:
- semantic-role-labeling
- multiword-expression-detection
---

# Dataset Card for ssj500k

**Important**: there exists another HF implementation of the dataset ([classla/ssj500k](https://huggingface.co/datasets/classla/ssj500k)), but it seems to be more narrowly focused. **This implementation is designed for more general use** - the CLASSLA version seems to expose only the specific training/validation/test annotations used in the CLASSLA library, for only a subset of the data. 

### Dataset Summary

The ssj500k training corpus contains about 500 000 tokens manually annotated on the levels of tokenization, sentence segmentation, morphosyntactic tagging, and lemmatization. It is also partially annotated for the following tasks:
- named entity recognition (config `named_entity_recognition`)  
- dependency parsing(*), Universal Dependencies style (config `dependency_parsing_ud`)  
- dependency parsing, JOS/MULTEXT-East style (config `dependency_parsing_jos`)  
- semantic role labeling (config `semantic_role_labeling`)  
- multi-word expressions (config `multiword_expressions`)  

If you want to load all the data along with their partial annotations, please use the config `all_data`.  

\* _The UD dependency parsing labels are included here for completeness, but using the dataset [universal_dependencies](https://huggingface.co/datasets/universal_dependencies) should be preferred for dependency parsing applications to ensure you are using the most up-to-date data._  

### Supported Tasks and Leaderboards

Sentence tokenization, sentence segmentation, morphosyntactic tagging, lemmatization, named entity recognition, dependency parsing, semantic role labeling, multi-word expression detection.

### Languages

Slovenian.

## Dataset Structure

### Data Instances

A sample instance from the dataset (using the config `all_data`):
```
{
  'id_doc': 'ssj1', 
  'idx_par': 0, 
  'idx_sent': 0, 
  'id_words': ['ssj1.1.1.t1', 'ssj1.1.1.t2', 'ssj1.1.1.t3', 'ssj1.1.1.t4', 'ssj1.1.1.t5', 'ssj1.1.1.t6', 'ssj1.1.1.t7', 'ssj1.1.1.t8', 'ssj1.1.1.t9', 'ssj1.1.1.t10', 'ssj1.1.1.t11', 'ssj1.1.1.t12', 'ssj1.1.1.t13', 'ssj1.1.1.t14', 'ssj1.1.1.t15', 'ssj1.1.1.t16', 'ssj1.1.1.t17', 'ssj1.1.1.t18', 'ssj1.1.1.t19', 'ssj1.1.1.t20', 'ssj1.1.1.t21', 'ssj1.1.1.t22', 'ssj1.1.1.t23', 'ssj1.1.1.t24'], 
  'words': ['"', 'Tistega', 'večera', 'sem', 'preveč', 'popil', ',', 'zgodilo', 'se', 'je', 'mesec', 'dni', 'po', 'tem', ',', 'ko', 'sem', 'izvedel', ',', 'da', 'me', 'žena', 'vara', '.'], 
  'lemmas': ['"', 'tisti', 'večer', 'biti', 'preveč', 'popiti', ',', 'zgoditi', 'se', 'biti', 'mesec', 'dan', 'po', 'ta', ',', 'ko', 'biti', 'izvedeti', ',', 'da', 'jaz', 'žena', 'varati', '.'], 
  'msds': ['UPosTag=PUNCT', 'UPosTag=DET|Case=Gen|Gender=Masc|Number=Sing|PronType=Dem', 'UPosTag=NOUN|Case=Gen|Gender=Masc|Number=Sing', 'UPosTag=AUX|Mood=Ind|Number=Sing|Person=1|Polarity=Pos|Tense=Pres|VerbForm=Fin', 'UPosTag=DET|PronType=Ind', 'UPosTag=VERB|Aspect=Perf|Gender=Masc|Number=Sing|VerbForm=Part', 'UPosTag=PUNCT', 'UPosTag=VERB|Aspect=Perf|Gender=Neut|Number=Sing|VerbForm=Part', 'UPosTag=PRON|PronType=Prs|Reflex=Yes|Variant=Short', 'UPosTag=AUX|Mood=Ind|Number=Sing|Person=3|Polarity=Pos|Tense=Pres|VerbForm=Fin', 'UPosTag=NOUN|Animacy=Inan|Case=Acc|Gender=Masc|Number=Sing', 'UPosTag=NOUN|Case=Gen|Gender=Masc|Number=Plur', 'UPosTag=ADP|Case=Loc', 'UPosTag=DET|Case=Loc|Gender=Neut|Number=Sing|PronType=Dem', 'UPosTag=PUNCT', 'UPosTag=SCONJ', 'UPosTag=AUX|Mood=Ind|Number=Sing|Person=1|Polarity=Pos|Tense=Pres|VerbForm=Fin', 'UPosTag=VERB|Aspect=Perf|Gender=Masc|Number=Sing|VerbForm=Part', 'UPosTag=PUNCT', 'UPosTag=SCONJ', 'UPosTag=PRON|Case=Acc|Number=Sing|Person=1|PronType=Prs|Variant=Short', 'UPosTag=NOUN|Case=Nom|Gender=Fem|Number=Sing', 'UPosTag=VERB|Aspect=Imp|Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin', 'UPosTag=PUNCT'], 
  'has_ne_ann': True, 
  'has_ud_dep_ann': True, 
  'has_jos_dep_ann': True, 
  'has_srl_ann': True, 
  'has_mwe_ann': True, 
  'ne_tags': ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], 
  'ud_dep_head': [5, 2, 5, 5, 5, -1, 7, 5, 7, 7, 7, 10, 13, 10, 17, 17, 17, 13, 22, 22, 22, 22, 17, 5], 
  'ud_dep_rel': ['punct', 'det', 'obl', 'aux', 'advmod', 'root', 'punct', 'parataxis', 'expl', 'aux', 'obl', 'nmod', 'case', 'nmod', 'punct', 'mark', 'aux', 'acl', 'punct', 'mark', 'obj', 'nsubj', 'ccomp', 'punct'], 
  'jos_dep_head': [-1, 2, 5, 5, 5, -1, -1, -1, 7, 7, 7, 10, 13, 10, -1, 17, 17, 13, -1, 22, 22, 22, 17, -1], 
  'jos_dep_rel': ['Root', 'Atr', 'AdvO', 'PPart', 'AdvM', 'Root', 'Root', 'Root', 'PPart', 'PPart', 'AdvO', 'Atr', 'Atr', 'Atr', 'Root', 'Conj', 'PPart', 'Atr', 'Root', 'Conj', 'Obj', 'Sb', 'Obj', 'Root'], 
  'srl_info': [
    {'idx_arg': 2, 'idx_head': 5, 'role': 'TIME'},
    {'idx_arg': 4, 'idx_head': 5, 'role': 'QUANT'},
    {'idx_arg': 10, 'idx_head': 7, 'role': 'TIME'},
    {'idx_arg': 20, 'idx_head': 22, 'role': 'PAT'},
    {'idx_arg': 21, 'idx_head': 22, 'role': 'ACT'},
    {'idx_arg': 22, 'idx_head': 17, 'role': 'RESLT'}
  ],
  'mwe_info': [
    {'type': 'IRV', 'word_indices': [7, 8]}
  ]
}
```

### Data Fields

The following attributes are present in the most general config (`all_data`). Please see below for attributes present in the specific configs.  
- `id_doc`: a string containing the identifier of the document;  
- `idx_par`: an int32 containing the consecutive number of the paragraph, which the current sentence is a part of;  
- `idx_sent`: an int32 containing the consecutive number of the current sentence inside the current paragraph;  
- `id_words`: a list of strings containing the identifiers of words - potentially redundant, helpful for connecting the dataset with external datasets like coref149;  
- `words`: a list of strings containing the words in the current sentence;  
- `lemmas`: a list of strings containing the lemmas in the current sentence;  
- `msds`: a list of strings containing the morphosyntactic description of words in the current sentence;  
- `has_ne_ann`: a bool indicating whether the current example has named entities annotated;  
- `has_ud_dep_ann`: a bool indicating whether the current example has dependencies (in UD style) annotated;  
- `has_jos_dep_ann`: a bool indicating whether the current example has dependencies (in JOS style) annotated;  
- `has_srl_ann`: a bool indicating whether the current example has semantic roles annotated;  
- `has_mwe_ann`: a bool indicating whether the current example has multi-word expressions annotated;    
- `ne_tags`: a list of strings containing the named entity tags encoded using IOB2 - if `has_ne_ann=False` all tokens are annotated with `"N/A"`;  
- `ud_dep_head`: a list of int32 containing the head index for each word (using UD guidelines) - the head index of the root word is `-1`; if `has_ud_dep_ann=False` all tokens are annotated with `-2`;   
- `ud_dep_rel`: a list of strings containing the relation with the head for each word (using UD guidelines) - if `has_ud_dep_ann=False` all tokens are annotated with `"N/A"`;  
- `jos_dep_head`: a list of int32 containing the head index for each word (using JOS guidelines) - the head index of the root word is `-1`; if `has_jos_dep_ann=False` all tokens are annotated with `-2`;  
- `jos_dep_rel`: a list of strings containing the relation with the head for each word (using JOS guidelines) - if `has_jos_dep_ann=False` all tokens are annotated with `"N/A"`;  
- `srl_info`: a list of dicts, each containing index of the argument word, the head (verb) word, and the semantic role - if `has_srl_ann=False` this list is empty;  
- `mwe_info`: a list of dicts, each containing word indices and the type of a multi-word expression;  

#### Data fields in 'named_entity_recognition'
```
['id_doc', 'idx_par', 'idx_sent', 'id_words', 'words', 'lemmas', 'msds', 'ne_tags']
```

#### Data fields in 'dependency_parsing_ud'
```
['id_doc', 'idx_par', 'idx_sent', 'id_words', 'words', 'lemmas', 'msds', 'ud_dep_head', 'ud_dep_rel']
```

#### Data fields in 'dependency_parsing_jos'
```
['id_doc', 'idx_par', 'idx_sent', 'id_words', 'words', 'lemmas', 'msds', 'jos_dep_head', 'jos_dep_rel']
```

#### Data fields in 'semantic_role_labeling'
```
['id_doc', 'idx_par', 'idx_sent', 'id_words', 'words', 'lemmas', 'msds', 'srl_info']
```

#### Data fields in 'multiword_expressions'
```
['id_doc', 'idx_par', 'idx_sent', 'id_words', 'words', 'lemmas', 'msds', 'mwe_info']
```

## Additional Information

### Dataset Curators

Simon Krek; et al. (please see http://hdl.handle.net/11356/1434 for the full list)

### Licensing Information

CC BY-NC-SA 4.0.

### Citation Information

The paper describing the dataset:
```
@InProceedings{krek2020ssj500k,
title = {The ssj500k Training Corpus for Slovene Language Processing},
author={Krek, Simon and Erjavec, Tomaž and Dobrovoljc, Kaja and Gantar, Polona and Arhar Holdt, Spela and Čibej, Jaka and Brank, Janez},
booktitle={Proceedings of the Conference on Language Technologies and Digital Humanities},
year={2020},
pages={24-33}
}
```

The resource itself:
```
@misc{krek2021clarinssj500k,
title = {Training corpus ssj500k 2.3},
author = {Krek, Simon and Dobrovoljc, Kaja and Erjavec, Toma{\v z} and Mo{\v z}e, Sara and Ledinek, Nina and Holz, Nanika and Zupan, Katja and Gantar, Polona and Kuzman, Taja and {\v C}ibej, Jaka and Arhar Holdt, {\v S}pela and Kav{\v c}i{\v c}, Teja and {\v S}krjanec, Iza and Marko, Dafne and Jezer{\v s}ek, Lucija and Zajc, Anja},
url = {http://hdl.handle.net/11356/1434},
year = {2021} }
```

### Contributions

Thanks to [@matejklemen](https://github.com/matejklemen) for adding this dataset.