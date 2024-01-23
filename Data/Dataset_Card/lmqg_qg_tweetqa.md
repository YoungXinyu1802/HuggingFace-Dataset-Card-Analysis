---
license: cc-by-sa-4.0
pretty_name: TweetQA for question generation
language: en
multilinguality: monolingual
size_categories: 1k<n<10K
source_datasets: tweet_qa
task_categories:
- text-generation
task_ids:
- language-modeling
tags:
- question-generation
---

# Dataset Card for "lmqg/qg_tweetqa"


## Dataset Description
- **Repository:** [https://github.com/asahi417/lm-question-generation](https://github.com/asahi417/lm-question-generation)
- **Paper:** [https://arxiv.org/abs/2210.03992](https://arxiv.org/abs/2210.03992)
- **Point of Contact:** [Asahi Ushio](http://asahiushio.com/)

### Dataset Summary
This is the question & answer generation dataset based on the [tweet_qa](https://huggingface.co/datasets/tweet_qa). The test set of the original data is not publicly released, so we randomly sampled test questions from the training set.

### Supported Tasks and Leaderboards
* `question-answer-generation`: The dataset is assumed to be used to train a model for question & answer generation.
  Success on this task is typically measured by achieving a high BLEU4/METEOR/ROUGE-L/BERTScore/MoverScore (see our paper for more in detail).

### Languages
English (en)

## Dataset Structure
An example of 'train' looks as follows.
```
{
  'answer': 'vine',
  'paragraph_question': 'question: what site does the link take you to?, context:5 years in 5 seconds. Darren Booth (@darbooth) January 25, 2013',
  'question': 'what site does the link take you to?',
  'paragraph': '5 years in 5 seconds. Darren Booth (@darbooth) January 25, 2013'
}
```
The data fields are the same among all splits.
- `questions`: a `list` of `string` features. 
- `answers`: a `list` of `string` features.
- `paragraph`: a `string` feature.
- `question_answer`: a `string` feature.

## Data Splits

|train|validation|test |
|----:|---------:|----:|
|9489 |      1086| 1203|


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