---
license: cc-by-sa-4.0
pretty_name: SQuAD for question generation
language: ja
multilinguality: monolingual
size_categories: 1k<n<10K
source_datasets: lmqg/qg_jaquad
task_categories:
- text-generation
task_ids:
- language-modeling
tags:
- question-generation
---

# Dataset Card for "lmqg/qag_jaquad"


## Dataset Description
- **Repository:** [https://github.com/asahi417/lm-question-generation](https://github.com/asahi417/lm-question-generation)
- **Paper:** [https://arxiv.org/abs/2210.03992](https://arxiv.org/abs/2210.03992)
- **Point of Contact:** [Asahi Ushio](http://asahiushio.com/)

### Dataset Summary
This is the question & answer generation dataset based on the JAQuAD.

### Supported Tasks and Leaderboards
* `question-answer-generation`: The dataset is assumed to be used to train a model for question & answer generation.
  Success on this task is typically measured by achieving a high BLEU4/METEOR/ROUGE-L/BERTScore/MoverScore (see our paper for more in detail).

### Languages
Japanese (ja)

## Dataset Structure
An example of 'train' looks as follows.
```
{
  "paragraph": ""Nerdilinga"は898年にカロリング朝の王領として初めて文献に記録されている。レーゲンスブルク司教の統治下でネルトリンゲンは市場町に成長していった。1215年にネルトリンゲンは皇帝フリードリヒ2世から都市権を与えられ、帝国自由都市となった。この年に最初の市壁が築かれた。その縄張りは現在も街の地図に見て取れる。1219年、ネルトリンゲンの聖霊降臨祭についての最も古い文献上の記録が遺されている。重要な交易路が交差するこの都市は穀物、家畜、織物、毛皮、金属製品の主要な集散地に発展していった。ネルトリンゲンはフランクフルトと並ぶドイツで最も重要な遠距離交易都市の一つとなったのである。",
  "questions": [ "1215年にネルトリンゲンは誰から都市権を与えられ、帝国自由都市となったか。", "\"Nerdilinga\"の最初の記録は何年のものですか。" ],
  "answers": [ "皇帝フリードリヒ2世", "898年" ],
  "questions_answers": "question: 1215年にネルトリンゲンは誰から都市権を与えられ、帝国自由都市となったか。, answer: 皇帝フリードリヒ2世 | question: "Nerdilinga"の最初の記録は何年のものですか。, answer: 898年"
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
|9508|     1431 | 3050|


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