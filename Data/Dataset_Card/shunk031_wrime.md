---
annotations_creators:
- crowdsourced

language:
- ja

language_creators:
- crowdsourced

license:
- unknown

multilinguality:
- monolingual

pretty_name: wrime

tags:
- sentiment-analysis
- wrime

task_categories:
- text-classification
task_ids:
- sentiment-classification

datasets:
- ver1
- ver2

metrics:
- accuracy
---

# Dataset Card for WRIME

[![CI](https://github.com/shunk031/huggingface-datasets_wrime/actions/workflows/ci.yaml/badge.svg)](https://github.com/shunk031/huggingface-datasets_wrime/actions/workflows/ci.yaml)

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

- Homepage: https://github.com/ids-cv/wrime
- Repository: https://github.com/shunk031/huggingface-datasets_wrime
- Paper: https://aclanthology.org/2021.naacl-main.169/

### Dataset Summary

In this study, we introduce a new dataset, WRIME, for emotional intensity estimation. We collect both the subjective emotional intensity ofthe writers themselves and the objective one annotated by the readers, and explore the differences between them. In our data collection, we hired 50 participants via crowdsourcing service. They annotated their own past posts on a social networking service (SNS) with the subjective emotional intensity. We also hired 3 annotators, who annotated allposts with the objective emotional intensity. Consequently, our Japanese emotion analysis datasetconsists of 17,000 posts with both subjective andobjective emotional intensities for Plutchik’s eightemotions ([Plutchik, 1980](https://www.sciencedirect.com/science/article/pii/B9780125587013500077)), which are given in afour-point scale (no, weak, medium, and strong).

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

- Japanese

## Dataset Structure

### Data Instances

When loading a specific configuration, users has to append a version dependent suffix:

```python
from datasets import load_dataset

dataset = load_dataset("shunk031/wrime", name="ver1")

print(dataset)
# DatasetDict({
#     train: Dataset({
#         features: ['sentence', 'user_id', 'datetime', 'writer', 'reader1', 'reader2', 'reader3', 'avg_readers'],
#         num_rows: 40000
#     })
#     validation: Dataset({
#         features: ['sentence', 'user_id', 'datetime', 'writer', 'reader1', 'reader2', 'reader3', 'avg_readers'],
#         num_rows: 1200
#     })
#     test: Dataset({
#         features: ['sentence', 'user_id', 'datetime', 'writer', 'reader1', 'reader2', 'reader3', 'avg_readers'],
#         num_rows: 2000
#     })
# })
```

#### Ver. 1

An example of looks as follows:

```json
{
    "sentence": "ぼけっとしてたらこんな時間｡チャリあるから食べにでたいのに…",
    "user_id": "1",
    "datetime": "2012/07/31 23:48",
    "writer": {
        "joy": 0,
        "sadness": 1,
        "anticipation": 2,
        "surprise": 1,
        "anger": 1,
        "fear": 0,
        "disgust": 0,
        "trust": 1
    },
    "reader1": {
        "joy": 0,
        "sadness": 2,
        "anticipation": 0,
        "surprise": 0,
        "anger": 0,
        "fear": 0,
        "disgust": 0,
        "trust": 0
    },
    "reader2": {
        "joy": 0,
        "sadness": 2,
        "anticipation": 0,
        "surprise": 1,
        "anger": 0,
        "fear": 0,
        "disgust": 0,
        "trust": 0
    },
    "reader3": {
        "joy": 0,
        "sadness": 2,
        "anticipation": 0,
        "surprise": 0,
        "anger": 0,
        "fear": 1,
        "disgust": 1,
        "trust": 0
    },
    "avg_readers": {
        "joy": 0,
        "sadness": 2,
        "anticipation": 0,
        "surprise": 0,
        "anger": 0,
        "fear": 0,
        "disgust": 0,
        "trust": 0
    }
}
```

#### Ver. 1

An example of looks as follows:

```json
{
    "sentence": "ぼけっとしてたらこんな時間。チャリあるから食べにでたいのに…", 
    "user_id": "1", 
    "datetime": "2012/7/31 23:48", 
    "writer": {
        "joy": 0, 
        "sadness": 1, 
        "anticipation": 2, 
        "surprise": 1, 
        "anger": 1, 
        "fear": 0, 
        "disgust": 0, 
        "trust": 1, 
        "sentiment": 0
    }, 
    "reader1": {
        "joy": 0, 
        "sadness": 2, 
        "anticipation": 0, 
        "surprise": 0, 
        "anger": 0, 
        "fear": 0, 
        "disgust": 0, 
        "trust": 0, 
        "sentiment": -2
    }, 
    "reader2": {
        "joy": 0, 
        "sadness": 2, 
        "anticipation": 0, 
        "surprise": 0, 
        "anger": 0, 
        "fear": 1, 
        "disgust": 1, 
        "trust": 0, 
        "sentiment": -1
    }, 
    "reader3": {
        "joy": 0, 
        "sadness": 2, 
        "anticipation": 0, 
        "surprise": 1, 
        "anger": 0, 
        "fear": 0, 
        "disgust": 0, 
        "trust": 0, 
        "sentiment": -1
    }, 
    "avg_readers": {
        "joy": 0, 
        "sadness": 2, 
        "anticipation": 0, 
        "surprise": 0, 
        "anger": 0, 
        "fear": 0, 
        "disgust": 0, 
        "trust": 0, 
        "sentiment": -1
    }
}
```

### Data Fields

#### Ver. 1

- `sentence`: 投稿テキスト
- `user_id`: ユーザー ID
- `datetime`: 投稿日時
- `writer`: 主観 （書き手）
    - `joy`: 主観の喜びの感情
    - `sadness`: 主観の悲しみの感情
    - `anticipation`: 主観の期待の感情
    - `surprise`: 主観の驚きの感情
    - `anger`: 主観の怒りの感情
    - `fear`: 主観の恐れの感情
    - `disgust`: 主観の嫌悪の感情
    - `trust`: 主観の信頼の感情
- `reader1`: 客観 A （読み手 A)
    - `joy`: 客観 A の喜びの感情
    - `sadness`: 客観 A の悲しみの感情
    - `anticipation`: 客観 A の期待の感情
    - `surprise`: 客観 A の驚きの感情
    - `anger`: 客観 A の怒りの感情
    - `fear`: 客観 A の恐れの感情
    - `disgust`: 客観 A の嫌悪の感情
    - `trust`: 客観 A の信頼の感情
- `reader2`: 客観 B （読み手 B)
    - `joy`: 客観 B の喜びの感情
    - `sadness`: 客観 B の悲しみの感情
    - `anticipation`: 客観 B の期待の感情
    - `surprise`: 客観 B の驚きの感情
    - `anger`: 客観 B の怒りの感情
    - `fear`: 客観 B の恐れの感情
    - `disgust`: 客観 B の嫌悪の感情
    - `trust`: 客観 B の信頼の感情
- `reader3`: 客観 C （読み手 C)
    - `joy`: 客観 C の喜びの感情
    - `sadness`: 客観 C の悲しみの感情
    - `anticipation`: 客観 C の期待の感情
    - `surprise`: 客観 C の驚きの感情
    - `anger`: 客観 C の怒りの感情
    - `fear`: 客観 C の恐れの感情
    - `disgust`: 客観 C の嫌悪の感情
    - `trust`: 客観 C の信頼の感情
- `avg_readers`
    - `joy`: 客観 A, B, C 平均の喜びの感情
    - `sadness`: 客観 A, B, C 平均の悲しみの感情
    - `anticipation`: 客観 A, B, C 平均の期待の感情
    - `surprise`: 客観 A, B, C 平均の驚きの感情
    - `anger`: 客観 A, B, C 平均の怒りの感情
    - `fear`: 客観 A, B, C 平均の恐れの感情
    - `disgust`: 客観 A, B, C 平均の嫌悪の感情
    - `trust`: 客観 A, B, C 平均の信頼の感情

#### Ver. 2

- `sentence`: 投稿テキスト
- `user_id`: ユーザー ID
- `datetime`: 投稿日時
- `writer`: 主観 （書き手）
    - `joy`: 主観の喜びの感情
    - `sadness`: 主観の悲しみの感情
    - `anticipation`: 主観の期待の感情
    - `surprise`: 主観の驚きの感情
    - `anger`: 主観の怒りの感情
    - `fear`: 主観の恐れの感情
    - `disgust`: 主観の嫌悪の感情
    - `trust`: 主観の信頼の感情
    - `sentiment`: 主観の感情極性
- `reader1`: 客観 A （読み手 A)
    - `joy`: 客観 A の喜びの感情
    - `sadness`: 客観 A の悲しみの感情
    - `anticipation`: 客観 A の期待の感情
    - `surprise`: 客観 A の驚きの感情
    - `anger`: 客観 A の怒りの感情
    - `fear`: 客観 A の恐れの感情
    - `disgust`: 客観 A の嫌悪の感情
    - `trust`: 客観 A の信頼の感情
    - `sentiment`: 客観 A の感情極性
- `reader2`: 客観 B （読み手 B)
    - `joy`: 客観 B の喜びの感情
    - `sadness`: 客観 B の悲しみの感情
    - `anticipation`: 客観 B の期待の感情
    - `surprise`: 客観 B の驚きの感情
    - `anger`: 客観 B の怒りの感情
    - `fear`: 客観 B の恐れの感情
    - `disgust`: 客観 B の嫌悪の感情
    - `trust`: 客観 B の信頼の感情
    - `sentiment`: 客観 B の感情極性
- `reader3`: 客観 C （読み手 C)
    - `joy`: 客観 C の喜びの感情
    - `sadness`: 客観 C の悲しみの感情
    - `anticipation`: 客観 C の期待の感情
    - `surprise`: 客観 C の驚きの感情
    - `anger`: 客観 C の怒りの感情
    - `fear`: 客観 C の恐れの感情
    - `disgust`: 客観 C の嫌悪の感情
    - `trust`: 客観 C の信頼の感情
    - `sentiment`: 客観 C の感情極性
- `avg_readers`
    - `joy`: 客観 A, B, C 平均の喜びの感情
    - `sadness`: 客観 A, B, C 平均の悲しみの感情
    - `anticipation`: 客観 A, B, C 平均の期待の感情
    - `surprise`: 客観 A, B, C 平均の驚きの感情
    - `anger`: 客観 A, B, C 平均の怒りの感情
    - `fear`: 客観 A, B, C 平均の恐れの感情
    - `disgust`: 客観 A, B, C 平均の嫌悪の感情
    - `trust`: 客観 A, B, C 平均の信頼の感情
    - `sentiment`: 客観 A, B, C 平均の感情極性

### Data Splits

| name | train  | validation | test  |
|------|-------:|-----------:|------:|
| ver1 | 40,000 | 1,200      | 2,000 |
| ver2 | 30,000 | 2,500      | 2,500 |

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

From [the README](https://github.com/ids-cv/wrime/blob/master/README.en.md#licence) of the GitHub:

- The dataset is available for research purposes only.
- Redistribution of the dataset is prohibited.

### Citation Information

```bibtex
@inproceedings{kajiwara-etal-2021-wrime,
    title = "{WRIME}: A New Dataset for Emotional Intensity Estimation with Subjective and Objective Annotations",
    author = "Kajiwara, Tomoyuki  and
      Chu, Chenhui  and
      Takemura, Noriko  and
      Nakashima, Yuta  and
      Nagahara, Hajime",
    booktitle = "Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies",
    month = jun,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.naacl-main.169",
    doi = "10.18653/v1/2021.naacl-main.169",
    pages = "2095--2104",
    abstract = "We annotate 17,000 SNS posts with both the writer{'}s subjective emotional intensity and the reader{'}s objective one to construct a Japanese emotion analysis dataset. In this study, we explore the difference between the emotional intensity of the writer and that of the readers with this dataset. We found that the reader cannot fully detect the emotions of the writer, especially anger and trust. In addition, experimental results in estimating the emotional intensity show that it is more difficult to estimate the writer{'}s subjective labels than the readers{'}. The large gap between the subjective and objective emotions imply the complexity of the mapping from a post to the subjective emotion intensities, which also leads to a lower performance with machine learning models.",
}
```

```bibtex
@inproceedings{suzuki-etal-2022-japanese,
    title = "A {J}apanese Dataset for Subjective and Objective Sentiment Polarity Classification in Micro Blog Domain",
    author = "Suzuki, Haruya  and
      Miyauchi, Yuto  and
      Akiyama, Kazuki  and
      Kajiwara, Tomoyuki  and
      Ninomiya, Takashi  and
      Takemura, Noriko  and
      Nakashima, Yuta  and
      Nagahara, Hajime",
    booktitle = "Proceedings of the Thirteenth Language Resources and Evaluation Conference",
    month = jun,
    year = "2022",
    address = "Marseille, France",
    publisher = "European Language Resources Association",
    url = "https://aclanthology.org/2022.lrec-1.759",
    pages = "7022--7028",
    abstract = "We annotate 35,000 SNS posts with both the writer{'}s subjective sentiment polarity labels and the reader{'}s objective ones to construct a Japanese sentiment analysis dataset. Our dataset includes intensity labels (\textit{none}, \textit{weak}, \textit{medium}, and \textit{strong}) for each of the eight basic emotions by Plutchik (\textit{joy}, \textit{sadness}, \textit{anticipation}, \textit{surprise}, \textit{anger}, \textit{fear}, \textit{disgust}, and \textit{trust}) as well as sentiment polarity labels (\textit{strong positive}, \textit{positive}, \textit{neutral}, \textit{negative}, and \textit{strong negative}). Previous studies on emotion analysis have studied the analysis of basic emotions and sentiment polarity independently. In other words, there are few corpora that are annotated with both basic emotions and sentiment polarity. Our dataset is the first large-scale corpus to annotate both of these emotion labels, and from both the writer{'}s and reader{'}s perspectives. In this paper, we analyze the relationship between basic emotion intensity and sentiment polarity on our dataset and report the results of benchmarking sentiment polarity classification.",
}
```

### Contributions

Thanks to [@moguranosenshi](https://github.com/moguranosenshi) for creating this dataset.
