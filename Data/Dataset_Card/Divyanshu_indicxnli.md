---
annotations_creators:
- machine-generated
language_creators:
- machine-generated
language:
- as
- bn
- gu
- hi
- kn
- ml
- mr
- or
- pa
- ta
- te
license:
- cc0-1.0
multilinguality:
- multilingual
pretty_name: IndicXNLI
size_categories:
- 1M<n<10M
source_datasets:
- original
task_categories:
- text-classification
task_ids:
- natural-language-inference
---

# Dataset Card for "IndicXNLI"

## Table of Contents

- [Dataset Card for "IndicXNLI"](#dataset-card-for-indicxnli)
  - [Table of Contents](#table-of-contents)
  - [Dataset Description](#dataset-description)
    - [Dataset Summary](#dataset-summary)
    - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
    - [Languages](#languages)
  - [Dataset Structure](#dataset-structure)
    - [Data Instances](#data-instances)
    - [Data Fields](#data-fields)
    - [Data Splits](#data-splits)

## Dataset Description

- **Homepage:** <https://github.com/divyanshuaggarwal/IndicXNLI>
- **Paper:** [IndicXNLI: Evaluating Multilingual Inference for Indian Languages](https://arxiv.org/abs/2204.08776)
- **Point of Contact:** [Divyanshu Aggarwal](mailto:divyanshuggrwl@gmail.com)

### Dataset Summary

INDICXNLI is similar to existing
XNLI dataset in shape/form, but focusses on Indic language family. INDICXNLI include NLI
data for eleven major Indic languages that includes
Assamese (‘as’), Gujarat (‘gu’), Kannada (‘kn’),
Malayalam (‘ml’), Marathi (‘mr’), Odia (‘or’),
Punjabi (‘pa’), Tamil (‘ta’), Telugu (‘te’), Hindi
(‘hi’), and Bengali (‘bn’).

### Supported Tasks and Leaderboards

**Tasks:** Natural Language Inference

**Leaderboards:** Currently there is no Leaderboard for this dataset.

### Languages

- `Assamese (as)`
- `Bengali (bn)`
- `Gujarati (gu)`
- `Kannada (kn)`
- `Hindi (hi)`
- `Malayalam (ml)`
- `Marathi (mr)`
- `Oriya (or)`
- `Punjabi (pa)`
- `Tamil (ta)`
- `Telugu (te)`

## Dataset Structure

### Data Instances

One example from the `hi` dataset is given below in JSON format.

  ```python
 {'premise': 'अवधारणात्मक रूप से क्रीम स्किमिंग के दो बुनियादी आयाम हैं-उत्पाद और भूगोल।',
 'hypothesis': 'उत्पाद और भूगोल क्रीम स्किमिंग का काम करते हैं।',
 'label': 1 (neutral) }
  ```

### Data Fields

- `premise (string)`: Premise Sentence
- `hypothesis (string)`: Hypothesis Sentence
- `label (integer)`: Integer label `0` if hypothesis `entails` the premise, `2` if hypothesis `negates` the premise and `1` otherwise.

### Data Splits

<!-- Below is the dataset split given for `hi` dataset.

```python
DatasetDict({
    train: Dataset({
        features: ['premise', 'hypothesis', 'label'],
        num_rows: 392702
    })
    test: Dataset({
        features: ['premise', 'hypothesis', 'label'],
        num_rows: 5010
    })
    validation: Dataset({
        features: ['premise', 'hypothesis', 'label'],
        num_rows: 2490
    })
})

``` -->

Language      | ISO 639-1 Code |Train | Test | Dev |
--------------|----------------|-------|-----|------|
Assamese | as | 392,702 | 5,010 | 2,490 |
Bengali | bn | 392,702 | 5,010 | 2,490 |
Gujarati | gu |  392,702 | 5,010 | 2,490 |
Hindi | hi | 392,702 | 5,010 | 2,490 |
Kannada | kn |  392,702 | 5,010 | 2,490 |
Malayalam | ml |392,702  | 5,010 | 2,490 |
Marathi | mr |392,702 | 5,010 | 2,490 |
Oriya | or | 392,702 | 5,010 | 2,490 |
Punjabi | pa | 392,702 | 5,010 | 2,490 |
Tamil | ta | 392,702 | 5,010 | 2,490 |
Telugu | te | 392,702 | 5,010 | 2,490 |

<!-- The dataset split remains same across all languages. -->

## Dataset usage

Code snippet for using the dataset using datasets library.

```python
from datasets import load_dataset

dataset = load_dataset("Divyanshu/indicxnli")
```

## Dataset Creation
Machine translation of XNLI english dataset to 11 listed Indic Languages.

### Curation Rationale

[More information needed]

### Source Data

[XNLI dataset](https://cims.nyu.edu/~sbowman/xnli/)

#### Initial Data Collection and Normalization

[Detailed in the paper](https://arxiv.org/abs/2204.08776)

#### Who are the source language producers?

[Detailed in the paper](https://arxiv.org/abs/2204.08776)

#### Human Verification Process

[Detailed in the paper](https://arxiv.org/abs/2204.08776)


## Considerations for Using the Data

### Social Impact of Dataset

[Detailed in the paper](https://arxiv.org/abs/2204.08776)

### Discussion of Biases

[Detailed in the paper](https://arxiv.org/abs/2204.08776)

### Other Known Limitations

[Detailed in the paper](https://arxiv.org/abs/2204.08776)

### Dataset Curators

Divyanshu Aggarwal, Vivek Gupta, Anoop Kunchukuttan

### Licensing Information

Contents of this repository are restricted to only non-commercial research purposes under the [Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/). Copyright of the dataset contents belongs to the original copyright holders.

### Citation Information

If you use any of the datasets, models or code modules, please cite the following paper:

```
@misc{https://doi.org/10.48550/arxiv.2204.08776,
  doi = {10.48550/ARXIV.2204.08776},
  
  url = {https://arxiv.org/abs/2204.08776},
  
  author = {Aggarwal, Divyanshu and Gupta, Vivek and Kunchukuttan, Anoop},
  
  keywords = {Computation and Language (cs.CL), Artificial Intelligence (cs.AI), FOS: Computer and information sciences, FOS: Computer and information sciences},
  
  title = {IndicXNLI: Evaluating Multilingual Inference for Indian Languages}, 
  
  publisher = {arXiv},
  
  year = {2022},
  
  copyright = {Creative Commons Attribution 4.0 International}
}
```

<!-- ### Contributions -->
