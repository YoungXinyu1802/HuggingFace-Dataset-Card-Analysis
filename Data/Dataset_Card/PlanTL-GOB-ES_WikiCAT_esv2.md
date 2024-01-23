---
YAML tags:
annotations_creators:
- automatically-generated
language_creators:
- found
language:
- es
license:
- cc-by-sa-3.0
multilinguality:
- monolingual
pretty_name: wikicat_esv2
size_categories:
- unknown
source_datasets: []
task_categories:
- text-classification
task_ids:
- multi-class-classification
---

# WikiCAT_ca: Spanish Text Classification dataset


## Dataset Description

- **Paper:** 

- **Point of Contact:** carlos.rodriguez1@bsc.es


**Repository**




### Dataset Summary

WikiCAT_ca is a Spanish corpus for thematic Text Classification tasks. It is created automatically from Wikipedia and Wikidata sources, and contains 8401 articles from the Viquipedia classified under 12 different categories.

This dataset was developed by BSC TeMU as part of the PlanTL project, and intended as an evaluation of LT capabilities to generate useful synthetic corpus.

### Supported Tasks and Leaderboards

Text classification, Language Model

### Languages

ES- Spanish

## Dataset Structure

### Data Instances

Two json files, one for each split.

### Data Fields

We used a simple model with the article text and associated labels, without further metadata.

#### Example:

<pre>
{'sentence': 'La economía de Reunión se ha basado tradicionalmente en la agricultura. La caña de azúcar ha sido el cultivo principal durante más de un siglo, y en algunos años representa el 85% de las exportaciones. El gobierno ha estado impulsando el desarrollo de una industria turística para aliviar el alto desempleo, que representa más del 40% de la fuerza laboral.(...) El PIB total de la isla fue de 18.800 millones de dólares EE.UU. en 2007., 'label': 'Economía'}


</pre>

#### Labels

'Religión', 'Entretenimiento', 'Música', 'Ciencia_y_Tecnología', 'Política', 'Economía', 'Matemáticas', 'Humanidades', 'Deporte', 'Derecho', 'Historia', 'Filosofía'

### Data Splits

* hfeval_esv5.json: 1681 label-document pairs
* hftrain_esv5.json: 6716  label-document pairs


## Dataset Creation

### Methodology

La páginas de "Categoría" representan los temas.
para cada tema, extraemos las páginas asociadas a ese primer nivel de la jerarquía, y utilizamos el resúmen ("summary") como texto representativo.

### Curation Rationale



### Source Data

#### Initial Data Collection and Normalization

The source data are thematic categories in the different Wikipedias

#### Who are the source language producers?


### Annotations

#### Annotation process
Automatic annotation

#### Who are the annotators?

[N/A]

### Personal and Sensitive Information

No personal or sensitive information included.

## Considerations for Using the Data

### Social Impact of Dataset

We hope this corpus contributes to the development of language models in Spanish.

### Discussion of Biases

We are aware that this data might contain biases. We have not applied any steps to reduce their impact.

### Other Known Limitations

[N/A]

## Additional Information

### Dataset Curators

Text Mining Unit (TeMU) at the Barcelona Supercomputing Center (bsc-temu@bsc.es). 

For further information, send an email to (plantl-gob-es@bsc.es).

This work was funded by the [Spanish State Secretariat for Digitalization and Artificial Intelligence (SEDIA)](https://avancedigital.mineco.gob.es/en-us/Paginas/index.aspx) within the framework of the [Plan-TL](https://plantl.mineco.gob.es/Paginas/index.aspx).

### Licensing Information

This work is licensed under [CC Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/) License.

Copyright by the Spanish State Secretariat for Digitalization and Artificial Intelligence (SEDIA) (2022)

### Contributions

[N/A]
