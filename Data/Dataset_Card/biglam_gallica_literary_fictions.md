---
language: fr
license: cc0-1.0
multilinguality:
- monolingual
pretty_name: Literary fictions of Gallica
source_datasets:
- original
task_categories:
- text-generation
task_ids:
- language-modeling
---

# Dataset Card for Literary fictions of Gallica

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

- **Homepage:** https://doi.org/10.5281/zenodo.4660197
- **Repository:**
- **Paper:**
- **Leaderboard:**
- **Point of Contact:**

### Dataset Summary

The collection "Fiction littéraire de Gallica" includes 19,240 public domain documents from the digital platform of the French National Library that were originally classified as novels or, more broadly, as literary fiction in prose. It consists of 372 tables of data in tsv format for each year of publication from 1600 to 1996 (all the missing years are in the 17th and 20th centuries). Each table is structured at the page-level of each novel (5,723,986 pages in all). It contains the complete text with the addition of some metadata. It can be opened in Excel or, preferably, with the new data analysis environments in R or Python (tidyverse, pandas…)

This corpus can be used for large-scale quantitative analyses in computational humanities. The OCR text is presented in a raw format without any correction or enrichment in order to be directly processed for text mining purposes.

The extraction is based on a historical categorization of the novels: the Y2 or Ybis classification. This classification, invented in 1730, is the only one that has been continuously applied to the BNF collections now available in the public domain (mainly before 1950). Consequently, the dataset is based on a definition of "novel" that is generally contemporary of the publication.

A French data paper (in PDF and HTML) presents the construction process of the Y2 category and describes the structuring of the corpus. It also gives several examples of possible uses for computational humanities projects.

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

[More Information Needed]

## Dataset Structure

### Data Instances

```
{
  'main_id': 'bpt6k97892392_p174',
  'catalogue_id': 'cb31636383z',
  'titre': "L'île du docteur Moreau",
  'nom_auteur': 'Wells',
  'prenom_auteur': 'Herbert George',
  'date': 1946,
  'document_ocr': 99,
  'date_enligne': '07/08/2017',
  'gallica': 'http://gallica.bnf.fr/ark:/12148/bpt6k97892392/f174',
  'page': 174,
  'texte': "_p_ dans leur expression et leurs gestes souples, d au- c tres semblables à des estropiés, ou si étrangement i défigurées qu'on eût dit les êtres qui hantent nos M rêves les plus sinistres. Au delà, se trouvaient d 'un côté les lignes onduleuses -des roseaux, de l'autre, s un dense enchevêtrement de palmiers nous séparant du ravin des 'huttes et, vers le Nord, l horizon brumeux du Pacifique. - _p_ — Soixante-deux, soixante-trois, compta Mo- H reau, il en manque quatre. J _p_ — Je ne vois pas l'Homme-Léopard, dis-je. | Tout à coup Moreau souffla une seconde fois dans son cor, et à ce son toutes les bêtes humai- ' nes se roulèrent et se vautrèrent dans la poussière. Alors se glissant furtivement hors des roseaux, rampant presque et essayant de rejoindre le cercle des autres derrière le dos de Moreau, parut l'Homme-Léopard. Le dernier qui vint fut le petit Homme-Singe. Les autres, échauffés et fatigués par leurs gesticulations, lui lancèrent de mauvais regards. _p_ — Assez! cria Moreau, de sa voix sonore et ferme. Toutes les bêtes s'assirent sur leurs talons et cessèrent leur adoration. - _p_ — Où est celui |qui enseigne la Loi? demanda Moreau."
}
```

### Data Fields

- `main_id`: Unique identifier of the page of the roman.
- `catalogue_id`: Identifier of the edition in the BNF catalogue.
- `titre`: Title of the edition as it appears in the catalog.
- `nom_auteur`: Author's name.
- `prenom_auteur`: Author's first name.
- `date`: Year of edition.
- `document_ocr`: Estimated quality of ocerization for the whole document as a percentage of words probably well recognized (from 1-100).
- `date_enligne`: Date of the online publishing of the digitization on Gallica.
- `gallica`: URL of the document on Gallica.
- `page`: Document page number (this is the pagination of the digital file, not the one of the original document).
- `texte`: Page text, as rendered by OCR.

### Data Splits

The dataset contains a single "train" split.

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed]

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

[Creative Commons Zero v1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/legalcode).

### Citation Information

```
@dataset{langlais_pierre_carl_2021_4751204,
  author       = {Langlais, Pierre-Carl},
  title        = {{Fictions littéraires de Gallica / Literary 
                   fictions of Gallica}},
  month        = apr,
  year         = 2021,
  publisher    = {Zenodo},
  version      = 1,
  doi          = {10.5281/zenodo.4751204},
  url          = {https://doi.org/10.5281/zenodo.4751204}
}
```

### Contributions

Thanks to [@albertvillanova](https://github.com/albertvillanova) for adding this dataset.
