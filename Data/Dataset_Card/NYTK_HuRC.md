---
YAML tags:
annotations_creators:
- crowdsourced
language_creators:
- found
- expert-generated
language:
- hu
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: HuRC
size_categories:
- unknown
source_datasets:
- extended|other
task_categories:
- question-answering
task_ids:
- extractive-qa
- abstractive-qa
---

# Dataset Card for HuRC
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
- **Homepage:**
- **Repository:**
[HuRC dataset](https://github.com/nytud/HuRC)
- **Paper:**
- **Leaderboard:**
- **Point of Contact:**
[lnnoemi](mailto:ligeti-nagy.noemi@nytud.hu)

### Dataset Summary

This is the dataset card for the Hungarian Corpus for Reading Comprehension with Commonsense Reasoning (HuRC), which is also part of the Hungarian Language Understanding Evaluation Benchmark Kit HuLU.
The dataset contains 80 614 instances. Each instance is composed of a lead, a passage and a cloze-style query with a masked entity. The task is to select the named entity that is being masked in the query.
The data was automatically collected from the online news of Népszabadság online (nol.hu).

### Languages

The BCP-47 code for Hungarian, the only represented language in this dataset, is hu-HU. 

## Dataset Structure

### Data Instances

For each instance, there is an id, a lead, a passage, a query and a MASK. 
An example:
```
{
 "id": "1",
 "lead": ["A Közigazgatási és Igazságügyi Minisztérium szerint a Bárka Színház esetében felmerült a felelőtlen gazdálkodás gyanúja, egyes értesülések szerint pedig ebben    \"a színház igazgatójának és gazdasági vezetőjének felelőssége is felmerül\""],
 "passage": [
            "A teátrumnak Navracsics Tibor közigazgatási és igazságügyi miniszterhez és Kocsis Máté VIII. kerületi polgármesterhez",
            "reagálva a tárca azt írta, hogy a felelőtlen gazdálkodás gyanújában \"egyes értesülések szerint a színház igazgatójának és gazdasági vezetőjének felelőssége is felmerül\". A KIM \"éppen ezért nagyon várja az Állami Számvevőszék készülő jelentését, hogy tiszta képet kaphasson a színház működéséről\".",
            "A minisztérium hangsúlyozta, hogy az elmúlt évben is mindent elkövetett azért, hogy a Bárka Színház \"valós, rangos művészeti térként\" működjön, és a továbbiakban is ez a szándéka, de jelenleg a társulat működtetését a minisztérium fenntartói támogatás formájában jogszerűen még nem tudja megoldani.",
            "A teátrum az átadás-átvétel elhúzódásának okát keresve tette közzé nyílt levelét, amelyben elmaradó fizetésekre, előadásokra és bemutatókra hívta fel a figyelmet, és jelezte, hogy várja a helyzet megoldását.",
            "A színház átadás-átvétele jelenleg zajlik, a folyamat végeztével a Bárka a józsefvárosi önkormányzattól állami tulajdonba, a tervek szerint a Közigazgatási és Igazságügyi Minisztérium fenntartásába kerül."
        ],
"query": "A KIM 2014-es költségvetésében szerepel a Bárka Színház, de amíg nem a minisztérium a [MASK] fenntartója, addig ez a költségvetési keret nem nyitható meg.",
"MASK": "Bárka",
}
```

### Data Fields

- id: unique id of the instances;
- lead: a short summary of the article as it was extracted from the source texts;
- passage: 3-6 paragraphs of texts as the body of the article;
- query: the last paragraph of an article, some kind of summary or conclusion, with a named entity masked (with [MASK]) in it;
- MASK: the masked named entity. 

### Data Splits
HuRC has 3 splits: *train*, *validation* and *test*. 

| Dataset split | Number of instances in the split | Proportion of the split
|---------------|----------------------------------| ---------|
| train         | 64614                              | 80%|
| validation    | 8000                             |10%|
| test          | 8000                              |10%|

The test data is distributed without the MASK fields. To evaluate your model, please [contact us](mailto:ligeti-nagy.noemi@nytud.hu), or check [HuLU's website](hulu.nlp.nytud.hu) for an automatic evaluation (this feature is under construction at the moment).  

## Dataset Creation

### Source Data

#### Initial Data Collection and Normalization

To produce the Hungarian material, we used the daily articles from Népszabadság Online which had titles and summaries as well. We selected 3-6 paragraphs from each article from the ones which contain proper nouns both in the main part and the summary as well. We trained a NER model using huBERT (Nemeskey 2021) for recognizing proper nouns. NerKor (Simon és Vadász 2021) and Huggingface’s token-level classification library were used to fine-tune the model. Our model achieved an F-score of 90.18 on the test material. As a final step, we found pairs of proper names which are present both in the main article and the summary. Multiple articles contained more than one such pairs so we used those more than once. This resulted in a database of 88655 instances (from 49782 articles). 

The quantitative properties of our corpus are as follows: Number of articles: 88655 Number of different articles (type): 49782 Token: 27703631 Type: 1115.260 Average length of text (token): 249.42 (median: 229) Average question length (token): 63.07 (median: 56). We fine-tuned the corpus by hand.

One annotator per 100 unit checked and validated the dataset for which we provided our own demo interface. Automatic masking and the previous occurrence of the entity was checked. This resulted in a database of 80 614 validated entries.

## Additional Information

### Licensing Information

HuRC is released under the cc-by-4.0 license.

### Citation Information

If you use this resource or any part of its documentation, please refer to:

Ligeti-Nagy, N., Ferenczi, G., Héja, E., Jelencsik-Mátyus, K., Laki, L. J., Vadász, N., Yang, Z. Gy. and Váradi, T. (2022) HuLU: magyar nyelvű benchmark adatbázis kiépítése a neurális nyelvmodellek kiértékelése céljából [HuLU: Hungarian benchmark dataset to evaluate neural language models]. XVIII. Magyar Számítógépes Nyelvészeti Konferencia. (in press)

```

@inproceedings{ligetinagy2022hulu,
  title={HuLU: magyar nyelvű benchmark adatbázis kiépítése a neurális nyelvmodellek kiértékelése céljából},
  author={Ligeti-Nagy, N. and Ferenczi, G. and Héja, E. and Jelencsik-Mátyus, K. and Laki, L. J. and Vadász, N. and Yang, Z. Gy. and Váradi, T.},
  booktitle={XVIII. Magyar Számítógépes Nyelvészeti Konferencia},
  year={2022}
}
```


### Contributions

Thanks to [lnnoemi](https://github.com/lnnoemi) for adding this dataset.