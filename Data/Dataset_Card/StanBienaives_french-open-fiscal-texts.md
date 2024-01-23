---
annotations_creators:
- no-annotation
language_creators:
- other
language:
- fr-FR
license:
- cc0-1.0
multilinguality:
- monolingual
pretty_name: french-open-fiscal-texts
size_categories:
- 100K<n<1M
source_datasets:
- original
task_categories:
- summarization
- feature-extraction
task_ids: []
---

# Dataset Card for french-open-fiscal-texts

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

- **Homepage:** https://echanges.dila.gouv.fr/OPENDATA/JADE/
- **Repository:** [Needs More Information]
- **Paper:** [Needs More Information]
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [Needs More Information]

### Dataset Summary

This dataset is an extraction from the OPENDATA/JADE. A list of case laws from the French court "Conseil d'Etat".


### Supported Tasks and Leaderboards

[Needs More Information]

### Languages

fr-FR

## Dataset Structure

### Data Instances

```json
{
   "file": "CETATEXT000007584427.xml",
   "title": "Cour administrative d'appel de Marseille, 3�me chambre - formation � 3, du 21 octobre 2004, 00MA01080, in�dit au recueil Lebon",
   "summary": "",
    "content": "Vu la requête, enregistrée le 22 mai 2000, présentée pour M. Roger X, par Me Luherne, élisant domicile ...), et les mémoires complémentaires en date des 28 octobre 2002, 22 mars 2004 et 16 septembre 2004 ; M. X demande à la Cour :\n\n\n \n 11/ d'annuler le jugement n° 951520 en date du 16 mars 2000 par lequel le Tribunal administratif de Montpellier a rejeté sa requête tendant à la réduction des cotisations supplémentaires à l'impôt sur le revenu et des pénalités dont elles ont été assorties, auxquelles il a été assujetti au titre des années 1990, 1991 et 1992 ;\n\n\n \n 22/ de prononcer la réduction desdites cotisations ;\n\n\n \n 3°/ de condamner de l'Etat à lui verser une somme de 32.278 francs soit 4.920,75 euros"
}
```

### Data Fields

`file`: identifier on the JADE OPENDATA file

`title`: Name of the law case  
`summary`: Summary provided by JADE (may be missing)  
`content`: Text content of the case law

### Data Splits

train  
test


## Dataset Creation

### Curation Rationale

This dataset is an attempt to gather multiple tax related french text law.  
The first intent it to build model to summarize law cases

### Source Data

#### Initial Data Collection and Normalization

Collected from the https://echanges.dila.gouv.fr/OPENDATA/
- Filtering xml files containing "Code général des impôts" (tax related)
- Extracting content, summary, identifier, title


#### Who are the source language producers?

DILA

### Annotations

#### Annotation process

[Needs More Information]

#### Who are the annotators?

[Needs More Information]

### Personal and Sensitive Information

[Needs More Information]

## Considerations for Using the Data

### Social Impact of Dataset

[Needs More Information]

### Discussion of Biases

[Needs More Information]

### Other Known Limitations

[Needs More Information]

## Additional Information

### Dataset Curators

[Needs More Information]

### Licensing Information

[Needs More Information]

### Citation Information

[Needs More Information]