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

# Dataset Card for "lmqg/qag_tweetqa"


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
  "paragraph": "I would hope that Phylicia Rashad would apologize now that @missjillscott has! You cannot discount 30 victims who come with similar stories.— JDWhitner (@JDWhitner) July 7, 2015",
  "questions": [ "what should phylicia rashad do now?", "how many victims have come forward?" ],
  "answers": [ "apologize", "30" ],
  "questions_answers": "Q: what should phylicia rashad do now?, A: apologize Q: how many victims have come forward?, A: 30"
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
|4536 |       583|  583|


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