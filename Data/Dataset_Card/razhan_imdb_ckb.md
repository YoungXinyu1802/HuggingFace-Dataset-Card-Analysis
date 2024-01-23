---
annotations_creators:
- expert-generated
language:
- ckb
- ku
language_creators:
- crowdsourced
license:
- other
multilinguality:
- monolingual
pretty_name: IMDB_CKB
size_categories:
- 10K<n<100K
source_datasets:
- extended|imdb
tags:
- central kurdish
- kurdish
- sorani
- kurdi
task_categories:
- text-classification
task_ids:
- sentiment-analysis
- sentiment-classification
dataset_info:
  features:
    - name: text
      dtype: string
    - name: label
      dtype:
        class_label:
          names:
            '0': neg
            '1': pos
  config_name: plain_text
  splits:
    - name: train
      num_examples: 24903
    - name: test
      num_examples: 24692
---

# Dataset Card for IMDB Kurdish

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

- **Homepage:** [http://ai.stanford.edu/~amaas/data/sentiment/](http://ai.stanford.edu/~amaas/data/sentiment/)
- **Repository:** [https://github.com/Hrazhan/IMDB_Kurdish/](https://github.com/Hrazhan/IMDB_Kurdish/)
- **Point of Contact:** [Razhan Hameed](https://twitter.com/RazhanHameed)
- **Paper:**
- **Leaderboard:**

### Dataset Summary

Central Kurdish translation of the famous IMDB movie reviews dataset.

The dataset contains 50K highly polar movie reviews, divided into two equal classes of positive and negative reviews. We can perform binary sentiment classification using this dataset. 
The availability of datasets in Kurdish, such as the IMDB movie reviews dataset, can help researchers and developers train and evaluate machine learning models for Kurdish language processing.
However, it is important to note that machine learning algorithms can only be as accurate as the data they are trained on (in this case the quality of the translation), so the quality and relevance of the dataset will affect the performance of the resulting model.
For more information about the dataset, please go through the following link: http://ai.stanford.edu/~amaas/data/sentiment/

P.S. This dataset is translated with Google Translator.

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

Central Kurdish

## Dataset Structure

### Data Instances

An example of 'train' looks as follows.
```
{
    "label": 0,
    "text": ""فیلمێکی زۆر باش، کە سەرنج دەخاتە سەر پرسێکی زۆر گرنگ. نەخۆشی کحولی کۆرپەلە کەموکوڕییەکی زۆر جددی لە لەدایکبوونە کە بە تەواوی دەتوانرێت ڕێگری لێبکرێت. ئەگەر خێزانە زیاترەکان ئەم فیلمە ببینن، ڕەنگە منداڵی زیاتر وەک ئادەم کۆتاییان نەهاتبێت. جیمی سمیس لە یەکێک لە باشترین ڕۆڵەکانیدا نمایش دەکات تا ئێستا. ئەمە فیلمێکی نایاب و باشە کە خێزانێکی زۆر تایبەت لەبەرچاو دەگرێت و پێویستییەکی زۆر گرنگی هەیە. ئەمەش جیاواز نییە لە هەزاران خێزان کە ئەمڕۆ لە ئەمریکا هەن. منداڵان هەن کە لەگەڵ ئەم جیهانەدا خەبات دەکەن. بەڕاستی خاڵە گرنگەکە لێرەدا ئەوەیە کە دەکرا ڕێگری لە هەموو شتێک بکرێت. خەڵکی زیاتر دەبێ ئەم فیلمە ببینن و ئەوەی کە هەیەتی بە جددی وەریبگرێت. بە باشی ئەنجام دراوە، بە پەیامی گرنگ، بە شێوەیەکی بەڕێزانە مامەڵەی لەگەڵ دەکرێت."
}
```

### Data Fields


plain_text

    text: a string feature.
    label: a classification label, with possible values including neg (0), pos (1).


### Data Splits

|   name   |train|test|
|----------|----:|----:|
|plain_text|24903|24692|

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

[More Information Needed]

### Licensing Information

[More Information Needed]

### Citation Information

```
@InProceedings{maas-EtAl:2011:ACL-HLT2011,
  author    = {Maas, Andrew L.  and  Daly, Raymond E.  and  Pham, Peter T.  and  Huang, Dan  and  Ng, Andrew Y.  and  Potts, Christopher},
  title     = {Learning Word Vectors for Sentiment Analysis},
  booktitle = {Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics: Human Language Technologies},
  month     = {June},
  year      = {2011},
  address   = {Portland, Oregon, USA},
  publisher = {Association for Computational Linguistics},
  pages     = {142--150},
  url       = {http://www.aclweb.org/anthology/P11-1015}
}

```

### Contributions

Thanks to [Razhan Hameed](https://twitter.com/RazhanHameed) for adding this dataset.
