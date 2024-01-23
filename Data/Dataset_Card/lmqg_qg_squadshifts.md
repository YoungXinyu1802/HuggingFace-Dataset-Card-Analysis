---
license: cc-by-4.0
pretty_name: SubjQA for question generation
language: en
multilinguality: monolingual
size_categories: 10K<n<100K
source_datasets: subjqa
task_categories:
- text-generation
task_ids:
- language-modeling
tags:
- question-generation
---

# Dataset Card for "lmqg/qg_squadshifts"

## Dataset Description
- **Repository:** [https://github.com/asahi417/lm-question-generation](https://github.com/asahi417/lm-question-generation)
- **Paper:** [https://arxiv.org/abs/2210.03992](https://arxiv.org/abs/2210.03992)
- **Point of Contact:** [Asahi Ushio](http://asahiushio.com/)

### Dataset Summary
This is a subset of [QG-Bench](https://github.com/asahi417/lm-question-generation/blob/master/QG_BENCH.md#datasets), a unified question generation benchmark proposed in
 ["Generative Language Models for Paragraph-Level Question Generation: A Unified Benchmark and Evaluation, EMNLP 2022 main conference"](https://arxiv.org/abs/2210.03992).
Modified version of [SQuADShifts](https://modestyachts.github.io/squadshifts-website/index.html) for question generation (QG) task.

### Supported Tasks and Leaderboards
* `question-generation`: The dataset can be used to train a model for question generation.
  Success on this task is typically measured by achieving a high BLEU4/METEOR/ROUGE-L/BERTScore/MoverScore (see our paper for more in detail).

### Languages
English (en)

## Dataset Structure

An example of 'train' looks as follows.
```
{
  "question": "has there ever been a legal challange?",
  "paragraph": "The status of the Armenian Apostolic Church within the Republic of Armenia is defined in the country's constitution. Article 8.1 of the Constitution of Armenia states: "The Republic of Armenia recognizes the exclusive historical mission of the Armenian Apostolic Holy Church as a national church, in the spiritual life, development of the national culture and preservation of the national identity of the people of Armenia." Among others, ethnographer Hranush Kharatyan has questioned the constitutionality of the phrase "national church".",
  "answer": "Among others, ethnographer Hranush Kharatyan has questioned the constitutionality of the phrase "national church",
  "sentence": "Article 8.1 of the Constitution of Armenia states: "The Republic of Armenia recognizes the exclusive historical mission of the Armenian Apostolic Holy Church as a national church, in the spiritual life, development of the national culture and preservation of the national identity of the people of Armenia." Among others, ethnographer Hranush Kharatyan has questioned the constitutionality of the phrase "national church",
  "paragraph_sentence": "The status of the Armenian Apostolic Church within the Republic of Armenia is defined in the country's constitution. <hl> Article 8.1 of the Constitution of Armenia states: "The Republic of Armenia recognizes the exclusive historical mission of the Armenian Apostolic Holy Church as a national church, in the spiritual life, development of the national culture and preservation of the national identity of the people of Armenia." Among others, ethnographer Hranush Kharatyan has questioned the constitutionality of the phrase "national church". <hl>",
  "paragraph_answer": "The status of the Armenian Apostolic Church within the Republic of Armenia is defined in the country's constitution. Article 8.1 of the Constitution of Armenia states: "The Republic of Armenia recognizes the exclusive historical mission of the Armenian Apostolic Holy Church as a national church, in the spiritual life, development of the national culture and preservation of the national identity of the people of Armenia." <hl> Among others, ethnographer Hranush Kharatyan has questioned the constitutionality of the phrase "national church". <hl>",
  "sentence_answer": "Article 8.1 of the Constitution of Armenia states: "The Republic of Armenia recognizes the exclusive historical mission of the Armenian Apostolic Holy Church as a national church, in the spiritual life, development of the national culture and preservation of the national identity of the people of Armenia." <hl> Among others, ethnographer Hranush Kharatyan has questioned the constitutionality of the phrase "national church". <hl>"
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

### Data Splits

|   name      |train  | valid | test |
|-------------|------:|------:|-----:|
|default (all)|9209|6283 |18,844|
| amazon      |3295|1648|4942|
| new_wiki    |2646|1323|3969|
| nyt         |3355|1678|5032|
| reddit      |3268|1634|4901|

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