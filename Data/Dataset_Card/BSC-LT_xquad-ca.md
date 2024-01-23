---
language:
- ca
---
# XQuAD-Ca

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

## Digital Object Identifier (DOI) and access to dataset files

https://doi.org/10.5281/zenodo.4526224


## Introduction

Professional translation into Catalan of XQuAD dataset (https://github.com/deepmind/xquad).

XQuAD (Cross-lingual Question Answering Dataset) is a benchmark dataset for evaluating cross-lingual question answering performance. The dataset consists of a subset of 240 paragraphs and 1190 question-answer pairs from the development set of SQuAD v1.1 (Rajpurkar et al., 2016) together with their professional translations into ten languages: Spanish, German, Greek, Russian, Turkish, Arabic, Vietnamese, Thai, Chinese, and Hindi. Rumanian was added later. We added the 13th language to the corpus using also professional native catalan translators.

XQuAD and XQuAD-Ca datasets are released under [CC-by-sa] (https://creativecommons.org/licenses/by-sa/3.0/legalcode) licence. 

### Supported Tasks and Leaderboards

Cross-lingual-QA, Extractive-QA, Language Model

### Languages

CA- Catalan

### Directory structure

* README.md
* .gitattributes
* test.json - json-formatted file with the dataset
* xquad-ca.py

## Dataset Structure

### Data Instances

One json file

### Data Fields

Follows ((Rajpurkar, Pranav et al., 2016) for SQuAD v1 datasets. (see below for full reference)

### Example:
<pre>
{
  "data": [
    {
    
          "context": "Al llarg de la seva existència, Varsòvia ha estat una ciutat multicultural. Segons el cens del 1901, de 711.988 habitants, el 56,2 % eren catòlics, el 35,7 % jueus, el 5 % cristians ortodoxos grecs i el 2,8 % protestants. Vuit anys després, el 1909, hi havia 281.754 jueus (36,9 %), 18.189 protestants (2,4 %) i 2.818 mariavites (0,4 %). Això va provocar que es construïssin centenars de llocs de culte religiós a totes les parts de la ciutat. La majoria d’ells es van destruir després de la insurrecció de Varsòvia del 1944. Després de la guerra, les noves autoritats comunistes de Polònia van apocar la construcció d’esglésies i només se’n va construir un petit nombre.",
          "qas": [
            
            {
              "answers": [
                {
                  "text": "711.988",
                  "answer_start": 104
                }
              ],
              "id": "57338007d058e614000b5bdb",
              "question": "Quina era la població de Varsòvia l’any 1901?"
            },
            {
              "answers": [
                {
                  "text": "56,2 %",
                  "answer_start": 126
                }
              ],
              "id": "57338007d058e614000b5bdc",
              "question": "Dels habitants de Varsòvia l’any 1901, quin percentatge era catòlic?"
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

One

## Dataset Creation

### Methodology

For more information on how XQuAD was created, refer to the paper, On the Cross-lingual Transferability of Monolingual Representations (https://arxiv.org/abs/1910.11856), or visit the webpage https://github.com/deepmind/xquad

Translation into Catalan was commissioned by BSC TeMU within the AINA project. 

### Curation Rationale

For compatibility with similar datasets in other languages, and to allow inter-lingual comparisons. 

### Source Data

- https://github.com/deepmind/xquad

#### Initial Data Collection and Normalization

Professional translation of XQuAD into Catalan

#### Who are the source language producers?

For more information on how XQuAD was created, refer to the paper, On the Cross-lingual Transferability of Monolingual Representations (https://arxiv.org/abs/1910.11856), or visit the webpage https://github.com/deepmind/xquad

### Annotations

#### Annotation process

None

#### Who are the annotators?

Translation whas commisioned to a professional translation company.

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