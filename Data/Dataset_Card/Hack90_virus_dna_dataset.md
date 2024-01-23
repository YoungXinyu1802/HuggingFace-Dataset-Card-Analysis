---
dataset_info:
  features:
  - name: description
    dtype: string
  - name: family
    dtype: string
  - name: text
    dtype: string
  - name: genome_length
    dtype: int64
  - name: organism_id
    dtype: string
  splits:
  - name: train
    num_bytes: 1478065196
    num_examples: 117768
  download_size: 2825074
  dataset_size: 1478065196
---
[Needs More Information]

# Dataset Card for virus_dna_dataset

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

- **Homepage:** [Needs More Information]
- **Repository:** [Needs More Information]
- **Paper:** [Needs More Information]
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [Needs More Information]

### Dataset Summary

A collection of full virus genome dna, the dataset was built from NCBI data 

### Supported Tasks and Leaderboards

[Needs More Information]

### Languages

DNA

## Dataset Structure

### Data Instances

{ 'Description' : 'NC_030848.1 Haloarcula californiae icosahedral...',  'dna_sequence' : 'TCATCTC TCTCTCT CTCTCTT GTTCCCG CGCCCGC CCGCCC...', 
'sequence_length':'35787', 'organism_id':' AB063393.2'}    


### Data Fields

{ 'Description' : 'this contains the description about the DNA sequence contained in the NCBI dataset',  'dna_sequence' : 'this contains the dna sequence grouped by 7 nucleotides', 
'sequence_length':'this contains the length of the dna sequence'}    

### Data Splits

[Needs More Information]

## Dataset Creation

### Curation Rationale

The goal of this dataset was to make it easier to train an LLM on virus DNA

### Source Data

#### Initial Data Collection and Normalization

DNA sequences were grouped by 7 nucleotides to make it easier to tokenize. Only full genomes were selected 

#### Who are the source language producers?

Viruses :) 

### Annotations

#### Annotation process

NCBI

#### Who are the annotators?

NCBI

### Personal and Sensitive Information

N/A

## Considerations for Using the Data

### Social Impact of Dataset

Make it easier to train LLMs on virus DNA

### Discussion of Biases

Only virus data that has been sequenced and upload into NCBI is contained in here

### Other Known Limitations

[Needs More Information]

## Additional Information

### Dataset Curators

Hassan Ahmed 

### Licensing Information

[Needs More Information]

### Citation Information

[Needs More Information]