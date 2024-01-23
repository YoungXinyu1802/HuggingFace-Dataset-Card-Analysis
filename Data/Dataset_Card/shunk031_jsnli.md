---
language:
- ja

license: 
- cc-by-sa-4.0

multilinguality:
- monolingual

task_categories:
- text-classification

task_ids:
- natural-language-inference
- multi-input-text-classification

tags:
- natural-language-inference
- nli
- jsnli

datasets:
- without-filtering
- with-filtering

metrics:
- accuracy
---

# Dataset Card for JSNLI

[![CI](https://github.com/shunk031/huggingface-datasets_jsnli/actions/workflows/ci.yaml/badge.svg)](https://github.com/shunk031/huggingface-datasets_jsnli/actions/workflows/ci.yaml)

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Dataset Preprocessing](#dataset-preprocessing)
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

- Homepage: https://nlp.ist.i.kyoto-u.ac.jp/?%E6%97%A5%E6%9C%AC%E8%AA%9ESNLI%28JSNLI%29%E3%83%87%E3%83%BC%E3%82%BF%E3%82%BB%E3%83%83%E3%83%88
- Repository: https://github.com/shunk031/huggingface-datasets_jsnli

### Dataset Summary

[日本語 SNLI(JSNLI) データセット - KUROHASHI-CHU-MURAWAKI LAB](https://nlp.ist.i.kyoto-u.ac.jp/?%E6%97%A5%E6%9C%AC%E8%AA%9ESNLI%28JSNLI%29%E3%83%87%E3%83%BC%E3%82%BF%E3%82%BB%E3%83%83%E3%83%88 ) より：

> 本データセットは自然言語推論 (NLI) の標準的ベンチマークである [SNLI](https://nlp.stanford.edu/projects/snli/) を日本語に翻訳したものです。

### Dataset Preprocessing

### Supported Tasks and Leaderboards

### Languages

注釈はすべて日本語を主要言語としています。

## Dataset Structure

> データセットは TSV フォーマットで、各行がラベル、前提、仮説の三つ組を表します。前提、仮説は JUMAN++ によって形態素分割されています。以下に例をあげます。

```
entailment      自転車 で ２ 人 の 男性 が レース で 競い ます 。       人々 は 自転車 に 乗って います 。
```

### Data Instances

```python
from datasets import load_dataset
load_dataset("shunk031/jsnli", "without-filtering")
```

```json
{
    'label': 'neutral', 
    'premise': 'ガレージ で 、 壁 に ナイフ を 投げる 男 。', 
    'hypothesis': '男 は 魔法 の ショー の ため に ナイフ を 投げる 行為 を 練習 して い ます 。'
}
```

### Data Fields

### Data Splits

| name              | train   | validation |
|-------------------|--------:|-----------:|
| without-filtering | 548,014 | 3,916      |
| with-filtering    | 533,005 | 3,916      |

## Dataset Creation

### Curation Rationale

### Source Data

#### Initial Data Collection and Normalization

#### Who are the source language producers?

### Annotations

#### Annotation process

> SNLI に機械翻訳を適用した後、評価データにクラウドソーシングによる正確なフィルタリング、学習データに計算機による自動フィルタリングを施すことで構築されています。
> データセットは学習データを全くフィルタリングしていないものと、フィルタリングした中で最も精度が高かったものの 2 種類を公開しています。データサイズは、フィルタリング前の学習データが 548,014 ペア、フィルタリング後の学習データが 533,005 ペア、評価データは 3,916 ペアです。詳細は参考文献を参照してください。

#### Who are the annotators?

### Personal and Sensitive Information

## Considerations for Using the Data

### Social Impact of Dataset

### Discussion of Biases

### Other Known Limitations

## Additional Information

> 本データセットに関するご質問は nl-resource あっと nlp.ist.i.kyoto-u.ac.jp 宛にお願いいたします。

### Dataset Curators

### Licensing Information

> このデータセットのライセンスは、SNLI のライセンスと同じ [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) に従います。SNLI に関しては参考文献を参照してください。

### Citation Information

```bibtex
@article{吉越卓見 2020 機械翻訳を用いた自然言語推論データセットの多言語化，
  title={機械翻訳を用いた自然言語推論データセットの多言語化},
  author={吉越卓見 and 河原大輔 and 黒橋禎夫 and others},
  journal={研究報告自然言語処理 (NL)},
  volume={2020},
  number={6},
  pages={1--8},
  year={2020}
}
```

```bibtex
@inproceedings{bowman2015large,
  title={A large annotated corpus for learning natural language inference},
  author={Bowman, Samuel and Angeli, Gabor and Potts, Christopher and Manning, Christopher D},
  booktitle={Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing},
  pages={632--642},
  year={2015}
}
```

```bibtex
@article{young2014image,
  title={From image descriptions to visual denotations: New similarity metrics for semantic inference over event descriptions},
  author={Young, Peter and Lai, Alice and Hodosh, Micah and Hockenmaier, Julia},
  journal={Transactions of the Association for Computational Linguistics},
  volume={2},
  pages={67--78},
  year={2014},
  publisher={MIT Press}
}
```

### Contributions

JSNLI データセットを公開してくださった吉越 卓見さま，河原 大輔さま，黒橋 禎夫さまに心から感謝します。
