# Dataset Card for [corpusELE.csv]

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

corpusELE is a dataset made of texts from students of Spanish as Foreign Language (**ELE**), all from a set of files of **CAES** (Corpus de Aprendices de Español como Lengua Extranjera) downloaded from the website of the **Instituto Cervantes**. The main objective of this dataset is the creation and subsequent training, by means of Deep Learning, of a classification model that, based on these data, allows to establish, given an expression in Spanish, the level of knowledge of Spanish and even the mother tongue of the speaker.

In linguistics, a corpus is a more or less extensive set of texts in electronic format that have been assembled in a computer application, according to a certain design, to facilitate the study of the language or linguistic variety from which these texts have been extracted. Among the many types and subtypes of corpora that currently exist, the so-called 'learner corpora' contain texts produced by people who are learning a given language and who speak different initial, familiar or mother tongues and different degrees of knowledge of the target language (levels) and CAES is one of those.

* **File Name**: corpusELE.csv
* **Content Description**: Set of text from ELE students of different levels of proficiency and with different mother tongues.
* **File Type**: CSV separated by COMMA
* **Header Descriptions**: Included in the dataset (first row)
* **Encoding type**: UTF-8


### Dataset Summary

* Number of Columns: 6
* Number of Rows: 46.787


### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

Spanish

## Dataset Structure

1. **numero** (float): CAES phrase or text number.
2. **nivel** (string): Level of knowledge of Spanish of the ELE student who has provided the text. It will be one of those established in the Common European Framework of Reference in the learning of foreign languages.
3. **lenguaM** (string): Mother tongue of the ELE student to which the registered text belongs.
4. **pClave** (string): Key Word in the phrase or text. As indicated, it may be a punctuation mark, a mark or any other element or character in the sentence considered prominent or characteristic.
5. **frase** (string): Complete phrase or text provided by the ELE student. It is made up of the concatenation of the two parts into which it has been segmented in the source files and it also includes the word or key element.
6. **archivo** (string): It is and additional information included in the dataset in order to be able to use it in the preprocessing of the data. It refers to the name of the file from which the corresponding text has been taken. Although this information is not necessary for the object of the work, it is of interest when debugging the data capture. Later it will be information that we can do without.

### Data Instances

Each instance of the dataset consists of a single sentence or text

### Data Fields

[More Information Needed]

### Data Splits

[More Information Needed]

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

The Cervantes Institute, on its website (www.institutocervantes.es), makes freely available to users the so-called CAES or Corpus de Aprendices de Español, currently in its version 2.1. published in March 2022.

#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

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

Thanks to [@github-username](https://github.com/<github-username>) for adding this dataset.