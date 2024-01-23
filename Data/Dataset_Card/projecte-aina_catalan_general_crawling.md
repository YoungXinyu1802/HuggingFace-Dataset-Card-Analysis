---
annotations_creators:
- no-annotation
language_creators:
- found
language:
- ca
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: Catalan General Crawling
size_categories:
- 1M<n<10M
source_datasets:
- original
task_categories:
- fill-mask
task_ids: []
---

# Dataset Card for Catalan General Crawling

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Homepage:** https://zenodo.org/record/5483031
- **Paper:** [Are Multilingual Models the Best Choice for Moderately Under-resourced Languages? A Comprehensive Assessment for Catalan](https://arxiv.org/abs/2107.07903)
- **Point of Contact:** [ona.degibert@bsc.es](ona.degibert@bsc.es)

### Dataset Summary

The Catalan General Crawling Corpus is a 435-million-token web corpus of Catalan built from the web. It has been obtained by crawling the 500 most popular .cat and .ad domains during July 2020. It consists of 434,817,705 tokens, 19,451,691 sentences and 1,016,114 documents. Documents are separated by single new lines. It is a subcorpus of the Catalan Textual Corpus.

### Supported Tasks and Leaderboards

This corpus is mainly intended to pretrain language models and word representations.

### Languages

The dataset is in Catalan (`ca-CA`).

## Dataset Structure

### Data Instances

```
{
  'text': 'Reduïu els costos dels processos administratius al vostre organisme públic\nEviteu els desplaçaments i pèrdua de temps als ciutadans en les seves gestions\nOferiu una administració més transparent a
 ciutadans i empreses\nEns grans i petits experimenten aquesta transformació amb èxit, gràcies al suport de l\'AOC\nDepartament de Sistemes d\'Informació i Processos\n" Via Oberta ens ha permès fer efectiu el d
ret dels ciutadans a no aportar documents, eliminant paper i simplificant procediments"\n" e.FACT proporciona informació indispensable per a la realització de les auditories del registre comptable de factures d
e les Administracions Públiques Catalanes"\nCoordinador del departament d\'Informàtica\n"El servei VIA OBERTA és el que ha aportat majors avantatges per als ciutadans"\n"Amb l\' e-NOTUM hem escurçat els procedi
ments en 12 dies, quasi un 40% menys!"\nCoordinadora d\'organització de persones i e-administració\n" Via Oberta ofereix millores per als ciutadans al no haver d\'aportar cap document"\nResponsable d\'Informàti
ca i Administració Electrònica\n" e-TRAM ens ha permès implantar un servei de tramitació electrònica per als ciutadans de forma ràpida, senzilla i amb un cost reduït"\n"Els municipis amb pocs habitants trobem e
n els serveis de l\'AOC la gratuïtat i la comoditat necessàries per dur a terme el nostre dia a dia"\n"Les T-CAT han permès incorporar de forma segura la signatura electrònica dins dels nostres procediments afa
vorint la transformació digital de la nostra activitat"\nCap de Departament de Sistemes i Tecnologies de la Informació\n"Amb el desplegament de l\' idCAT hem apropat l\'Ajuntament a la ciutadania"\n"Mitjançant
els serveis de Govern Obert de l\'AOC hem pogut fer fàcil el que sembla difícil"\n"Al tauler electrònic pots penjar fins i tot el projecte sencer i al final et permet fer també la diligència"\nÀrea de Promoció
Econòmica, Administració i Hisenda\n"El Sobre Digital i la PSCP han aconseguit una comunió senzilla entre empreses i administració per universalitzar la compra pública electrònica"\n"L\' e-SET és la implantació
 d\'un nou sistema de treball que facilita la feina del dia a dia"\nCap del servei de contractació i compres\n"El Sobre Digital, una experiència imprescindible per a la bona administració amb estalvi de recurso
s i millora de la seguretat jurídica i la transparència"\nÀrea d\'Organització i Administració Electrònica\n"El desplegament de la valisa electrònica ha estat clau en el procés de transformació digital dels nos
tres procediments interns"\n"L\' Hèstia permet el treball en temps real i des de qualsevol lloc, així com sistematitzar la pràctica professional, recollir la informació ordenadament i amb el mateix llenguatge"\
nConsulta els materials del Congrés de Govern Digital 2019\nGoverns transparents, fluids, dinàmics, líquids... un bon lema pel principal objectiu de la governança del segle XXI: democratitzar-ho tot.\nConfluènc
ies, rius, cooperació.\nCatalunya, Mediterrània, mar de drets.\nA favor: totes les Administracions movent-se per posar-se al dia i millorar, tot aprofitant la revolució digital.\nEn contra: quants cops estem re
inventant la roda i quantes quantes oportunitats perdudes de fer-ho una única vegada i de forma coordinada i col·laborativa?\n"La transparència és una oportunitat.\nHem de perdre tota por a explicar què fem": l
a conclusió de la taula d\'alcaldies de la Jornada de Govern Obert pic.twitter.com/ERbgLSIXZM\nEl director general de Participació Ciutadana ens convida a transformar les administracions públiques a partir de l
a participació ciutadana\nEns cal que allò que preocupa i ocupa els governants formi part d\'allò en què participa la ciutadania pic.twitter.com/NwQr4EZSCS: "A moltes institucions encara els sona xinés això de
les dades obertes i la transparència.\nDe que serveix que hi hagi un portal, si llavors no hi ha dades?\nLlavors l\'accés a la informació pels periodistes és molt parcial".\nOferim eines que, conjuntament amb l
a metodologia i el suport necessari, fan possible l\'assoliment d\'un govern digital\nPosem al vostre abast tot el coneixement: formació, guies, normatives, etc.\nTenim eines per gestionar àgilment part del pro
cés administratiu del vostre ens\nEl nostre equip farà tot el possible per resoldre les vostres incidències\nSabem que es tracta d\'una decisió molt important per al vostre ens i és per això que us ho volem pos
ar fàcil.\nLa selecció de l\'actualitat d\'Administració Oberta a la vostra safata.'
}
```

### Data Fields

- `text` (str): Text.

### Data Splits

The dataset contains a single split: `train`.

## Dataset Creation

### Curation Rationale

We created this corpus to contribute to the development of language models in Catalan, a low-resource language.

### Source Data

#### Initial Data Collection and Normalization

The corpus has been obtained by crawling the 500 most popular .cat and .ad domains during July 2020.
For preprocessing we used [Corpus-Cleaner](https://github.com/TeMU-BSC/corpus-cleaner-acl), a modular Python-based toolkit to clean raw text corpora through generator pipelines.

#### Who are the source language producers?

The data comes from multiple web pages in Catalan.

### Annotations

The dataset is unannotated.

#### Annotation process

[N/A]

#### Who are the annotators?

[N/A]

### Personal and Sensitive Information

Since all data comes from public websites, no anonymisation process was performed.

## Considerations for Using the Data

### Social Impact of Dataset

We hope this corpus contributes to the development of language models in Catalan, a low-resource language.

### Discussion of Biases

We are aware that since the data comes from unreliable web pages, some biases may be present in the dataset. Nonetheless, we have not applied any steps to reduce their impact.

### Other Known Limitations

[N/A]

## Additional Information

### Dataset Curators

Text Mining Unit (TeMU) at the Barcelona Supercomputing Center (bsc-temu@bsc.es)

This work was funded by the [Departament de la Vicepresidència i de Polítiques Digitals i Territori de la Generalitat de Catalunya](https://politiquesdigitals.gencat.cat/ca/inici/index.html#googtrans(ca|en) within the framework of [Projecte AINA](https://politiquesdigitals.gencat.cat/ca/economia/catalonia-ai/aina).

### Licensing Information

[Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/).

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
    eprint={2107.07903},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```

### Contributions

Thanks to [@albertvillanova](https://github.com/albertvillanova) for adding this dataset.
