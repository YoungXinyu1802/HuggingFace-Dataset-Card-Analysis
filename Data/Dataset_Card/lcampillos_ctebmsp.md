---
license: cc-by-4.0
language: 
- es
multilinguality:
- monolingual
task_categories:
- token-classification
task_ids:
- named-entity-recognition
pretty_name:
- CT-EBM-SP 
---
# CT-EBM-SP (Clinical Trials for Evidence-based Medicine in Spanish) 

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

- **Homepage:** http://www.lllf.uam.es/ESP/nlpmedterm_en.html
- **Repository:** http://www.lllf.uam.es/ESP/nlpdata/wp2/CT-EBM-SP.zip
- **Paper:** Campillos-Llanos, L., Valverde-Mateos, A., Capllonch-Carrión, A., & Moreno-Sandoval, A. (2021). A clinical trials corpus annotated with UMLS entities to enhance the access to evidence-based medicine. BMC medical informatics and decision making, 21(1), 1-19
- **Point of Contact:** leonardo.campillos AT gmail.com

### Dataset Summary

The [Clinical Trials for Evidence-Based-Medicine in Spanish corpus](http://www.lllf.uam.es/ESP/nlpdata/wp2/) is a collection of 1200 texts about clinical trials studies and clinical trials announcements:
- 500 abstracts from journals published under a Creative Commons license, e.g. available in PubMed or the Scientific Electronic Library Online (SciELO)
- 700 clinical trials announcements published in the European Clinical Trials Register and Repositorio Español de Estudios Clínicos

If you use the CT-EBM-SP resource, please, cite as follows:

```
@article{campillosetal-midm2021,
        title = {A clinical trials corpus annotated with UMLS© entities to enhance the access to Evidence-Based Medicine},
        author = {Campillos-Llanos, Leonardo and Valverde-Mateos, Ana and Capllonch-Carri{\'o}n, Adri{\'a}n and Moreno-Sandoval, Antonio},
        journal = {BMC Medical Informatics and Decision Making},
        volume={21},
        number={1},
        pages={1--19},
        year={2021},
        publisher={BioMed Central}
}
```

### Supported Tasks 

Medical Named Entity Recognition

### Languages

Spanish

## Dataset Structure

### Data Instances
- 292 173 tokens
- 46 699 entities of the following [Unified Medical Language System (UMLS)](https://www.nlm.nih.gov/research/umls/index.html) semantic groups: 
  - ANAT (anatomy and body parts): 6728 entities
  - CHEM (chemical and pharmacological substances): 9224 entities
  - DISO (pathologic conditions): 13 067 entities
  - PROC (therapeutic and diagnostic procedures, and laboratory analyses): 17 680 entities


### Data Splits

- Train: 175 203 tokens, 28 101 entities
- Development: 58 670 tokens, 9629 entities
- Test: 58 300 tokens, 8969 entities

## Dataset Creation

### Source Data

- Abstracts from journals published under a Creative Commons license, available in [PubMed](https://pubmed.ncbi.nlm.nih.gov/) or the [Scientific Electronic Library Online (SciELO)](https://scielo.org/es/)
- Clinical trials announcements published in the [European Clinical Trials Register](https://www.clinicaltrialsregister.eu) and [Repositorio Español de Estudios Clínicos](https://reec.aemps.es)


### Annotations

#### Who are the annotators?

- Leonardo Campillos-Llanos, Computational Linguist, Consejo Superior de Investigaciones Científicas
- Adrián Capllonch-Carrión, Medical Doctor, Centro de Salud Retiro, Hospital Universitario Gregorio Marañón
- Ana Valverde-Mateos, Medical Lexicographer, Spanish Royal Academy of Medicine

## Considerations for Using the Data

**Disclosure**: This dataset is under development and needs to be improved. It should not be used for medical decision making without human assistance and supervision.

This resource is intended for a generalist purpose, and may have bias and/or any other undesirable distortions.

The owner or creator of the models will in no event be liable for any results arising from the use made by third parties of this dataset.

**Descargo de responsabilidad**: Este conjunto de datos se encuentra en desarrollo y no debe ser empleada para la toma de decisiones médicas

La finalidad de este modelo es generalista, y puede tener sesgos y/u otro tipo de distorsiones indeseables.

El propietario o creador de los modelos de ningún modo será responsable de los resultados derivados del uso que las terceras partes hagan de estos datos.