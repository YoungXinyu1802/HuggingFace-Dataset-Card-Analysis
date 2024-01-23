---
language:
- multilingual
license:
- cc-by-nc-sa-4.0 
multilinguality:
- multilingual
source_datasets:
- FLORES-101, FLORES-200, PAWS-X, XNLI, XTREME, WinoMT, Wino-X, MuCOW, EuroParl ConDisco, ParcorFull
task_categories:
- translation
pretty_name: ACES

---

# Dataset Card for ACES

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
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
    - [Discussion of Biases](#discussion-of-biases)
    - [Usage](#usage)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contact](#contact)
  
## Dataset Description

- **Repository:** [ACES dataset repository](https://github.com/EdinburghNLP/ACES)
- **Paper:** [arXiv](https://arxiv.org/abs/2210.15615)


### Dataset Summary

ACES consists of 36,476 examples covering 146 language pairs and representing challenges from 68 phenomena for evaluating machine translation metrics. We focus on translation accuracy errors and base the phenomena covered in our challenge set on the Multidimensional Quality Metrics (MQM) ontology. The phenomena range from simple perturbations at the word/character level to more complex errors based on discourse and real-world knowledge. 
### Supported Tasks and Leaderboards

-Machine translation evaluation of metrics

-Potentially useful for contrastive machine translation evaluation

### Languages

The dataset covers 146 language pairs as follows: 

af-en, af-fa, ar-en, ar-fr, ar-hi, be-en, bg-en, bg-lt, ca-en, ca-es, cs-en, da-en, de-en, de-es, de-fr, de-ja, de-ko, de-ru, de-zh, el-en, en-af, en-ar, en-be, en-bg, en-ca, en-cs, en-da, en-de, en-el, en-es, en-et, en-fa, en-fi, en-fr, en-gl, en-he, en-hi, en-hr, en-hu, en-hy, en-id, en-it, en-ja, en-ko, en-lt, en-lv, en-mr, en-nl, en-no, en-pl, en-pt, en-ro, en-ru, en-sk, en-sl, en-sr, en-sv, en-ta, en-tr, en-uk, en-ur, en-vi, en-zh, es-ca, es-de, es-en, es-fr, es-ja, es-ko, es-zh, et-en, fa-af, fa-en, fi-en, fr-de, fr-en, fr-es, fr-ja, fr-ko, fr-mr, fr-ru, fr-zh, ga-en, gl-en, he-en, he-sv, hi-ar, hi-en, hr-en, hr-lv, hu-en, hy-en, hy-vi, id-en, it-en, ja-de, ja-en, ja-es, ja-fr, ja-ko, ja-zh, ko-de, ko-en, ko-es, ko-fr, ko-ja, ko-zh, lt-bg, lt-en, lv-en, lv-hr, mr-en, nl-en, no-en, pl-en, pl-mr, pl-sk, pt-en, pt-sr, ro-en, ru-de, ru-en, ru-es, ru-fr, sk-en, sk-pl, sl-en, sr-en, sr-pt, sv-en, sv-he, sw-en, ta-en, th-en, tr-en, uk-en, ur-en, vi-en, vi-hy, wo-en, zh-de, zh-en, zh-es, zh-fr, zh-ja, zh-ko

## Dataset Structure

### Data Instances

Each data instance contains the following features: _source_, _good-translation_, _incorrect-translation_, _reference_, _phenomena_, _langpair_

See the [ACES corpus viewer](https://huggingface.co/datasets/nikitam/ACES/viewer/nikitam--ACES/train) to explore more examples.

An example from the ACES challenge set looks like the following:
```
{'source': "Proper nutritional practices alone cannot generate elite performances, but they can significantly affect athletes' overall wellness.", 'good-translation': 'Las prácticas nutricionales adecuadas por sí solas no pueden generar rendimiento de élite, pero pueden afectar significativamente el bienestar general de los atletas.', 'incorrect-translation': 'Las prácticas nutricionales adecuadas por sí solas no pueden generar rendimiento de élite, pero pueden afectar significativamente el bienestar general de los jóvenes atletas.', 'reference': 'No es posible que las prácticas nutricionales adecuadas, por sí solas, generen un rendimiento de elite, pero puede influir en gran medida el bienestar general de los atletas .', 'phenomena': 'addition', 'langpair': 'en-es'}


```

### Data Fields

- 'source': a string containing the text that needs to be translated
- 'good-translation': possible translation of the source sentence
- 'incorrect-translation': translation of the source sentence that contains an error or phenomenon of interest
- 'reference': the gold standard translation 
- 'phenomena': the type of error or phenomena being studied in the example
- 'langpair': the source language and the target language pair of the example

Note that the _good-translation_ may not be free of errors but it is a better translation than the _incorrect-translation_

### Data Splits

The ACES dataset has 1 split: _train_ which contains the challenge set. There are  36476 examples. 

## Dataset Creation

### Curation Rationale

With the advent of neural networks and especially Transformer-based architectures, machine translation outputs have become more and more fluent. Fluency errors are also judged less severely than accuracy errors by human evaluators \citep{freitag-etal-2021-experts} which reflects the fact that accuracy errors can have dangerous consequences in certain contexts, for example in the medical and legal domains. For these reasons, we decided to build a challenge set focused on accuracy errors. 

Another aspect we focus on is including a broad range of language pairs in ACES. Whenever possible we create examples for all language pairs covered in a source dataset when we use automatic approaches. For phenomena where we create examples manually, we also aim to cover at least two language pairs per phenomenon but are of course limited to the languages spoken by the authors.

We aim to offer a collection of challenge sets covering both easy and hard phenomena. While it may be of interest to the community to continuously test on harder examples to check where machine translation evaluation metrics still break, we believe that easy challenge sets are just as important to ensure that metrics do not suddenly become worse at identifying error types that were previously considered ``solved''. Therefore, we take a holistic view when creating ACES and do not filter out individual examples or exclude challenge sets based on baseline metric performance or other factors.



### Source Data

#### Initial Data Collection and Normalization

Please see Sections 4 and 5 of the paper. 

#### Who are the source language producers?

The dataset contains sentences found in FLORES-101, FLORES-200, PAWS-X, XNLI, XTREME, WinoMT, Wino-X, MuCOW, EuroParl ConDisco, ParcorFull datasets. Please refer to the respective papers for further details. 

### Personal and Sensitive Information

The external datasets may contain sensitive information. Refer to the respective datasets for further details. 

## Considerations for Using the Data

### Usage

ACES has been primarily designed to evaluate machine translation metrics on the accuracy errors. We expect the metric to score _good-translation_ consistently higher than _incorrect-translation_. We report the performance of metric based on Kendall-tau like correlation. It measures the number of times a metric scores the good translation above the incorrect translation (concordant) and equal to or lower than the incorrect translation (discordant).

### Discussion of Biases

Some examples within the challenge set exhibit biases, however, this is necessary in order to expose the limitations of existing metrics.

### Other Known Limitations
The ACES challenge set exhibits a number of biases. Firstly, there is greater coverage in terms of phenomena and the number of examples for the en-de and en-fr language pairs. This is in part due to the manual effort required to construct examples for some phenomena, in particular, those belonging to the discourse-level and real-world knowledge categories. Further, our choice of language pairs is also limited to the ones available in XLM-R. Secondly, ACES contains more examples for those phenomena for which examples could be generated automatically, compared to those that required manual construction/filtering. Thirdly, some of the automatically generated examples require external libraries which are only available for a few languages (e.g. Multilingual Wordnet). Fourthly, the focus of the challenge set is on accuracy errors. We leave the development of challenge sets for fluency errors to future work.

As a result of using existing datasets as the basis for many of the examples, errors present in these datasets may be propagated through into ACES. Whilst we acknowledge that this is undesirable, in our methods for constructing the incorrect translation we aim to ensure that the quality of the incorrect translation is always worse than the corresponding good translation.

The results and analyses presented in the paper exclude those metrics submitted to the WMT 2022 metrics shared task that provides only system-level outputs. We focus on metrics that provide segment-level outputs as this enables us to provide a broad overview of metric performance on different phenomenon categories and to conduct fine-grained analyses of performance on individual phenomena. For some of the fine-grained analyses, we apply additional constraints based on the language pairs covered by the metrics, or whether the metrics take the source as input, to address specific questions of interest. As a result of applying some of these additional constraints, our investigations tend to focus more on high and medium-resource languages than on low-resource languages. We hope to address this shortcoming in future work.


## Additional Information


### Licensing Information

The ACES dataset is Creative Commons Attribution Non-Commercial Share Alike 4.0 (cc-by-nc-sa-4.0) 

### Citation Information

@inproceedings{amrhein-aces-2022,
title = "{ACES}: Translation Accuracy Challenge Sets for Evaluating Machine Translation Metrics",
author = {Amrhein, Chantal  and
  Moghe, Nikita and
  Guillou, Liane},
booktitle = "Seventh Conference on Machine Translation (WMT22)",
month = dec,
year = "2022",
address = "Abu Dhabi, United Arab Emirates",
publisher = "Association for Computational Linguistics",
eprint = {2210.15615}
}

### Contact
[Chantal Amrhein](mailto:amrhein@cl.uzh.ch) and [Nikita Moghe](mailto:nikita.moghe@ed.ac.uk) and [Liane Guillou](mailto:lguillou@ed.ac.uk)

Dataset card based on [Allociné](https://huggingface.co/datasets/allocine) 