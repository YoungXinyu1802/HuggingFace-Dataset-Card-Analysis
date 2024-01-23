---
language:
- ca
---

# Named Entites from Ancora Corpus

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

https://doi.org/10.5281/zenodo.4529299


## Introduction

This is a dataset for Named Entity Recognition (NER) from <a href="http://clic.ub.edu/corpus/">Ancora corpus</a> adapted for Machine Learning and Language Model evaluation purposes.

Since multiwords (including Named Entities) in the original Ancora corpus are aggregated as a single lexical item using underscores (e.g. "Ajuntament_de_Barcelona") we splitted them to align with word-per-line format, and added conventional <a href="https://en.wikipedia.org/wiki/Inside%E2%80%93outside%E2%80%93beginning_(tagging)">Begin-Inside-Outside (IOB) tags</a> to mark and classify Named Entities. We did not filter out the different categories of NEs from Ancora (weak and strong). We did 6 minor edits by hand.

AnCora corpus is used under [CC-by] (https://creativecommons.org/licenses/by/4.0/) licence. 

This dataset was developed by BSC TeMU as part of the AINA project, and to enrich the Catalan Language Understanding Benchmark (CLUB). 

### Supported Tasks and Leaderboards

Named Entities Recognition, Language Model

### Languages

CA- Catalan

### Directory structure
 
* dev.txt
* test.txt
* train.txt


## Dataset Structure

### Data Instances

three two-column files, one for each split.

### Data Fields

Every file has two columns, with the word form or punctuation symbol in the first one and the corresponding IOB tag in the second one.

### Example:
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

### Data Splits

One for each sub-dataset for train, evaluation and test.

## Dataset Creation

### Methodology

We adapted the NER labels from Ancora corpus to a word-per-line format. 
Since multiwords in the original Ancora corpus are aggregated as a single lexical item using underscores (e.g. "Ajuntament_de_Barcelona") we splitted them to align with this format, and added conventional <a href="https://en.wikipedia.org/wiki/Inside%E2%80%93outside%E2%80%93beginning_(tagging)">Begin-Inside-Outside (IOB) tags</a> to mark and classify Named Entities. We did not filter out the different categories of NEs from Ancora (weak and strong). We did 6 minor edits by hand.

### Curation Rationale

### Source Data

#### Initial Data Collection and Normalization

AnCora consists of a Catalan corpus (AnCora-CA) and a Spanish corpus (AnCora-ES), each of them of 500,000 tokens (some multi-word). The corpora are annotated for linguistic phenomena at different levels.
AnCora corpus is mainly based on newswire texts. For more information, refer to Taulé, M., M.A. Martí, M. Recasens (2009). “AnCora: Multilevel Annotated Corpora for Catalan and Spanish”, Proceedings of 6th International Conference on language Resources and Evaluation. http://www.lrec-conf.org/proceedings/lrec2008/pdf/35_paper.pdf

#### Who are the source language producers?

Catalan Ancora corpus is compiled from articles from the following news outlets: <a href="https://www.efe.com">EFE</a>, <a href="https://www.acn.cat">ACN</a>, <a href="https://www.elperiodico.cat/ca/">El Periodico</a>.

### Annotations

#### Annotation process

We adapted the NER labels from Ancora corpus to a token-per-line, multi-column format. 

#### Who are the annotators?

Original annotators from Ancora corpus.


### Dataset Curators

Carlos Rodríguez and Carme Armentano, from BSC-CNS, did the conversion and curation.

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

<a rel="license" href="https://creativecommons.org/licenses/by/4.0/"><img alt="Attribution 4.0 International License" style="border-width:0" src="https://chriszabriskie.com/img/cc-by.png" width="100"/></a><br />This work is licensed under a <a rel="license" href="https://creativecommons.org/licenses/by/4.0/">Attribution 4.0 International License</a>.


