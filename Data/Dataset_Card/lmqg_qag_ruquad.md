---
license: cc-by-sa-4.0
pretty_name: SQuAD for question generation
language: ru
multilinguality: monolingual
size_categories: 1k<n<10K
source_datasets: lmqg/qg_ruquad
task_categories:
- text-generation
task_ids:
- language-modeling
tags:
- question-generation
---

# Dataset Card for "lmqg/qag_ruquad"


## Dataset Description
- **Repository:** [https://github.com/asahi417/lm-question-generation](https://github.com/asahi417/lm-question-generation)
- **Paper:** [https://arxiv.org/abs/2210.03992](https://arxiv.org/abs/2210.03992)
- **Point of Contact:** [Asahi Ushio](http://asahiushio.com/)

### Dataset Summary
This is the question & answer generation dataset based on the RUQuAD.

### Supported Tasks and Leaderboards
* `question-answer-generation`: The dataset is assumed to be used to train a model for question & answer generation.
  Success on this task is typically measured by achieving a high BLEU4/METEOR/ROUGE-L/BERTScore/MoverScore (see our paper for more in detail).

### Languages
Russian (ru)

## Dataset Structure
An example of 'train' looks as follows.
```
{
  "paragraph": " Everybody , как и хотела Мадонна, выпускают синглом. При нулевом бюджете на раскрутку фото певицы решают не помещать на обложке, чтобы не отпугнуть цветную аудиторию якобы негритянской диско-соул-певицы . Everybody поднимается на 3-е место в чарте Hot Dance Club Songs, а потом на 107 место в основном, немного не дотянув до первой сотни Hot 100 журнала Billboard[91]. Менеджмент считает это отличным результатом, учитывая нулевые затраты на пиар, и хочет убедиться, что взлёт Everybody не случаен. По просьбе Мадонны вместо Каминса берут более опытного штатного аранжировщика Warner Bros. Records Регги Лукаса (англ.)русск.. Второй сингл Burning Up тоже достигает в чарте танцевальных хитов 3-го места, повторив успех Everybody . И только после этого Мадонне позволяют арендовать студию для записи первого альбома[91].",
  "questions": [ "При каком бюджете на раскрутку фото певицы решают не помещать на обложке ?", "Какой альбом Мадонны выпускают синглом?", "Имя более опытного штатного аранжировщика берут по просьбе Мадонны вместо Каминсаболее ?", "Почему при нулевом бджете фото певицы решают не помещать на обложке ?", "На каое место Everybody поднимается в чарте Hot Dance Club Songs?" ],
  "answers": [ "При нулевом", " Everybody ", "Warner Bros", "чтобы не отпугнуть цветную аудиторию якобы негритянской диско-соул-певицы ", "на 3-е место" ],
  "questions_answers": "question: При каком бюджете на раскрутку фото певицы решают не помещать на обложке ?, answer: При нулевом | question: Какой альбом Мадонны выпускают синглом?, answer: Everybody | question: Имя более опытного штатного аранжировщика берут по просьбе Мадонны вместо Каминсаболее ?, answer: Warner Bros | question: Почему при нулевом бджете фото певицы решают не помещать на обложке ?, answer: чтобы не отпугнуть цветную аудиторию якобы негритянской диско-соул-певицы | question: На каое место Everybody поднимается в чарте Hot Dance Club Songs?, answer: на 3-е место"
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
|10407|     4079 | 4017|


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