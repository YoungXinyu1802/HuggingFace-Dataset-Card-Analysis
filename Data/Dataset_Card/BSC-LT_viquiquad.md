---
language:
- ca
---
# ViquiQuAD, An extractive QA dataset for catalan, from the Wikipedia

## BibTeX  citation

If you use any of these resources (datasets or models) in your work, please cite our latest paper:

```bibtex
@inproceedings{armengol-estape-etal-2021-multilingual,
    title = "Are Multilingual Models the Best Choice for Moderately Under-resourced Languages? {A} Comprehensive Assessment for {C}atalan",
    author = "Armengol-Estap{\'e}, Jordi  and
      Carrino, Casimiro Pio  and
      Rodriguez-Penagos, Carlos  and
      de Gibert Bonet, Ona  and
      Armentano-Oller, Carme  and
      Gonzalez-Agirre, Aitor  and
      Melero, Maite  and
      Villegas, Marta",
    booktitle = "Findings of the Association for Computational Linguistics: ACL-IJCNLP 2021",
    month = aug,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.findings-acl.437",
    doi = "10.18653/v1/2021.findings-acl.437",
    pages = "4933--4946",
}
```


# Digital Object Identifier (DOI) and access to dataset files

https://doi.org/10.5281/zenodo.4562345


## Introduction

This dataset contains 3111 contexts extracted from a set of 597 high quality original (no translations) articles in the Catalan Wikipedia "Viquipèdia" (ca.wikipedia.org), and 1 to 5 questions with their answer for each fragment.

Viquipedia articles are used under [CC-by-sa] (https://creativecommons.org/licenses/by-sa/3.0/legalcode) licence. 

This dataset can be used to fine-tune and evaluate extractive-QA and Language Models. It is part of the Catalan Language Understanding Benchmark (CLUB) as presented in: 

Armengol-Estapé J., Carrino CP., Rodriguez-Penagos C., de Gibert Bonet O., Armentano-Oller C., Gonzalez-Agirre A., Melero M. and Villegas M.,Are Multilingual Models the Best Choice for Moderately Under-resourced Languages? A Comprehensive Assessment for Catalan". Findings of ACL 2021 (ACL-IJCNLP 2021).

### Supported Tasks and Leaderboards

Extractive-QA, Language Model

### Languages

CA- Catalan

### Directory structure

* README
* dev.json
* test.json
* train.json
* viquiquad.py

## Dataset Structure

### Data Instances

json files

### Data Fields

Follows ((Rajpurkar, Pranav et al., 2016) for squad v1 datasets. (see below for full reference)

### Example:
<pre>
{
  "data": [
    {
      "title": "Frederick W. Mote",
      "paragraphs": [
        {
          "context": "L'historiador Frederick W. Mote va escriure que l'ús del terme \\\\\\\\\\\\\\\\"classes socials\\\\\\\\\\\\\\\\" per a aquest sistema era enganyós i que la posició de les persones dins del sistema de quatre classes no era una indicació del seu poder social i riquesa reals, sinó que només implicava \\\\\\\\\\\\\\\\"graus de privilegi\\\\\\\\\\\\\\\\" als quals tenien dret institucionalment i legalment, de manera que la posició d'una persona dins de les classes no era una garantia de la seva posició, ja que hi havia xinesos rics i amb bona reputació social, però alhora hi havia menys mongols i semu rics que mongols i semu que vivien en la pobresa i eren maltractats.",
          "qas": [
            {
              "answers": [
                {
                  "text": "Frederick W. Mote",
                  "answer_start": 14
                }
              ],
              "id": "5728848cff5b5019007da298",
              "question": "Qui creia que el sistema de classes socials de Yuan no s’hauria d’anomenar classes socials?"
            },
            ...
          ]
        }
      ]
    }, 
    ...
   ]
} 

</pre>

### Data Splits

train.development,test

## Content analysis

### Number of articles, paragraphs and questions

* Number of articles: 597
* Number of contexts: 3111
* Number of questions: 15153
* Questions/context: 4.87
* Number of sentences in contexts: 15100
* Sentences/context: 4.85

### Number of tokens

* tokens in context: 469335
* tokens/context 150.86
* tokens in questions: 145249
* tokens/questions: 9.58
* tokens in answers: 63246
* tokens/answers: 4.17

### Lexical variation

After filtering (tokenization, stopwords, punctuation, case), 83,88% of the words in the question can be found in the Context

### Question type 

| Question | Count | % |
|--------|-----|------|
| què |  4220 | 27.85 % |
| qui |  2239 | 14.78 % |
| com |  1964 | 12.96 % |
| quan |  1133 | 7.48 % |
| on |  1580 | 10.43 % |
| quant |  925 | 6.1 % |
| quin |  3399 | 22.43 % |
| no question mark | 21 | 0.14 % |

### Question-answer relationships

From 100 randomly selected samples:

* Lexical variation: 33.0%
* World knowledge: 16.0%
* Syntactic variation: 35.0%
* Multiple sentence: 17.0%

## Dataset Creation

### Methodology

From a set of high quality, non-translation, articles in the Catalan Wikipedia (ca.wikipedia.org), 597 were randomly chosen, and from them 3111, 5-8 sentence contexts were extracted. We commissioned creation of between 1 and 5 questions for each context, following an adaptation of the guidelines from SQUAD 1.0 [Rajpurkar, Pranav et al. “SQuAD: 100, 000+ Questions for Machine Comprehension of Text.” EMNLP (2016)], (http://arxiv.org/abs/1606.05250). In total, 15153 pairs of a question and an extracted fragment that contains the answer were created.

### Curation Rationale

For compatibility with similar datasets in other languages, we followed as close as possible existing curation guidelines. 

### Source Data

- https://ca.wikipedia.org

#### Initial Data Collection and Normalization

The source data are scraped articles from the Catalan wikipedia site (https://ca.wikipedia.org). 

#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

We commissioned the creation of 1 to 5 questions for each context, following an adaptation of the guidelines from SQUAD 1.0 (Rajpurkar, Pranav et al. “SQuAD: 100, 000+ Questions for Machine Comprehension of Text.” EMNLP (2016)), http://arxiv.org/abs/1606.05250.

#### Who are the annotators?

Native language speakers.

### Dataset Curators

Carlos Rodríguez and Carme Armentano, from BSC-CNS

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


## License

<a rel="license" href="https://creativecommons.org/licenses/by-sa/4.0/"><img alt="Attribution-ShareAlike 4.0 International License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="https://creativecommons.org/licenses/by-sa/4.0/">Attribution-ShareAlike 4.0 International License</a>.
