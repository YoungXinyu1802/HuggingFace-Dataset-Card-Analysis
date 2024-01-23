---
annotations_creators:
- found
language_creators:
- expert-generated
language:
- cs
- de
- en
- et
- fi
- fr
- gu
- iu
- ja
- kk
- km
- lt
- lv
- pl
- ps
- ro
- ru
- ta
- tr
- zh
license:
- unknown
multilinguality:
- multilingual
- translation
size_categories:
- unknown
source_datasets:
- extended|wmt16
- extended|wmt17
- extended|wmt18
- extended|wmt19
- extended|wmt20
task_categories:
- text-generation
- translation
task_ids: []
pretty_name: wmt_vat
tags:
- conditional-text-generation
---

# Dataset Card for Variance-Aware MT Test Sets

## Table of Contents

- [Dataset Card for Variance-Aware MT Test Sets](#dataset-card-for-variance-aware-mt-test-sets)
  - [Table of Contents](#table-of-contents)
  - [Dataset Description](#dataset-description)
    - [Dataset Summary](#dataset-summary)
    - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
      - [Machine Translation](#machine-translation)
    - [Languages](#languages)
  - [Dataset Structure](#dataset-structure)
    - [Data Instances](#data-instances)
    - [Data Fields](#data-fields)
    - [Data Splits](#data-splits)
    - [Dataset Creation](#dataset-creation)
  - [Additional Information](#additional-information)
    - [Dataset Curators](#dataset-curators)
    - [Licensing Information](#licensing-information)
    - [Citation Information](#citation-information)

## Dataset Description

- **Repository:** [Github](https://github.com/NLP2CT/Variance-Aware-MT-Test-Sets)
- **Paper:** [NeurIPS](https://openreview.net/forum?id=hhKA5k0oVy5)
- **Point of Contact:** [Runzhe Zhan](mailto:nlp2ct.runzhe@gmail.com)

### Dataset Summary

This dataset comprises 70 small and discriminative test sets for machine translation (MT) evaluation called variance-aware test sets (VAT), covering 35 translation directions from WMT16 to WMT20 competitions. VAT is automatically created by a novel variance-aware filtering method that filters the indiscriminative test instances of the current MT benchmark without any human labor. Experimental results show that VAT outperforms the original WMT benchmark in terms of the correlation with human judgment across mainstream language pairs and test sets. Further analysis on the properties of VAT reveals the challenging linguistic features (e.g., translation of low-frequency words and proper nouns) for the competitive MT systems, providing guidance for constructing future MT test sets.

**Disclaimer**: *The VAT test sets are hosted through Github by the [Natural Language Processing & Portuguese-Chinese Machine Translation Laboratory (NLP2CT Lab)](http://nlp2ct.cis.um.edu.mo/) of the University of Macau. They were introduced by the paper [Variance-Aware Machine Translation Test Sets](https://openreview.net/forum?id=hhKA5k0oVy5) by [Runzhe Zhan](https://runzhe.me/), [Xuebo Liu](https://sunbowliu.github.io/), [Derek F. Wong](https://www.fst.um.edu.mo/personal/derek-wong/), [Lidia S. Chao](https://aclanthology.org/people/l/lidia-s-chao/) and follow the original licensing for WMT test sets.

### Supported Tasks and Leaderboards

#### Machine Translation

Refer to the [original paper](https://openreview.net/forum?id=hhKA5k0oVy5) for additional details on model evaluation on VAT.

### Languages

The following table taken from the original paper lists the languages supported by the VAT test sets, for a total of 70 language pairs:

| ↔️ | `wmt16` | `wmt17` | `wmt18` | `wmt19` | `wmt20` |
|----------:|:--------|:--------|:--------|--------:|--------:|
| `xx_en` | `cs`,`de`,`fi`, <br /> `ro`,`ru`,`tr` | `cs`,`de`,`fi`,`lv`, <br /> `ru`,`tr`,`zh` | `cs`,`de`,`et`,`fi`, <br /> `ru`,`tr`,`zh` | `de`,`fi`,`gu`, <br /> `kk`,`lt`,`ru`,`zh` | `cs`,`de`,`iu`,`ja`,`km`, <br /> `pl`,`ps`,`ru`,`ta`,`zh`|
| `en_xx` | `ru` | `cs`,`de`,`fi`, <br /> `lv`,`ru`,`tr`,`zh` | `cs`,`de`,`et`,`fi`, <br /> `ru`,`tr`,`zh` | `cs`,`de`,`fi`,`gu`, <br /> `kk`,`lt`,`ru`,`zh` | `cs`,`de`,`ja`,`pl`, <br /> `ru`,`ta`,`zh`|
| `xx_yy`     | / | / | / | `de_cs`,`de_fr`, <br /> `fr_de` | / |

To use any one of the test set, pass `wmtXX_src_tgt` as configuration name to the `load_dataset` command. E.g. to load the English-Russian test set from `wmt16`, use `load_dataset('gsarti/wmt_vat', 'wmt16_en_ru')`.


## Dataset Structure

### Data Instances

A sample from the `test` split (the only available split) for the WMT16 English-Russian language (`wmt16_en_ru` config) is provided below. All configurations have the same structure.

```python
{
	'orig_id': 0,
	'source': 'The social card of residents of Ivanovo region is to be recognised as an electronic payment instrument.',
	'reference': 'Социальная карта жителя Ивановской области признается электронным средством платежа.'
}
```

The text is provided as-in the original dataset, without further preprocessing or tokenization.

### Data Fields

- `orig_id`: Id corresponding to the row id in the original dataset, before variance-aware filtering.
- `source`: The source sentence.
- `reference`: The reference sentence in the target language.

### Data Splits

Taken from the original repository:

| Configuration | # Sentences | # Words | # Vocabulary |
| :-----------: | :--------: | :-----: | :--------------: |
| `wmt20_km_en` |    928     |  17170  |       3645       |
| `wmt20_cs_en` |    266     |  12568  |       3502       |
| `wmt20_en_de` |    567     |  21336  |       5945       |
| `wmt20_ja_en` |    397     |  10526  |       3063       |
| `wmt20_ps_en` |    1088    |  20296  |       4303       |
| `wmt20_en_zh` |    567     |  18224  |       5019       |
| `wmt20_en_ta` |    400     |  7809   |       4028       |
| `wmt20_de_en` |    314     |  16083  |       4046       |
| `wmt20_zh_en` |    800     |  35132  |       6457       |
| `wmt20_en_ja` |    400     |  12718  |       2969       |
| `wmt20_en_cs` |    567     |  16579  |       6391       |
| `wmt20_en_pl` |    400     |  8423   |       3834       |
| `wmt20_en_ru` |    801     |  17446  |       6877       |
| `wmt20_pl_en` |    400     |  7394   |       2399       |
| `wmt20_iu_en` |    1188    |  23494  |       3876       |
| `wmt20_ru_en` |    396     |  6966   |       2330       |
| `wmt20_ta_en` |    399     |  7427   |       2148       |
| `wmt19_zh_en` |    800     |  36739  |       6168       |
| `wmt19_en_cs` |    799     |  15433  |       6111       |
| `wmt19_de_en` |    800     |  15219  |       4222       |
| `wmt19_en_gu` |    399     |  8494   |       3548       |
| `wmt19_fr_de` |    680     |  12616  |       3698       |
| `wmt19_en_zh` |    799     |  20230  |       5547       |
| `wmt19_fi_en` |    798     |  13759  |       3555       |
| `wmt19_en_fi` |    799     |  13303  |       6149       |
| `wmt19_kk_en` |    400     |  9283   |       2584       |
| `wmt19_de_cs` |    799     |  15080  |       6166       |
| `wmt19_lt_en` |    400     |  10474  |       2874       |
| `wmt19_en_lt` |    399     |  7251   |       3364       |
| `wmt19_ru_en` |    800     |  14693  |       3817       |
| `wmt19_en_kk` |    399     |  6411   |       3252       |
| `wmt19_en_ru` |    799     |  16393  |       6125       |
| `wmt19_gu_en` |    406     |  8061   |       2434       |
| `wmt19_de_fr` |    680     |  16181  |       3517       |
| `wmt19_en_de` |    799     |  18946  |       5340       |
| `wmt18_en_cs` |    1193    |  19552  |       7926       |
| `wmt18_cs_en` |    1193    |  23439  |       5453       |
| `wmt18_en_fi` |    1200    |  16239  |       7696       |
| `wmt18_en_tr` |    1200    |  19621  |       8613       |
| `wmt18_en_et` |    800     |  13034  |       6001       |
| `wmt18_ru_en` |    1200    |  26747  |       6045       |
| `wmt18_et_en` |    800     |  20045  |       5045       |
| `wmt18_tr_en` |    1200    |  25689  |       5955       |
| `wmt18_fi_en` |    1200    |  24912  |       5834       |
| `wmt18_zh_en` |    1592    |  42983  |       7985       |
| `wmt18_en_zh` |    1592    |  34796  |       8579       |
| `wmt18_en_ru` |    1200    |  22830  |       8679       |
| `wmt18_de_en` |    1199    |  28275  |       6487       |
| `wmt18_en_de` |    1199    |  25473  |       7130       |
| `wmt17_en_lv` |    800     |  14453  |       6161       |
| `wmt17_zh_en` |    800     |  20590  |       5149       |
| `wmt17_en_tr` |    1203    |  17612  |       7714       |
| `wmt17_lv_en` |    800     |  18653  |       4747       |
| `wmt17_en_de` |    1202    |  22055  |       6463       |
| `wmt17_ru_en` |    1200    |  24807  |       5790       |
| `wmt17_en_fi` |    1201    |  17284  |       7763       |
| `wmt17_tr_en` |    1203    |  23037  |       5387       |
| `wmt17_en_zh` |    800     |  18001  |       5629       |
| `wmt17_en_ru` |    1200    |  22251  |       8761       |
| `wmt17_fi_en` |    1201    |  23791  |       5300       |
| `wmt17_en_cs` |    1202    |  21278  |       8256       |
| `wmt17_de_en` |    1202    |  23838  |       5487       |
| `wmt17_cs_en` |    1202    |  22707  |       5310       |
| `wmt16_tr_en` |    1200    |  19225  |       4823       |
| `wmt16_ru_en` |    1199    |  23010  |       5442       |
| `wmt16_ro_en` |    800     |  16200  |       3968       |
| `wmt16_de_en` |    1200    |  22612  |       5511       |
| `wmt16_en_ru` |    1199    |  20233  |       7872       |
| `wmt16_fi_en` |    1200    |  20744  |       5176       |
| `wmt16_cs_en` |    1200    |  23235  |       5324       |

### Dataset Creation

The dataset was created by retaining a subset of the top 40% instances from various WMT test sets for which the variance between automatic scores (BLEU, BLEURT, COMET, BERTScore) was the highest. Please refer to the original article [Variance-Aware Machine Translation Test Sets](https://openreview.net/forum?id=hhKA5k0oVy5) for additional information on dataset creation.

## Additional Information

### Dataset Curators

The original authors of VAT are the curators of the original dataset. For problems or updates on this 🤗 Datasets version, please contact [gabriele.sarti996@gmail.com](mailto:gabriele.sarti996@gmail.com).

### Licensing Information

The variance-aware test set were created based on the original WMT test set. Thus, the the [original data licensing plan](http://www.statmt.org/wmt20/translation-task.html) already stated by WMT organizers is still applicable:

> The data released for the WMT news translation task can be freely used for research purposes, we just ask that you cite the WMT shared task overview paper, and respect any additional citation requirements on the individual data sets. For other uses of the data, you should consult with original owners of the data sets.

### Citation Information

Please cite the authors if you use these corpora in your work. It is also advised to cite the original WMT shared task paper for the specific test sets that were used.

```bibtex
@inproceedings{
    zhan2021varianceaware,
    title={Variance-Aware Machine Translation Test Sets},
    author={Runzhe Zhan and Xuebo Liu and Derek F. Wong and Lidia S. Chao},
    booktitle={Thirty-fifth Conference on Neural Information Processing Systems, Datasets and Benchmarks Track},
    year={2021},
    url={https://openreview.net/forum?id=hhKA5k0oVy5}
}
```