---
annotations_creators:
- expert-generated
language_creators:
- found
language:
- es
license:
- cc-by-sa-4.0
multilinguality:
- monolingual
pretty_name: Spanish Question Answering Corpus (SQAC)
source_datasets:
- original
task_categories:
- question-answering
task_ids:
- extractive-qa

---

# SQAC (Spanish Question-Answering Corpus)

## Dataset Description

SQAC is an extractive QA dataset for the Spanish language.

- **Paper:** [MarIA: Spanish Language Models](https://upcommons.upc.edu/bitstream/handle/2117/367156/6405-5863-1-PB%20%281%29.pdf?sequence=1)
- **Point of Contact:** carlos.rodriguez1@bsc.es
- **Leaderboard:** [EvalEs] (https://plantl-gob-es.github.io/spanish-benchmark/)

### Dataset Summary

Contains 6,247 contexts and 18,817 questions with their respective answers, 1 to 5 for each fragment.

The sources of the contexts are:
* Encyclopedic articles from the [Spanish Wikipedia](https://es.wikipedia.org/), used under [CC-by-sa licence](https://creativecommons.org/licenses/by-sa/3.0/legalcode). 
* News articles from [Wikinews](https://es.wikinews.org/), used under [CC-by licence](https://creativecommons.org/licenses/by/2.5/). 
* Newswire and literature text from the [AnCora corpus](http://clic.ub.edu/corpus/en), used under [CC-by licence](https://creativecommons.org/licenses/by/4.0/legalcode). 

### Supported Tasks

Extractive-QA

### Languages

- Spanish (es)

### Directory Structure
- README.md
- SQAC.py
- dev.json
- test.json
- train.json

## Dataset Structure

### Data Instances

<pre>
{
	'id': '6cf3dcd6-b5a3-4516-8f9e-c5c1c6b66628', 
	'title': 'Historia de Japón', 
	'context': 'La historia de Japón (日本の歴史 o 日本史, Nihon no rekishi / Nihonshi?) es la sucesión de hechos acontecidos dentro del archipiélago japonés. Algunos de estos hechos aparecen aislados e influenciados por la naturaleza geográfica de Japón como nación insular, en tanto que otra serie de hechos, obedece a influencias foráneas como en el caso del Imperio chino, el cual definió su idioma, su escritura y, también, su cultura política. Asimismo, otra de las influencias foráneas fue la de origen occidental, lo que convirtió al país en una nación industrial, ejerciendo con ello una esfera de influencia y una expansión territorial sobre el área del Pacífico. No obstante, dicho expansionismo se detuvo tras la Segunda Guerra Mundial y el país se posicionó en un esquema de nación industrial con vínculos a su tradición cultural.', 
	'question': '¿Qué influencia convirtió Japón en una nación industrial?', 
	'answers': {
		'text': ['la de origen occidental'], 
		'answer_start': [473]
	}
}
</pre>

### Data Fields

<pre>
{
  id: str
  title: str
  context: str
  question: str
  answers: {
    answer_start: [int]
    text: [str]
  }
}
</pre>

### Data Splits

| Split | Size |
| ------------- | ------------- |
| `train`  | 15,036  |
| `dev`  | 1,864  |
| `test`  | 1.910  |

## Content analysis

### Number of articles, paragraphs and questions

* Number of articles: 3,834
* Number of contexts: 6,247
* Number of questions: 18,817
* Number of sentences: 48,026
* Questions/Context ratio: 3.01
* Sentences/Context ratio: 7.70

### Number of tokens

* Total tokens in context: 1,561,616
* Average tokens/context: 250
* Total tokens in questions: 203,235
* Average tokens/question: 10.80
* Total tokens in answers: 90,307
* Average tokens/answer: 4.80

### Lexical variation

46.38% of the words in the Question can be found in the Context.

### Question type 

| Question | Count | % |
|----------|-------:|---:|
| qué | 6,381 | 33.91 % |
| quién/es | 2,952 | 15.69 % |
| cuál/es | 2,034 | 10.81 % |
| cómo | 1,949 | 10.36 % |
| dónde | 1,856 | 9.86 % |
| cuándo | 1,639 | 8.71 % |
| cuánto | 1,311 | 6.97 % |
| cuántos | 495 |2.63 % |
| adónde | 100 | 0.53 % |
| cuánta | 49 | 0.26 % |
| no question mark | 43 | 0.23 % |
| cuántas | 19 | 0.10 % |

## Dataset Creation

### Curation Rationale

For compatibility with similar datasets in other languages, we followed as close as possible existing curation guidelines from SQUAD 1.0 [(Rajpurkar, Pranav et al.)](http://arxiv.org/abs/1606.05250).

### Source Data

#### Initial Data Collection and Normalization

The source data are scraped articles from Wikinews, the Spanish Wikipedia and the AnCora corpus.

- [Spanish Wikipedia](https://es.wikipedia.org)
- [Spanish Wikinews](https://es.wikinews.org/)
- [AnCora corpus](http://clic.ub.edu/corpus/en)

#### Who are the source language producers?

Contributors to the aforementioned sites.

### Annotations

#### Annotation process

We commissioned the creation of 1 to 5 questions for each context, following an adaptation of the guidelines from SQUAD 1.0 [(Rajpurkar, Pranav et al.)](http://arxiv.org/abs/1606.05250).

#### Who are the annotators?

Native language speakers.

### Personal and Sensitive Information

No personal or sensitive information included.

## Considerations for Using the Data

### Social Impact of Dataset

This corpus contributes to the development of language models in Spanish.

### Discussion of Biases

No postprocessing steps were applied to mitigate potential social biases.



## Additional Information

### Dataset Curators 
Text Mining Unit (TeMU) at the Barcelona Supercomputing Center (bsc-temu@bsc.es). 

For further information, send an email to (plantl-gob-es@bsc.es).

This work was funded by the [Spanish State Secretariat for Digitalization and Artificial Intelligence (SEDIA)](https://avancedigital.mineco.gob.es/en-us/Paginas/index.aspx) within the framework of the [Plan-TL](https://plantl.mineco.gob.es/Paginas/index.aspx).

### Licensing information
This work is licensed under [CC Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/) License.

Copyright by the Spanish State Secretariat for Digitalization and Artificial Intelligence (SEDIA) (2022)

### Citation Information

```
@article{maria,
	author = {Asier Gutiérrez-Fandiño and Jordi Armengol-Estapé and Marc Pàmies and Joan Llop-Palao and Joaquin Silveira-Ocampo and Casimiro Pio Carrino and Carme Armentano-Oller and Carlos Rodriguez-Penagos and Aitor Gonzalez-Agirre and Marta Villegas},
	title = {MarIA: Spanish Language Models},
	journal = {Procesamiento del Lenguaje Natural},
	volume = {68},
	number = {0},
	year = {2022},
	issn = {1989-7553},
	url = {http://journal.sepln.org/sepln/ojs/ojs/index.php/pln/article/view/6405},
	pages = {39--60}
}
```

### Contributions 

[N/A]
