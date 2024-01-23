---
language:
- en
- it
license:
- unknown
multilinguality:
- monolingual
- translation
pretty_name: Europarl v7 (en-it split)
tags: []
task_categories:
- translation
task_ids: []
---

# Dataset Card for Europarl v7 (en-it split)

This dataset contains only the English-Italian split of Europarl v7.
We created the dataset to provide it to the [M2L 2022 Summer School](https://www.m2lschool.org/) students.

For all the information on the dataset, please refer to: [https://www.statmt.org/europarl/](https://www.statmt.org/europarl/)  

## Dataset Structure

### Data Fields

- sent_en: English transcript
- sent_it: Italian translation

### Data Splits

We created three custom training/validation/testing splits. Feel free to rearrange them if needed. These ARE NOT by any means official splits. 

- train (1717204 pairs)
- validation (190911 pairs)
- test (1000 pairs)

### Citation Information

If using the dataset, please cite:

`Koehn, P. (2005). Europarl: A parallel corpus for statistical machine translation. In Proceedings of machine translation summit x: papers (pp. 79-86).`

### Contributions

Thanks to [@g8a9](https://github.com/g8a9) for adding this dataset.
