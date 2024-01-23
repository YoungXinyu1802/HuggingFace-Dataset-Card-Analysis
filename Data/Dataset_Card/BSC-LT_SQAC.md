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
size_categories:
- unknown
source_datasets:
- original
task_categories:
- question-answering
task_ids:
- extractive-qa

---

**⚠️NOTICE⚠️: THIS MODEL HAS BEEN MOVED TO THE FOLLOWING URL AND WILL SOON BE REMOVED:** https://huggingface.co/datasets/PlanTL-GOB-ES/SQAC

# SQAC (Spanish Question-Answering Corpus): An extractive QA dataset for the Spanish language

## BibTeX  citation

```bibtex
@article{DBLP:journals/corr/abs-2107-07253,
  author    = {Asier Guti{\'{e}}rrez{-}Fandi{\~{n}}o and
               Jordi Armengol{-}Estap{\'{e}} and
               Marc P{\`{a}}mies and
               Joan Llop{-}Palao and
               Joaqu{\'{\i}}n Silveira{-}Ocampo and
               Casimiro Pio Carrino and
               Aitor Gonzalez{-}Agirre and
               Carme Armentano{-}Oller and
               Carlos Rodr{\'{\i}}guez Penagos and
               Marta Villegas},
  title     = {Spanish Language Models},
  journal   = {CoRR},
  volume    = {abs/2107.07253},
  year      = {2021},
  url       = {https://arxiv.org/abs/2107.07253},
  archivePrefix = {arXiv},
  eprint    = {2107.07253},
  timestamp = {Wed, 21 Jul 2021 15:55:35 +0200},
  biburl    = {https://dblp.org/rec/journals/corr/abs-2107-07253.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```

See the pre-print version of our paper for further details: https://arxiv.org/abs/2107.07253

<!-- ## Digital Object Identifier (DOI) and access to dataset files --> 


## Introduction

This dataset contains 6,247 contexts and 18,817 questions with their answers, 1 to 5 for each fragment.

The sources of the contexts are:
* Encyclopedic articles from [Wikipedia in Spanish](https://es.wikipedia.org/), used under [CC-by-sa licence](https://creativecommons.org/licenses/by-sa/3.0/legalcode). 
* News from [Wikinews in Spanish](https://es.wikinews.org/), used under [CC-by licence](https://creativecommons.org/licenses/by/2.5/). 
* Text from the Spanish corpus [AnCora](http://clic.ub.edu/corpus/en), which is a mix from diferent newswire and literature sources, used under [CC-by licence](https://creativecommons.org/licenses/by/4.0/legalcode). 

This dataset can be used to build extractive-QA.

### Supported Tasks and Leaderboards

Extractive-QA

### Languages

ES - Spanish

### Directory structure

* README.md
* dev.json
* test.json
* train.json
* sqac.py

## Dataset Structure

### Data Instances

JSON files

### Data Fields

Follows (Rajpurkar, Pranav et al., 2016) for squad v1 datasets. (see below for full reference).
We added a field "source" with the source of the context.

### Example
<pre>
{
  "data": [
    {
      "paragraphs": [
        {
          "context": "Al cogote, y fumando como una cafetera. Ah!, no era él, éramos todos nosotros. Luego llegó Billie Holiday. Bajo el epígrafe Arte, la noche temática, pasaron la vida de la única cantante del universo que no es su voz, sino su alma lo que se escucha cuando interpreta. Gata golpeada por el mundo, pateada, violada, enganchada a todos los paraísos artificiales del planeta, jamás encontró el Edén. El Edén lo encontramos nosotros cuando, al concluir la sesión de la tele, pusimos en la doméstica cadena de sonido el mítico Last Recording, su última grabación (marzo de 1959), con la orquesta de Ray Ellis y el piano de Hank Jones. Se estaba muriendo Lady Day, y no obstante, mientras moría, su alma cantaba, Baby, won't you please come home. O sea, niño, criatura, amor, vuelve, a casa por favor.",
          "qas": [
            {
              "question": "¿Quién se incorporó a la reunión más adelante?",
              "id": "c5429572-64b8-4c5d-9553-826f867b07be",
              "answers": [
                {
                  "answer_start": 91,
                  "text": "Billie Holiday"
                }
              ]
            },
            
            ...
            
            ]
        }
      ],
      "title": "P_129_20010702_&_P_154_20010102_&_P_108_20000301_c_&_P_108_20000601_d",
      "source": "ancora"
    },
    ...
  ]
}

</pre>

### Data Splits

- train
- development
- test

## Content analysis

### Number of articles, paragraphs and questions

* Number of articles: 3,834
* Number of contexts: 6,247
* Number of questions: 18,817
* Questions/context: 3.01
* Number of sentences: 48,026
* Sentences/context: 7.70

### Number of tokens

* Total tokens in context: 1,561,616
* Tokens/context 250.30
* Total tokens in questions: 203,235
* Tokens in questions/questions: 10.80
* Tokens in questions/tokens in context: 0.13
* Total tokens in answers: 90,307
* Tokens in answers/answers: 4.80
* Tokens in answers/tokens in context: 0.06

### Lexical variation

46.38 of the words in the Question can be found in the Context.

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

### Methodology

6,247 contexts were randomly chosen from the three corpus described below. We commisioned the creation of between 1 and 5 questions for each context, following an adaptation of the guidelines from SQUAD 1.0 [Rajpurkar, Pranav et al. “SQuAD: 100, 000+ Questions for Machine Comprehension of Text.” EMNLP (2016)](http://arxiv.org/abs/1606.05250). In total, 18,817 pairs of a question and an extracted fragment that contains the answer were created.


### Curation Rationale

For compatibility with similar datasets in other languages, we followed as close as possible existing curation guidelines. We also created another QA dataset with Wikipedia to ensure thematic and stylistic variety.

### Source Data

- Spanish Wikipedia: https://es.wikipedia.org
- Spanish Wikinews: https://es.wikinews.org/
- AnCora corpus: http://clic.ub.edu/corpus/en

#### Initial Data Collection and Normalization

The source data are scraped articles from the Spanish Wikipedia site, Wikinews site and from AnCora corpus.

#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

We commissioned the creation of 1 to 5 questions for each context, following an adaptation of the guidelines from SQUAD 1.0 [Rajpurkar, Pranav et al. “SQuAD: 100, 000+ Questions for Machine Comprehension of Text.” EMNLP (2016)](http://arxiv.org/abs/1606.05250).


#### Who are the annotators?

Native language speakers.

### Dataset Curators

Carlos Rodríguez and Carme Armentano, from BSC-CNS.

### Personal and Sensitive Information

No personal or sensitive information included.

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Contact

Carlos Rodríguez-Penagos or Carme Armentano-Oller (bsc-temu@bsc.es)

## Funding
This work was partially funded by the Spanish State Secretariat for Digitalization and Artificial Intelligence (SEDIA) within the framework of the Plan-TL.

## License

<a rel="license" href="https://creativecommons.org/licenses/by-sa/4.0/"><img alt="Attribution-ShareAlike 4.0 International License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="https://creativecommons.org/licenses/by-sa/4.0/">Attribution-ShareAlike 4.0 International License</a>.
