---
license: cc-by-4.0
pretty_name: SQuAD for question generation
language: en
multilinguality: monolingual
size_categories: 10K<n<100K
source_datasets: squad
task_categories:
- text-generation
task_ids:
- language-modeling
tags:
- question-generation
---

# Dataset Card for "lmqg/qg_squad"

## Dataset Description
- **Repository:** [https://github.com/asahi417/lm-question-generation](https://github.com/asahi417/lm-question-generation)
- **Paper:** [https://arxiv.org/abs/2210.03992](https://arxiv.org/abs/2210.03992)
- **Point of Contact:** [Asahi Ushio](http://asahiushio.com/)

### Dataset Summary
This is a subset of [QG-Bench](https://github.com/asahi417/lm-question-generation/blob/master/QG_BENCH.md#datasets), a unified question generation benchmark proposed in
 ["Generative Language Models for Paragraph-Level Question Generation: A Unified Benchmark and Evaluation, EMNLP 2022 main conference"](https://arxiv.org/abs/2210.03992).
This is [SQuAD](https://rajpurkar.github.io/SQuAD-explorer/) dataset for question generation (QG) task. The split 
of train/development/test set follows the ["Neural Question Generation"](https://arxiv.org/abs/1705.00106) work and is 
compatible with the [leader board](https://paperswithcode.com/sota/question-generation-on-squad11).


### Supported Tasks and Leaderboards
* `question-generation`: The dataset is assumed to be used to train a model for question generation.
  Success on this task is typically measured by achieving a high BLEU4/METEOR/ROUGE-L/BERTScore/MoverScore (see our paper for more in detail).
  This task has an active leaderboard which can be found at [here](https://paperswithcode.com/sota/question-generation-on-squad11).

### Languages
English (en)

## Dataset Structure
An example of 'train' looks as follows.
```
{
  "question": "What is heresy mainly at odds with?",
  "paragraph": "Heresy is any provocative belief or theory that is strongly at variance with established beliefs or customs. A heretic is a proponent of such claims or beliefs. Heresy is distinct from both apostasy, which is the explicit renunciation of one's religion, principles or cause, and blasphemy, which is an impious utterance or action concerning God or sacred things.",
  "answer": "established beliefs or customs",
  "sentence": "Heresy is any provocative belief or theory that is strongly at variance with established beliefs or customs .",
  "paragraph_sentence": "<hl> Heresy is any provocative belief or theory that is strongly at variance with established beliefs or customs . <hl> A heretic is a proponent of such claims or beliefs. Heresy is distinct from both apostasy, which is the explicit renunciation of one's religion, principles or cause, and blasphemy, which is an impious utterance or action concerning God or sacred things.",
  "paragraph_answer": "Heresy is any provocative belief or theory that is strongly at variance with <hl> established beliefs or customs <hl>. A heretic is a proponent of such claims or beliefs. Heresy is distinct from both apostasy, which is the explicit renunciation of one's religion, principles or cause, and blasphemy, which is an impious utterance or action concerning God or sacred things.",
  "sentence_answer": "Heresy is any provocative belief or theory that is strongly at variance with <hl> established beliefs or customs <hl> ."
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
|75722|     10570|11877|


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