---
annotations_creators:
- other
language:
- en
language_creators:
- found
license:
- other
multilinguality:
- monolingual
pretty_name: KBP37 is an English Relation Classification dataset
size_categories:
- 10K<n<100K
source_datasets:
- extended|other
tags:
- relation extraction
task_categories:
- text-classification
task_ids:
- multi-class-classification
dataset_info:
- config_name: kbp37
  features:
  - name: id
    dtype: string
  - name: sentence
    dtype: string
  - name: relation
    dtype:
      class_label:
        names:
          '0': no_relation
          '1': org:alternate_names(e1,e2)
          '2': org:alternate_names(e2,e1)
          '3': org:city_of_headquarters(e1,e2)
          '4': org:city_of_headquarters(e2,e1)
          '5': org:country_of_headquarters(e1,e2)
          '6': org:country_of_headquarters(e2,e1)
          '7': org:founded(e1,e2)
          '8': org:founded(e2,e1)
          '9': org:founded_by(e1,e2)
          '10': org:founded_by(e2,e1)
          '11': org:members(e1,e2)
          '12': org:members(e2,e1)
          '13': org:stateorprovince_of_headquarters(e1,e2)
          '14': org:stateorprovince_of_headquarters(e2,e1)
          '15': org:subsidiaries(e1,e2)
          '16': org:subsidiaries(e2,e1)
          '17': org:top_members/employees(e1,e2)
          '18': org:top_members/employees(e2,e1)
          '19': per:alternate_names(e1,e2)
          '20': per:alternate_names(e2,e1)
          '21': per:cities_of_residence(e1,e2)
          '22': per:cities_of_residence(e2,e1)
          '23': per:countries_of_residence(e1,e2)
          '24': per:countries_of_residence(e2,e1)
          '25': per:country_of_birth(e1,e2)
          '26': per:country_of_birth(e2,e1)
          '27': per:employee_of(e1,e2)
          '28': per:employee_of(e2,e1)
          '29': per:origin(e1,e2)
          '30': per:origin(e2,e1)
          '31': per:spouse(e1,e2)
          '32': per:spouse(e2,e1)
          '33': per:stateorprovinces_of_residence(e1,e2)
          '34': per:stateorprovinces_of_residence(e2,e1)
          '35': per:title(e1,e2)
          '36': per:title(e2,e1)
  splits:
  - name: train
    num_bytes: 3570626
    num_examples: 15917
  - name: validation
    num_bytes: 388935
    num_examples: 1724
  - name: test
    num_bytes: 762806
    num_examples: 3405
  download_size: 5106673
  dataset_size: 4722367
- config_name: kbp37_formatted
  features:
  - name: id
    dtype: string
  - name: token
    sequence: string
  - name: subj_start
    dtype: int32
  - name: subj_end
    dtype: int32
  - name: obj_start
    dtype: int32
  - name: obj_end
    dtype: int32
  - name: relation
    dtype:
      class_label:
        names:
          '0': no_relation
          '1': org:alternate_names(e1,e2)
          '2': org:alternate_names(e2,e1)
          '3': org:city_of_headquarters(e1,e2)
          '4': org:city_of_headquarters(e2,e1)
          '5': org:country_of_headquarters(e1,e2)
          '6': org:country_of_headquarters(e2,e1)
          '7': org:founded(e1,e2)
          '8': org:founded(e2,e1)
          '9': org:founded_by(e1,e2)
          '10': org:founded_by(e2,e1)
          '11': org:members(e1,e2)
          '12': org:members(e2,e1)
          '13': org:stateorprovince_of_headquarters(e1,e2)
          '14': org:stateorprovince_of_headquarters(e2,e1)
          '15': org:subsidiaries(e1,e2)
          '16': org:subsidiaries(e2,e1)
          '17': org:top_members/employees(e1,e2)
          '18': org:top_members/employees(e2,e1)
          '19': per:alternate_names(e1,e2)
          '20': per:alternate_names(e2,e1)
          '21': per:cities_of_residence(e1,e2)
          '22': per:cities_of_residence(e2,e1)
          '23': per:countries_of_residence(e1,e2)
          '24': per:countries_of_residence(e2,e1)
          '25': per:country_of_birth(e1,e2)
          '26': per:country_of_birth(e2,e1)
          '27': per:employee_of(e1,e2)
          '28': per:employee_of(e2,e1)
          '29': per:origin(e1,e2)
          '30': per:origin(e2,e1)
          '31': per:spouse(e1,e2)
          '32': per:spouse(e2,e1)
          '33': per:stateorprovinces_of_residence(e1,e2)
          '34': per:stateorprovinces_of_residence(e2,e1)
          '35': per:title(e1,e2)
          '36': per:title(e2,e1)
  splits:
  - name: train
    num_bytes: 4975792
    num_examples: 15917
  - name: validation
    num_bytes: 542576
    num_examples: 1724
  - name: test
    num_bytes: 1062977
    num_examples: 3405
  download_size: 5106673
  dataset_size: 6581345
---
# Dataset Card for "kbp37"
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
- **Homepage:** [More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
- **Repository:** [kbp37](https://github.com/zhangdongxu/kbp37)
- **Paper:** [Relation Classification via Recurrent Neural Network](https://arxiv.org/abs/1508.01006)
- **Point of Contact:** [More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
- **Size of downloaded dataset files:** 5.11 MB
- **Size of the generated dataset:** 6.58 MB

### Dataset Summary
KBP37 is a revision of MIML-RE annotation dataset, provided by Gabor Angeli et al. (2014). They use both the 2010 and 
2013 KBP official document collections, as well as a July 2013 dump of Wikipedia as the text corpus for annotation. 
There are 33811 sentences been annotated. Zhang and Wang made several refinements:
1. They add direction to the relation names, e.g. '`per:employee_of`' is split into  '`per:employee of(e1,e2)`'
and '`per:employee of(e2,e1)`'. They also replace '`org:parents`' with '`org:subsidiaries`' and replace
'`org:member of’ with '`org:member`' (by their reverse directions).
2. They discard low frequency relations such that both directions of each relation occur more than 100 times in the 
dataset.

KBP37 contains 18 directional relations and an additional '`no_relation`' relation, resulting in 37 relation classes.

Note: 
- There is a formatted version that you can load with `datasets.load_dataset('kbp37', name='kbp37_formatted')`. This version is tokenized with spaCy and
  provides entity offsets. It discards some examples, however, that are invalid in the original dataset and lead to entity offset errors, e.g. train/1276.
  - train: 15807, validation: 1714, test: 3379


### Supported Tasks and Leaderboards

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Languages

The language data in KBP37 is in English (BCP-47 en)

## Dataset Structure

### Data Instances

#### kbp37
- **Size of downloaded dataset files:** 5.11 MB
- **Size of the generated dataset:** 4.7 MB
An example of 'train' looks as follows:
```json
{
  "id": "0",
  "sentence": "<e1> Thom Yorke </e1> of <e2> Radiohead </e2> has included the + for many of his signature distortion sounds using a variety of guitars to achieve various tonal options .",
  "relation": 27
}
```

#### kbp37_formatted
- **Size of downloaded dataset files:** 5.11 MB
- **Size of the generated dataset:** 6.58 MB
An example of 'train' looks as follows:
```json
{
  "id": "1",
  "token": ["Leland", "High", "School", "is", "a", "public", "high", "school", "located", "in", "the", "Almaden", "Valley", "in", "San", "Jose", "California", "USA", "in", "the", "San", "Jose", "Unified", "School", "District", "."],
  "subj_start": 0,
  "subj_end": 3,
  "obj_start": 14,
  "obj_end": 16,
  "relation": 3
}
```

### Data Fields

#### kbp37
- `id`: the instance id of this sentence, a `string` feature.
- `sentence`: the sentence, a `string` features.
- `relation`: the relation label of this instance, an `int` classification label.

```python
{"no_relation": 0, "org:alternate_names(e1,e2)": 1, "org:alternate_names(e2,e1)": 2, "org:city_of_headquarters(e1,e2)": 3, "org:city_of_headquarters(e2,e1)": 4, "org:country_of_headquarters(e1,e2)": 5, "org:country_of_headquarters(e2,e1)": 6, "org:founded(e1,e2)": 7, "org:founded(e2,e1)": 8, "org:founded_by(e1,e2)": 9, "org:founded_by(e2,e1)": 10, "org:members(e1,e2)": 11, "org:members(e2,e1)": 12, "org:stateorprovince_of_headquarters(e1,e2)": 13, "org:stateorprovince_of_headquarters(e2,e1)": 14, "org:subsidiaries(e1,e2)": 15, "org:subsidiaries(e2,e1)": 16, "org:top_members/employees(e1,e2)": 17, "org:top_members/employees(e2,e1)": 18, "per:alternate_names(e1,e2)": 19, "per:alternate_names(e2,e1)": 20, "per:cities_of_residence(e1,e2)": 21, "per:cities_of_residence(e2,e1)": 22, "per:countries_of_residence(e1,e2)": 23, "per:countries_of_residence(e2,e1)": 24, "per:country_of_birth(e1,e2)": 25, "per:country_of_birth(e2,e1)": 26, "per:employee_of(e1,e2)": 27, "per:employee_of(e2,e1)": 28, "per:origin(e1,e2)": 29, "per:origin(e2,e1)": 30, "per:spouse(e1,e2)": 31, "per:spouse(e2,e1)": 32, "per:stateorprovinces_of_residence(e1,e2)": 33, "per:stateorprovinces_of_residence(e2,e1)": 34, "per:title(e1,e2)": 35, "per:title(e2,e1)": 36}
```

#### kbp37_formatted
- `id`: the instance id of this sentence, a `string` feature.
- `token`: the list of tokens of this sentence, obtained with spaCy, a `list` of `string` features.
- `subj_start`: the 0-based index of the start token of the relation subject mention, an `int` feature.
- `subj_end`: the 0-based index of the end token of the relation subject mention, exclusive, an `int` feature.
- `obj_start`: the 0-based index of the start token of the relation object mention, an `int` feature.
- `obj_end`: the 0-based index of the end token of the relation object mention, exclusive, an `int` feature.
- `relation`: the relation label of this instance, an `int` classification label (same as `'kbp37''`).

### Data Splits

|       | Train | Dev  | Test |
|-------|-------|------|------|
| KBP37 | 15917 | 1724 | 3405 |

## Dataset Creation

### Curation Rationale

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

#### Who are the source language producers?

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Annotations

#### Annotation process

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

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
@article{DBLP:journals/corr/ZhangW15a,
  author    = {Dongxu Zhang and
               Dong Wang},
  title     = {Relation Classification via Recurrent Neural Network},
  journal   = {CoRR},
  volume    = {abs/1508.01006},
  year      = {2015},
  url       = {http://arxiv.org/abs/1508.01006},
  eprinttype = {arXiv},
  eprint    = {1508.01006},
  timestamp = {Fri, 04 Nov 2022 18:37:50 +0100},
  biburl    = {https://dblp.org/rec/journals/corr/ZhangW15a.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```

### Contributions

Thanks to [@phucdev](https://github.com/phucdev) for adding this dataset.