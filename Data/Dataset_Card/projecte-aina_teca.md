---
YAML tags:

annotations_creators:
- expert-generated
language_creators:
- found
language:
- ca
license:
- cc-by-nc-nd-4.0
multilinguality:
- monolingual
pretty_name: teca
size_categories:
- unknown
source_datasets: []
task_categories:
- text-classification
task_ids:
- natural-language-inference

---

# Dataset Card for TE-ca


## Dataset Description

- **Website:** https://zenodo.org/record/4761458

- **Paper:** [Are Multilingual Models the Best Choice for Moderately Under-resourced Languages? A Comprehensive Assessment for Catalan](https://arxiv.org/abs/2107.07903)

- **Point of Contact:** [Carlos Rodríguez-Penagos](carlos.rodriguez1@bsc.es) and [Carme Armentano-Oller](carme.armentano@bsc.es)


### Dataset Summary

TE-ca is a dataset of textual entailment in Catalan, which contains 21,163 pairs of premises and hypotheses, annotated according to the inference relation they have (implication, contradiction or neutral).

This dataset was developed by [BSC TeMU](https://temu.bsc.es/) as part of [Projecte AINA](https://politiquesdigitals.gencat.cat/ca/economia/catalonia-ai/aina/), to enrich the [Catalan Language Understanding Benchmark (CLUB)](https://club.aina.bsc.es/). 

### Supported Tasks and Leaderboards

Textual entailment, Text classification, Language Model

### Languages

The dataset is in Catalan (`ca-CA`).

## Dataset Structure

### Data Instances

Three JSON files, one for each split.

### Example:

<pre>
    
    {
        "id": 3247,
        "premise": "L'ONU adopta a Marràqueix un pacte no vinculant per les migracions",
        "hypothesis": "S'acorden unes recomanacions per les persones migrades a Marràqueix",
        "label": "0"
    },
    {
        "id": 2825,
        "premise": "L'ONU adopta a Marràqueix un pacte no vinculant per les migracions",
        "hypothesis": "Les persones migrades seran acollides a Marràqueix",
        "label": "1"
    },
    {
        "id": 2431,
        "premise": "L'ONU adopta a Marràqueix un pacte no vinculant per les migracions",
        "hypothesis": "L'acord impulsat per l'ONU lluny de tancar-se",
        "label": "2"
    },
</pre>

### Data Fields

- premise: text
- hypothesis: text related to the premise
- label: relation between premise and hypothesis:
    * 0: entailment
    * 1: neutral
    * 2: contradiction
    
### Data Splits

* dev.json: 2116 examples
* test.json: 2117 examples
* train.json: 16930 examples

## Dataset Creation

### Curation Rationale
We created this dataset to contribute to the development of language models in Catalan, a low-resource language.

### Source Data

Source sentences are extracted from the [Catalan Textual Corpus](https://doi.org/10.5281/zenodo.4519349) and from [VilaWeb](https://www.vilaweb.cat) newswire.

#### Initial Data Collection and Normalization

12000 sentences from the BSC [Catalan Textual Corpus](https://doi.org/10.5281/zenodo.4519349), together with 6200 headers from the Catalan news site [VilaWeb](https://www.vilaweb.cat), were chosen randomly. We filtered them by different criteria, such as length and stand-alone intelligibility. For each selected text, we commissioned 3 hypotheses (one for each entailment category) to be written by a team of native annotators. 

Some sentence pairs were excluded because of inconsistencies. 

#### Who are the source language producers?

The Catalan Textual Corpus corpus consists of several corpora gathered from web crawling and public corpora. More information can be found [here](https://doi.org/10.5281/zenodo.4519349).

[VilaWeb](https://www.vilaweb.cat) is a Catalan newswire.

### Annotations

#### Annotation process

We commissioned 3 hypotheses (one for each entailment category) to be written by a team of annotators. 

#### Who are the annotators?

Annotators are a team of native language collaborators from two independent companies.

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

This work was funded by the [Departament de la Vicepresidència i de Polítiques Digitals i Territori de la Generalitat de Catalunya](https://politiquesdigitals.gencat.cat/ca/inici/index.html#googtrans(ca|en) within the framework of [Projecte AINA](https://politiquesdigitals.gencat.cat/ca/economia/catalonia-ai/aina).


### Licensing Information

This work is licensed under an <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/">Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.

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
