---
annotations_creators:
- found
language_creators:
- found
language:
- ca
license:
- cc-by-nc-nd-4.0
multilinguality:
- monolingual
pretty_name: GuiaCat
size_categories:
- ?
task_categories:
- text-classification
task_ids:
- sentiment-classification
- sentiment-scoring
---

# Dataset Card for GuiaCat

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

- **Point of Contact:** [blanca.calvo@bsc.es](blanca.calvo@bsc.es)

### Dataset Summary

GuiaCat is a dataset consisting of 5.750 restaurant reviews in Catalan, with 5 associated scores and a label of sentiment. The data was provided by [GuiaCat](https://guiacat.cat) and curated by the BSC. 

### Supported Tasks and Leaderboards

This corpus is mainly intended for sentiment analysis.

### Languages

The dataset is in Catalan (`ca-CA`).

## Dataset Structure

The dataset consists of restaurant reviews labelled with 5 scores: service, food, price-quality, environment, and average. Reviews also have a sentiment label, derived from the average score, all stored as a csv file. 

### Data Instances

```
7,7,7,7,7.0,"Aquest restaurant té una llarga història. Ara han tornat a canviar d'amos i aquest canvi s'ha vist molt repercutit en la carta, preus, servei, etc. Hi ha molta varietat de menjar, i tot boníssim, amb especialitats molt ben trobades. El servei molt càlid i agradable, dóna gust que et serveixin així. I la decoració molt agradable també, bastant curiosa. En fi, pel meu gust, un bon restaurant i bé de preu.",bo

8,9,8,7,8.0,"Molt recomanable en tots els sentits. El servei és molt atent, pulcre i gens agobiant; alhora els plats també presenten un aspecte acurat, cosa que fa, juntament amb l'ambient, que t'oblidis de que, malauradament, està situat pròxim a l'autopista.Com deia, l'ambient és molt acollidor, té un menjador principal molt elegant, perfecte per quedar bé amb tothom!Tot i això, destacar la bona calitat / preu, ja que aquest restaurant té una carta molt extensa en totes les branques i completa, tant de menjar com de vins. Pel qui entengui de vins, podriem dir que tot i tenir una carta molt rica, es recolza una mica en els clàssics.",molt bo
```

### Data Fields
- service: a score from 0 to 10 grading the service
- food: a score from 0 to 10 grading the food
- price-quality: a score from 0 to 10 grading the relation between price and quality
- environment: a score from 0 to 10 grading the environment
- avg: average of all the scores
- text: the review
- label: it can be "molt bo", "bo", "regular", "dolent", "molt dolent"

### Data Splits

* dev.csv: 500 examples
* test.csv: 500 examples
* train.csv: 4,750 examples

## Dataset Creation

### Curation Rationale

We created this corpus to contribute to the development of language models in Catalan, a low-resource language. 

### Source Data

The data of this dataset has been provided by [GuiaCat](https://guiacat.cat).

#### Initial Data Collection and Normalization

[N/A]

#### Who are the source language producers?

The language producers were the users from GuiaCat.

### Annotations

The annotations are automatically derived from the scores that the users provided while reviewing the restaurants.

#### Annotation process

The mapping between average scores and labels is:
- Higher than 8: molt bo
- Between 8 and 6: bo
- Between 6 and 4: regular
- Between 4 and 2: dolent
- Less than 2: molt dolent

#### Who are the annotators?

Users

### Personal and Sensitive Information

No personal information included, although it could contain hate or abusive language.

## Considerations for Using the Data

### Social Impact of Dataset

We hope this corpus contributes to the development of language models in Catalan, a low-resource language.

### Discussion of Biases

We are aware that this data might contain biases. We have not applied any steps to reduce their impact.

### Other Known Limitations

[N/A]

## Additional Information

### Dataset Curators

Text Mining Unit (TeMU) at the Barcelona Supercomputing Center (bsc-temu@bsc.es).

This work was funded by the [Departament de la Vicepresidència i de Polítiques Digitals i Territori de la Generalitat de Catalunya](https://politiquesdigitals.gencat.cat/ca/inici/index.html#googtrans(ca|en) within the framework of [Projecte AINA](https://politiquesdigitals.gencat.cat/ca/economia/catalonia-ai/aina).


### Licensing Information

[Creative Commons Attribution Non-commercial No-Derivatives 4.0 International](https://creativecommons.org/licenses/by-nc-nd/4.0/).

### Citation Information

```
```

### Contributions

We want to thank GuiaCat for providing this data.





