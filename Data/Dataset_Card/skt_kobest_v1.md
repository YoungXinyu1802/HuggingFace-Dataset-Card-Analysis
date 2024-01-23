---
pretty_name: KoBEST
annotations_creators:
- expert-generated
language_creators:
- expert-generated
language:
- ko
license:
- cc-by-sa-4.0
multilinguality:
- monolingual
size_categories:
- 10K<n<100K
source_datasets:
- original
---

# Dataset Card for KoBEST

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

- **Repository:** https://github.com/SKT-LSL/KoBEST_datarepo
- **Paper:**
- **Point of Contact:** https://github.com/SKT-LSL/KoBEST_datarepo/issues

### Dataset Summary

KoBEST is a Korean benchmark suite consists of 5 natural language understanding tasks that requires advanced knowledge in Korean.

### Supported Tasks and Leaderboards

Boolean Question Answering, Choice of Plausible Alternatives, Words-in-Context, HellaSwag, Sentiment Negation Recognition

### Languages

`ko-KR`

## Dataset Structure

### Data Instances

#### KB-BoolQ
An example of a data point looks as follows.
```
{'paragraph': '두아 리파(Dua Lipa, 1995년 8월 22일 ~ )는 잉글랜드의 싱어송라이터, 모델이다. BBC 사운드 오브 2016 명단에 노미닛되었다. 싱글 "Be the One"가 영국 싱글 차트 9위까지 오르는 등 성과를 보여주었다.',
 'question': '두아 리파는 영국인인가?',
 'label': 1}
```

#### KB-COPA
An example of a data point looks as follows.
```
{'premise': '물을 오래 끓였다.',
 'question': '결과',
 'alternative_1': '물의 양이 늘어났다.',
 'alternative_2': '물의 양이 줄어들었다.',
 'label': 1}
```

#### KB-WiC
An example of a data point looks as follows.
```
{'word': '양분',
 'context_1': '토양에 [양분]이 풍부하여 나무가 잘 자란다.	',
 'context_2': '태아는 모체로부터 [양분]과 산소를 공급받게 된다.',
 'label': 1}
```

#### KB-HellaSwag
An example of a data point looks as follows.
```
{'context': '모자를 쓴 투수가 타자에게 온 힘을 다해 공을 던진다. 공이 타자에게 빠른 속도로 다가온다. 타자가 공을 배트로 친다. 배트에서 깡 소리가 난다. 공이 하늘 위로 날아간다.',
 'ending_1': '외야수가 떨어지는 공을 글러브로 잡는다.',
 'ending_2': '외야수가 공이 떨어질 위치에 자리를 잡는다.',
 'ending_3': '심판이 아웃을 외친다.',
 'ending_4': '외야수가 공을 따라 뛰기 시작한다.',
 'label': 3}
```

#### KB-SentiNeg
An example of a data point looks as follows.
```
{'sentence': '택배사 정말 마음에 듬',
 'label': 1}
```

### Data Fields

### KB-BoolQ
+ `paragraph`: a `string` feature
+ `question`: a `string` feature
+ `label`: a classification label, with possible values `False`(0) and `True`(1)


### KB-COPA
+ `premise`: a `string` feature
+ `question`: a `string` feature
+ `alternative_1`: a `string` feature
+ `alternative_2`: a `string` feature
+ `label`: an answer candidate label, with possible values `alternative_1`(0) and `alternative_2`(1)


### KB-WiC
+ `target_word`: a `string` feature
+ `context_1`: a `string` feature
+ `context_2`: a `string` feature
+ `label`: a classification label, with possible values `False`(0) and `True`(1)

### KB-HellaSwag
+ `target_word`: a `string` feature
+ `context_1`: a `string` feature
+ `context_2`: a `string` feature
+ `label`: a classification label, with possible values `False`(0) and `True`(1)

### KB-SentiNeg
+ `sentence`: a `string` feature
+ `label`: a classification label, with possible values `Negative`(0) and `Positive`(1)


### Data Splits

#### KB-BoolQ

+ train: 3,665
+ dev: 700
+ test: 1,404

#### KB-COPA

+ train: 3,076
+ dev: 1,000
+ test: 1,000

#### KB-WiC

+ train: 3,318
+ dev: 1,260
+ test: 1,260

#### KB-HellaSwag

+ train: 3,665
+ dev: 700
+ test: 1,404

#### KB-SentiNeg

+ train: 3,649
+ dev: 400
+ test: 397
+ test_originated: 397 (Corresponding training data where the test set is originated from.)

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

```
@misc{https://doi.org/10.48550/arxiv.2204.04541,
  doi = {10.48550/ARXIV.2204.04541},
  url = {https://arxiv.org/abs/2204.04541},
  author = {Kim, Dohyeong and Jang, Myeongjun and Kwon, Deuk Sin and Davis, Eric},
  title = {KOBEST: Korean Balanced Evaluation of Significant Tasks},
  publisher = {arXiv},
  year = {2022},
}
```

[More Information Needed]

### Contributions

Thanks to [@MJ-Jang](https://github.com/MJ-Jang) for adding this dataset.