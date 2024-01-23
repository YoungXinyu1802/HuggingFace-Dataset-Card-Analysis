# Dataset Card for ru-med-ner

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-instances)
- [Additional Information](#additional-information)
  - [Citation Information](#citation-information)

## Dataset Description

- **Homepage:** https://github.com/pavel-blinov/RuMedBench
- **Repository:** https://github.com/pavel-blinov/RuMedBench
- **Paper:** https://arxiv.org/abs/2201.06499
- **Leaderboard:** https://github.com/pavel-blinov/RuMedBench
- **Point of Contact:** Blinov.P.D@sberbank.ru

### Dataset Summary

NER dataset for Russian language, extracted from medical records\\
See https://github.com/pavel-blinov/RuMedBench for details

### Supported Tasks and Leaderboards

[Needs More Information]

### Languages

- ru-RU

## Dataset Structure

### Data Instances

```javascript
{"idx": "2472239.tsv_0", "tokens": ["", "?5@2K9", "65", "45=L", "?@8<5=5=8O", "2K?8;0", "5", "B01;5B>:", ",", "?@>A=C;0AL", "=>GLN", "8", "A>=", ":0:", ">B18;>", "."], "ner_tags": ["O", "O", "O", "O", "O", "O", "O", "B-Drugform", "O", "B-ADR", "O", "O", "B-ADR", "I-ADR", "I-ADR", "O"]}
```

### Data Fields

- idx: example id
- tokens: list of words from example
- ner_tags: ner tags

### Citation Information

```
@misc{blinov2022rumedbench,
    title={RuMedBench: A Russian Medical Language Understanding Benchmark},
    author={Pavel Blinov and Arina Reshetnikova and Aleksandr Nesterov and Galina Zubkova and Vladimir Kokh},
    year={2022},
    eprint={2201.06499},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```