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
pretty_name: Google-IISc Distant Supervision (GIDS) dataset for distantly-supervised
  relation extraction
size_categories:
- 10K<n<100k
source_datasets:
- extended|other
tags:
- relation extraction
task_categories:
- text-classification
task_ids:
- multi-class-classification
dataset_info:
- config_name: gids
  features:
  - name: sentence
    dtype: string
  - name: subj_id
    dtype: string
  - name: obj_id
    dtype: string
  - name: subj_text
    dtype: string
  - name: obj_text
    dtype: string
  - name: relation
    dtype:
      class_label:
        names:
          '0': NA
          '1': /people/person/education./education/education/institution
          '2': /people/person/education./education/education/degree
          '3': /people/person/place_of_birth
          '4': /people/deceased_person/place_of_death
  splits:
  - name: train
    num_bytes: 5088421
    num_examples: 11297
  - name: validation
    num_bytes: 844784
    num_examples: 1864
  - name: test
    num_bytes: 2568673
    num_examples: 5663
  download_size: 8941490
  dataset_size: 8501878
- config_name: gids_formatted
  features:
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
          '0': NA
          '1': /people/person/education./education/education/institution
          '2': /people/person/education./education/education/degree
          '3': /people/person/place_of_birth
          '4': /people/deceased_person/place_of_death
  splits:
  - name: train
    num_bytes: 7075362
    num_examples: 11297
  - name: validation
    num_bytes: 1173957
    num_examples: 1864
  - name: test
    num_bytes: 3573706
    num_examples: 5663
  download_size: 8941490
  dataset_size: 11823025
---
# Dataset Card for "gids"
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
- **Repository:** [RE-DS-Word-Attention-Models](https://github.com/SharmisthaJat/RE-DS-Word-Attention-Models/tree/master/Data/GIDS)
- **Paper:** [Improving Distantly Supervised Relation Extraction using Word and Entity Based Attention](https://arxiv.org/abs/1804.06987)
- **Size of downloaded dataset files:** 8.94 MB
- **Size of the generated dataset:** 11.82 MB

### Dataset Summary
The Google-IISc Distant Supervision (GIDS) is a new dataset for distantly-supervised relation extraction.
GIDS is seeded from the human-judged Google relation extraction corpus. 
See the paper for full details: [Improving Distantly Supervised Relation Extraction using Word and Entity Based Attention](https://arxiv.org/abs/1804.06987)

Note: 
- There is a formatted version that you can load with `datasets.load_dataset('gids', name='gids_formatted')`. This version is tokenized with spaCy, removes the underscores in the entities and provides entity offsets.

### Supported Tasks and Leaderboards
- **Tasks:** Relation Classification
- **Leaderboards:** [More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
### Languages
The language in the dataset is English.
## Dataset Structure
### Data Instances

#### gids
- **Size of downloaded dataset files:** 8.94 MB
- **Size of the generated dataset:** 8.5 MB
An example of 'train' looks as follows:
```json
{
  "sentence": "War as appropriate. Private Alfred James_Smurthwaite Sample. 26614. 2nd Battalion Yorkshire Regiment. Son of Edward James Sample, of North_Ormesby , Yorks. Died 2 April 1917. Aged 29. Born Ormesby, Enlisted Middlesbrough. Buried BUCQUOY ROAD CEMETERY, FICHEUX. Not listed on the Middlesbrough War Memorial Private Frederick Scott. 46449. 4th Battalion Yorkshire Regiment. Son of William and Maria Scott, of 25, Aspinall St., Heywood, Lancs. Born at West Hartlepool. Died 27 May 1918. Aged 24.", 
  "subj_id": "/m/02qt0sv", 
  "obj_id": "/m/0fnhl9", 
  "subj_text": "James_Smurthwaite", 
  "obj_text": "North_Ormesby", 
  "relation": 4
}
```

#### gids_formatted
- **Size of downloaded dataset files:** 8.94 MB
- **Size of the generated dataset:** 11.82 MB
An example of 'train' looks as follows:
```json
{
  "token": ["announced", "he", "had", "closed", "shop", ".", "Mary", "D.", "Crisp", "Coyle", "opened", "in", "1951", ".", "Stoffey", ",", "a", "Maricopa", "County", "/", "Phoenix", "city", "resident", "and", "longtime", "customer", ",", "bought", "the", "business", "in", "2011", ",", "when", "then", "owners", "were", "facing", "closure", ".", "He", "renovated", "the", "diner", "is", "interior", ",", "increased", "training", "for", "staff", "and", "expanded", "the", "menu", "."], 
  "subj_start": 6, 
  "subj_end": 9, 
  "obj_start": 17, 
  "obj_end": 22, 
  "relation": 4
}
```

### Data Fields
The data fields are the same among all splits.

#### gids
- `sentence`: the sentence, a `string` feature.
- `subj_id`: the id of the relation subject mention, a `string` feature.
- `obj_id`: the id of the relation object mention, a `string` feature.
- `subj_text`: the text of the relation subject mention, a `string` feature.
- `obj_text`: the text of the relation object mention, a `string` feature.
- `relation`: the relation label of this instance, an `int` classification label.

```python
{"NA": 0, "/people/person/education./education/education/institution": 1, "/people/person/education./education/education/degree": 2, "/people/person/place_of_birth": 3, "/people/deceased_person/place_of_death": 4}
```
#### gids_formatted
- `token`: the list of tokens of this sentence, obtained with spaCy, a `list` of `string` features.
- `subj_start`: the 0-based index of the start token of the relation subject mention, an `ìnt` feature.
- `subj_end`: the 0-based index of the end token of the relation subject mention, exclusive, an `ìnt` feature.
- `obj_start`: the 0-based index of the start token of the relation object mention, an `ìnt` feature.
- `obj_end`: the 0-based index of the end token of the relation object mention, exclusive, an `ìnt` feature.
- `relation`: the relation label of this instance, an `int` classification label.

```python
{"NA": 0, "/people/person/education./education/education/institution": 1, "/people/person/education./education/education/degree": 2, "/people/person/place_of_birth": 3, "/people/deceased_person/place_of_death": 4}
```
### Data Splits

|      | Train | Dev  | Test |
|------|-------|------|------|
| GIDS | 11297 | 1864 | 5663 |

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
@article{DBLP:journals/corr/abs-1804-06987,
  author    = {Sharmistha Jat and
               Siddhesh Khandelwal and
               Partha P. Talukdar},
  title     = {Improving Distantly Supervised Relation Extraction using Word and
               Entity Based Attention},
  journal   = {CoRR},
  volume    = {abs/1804.06987},
  year      = {2018},
  url       = {http://arxiv.org/abs/1804.06987},
  eprinttype = {arXiv},
  eprint    = {1804.06987},
  timestamp = {Fri, 15 Nov 2019 17:16:02 +0100},
  biburl    = {https://dblp.org/rec/journals/corr/abs-1804-06987.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```

### Contributions
Thanks to [@phucdev](https://github.com/phucdev) for adding this dataset.