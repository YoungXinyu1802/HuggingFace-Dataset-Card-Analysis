---
annotations_creators:
- expert-generated
language:
- en
language_creators:
- found
license:
- other
multilinguality:
- monolingual
pretty_name: ScienceIE is a dataset for the SemEval task of extracting key phrases
  and relations between them from scientific documents
size_categories:
- 1K<n<10K
source_datasets: []
tags:
- research papers
- scientific papers
task_categories:
- token-classification
- text-classification
task_ids:
- named-entity-recognition
- multi-class-classification
dataset_info:
- config_name: ner
  features:
  - name: id
    dtype: string
  - name: tokens
    sequence: string
  - name: tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-Material
          '2': I-Material
          '3': B-Process
          '4': I-Process
          '5': B-Task
          '6': I-Task
  splits:
  - name: train
    num_bytes: 1185670
    num_examples: 2388
  - name: validation
    num_bytes: 204095
    num_examples: 400
  - name: test
    num_bytes: 399069
    num_examples: 838
  download_size: 13704567
  dataset_size: 1788834
- config_name: re
  features:
  - name: id
    dtype: string
  - name: tokens
    dtype: string
  - name: arg1_start
    dtype: int32
  - name: arg1_end
    dtype: int32
  - name: arg1_type
    dtype: string
  - name: arg2_start
    dtype: int32
  - name: arg2_end
    dtype: int32
  - name: arg2_type
    dtype: string
  - name: relation
    dtype:
      class_label:
        names:
          '0': O
          '1': Synonym-of
          '2': Hyponym-of
  splits:
  - name: train
    num_bytes: 11738520
    num_examples: 24558
  - name: validation
    num_bytes: 2347796
    num_examples: 4838
  - name: test
    num_bytes: 2835275
    num_examples: 6618
  download_size: 13704567
  dataset_size: 16921591
- config_name: subtask_a
  features:
  - name: id
    dtype: string
  - name: tokens
    sequence: string
  - name: tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B
          '2': I
  splits:
  - name: train
    num_bytes: 1185670
    num_examples: 2388
  - name: validation
    num_bytes: 204095
    num_examples: 400
  - name: test
    num_bytes: 399069
    num_examples: 838
  download_size: 13704567
  dataset_size: 1788834
- config_name: subtask_b
  features:
  - name: id
    dtype: string
  - name: tokens
    sequence: string
  - name: tags
    sequence:
      class_label:
        names:
          '0': O
          '1': M
          '2': P
          '3': T
  splits:
  - name: train
    num_bytes: 1185670
    num_examples: 2388
  - name: validation
    num_bytes: 204095
    num_examples: 400
  - name: test
    num_bytes: 399069
    num_examples: 838
  download_size: 13704567
  dataset_size: 1788834
- config_name: subtask_c
  features:
  - name: id
    dtype: string
  - name: tokens
    sequence: string
  - name: tags
    sequence:
      sequence:
        class_label:
          names:
            '0': O
            '1': S
            '2': H
  splits:
  - name: train
    num_bytes: 20103682
    num_examples: 2388
  - name: validation
    num_bytes: 3575511
    num_examples: 400
  - name: test
    num_bytes: 6431513
    num_examples: 838
  download_size: 13704567
  dataset_size: 30110706
---

# Dataset Card for ScienceIE

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

- **Homepage:** [https://scienceie.github.io/index.html](https://scienceie.github.io/index.html)
- **Repository:** [https://github.com/ScienceIE/scienceie.github.io](https://github.com/ScienceIE/scienceie.github.io)
- **Paper:** [SemEval 2017 Task 10: ScienceIE - Extracting Keyphrases and Relations from Scientific Publications](https://arxiv.org/abs/1704.02853)
- **Leaderboard:** [https://competitions.codalab.org/competitions/15898](https://competitions.codalab.org/competitions/15898)
- **Size of downloaded dataset files:** 13.7 MB
- **Size of generated dataset files:** 17.4 MB

### Dataset Summary

ScienceIE is a dataset for the SemEval task of extracting key phrases and relations between them from scientific documents.
A corpus for the task was built from ScienceDirect open access publications and was available freely for participants, without the need to sign a copyright agreement. Each data instance consists of one paragraph of text, drawn from a scientific paper.
Publications were provided in plain text, in addition to xml format, which included the full text of the publication as well as additional metadata. 500 paragraphs from journal articles evenly distributed among the domains Computer Science, Material Sciences and Physics were selected.
The training data part of the corpus consists of 350 documents, 50 for development and 100 for testing. This is similar to the pilot task described in Section 5, for which 144 articles were used for training, 40 for development and for 100 testing.

There are three subtasks:

- Subtask (A): Identification of keyphrases 
  - Given a scientific publication, the goal of this task is to identify all the keyphrases in the document.
- Subtask (B): Classification of identified keyphrases
  - In this task, each keyphrase needs to be labelled by one of three types: (i) PROCESS, (ii) TASK, and (iii) MATERIAL. 
    - PROCESS: Keyphrases relating to some scientific model, algorithm or process should be labelled by PROCESS. 
    - TASK: Keyphrases those denote the application, end goal, problem, task should be labelled by TASK. 
    - MATERIAL: MATERIAL keyphrases identify the resources used in the paper.
- Subtask (C): Extraction of relationships between two identified keyphrases 
  - Every pair of keyphrases need to be labelled by one of three types: (i) HYPONYM-OF, (ii) SYNONYM-OF, and (iii) NONE. 
    - HYPONYM-OF: The relationship between two keyphrases A and B is HYPONYM-OF if semantic field of A is included within that of B. One example is Red HYPONYM-OF Color. 
    - SYNONYM-OF: The relationship between two keyphrases A and B is SYNONYM-OF if they both denote the same semantic field, for example Machine Learning SYNONYM-OF ML.

Note: In this repository the documents were split into sentences using spaCy, resulting in a 2388, 400, 838 split. The `id` consists of the document id and the example index within the document separated by an underscore, e.g. `S0375960115004120_1`. This should enable you to reconstruct the documents from the sentences.

### Supported Tasks and Leaderboards

- **Tasks:** Key phrase extraction and relation extraction in scientific documents
- **Leaderboards:** [https://competitions.codalab.org/competitions/15898](https://competitions.codalab.org/competitions/15898)

### Languages

The language in the dataset is English.

## Dataset Structure

### Data Instances

#### subtask_a
- **Size of downloaded dataset files:** 13.7 MB
- **Size of the generated dataset:** 17.4 MB
  
An example of 'train' looks as follows:
```json
{
  "id": "S0375960115004120_1", 
  "tokens": ["Another", "remarkable", "feature", "of", "the", "quantum", "field", "treatment", "can", "be", "revealed", "from", "the", "investigation", "of", "the", "vacuum", "state", "."], 
  "tags": [0, 0, 0, 0, 0, 1, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0]
}
```
#### subtask_b
- **Size of downloaded dataset files:** 13.7 MB
- **Size of the generated dataset:** 17.4 MB
  
An example of 'train' looks as follows:
```json
{
  "id": "S0375960115004120_2", 
  "tokens": ["For", "a", "classical", "field", ",", "vacuum", "is", "realized", "by", "simply", "setting", "the", "potential", "to", "zero", "resulting", "in", "an", "unaltered", ",", "free", "evolution", "of", "the", "particle", "'s", "plane", "wave", "(", "|ψI〉=|ψIII〉=|k0", "〉", ")", "."], 
  "tags": [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0]
}
```

#### subtask_c
- **Size of downloaded dataset files:** 13.7 MB
- **Size of the generated dataset:** 30.1 MB
  
An example of 'train' looks as follows:
```json
{
  "id": "S0375960115004120_3",
  "tokens": ["In", "the", "quantized", "treatment", ",", "vacuum", "is", "represented", "by", "an", "initial", "Fock", "state", "|n0=0", "〉", "which", "still", "interacts", "with", "the", "particle", "and", "yields", "as", "final", "state", "|ΨIII", "〉", "behind", "the", "field", "region(19)|ΨI〉=|k0〉⊗|0〉⇒|ΨIII〉=∑n=0∞t0n|k−n〉⊗|n", "〉", "with", "a", "photon", "exchange", "probability(20)P0,n=|t0n|2=1n!e−Λ2Λ2n", "The", "particle", "thus", "transfers", "energy", "to", "the", "vacuum", "field", "leading", "to", "a", "Poissonian", "distributed", "final", "photon", "number", "."],
  "tags": [[0, 0, ...], [0, 0, ...], ...]
}
```
Note: The tag sequence consists of vectors for each token, that encode what the relationship between that token
and every other token in the sequence is for the first token in each key phrase.

#### ner
- **Size of downloaded dataset files:** 13.7 MB
- **Size of the generated dataset:** 17.4 MB
  
An example of 'train' looks as follows:
```json
{
  "id": "S0375960115004120_4", 
  "tokens": ["Let", "'s", "consider", ",", "for", "example", ",", "a", "superconducting", "resonant", "circuit", "as", "source", "of", "the", "field", "."], 
  "tags": [0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 0, 0, 0, 0, 0, 0]
}
```

#### re
- **Size of downloaded dataset files:** 13.7 MB
- **Size of the generated dataset:** 16.4 MB
  
An example of 'train' looks as follows:
```json
{
  "id": "S0375960115004120_5", 
  "tokens": ["In", "the", "quantized", "treatment", ",", "vacuum", "is", "represented", "by", "an", "initial", "Fock", "state", "|n0=0", "〉", "which", "still", "interacts", "with", "the", "particle", "and", "yields", "as", "final", "state", "|ΨIII", "〉", "behind", "the", "field", "region(19)|ΨI〉=|k0〉⊗|0〉⇒|ΨIII〉=∑n=0∞t0n|k−n〉⊗|n", "〉", "with", "a", "photon", "exchange", "probability(20)P0,n=|t0n|2=1n!e−Λ2Λ2n", "The", "particle", "thus", "transfers", "energy", "to", "the", "vacuum", "field", "leading", "to", "a", "Poissonian", "distributed", "final", "photon", "number", "."], 
  "arg1_start": 2, 
  "arg1_end": 4, 
  "arg1_type": "Task", 
  "arg2_start": 5, 
  "arg2_end": 6, 
  "arg2_type": "Material", 
  "relation": 0
}
```

### Data Fields

#### subtask_a
- `id`: the instance id of this sentence, a `string` feature.
- `tokens`: the list of tokens of this sentence, obtained with spaCy, a `list` of `string` features.
- `tags`: the list of tags of this sentence marking a token as being outside, at the beginning, or inside a key phrase, a `list` of classification labels.

```python
{"O": 0, "B": 1, "I": 2}
```

#### subtask_b
- `id`: the instance id of this sentence, a `string` feature.
- `tokens`: the list of tokens of this sentence, obtained with spaCy, a `list` of `string` features.
- `tags`: the list of tags of this sentence marking a token as being outside a key phrase, or being part of a material, process or task, a `list` of classification labels.

```python
{"O": 0, "M": 1, "P": 2, "T": 3}
```

#### subtask_c
- `id`: the instance id of this sentence, a `string` feature.
- `tokens`: the list of tokens of this sentence, obtained with spaCy, a `list` of `string` features.
- `tags`: a vector for each token, that encodes what the relationship between that token and every other token in the sequence is for the first token in each key phrase, a `list` of a `list` of a classification label.

```python
{"O": 0, "S": 1, "H": 2}
```

#### ner
- `id`: the instance id of this sentence, a `string` feature.
- `tokens`: the list of tokens of this sentence, obtained with spaCy, a `list` of `string` features.
- `tags`: the list of ner tags of this sentence, a `list` of classification labels.

```python
{"O": 0, "B-Material": 1, "I-Material": 2, "B-Process": 3, "I-Process": 4, "B-Task": 5, "I-Task": 6}
```

#### re
- `id`: the instance id of this sentence, a `string` feature.
- `token`: the list of tokens of this sentence, obtained with spaCy, a `list` of `string` features.
- `arg1_start`: the 0-based index of the start token of the relation arg1 mention, an `ìnt` feature.
- `arg1_end`: the 0-based index of the end token of the relation arg1 mention, exclusive, an `ìnt` feature.
- `arg1_type`: the key phrase type of the end token of the relation arg1 mention, a `string` feature.
- `arg2_start`: the 0-based index of the start token of the relation arg2 mention, an `ìnt` feature.
- `arg2_end`: the 0-based index of the end token of the relation arg2 mention, exclusive, an `ìnt` feature.
- `arg2_type`: the key phrase type of the relation arg2 mention, a `string` feature.
- `relation`: the relation label of this instance, a classification label.

```python
{"O": 0, "Synonym-of": 1, "Hyponym-of": 2}
```

### Data Splits

|           | Train | Dev  | Test |
|-----------|-------|------|------|
| subtask_a | 2388  | 400  | 838  |
| subtask_b | 2388  | 400  | 838  |
| subtask_c | 2388  | 400  | 838  |
| ner       | 2388  | 400  | 838  |
| re        | 24558 | 4838 | 6618 |

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
@article{DBLP:journals/corr/AugensteinDRVM17,
  author    = {Isabelle Augenstein and
               Mrinal Das and
               Sebastian Riedel and
               Lakshmi Vikraman and
               Andrew McCallum},
  title     = {SemEval 2017 Task 10: ScienceIE - Extracting Keyphrases and Relations
               from Scientific Publications},
  journal   = {CoRR},
  volume    = {abs/1704.02853},
  year      = {2017},
  url       = {http://arxiv.org/abs/1704.02853},
  eprinttype = {arXiv},
  eprint    = {1704.02853},
  timestamp = {Mon, 13 Aug 2018 16:46:36 +0200},
  biburl    = {https://dblp.org/rec/journals/corr/AugensteinDRVM17.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```

### Contributions

Thanks to [@phucdev](https://github.com/phucdev) for adding this dataset.