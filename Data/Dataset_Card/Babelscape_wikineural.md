---
annotations_creators:
- machine-generated
language_creators:
- machine-generated
language:
- de
- en
- es
- fr
- it
- nl
- pl
- pt
- ru
license:
- cc-by-nc-sa-4.0
multilinguality:
- multilingual
source_datasets:
- original
task_categories:
- token-classification
task_ids:
- named-entity-recognition
pretty_name: wikineural-dataset
tags:
- structure-prediction
---

## Table of Contents
- [Description](#description)
- [Dataset Structure](#dataset-structure)
- [Additional Information](#additional-information)
  
## Dataset Card for WikiNEuRal dataset

## Dataset Description

- **Summary:** Training data for NER in 9 languages.
- **Repository:** [https://github.com/Babelscape/wikineural](https://github.com/Babelscape/wikineural)
- **Paper:** [https://aclanthology.org/wikineural](https://aclanthology.org/2021.findings-emnlp.215/)
- **Point of Contact:** [tedeschi@babelscape.com](tedeschi@babelscape.com)


## Description

- **Summary:** In a nutshell, WikiNEuRal consists in a novel technique which builds upon a multilingual lexical knowledge base (i.e., [BabelNet](https://babelnet.org/)) and transformer-based architectures (i.e., [BERT](https://arxiv.org/abs/1810.04805)) to produce high-quality annotations for multilingual NER. It shows consistent improvements of up to 6 span-based F1-score points against state-of-the-art alternative data production methods on common benchmarks for NER. We used this methodology to automatically generate training data for NER in 9 languages.
- **Repository:** [https://github.com/Babelscape/wikineural](https://github.com/Babelscape/wikineural)
- **Paper:** [https://aclanthology.org/wikineural](https://aclanthology.org/2021.findings-emnlp.215/)
- **Point of Contact:** [tedeschi@babelscape.com](tedeschi@babelscape.com)

## Dataset Structure

The data fields are the same among all splits.
- `tokens`: a `list` of `string` features.
- `ner_tags`: a `list` of classification labels (`int`). Full tagset with indices:
```python
{'O': 0, 'B-PER': 1, 'I-PER': 2, 'B-ORG': 3, 'I-ORG': 4, 'B-LOC': 5, 'I-LOC': 6, 'B-MISC': 7, 'I-MISC': 8}
```
- `lang`: a `string` feature. Full list of language: Dutch (nl), English (en), French (fr), German (de), Italian (it), Polish (pl), Portugues (pt), Russian (ru), Spanish (es).


## Dataset Statistics

The table below shows the number of sentences, number of tokens and number of instances per class, for each of the 9 languages.

| Dataset Version | Sentences | Tokens | PER | ORG | LOC | MISC | OTHER |
| :------------- | -------------: | -------------: | -------------: | -------------: | -------------: | -------------: | -------------: |
| WikiNEuRal EN | 116k | 2.73M | 51k | 31k | 67k | 45k | 2.40M |
| WikiNEuRal ES | 95k | 2.33M | 43k | 17k | 68k | 25k | 2.04M |
| WikiNEuRal NL | 107k | 1.91M | 46k | 22k | 61k | 24k | 1.64M |
| WikiNEuRal DE | 124k | 2.19M | 60k | 32k | 59k | 25k | 1.87M |
| WikiNEuRal RU | 123k | 2.39M | 40k | 26k | 89k | 25k | 2.13M |
| WikiNEuRal IT | 111k | 2.99M | 67k | 22k | 97k | 26k | 2.62M |
| WikiNEuRal FR | 127k | 3.24M | 76k | 25k | 101k | 29k | 2.83M |
| WikiNEuRal PL | 141k | 2.29M | 59k | 34k | 118k | 22k | 1.91M |
| WikiNEuRal PT | 106k | 2.53M | 44k | 17k | 112k | 25k | 2.20M |

## Additional Information

- **Licensing Information**: Contents of this repository are restricted to only non-commercial research purposes under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/). Copyright of the dataset contents belongs to the original copyright holders.

- **Citation Information**: Please consider citing our work if you use data and/or code from this repository.
```bibtex
@inproceedings{tedeschi-etal-2021-wikineural-combined,
    title = "{W}iki{NE}u{R}al: {C}ombined Neural and Knowledge-based Silver Data Creation for Multilingual {NER}",
    author = "Tedeschi, Simone  and
      Maiorca, Valentino  and
      Campolungo, Niccol{\`o}  and
      Cecconi, Francesco  and
      Navigli, Roberto",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2021",
    month = nov,
    year = "2021",
    address = "Punta Cana, Dominican Republic",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.findings-emnlp.215",
    pages = "2521--2533",
    abstract = "Multilingual Named Entity Recognition (NER) is a key intermediate task which is needed in many areas of NLP. In this paper, we address the well-known issue of data scarcity in NER, especially relevant when moving to a multilingual scenario, and go beyond current approaches to the creation of multilingual silver data for the task. We exploit the texts of Wikipedia and introduce a new methodology based on the effective combination of knowledge-based approaches and neural models, together with a novel domain adaptation technique, to produce high-quality training corpora for NER. We evaluate our datasets extensively on standard benchmarks for NER, yielding substantial improvements up to 6 span-based F1-score points over previous state-of-the-art systems for data creation.",
}
```
- **Contributions**: Thanks to [@sted97](https://github.com/sted97) for adding this dataset.
