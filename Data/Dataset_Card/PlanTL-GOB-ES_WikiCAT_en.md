---
YAML tags:
annotations_creators:
- automatically-generated
language_creators:
- found
language:
- en
license:
- cc-by-sa-3.0
multilinguality:
- monolingual
pretty_name: wikicat_en
size_categories:
- unknown
source_datasets: []
task_categories:
- text-classification
task_ids:
- multi-class-classification
---

# WikiCAT_en (Text Classification) English dataset


## Dataset Description

- **Paper:** 

- **Point of Contact:** 

carlos.rodriguez1@bsc.es


**Repository**

https://github.com/TeMU-BSC/WikiCAT

### Dataset Summary

WikiCAT_en is a English corpus for thematic Text Classification tasks. It is created automatically from Wikipedia and Wikidata sources, and contains 28921 article summaries from the Wikiipedia classified under 19 different categories.

This dataset was developed by BSC TeMU as part of the PlanTL project, and intended as an evaluation of LT capabilities to generate useful synthetic corpus.

### Supported Tasks and Leaderboards

Text classification, Language Model

### Languages

EN - English

## Dataset Structure

### Data Instances

Two json files, one for each split.

### Data Fields

We used a simple model with the article text and associated labels, without further metadata.

#### Example:

<pre>
{"version": "1.1.0",
 "data":
   [
    {
     {'sentence': 'The IEEE Donald G. Fink Prize Paper Award was established in 1979 by the board of directors of the Institute of Electrical and Electronics Engineers (IEEE) in honor of Donald G. Fink. He was a past president of the Institute of Radio Engineers (IRE), and the first general manager and executive director of the IEEE. Recipients of this award received a certificate and an honorarium. The award was presented annually since 1981 and discontinued in 2016.', 'label': 'Engineering'
     },
    .
    .
    .
  ]
}


</pre>

#### Labels

'Health', 'Law', 'Entertainment', 'Religion', 'Business', 'Science', 'Engineering', 'Nature', 'Philosophy', 'Economy', 'Sports', 'Technology', 'Government', 'Mathematics', 'Military', 'Humanities', 'Music', 'Politics', 'History'

### Data Splits

* hftrain_en.json: 20237 label-document pairs
* hfeval_en.json: 8684  label-document pairs


## Dataset Creation

### Methodology

Se eligen páginas de partida “Category:” para representar los temas en cada lengua.

Se extrae para cada categoría las páginas principales, así como las subcategorías, y las páginas individuales bajo estas subcategorías de primer nivel.
Para cada página, se extrae también el “summary” que proporciona Wikipedia.
 

### Curation Rationale


### Source Data

#### Initial Data Collection and Normalization

The source data are Wikipedia page summaries and thematic categories

#### Who are the source language producers?



### Annotations

#### Annotation process



#### Who are the annotators?

Automatic annotation

### Personal and Sensitive Information

No personal or sensitive information included.

## Considerations for Using the Data

### Social Impact of Dataset

[N/A]

### Discussion of Biases

[N/A]

### Other Known Limitations

[N/A]

## Additional Information

### Dataset Curators 
Text Mining Unit (TeMU) at the Barcelona Supercomputing Center (bsc-temu@bsc.es). 

For further information, send an email to (plantl-gob-es@bsc.es).

This work was funded by the [Spanish State Secretariat for Digitalization and Artificial Intelligence (SEDIA)](https://avancedigital.mineco.gob.es/en-us/Paginas/index.aspx) within the framework of the [Plan-TL](https://plantl.mineco.gob.es/Paginas/index.aspx).

### Licensing information
This work is licensed under [CC Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/) License.

Copyright by the Spanish State Secretariat for Digitalization and Artificial Intelligence (SEDIA) (2022)

### Contributions
[N/A]