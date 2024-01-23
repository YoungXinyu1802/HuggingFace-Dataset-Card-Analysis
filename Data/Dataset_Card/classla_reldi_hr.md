---
language:
- hr
license:
- cc-by-sa-4.0
task_categories:
- other
task_ids:
- lemmatization
- named-entity-recognition
- part-of-speech
tags:
- structure-prediction
- normalization
- tokenization
---
This dataset is based on 3,871 Croatian tweets that were segmented into sentences, tokens, and annotated with normalized forms, lemmas, MULTEXT-East tags (XPOS), UPOS tags and morphological features, and named entities.

The dataset contains 6339 training samples (sentences), 815 validation samples and 785 test samples. 
Each sample represents a sentence and includes the following features: sentence ID ('sent\_id'), 
list of tokens ('tokens'), list of normalised tokens ('norms'), list of lemmas ('lemmas'), list of UPOS tags ('upos\_tags'), 
list of MULTEXT-East tags ('xpos\_tags), list of morphological features ('feats'), 
and list of named entity IOB tags ('iob\_tags'), which are encoded as class labels.

If you are using this dataset in your research, please cite the following paper:

```
@article{Miličević_Ljubešić_2016,
title={Tviterasi, tviteraši or twitteraši? Producing and analysing a normalised dataset of Croatian and Serbian tweets}, 
volume={4}, 
url={https://revije.ff.uni-lj.si/slovenscina2/article/view/7007}, 
DOI={10.4312/slo2.0.2016.2.156-188}, 
number={2}, 
journal={Slovenščina 2.0: empirical, applied and interdisciplinary research}, 
author={Miličević, Maja and Ljubešić, Nikola}, 
year={2016}, 
month={Sep.}, 
pages={156–188} }
```
