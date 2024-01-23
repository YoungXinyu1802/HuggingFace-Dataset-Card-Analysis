---
annotations_creators:
- crowdsourced
language_creators:
- crowdsourced
language:
- en
multilinguality:
- monolingual
license:
- cc-by-4.0
pretty_name: CORD
size_categories:
- 1K<n<10K
source_datasets:
- original
task_categories:
- token-classification
task_ids:
- parsing
---

# Dataset Card for CORD (Consolidated Receipt Dataset)

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Additional Information](#additional-information)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Repository: https://github.com/clovaai/cord**
- **Paper: https://openreview.net/pdf?id=SJl3z659UH**
- **Leaderboard: https://paperswithcode.com/dataset/cord**

### Dataset Summary

[More Information Needed]

### Supported Tasks and Leaderboards

[More Information Needed]

## Dataset Structure

### Data Instances

[More Information Needed]

### Data Fields

```python
{
  "id": datasets.Value("string"),
  "words": datasets.Sequence(datasets.Value("string")),
  "bboxes": datasets.Sequence(datasets.Sequence(datasets.Value("int64"))),
  "labels": datasets.Sequence(datasets.features.ClassLabel(names=_LABELS)),
  "images": datasets.features.Image(),
}
```

### Data Splits

- train (800 rows)
- validation (100 rows)
- test (100 rows)

## Dataset Creation

### Licensing Information

[Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/)

### Citation Information

```
@article{park2019cord,
  title={CORD: A Consolidated Receipt Dataset for Post-OCR Parsing},
  author={Park, Seunghyun and Shin, Seung and Lee, Bado and Lee, Junyeop and Surh, Jaeheung and Seo, Minjoon and Lee, Hwalsuk}
  booktitle={Document Intelligence Workshop at Neural Information Processing Systems}
  year={2019}
}
```

### Contributions

Thanks to [@clovaai](https://github.com/clovaai) for adding this dataset.