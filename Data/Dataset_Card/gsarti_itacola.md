---
annotations_creators:
- expert-generated
language_creators:
- expert-generated
language:
- it
license:
- unknown
multilinguality:
- monolingual
pretty_name: itacola
size_categories:
- unknown
source_datasets:
- original
task_categories:
- text-classification
task_ids:
- acceptability-classification
---

# Dataset Card for ItaCoLA

## Table of Contents

- [Dataset Card for ItaCoLA](#dataset-card-for-itacola)
  - [Table of Contents](#table-of-contents)
  - [Dataset Description](#dataset-description)
    - [Dataset Summary](#dataset-summary)
    - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
      - [Acceptability Classification](#acceptability-classification)
    - [Languages](#languages)
  - [Dataset Structure](#dataset-structure)
    - [Data Instances](#data-instances)
      - [Scores Configuration](#scores-configuration)
      - [Phenomena Configuration](#phenomena-configuration)
    - [Data Splits](#data-splits)
    - [Dataset Creation](#dataset-creation)
  - [Additional Information](#additional-information)
    - [Dataset Curators](#dataset-curators)
    - [Licensing Information](#licensing-information)
    - [Citation Information](#citation-information)

## Dataset Description

- **Repository:** [Github](https://github.com/dhfbk/ItaCoLA-dataset)
- **Paper:** [Arxiv](http://ceur-ws.org/Vol-2765/paper169.pdf)
- **Point of Contact:** [Daniela Trotta](dtrotta@unisa.it)

### Dataset Summary

The Italian Corpus of Linguistic Acceptability includes almost 10k sentences taken from linguistic literature with a binary annotation made by the original authors themselves. The work is inspired by the English [Corpus of Linguistic Acceptability](https://nyu-mll.github.io/CoLA/).

**Disclaimer**: *The ItaCoLA corpus is hosted on Github by the [Digital Humanities group at FBK](https://dh.fbk.eu/)*. It was introduced in the article [Monolingual and Cross-Lingual Acceptability Judgments with the Italian CoLA corpus](https://arxiv.org/abs/2109.12053) by [Daniela Trotta](https://dh.fbk.eu/author/daniela/), [Raffaele Guarasci](https://www.icar.cnr.it/persone/guarasci/), [Elisa Leonardelli](https://dh.fbk.eu/author/elisa/), [Sara Tonelli](https://dh.fbk.eu/author/sara/)

### Supported Tasks and Leaderboards

#### Acceptability Classification

The following table is taken from Table 4 of the original paper, where an LSTM and a BERT model pretrained on the Italian languages are fine-tuned on the `train` split of the corpus and evaluated respectively on the `test` split (*In-domain*, `in`) and on the acceptability portion of the [AcCompl-it] corpus (*Out-of-domain*, `out`). Models are evaluated with accuracy (*Acc.*) and Matthews Correlation Coefficient (*MCC*) in both settings. Results are averaged over 10 runs with ±stdev. error bounds.

|          |  `in`, Acc.|  `in`, MCC| `out`, Acc.|`out`, MCC|
|---------:|-----------:|----------:|-----------:|---------:|
|`LSTM`    | 0.794      | 0.278 ± 0.029 | 0.605  | 0.147 ± 0.066 |
|`ITA-BERT`| 0.904      | 0.603 ± 0.022 | 0.683  | 0.198 ± 0.036 |

### Languages

The language data in ItaCoLA is in Italian (BCP-47 `it`)

## Dataset Structure

### Data Instances

#### Scores Configuration

The `scores` configuration contains sentences with acceptability judgments. An example from the `train` split of the `scores` config (default) is provided below.

```json
{
    "unique_id": 1,
    "source": "Graffi_1994",
    "acceptability": 1,
    "sentence": "Quest'uomo mi ha colpito."
}
```

The text is provided as-is, without further preprocessing or tokenization.

The fields are the following:

- `unique_id`: Unique identifier for the sentence across configurations.
- `source`: Original source for the sentence.
- `acceptability`: Binary score, 1 = acceptable, 0 = not acceptable.
- `sentence`: The evaluated sentence.

#### Phenomena Configuration

The `phenomena` configuration contains a sample of sentences from `scores` that has been manually annotated to denote the presence of 9 linguistic phenomena. An example from the `train` split is provided below:

```json
{
    "unique_id": 1,
    "source": "Graffi_1994",
    "acceptability": 1,
    "sentence": "Quest'uomo mi ha colpito.",
    "cleft_construction": 0,
    "copular_construction": 0,
    "subject_verb_agreement": 1,
    "wh_islands_violations": 0,
    "simple": 0,
    "question": 0,
    "auxiliary": 1,
    "bind": 0,
    "indefinite_pronouns": 0
}
```

For each one of the new fields, the value of the binary score denotes the presence (1) or the absence (0) of the respective phenomenon. Refer to the original paper for a detailed description of each phenomenon.

### Data Splits

|     config| train| test|
|----------:|-----:|----:|
|`scores`   | 7801 | 975 |
|`phenomena`| 2088 | -   |

### Dataset Creation

Please refer to the original article [Monolingual and Cross-Lingual Acceptability Judgments with the Italian CoLA corpus](https://arxiv.org/abs/2109.12053) for additional information on dataset creation.

## Additional Information

### Dataset Curators

The authors are the curators of the original dataset. For problems or updates on this 🤗 Datasets version, please contact [gabriele.sarti996@gmail.com](mailto:gabriele.sarti996@gmail.com).

### Licensing Information

No licensing information available.

### Citation Information

Please cite the authors if you use these corpora in your work:

```bibtex
@inproceedings{trotta-etal-2021-monolingual-cross,
    title = "Monolingual and Cross-Lingual Acceptability Judgments with the {I}talian {C}o{LA} corpus",
    author = "Trotta, Daniela  and
      Guarasci, Raffaele  and
      Leonardelli, Elisa  and
      Tonelli, Sara",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2021",
    month = nov,
    year = "2021",
    address = "Punta Cana, Dominican Republic",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.findings-emnlp.250",
    doi = "10.18653/v1/2021.findings-emnlp.250",
    pages = "2929--2940"
}
```
