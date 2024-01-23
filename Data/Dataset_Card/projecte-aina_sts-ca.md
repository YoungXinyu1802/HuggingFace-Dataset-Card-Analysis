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
size_categories:
- unknown
source_datasets: []
task_categories:
- text-classification
task_ids:
- semantic-similarity-scoring
- text-scoring
pretty_name: sts-ca
---

# Dataset Card for STS-ca

## Dataset Description
- **Website:** https://zenodo.org/record/4761434

- **Paper:** [Are Multilingual Models the Best Choice for Moderately Under-resourced Languages? A Comprehensive Assessment for Catalan](https://arxiv.org/abs/2107.07903)

- **Point of Contact:** [Carlos Rodríguez-Penagos](carlos.rodriguez1@bsc.es) and [Carme Armentano-Oller](carme.armentano@bsc.es)



### Dataset Summary

STS-ca corpus is a benchmark for evaluating Semantic Text Similarity in Catalan. This dataset was developed by [BSC TeMU](https://temu.bsc.es/) as part of [Projecte AINA](https://politiquesdigitals.gencat.cat/ca/economia/catalonia-ai/aina/), to enrich the [Catalan Language Understanding Benchmark (CLUB)](https://club.aina.bsc.es/).


### Supported Tasks and Leaderboards

This dataset can be used to build and score semantic similarity models in Catalan.

### Languages

The dataset is in Catalan (`ca-CA`).

## Dataset Structure

### Data Instances

Follows [SemEval challenges](https://www.aclweb.org/anthology/S13-1004.pdf):
* index (int)
* id (str): Unique ID assigned to the sentence pair.
* sentence 1 (str): First sentence of the pair.
* sentence 2 (str): Second sentence of the pair.
* avg (float): Gold truth

#### Example

 |  index  |  id  |  sentence 1  |  sentence 2  |  avg  | 
 | ------- | ---- | ------------ | ------------ | ----- | 
| 19 | ACN2_131 | Els manifestants ocupen l'Imperial Tarraco durant una hora fent jocs de taula | Els manifestants ocupen l'Imperial Tarraco i fan jocs de taula | 4 |
| 21 | TE2_80 | El festival comptarà amb cinc escenaris i se celebrarà entre el 7 i el 9 de juliol al Parc del Fòrum. | El festival se celebrarà el 7 i 8 de juliol al Parc del Fòrum de Barcelona | 3 |
| 23 | Oscar2_609 | Aleshores hi posarem un got de vi i continuarem amb la cocció fins que s'hagi evaporat el vi i ho salpebrarem. | Mentre, hi posarem el vi al sofregit i deixarem coure uns 7/8′, fins que el vi s'evapori. | 3 |
| 25 | Viqui2_48 | L'arboç grec (Arbutus andrachne) és un arbust o un petit arbre dins la família ericàcia. | El ginjoler ("Ziziphus jujuba") és un arbust o arbre petit de la família de les "Rhamnaceae". | 2.75 |
| 27 | ACN2_1072 | Mentre han estat davant la comandància, els manifestants han cridat consignes a favor de la independència i han cantat cançons com 'L'estaca'. | Entre les consignes que han cridat s'ha pogut escoltar càntics com 'els carrers seran sempre nostres' i contínues consignes en favor de la independència. | 3 |
| 28 | Viqui2_587 | Els cinc municipis ocupen una superfície de poc més de 100 km2 i conjuntament sumen una població total aproximada de 3.691 habitants (any 2019). | Té una població d'1.811.177 habitants (2005) repartits en 104 municipis d'una superfície total de 14.001 km2. | 2.67 |


### Data Fields

This dataset follows [SemEval](https://www.aclweb.org/anthology/S13-1004.pdf) challenges formats and conventions.

### Data Splits

- sts_cat_dev_v1.tsv (500 annotated pairs)

- sts_cat_train_v1.tsv (2073 annotated pairs)

- sts_cat_test_v1.tsv (500 annotated pairs)

## Dataset Creation

### Curation Rationale

We created this dataset to contribute to the development of language models in Catalan, a low-resource language.

### Source Data

#### Initial Data Collection and Normalization

Random sentences were extracted from 3 Catalan subcorpus from the [Catalan Textual Corpus](https://zenodo.org/record/4519349#.Ys_0PexBzOs): [ACN](https://www.acn.cat/), [Oscar](https://oscar-corpus.com/) and [Wikipedia](https://ca.wikipedia.org/wiki/Portada).

We generated candidate pairs using a combination of metrics from Doc2Vec, Jaccard and a BERT-like model (“[distiluse-base-multilingual-cased-v2](https://huggingface.co/distilbert-base-multilingual-cased)”). Finally, we  manually reviewed the generated pairs to reject non-relevant pairs (identical or ungrammatical sentences, etc.) before providing them to the annotation team.

The average of the four annotations was selected as a “ground truth” for each sentence pair, except when an annotator diverged in more than one unit from the average. In these cases, we discarded the divergent annotation and recalculated the average without it. We also discarded 45 sentence pairs because the annotators disagreed too much.

For compatibility with similar datasets in other languages, we followed as close as possible existing curation guidelines.

#### Who are the source language producers?

The [Catalan Textual Corpus](https://zenodo.org/record/4519349#.Ys_0PexBzOs) is a 1760-million-token web corpus of Catalan built from several sources: existing corpus such as DOGC, CaWac (non-deduplicated version), Oscar (unshuffled version), Open Subtitles, Catalan Wikipedia; and three brand new crawlings: the Catalan General Crawling, obtained by crawling the 500 most popular .cat and .ad domains; the Catalan Government Crawling, obtained by crawling the .gencat domain and subdomains, belonging to the Catalan Government; and the ACN corpus with 220k news items from March 2015 until October 2020, crawled from the Catalan News Agency.

### Annotations

#### Annotation process

We comissioned the manual annotation of the similarity between the sentences of each pair, following the provided guidelines.

#### Who are the annotators?

A team of native language speakers from 2 different companies, working independently.

### Personal and Sensitive Information

No personal or sensitive information included.

## Considerations for Using the Data

### Social Impact of Dataset

We hope this dataset contributes to the development of language models in Catalan, a low-resource language.

### Discussion of Biases

[N/A]

### Other Known Limitations

[N/A]

## Additional Information

### Dataset Curators

Text Mining Unit (TeMU) at the Barcelona Supercomputing Center (bsc-temu@bsc.es)

This work was funded by the [Departament de la Vicepresidència i de Polítiques Digitals i Territori de la Generalitat de Catalunya](https://politiquesdigitals.gencat.cat/en/inici/index.html) within the framework of [Projecte AINA](https://politiquesdigitals.gencat.cat/ca/economia/catalonia-ai/aina/).

### Licensing Information

This work is licensed under a <a rel="license" href="https://creativecommons.org/licenses/by-sa/4.0/">Attribution-ShareAlike 4.0 International License</a>.

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

[DOI](https://doi.org/10.5281/zenodo.4529183)

### Contributions

[N/A]

