---
license: cc-by-sa-4.0
pretty_name: SQuAD for question generation
language: ko
multilinguality: monolingual
size_categories: 1k<n<10K
source_datasets: lmqg/qg_koquad
task_categories:
- text-generation
task_ids:
- language-modeling
tags:
- question-generation
---

# Dataset Card for "lmqg/qag_koquad"


## Dataset Description
- **Repository:** [https://github.com/asahi417/lm-question-generation](https://github.com/asahi417/lm-question-generation)
- **Paper:** [https://arxiv.org/abs/2210.03992](https://arxiv.org/abs/2210.03992)
- **Point of Contact:** [Asahi Ushio](http://asahiushio.com/)

### Dataset Summary
This is the question & answer generation dataset based on the KOQuAD.

### Supported Tasks and Leaderboards
* `question-answer-generation`: The dataset is assumed to be used to train a model for question & answer generation.
  Success on this task is typically measured by achieving a high BLEU4/METEOR/ROUGE-L/BERTScore/MoverScore (see our paper for more in detail).

### Languages
Korean (ko)

## Dataset Structure
An example of 'train' looks as follows.
```
{
  "paragraph": ""3.13 만세운동" 은 1919년 3.13일 전주에서 일어난 만세운동이다. 지역 인사들과 함께 신흥학교 학생들이 주도적인 역할을 하며, 만세운동을 이끌었다. 박태련, 김신극 등 전주 지도자들은 군산에서 4일과 5일 독립만세 시위가 감행됐다는 소식에 듣고 준비하고 있었다. 천도교와 박태련 신간회 총무집에서 필요한 태극기를 인쇄하기로 했었다. 서울을 비롯한 다른 지방에서 시위가 계속되자 일본경찰은 신흥학교와 기전학교를 비롯한 전주시내 학교에 강제 방학조치를 취했다. 이에 최종삼 등 신흥학교 학생 5명은 밤을 이용해 신흥학교 지하실에서 태극기 등 인쇄물을 만들었다. 준비를 마친 이들은 13일 장터로 모이기 시작했고, 채소가마니로 위장한 태극기를 장터로 실어 나르고 거사 직전 시장 입구인 완산동과 전주교 건너편에서 군중들에게 은밀히 배부했다. 낮 12시20분께 신흥학교와 기전학교 학생 및 천도교도 등은 태극기를 들고 만세를 불렀다. 남문 밖 시장, 제2보통학교(현 완산초등학교)에서 모여 인쇄물을 뿌리며 시가지로 구보로 행진했다. 시위는 오후 11시까지 서너차례 계속됐다. 또 다음날 오후 3시에도 군중이 모여 만세를 불렀다. 이후 고형진, 남궁현, 김병학, 김점쇠, 이기곤, 김경신 등 신흥학교 학생들은 시위를 주도했다는 혐의로 모두 실형 1년을 언도 받았다. 이외 신흥학교 학생 3명은 일제의 고문에 옥사한 것으로 알려졌다. 또 시위를 지도한 김인전 목사는 이후 중국 상해로 거처를 옮겨 임시정부에서 활동했다. 현재 신흥학교 교문 옆에 만세운동 기념비가 세워져 있다.",
  "questions": [ "만세운동 기념비가 세워져 있는 곳은?", "일본경찰의 강제 방학조치에도 불구하고 학생들은 신흥학교 지하실에 모여서 어떤 인쇄물을 만들었는가?", "여러 지방에서 시위가 일어나자 일본경찰이 전주시내 학교에 감행한 조치는 무엇인가?", "지역인사들과 신흥고등학교 학생들이 주도적인 역할을 한 3.13 만세운동이 일어난 해는?", "신흥학교 학생들은 시위를 주도했다는 혐의로 모두 실형 몇년을 언도 받았는가?", "만세운동에서 주도적인 역할을 한 이들은?", "1919년 3.1 운동이 일어난 지역은 어디인가?", "3.13 만세운동이 일어난 곳은?" ],
  "answers": [ "신흥학교 교문 옆", "태극기", "강제 방학조치", "1919년", "1년", "신흥학교 학생들", "전주", "전주" ],
  "questions_answers": "question: 만세운동 기념비가 세워져 있는 곳은?, answer: 신흥학교 교문 옆 | question: 일본경찰의 강제 방학조치에도 불구하고 학생들은 신흥학교 지하실에 모여서 어떤 인쇄물을 만들었는가?, answer: 태극기 | question: 여러 지방에서 시위가 일어나자 일본경찰이 전주시내 학교에 감행한 조치는 무엇인가?, answer: 강제 방학조치 | question: 지역인사들과 신흥고등학교 학생들이 주도적인 역할을 한 3.13 만세운동이 일어난 해는?, answer: 1919년 | question: 신흥학교 학생들은 시위를 주도했다는 혐의로 모두 실형 몇년을 언도 받았는가?, answer: 1년 | question: 만세운동에서 주도적인 역할을 한 이들은?, answer: 신흥학교 학생들 | question: 1919년 3.1 운동이 일어난 지역은 어디인가?, answer: 전주 | question: 3.13 만세운동이 일어난 곳은?, answer: 전주"
  }
```
The data fields are the same among all splits.
- `questions`: a `list` of `string` features. 
- `answers`: a `list` of `string` features.
- `paragraph`: a `string` feature.
- `questions_answers`: a `string` feature.

## Data Splits

|train|validation|test |
|----:|---------:|----:|
|9600 |     960  | 4442|


## Citation Information

```
@inproceedings{ushio-etal-2022-generative,
    title = "{G}enerative {L}anguage {M}odels for {P}aragraph-{L}evel {Q}uestion {G}eneration",
    author = "Ushio, Asahi  and
        Alva-Manchego, Fernando  and
        Camacho-Collados, Jose",
    booktitle = "Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing",
    month = dec,
    year = "2022",
    address = "Abu Dhabi, U.A.E.",
    publisher = "Association for Computational Linguistics",
}
```