---
license: other
---
---
annotations_creators:
- crowdsourced
language:
- ja
language_creators:
- crowdsourced
license:
- cc-by-sa-4.0
multilinguality:
- monolingual
paperswithcode_id: squad
pretty_name: squad-ja
size_categories:
- 100K<n<1M
source_datasets:
- original
tags: []
task_categories:
- question-answering
task_ids:
- open-domain-qa
- extractive-qa
train-eval-index:
- col_mapping:
    answers:
      answer_start: answer_start
      text: text
    context: context
    question: question
  config: squad_v2
  metrics:
  - name: SQuAD v2
    type: squad_v2
  splits:
    eval_split: validation
    train_split: train
  task: question-answering
  task_id: extractive_question_answering
---

# Dataset Card for [Dataset Name]

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
- **Paper:**
- **Leaderboard:**
- **Point of Contact:**

### Dataset Summary
Google翻訳APIで翻訳した日本語版SQuAD2.0


### Supported Tasks and Leaderboards

[More Information Needed]

### Languages
Japanese

## Dataset Structure


### Data Instances

```
{
  "start": 43,
  "end": 88,
  "question": "ビヨンセ は いつ から 人気 を 博し 始め ました か ？",
  "context": "BeyoncéGiselleKnowles - Carter （ /b i ː ˈ j ɒ nse ɪ / bee - YON - say ） （ 1981 年 9 月 4 日 生まれ ） は 、 アメリカ の シンガー 、 ソング ライター 、 レコード プロデューサー 、 女優 です 。 テキサス 州 ヒューストン で 生まれ育った 彼女 は 、 子供 の 頃 に さまざまな 歌 と 踊り の コンテスト に 出演 し 、 1990 年 代 後半 に R ＆ B ガールグループ Destiny & 39 ; sChild の リード シンガー と して 名声 を 博し ました 。 父親 の マシューノウルズ が 管理 する この グループ は 、 世界 で 最も 売れて いる 少女 グループ の 1 つ に なり ました 。 彼 ら の 休み は ビヨンセ の デビュー アルバム 、 DangerouslyinLove （ 2003 ） の リリース を 見 ました 。 彼女 は 世界 中 で ソロ アーティスト と して 確立 し 、 5 つ の グラミー 賞 を 獲得 し 、 ビル ボード ホット 100 ナンバーワン シングル 「 CrazyinLove 」 と 「 BabyBoy 」 を フィーチャー し ました 。",
  "id": "56be85543aeaaa14008c9063"
}
```

### Data Fields
- start
- end
- question
- context
- id

### Data Splits

- train 86820
- valid 5927

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

[More Information Needed]

### Contributions

Thanks to [@github-username](https://github.com/<github-username>) for adding this dataset.