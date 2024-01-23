---
language:
- ca
---
# TeCla (Text Classification) Catalan dataset

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

https://doi.org/10.5281/zenodo.4627198


## Introduction

TeCla is a Catalan News corpus for thematic Text Classification tasks. It contains 153.265 articles classified under 30 different categories.

The source data is crawled from the ACN (Catalan News Agency) site: [http://www.acn.cat], and used under CC-BY-NC-ND 4.0 licence. The dataset is released under the same licence, and is intended exclusively for training Machine Learning models.

This dataset was developed by BSC TeMU as part of the AINA project, and intended as part of CLUB (Catalan Language Understanding Benchmark). It is part of the Catalan Language Understanding Benchmark (CLUB) as presented in: 

Armengol-Estapé J., Carrino CP., Rodriguez-Penagos C., de Gibert Bonet O., Armentano-Oller C., Gonzalez-Agirre A., Melero M. and Villegas M.,Are Multilingual Models the Best Choice for Moderately Under-resourced Languages? A Comprehensive Assessment for Catalan". Findings of ACL 2021 (ACL-IJCNLP 2021).


### Supported Tasks and Leaderboards

Text classification, Language Model

### Languages

CA- Catalan

### Directory structure

* **.gitattributes**
* **README.md**
* **dev.json** - json-formatted file with the dev split of the dataset
* **tecla.py**
* **test.json** - json-formatted file with the test split of the dataset
* **train.json** - json-formatted file with the train split of the dataset

## Dataset Structure

### Data Instances

Three json files, one for each split.

### Data Fields

We used a simple model with the article text and associated labels, without further metadata.

### Example:

<pre>
{"version": "1.0",
 "data":
   [
    {
     'sentence': 'L\\\\'editorial valenciana Media Vaca, Premi Nacional a la Millor Tasca Editorial Cultural del 2018. El jurat en destaca la cura "exquisida" del catàleg, la qualitat dels llibres i el "respecte" pels lectors. ACN Madrid.-L\\\\'editorial valenciana Media Vaca ha obtingut el Premi Nacional a la Millor Labor Editorial Cultural corresponent a l\\\\'any 2018 que atorga el Ministeri de Cultura i Esports. El guardó pretén distingir la tasca editorial d\\\\'una persona física o jurídica que hagi destacat per l\\\\'aportació a la vida cultural espanyola. El premi és de caràcter honorífic i no té dotació econòmica. En el cas de Media Vaca, fundada pel valencià Vicente Ferrer i la bilbaïna Begoña Lobo, el jurat n\\\\'ha destacat la cura "exquisida" del catàleg, la qualitat dels llibres i el "respecte" pels lectors i per la resta d\\\\'agents de la cadena del llibre. Media Vaca va publicar els primers llibres el desembre del 1998. El catàleg actual el componen 64 títols dividits en sis col·leccions, que barregen ficció i no ficció. Des del Ministeri de Cultura es destaca que la il·lustració té un pes "fonamental" als productes de l\\\\'editorial i que la majoria de projectes solen partir de propostes literàries i textos preexistents. L\\\\'editorial ha rebut quatre vegades el Bologna Ragazzi Award. És l\\\\'única editorial estatal que ha aconseguit el guardó que atorga la Fira del Llibre per a Nens de Bolonya, la més important del sector.', 
    'label': 'Lletres'
    },
    .
    .
    .
  ]
}


</pre>

### Data Splits
* train.json: 122587 article-label pairs
* dev.json: 15339  article-label pairs
* test.json: 15339  article-label pairs

### Labels

'Societat', 'Política', 'Turisme', 'Salut', 'Economia', 'Successos', 'Partits', 'Educació', 'Policial', 'Medi ambient', 'Parlament', 'Empresa', 'Judicial', 'Unió Europea', 'Comerç', 'Cultura', 'Cinema', 'Govern', 'Lletres', 'Infraestructures', 'Música', 'Festa i cultura popular', 'Teatre', 'Mobilitat', 'Govern espanyol', 'Equipaments i patrimoni', 'Meteorologia', 'Treball', 'Trànsit', 'Món'


### Labels in the dataset by frequency

train.json: 122587 articles

| Label | Num art |% art |
|:-----------------------|--------------:|------: |
| Societat | 24975 | 20.37% |
| Política | 18344 | 14.96% |
| Partits | 10056 | 8.2% |
| Successos | 7874 | 6.42% |
| Judicial | 5788 | 4.72% |
| Policial | 5557 | 4.53% |
| Salut | 5430 | 4.43% |
| Economia | 5032 | 4.1% |
| Parlament | 4176 | 3.41% |
| Medi_ambient | 3027 | 2.47% |
| Música | 2872 | 2.34% |
| Educació | 2757 | 2.25% |
| Empresa | 2698 | 2.2% |
| Cultura | 2495 | 2.04% |
| Unió_Europea | 2064 | 1.68% |
| Govern | 2039 | 1.66% |
| Infraestructures | 1740 | 1.42% |
| Treball | 1655 | 1.35% |
| Mobilitat | 1624 | 1.32% |
| Cinema | 1560 | 1.27% |
| Teatre | 1492 | 1.22% |
| Turisme | 1232 | 1.01% |
| Equipaments_i_patrimoni | 1229 | 1.0% |
| Lletres | 1180 | 0.96% |
| Meteorologia | 1080 | 0.88% |
| Comerç | 984 | 0.8% |
| Govern_espanyol | 983 | 0.8% |
| Món | 893 | 0.73% |
| Festa_i_cultura_popular | 888 | 0.72% |
| Trànsit | 863 | 0.7% |

dev.json and test.json: 153265 articles each split

| Label | Num art |% art |
|:----------------------- | --------------:| ------: |
| Societat | 3122 | 20.35% |
| Política | 2294 | 14.96% |
| Partits | 1257 | 8.19% |
| Successos | 985 | 6.42% |
| Judicial | 724 | 4.72% |
| Policial | 695 | 4.53% |
| Salut | 679 | 4.43% |
| Economia | 630 | 4.11% |
| Parlament | 523 | 3.41% |
| Medi_ambient | 379 | 2.47% |
| Música | 359 | 2.34% |
| Educació | 345 | 2.25% |
| Empresa | 338 | 2.2% |
| Cultura | 312 | 2.03% |
| Unió_Europea | 258 | 1.68% |
| Govern | 256 | 1.67% |
| Infraestructures | 218 | 1.42% |
| Treball | 208 | 1.36% |
| Mobilitat | 204 | 1.33% |
| Cinema | 195 | 1.27% |
| Teatre | 187 | 1.22% |
| Turisme | 154 | 1.0% |
| Equipaments_i_patrimoni | 154 | 1.0% |
| Lletres | 148 | 0.96% |
| Meteorologia | 135 | 0.88% |
| Govern_espanyol | 124 | 0.81% |
| Comerç | 123 | 0.8% |
| Festa_i_cultura_popular | 112 | 0.73% |
| Món | 112 | 0.73% |
| Trànsit | 109 | 0.71% |


## Dataset Creation

### Methodology

We crawled 219.586 articles from the Catalan News Agency (www.acn.cat) newswire archive, the latest from October 11, 2020.
We used the "subsection" category as a classification label, after excluding territorial labels (see territorial_labels.txt file) and labels with less than 2000 occurrences. With this criteria compiled a total of 153.265 articles for this text classification dataset.

### Curation Rationale

We used the "subsection" category as a classification label, after excluding territorial labels (see territorial_labels.txt file) and labels with less than 2000 occurrences.

### Source Data

#### Initial Data Collection and Normalization

The source data are crawled articles from ACN (Catalan News Agency) site: www.acn.cat

#### Who are the source language producers?

The Catalan News Agency (CNA, in Catalan: Agència Catalana de Notícies (ACN)) is a news agency owned by the Catalan government via the public corporation Intracatalònia, SA. It is one of the first digital news agencies created in Europe and has been operating since 1999 (source: [https://en.wikipedia.org/wiki/Catalan_News_Agency])

### Annotations

#### Annotation process

We used the "subsection" category as a classification label, after excluding territorial labels (see territorial_labels.txt file) and labels with less than 2000 occurrences.

#### Who are the annotators?

Editorial staff classified the articles under the different thematic sections, and we extracted these from metadata.

### Dataset Curators

Casimiro Pio Carrino, Carlos Rodríguez and Carme Armentano, from BSC-CNS

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

<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Attribution-NonCommercial-NoDerivatives 4.0 International License" style="border-width:0" src="http://d2klr1ixr44jla.cloudfront.net/306/125/0.5-0.5/assets/images/55132bfeb13b7b027c000041.png" width="100"/></a><br />This work is licensed under a <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/">Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.

