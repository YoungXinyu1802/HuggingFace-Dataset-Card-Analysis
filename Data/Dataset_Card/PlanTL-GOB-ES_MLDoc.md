
---
YAML tags:

annotations_creators:
- expert-generated
language:
- es
language_creators:
- found
multilinguality:
- multilingual
pretty_name: MLDoc
license: cc-by-nc-4.0
size_categories: []
source_datasets: []
tags: []
task_categories:
- text-classification
task_ids: []

---


# MLDoc

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
- **Website:** https://github.com/facebookresearch/MLDoc


### Dataset Summary

For document classification, we use the Multilingual Document Classification Corpus (MLDoc) [(Schwenk and Li, 2018)](http://www.lrec-conf.org/proceedings/lrec2018/pdf/658.pdf), a cross-lingual document classification dataset covering 8 languages. We use the Spanish portion to evaluate our models on monolingual classification as part of the EvalEs Spanish language benchmark. The corpus consists of 14,458 news articles from Reuters classified in four categories: Corporate/Industrial, Economics, Government/Social and Markets.

This dataset can't be downloaded straight from HuggingFace as it requires signing specific agreements. The detailed instructions on how to download it can be found in this [repository](https://github.com/facebookresearch/MLDoc).

### Supported Tasks and Leaderboards

Text Classification

### Languages

The dataset is in English, German, French, Spanish, Italian, Russian, Japanese and Chinese. 

## Dataset Structure

### Data Instances

<pre>
MCAT	b' FRANCFORT, 17 feb (Reuter) - La Bolsa de Francfort abri\xc3\xb3 la sesi\xc3\xb3n de corros con baja por la ca\xc3\xadda del viernes en Wall Street y una toma de beneficios.   El d\xc3\xb3lar ayudaba a apuntalar al mercado, que pronto podr\xc3\xada reanudar su tendencia alcista.   Volkswagen bajaba por los da\xc3\xb1os ocasionados por la huelga de camioneros en Espa\xc3\xb1a.   Preussag participaba en un joint venture de exploraci\xc3\xb3n petrol\xc3\xadfera en Filipinas con Atlantic Richfield Co.   A las 0951 GMT, el Dax 30 bajaba 10,49 puntos, un 0,32 pct, a 3.237,69 tras abrir a un m\xc3\xa1ximo de 3.237,69.   (c) Reuters Limited 1997. '
</pre>

### Data Fields

- Label: CCAT (Corporate/Industrial), ECAT (Economics), GCAT (Government/Social) and MCAT (Markets)
- Text

### Data Splits

- train.tsv: 9,458 lines
- valid.tsv: 1,000 lines 
- test.tsv: 4,000 lines 

## Dataset Creation

### Curation Rationale

[N/A] 

### Source Data

The source data is from the Reuters Corpus. In 2000, Reuters Ltd made available a large collection of Reuters News stories for use in research and development of natural language processing, information retrieval, and machine learning systems. This corpus, known as "Reuters Corpus, Volume 1" or RCV1, is significantly larger than the older, well-known Reuters-21578 collection heavily used in the text classification community.

For more information visit the paper [(Lewis et al., 2004)](https://www.jmlr.org/papers/volume5/lewis04a/lewis04a.pdf).

#### Initial Data Collection and Normalization

For more information visit the paper [(Lewis et al., 2004)](https://www.jmlr.org/papers/volume5/lewis04a/lewis04a.pdf).

#### Who are the source language producers?

For more information visit the paper [(Lewis et al., 2004)](https://www.jmlr.org/papers/volume5/lewis04a/lewis04a.pdf).

### Annotations

#### Annotation process

For more information visit the paper [(Schwenk and Li, 2018; Lewis et al., 2004)](http://www.lrec-conf.org/proceedings/lrec2018/pdf/658.pdf).

#### Who are the annotators?

For more information visit the paper [(Schwenk and Li, 2018; Lewis et al., 2004)](http://www.lrec-conf.org/proceedings/lrec2018/pdf/658.pdf).

### Personal and Sensitive Information

[N/A]

## Considerations for Using the Data

### Social Impact of Dataset

This dataset contributes to the development of language models in Spanish.

### Discussion of Biases

[N/A]

### Other Known Limitations

[N/A]

## Additional Information

### Dataset Curators

[N/A]

### Licensing Information

Access to the actual news stories of the Reuters Corpus (both RCV1 and RCV2) requires a NIST agreement. The stories in the Reuters Corpus are under the copyright of Reuters Ltd and/or Thomson Reuters, and their use is governed by the following agreements:
- Organizational agreement: This agreement must be signed by the person responsible for the data at your organization, and sent to NIST.
- Individual agreement: This agreement must be signed by all researchers using the Reuters Corpus at your organization, and kept on file at your organization. 

For more information about the agreement see [here](https://trec.nist.gov/data/reuters/reuters.html)

### Citation Information

The following paper must be cited when using this corpus:

```
@InProceedings{SCHWENK18.658,
  author = {Holger Schwenk and Xian Li},
  title = {A Corpus for Multilingual Document Classification in Eight Languages},
  booktitle = {Proceedings of the Eleventh International Conference on Language Resources and Evaluation (LREC 2018)},
  year = {2018},
  month = {may},
  date = {7-12},
  location = {Miyazaki, Japan},
  editor = {Nicoletta Calzolari (Conference chair) and Khalid Choukri and Christopher Cieri and Thierry Declerck and Sara Goggi and Koiti Hasida and Hitoshi Isahara and Bente Maegaard and Joseph Mariani and Hélène Mazo and Asuncion Moreno and Jan Odijk and Stelios Piperidis and Takenobu Tokunaga},
  publisher = {European Language Resources Association (ELRA)},
  address = {Paris, France},
  isbn = {979-10-95546-00-9},
  language = {english}
  }
  
  @inproceedings{schwenk-li-2018-corpus,
    title = "A Corpus for Multilingual Document Classification in Eight Languages",
    author = "Schwenk, Holger  and
      Li, Xian",
    booktitle = "Proceedings of the Eleventh International Conference on Language Resources and Evaluation ({LREC} 2018)",
    month = may,
    year = "2018",
    address = "Miyazaki, Japan",
    publisher = "European Language Resources Association (ELRA)",
    url = "https://aclanthology.org/L18-1560",
}
  ```



