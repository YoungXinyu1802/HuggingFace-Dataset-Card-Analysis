---
YAML tags:
annotations_creators:
- auromatically-generated
language_creators:
- found
language:
- ca
license:
- cc-by-sa-3.0
multilinguality:
- monolingual
pretty_name: wikicat_ca
size_categories:
- unknown
source_datasets: []
task_categories:
- text-classification
task_ids:
- multi-class-classification
---

# WikiCAT_ca: Catalan Text Classification dataset


## Dataset Description

- **Paper:** 

- **Point of Contact:** carlos.rodriguez1@bsc.es


**Repository**

https://github.com/TeMU-BSC/WikiCAT


### Dataset Summary

WikiCAT_ca is a Catalan corpus for thematic Text Classification tasks. It is created automagically from Wikipedia and Wikidata sources, and contains 13201 articles from the Viquipedia classified under 13 different categories.

This dataset was developed by BSC TeMU as part of the AINA project, and intended as an evaluation of LT capabilities to generate useful synthetic corpus.

### Supported Tasks and Leaderboards

Text classification, Language Model

### Languages

CA- Catalan

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
     'sentence': ' Celsius és conegut com l\'inventor de l\'escala centesimal del termòmetre. Encara que aquest instrument és un invent molt antic, la història de la seva gradació és molt més capritxosa. Durant el segle xvi era graduat com "fred" col·locant-lo (...)', 
    'label': 'Ciència'
    },
    .
    .
    .
  ]
}


</pre>

#### Labels

'Ciència_i_Tecnologia', 'Dret', 'Economia', 'Enginyeria', 'Entreteniment', 'Esport', 'Filosofia', 'Història', 'Humanitats', 'Matemàtiques', 'Música', 'Política', 'Religió'

### Data Splits

* dev_ca.json: 2484 label-document pairs
* train_ca.json:  9907 label-document pairs


## Dataset Creation

### Methodology


“Category” starting pages are chosen to represent the topics in each language.

We extract, for each category, the main pages, as well as the subcategories ones, and the individual pages under this first level.
For each page, the "summary" provided by Wikipedia is also extracted as the representative text.

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

We hope this corpus contributes to the development of language models in Catalan, a low-resource language.

### Discussion of Biases

We are aware that this data might contain biases. We have not applied any steps to reduce their impact.

### Other Known Limitations

[N/A]

## Additional Information

### Dataset Curators

Text Mining Unit (TeMU) at the Barcelona Supercomputing Center (bsc-temu@bsc.es)

This work was funded by the [Departament de la Vicepresidència i de Polítiques Digitals i Territori de la Generalitat de Catalunya](https://politiquesdigitals.gencat.cat/ca/inici/index.html#googtrans(ca|en) within the framework of [Projecte AINA](https://politiquesdigitals.gencat.cat/ca/economia/catalonia-ai/aina).

### Licensing Information

This work is licensed under a <a rel="license" href="https://creativecommons.org/licenses/by-sa/4.0/">Attribution-ShareAlike 4.0 International</a>.

### Contributions

[N/A]
