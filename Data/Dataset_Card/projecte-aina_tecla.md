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
pretty_name: tecla
size_categories:
- unknown
source_datasets: []
task_categories:
- text-classification
task_ids:
- multi-class-classification
---

# Dataset Card for TeCla 

## Dataset Description

- **Website:** [Zenodo](https://zenodo.org/record/7334110)
- **Point of Contact:** [Irene Baucells de la Peña](irene.baucells@bsc.es), [Carlos Rodríguez-Penagos](carlos.rodriguez1@bsc.es) and [Carme Armentano-Oller](carme.armentano@bsc.es)



### Dataset Summary

TeCla (Text Classification) is a Catalan News corpus for thematic multi-class Text Classification tasks. The present version (2.0) contains 113.376 articles classified under a hierarchical class structure consisting of a coarse-grained and a fine-grained class. Each of the 4 coarse-grained classes accept a subset of fine-grained ones, 53 in total. 

The previous version (1.0.1) can still be found at https://zenodo.org/record/4761505

This dataset was developed by [BSC TeMU](https://temu.bsc.es/) as part of [Projecte AINA](https://politiquesdigitals.gencat.cat/ca/economia/catalonia-ai/aina/), to enrich the [Catalan Language Understanding Benchmark (CLUB)](https://club.aina.bsc.es/).

### Supported Tasks and Leaderboards

Text classification, Language Model

### Languages

The dataset is in Catalan (`ca-CA`).

## Dataset Structure

### Data Instances

Three json files, one for each split.

### Data Fields

Each example contains the following 3 fields: 
* text: the article text (string)
* label1: the coarse-grained class
* label2: the fine-grained class

#### Example:

<pre>
{"version": "2.0",
 "data":
   [
    {
     'sentence': "La setena edició del Festival Fantàstik inclourà les cintes 'Matar a dios' i 'Mandy' i un homenatge a 'Mi vecino Totoro'. Es projectaran 22 curtmetratges seleccionats d'entre més de 500 presentats a nivell internacional. El Centre Cultural de Granollers acull del 8 a l'11 de novembre la setena edició del Festival Fantàstik. El certamen, que s'allargarà un dia, arrencarà amb la projecció de la cinta de Caye Casas i Albert Pide 'Matar a Dios'. Els dos directors estaran presents en la inauguració de la cita. A més, els asssitents podran gaudir de 'Mandy', el darrer treball de Nicolas Cage. Altres llargmetratges seleccionats per aquest any són 'Aterrados' (2017), 'Revenge' (2017), 'A Mata Negra' (2018), 'Top Knot Detective' (2018) i 'La Gran Desfeta' (2018). A més, amb motiu del trentè aniversari de la pel·lícula 'El meu veí Totoro' es durà a terme l'exposició dedicada a aquest film '30 anys 30 artistes' comissariada per Jordi Pastor i Reinaldo Pereira. La mostra '30 anys 30 artistes' recull els treballs de trenta artistes d'estils diferents al voltant de la figura de Totoro i el seu director. Es podrà veure durant els dies de festival i es complementarà amb la projecció de la pel·lícula el diumenge 11 de novembre. Al llarg del festival també es projectaran els 22 curtmetratges prèviament seleccionats d'entre més de 500 presentats a nivell internacional. El millor tindrà una dotació de 1000 euros fruit de la unió de forces amb el Mercat Audiovisual de Catalunya.", 
    'label1': 'Cultura',
    'label2': 'Cinema'
    },
    ...
  ]
}


</pre>

#### Labels

* label1: 'Societat', 'Política', 'Economia', 'Cultura'
* label2: 'Llengua', 'Infraestructures', 'Arts', 'Parlament', 'Noves tecnologies', 'Castells', 'Successos', 'Empresa', 'Mobilitat', 'Teatre', 'Treball', 'Logística', 'Urbanisme', 'Govern', 'Entitats', 'Finances', 'Govern espanyol', 'Trànsit', 'Indústria', 'Esports', 'Exteriors', 'Medi ambient', 'Habitatge', 'Salut', 'Equipaments i patrimoni', 'Recerca', 'Cooperació', 'Innovació', 'Agroalimentació', 'Policial', 'Serveis Socials', 'Cinema', 'Memòria històrica', 'Turisme', 'Política municipal', 'Comerç', 'Universitats', 'Hisenda', 'Judicial', 'Partits', 'Música', 'Lletres', 'Religió', 'Festa i cultura popular', 'Unió Europea', 'Moda', 'Moviments socials', 'Comptes públics', 'Immigració', 'Educació', 'Gastronomia', 'Meteorologia', 'Energia'

### Data Splits

Train, development and test splits were created in a stratified fashion, following a 0.8, 0.05 and 0.15 proportion, respectively. The sizes of each split are the following:
* train.json: 90700 examples
* dev.json: 5669 examples
* test.json: 17007 examples

## Dataset Creation

### Curation Rationale

We created this dataset to contribute to the development of language models in Catalan, a low-resource language.

### Source Data

#### Initial Data Collection and Normalization

The source data are crawled articles from the Catalan News Agency ([Agència Catalana de Notícies, ACN](https://www.acn.cat/)) site.

We crawled 219.586 articles from the Catalan News Agency ([Agència Catalana de Notícies; ACN](https://www.acn.cat/)) newswire archive, the latest from October 11, 2020.

From the crawled data, we selected those articles whose 'section' and 'subsection' categories followed the expected codification combinations included in the ACN's style guide and whose 'section' complied the requirements of containing subsections and being thematically founded (in contrast to geographically defined categories such as 'Món' and 'Unió Europea'). The articles originally belonging to the 'Unió Europea' section, which were related to political organisms from the European Union, were included in the 'Política' coarse-grained category (within a fine-grained category named 'Unió Europea') due to its close proximity between some of the original subsections of 'Política' and those of 'Unió Europea', both defined by the specific political organism dealt with in the article.   

The text field in each example is a concatenation of the original title, subtitle and body of the article (before the concatenation, both title and subtitle were added a final dot whenever they lacked one). The preprocessing of the texts was minimal and consisted in the removal of the pattern "ACN {location}.-" included before the body in each text as well as newlines originally used to divide the text in paragraphs.


#### Who are the source language producers?

The Catalan News Agency ([Agència Catalana de Notícies; ACN](https://www.acn.cat/)) is a news agency owned by the Catalan government via the public corporation Intracatalònia, SA. It is one of the first digital news agencies created in Europe and has been operating since 1999 (source: [wikipedia](https://en.wikipedia.org/wiki/Catalan_News_Agency)).

### Annotations

#### Annotation process

The crawled data contained the categories' annotations, which were then used to create this dataset with the mentioned criteria.

#### Who are the annotators?

Editorial staff classified the articles under the different thematic sections and subsections, and we extracted these from metadata.

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

Irene Baucells (irene.baucells@bsc.es), Casimiro Pio Carrino (casimiro.carrino@bsc.es), Carlos Rodríguez (carlos.rodriguez1@bsc.es) and Carme Armentano (carme.armentano@bsc.es), from [BSC-CNS](https://www.bsc.es/).

This work was funded by the [Departament de la Vicepresidència i de Polítiques Digitals i Territori de la Generalitat de Catalunya](https://politiquesdigitals.gencat.cat/ca/inici/index.html#googtrans(ca|en) within the framework of [Projecte AINA](https://politiquesdigitals.gencat.cat/ca/economia/catalonia-ai/aina).


### Licensing Information

This work is licensed under a <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/">Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.

### Citation Information

[DOI]([https://doi.org/10.5281/zenodo.7334110])

