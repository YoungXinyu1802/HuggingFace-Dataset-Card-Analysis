---
license: cc-by-sa-4.0
pretty_name: SQuAD for question generation
language: en
multilinguality: monolingual
size_categories: 1k<n<10K
source_datasets: lmqg/qg_squad
task_categories:
- text-generation
task_ids:
- language-modeling
tags:
- question-generation
---

# Dataset Card for "lmqg/qag_squad"


## Dataset Description
- **Repository:** [https://github.com/asahi417/lm-question-generation](https://github.com/asahi417/lm-question-generation)
- **Paper:** [https://arxiv.org/abs/2210.03992](https://arxiv.org/abs/2210.03992)
- **Point of Contact:** [Asahi Ushio](http://asahiushio.com/)

### Dataset Summary
This is the question & answer generation dataset based on the SQuAD.

### Supported Tasks and Leaderboards
* `question-answer-generation`: The dataset is assumed to be used to train a model for question & answer generation.
  Success on this task is typically measured by achieving a high BLEU4/METEOR/ROUGE-L/BERTScore/MoverScore (see our paper for more in detail).

### Languages
English (en)

## Dataset Structure
An example of 'train' looks as follows.
```
{
  "paragraph": "\"4 Minutes\" was released as the album's lead single and peaked at number three on the Billboard Hot 100. It was Madonna's 37th top-ten hit on the chart—it pushed Madonna past Elvis Presley as the artist with the most top-ten hits. In the UK she retained her record for the most number-one singles for a female artist; \"4 Minutes\" becoming her thirteenth. At the 23rd Japan Gold Disc Awards, Madonna received her fifth Artist of the Year trophy from Recording Industry Association of Japan, the most for any artist. To further promote the album, Madonna embarked on the Sticky & Sweet Tour; her first major venture with Live Nation. With a gross of $280 million, it became the highest-grossing tour by a solo artist then, surpassing the previous record Madonna set with the Confessions Tour; it was later surpassed by Roger Waters' The Wall Live. It was extended to the next year, adding new European dates, and after it ended, the total gross was $408 million.",
  "questions": [
    "Which single was released as the album's lead single?",
    "Madonna surpassed which artist with the most top-ten hits?",
    "4 minutes became Madonna's which number one single in the UK?",
    "What is the name of the first tour with Live Nation?",
    "How much did Stick and Sweet Tour grossed?"
  ],
  "answers": [
    "4 Minutes",
    "Elvis Presley",
    "thirteenth",
    "Sticky & Sweet Tour",
    "$280 million,"
  ],
  "questions_answers": "question: Which single was released as the album's lead single?, answer: 4 Minutes | question: Madonna surpassed which artist with the most top-ten hits?, answer: Elvis Presley | question: 4 minutes became Madonna's which number one single in the UK?, answer: thirteenth | question: What is the name of the first tour with Live Nation?, answer: Sticky & Sweet Tour | question: How much did Stick and Sweet Tour grossed?, answer: $280 million,"
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
|16462|     2067 | 2429|


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