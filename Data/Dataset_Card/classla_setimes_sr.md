---
language:
- sr
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

The SETimes\_sr training corpus contains 86,726 Serbian tokens manually annotated on the levels of tokenisation, sentence segmentation, morphosyntactic tagging, lemmatisation, named entities and dependency syntax.

The dataset contains 3177 training samples, 395 validation samples and 319 test samples 
across the respective data splits. Each sample represents a sentence and includes the following features:
sentence ID ('sent\_id'), sentence text ('text'), list of tokens ('tokens'), list of lemmas ('lemmas'), 
list of MULTEXT-East tags ('xpos\_tags), list of UPOS tags ('upos\_tags'), 
list of morphological features ('feats'), list of IOB tags ('iob\_tags') and list of universal dependencies ('uds'). 

Three dataset configurations are available, namely 'ner', 'upos', and 'ud', with the corresponding features
encoded as class labels. If the configuration is not specified, it defaults to 'ner'.

If you use this dataset in your research, please cite the following paper:

```
@inproceedings{samardzic-etal-2017-universal,
    title = "{U}niversal {D}ependencies for {S}erbian in Comparison with {C}roatian and Other {S}lavic Languages",
    author = "Samard{\v{z}}i{\'c}, Tanja  and
      Starovi{\'c}, Mirjana  and
      Agi{\'c}, {\v{Z}}eljko  and
      Ljube{\v{s}}i{\'c}, Nikola",
    booktitle = "Proceedings of the 6th Workshop on {B}alto-{S}lavic Natural Language Processing",
    month = apr,
    year = "2017",
    address = "Valencia, Spain",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/W17-1407",
    doi = "10.18653/v1/W17-1407",
    pages = "39--44",
}
```