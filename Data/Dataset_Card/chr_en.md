---
annotations_creators:
- expert-generated
- found
- no-annotation
language_creators:
- found
language:
- chr
- en
license:
- other
multilinguality:
- monolingual
- multilingual
- translation
size_categories:
- 100K<n<1M
- 10K<n<100K
- 1K<n<10K
source_datasets:
- original
task_categories:
- fill-mask
- text-generation
- translation
task_ids:
- language-modeling
- masked-language-modeling
paperswithcode_id: chren
configs:
- monolingual
- monolingual_raw
- parallel
- parallel_raw
dataset_info:
- config_name: monolingual_raw
  features:
  - name: text_sentence
    dtype: string
  - name: text_title
    dtype: string
  - name: speaker
    dtype: string
  - name: date
    dtype: int32
  - name: type
    dtype: string
  - name: dialect
    dtype: string
  splits:
  - name: full
    num_bytes: 1210828
    num_examples: 5210
  download_size: 28899321
  dataset_size: 1210828
- config_name: parallel_raw
  features:
  - name: line_number
    dtype: string
  - name: sentence_pair
    dtype:
      translation:
        languages:
        - en
        - chr
  - name: text_title
    dtype: string
  - name: speaker
    dtype: string
  - name: date
    dtype: int32
  - name: type
    dtype: string
  - name: dialect
    dtype: string
  splits:
  - name: full
    num_bytes: 5012923
    num_examples: 14151
  download_size: 28899321
  dataset_size: 5012923
- config_name: monolingual
  features:
  - name: sentence
    dtype: string
  splits:
  - name: chr
    num_bytes: 882848
    num_examples: 5210
  - name: en5000
    num_bytes: 615295
    num_examples: 5000
  - name: en10000
    num_bytes: 1211645
    num_examples: 10000
  - name: en20000
    num_bytes: 2432378
    num_examples: 20000
  - name: en50000
    num_bytes: 6065780
    num_examples: 49999
  - name: en100000
    num_bytes: 12130564
    num_examples: 100000
  download_size: 28899321
  dataset_size: 23338510
- config_name: parallel
  features:
  - name: sentence_pair
    dtype:
      translation:
        languages:
        - en
        - chr
  splits:
  - name: train
    num_bytes: 3089658
    num_examples: 11639
  - name: dev
    num_bytes: 260409
    num_examples: 1000
  - name: out_dev
    num_bytes: 78134
    num_examples: 256
  - name: test
    num_bytes: 264603
    num_examples: 1000
  - name: out_test
    num_bytes: 80967
    num_examples: 256
  download_size: 28899321
  dataset_size: 3773771
---

# Dataset Card for ChrEn

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
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Repository:** [Github repository for ChrEn](https://github.com/ZhangShiyue/ChrEn)
- **Paper:** [ChrEn: Cherokee-English Machine Translation for Endangered Language Revitalization](https://arxiv.org/abs/2010.04791)
- **Point of Contact:** [benfrey@email.unc.edu](benfrey@email.unc.edu)

### Dataset Summary

ChrEn is a Cherokee-English parallel dataset to facilitate machine translation research between Cherokee and English.
ChrEn is extremely low-resource contains 14k sentence pairs in total, split in ways that facilitate both in-domain and out-of-domain evaluation.
ChrEn also contains 5k Cherokee monolingual data to enable semi-supervised learning.

### Supported Tasks and Leaderboards

The dataset is intended to use for `machine-translation` between Enlish (`en`) and Cherokee (`chr`).

### Languages

The dataset contains Enlish (`en`) and Cherokee (`chr`) text. The data encompasses both existing dialects of Cherokee: the Overhill dialect, mostly spoken in Oklahoma (OK), and the Middle dialect, mostly used in North Carolina (NC).

## Dataset Structure

### Data Instances

[More Information Needed]

### Data Fields

[More Information Needed]

### Data Splits

[More Information Needed]

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

Many of the source texts were translations of English materials, which means that the Cherokee structures may not be 100% natural in terms of what a speaker might spontaneously produce. Each text was translated by people who speak Cherokee as the first language, which means there is a high probability of grammaticality. These data were originally available in PDF version. We apply the Optical Character Recognition (OCR) via Tesseract OCR engine to extract the Cherokee and English text.

#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

The sentences were manually aligned by Dr. Benjamin Frey a proficient second-language speaker of Cherokee, who also fixed the errors introduced by OCR. This process is time-consuming and took several months.

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

The dataset was gathered and annotated by Shiyue Zhang, Benjamin Frey, and Mohit Bansal at UNC Chapel Hill.

### Licensing Information

The copyright of the data belongs to original book/article authors or translators (hence, used for research purpose; and please contact Dr. Benjamin Frey for other copyright questions).

### Citation Information

```
@inproceedings{zhang2020chren,
  title={ChrEn: Cherokee-English Machine Translation for Endangered Language Revitalization},
  author={Zhang, Shiyue and Frey, Benjamin and Bansal, Mohit},
  booktitle={EMNLP2020},
  year={2020}
}
```

### Contributions

Thanks to [@yjernite](https://github.com/yjernite), [@lhoestq](https://github.com/lhoestq) for adding this dataset.