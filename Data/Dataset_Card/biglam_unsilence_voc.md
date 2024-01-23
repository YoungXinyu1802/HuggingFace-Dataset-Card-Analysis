---
license: cc-by-4.0
dataset_info:
  features:
  - name: tokens
    sequence: string
  - name: NE-MAIN
    sequence:
      class_label:
        names:
          '0': B-Organization
          '1': B-Organization,B-Place
          '2': B-Organization,I-Person
          '3': B-Organization,I-Place
          '4': B-Person
          '5': B-Person,B-Place
          '6': B-Person,I-Place
          '7': B-Place
          '8': I-Organization
          '9': I-Organization,B-Place
          '10': I-Organization,I-Person
          '11': I-Organization,I-Person,B-Place
          '12': I-Organization,I-Person,I-Place
          '13': I-Organization,I-Place
          '14': I-Person
          '15': I-Person,B-Place
          '16': I-Person,I-Place
          '17': I-Place
          '18': O
  - name: NE-PER-NAME
    sequence:
      class_label:
        names:
          '0': I-ProperName
          '1': O
          '2': B-ProperName
          '3': ''
  - name: NE-PER-GENDER
    sequence:
      class_label:
        names:
          '0': B-Group
          '1': B-Man
          '2': B-Man,B-Unspecified
          '3': B-Man,I-Woman
          '4': B-Unspecified
          '5': B-Unspecified,I-Woman
          '6': B-Woman
          '7': I-Group
          '8': I-Man
          '9': I-Man,I-Unspecified
          '10': I-Man,I-Woman
          '11': I-Unspecified
          '12': I-Unspecified,I-Woman
          '13': I-Woman
          '14': NE-PER-GENDER
          '15': O
  - name: NE-PER-LEGAL-STATUS
    sequence:
      class_label:
        names:
          '0': B-Enslaved
          '1': B-Freed
          '2': B-Unspecified
          '3': I-Enslaved
          '4': I-Freed
          '5': I-Unspecified
          '6': NE-PER-LEGAL-STATUS
          '7': O
  - name: NE-PER-ROLE
    sequence:
      class_label:
        names:
          '0': B-Acting_Notary
          '1': B-Beneficiary
          '2': B-Notary
          '3': B-Other
          '4': B-Testator
          '5': B-Testator_Beneficiary
          '6': B-Witness
          '7': I-Acting_Notary
          '8': I-Beneficiary
          '9': I-Beneficiary,B-Other
          '10': I-Beneficiary,I-Other
          '11': I-Notary
          '12': I-Other
          '13': I-Testator
          '14': I-Testator_Beneficiary
          '15': I-Witness
          '16': NE-PER-ROLE
          '17': O
  - name: NE-ORG-BENEFICIARY
    sequence:
      class_label:
        names:
          '0': B-No
          '1': B-Yes
          '2': I-No
          '3': I-Yes
          '4': NE-ORG-BENEFICIARY
          '5': O
  - name: MISC
    dtype: string
  - name: document_id
    dtype: string
  splits:
  - name: train
    num_bytes: 31436367
    num_examples: 2199
  download_size: 12669993
  dataset_size: 31436367
task_categories:
- token-classification
task_ids:
  - named-entity-recognition
language:
- nl
tags:
- 'lam '
pretty_name: Unsilencing Colonial Archives via Automated Entity Recognition
size_categories:
- 1K<n<10K
---

# Dataset Card for Unsilencing Colonial Archives via Automated Entity Recognition

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

- **Homepage:** https://github.com/budh333/UnSilence_VOC/tree/v1.3 
- **Repository:** https://doi.org/10.5281/zenodo.6958524
- **Paper:** https://arxiv.org/abs/2210.02194
- **Leaderboard:**
- **Point of Contact:** * [Mrinalini Luthra](mailto:mrinalini.luthra@gmail.com)

### Dataset Summary

**Note**: this data card was adapted from documentation and a [data card](https://github.com/budh333/UnSilence_VOC/blob/main/Datacard.pdf) written by the creators of the dataset.  

> Colonial archives are at the center of increased interest from a variety of perspectives, as they contain traces of historically marginalized people. Unfortunately, like most archives, they remain difficult to access due to significant persisting barriers. We focus here on one of them: the biases to be found in historical findings aids, such as indices of person names, which remain in use to this day. In colonial archives, indexes can perpetrate silences by omitting to include mentions of historically marginalized persons. In order to overcome such limitation and pluralize the scope of existing finding aids, we propose using automated entity recognition. To this end, we contribute a fit-for-purpose annotation typology and apply it on the colonial archive of the Dutch East India Company (VOC). We release a corpus of nearly 70,000 annotations as a shared task, for which we provide strong baselines using state-of-the-art neural network models.

This dataset is based on the digitized collection of the Dutch East India
Company (VOC) Testaments under the custody of the Dutch National
Archives. These testaments of VOC-servants are mainly from the 18th
century, for the most part drawn up in the Asian VOC-settlements and
to a lesser extent on the VOC ships and in the Republic. The
testaments have a fixed order in the text structure and the language is
18th century Dutch.

The dataset has 68,429 annotations spanning over 79,797 tokens
across 2193 unique pages. 47% of the total annotations correspond to
entities and 53% to attributes of those entities. Of the 32,203 entity
annotations, 11,715 (36.3%) correspond to instances that represent
persons with associated attributes of gender, legal status and notarial
role, 4,510 (14%) correspond to instances of places, 1,080 (3.5%)
correspond to organizations with attribute beneficiary and 14,898
(46.2%) correspond to proper names (of places, organizations and
persons).


### Supported Tasks and Leaderboards

- named-entity-recognition: This dataset can be used to train a model for Named Entity Recognition. In particular, the dataset was designed to detect mentions of people in archival documents. 

### Languages

The dataset contains 18th Century Dutch. The text in the dataset was produced via handwritten text recognition so contains some errors. 

## Dataset Structure

### Data Instances

Each datapoint refers to a central entity that can be a person, place, organization or proper name or their attributes such as gender, legal
status and notarial role of a person.

### Data Fields

- tokens: tokens being annotated 
- NE-MAIN: main entity type, i.e. person, place, Organization, ProperName
- NE-PER-NAME: person name entity 
- NE-PER-GENDER: When the mention of a person is followed or preceded by
trigger words which reveal their gender, the text is annotated
as a Person with the appropriate value of the attribute Gender.
When a person is mentioned without a gender trigger word,
their gender is marked as Unspecified. 
- NE-PER-LEGAL-STATUS: legal status where known, i.e. Free(d), Enslaved, Unspecified
- NE-PER-ROLE: The attribute Role refers to roles specific to testaments in notarial archives, which may take exactly one of the following
values: Testator, Notary, Witness, Beneficiary, Acting Notary, Testator Beneficiary or Other
- NE-ORG-BENEFICIARY: Organizations have the attribute Beneficiary which can take the value Yes or No depending on
whether the testator decides an organization to be their beneficiary. 
- MISC: other annotations not fitting into the above labels.
- document_id: id for the document being annotated


### Data Splits

[More Information Needed]

## Dataset Creation

### Curation Rationale

This dataset was created for training entity recognition models to create more inclusive content based indexes on the collection of VOC testaments.


### Source Data

#### Initial Data Collection and Normalization

This dataset is based on the digitized collection of the Dutch East India
Company (VOC) Testaments under the custody of the Dutch National
Archives. 

#### Who are the source language producers?

[More Information Needed]

### Annotations

| Entity       | #      | %    |
|--------------|--------|------|
| Person       | 11,715 | 36.4 |
| Place        | 4,510  | 14   |
| Organization | 1,080  | 3.4  |
| ProperName   | 14,898 | 46.2 |

#### Annotation process

Annotations were created as a shared annotation task on the Brat annotation software. Annotations were created by highlighting the relevant span of
text and choosing its entity type and where applicable exactly one attribute value through a drop down menu. To tag the same span as two entities, the span must be selected two times and labelled accordingly. For example: ‘Adam Domingo’ has been labelled twice as a Person and ProperName.

#### Who are the annotators?



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

[More Information Needed]

### Licensing Information

[More Information Needed]

### Citation Information

[More Information Needed]

### Contributions

Thanks to [@davanstrien](https://github.com/davanstrien) for adding this dataset.
