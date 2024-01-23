---
license: cc-by-nc-4.0
---
# Dataset Card for TexPrax

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

- **Homepage: https://texprax.de/**
- **Repository: https://github.com/UKPLab/TexPrax**
- **Paper: https://arxiv.org/abs/2208.07846**
- **Leaderboard: n/a**
- **Point of Contact: Ji-Ung Lee (http://www.ukp.tu-darmstadt.de/)**

### Dataset Summary

This dataset contains dialogues collected from German factory workers at the _Center for industrial productivity_ ([CiP](https://www.prozesslernfabrik.de/)). The  dialogues mostly concern issues workers encounter during their daily work, such as machines breaking down, material missing, etc. The dialogues are further expert-annotated on a sentence level (problem, cause, solution, other) for sentence classification and on a token level for named entity recognition using a BIO tagging scheme. Note, that the dataset was collected in three rounds, each around one year apart. Here, we provide the data only split into train and test data where the test data was collected at the last round (July 2022). Additionally, the data from the first round is split into two subdomains, industry 4.0 (industrie) and machining (zerspanung). The splits were made according to the respective groups of people working at different assembly lines in the factory.

### Supported Tasks and Leaderboards

This dataset supports the following tasks:

* Sentence classification
* Named entity recognition (will be updated soon with the new indexing)
* Dialog generation (so far not evaluated)

### Languages

German

## Dataset Structure

### Data Instances

On sentence level, each instance consists of the dialog-id, turn-id, sentence-id, the sentence (raw), the label, the domain, and the subsplit. 

```
{"185";"562";993";"wie kriege ich die Dichtung raus?";"P";"n/a";"3"}
```

On token level, each instance consists of a unique identifier, a list of tokens containing the whole dialog, the list of labels (bio-tagged entities), and the subsplit.
```
{"178_0";"['Hi', 'wie', 'kriege', 'ich', 'die', 'Dichtung', 'raus', '?', 'in', 'der', 'Schublade', 'gibt', 'es', 'einen', 'Dichtungszieher']";"['O', 'O', 'O', 'O', 'O', 'B-PRE', 'O', 'O', 'O', 'O', 'B-LOC', 'O', 'O', 'O', 'B-PE']";"Batch 3"}
```

### Data Fields

Sentence level: 

* dialog-id: unique identifier for the dialog
* turn-id: unique identifier for the turn
* sentence-id: unique identifier for the dialog
* sentence: the respective sentence
* label: the label (_P_ for Problem, _C_ for Cause, _S_ for solution, and _O_ for Other)
* domain: the subdomains where the data was collected from. Domains are industry, machining, or n/a (for batch 2 and batch 3).
* subsplit: the respective subsplit of the data (see below)

Token level: 

* id: the identifier
* tokens: a list of tokens (i.e., the tokenized dialogue) 
* entities: the named entity in a BIO scheme (_B-X_, _I-X_, or O). 
* subsplit: the respective subsplit of the data (see below)


### Data Splits

The dataset is split into train and test splits, but contains further subsplits (subsplit column). Note, that the splits are collected at different times with some turnaround in the workforce. Hence, later data (especially the data from batch 2) contains more turns (due to increased search for a cause) as more inexperienced workers who newly joined were employed in the factory. 

Train:
* Batch 1 industrie: data collected in October 2020 from workers in the industry 4.0 assembly line
* Batch 1 zerspanung: data collected in October 2020 from workers in the machining assembly line
* Batch 2: data collected in-between October 2021-June 2022 from all workers

Test:
* Batch 3: data collected in July 2022 together with the system usability study run

Sentence level statistics: 

| Batch  | Dialogues | Turns | Sentences |   
|---|---|---|---|
| 1  |  81 | 246  | 553  |   
| 2 |  97 | 309  | 432  |   
| 3  |  24 | 36  | 42  |   
| Overall | 202 | 591 | 1,027 |   

Token level statistics: 
[Needs to be added]

## Dataset Creation

### Curation Rationale

This dataset provides task-oriented dialogues that solve a very domain specific problem.  

### Source Data

#### Initial Data Collection and Normalization

The data was generated by workers at the [CiP](https://www.prozesslernfabrik.de/). The data was collected in three rounds (October 2020, October 2021-June 2022, July 2022). As the dialogues occurred during their daily work, one distinct property of the dataset is that all dialogues are very informal 'ne', contain abbreviations 'vll', and filler words such as 'ah'. For a detailed description please see the [paper](https://arxiv.org/abs/2208.07846).

#### Who are the source language producers?

German factory workers working at the [CiP](https://www.prozesslernfabrik.de/)

### Annotations

#### Annotation process

**Token level.** Token level annotation was done by researchers who are responsible for supervising and teaching workers at the CiP. The data was first split into three parts, each annotated by one researcher. Next, each researcher cross-examined the other researchers' annotations. If there were disagreements, all three researchers discussed the final label.

**Sentence level.** Sentence level annotations were collected from the factory workers who also generated the dialogues. For details about the data collection, please see the [TexPrax demo paper](https://arxiv.org/abs/2208.07846).

#### Who are the annotators?

**Token level.**  Researchers working at the CiP.

**Sentence level.** The factory workers themselves.

### Personal and Sensitive Information

This dataset is fully anonymized. All occurrences of names have been manually checked during annotation and replaced with a random token.

## Considerations for Using the Data

### Social Impact of Dataset

Informal language especially used in short messages, however, seldom considered in existing NLP datasets. This dataset could serve as an interesting evaluation task for transferring language models to low-resource, but highly specific domains. Moreover, we note that despite all abbreviations, typos, and local dialects used in the messages, all workers were able to understand the questions as well as replies. This should be a standard future NLP models should be able to uphold. 

### Discussion of Biases

The dialogues are very much on a professional level. The workers were informed (and gave their consent) in advance that their messages are being recorded and processed, which may have influenced them to hold only professional conversations, hence, all dialogues concern inanimate objects (i.e., machines). 

### Other Known Limitations

[More Information Needed]

## Additional Information

You can download the data via:

```
from datasets import load_dataset

dataset = load_dataset("UKPLab/TexPrax") # default config is sentence classification
dataset = load_dataset("UKPLab/TexPrax", "ner") # use the ner tag for named entity recognition
``` 
Please find more information about the code and how the data was collected on [GitHub](https://github.com/UKPLab/TexPrax).

### Dataset Curators

Curation is managed by our [data manager](https://www.informatik.tu-darmstadt.de/ukp/research_ukp/ukp_research_data_and_software/ukp_data_and_software.en.jsp) at UKP.

### Licensing Information

[CC-by-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)

### Citation Information

Please cite this data using: 

```
@article{stangier2022texprax,
  title={TexPrax: A Messaging Application for Ethical, Real-time Data Collection and Annotation},
  author={Stangier, Lorenz and Lee, Ji-Ung and Wang, Yuxi and M{\"u}ller, Marvin and Frick, Nicholas and Metternich, Joachim and Gurevych, Iryna},
  journal={arXiv preprint arXiv:2208.07846},
  year={2022}
}
```

### Contributions

Thanks to [@Wuhn](https://github.com/Wuhn) for adding this dataset.

## Tags

annotations_creators:
- expert-generated

language:
- de

language_creators:
- expert-generated

license:
- cc-by-nc-4.0

multilinguality:
- monolingual

pretty_name: TexPrax-Conversations

size_categories:
- n<1K
- 1K<n<10K

source_datasets:
- original

tags:
- dialog
- expert to expert conversations
- task-oriented

task_categories:
- token-classification
- text-classification

task_ids:
- named-entity-recognition
- multi-class-classification