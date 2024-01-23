---
annotations_creators:
- expert-generated
language_creators:
- found
language:
- ca
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: ancora-ca-ner
size_categories:
- unknown
source_datasets: []
task_categories: []
task_ids: []
---

# Dataset Card for AnCora-Ca-NER
 
## Dataset Description

- **Website:** https://zenodo.org/record/5036651
- **Paper:** [Are Multilingual Models the Best Choice for Moderately Under-resourced Languages? A Comprehensive Assessment for Catalan](https://arxiv.org/abs/2107.07903)
- **Paper:** [AnCora: Multilevel Annotated Corpora for Catalan and Spanish](http://www.lrec-conf.org/proceedings/lrec2008/pdf/35_paper.pdf)
- **Point of Contact:** [Carlos Rodríguez-Penagos](carlos.rodriguez1@bsc.es) and [Carme Armentano-Oller](carme.armentano@bsc.es)

### Dataset Summary

This is a dataset for Named Entity Recognition (NER) in Catalan. It adapts <a href="http://clic.ub.edu/corpus/">AnCora corpus</a> for Machine Learning and Language Model evaluation purposes.

[AnCora corpus](http://clic.ub.edu/corpus/) is used under [CC-by](https://creativecommons.org/licenses/by/4.0/) licence. 

This dataset was developed by [BSC TeMU](https://temu.bsc.es/) as part of the [Projecte AINA](https://politiquesdigitals.gencat.cat/ca/economia/catalonia-ai/aina/), to enrich the [Catalan Language Understanding Benchmark (CLUB)](https://club.aina.bsc.es/).


### Supported Tasks and Leaderboards

Named Entities Recognition, Language Model

### Languages

The dataset is in Catalan (`ca-CA`).

## Dataset Structure

### Data Instances

Three two-column files, one for each split. 

<pre>
    Fundació B-ORG
    Privada I-ORG
    Fira I-ORG
    de I-ORG
    Manresa I-ORG
    ha O
    fet O
    un O
    balanç O
    de O
    l' O
    activitat O
    del O
    Palau B-LOC
    Firal I-LOC
</pre>

### Data Fields

Every file has two columns, with the word form or punctuation symbol in the first one and the corresponding IOB tag in the second one.

### Data Splits

We took the original train, dev and test splits from the [UD version of the corpus](https://huggingface.co/datasets/universal_dependencies)

- train: 10,630 examples
- validation: 1,429 examples
- test: 1,528 examples


## Dataset Creation

### Curation Rationale

We created this corpus to contribute to the development of language models in Catalan, a low-resource language.

### Source Data

#### Initial Data Collection and Normalization

[AnCora](http://clic.ub.edu/corpus/) consists of a Catalan corpus (AnCora-CA) and a Spanish corpus (AnCora-ES), each of them of 500,000 tokens (some multi-word). The corpora are annotated for linguistic phenomena at different levels.
AnCora corpus is mainly based on newswire texts. For more information, refer to Taulé, M., M.A. Martí, M. Recasens (2009): <a href="http://www.lrec-conf.org/proceedings/lrec2008/pdf/35_paper.pdf">"AnCora: Multilevel Annotated Corpora for Catalan and Spanish”</a>, Proceedings of 6th International Conference on language Resources and Evaluation.

#### Who are the source language producers?

Catalan [AnCora corpus](http://clic.ub.edu/corpus/) is compiled from articles from the following news outlets: <a href="https://www.efe.com">EFE</a>, <a href="https://www.acn.cat">ACN</a>, <a href="https://www.elperiodico.cat/ca/">El Periodico</a>.

### Annotations

#### Annotation process

We adapted the NER labels from [AnCora corpus](http://clic.ub.edu/corpus/) to a token-per-line, multi-column format. 

#### Who are the annotators?

Original annotators from [AnCora corpus](http://clic.ub.edu/corpus/).

### Personal and Sensitive Information

No personal or sensitive information included.

## Considerations for Using the Data

### Social Impact of Dataset

We hope this corpus contributes to the development of language models in Catalan, a low-resource language.

### Discussion of Biases

[N/A]

### Other Known Limitations

[N/A]

## Additional Information
### Dataset Curators

Text Mining Unit (TeMU) at the Barcelona Supercomputing Center (bsc-temu@bsc.es)

This work was funded by the [Departament de la Vicepresidència i de Polítiques Digitals i Territori de la Generalitat de Catalunya](https://politiquesdigitals.gencat.cat/en/inici/index.html) within the framework of [Projecte AINA](https://politiquesdigitals.gencat.cat/ca/economia/catalonia-ai/aina/).

### Licensing information

This work is licensed under a <a rel="license" href="https://creativecommons.org/licenses/by/4.0/">Attribution 4.0 International License</a>.

### Citation Information

```
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


[DOI](https://doi.org/10.5281/zenodo.4529299)


### Contributions

[N/A]