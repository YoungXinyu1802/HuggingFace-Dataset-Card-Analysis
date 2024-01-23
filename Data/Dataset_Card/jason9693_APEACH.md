---
annotations_creators:
- crowdsourced
- crowd-generated
language_creators:
- found
language:
- ko
license:
- cc-by-sa-4.0
multilinguality:
- monolingual
paperswithcode_id: apeach
pretty_name: 'APEACH'
size_categories:
- 1K<n<10K
source_datasets:
- original
task_categories:
- text-classification
task_ids:
- binary-classification
---
# Dataset for project: kor_hate_eval(APEACH)

![](https://github.com/jason9693/APEACH/raw/master/resource/dist_topics.png)

## Sample Code
<a href="https://colab.research.google.com/drive/1djd0fuoMYIaf7VCHaLQIziJi4_yBJruP#scrollTo=VPR24ysr5Q7k"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="base"/></a>

## Dataset Descritpion

Korean Hate Speech Evaluation Datasets : trained with [BEEP!](https://huggingface.co/datasets/kor_hate) and evaluate with [APEACH](https://github.com/jason9693/APEACH)

- **Repository: [Korean HateSpeech Evaluation Dataset](https://github.com/jason9693/APEACH)**
- **Paper: [APEACH: Attacking Pejorative Expressions with Analysis on Crowd-Generated Hate Speech Evaluation Datasets](https://arxiv.org/abs/2202.12459)**
- **Point of Contact: [Kichang Yang](ykcha9@gmail.com)**

### Languages

ko-KR

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
{'text': ['(현재 호텔주인 심정) 아18 난 마른하늘에 날벼락맞고 호텔망하게생겼는데 누군 계속 추모받네....',
  '....한국적인 미인의 대표적인 분...너무나 곱고아름다운모습...그모습뒤의 슬픔을 미처 알지못했네요ㅠ'],
 'class': ['Spoiled', 'Default']}
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "text": "Value(dtype='string', id=None)",
  "class": "ClassLabel(num_classes=2, names=['Default', 'Spoiled'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train (binarized BEEP!)        | 7896 |
| valid  (APEACH)       | 3770 |

## Citation
```
@article{yang2022apeach,
  title={APEACH: Attacking Pejorative Expressions with Analysis on Crowd-Generated Hate Speech Evaluation Datasets},
  author={Yang, Kichang and Jang, Wonjun and Cho, Won Ik},
  journal={arXiv preprint arXiv:2202.12459},
  year={2022}
}
```
