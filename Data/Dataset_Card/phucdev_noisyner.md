---
annotations_creators:
- expert-generated
language:
- et
language_creators:
- found
license:
- cc-by-nc-4.0
multilinguality:
- monolingual
paperswithcode_id: noisyner
pretty_name: NoisyNER
size_categories:
- 10K<n<100K
source_datasets:
- original
tags:
- newspapers
- 1997-2009
task_categories:
- token-classification
task_ids:
- named-entity-recognition
dataset_info:
- config_name: estner_clean
  features:
  - name: id
    dtype: string
  - name: tokens
    sequence: string
  - name: lemmas
    sequence: string
  - name: grammar
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-ORG
          '4': I-ORG
          '5': B-LOC
          '6': I-LOC
  splits:
  - name: train
    num_bytes: 7544221
    num_examples: 11365
  - name: validation
    num_bytes: 986310
    num_examples: 1480
  - name: test
    num_bytes: 995204
    num_examples: 1433
  download_size: 6258130
  dataset_size: 9525735
- config_name: NoisyNER_labelset1
  features:
  - name: id
    dtype: string
  - name: tokens
    sequence: string
  - name: lemmas
    sequence: string
  - name: grammar
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-ORG
          '4': I-ORG
          '5': B-LOC
          '6': I-LOC
  splits:
  - name: train
    num_bytes: 7544221
    num_examples: 11365
  - name: validation
    num_bytes: 986310
    num_examples: 1480
  - name: test
    num_bytes: 995204
    num_examples: 1433
  download_size: 6194276
  dataset_size: 9525735
- config_name: NoisyNER_labelset2
  features:
  - name: id
    dtype: string
  - name: tokens
    sequence: string
  - name: lemmas
    sequence: string
  - name: grammar
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-ORG
          '4': I-ORG
          '5': B-LOC
          '6': I-LOC
  splits:
  - name: train
    num_bytes: 7544221
    num_examples: 11365
  - name: validation
    num_bytes: 986310
    num_examples: 1480
  - name: test
    num_bytes: 995204
    num_examples: 1433
  download_size: 6201072
  dataset_size: 9525735
- config_name: NoisyNER_labelset3
  features:
  - name: id
    dtype: string
  - name: tokens
    sequence: string
  - name: lemmas
    sequence: string
  - name: grammar
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-ORG
          '4': I-ORG
          '5': B-LOC
          '6': I-LOC
  splits:
  - name: train
    num_bytes: 7544221
    num_examples: 11365
  - name: validation
    num_bytes: 986310
    num_examples: 1480
  - name: test
    num_bytes: 995204
    num_examples: 1433
  download_size: 6231384
  dataset_size: 9525735
- config_name: NoisyNER_labelset4
  features:
  - name: id
    dtype: string
  - name: tokens
    sequence: string
  - name: lemmas
    sequence: string
  - name: grammar
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-ORG
          '4': I-ORG
          '5': B-LOC
          '6': I-LOC
  splits:
  - name: train
    num_bytes: 7544221
    num_examples: 11365
  - name: validation
    num_bytes: 986310
    num_examples: 1480
  - name: test
    num_bytes: 995204
    num_examples: 1433
  download_size: 6201072
  dataset_size: 9525735
- config_name: NoisyNER_labelset5
  features:
  - name: id
    dtype: string
  - name: tokens
    sequence: string
  - name: lemmas
    sequence: string
  - name: grammar
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-ORG
          '4': I-ORG
          '5': B-LOC
          '6': I-LOC
  splits:
  - name: train
    num_bytes: 7544221
    num_examples: 11365
  - name: validation
    num_bytes: 986310
    num_examples: 1480
  - name: test
    num_bytes: 995204
    num_examples: 1433
  download_size: 6231384
  dataset_size: 9525735
- config_name: NoisyNER_labelset6
  features:
  - name: id
    dtype: string
  - name: tokens
    sequence: string
  - name: lemmas
    sequence: string
  - name: grammar
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-ORG
          '4': I-ORG
          '5': B-LOC
          '6': I-LOC
  splits:
  - name: train
    num_bytes: 7544221
    num_examples: 11365
  - name: validation
    num_bytes: 986310
    num_examples: 1480
  - name: test
    num_bytes: 995204
    num_examples: 1433
  download_size: 6226516
  dataset_size: 9525735
- config_name: NoisyNER_labelset7
  features:
  - name: id
    dtype: string
  - name: tokens
    sequence: string
  - name: lemmas
    sequence: string
  - name: grammar
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-ORG
          '4': I-ORG
          '5': B-LOC
          '6': I-LOC
  splits:
  - name: train
    num_bytes: 7544221
    num_examples: 11365
  - name: validation
    num_bytes: 986310
    num_examples: 1480
  - name: test
    num_bytes: 995204
    num_examples: 1433
  download_size: 6229668
  dataset_size: 9525735
---

# Dataset Card for NoisyNER

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

- **Repository:** [Estonian NER corpus](https://doi.org/10.15155/1-00-0000-0000-0000-00073L), [NoisyNER dataset](https://github.com/uds-lsv/NoisyNER)
- **Paper:** [Named Entity Recognition in Estonian](https://aclanthology.org/W13-2412/), [Analysing the Noise Model Error for Realistic Noisy Label Data](https://arxiv.org/abs/2101.09763)
- **Dataset:** NoisyNER
- **Domain:** News
- **Size of downloaded dataset files:** 6.23 MB 
- **Size of the generated dataset files:** 9.53 MB

### Dataset Summary

NoisyNER is a dataset for the evaluation of methods to handle noisy labels when training machine learning models. 

- Entity Types: `PER`, `ORG`, `LOC`
  
It is from the NLP/Information Extraction domain and was created through a realistic distant supervision technique. Some highlights and interesting aspects of the data are:

- Seven sets of labels with differing noise patterns to evaluate different noise levels on the same instances
- Full parallel clean labels available to compute upper performance bounds or study scenarios where a small amount of gold-standard data can be leveraged
- Skewed label distribution (typical for Named Entity Recognition tasks)
- For some label sets: noise level higher than the true label probability
- Sequential dependencies between the labels

For more details on the dataset and its creation process, please refer to the original author's publication https://ojs.aaai.org/index.php/AAAI/article/view/16938 (published at AAAI'21).

This dataset is based on the Estonian NER corpus. For more details see https://aclanthology.org/W13-2412/

### Supported Tasks and Leaderboards

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Languages

The language data in NoisyNER is in Estonian (BCP-47 et)

## Dataset Structure

### Data Instances

An example of 'train' looks as follows.
```
{
  'id': '0',
  'tokens': ['Tallinna', 'õhusaaste', 'suureneb', '.'],
  'lemmas': ['Tallinn+0', 'õhu_saaste+0', 'suurene+b', '.'],
  'grammar': ['_H_ sg g', '_S_ sg n', '_V_ b', '_Z_'],
  'ner_tags': [5, 0, 0, 0]
}
```

### Data Fields

The data fields are the same among all splits.

- `id`: a `string` feature.
- `tokens`: a `list` of `string` features.
- `lemmas`: a `list` of `string` features.
- `grammar`: a `list` of `string` features.
- `ner_tags`: a `list` of classification labels (`int`). Full tagset with indices:

```python
{'O': 0, 'B-PER': 1, 'I-PER': 2, 'B-ORG': 3, 'I-ORG': 4, 'B-LOC': 5, 'I-LOC': 6}
```

### Data Splits

The splits are the same across all configurations.

|train|validation|test|
|----:|---------:|---:|
|11365|      1480|1433|

## Dataset Creation

### Curation Rationale

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Source Data

#### Initial Data Collection and Normalization

Tkachenko et al (2013) collected 572 news stories published in the local online newspapers [Delfi](http://delfi.ee/) and [Postimees](http://postimees.ee/) between 1997 and 2009. Selected articles cover both local and international news on a range of topics including politics, economics and sports. The raw text was preprocessed using the morphological disambiguator t3mesta ([Kaalep and
Vaino, 1998](https://www.cl.ut.ee/yllitised/kk_yhest_1998.pdf)) provided by [Filosoft](http://www.filosoft.ee/). The processing steps involve tokenization, lemmatization, part-of-speech tagging, grammatical and morphological analysis. 

#### Who are the source language producers?

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Annotations

#### Annotation process

According to Tkachenko et al (2013) one of the authors manually tagged the corpus and the other author examined the tags, after which conflicting cases were resolved.
The total size of the corpus is 184,638 tokens. Tkachenko et al (2013) provide the following number of named entities in the corpus:

|        | PER  | LOC  | ORG  | Total |
|--------|------|------|------|-------|
|    All | 5762 | 5711 | 3938 | 15411 |
| Unique | 3588 | 1589 | 1987 | 7164  |

Hedderich et al (2021) obtained the noisy labels through a distant supervision/automatic annotation approach. They extracted lists of named entities from Wikidata and matched them against words in the text via the ANEA tool ([Hedderich, Lange, and Klakow 2021](https://arxiv.org/abs/2102.13129)). They also used heuristic functions to correct errors caused by non-complete lists of entities,
grammatical complexities of Estonian that do not allow simple string matching or entity lists in conflict with each other. For instance, they normalized the grammatical form of a word or excluded certain high false-positive words. They provide seven sets of labels that differ in the noise process. This results in 8 different configurations, when added to the original split with clean labels.

#### Who are the annotators?

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Personal and Sensitive Information

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Discussion of Biases

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Other Known Limitations

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

## Additional Information

### Dataset Curators

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Licensing Information

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)


### Citation Information

```
@inproceedings{tkachenko-etal-2013-named,
    title = "Named Entity Recognition in {E}stonian",
    author = "Tkachenko, Alexander  and
      Petmanson, Timo  and
      Laur, Sven",
    booktitle = "Proceedings of the 4th Biennial International Workshop on {B}alto-{S}lavic Natural Language Processing",
    month = aug,
    year = "2013",
    address = "Sofia, Bulgaria",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/W13-2412",
    pages = "78--83",
}
@article{Hedderich_Zhu_Klakow_2021, 
    title={Analysing the Noise Model Error for Realistic Noisy Label Data}, 
    author={Hedderich, Michael A. and Zhu, Dawei and Klakow, Dietrich},  
    volume={35}, 
    url={https://ojs.aaai.org/index.php/AAAI/article/view/16938}, 
    number={9}, 
    journal={Proceedings of the AAAI Conference on Artificial Intelligence},
    year={2021}, 
    month={May}, 
    pages={7675-7684}, 
}
```

### Contributions

Thanks to [@phucdev](https://github.com/phucdev) for adding this dataset.