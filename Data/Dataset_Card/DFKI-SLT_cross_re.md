---
annotations_creators:
- expert-generated
language:
- en
language_creators:
- found
license: []
multilinguality:
- monolingual
pretty_name: CrossRE is a cross-domain dataset for relation extraction
size_categories:
- 10K<n<100K
source_datasets: 
- extended|cross_ner
tags:
- cross domain
- ai
- news
- music
- literature
- politics
- science
task_categories:
- text-classification
task_ids:
- multi-class-classification
dataset_info:
- config_name: ai
  features:
  - name: doc_key
    dtype: string
  - name: sentence
    sequence: string
  - name: ner
    sequence:
    - name: id-start
      dtype: int32
    - name: id-end
      dtype: int32
    - name: entity-type
      dtype: string
  - name: relations
    sequence:
    - name: id_1-start
      dtype: int32
    - name: id_1-end
      dtype: int32
    - name: id_2-start
      dtype: int32
    - name: id_2-end
      dtype: int32
    - name: relation-type
      dtype: string
    - name: Exp
      dtype: string
    - name: Un
      dtype: bool
    - name: SA
      dtype: bool
  splits:
  - name: train
    num_bytes: 62411
    num_examples: 100
  - name: validation
    num_bytes: 183717
    num_examples: 350
  - name: test
    num_bytes: 217353
    num_examples: 431
  download_size: 508107
  dataset_size: 463481
- config_name: literature
  features:
  - name: doc_key
    dtype: string
  - name: sentence
    sequence: string
  - name: ner
    sequence:
    - name: id-start
      dtype: int32
    - name: id-end
      dtype: int32
    - name: entity-type
      dtype: string
  - name: relations
    sequence:
    - name: id_1-start
      dtype: int32
    - name: id_1-end
      dtype: int32
    - name: id_2-start
      dtype: int32
    - name: id_2-end
      dtype: int32
    - name: relation-type
      dtype: string
    - name: Exp
      dtype: string
    - name: Un
      dtype: bool
    - name: SA
      dtype: bool
  splits:
  - name: train
    num_bytes: 62699
    num_examples: 100
  - name: validation
    num_bytes: 246214
    num_examples: 400
  - name: test
    num_bytes: 264450
    num_examples: 416
  download_size: 635130
  dataset_size: 573363
- config_name: music
  features:
  - name: doc_key
    dtype: string
  - name: sentence
    sequence: string
  - name: ner
    sequence:
    - name: id-start
      dtype: int32
    - name: id-end
      dtype: int32
    - name: entity-type
      dtype: string
  - name: relations
    sequence:
    - name: id_1-start
      dtype: int32
    - name: id_1-end
      dtype: int32
    - name: id_2-start
      dtype: int32
    - name: id_2-end
      dtype: int32
    - name: relation-type
      dtype: string
    - name: Exp
      dtype: string
    - name: Un
      dtype: bool
    - name: SA
      dtype: bool
  splits:
  - name: train
    num_bytes: 69846
    num_examples: 100
  - name: validation
    num_bytes: 261497
    num_examples: 350
  - name: test
    num_bytes: 312165
    num_examples: 399
  download_size: 726956
  dataset_size: 643508
- config_name: news
  features:
  - name: doc_key
    dtype: string
  - name: sentence
    sequence: string
  - name: ner
    sequence:
    - name: id-start
      dtype: int32
    - name: id-end
      dtype: int32
    - name: entity-type
      dtype: string
  - name: relations
    sequence:
    - name: id_1-start
      dtype: int32
    - name: id_1-end
      dtype: int32
    - name: id_2-start
      dtype: int32
    - name: id_2-end
      dtype: int32
    - name: relation-type
      dtype: string
    - name: Exp
      dtype: string
    - name: Un
      dtype: bool
    - name: SA
      dtype: bool
  splits:
  - name: train
    num_bytes: 49102
    num_examples: 164
  - name: validation
    num_bytes: 77952
    num_examples: 350
  - name: test
    num_bytes: 96301
    num_examples: 400
  download_size: 239763
  dataset_size: 223355
- config_name: politics
  features:
  - name: doc_key
    dtype: string
  - name: sentence
    sequence: string
  - name: ner
    sequence:
    - name: id-start
      dtype: int32
    - name: id-end
      dtype: int32
    - name: entity-type
      dtype: string
  - name: relations
    sequence:
    - name: id_1-start
      dtype: int32
    - name: id_1-end
      dtype: int32
    - name: id_2-start
      dtype: int32
    - name: id_2-end
      dtype: int32
    - name: relation-type
      dtype: string
    - name: Exp
      dtype: string
    - name: Un
      dtype: bool
    - name: SA
      dtype: bool
  splits:
  - name: train
    num_bytes: 76004
    num_examples: 101
  - name: validation
    num_bytes: 277633
    num_examples: 350
  - name: test
    num_bytes: 295294
    num_examples: 400
  download_size: 726427
  dataset_size: 648931
- config_name: science
  features:
  - name: doc_key
    dtype: string
  - name: sentence
    sequence: string
  - name: ner
    sequence:
    - name: id-start
      dtype: int32
    - name: id-end
      dtype: int32
    - name: entity-type
      dtype: string
  - name: relations
    sequence:
    - name: id_1-start
      dtype: int32
    - name: id_1-end
      dtype: int32
    - name: id_2-start
      dtype: int32
    - name: id_2-end
      dtype: int32
    - name: relation-type
      dtype: string
    - name: Exp
      dtype: string
    - name: Un
      dtype: bool
    - name: SA
      dtype: bool
  splits:
  - name: train
    num_bytes: 63876
    num_examples: 103
  - name: validation
    num_bytes: 224402
    num_examples: 351
  - name: test
    num_bytes: 249075
    num_examples: 400
  download_size: 594058
  dataset_size: 537353
---
# Dataset Card for CrossRE
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
- **Repository:** [CrossRE](https://github.com/mainlp/CrossRE)
- **Paper:** [CrossRE: A Cross-Domain Dataset for Relation Extraction](https://arxiv.org/abs/2210.09345)

### Dataset Summary
CrossRE is a new, freely-available crossdomain benchmark for RE, which comprises six distinct text domains and includes 
multilabel annotations. It includes the following domains: news, politics, natural science, music, literature and 
artificial intelligence. The semantic relations are annotated on top of CrossNER (Liu et al., 2021), a cross-domain
dataset for NER which contains domain-specific entity types.
The dataset contains 17 relation labels for the six domains: PART-OF, PHYSICAL, USAGE, ROLE, SOCIAL, 
GENERAL-AFFILIATION, COMPARE, TEMPORAL, ARTIFACT, ORIGIN, TOPIC, OPPOSITE, CAUSE-EFFECT, WIN-DEFEAT, TYPEOF, NAMED, and 
RELATED-TO.

For details, see the paper: https://arxiv.org/abs/2210.09345

### Supported Tasks and Leaderboards

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Languages

The language data in CrossRE is in English (BCP-47 en)

## Dataset Structure

### Data Instances

#### news
- **Size of downloaded dataset files:** 0.24 MB
- **Size of the generated dataset:** 0.22 MB

An example of 'train' looks as follows:
```python
{
  "doc_key": "news-train-1", 
  "sentence": ["EU", "rejects", "German", "call", "to", "boycott", "British", "lamb", "."], 
  "ner": [
    {"id-start": 0, "id-end": 0, "entity-type": "organisation"}, 
    {"id-start": 2, "id-end": 3, "entity-type": "misc"}, 
    {"id-start": 6, "id-end": 7, "entity-type": "misc"}
  ], 
  "relations": [
    {"id_1-start": 0, "id_1-end": 0, "id_2-start": 2, "id_2-end": 3, "relation-type": "opposite", "Exp": "rejects", "Un": False, "SA": False}, 
    {"id_1-start": 2, "id_1-end": 3, "id_2-start": 6, "id_2-end": 7, "relation-type": "opposite", "Exp": "calls_for_boycot_of", "Un": False, "SA": False}, 
    {"id_1-start": 2, "id_1-end": 3, "id_2-start": 6, "id_2-end": 7, "relation-type": "topic", "Exp": "", "Un": False, "SA": False}
  ]
}
```

#### politics
- **Size of downloaded dataset files:** 0.73 MB
- **Size of the generated dataset:** 0.65 MB

An example of 'train' looks as follows:
```python
{
  "doc_key": "politics-train-1", 
  "sentence": ["Parties", "with", "mainly", "Eurosceptic", "views", "are", "the", "ruling", "United", "Russia", ",", "and", "opposition", "parties", "the", "Communist", "Party", "of", "the", "Russian", "Federation", "and", "Liberal", "Democratic", "Party", "of", "Russia", "."], 
  "ner": [
    {"id-start": 8, "id-end": 9, "entity-type": "politicalparty"}, 
    {"id-start": 15, "id-end": 20, "entity-type": "politicalparty"}, 
    {"id-start": 22, "id-end": 26, "entity-type": "politicalparty"}
  ], 
  "relations": [
    {"id_1-start": 8, "id_1-end": 9, "id_2-start": 15, "id_2-end": 20, "relation-type": "opposite", "Exp": "in_opposition", "Un": False, "SA": False}, 
    {"id_1-start": 8, "id_1-end": 9, "id_2-start": 22, "id_2-end": 26, "relation-type": "opposite", "Exp": "in_opposition", "Un": False, "SA": False}
  ]
}
```

#### science
- **Size of downloaded dataset files:** 0.59 MB
- **Size of the generated dataset:** 0.54 MB

An example of 'train' looks as follows:
```python
{
  "doc_key": "science-train-1", 
  "sentence": ["They", "may", "also", "use", "Adenosine", "triphosphate", ",", "Nitric", "oxide", ",", "and", "ROS", "for", "signaling", "in", "the", "same", "ways", "that", "animals", "do", "."], 
  "ner": [
    {"id-start": 4, "id-end": 5, "entity-type": "chemicalcompound"}, 
    {"id-start": 7, "id-end": 8, "entity-type": "chemicalcompound"}, 
    {"id-start": 11, "id-end": 11, "entity-type": "chemicalcompound"}
  ], 
  "relations": []
}
```

#### music
- **Size of downloaded dataset files:** 0.73 MB
- **Size of the generated dataset:** 0.64 MB

An example of 'train' looks as follows:
```python
{
  "doc_key": "music-train-1", 
  "sentence": ["In", "2003", ",", "the", "Stade", "de", "France", "was", "the", "primary", "site", "of", "the", "2003", "World", "Championships", "in", "Athletics", "."], 
  "ner": [
    {"id-start": 4, "id-end": 6, "entity-type": "location"}, 
    {"id-start": 13, "id-end": 17, "entity-type": "event"}
  ], 
  "relations": [
    {"id_1-start": 13, "id_1-end": 17, "id_2-start": 4, "id_2-end": 6, "relation-type": "physical", "Exp": "", "Un": False, "SA": False}
  ]
}
```

#### literature
- **Size of downloaded dataset files:** 0.64 MB
- **Size of the generated dataset:** 0.57 MB

An example of 'train' looks as follows:
```python
{
  "doc_key": "literature-train-1", 
  "sentence": ["In", "1351", ",", "during", "the", "reign", "of", "Emperor", "Toghon", "Temür", "of", "the", "Yuan", "dynasty", ",", "93rd-generation", "descendant", "Kong", "Huan", "(", "孔浣", ")", "'", "s", "2nd", "son", "Kong", "Shao", "(", "孔昭", ")", "moved", "from", "China", "to", "Korea", "during", "the", "Goryeo", ",", "and", "was", "received", "courteously", "by", "Princess", "Noguk", "(", "the", "Mongolian-born", "wife", "of", "the", "future", "king", "Gongmin", ")", "."], 
  "ner": [
    {"id-start": 7, "id-end": 9, "entity-type": "person"}, 
    {"id-start": 12, "id-end": 13, "entity-type": "country"}, 
    {"id-start": 17, "id-end": 18, "entity-type": "writer"}, 
    {"id-start": 20, "id-end": 20, "entity-type": "writer"}, 
    {"id-start": 26, "id-end": 27, "entity-type": "writer"}, 
    {"id-start": 29, "id-end": 29, "entity-type": "writer"}, 
    {"id-start": 33, "id-end": 33, "entity-type": "country"}, 
    {"id-start": 35, "id-end": 35, "entity-type": "country"}, 
    {"id-start": 38, "id-end": 38, "entity-type": "misc"}, 
    {"id-start": 45, "id-end": 46, "entity-type": "person"}, 
    {"id-start": 49, "id-end": 50, "entity-type": "misc"}, 
    {"id-start": 55, "id-end": 55, "entity-type": "person"}
  ], 
  "relations": [
    {"id_1-start": 7, "id_1-end": 9, "id_2-start": 12, "id_2-end": 13, "relation-type": "role", "Exp": "", "Un": False, "SA": False}, 
    {"id_1-start": 7, "id_1-end": 9, "id_2-start": 12, "id_2-end": 13, "relation-type": "temporal", "Exp": "", "Un": False, "SA": False}, 
    {"id_1-start": 17, "id_1-end": 18, "id_2-start": 26, "id_2-end": 27, "relation-type": "social", "Exp": "family", "Un": False, "SA": False}, 
    {"id_1-start": 20, "id_1-end": 20, "id_2-start": 17, "id_2-end": 18, "relation-type": "named", "Exp": "", "Un": False, "SA": False}, 
    {"id_1-start": 26, "id_1-end": 27, "id_2-start": 33, "id_2-end": 33, "relation-type": "physical", "Exp": "", "Un": False, "SA": False}, 
    {"id_1-start": 26, "id_1-end": 27, "id_2-start": 35, "id_2-end": 35, "relation-type": "physical", "Exp": "", "Un": False, "SA": False}, 
    {"id_1-start": 26, "id_1-end": 27, "id_2-start": 38, "id_2-end": 38, "relation-type": "temporal", "Exp": "", "Un": False, "SA": False}, 
    {"id_1-start": 26, "id_1-end": 27, "id_2-start": 45, "id_2-end": 46, "relation-type": "social", "Exp": "greeted_by", "Un": False, "SA": False}, 
    {"id_1-start": 29, "id_1-end": 29, "id_2-start": 26, "id_2-end": 27, "relation-type": "named", "Exp": "", "Un": False, "SA": False}, 
    {"id_1-start": 45, "id_1-end": 46, "id_2-start": 55, "id_2-end": 55, "relation-type": "social", "Exp": "marriage", "Un": False, "SA": False}, 
    {"id_1-start": 49, "id_1-end": 50, "id_2-start": 45, "id_2-end": 46, "relation-type": "named", "Exp": "", "Un": False, "SA": False}
  ]
}
```

#### ai
- **Size of downloaded dataset files:** 0.51 MB
- **Size of the generated dataset:** 0.46 MB

An example of 'train' looks as follows:
```python
{
  "doc_key": "ai-train-1", 
  "sentence": ["Popular", "approaches", "of", "opinion-based", "recommender", "system", "utilize", "various", "techniques", "including", "text", "mining", ",", "information", "retrieval", ",", "sentiment", "analysis", "(", "see", "also", "Multimodal", "sentiment", "analysis", ")", "and", "deep", "learning", "X.Y.", "Feng", ",", "H.", "Zhang", ",", "Y.J.", "Ren", ",", "P.H.", "Shang", ",", "Y.", "Zhu", ",", "Y.C.", "Liang", ",", "R.C.", "Guan", ",", "D.", "Xu", ",", "(", "2019", ")", ",", ",", "21", "(", "5", ")", ":", "e12957", "."], 
  "ner": [
    {"id-start": 3, "id-end": 5, "entity-type": "product"}, 
    {"id-start": 10, "id-end": 11, "entity-type": "field"}, 
    {"id-start": 13, "id-end": 14, "entity-type": "task"}, 
    {"id-start": 16, "id-end": 17, "entity-type": "task"}, 
    {"id-start": 21, "id-end": 23, "entity-type": "task"}, 
    {"id-start": 26, "id-end": 27, "entity-type": "field"}, 
    {"id-start": 28, "id-end": 29, "entity-type": "researcher"}, 
    {"id-start": 31, "id-end": 32, "entity-type": "researcher"}, 
    {"id-start": 34, "id-end": 35, "entity-type": "researcher"}, 
    {"id-start": 37, "id-end": 38, "entity-type": "researcher"}, 
    {"id-start": 40, "id-end": 41, "entity-type": "researcher"}, 
    {"id-start": 43, "id-end": 44, "entity-type": "researcher"}, 
    {"id-start": 46, "id-end": 47, "entity-type": "researcher"}, 
    {"id-start": 49, "id-end": 50, "entity-type": "researcher"}
  ], 
  "relations": [
    {"id_1-start": 3, "id_1-end": 5, "id_2-start": 10, "id_2-end": 11, "relation-type": "part-of", "Exp": "", "Un": False, "SA": False}, 
    {"id_1-start": 3, "id_1-end": 5, "id_2-start": 10, "id_2-end": 11, "relation-type": "usage", "Exp": "", "Un": False, "SA": False}, 
    {"id_1-start": 3, "id_1-end": 5, "id_2-start": 13, "id_2-end": 14, "relation-type": "part-of", "Exp": "", "Un": False, "SA": False}, 
    {"id_1-start": 3, "id_1-end": 5, "id_2-start": 13, "id_2-end": 14, "relation-type": "usage", "Exp": "", "Un": False, "SA": False}, 
    {"id_1-start": 3, "id_1-end": 5, "id_2-start": 16, "id_2-end": 17, "relation-type": "part-of", "Exp": "", "Un": False, "SA": False}, 
    {"id_1-start": 3, "id_1-end": 5, "id_2-start": 16, "id_2-end": 17, "relation-type": "usage", "Exp": "", "Un": False, "SA": False}, 
    {"id_1-start": 3, "id_1-end": 5, "id_2-start": 26, "id_2-end": 27, "relation-type": "part-of", "Exp": "", "Un": False, "SA": False}, 
    {"id_1-start": 3, "id_1-end": 5, "id_2-start": 26, "id_2-end": 27, "relation-type": "usage", "Exp": "", "Un": False, "SA": False}, 
    {"id_1-start": 21, "id_1-end": 23, "id_2-start": 16, "id_2-end": 17, "relation-type": "part-of", "Exp": "", "Un": False, "SA": False}, 
    {"id_1-start": 21, "id_1-end": 23, "id_2-start": 16, "id_2-end": 17, "relation-type": "type-of", "Exp": "", "Un": False, "SA": False}
  ]
}
```

### Data Fields

The data fields are the same among all splits.
- `doc_key`: the instance id of this sentence, a `string` feature.
- `sentence`: the list of tokens of this sentence, obtained with spaCy, a `list` of `string` features.
- `ner`: the list of named entities in this sentence, a `list` of `dict` features.
  - `id-start`: the start index of the entity, a `int` feature.
  - `id-end`: the end index of the entity, a `int` feature.
  - `entity-type`: the type of the entity, a `string` feature.
- `relations`: the list of relations in this sentence, a `list` of `dict` features.
  - `id_1-start`: the start index of the first entity, a `int` feature.
  - `id_1-end`: the end index of the first entity, a `int` feature.
  - `id_2-start`: the start index of the second entity, a `int` feature.
  - `id_2-end`: the end index of the second entity, a `int` feature.
  - `relation-type`: the type of the relation, a `string` feature.
  - `Exp`: the explanation of the relation type assigned, a `string` feature.
  - `Un`: uncertainty of the annotator, a `bool` feature.
  - `SA`: existence of syntax ambiguity which poses a challenge for the annotator, a `bool` feature.

### Data Splits
#### Sentences
|              | Train   | Dev     | Test    | Total   |
|--------------|---------|---------|---------|---------|
| news         | 164     | 350     | 400     | 914     |
| politics     | 101     | 350     | 400     | 851     |
| science      | 103     | 351     | 400     | 854     |
| music        | 100     | 350     | 399     | 849     |
| literature   | 100     | 400     | 416     | 916     |
| ai           | 100     | 350     | 431     | 881     |
| ------------ | ------- | ------- | ------- | ------- |
| total        | 668     | 2,151   | 2,46    | 5,265   |

#### Relations
|              | Train   | Dev     | Test    | Total   |
|--------------|---------|---------|---------|---------|
| news         | 175     | 300     | 396     | 871     |
| politics     | 502     | 1,616   | 1,831   | 3,949   |
| science      | 355     | 1,340   | 1,393   | 3,088   |
| music        | 496     | 1,861   | 2,333   | 4,690   |
| literature   | 397     | 1,539   | 1,591   | 3,527   |
| ai           | 350     | 1,006   | 1,127   | 2,483   |
| ------------ | ------- | ------- | ------- | ------- |
| total        | 2,275   | 7,662   | 8,671   | 18,608  |

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
@inproceedings{bassignana-plank-2022-crossre,
    title = "Cross{RE}: A {C}ross-{D}omain {D}ataset for {R}elation {E}xtraction",
    author = "Bassignana, Elisa and Plank, Barbara",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2022",
    year = "2022",
    publisher = "Association for Computational Linguistics"
}
```

### Contributions

Thanks to [@phucdev](https://github.com/phucdev) for adding this dataset.