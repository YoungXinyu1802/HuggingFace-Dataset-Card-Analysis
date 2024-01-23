---
license: cc-by-sa-3.0
pretty_name: JaQuAD for question generation
language: ja
multilinguality: monolingual
size_categories: 10K<n<100K
source_datasets: SkelterLabsInc/JaQuAD
task_categories:
- text-generation
task_ids:
- language-modeling
tags:
- question-generation
---

# Dataset Card for "lmqg/qg_jaquad"


## Dataset Description
- **Repository:** [https://github.com/asahi417/lm-question-generation](https://github.com/asahi417/lm-question-generation)
- **Paper:** [https://arxiv.org/abs/2210.03992](https://arxiv.org/abs/2210.03992)
- **Point of Contact:** [Asahi Ushio](http://asahiushio.com/)

### Dataset Summary
This is a subset of [QG-Bench](https://github.com/asahi417/lm-question-generation/blob/master/QG_BENCH.md#datasets), a unified question generation benchmark proposed in
 ["Generative Language Models for Paragraph-Level Question Generation: A Unified Benchmark and Evaluation, EMNLP 2022 main conference"](https://arxiv.org/abs/2210.03992).
This is [JaQuAD](https://github.com/SkelterLabsInc/JaQuAD) dataset compiled for question generation (QG) task. The test set of the original 
data is not publicly released, so we randomly sampled test questions from the training set. There are no overlap in terms of the paragraph across train, test, and validation split.

### Supported Tasks and Leaderboards
* `question-generation`: The dataset is assumed to be used to train a model for question generation.
  Success on this task is typically measured by achieving a high BLEU4/METEOR/ROUGE-L/BERTScore/MoverScore (see our paper for more in detail).

### Languages
Japanese (ja)

## Dataset Structure
An example of 'train' looks as follows.
```
{
  "question": "新型車両として6000系が構想されたのは、製造費用のほか、どんな費用を抑えるためだったの?",
  "paragraph": "三多摩地区開発による沿線人口の増加、相模原線延伸による多摩ニュータウン乗り入れ、都営地下鉄10号線(現都営地下鉄新宿線、以下新宿線と表記する)乗入構想により、京王線の利用客増加が見込まれ、相当数の車両を準備する必要に迫られるなか、製造費用、保守費用を抑えた新型車両として6000系が構想された。新宿線建設に際してはすでに1号線(後の浅草線)を1,435mm軌間で開業させていた東京都は京成電鉄と1号線との乗り入れにあたり京成電鉄の路線を1,372mmから1,435mmに改軌させた事例や、1,372mm軌間の特殊性から運輸省(当時、2001年から国土交通省)と共に京王にも改軌を求めたが、改軌工事中の輸送力確保が困難なことを理由に改軌しないことで決着している。",
  "answer": "保守費用",
  "sentence": "三多摩地区開発による沿線人口の増加、相模原線延伸による多摩ニュータウン乗り入れ、都営地下鉄10号線(現都営地下鉄新宿線、以下新宿線と表記する)乗入構想により、京王線の利用客増加が見込まれ、相当数の車両を準備する必要に迫られるなか、製造費用、保守費用を抑えた新型車両として6000系が構想された。",
  "paragraph_sentence": "<hl>三多摩地区開発による沿線人口の増加、相模原線延伸による多摩ニュータウン乗り入れ、都営地下鉄10号線(現都営地下鉄新宿線、以下新宿線と表記する)乗入構想により、京王線の利用客増加が見込まれ、相当数の車両を準備する必要に迫られるなか、製造費用、保守費用を抑えた新型車両として6000系が構想された。<hl>新宿線建設に際してはすでに1号線(後の浅草線)を1,435mm軌間で開業させていた東京都は京成電鉄と1号線との乗り入れにあたり京成電鉄の路線を1,372mmから1,435mmに改軌させた事例や、1,372mm軌間の特殊性から運輸省(当時、2001年から国土交通省)と共に京王にも改軌を求めたが、改軌工事中の輸送力確保が困難なことを理由に改軌しないことで決着している。",
  "paragraph_answer": "三多摩地区開発による沿線人口の増加、相模原線延伸による多摩ニュータウン乗り入れ、都営地下鉄10号線(現都営地下鉄新宿線、以下新宿線と表記する)乗入構想により、京王線の利用客増加が見込まれ、相当数の車両を準備する必要に迫られるなか、製造費用、<hl>保守費用<hl>を抑えた新型車両として6000系が構想された。新宿線建設に際してはすでに1号線(後の浅草線)を1,435mm軌間で開業させていた東京都は京成電鉄と1号線との乗り入れにあたり京成電鉄の路線を1,372mmから1,435mmに改軌させた事例や、1,372mm軌間の特殊性から運輸省(当時、2001年から国土交通省)と共に京王にも改軌を求めたが、改軌工事中の輸送力確保が困難なことを理由に改軌しないことで決着している。",
  "sentence_answer": "三多摩地区開発による沿線人口の増加、相模原線延伸による多摩ニュータウン乗り入れ、都営地下鉄10号線(現都営地下鉄新宿線、以下新宿線と表記する)乗入構想により、京王線の利用客増加が見込まれ、相当数の車両を準備する必要に迫られるなか、製造費用、<hl>保守費用<hl>を抑えた新型車両として6000系が構想された。"
}
```
The data fields are the same among all splits.
- `question`: a `string` feature. 
- `paragraph`: a `string` feature.
- `answer`: a `string` feature.
- `sentence`: a `string` feature.
- `paragraph_answer`: a `string` feature, which is same as the paragraph but the answer is highlighted by a special token `<hl>`.
- `paragraph_sentence`: a `string` feature, which is same as the paragraph but a sentence containing the answer is highlighted by a special token `<hl>`.
- `sentence_answer`: a `string` feature, which is same as the sentence but the answer is highlighted by a special token `<hl>`.

Each of `paragraph_answer`, `paragraph_sentence`, and `sentence_answer` feature is assumed to be used to train a question generation model,
but with different information. The `paragraph_answer` and `sentence_answer` features are for answer-aware question generation and 
`paragraph_sentence` feature is for sentence-aware question generation.

## Data Splits

|train|validation|test |
|----:|---------:|----:|
|27809|      3939| 3939|


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