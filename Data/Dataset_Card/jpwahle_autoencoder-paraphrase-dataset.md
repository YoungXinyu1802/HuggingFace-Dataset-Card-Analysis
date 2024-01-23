---
annotations_creators:
- machine-generated
language:
- en
language_creators:
- machine-generated
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: Autoencoder Paraphrase Dataset (BERT, RoBERTa, Longformer)
size_categories:
- 100K<n<1M
source_datasets:
- original
tags:
- bert
- roberta
- longformer
- plagiarism
- paraphrase
- academic integrity
- arxiv
- wikipedia
- theses
task_categories:
- text-classification
- text-generation
task_ids: []
paperswithcode_id: are-neural-language-models-good-plagiarists-a
dataset_info:
- split: train
  download_size: 2980464
  dataset_size: 2980464
- split: test
  download_size: 1690032
  dataset_size: 1690032
---

# Dataset Card for Machine Paraphrase Dataset (MPC)

## Table of Contents
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
  - [Curation Rat1.ionale](#curation-rationale)
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

- **Paper:** https://ieeexplore.ieee.org/document/9651895
- **Total size:** 2.23 GB
- **Train size:** 1.52 GB
- **Test size:** 861 MB

### Dataset Summary

The Autoencoder Paraphrase Corpus (APC) consists of ~200k examples of original, and paraphrases using three neural language models.
It uses three models (BERT, RoBERTa, Longformer) on three source texts (Wikipedia, arXiv, student theses).
The examples are aligned, i.e., we sample the same paragraphs for originals and paraphrased versions.

### How to use it
You can load the dataset using the `load_dataset` function:

```python
from datasets import load_dataset

ds = load_dataset("jpwahle/autoencoder-paraphrase-dataset")
print(ds[0])

#OUTPUT:
{
 'text': 'War memorial formally unveiled on Whit Monday 16 May 1921 by the Prince of Wales  later King Edward VIII  with Lutyens in attendance At the unveiling ceremony Captain Fortescue gave a speech during wherein he announced that 11 600 men and women from Devon had been inval while serving in imperialist war He later stated that some 63 700  8 000 regulars 36 700 volunteers  19 000 conscripts had served in the armed forces The heroism of the dead are recorded on a roll of honour of which three copies were made  one for Exeter Cathedral one To be held by Tasman county council and another honoring the Prince of Wales placed in a hollow in bedrock base of the war memorial The princes visit generated considerable excitement in the area Thousands of spectators lined the street to greet his motorcade and shops on Market High Street hung out banners with welcoming messages After the unveiling Edward spent ten days touring the local area',
 'label': 1,
 'dataset': 'wikipedia',
 'method': 'longformer'
}
```

### Supported Tasks and Leaderboards

Paraphrase Identification

### Languages

English

## Dataset Structure

### Data Instances

```json
{
 'text': 'War memorial formally unveiled on Whit Monday 16 May 1921 by the Prince of Wales  later King Edward VIII  with Lutyens in attendance At the unveiling ceremony Captain Fortescue gave a speech during wherein he announced that 11 600 men and women from Devon had been inval while serving in imperialist war He later stated that some 63 700  8 000 regulars 36 700 volunteers  19 000 conscripts had served in the armed forces The heroism of the dead are recorded on a roll of honour of which three copies were made  one for Exeter Cathedral one To be held by Tasman county council and another honoring the Prince of Wales placed in a hollow in bedrock base of the war memorial The princes visit generated considerable excitement in the area Thousands of spectators lined the street to greet his motorcade and shops on Market High Street hung out banners with welcoming messages After the unveiling Edward spent ten days touring the local area',
 'label': 1,
 'dataset': 'wikipedia',
 'method': 'longformer'
}
```

### Data Fields

| Feature | Description |
| --- | --- |
| `text` | The unique identifier of the paper. |
| `label` | Whether it is a paraphrase (1) or the original (0). |
| `dataset` | The source dataset (Wikipedia, arXiv, or theses). |
| `method` | The method used (bert, roberta, longformer). |

### Data Splits

- train (Wikipedia x [bert, roberta, longformer])
- test ([Wikipedia, arXiv, theses] x [bert, roberta, longformer])

## Dataset Creation

### Curation Rationale

Providing a resource for testing against autoencoder paraprhased plagiarism.

### Source Data

#### Initial Data Collection and Normalization

- Paragraphs from `featured articles` from the English Wikipedia dump
- Paragraphs from full-text pdfs of arXMLiv
- Paragraphs from full-text pdfs of Czech student thesis (bachelor, master, PhD).

#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

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

[Jan Philip Wahle](https://jpwahle.com/)

### Licensing Information

The Autoencoder Paraphrase Dataset is released under CC BY-NC 4.0. By using this corpus, you agree to its usage terms.

### Citation Information

```bib
@inproceedings{9651895,
	title        = {Are Neural Language Models Good Plagiarists? A Benchmark for Neural Paraphrase Detection},
	author       = {Wahle, Jan Philip and Ruas, Terry and Meuschke, Norman and Gipp, Bela},
	year         = 2021,
	booktitle    = {2021 ACM/IEEE Joint Conference on Digital Libraries (JCDL)},
	volume       = {},
	number       = {},
	pages        = {226--229},
	doi          = {10.1109/JCDL52503.2021.00065}
}
```

### Contributions

Thanks to [@jpwahle](https://github.com/jpwahle) for adding this dataset.