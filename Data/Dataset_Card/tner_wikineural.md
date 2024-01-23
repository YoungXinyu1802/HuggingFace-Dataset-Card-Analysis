---
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
multilinguality:
- multilingual
size_categories:
- 10K<100k
task_categories:
- token-classification
task_ids:
- named-entity-recognition
pretty_name: WikiNeural
---

# Dataset Card for "tner/wikineural"

## Dataset Description

- **Repository:** [T-NER](https://github.com/asahi417/tner)
- **Paper:** [https://aclanthology.org/2021.findings-emnlp.215/](https://aclanthology.org/2021.findings-emnlp.215/)
- **Dataset:** WikiNeural
- **Domain:** Wikipedia
- **Number of Entity:** 16


### Dataset Summary
WikiAnn NER dataset formatted in a part of [TNER](https://github.com/asahi417/tner) project.
- Entity Types: `PER`, `LOC`, `ORG`, `ANIM`, `BIO`, `CEL`, `DIS`, `EVE`, `FOOD`, `INST`, `MEDIA`, `PLANT`, `MYTH`, `TIME`, `VEHI`, `MISC`

## Dataset Structure

### Data Instances
An example of `train` of `de` looks as follows.

```
{
    'tokens': [ "Dieses", "wiederum", "basierte", "auf", "dem", "gleichnamigen", "Roman", "von", "Noël", "Calef", "." ],
    'tags': [ 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0 ]
}
```

### Label ID
The label2id dictionary can be found at [here](https://huggingface.co/datasets/tner/wikineural/raw/main/dataset/label.json).
```python
{
"O": 0,
"B-PER": 1,
"I-PER": 2,
"B-LOC": 3,
"I-LOC": 4,
"B-ORG": 5,
"I-ORG": 6,
"B-ANIM": 7,
"I-ANIM": 8,
"B-BIO": 9,
"I-BIO": 10,
"B-CEL": 11,
"I-CEL": 12,
"B-DIS": 13,
"I-DIS": 14,
"B-EVE": 15,
"I-EVE": 16,
"B-FOOD": 17,
"I-FOOD": 18,
"B-INST": 19,
"I-INST": 20,
"B-MEDIA": 21,
"I-MEDIA": 22,
"B-PLANT": 23,
"I-PLANT": 24,
"B-MYTH": 25,
"I-MYTH": 26,
"B-TIME": 27,
"I-TIME": 28,
"B-VEHI": 29,
"I-VEHI": 30,
"B-MISC": 31,
"I-MISC": 32
}
```

### Data Splits

| language   |   train |   validation |   test |
|:-----------|--------:|-------------:|-------:|
| de         |   98640 |        12330 |  12372 |
| en         |   92720 |        11590 |  11597 |
| es         |   76320 |         9540 |   9618 |
| fr         |  100800 |        12600 |  12678 |
| it         |   88400 |        11050 |  11069 |
| nl         |   83680 |        10460 |  10547 |
| pl         |  108160 |        13520 |  13585 |
| pt         |   80560 |        10070 |  10160 |
| ru         |   92320 |        11540 |  11580 |

### Citation Information

```
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
    doi = "10.18653/v1/2021.findings-emnlp.215",
    pages = "2521--2533",
    abstract = "Multilingual Named Entity Recognition (NER) is a key intermediate task which is needed in many areas of NLP. In this paper, we address the well-known issue of data scarcity in NER, especially relevant when moving to a multilingual scenario, and go beyond current approaches to the creation of multilingual silver data for the task. We exploit the texts of Wikipedia and introduce a new methodology based on the effective combination of knowledge-based approaches and neural models, together with a novel domain adaptation technique, to produce high-quality training corpora for NER. We evaluate our datasets extensively on standard benchmarks for NER, yielding substantial improvements up to 6 span-based F1-score points over previous state-of-the-art systems for data creation.",
}
```