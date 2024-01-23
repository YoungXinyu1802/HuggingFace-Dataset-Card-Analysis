annotations_creators:
- expert-generated
language_creators:
- expert-generated
languages:
- en
licenses:
- unknown
multilinguality:
- monolingual
paperswithcode_id: bc4chemd
pretty_name: BC4CHEMD
size_categories:
- 1K<n<10K
source_datasets:
- original
task_categories:
- structure-prediction
task_ids:
- named-entity-recognition

# Dataset Card for BC4CHEMD

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-instances)
  - [Data Splits](#data-instances)
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

## Dataset Description

- **Homepage:** 
https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/
- **Repository:** https://github.com/cambridgeltl/MTL-Bioinformatics-2016/tree/master/data/BC4CHEMD
- **Paper:** BioCreative V CDR task corpus: a resource for chemical disease relation extraction
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4860626/
- **Leaderboard:** [Needs More Information]
- **Point of Contact:**  [Zhiyong Lu] (mailto: Zhiyong.Lu@nih.gov)

### Dataset Summary

A corpus for both named entity recognition and chemical-disease relations in the literature. A total of 1500 articles have been annotated with automated assistance from PubTator. Jaccard agreement results and corpus statistics verified the reliability of the corpus. 

### Supported Tasks and Leaderboards

named-entity-recognition

### Languages

en

## Dataset Structure

### Data Instances


Instances of the dataset contain an array of `tokens`, `ner_tags` and an `id`. An example of an instance of the dataset:

{
  'tokens': ['DPP6','as','a','candidate','gene','for','neuroleptic','-','induced','tardive','dyskinesia','.']
, 'ner_tags': [0,0,0,0,0,0,0,0,0,0,0,0],
  'id': '0'
  }

### Data Fields


- `id`: Sentence identifier.  
- `tokens`: Array of tokens composing a sentence.  
- `ner_tags`: Array of tags, where `0` indicates no disease mentioned, `1` signals the first token of a chemical and `2` the subsequent chemical tokens.  

### Data Splits


The data is split into a train (3500 instances), validation (3500 instances) and test set (3000 instances).

## Dataset Creation

### Curation Rationale

 The goal of the dataset consists on improving the state-of-the-art in chemical name recognition and normalization research, by providing a high-quality gold standard thus enabling the development of machine-learning based approaches for such tasks.

### Source Data

#### Initial Data Collection and Normalization


The dataset consists on abstracts extracted from PubMed.

#### Who are the source language producers?


The source language producers are the authors of publication abstracts hosted in PubMed.

### Annotations

#### Annotation process

The curators were trained to mark up the text according to the labels specified in the guidelines. The raw text was not tokenized prior to the annotation and only the title was distinguished from the PubMed abstract. The selection of text spans was done at the character level, they did not allow nested annotations and distinct entity mentions should not overlap. Each text span was selected according to the annotation guidelines and classified manually into one of the CEM classes.

#### Who are the annotators?

The group of curators used for preparing the annotations was composed mainly of organic chemistry postgraduates with an average experience of 3-4 years in the annotation of chemical names and chemical structures.

### Personal and Sensitive Information

[N/A]

## Considerations for Using the Data

### Social Impact of Dataset

To avoid annotator bias, pairs of annotators were chosen randomly for each set, so that each pair of annotators overlapped for at most two sets.

### Discussion of Biases

The used CHEMDNER document set had to be representative and balanced in order to reflect the kind of documents that might mention the entity of interest.

### Other Known Limitations

[Needs More Information]

## Additional Information

### Dataset Curators

[Needs More Information]

### Licensing Information

[Needs More Information]

### Citation Information

[Needs More Information]