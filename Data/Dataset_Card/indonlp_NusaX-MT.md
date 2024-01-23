---
pretty_name: NusaX-MT
annotations_creators:
- expert-generated
language_creators:
- expert-generated
license:
- cc-by-sa-4.0
multilinguality:
- multilingual
language:
 - ace
 - ban
 - bjn
 - bug
 - en
 - id
 - jv
 - mad
 - min
 - nij
 - su
 - bbc
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- translation
dataset_info:
  features:
  - name: id
    dtype: string
  - name: text_1
    dtype: string
  - name: text_2
    dtype: string
  - name: text_1_lang
    dtype: string
  - name: text_2_lang
    dtype: string
---

# Dataset Card for NusaX-MT

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
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
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Repository:** [GitHub](https://github.com/IndoNLP/nusax/tree/main/datasets/mt)
- **Paper:** [EACL 2022](https://arxiv.org/abs/2205.15960)
- **Point of Contact:** [GitHub](https://github.com/IndoNLP/nusax/tree/main/datasets/mt)

### Dataset Summary

NusaX is a high-quality multilingual parallel corpus that covers 12 languages, Indonesian, English, and 10 Indonesian local languages, namely Acehnese, Balinese, Banjarese, Buginese, Madurese, Minangkabau, Javanese, Ngaju, Sundanese, and Toba Batak.
NusaX-MT is a parallel corpus for training and benchmarking machine translation models across 10 Indonesian local languages + Indonesian and English. The data is presented in csv format with 12 columns, one column for each language.


### Supported Tasks and Leaderboards

- Machine translation for Indonesian languages

### Languages

All possible pairs of the following:

- ace: acehnese,
- ban: balinese,
- bjn: banjarese,
- bug: buginese,
- eng: english,
- ind: indonesian,
- jav: javanese,
- mad: madurese,
- min: minangkabau,
- nij: ngaju,
- sun: sundanese,
- bbc: toba_batak,

## Dataset Creation

### Curation Rationale

There is a shortage of NLP research and resources for the Indonesian languages, despite the country having over 700 languages. With this in mind, we have created this dataset to support future research for the underrepresented languages in Indonesia.

### Source Data

#### Initial Data Collection and Normalization

NusaX-MT is a dataset for machine translation in Indonesian langauges that has been expertly translated by native speakers.

#### Who are the source language producers?

The data was produced by humans (native speakers).

### Annotations

#### Annotation process

NusaX-MT is derived from SmSA, which is the biggest publicly available dataset for Indonesian sentiment analysis. It comprises of comments and reviews from multiple online platforms. To ensure the quality of our dataset, we have filtered it by removing any abusive language and personally identifying information by manually reviewing all sentences. To ensure balance in the label distribution, we randomly picked 1,000 samples through stratified sampling and then translated them to the corresponding languages.

#### Who are the annotators?

Native speakers of both Indonesian and the corresponding languages.
Annotators were compensated based on the number of translated samples.

### Personal and Sensitive Information

Personal information is removed.

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Discussion of Biases

NusaX is created from review text. These data sources may contain some bias.

### Other Known Limitations

No other known limitations

## Additional Information

### Licensing Information

CC-BY-SA 4.0.

Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.

ShareAlike — If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.

No additional restrictions — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

Please contact authors for any information on the dataset.

### Citation Information

```
@misc{winata2022nusax,
      title={NusaX: Multilingual Parallel Sentiment Dataset for 10 Indonesian Local Languages},
      author={Winata, Genta Indra and Aji, Alham Fikri and Cahyawijaya,
      Samuel and Mahendra, Rahmad and Koto, Fajri and Romadhony,
      Ade and Kurniawan, Kemal and Moeljadi, David and Prasojo,
      Radityo Eko and Fung, Pascale and Baldwin, Timothy and Lau,
      Jey Han and Sennrich, Rico and Ruder, Sebastian},
      year={2022},
      eprint={2205.15960},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

### Contributions

Thanks to [@afaji](https://github.com/afaji) for adding this dataset.
