---
language:
- en
- ru
- ayr
- bho
- dyu
- fur
- wol


annotations_creators:
- found
language_creators:
- expert-generated
license:
- cc-by-sa-4.0
multilinguality:
- multilingual
- translation
pretty_name: nllb-multi-domain
size_categories:
- unknown
source_datasets:
- extended|flores
task_categories:
- conditional-text-generation
task_ids:
- machine-translation
paperswithcode_id: flores
---

# Dataset Card for NLLB Multi-Domain

## Table of Contents

- [Dataset Card for NLLB Multi-Domain](#dataset-card-for-nllb-multi-domain)
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
  - [Additional Information](#additional-information)
    - [Dataset Curators](#dataset-curators)
    - [Licensing Information](#licensing-information)
    - [Citation Information](#citation-information)

## Dataset Description

- **Home:** [Flores](https://github.com/facebookresearch/flores/tree/main/nllb_md)
- **Repository:** [Github](https://github.com/facebookresearch/flores/tree/main/nllb_md)

### Dataset Summary

NLLB Multi Domain is a set of professionally-translated sentences in News, Unscripted informal speech, and Health domains. It is designed to enable assessment of out-of-domain performance and to study domain adaptation for machine translation. Each domain has approximately 3000 sentences.

### Supported Tasks and Leaderboards
#### Multilingual Machine Translation
Refer to the [Dynabench leaderboard](https://dynabench.org/flores/Flores%20MT%20Evaluation%20(FULL)) for additional details on model evaluation on FLORES-101 in the context of the WMT2021 shared task on [Large-Scale Multilingual Machine Translation](http://www.statmt.org/wmt21/large-scale-multilingual-translation-task.html). Flores 200 is an extention of this.

### Languages

Language | FLORES-200 code
---|---
Central Aymara | ayr_Latn
Bhojpuri | bho_Deva
Dyula | dyu_Latn
Friulian | fur_Latn
Russian | rus_Cyrl
Wolof | wol_Latn

Use a hyphenated pairing to get two langauges in one datapoint (e.g., "eng_Latn-rus_Cyrl" will provide sentences in the format below).

## Dataset Structure
### Data Instances

See Dataset Viewer.

The text is provided as-in the original dataset, without further preprocessing or tokenization.

### Data Fields
- `id`: Row number for the data entry, starting at 1.
- `sentence`: The full sentence in the specific language (may have _lang for pairings)
- `domain`: The domain of the sentence.

### Dataset Creation
Please refer to the original article [No Language Left Behind: Scaling Human-Centered Machine Translation](https://arxiv.org/abs/2207.04672) for additional information on dataset creation.
## Additional Information
### Dataset Curators
See paper for details.
### Licensing Information
Licensed with Creative Commons Attribution Share Alike 4.0. License available [here](https://creativecommons.org/licenses/by-sa/4.0/).

### Citation Information
Please cite the authors if you use these corpora in your work:

```bibtex
@article{nllb2022,
  author    = {NLLB Team, Marta R. Costa-jussà, James Cross, Onur Çelebi, Maha Elbayad, Kenneth Heafield, Kevin Heffernan, Elahe Kalbassi,  Janice Lam, Daniel Licht, Jean Maillard, Anna Sun, Skyler Wang, Guillaume Wenzek, Al Youngblood, Bapi Akula, Loic Barrault, Gabriel Mejia Gonzalez, Prangthip Hansanti, John Hoffman, Semarley Jarrett, Kaushik Ram Sadagopan, Dirk Rowe, Shannon Spruit, Chau Tran, Pierre Andrews, Necip Fazil Ayan, Shruti Bhosale, Sergey Edunov, Angela Fan, Cynthia Gao, Vedanuj Goswami, Francisco Guzmán, Philipp Koehn, Alexandre Mourachko, Christophe Ropers, Safiyyah Saleem, Holger Schwenk, Jeff Wang},
  title     = {No Language Left Behind: Scaling Human-Centered Machine Translation},
  year      = {2022}
}
```

Please also cite prior work that this dataset builds on:

```bibtex
@inproceedings{,
  title={The FLORES-101  Evaluation Benchmark for Low-Resource and Multilingual Machine Translation},
  author={Goyal, Naman and Gao, Cynthia and Chaudhary, Vishrav and Chen, Peng-Jen and Wenzek, Guillaume and Ju, Da and Krishnan, Sanjana and Ranzato, Marc'Aurelio and Guzm\'{a}n, Francisco and Fan, Angela},
  year={2021}
}
```

```bibtex
@inproceedings{,
  title={Two New Evaluation Datasets for Low-Resource Machine Translation: Nepali-English and Sinhala-English},
  author={Guzm\'{a}n, Francisco and Chen, Peng-Jen and Ott, Myle and Pino, Juan and Lample, Guillaume and Koehn, Philipp and Chaudhary, Vishrav and Ranzato, Marc'Aurelio},
  journal={arXiv preprint arXiv:1902.01382},
  year={2019}
}
```