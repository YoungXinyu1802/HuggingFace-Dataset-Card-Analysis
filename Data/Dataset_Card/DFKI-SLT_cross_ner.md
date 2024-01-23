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
pretty_name: CrossNER is a cross-domain dataset for named entity recognition
size_categories:
- 10K<n<100K
source_datasets:
- extended|conll2003
tags:
- cross domain
- ai
- news
- music
- literature
- politics
- science
task_categories:
- token-classification
task_ids:
- named-entity-recognition
dataset_info:
- config_name: ai
  features:
  - name: id
    dtype: string
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-academicjournal
          '2': I-academicjournal
          '3': B-album
          '4': I-album
          '5': B-algorithm
          '6': I-algorithm
          '7': B-astronomicalobject
          '8': I-astronomicalobject
          '9': B-award
          '10': I-award
          '11': B-band
          '12': I-band
          '13': B-book
          '14': I-book
          '15': B-chemicalcompound
          '16': I-chemicalcompound
          '17': B-chemicalelement
          '18': I-chemicalelement
          '19': B-conference
          '20': I-conference
          '21': B-country
          '22': I-country
          '23': B-discipline
          '24': I-discipline
          '25': B-election
          '26': I-election
          '27': B-enzyme
          '28': I-enzyme
          '29': B-event
          '30': I-event
          '31': B-field
          '32': I-field
          '33': B-literarygenre
          '34': I-literarygenre
          '35': B-location
          '36': I-location
          '37': B-magazine
          '38': I-magazine
          '39': B-metrics
          '40': I-metrics
          '41': B-misc
          '42': I-misc
          '43': B-musicalartist
          '44': I-musicalartist
          '45': B-musicalinstrument
          '46': I-musicalinstrument
          '47': B-musicgenre
          '48': I-musicgenre
          '49': B-organisation
          '50': I-organisation
          '51': B-person
          '52': I-person
          '53': B-poem
          '54': I-poem
          '55': B-politicalparty
          '56': I-politicalparty
          '57': B-politician
          '58': I-politician
          '59': B-product
          '60': I-product
          '61': B-programlang
          '62': I-programlang
          '63': B-protein
          '64': I-protein
          '65': B-researcher
          '66': I-researcher
          '67': B-scientist
          '68': I-scientist
          '69': B-song
          '70': I-song
          '71': B-task
          '72': I-task
          '73': B-theory
          '74': I-theory
          '75': B-university
          '76': I-university
          '77': B-writer
          '78': I-writer
  splits:
  - name: train
    num_bytes: 65080
    num_examples: 100
  - name: validation
    num_bytes: 189453
    num_examples: 350
  - name: test
    num_bytes: 225691
    num_examples: 431
  download_size: 289173
  dataset_size: 480224
- config_name: literature
  features:
  - name: id
    dtype: string
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-academicjournal
          '2': I-academicjournal
          '3': B-album
          '4': I-album
          '5': B-algorithm
          '6': I-algorithm
          '7': B-astronomicalobject
          '8': I-astronomicalobject
          '9': B-award
          '10': I-award
          '11': B-band
          '12': I-band
          '13': B-book
          '14': I-book
          '15': B-chemicalcompound
          '16': I-chemicalcompound
          '17': B-chemicalelement
          '18': I-chemicalelement
          '19': B-conference
          '20': I-conference
          '21': B-country
          '22': I-country
          '23': B-discipline
          '24': I-discipline
          '25': B-election
          '26': I-election
          '27': B-enzyme
          '28': I-enzyme
          '29': B-event
          '30': I-event
          '31': B-field
          '32': I-field
          '33': B-literarygenre
          '34': I-literarygenre
          '35': B-location
          '36': I-location
          '37': B-magazine
          '38': I-magazine
          '39': B-metrics
          '40': I-metrics
          '41': B-misc
          '42': I-misc
          '43': B-musicalartist
          '44': I-musicalartist
          '45': B-musicalinstrument
          '46': I-musicalinstrument
          '47': B-musicgenre
          '48': I-musicgenre
          '49': B-organisation
          '50': I-organisation
          '51': B-person
          '52': I-person
          '53': B-poem
          '54': I-poem
          '55': B-politicalparty
          '56': I-politicalparty
          '57': B-politician
          '58': I-politician
          '59': B-product
          '60': I-product
          '61': B-programlang
          '62': I-programlang
          '63': B-protein
          '64': I-protein
          '65': B-researcher
          '66': I-researcher
          '67': B-scientist
          '68': I-scientist
          '69': B-song
          '70': I-song
          '71': B-task
          '72': I-task
          '73': B-theory
          '74': I-theory
          '75': B-university
          '76': I-university
          '77': B-writer
          '78': I-writer
  splits:
  - name: train
    num_bytes: 63181
    num_examples: 100
  - name: validation
    num_bytes: 244076
    num_examples: 400
  - name: test
    num_bytes: 270092
    num_examples: 416
  download_size: 334380
  dataset_size: 577349
- config_name: music
  features:
  - name: id
    dtype: string
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-academicjournal
          '2': I-academicjournal
          '3': B-album
          '4': I-album
          '5': B-algorithm
          '6': I-algorithm
          '7': B-astronomicalobject
          '8': I-astronomicalobject
          '9': B-award
          '10': I-award
          '11': B-band
          '12': I-band
          '13': B-book
          '14': I-book
          '15': B-chemicalcompound
          '16': I-chemicalcompound
          '17': B-chemicalelement
          '18': I-chemicalelement
          '19': B-conference
          '20': I-conference
          '21': B-country
          '22': I-country
          '23': B-discipline
          '24': I-discipline
          '25': B-election
          '26': I-election
          '27': B-enzyme
          '28': I-enzyme
          '29': B-event
          '30': I-event
          '31': B-field
          '32': I-field
          '33': B-literarygenre
          '34': I-literarygenre
          '35': B-location
          '36': I-location
          '37': B-magazine
          '38': I-magazine
          '39': B-metrics
          '40': I-metrics
          '41': B-misc
          '42': I-misc
          '43': B-musicalartist
          '44': I-musicalartist
          '45': B-musicalinstrument
          '46': I-musicalinstrument
          '47': B-musicgenre
          '48': I-musicgenre
          '49': B-organisation
          '50': I-organisation
          '51': B-person
          '52': I-person
          '53': B-poem
          '54': I-poem
          '55': B-politicalparty
          '56': I-politicalparty
          '57': B-politician
          '58': I-politician
          '59': B-product
          '60': I-product
          '61': B-programlang
          '62': I-programlang
          '63': B-protein
          '64': I-protein
          '65': B-researcher
          '66': I-researcher
          '67': B-scientist
          '68': I-scientist
          '69': B-song
          '70': I-song
          '71': B-task
          '72': I-task
          '73': B-theory
          '74': I-theory
          '75': B-university
          '76': I-university
          '77': B-writer
          '78': I-writer
  splits:
  - name: train
    num_bytes: 65077
    num_examples: 100
  - name: validation
    num_bytes: 259702
    num_examples: 380
  - name: test
    num_bytes: 327195
    num_examples: 465
  download_size: 414065
  dataset_size: 651974
- config_name: conll2003
  features:
  - name: id
    dtype: string
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-academicjournal
          '2': I-academicjournal
          '3': B-album
          '4': I-album
          '5': B-algorithm
          '6': I-algorithm
          '7': B-astronomicalobject
          '8': I-astronomicalobject
          '9': B-award
          '10': I-award
          '11': B-band
          '12': I-band
          '13': B-book
          '14': I-book
          '15': B-chemicalcompound
          '16': I-chemicalcompound
          '17': B-chemicalelement
          '18': I-chemicalelement
          '19': B-conference
          '20': I-conference
          '21': B-country
          '22': I-country
          '23': B-discipline
          '24': I-discipline
          '25': B-election
          '26': I-election
          '27': B-enzyme
          '28': I-enzyme
          '29': B-event
          '30': I-event
          '31': B-field
          '32': I-field
          '33': B-literarygenre
          '34': I-literarygenre
          '35': B-location
          '36': I-location
          '37': B-magazine
          '38': I-magazine
          '39': B-metrics
          '40': I-metrics
          '41': B-misc
          '42': I-misc
          '43': B-musicalartist
          '44': I-musicalartist
          '45': B-musicalinstrument
          '46': I-musicalinstrument
          '47': B-musicgenre
          '48': I-musicgenre
          '49': B-organisation
          '50': I-organisation
          '51': B-person
          '52': I-person
          '53': B-poem
          '54': I-poem
          '55': B-politicalparty
          '56': I-politicalparty
          '57': B-politician
          '58': I-politician
          '59': B-product
          '60': I-product
          '61': B-programlang
          '62': I-programlang
          '63': B-protein
          '64': I-protein
          '65': B-researcher
          '66': I-researcher
          '67': B-scientist
          '68': I-scientist
          '69': B-song
          '70': I-song
          '71': B-task
          '72': I-task
          '73': B-theory
          '74': I-theory
          '75': B-university
          '76': I-university
          '77': B-writer
          '78': I-writer
  splits:
  - name: train
    num_bytes: 3561081
    num_examples: 14041
  - name: validation
    num_bytes: 891431
    num_examples: 3250
  - name: test
    num_bytes: 811470
    num_examples: 3453
  download_size: 2694794
  dataset_size: 5263982
- config_name: politics
  features:
  - name: id
    dtype: string
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-academicjournal
          '2': I-academicjournal
          '3': B-album
          '4': I-album
          '5': B-algorithm
          '6': I-algorithm
          '7': B-astronomicalobject
          '8': I-astronomicalobject
          '9': B-award
          '10': I-award
          '11': B-band
          '12': I-band
          '13': B-book
          '14': I-book
          '15': B-chemicalcompound
          '16': I-chemicalcompound
          '17': B-chemicalelement
          '18': I-chemicalelement
          '19': B-conference
          '20': I-conference
          '21': B-country
          '22': I-country
          '23': B-discipline
          '24': I-discipline
          '25': B-election
          '26': I-election
          '27': B-enzyme
          '28': I-enzyme
          '29': B-event
          '30': I-event
          '31': B-field
          '32': I-field
          '33': B-literarygenre
          '34': I-literarygenre
          '35': B-location
          '36': I-location
          '37': B-magazine
          '38': I-magazine
          '39': B-metrics
          '40': I-metrics
          '41': B-misc
          '42': I-misc
          '43': B-musicalartist
          '44': I-musicalartist
          '45': B-musicalinstrument
          '46': I-musicalinstrument
          '47': B-musicgenre
          '48': I-musicgenre
          '49': B-organisation
          '50': I-organisation
          '51': B-person
          '52': I-person
          '53': B-poem
          '54': I-poem
          '55': B-politicalparty
          '56': I-politicalparty
          '57': B-politician
          '58': I-politician
          '59': B-product
          '60': I-product
          '61': B-programlang
          '62': I-programlang
          '63': B-protein
          '64': I-protein
          '65': B-researcher
          '66': I-researcher
          '67': B-scientist
          '68': I-scientist
          '69': B-song
          '70': I-song
          '71': B-task
          '72': I-task
          '73': B-theory
          '74': I-theory
          '75': B-university
          '76': I-university
          '77': B-writer
          '78': I-writer
  splits:
  - name: train
    num_bytes: 143507
    num_examples: 200
  - name: validation
    num_bytes: 422760
    num_examples: 541
  - name: test
    num_bytes: 472690
    num_examples: 651
  download_size: 724168
  dataset_size: 1038957
- config_name: science
  features:
  - name: id
    dtype: string
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-academicjournal
          '2': I-academicjournal
          '3': B-album
          '4': I-album
          '5': B-algorithm
          '6': I-algorithm
          '7': B-astronomicalobject
          '8': I-astronomicalobject
          '9': B-award
          '10': I-award
          '11': B-band
          '12': I-band
          '13': B-book
          '14': I-book
          '15': B-chemicalcompound
          '16': I-chemicalcompound
          '17': B-chemicalelement
          '18': I-chemicalelement
          '19': B-conference
          '20': I-conference
          '21': B-country
          '22': I-country
          '23': B-discipline
          '24': I-discipline
          '25': B-election
          '26': I-election
          '27': B-enzyme
          '28': I-enzyme
          '29': B-event
          '30': I-event
          '31': B-field
          '32': I-field
          '33': B-literarygenre
          '34': I-literarygenre
          '35': B-location
          '36': I-location
          '37': B-magazine
          '38': I-magazine
          '39': B-metrics
          '40': I-metrics
          '41': B-misc
          '42': I-misc
          '43': B-musicalartist
          '44': I-musicalartist
          '45': B-musicalinstrument
          '46': I-musicalinstrument
          '47': B-musicgenre
          '48': I-musicgenre
          '49': B-organisation
          '50': I-organisation
          '51': B-person
          '52': I-person
          '53': B-poem
          '54': I-poem
          '55': B-politicalparty
          '56': I-politicalparty
          '57': B-politician
          '58': I-politician
          '59': B-product
          '60': I-product
          '61': B-programlang
          '62': I-programlang
          '63': B-protein
          '64': I-protein
          '65': B-researcher
          '66': I-researcher
          '67': B-scientist
          '68': I-scientist
          '69': B-song
          '70': I-song
          '71': B-task
          '72': I-task
          '73': B-theory
          '74': I-theory
          '75': B-university
          '76': I-university
          '77': B-writer
          '78': I-writer
  splits:
  - name: train
    num_bytes: 121928
    num_examples: 200
  - name: validation
    num_bytes: 276118
    num_examples: 450
  - name: test
    num_bytes: 334181
    num_examples: 543
  download_size: 485191
  dataset_size: 732227
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
- **Repository:** [CrossNER](https://github.com/zliucr/CrossNER)
- **Paper:** [CrossNER: Evaluating Cross-Domain Named Entity Recognition](https://arxiv.org/abs/2012.04373)

### Dataset Summary
CrossNER is a fully-labeled collected of named entity recognition (NER) data spanning over five diverse domains 
(Politics, Natural Science, Music, Literature, and Artificial Intelligence) with specialized entity categories for 
different domains. Additionally, CrossNER also includes unlabeled domain-related corpora for the corresponding five 
domains.

For details, see the paper: 
[CrossNER: Evaluating Cross-Domain Named Entity Recognition](https://arxiv.org/abs/2012.04373)

### Supported Tasks and Leaderboards

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Languages

The language data in CrossNER is in English (BCP-47 en)

## Dataset Structure

### Data Instances

#### conll2003
- **Size of downloaded dataset files:** 2.69 MB
- **Size of the generated dataset:** 5.26 MB

An example of 'train' looks as follows:
```json
{
  "id": "0", 
  "tokens": ["EU", "rejects", "German", "call", "to", "boycott", "British", "lamb", "."], 
  "ner_tags": [49, 0, 41, 0, 0, 0, 41, 0, 0]
}
```

#### politics
- **Size of downloaded dataset files:** 0.72 MB
- **Size of the generated dataset:** 1.04 MB

An example of 'train' looks as follows:
```json
{
  "id": "0", 
  "tokens": ["Parties", "with", "mainly", "Eurosceptic", "views", "are", "the", "ruling", "United", "Russia", ",", "and", "opposition", "parties", "the", "Communist", "Party", "of", "the", "Russian", "Federation", "and", "Liberal", "Democratic", "Party", "of", "Russia", "."], 
  "ner_tags": [0, 0, 0, 0, 0, 0, 0, 0, 55, 56, 0, 0, 0, 0, 0, 55, 56, 56, 56, 56, 56, 0, 55, 56, 56, 56, 56, 0]
}
```

#### science
- **Size of downloaded dataset files:** 0.49 MB
- **Size of the generated dataset:** 0.73 MB

An example of 'train' looks as follows:
```json
{
  "id": "0", 
  "tokens": ["They", "may", "also", "use", "Adenosine", "triphosphate", ",", "Nitric", "oxide", ",", "and", "ROS", "for", "signaling", "in", "the", "same", "ways", "that", "animals", "do", "."], 
  "ner_tags": [0, 0, 0, 0, 15, 16, 0, 15, 16, 0, 0, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}
```

#### music
- **Size of downloaded dataset files:** 0.41 MB
- **Size of the generated dataset:** 0.65 MB

An example of 'train' looks as follows:
```json
{
  "id": "0", 
  "tokens": ["In", "2003", ",", "the", "Stade", "de", "France", "was", "the", "primary", "site", "of", "the", "2003", "World", "Championships", "in", "Athletics", "."], 
  "ner_tags": [0, 0, 0, 0, 35, 36, 36, 0, 0, 0, 0, 0, 0, 29, 30, 30, 30, 30, 0]
}
```

#### literature
- **Size of downloaded dataset files:** 0.33 MB
- **Size of the generated dataset:** 0.58 MB

An example of 'train' looks as follows:
```json
{
  "id": "0",
  "tokens": ["In", "1351", ",", "during", "the", "reign", "of", "Emperor", "Toghon", "Temür", "of", "the", "Yuan", "dynasty", ",", "93rd-generation", "descendant", "Kong", "Huan", "(", "孔浣", ")", "'", "s", "2nd", "son", "Kong", "Shao", "(", "孔昭", ")", "moved", "from", "China", "to", "Korea", "during", "the", "Goryeo", ",", "and", "was", "received", "courteously", "by", "Princess", "Noguk", "(", "the", "Mongolian-born", "wife", "of", "the", "future", "king", "Gongmin", ")", "."], 
  "ner_tags": [0, 0, 0, 0, 0, 0, 0, 51, 52, 52, 0, 0, 21, 22, 0, 0, 0, 77, 78, 0, 77, 0, 0, 0, 0, 0, 77, 78, 0, 77, 0, 0, 0, 21, 0, 21, 0, 0, 41, 0, 0, 0, 0, 0, 0, 51, 52, 0, 0, 41, 0, 0, 0, 0, 0, 51, 0, 0]
}
```

#### ai
- **Size of downloaded dataset files:** 0.29 MB
- **Size of the generated dataset:** 0.48 MB

An example of 'train' looks as follows:
```json
{
  "id": "0", 
  "tokens": ["Popular", "approaches", "of", "opinion-based", "recommender", "system", "utilize", "various", "techniques", "including", "text", "mining", ",", "information", "retrieval", ",", "sentiment", "analysis", "(", "see", "also", "Multimodal", "sentiment", "analysis", ")", "and", "deep", "learning", "X.Y.", "Feng", ",", "H.", "Zhang", ",", "Y.J.", "Ren", ",", "P.H.", "Shang", ",", "Y.", "Zhu", ",", "Y.C.", "Liang", ",", "R.C.", "Guan", ",", "D.", "Xu", ",", "(", "2019", ")", ",", ",", "21", "(", "5", ")", ":", "e12957", "."], 
  "ner_tags": [0, 0, 0, 59, 60, 60, 0, 0, 0, 0, 31, 32, 0, 71, 72, 0, 71, 72, 0, 0, 0, 71, 72, 72, 0, 0, 31, 32, 65, 66, 0, 65, 66, 0, 65, 66, 0, 65, 66, 0, 65, 66, 0, 65, 66, 0, 65, 66, 0, 65, 66, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}
```

### Data Fields

The data fields are the same among all splits.
- `id`: the instance id of this sentence, a `string` feature.
- `tokens`: the list of tokens of this sentence, a `list` of `string` features.
- `ner_tags`: the list of entity tags, a `list` of classification labels.

```json
{"O": 0, "B-academicjournal": 1, "I-academicjournal": 2, "B-album": 3, "I-album": 4, "B-algorithm": 5, "I-algorithm": 6, "B-astronomicalobject": 7, "I-astronomicalobject": 8, "B-award": 9, "I-award": 10, "B-band": 11, "I-band": 12, "B-book": 13, "I-book": 14, "B-chemicalcompound": 15, "I-chemicalcompound": 16, "B-chemicalelement": 17, "I-chemicalelement": 18, "B-conference": 19, "I-conference": 20, "B-country": 21, "I-country": 22, "B-discipline": 23, "I-discipline": 24, "B-election": 25, "I-election": 26, "B-enzyme": 27, "I-enzyme": 28, "B-event": 29, "I-event": 30, "B-field": 31, "I-field": 32, "B-literarygenre": 33, "I-literarygenre": 34, "B-location": 35, "I-location": 36, "B-magazine": 37, "I-magazine": 38, "B-metrics": 39, "I-metrics": 40, "B-misc": 41, "I-misc": 42, "B-musicalartist": 43, "I-musicalartist": 44, "B-musicalinstrument": 45, "I-musicalinstrument": 46, "B-musicgenre": 47, "I-musicgenre": 48, "B-organisation": 49, "I-organisation": 50, "B-person": 51, "I-person": 52, "B-poem": 53, "I-poem": 54, "B-politicalparty": 55, "I-politicalparty": 56, "B-politician": 57, "I-politician": 58, "B-product": 59, "I-product": 60, "B-programlang": 61, "I-programlang": 62, "B-protein": 63, "I-protein": 64, "B-researcher": 65, "I-researcher": 66, "B-scientist": 67, "I-scientist": 68, "B-song": 69, "I-song": 70, "B-task": 71, "I-task": 72, "B-theory": 73, "I-theory": 74, "B-university": 75, "I-university": 76, "B-writer": 77, "I-writer": 78}
```

### Data Splits
|              | Train  | Dev   | Test  |
|--------------|--------|-------|-------|
| conll2003    | 14,987 | 3,466 | 3,684 |
| politics     | 200    | 541   | 651   |
| science      | 200    | 450   | 543   |
| music        | 100    | 380   | 456   |
| literature   | 100    | 400   | 416   |
| ai           | 100    | 350   | 431   |

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
@article{liu2020crossner,
      title={CrossNER: Evaluating Cross-Domain Named Entity Recognition}, 
      author={Zihan Liu and Yan Xu and Tiezheng Yu and Wenliang Dai and Ziwei Ji and Samuel Cahyawijaya and Andrea Madotto and Pascale Fung},
      year={2020},
      eprint={2012.04373},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

### Contributions

Thanks to [@phucdev](https://github.com/phucdev) for adding this dataset.