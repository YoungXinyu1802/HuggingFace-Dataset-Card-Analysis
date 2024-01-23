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
- <10K
task_categories:
- token-classification
task_ids:
- named-entity-recognition
pretty_name: MultiNERD
---

# Dataset Card for "tner/multinerd"

## Dataset Description

- **Repository:** [T-NER](https://github.com/asahi417/tner)
- **Paper:** [https://aclanthology.org/2022.findings-naacl.60/](https://aclanthology.org/2022.findings-naacl.60/)
- **Dataset:** MultiNERD
- **Domain:** Wikipedia, WikiNews
- **Number of Entity:** 18


### Dataset Summary
MultiNERD NER benchmark dataset formatted in a part of [TNER](https://github.com/asahi417/tner) project.
- Entity Types: `PER`, `LOC`, `ORG`, `ANIM`, `BIO`, `CEL`, `DIS`, `EVE`, `FOOD`, `INST`, `MEDIA`, `PLANT`, `MYTH`, `TIME`, `VEHI`, `MISC`, `SUPER`, `PHY`

## Dataset Structure

### Data Instances
An example of `train` of `de` looks as follows.

```
{
    'tokens': [ "Die", "Blätter", "des", "Huflattichs", "sind", "leicht", "mit", "den", "sehr", "ähnlichen", "Blättern", "der", "Weißen", "Pestwurz", "(", "\"", "Petasites", "albus", "\"", ")", "zu", "verwechseln", "." ],
    'tags': [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0 ]
}
```

### Label ID
The label2id dictionary can be found at [here](https://huggingface.co/datasets/tner/multinerd/raw/main/dataset/label.json).
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
"B-SUPER": 31,
"I-SUPER": 32,
"B-PHY": 33,
"I-PHY": 34
}
```

### Data Splits

| language   |   test |
|:-----------|-------:|
| de         | 156792 |
| en         | 164144 |
| es         | 173189 |
| fr         | 176185 |
| it         | 181927 |
| nl         | 171711 |
| pl         | 194965 |
| pt         | 177565 |
| ru         |  82858 |

### Citation Information

```
@inproceedings{tedeschi-navigli-2022-multinerd,
    title = "{M}ulti{NERD}: A Multilingual, Multi-Genre and Fine-Grained Dataset for Named Entity Recognition (and Disambiguation)",
    author = "Tedeschi, Simone  and
      Navigli, Roberto",
    booktitle = "Findings of the Association for Computational Linguistics: NAACL 2022",
    month = jul,
    year = "2022",
    address = "Seattle, United States",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.findings-naacl.60",
    doi = "10.18653/v1/2022.findings-naacl.60",
    pages = "801--812",
    abstract = "Named Entity Recognition (NER) is the task of identifying named entities in texts and classifying them through specific semantic categories, a process which is crucial for a wide range of NLP applications. Current datasets for NER focus mainly on coarse-grained entity types, tend to consider a single textual genre and to cover a narrow set of languages, thus limiting the general applicability of NER systems.In this work, we design a new methodology for automatically producing NER annotations, and address the aforementioned limitations by introducing a novel dataset that covers 10 languages, 15 NER categories and 2 textual genres.We also introduce a manually-annotated test set, and extensively evaluate the quality of our novel dataset on both this new test set and standard benchmarks for NER.In addition, in our dataset, we include: i) disambiguation information to enable the development of multilingual entity linking systems, and ii) image URLs to encourage the creation of multimodal systems.We release our dataset at https://github.com/Babelscape/multinerd.",
}
```