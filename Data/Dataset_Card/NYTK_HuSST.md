---
YAML tags:
annotations_creators:
- found
language_creators:
- found
- expert-generated
language:
- hu
license:
- bsd-2-clause
multilinguality:
- monolingual
pretty_name: HuSST
size_categories:
- unknown
source_datasets:
- extended|other
task_categories:
- text-classification
- text-scoring
task_ids:
- sentiment-classification
- sentiment-scoring
---

# Dataset Card for HuSST

## Table of Contents

- [Table of Contents](#table-of-contents)

- [Dataset Description](#dataset-description)

  - [Dataset Summary](#dataset-summary)

  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)

  - [Language](#language)

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
[HuSST dataset](https://github.com/nytud/HuSST)
- **Paper:**
- **Leaderboard:**
- **Point of Contact:**
[lnnoemi](mailto:ligeti-nagy.noemi@nytud.hu)

### Dataset Summary

This is the dataset card for the Hungarian version of the Stanford Sentiment Treebank. This dataset which is also part of the Hungarian Language Understanding Evaluation Benchmark Kit [HuLU](hulu.nlp.nytud.hu). The corpus was created by translating and re-annotating the original SST (Roemmele et al., 2011).

### Supported Tasks and Leaderboards

'sentiment classification'


'sentiment scoring'

### Language

The BCP-47 code for Hungarian, the only represented language in this dataset, is hu-HU. 

## Dataset Structure

### Data Instances

For each instance, there is an id, a sentence and a sentiment label.

An example:

```
{
"Sent_id": "dev_0",
"Sent": "Nos, a Jason elment Manhattanbe és a Pokolba kapcsán, azt hiszem, az elkerülhetetlen folytatások ötletlistájáról kihúzhatunk egy űrállomást 2455-ben (hé, ne lődd   le a poént).",
"Label": "neutral"
 }

```

### Data Fields

- Sent_id: unique id of the instances;

- Sent: the sentence, translation of an instance of the SST dataset;

- Label: "negative", "neutral", or "positive".

### Data Splits

HuSST has 3 splits: *train*, *validation* and *test*. 

| Dataset split | Number of instances in the split |
|---------------|----------------------------------|
| train         | 9344                              |
| validation    | 1168                              |
| test          | 1168                              |

The test data is distributed without the labels. To evaluate your model, please [contact us](mailto:ligeti-nagy.noemi@nytud.hu), or check [HuLU's website](hulu.nlp.nytud.hu) for an automatic evaluation (this feature is under construction at the moment). 

## Dataset Creation

### Source Data

#### Initial Data Collection and Normalization

The data is a translation of the content of the SST dataset (only the whole sentences were used). Each sentence was translated by a human translator. Each translation was manually checked and further refined by another annotator. 

### Annotations

#### Annotation process

The translated sentences were annotated by three human annotators with one of the following labels: negative, neutral and positive. Each sentence was then curated by a fourth annotator (the 'curator'). The final label is the decision of the curator based on the three labels of the annotators.

#### Who are the annotators?

The translators were native Hungarian speakers with English proficiency. The annotators were university students with some linguistic background. 

## Additional Information

### Licensing Information


### Citation Information

If you use this resource or any part of its documentation, please refer to:

Ligeti-Nagy, N., Ferenczi, G., Héja, E., Jelencsik-Mátyus, K., Laki, L. J., Vadász, N., Yang, Z. Gy. and Vadász, T. (2022) HuLU: magyar nyelvű benchmark adatbázis
kiépítése a neurális nyelvmodellek kiértékelése céljából [HuLU: Hungarian benchmark dataset to evaluate neural language models]. XVIII. Magyar Számítógépes Nyelvészeti Konferencia. pp. 431–446.

```

@inproceedings{ligetinagy2022hulu,
  title={HuLU: magyar nyelvű benchmark adatbázis kiépítése a neurális nyelvmodellek kiértékelése céljából},
  author={Ligeti-Nagy, N. and Ferenczi, G. and Héja, E. and Jelencsik-Mátyus, K. and Laki, L. J. and Vadász, N. and Yang, Z. Gy. and Vadász, T.},
  booktitle={XVIII. Magyar Számítógépes Nyelvészeti Konferencia},
  year={2022},
  pages = {431--446}
}

```

and to:

Socher et al. (2013), Recursive Deep Models for Semantic Compositionality Over a Sentiment Treebank. In: Proceedings of the 2013 Conference on Empirical Methods in Natural Language Processing. 1631--1642.

```

@inproceedings{socher-etal-2013-recursive,
    title = "Recursive Deep Models for Semantic Compositionality Over a Sentiment Treebank",
    author = "Socher, Richard  and
      Perelygin, Alex  and
      Wu, Jean  and
      Chuang, Jason  and
      Manning, Christopher D.  and
      Ng, Andrew  and
      Potts, Christopher",
    booktitle = "Proceedings of the 2013 Conference on Empirical Methods in Natural Language Processing",
    month = oct,
    year = "2013",
    address = "Seattle, Washington, USA",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/D13-1170",
    pages = "1631--1642",
}

```

### Contributions

Thanks to [lnnoemi](https://github.com/lnnoemi) for adding this dataset.