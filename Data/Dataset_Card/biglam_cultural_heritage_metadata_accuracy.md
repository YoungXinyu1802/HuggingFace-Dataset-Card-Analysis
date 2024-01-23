---
annotations_creators:
- machine-generated
- expert-generated
language:
- it
language_creators:
- expert-generated
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: Annotated dataset to assess the accuracy of the textual description of
  cultural heritage records
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- text-classification
task_ids:
- acceptability-classification
---

# Dataset Card for Annotated dataset to assess the accuracy of the textual description of cultural heritage records

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

- **Homepage:**[https://doi.org/10.6084/m9.figshare.13359104.v1](https://doi.org/10.6084/m9.figshare.13359104.v1)
- **Repository:**[https://doi.org/10.6084/m9.figshare.13359104.v1](https://doi.org/10.6084/m9.figshare.13359104.v1)
- **Paper:**[https://doi.org/10.1007/s00799-021-00302-1](https://doi.org/10.1007/s00799-021-00302-1)
- **Leaderboard:**
- **Point of Contact:**

### Dataset Summary

The dataset contains more than 100K textual descriptions of cultural items from [Cultura Italia](http://www.culturaitalia.it/opencms/index.jsp?language=en), the Italian National Cultural aggregator. Each of the description is labeled either HIGH or LOW quality, according its adherence to the standard cataloguing guidelines provided by Istituto Centrale per il Catalogo e la Documentazione (ICCD). More precisely, each description is labeled as HIGH quality if the object and subject of the item (for which the description is provided) are both described according to the ICCD guidelines, and as LOW quality in all other cases. Most of the dataset was manually annotated, with ~30K descriptions automatically labeled as LOW quality due to their length (less than 3 tokens) or their provenance from old (pre-2012), not curated, collections. The dataset was developed to support the training and testing of ML text classification approaches for automatically assessing the quality of textual descriptions in digital Cultural Heritage repositories.

### Supported Tasks and Leaderboards

This dataset can be used for text classification tasks. The [paper](https://doi.org/10.1007/s00799-021-00302-1) introducing the dataset achieved an f1 score of `.783` for the task of classifying if a metadata record was low or high quality. Please see the [results table](https://link.springer.com/article/10.1007/s00799-021-00302-1/tables/4) for a full overview of the results reported in the paper. 


### Languages

The dataset consists of Italian metadata records. The labels are in English. 

## Dataset Structure

The dataset has only one configuration.

### Data Instances

An example instance from the dataset:

``` python
{'metadata_text': 'Figure:putto.Oggetti:ghirlanda di fiori',
 'label': 0,
 'source': 'OpereArteVisiva'}
```

### Data Fields

The datafields are:

- `metadata_text`: this contains the metadata text which was sourced from [Cultura Italia](http://www.culturaitalia.it/opencms/index.jsp?language=en)
- `label`: this is the label indicating if the record is `High_Quality`, or `Low_Quality`. Most of the dataset was manually annotated, with ~30K descriptions automatically labelled as LOW quality due to their length (less than 3 tokens) or their provenance from old (pre-2012), not curated, collections.
- `source`: the source of the metadata record

### Data Splits

The dataset used 'ten-fold cross-validation' and doesn't report specific splits for train, validation and test data. 

## Dataset Creation

The dataset was generated using records from [Cultura Italia](http://www.culturaitalia.it/opencms/index.jsp?language=en). From the paper introducing the dataset:

> By using the textual description encoded by the dc:description element from the Dublin Core metadata schema, we collect a dataset of 100,821 descriptions, after duplicate removal. These records include mainly data from “Musei d’Italia” and “Regione Marche” datasets, which have been chosen because they contain a high number of non-empty dc:description elements. p.221

### Curation Rationale

From the paper:

> Duplicates were removed for two reasons: this reduced annotation effort in the subsequent manual annotation, and avoided that the same example appear both in the training and in the test set, a situation that could make classification biased and lead to inaccurate evaluation in supervised settings.Footnote 10 Duplicated descriptions were mainly short and of low-quality, reporting few generic words to describe an item (e.g. “Mensola.”, “Dipinto.”). p.221


### Source Data

#### Initial Data Collection and Normalization

The dataset was generated using records from [Cultura Italia](http://www.culturaitalia.it/opencms/index.jsp?language=en). This repository is accessible via an OAI-PMH handler or via a [SPARQL endpoint](http://dati.culturaitalia.it/sparql).

As discussed above duplicates were removed from the dataset.

#### Who are the source language producers?

The metadata producers are staff working in Italian cultural heritage institutions.

### Annotations

#### Annotation process

From the paper:

> "Most of the dataset was manually annotated, with ~30K descriptions automatically labeled as LOW quality due to their length (less than 3 tokens) or their provenance from old (pre-2012), not curated, collections."

To determine the quality of the collected descriptions the authors of the paper used guidelines from the [Istituto Centrale per il Catalogo e la Documentazione](http://www.iccd.beniculturali.it/)

From the paper:

> "More precisely, a specific section of the guidelines addresses how to describe any cultural item, clarifying that both the object and the subject of the item must be presented in the description as follows:

> Object: the object typology and shape must be described. To describe the object, the cataloguer must refer to the vocabularies provided by ICCD, using specific terminology (e.g. the technique used for paintings and drawings, or the material for the archaeological items);

> Subject: the cataloguer must report the iconographic and decorative settings of the item, such as the characters of the depicted scene in a painting and their attribution. Other aspects (e.g. the history behind the painting or the painter) should not be included." p.221


[More Information Needed]

#### Who are the annotators?

> "The annotation is carried out by an expert in cultural heritage who collaborated in the past with Cultura Italia and has therefore in-depth knowledge of the data characteristics and of the ICCD guidelines." p.222


### Personal and Sensitive Information

No personal or sensitive information is described in the paper.

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators
- Lorenzini, Matteo
- Rospocher, Marco
- Tonelli, Sara

### Licensing Information

[cc-by-4.0](https://creativecommons.org/licenses/by/4.0/)


### Citation Information

```
@article{Lorenzini2020,
author = "Matteo Lorenzini and Marco Rospocher and Sara Tonelli",
title = "{Annotated dataset to assess the accuracy of the textual description of cultural heritage records}",
year = "2020",
month = "12",
url = "https://figshare.com/articles/dataset/Annotated_dataset_to_assess_the_accuracy_of_the_textual_description_of_cultural_heritage_records/13359104",
doi = "10.6084/m9.figshare.13359104.v1"
}
```
### Contributions

Thanks to [@davanstrien](https://github.com/davanstrien) for adding this dataset.
