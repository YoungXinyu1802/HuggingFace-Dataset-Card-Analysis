---
language: fr
license: cc-by-4.0
multilinguality: monolingual
size_categories: 10K<n<100K
source_datasets: fquad
task_categories:
- text2text-generation
task_ids: []
pretty_name: FQuAD for question generation
tags:
- question-generation
---

# Dataset Card for "lmqg/qg_frquad"
***IMPORTANT***: This is a dummy dataset for [lmqg/qg_frquad](https://huggingface.co/datasets/lmqg/qg_frquad). The original FRQuAD requires to fill a form (https://fquad.illuin.tech/) to get the data, and our lmqg/qg_frquad follows FQuAD's license. If you need lmqg/qg_frquad, please first request the access to FQuAD on their website https://fquad.illuin.tech/ . Once you obtain the access, we will add you to our lmqg group so that you can access https://huggingface.co/datasets/lmqg/qg_frquad.
Leave a comment to the [discussion page](https://huggingface.co/datasets/lmqg/qg_frquad_dummy/discussions/1) to request access to the `lmqg/qg_frquad` after being granted FQuAD access!

## Dataset Description
- **Repository:** [https://github.com/asahi417/lm-question-generation](https://github.com/asahi417/lm-question-generation)
- **Paper:** [https://arxiv.org/abs/2210.03992](https://arxiv.org/abs/2210.03992)
- **Point of Contact:** [Asahi Ushio](http://asahiushio.com/)

### Dataset Summary
This is a subset of [QG-Bench](https://github.com/asahi417/lm-question-generation/blob/master/QG_BENCH.md#datasets), a unified question generation benchmark proposed in
 ["Generative Language Models for Paragraph-Level Question Generation: A Unified Benchmark and Evaluation, EMNLP 2022 main conference"](https://arxiv.org/abs/2210.03992).
This is a modified version of [FQuAD](https://huggingface.co/datasets/fquad) for question generation (QG) task.
Since the original dataset only contains training/validation set, we manually sample test set from training set, which
has no overlap in terms of the paragraph with the training set.

***IMPORTANT NOTE:*** The license of this dataset belongs to [FQuAD](https://fquad.illuin.tech/), so please check the guideline there and request the right to access the dataset [here](https://fquad.illuin.tech/) promptly if you use the datset.

### Supported Tasks and Leaderboards
* `question-generation`: The dataset is assumed to be used to train a model for question generation.
  Success on this task is typically measured by achieving a high BLEU4/METEOR/ROUGE-L/BERTScore/MoverScore (see our paper for more in detail).

### Languages
French (fr)

## Dataset Structure
An example of 'train' looks as follows.
```
{
  'answer': '16 janvier 1377',
  'question': 'Quand est-ce que Grégoire XI arrive à Rome ?',                                                                             
  'sentence': "Le pape poursuit son voyage jusqu'à Rome en passant par Corneto où il parvient le 6 décembre 1376, puis il arrive à Rome le 16 janvier 1377 en remontant le Tibre.",
  'paragraph': "Quant à Catherine, elle part par voie terrestre en passant par Saint-Tropez, Varazze, puis Gênes. C'est dans cette dernière ville que, selon la Legenda minore, elle aurait de nouveau rencontré Grégoire XI. Le pape poursuit son voyage jusqu'à Rome en passant par Corneto où il parvient le 6 décembre 1376, puis il arrive à Rome le 16 janvier 1377 en remontant le Tibre.",
  'sentence_answer': "Le pape poursuit son voyage jusqu'à Rome en passant par Corneto où il parvient le 6 décembre 1376, puis il arrive à Rome le <hl> 16 janvier 1377 <hl> en remontant le Tibre.",
  'paragraph_answer': "Quant à Catherine, elle part par voie terrestre en passant par Saint-Tropez, Varazze, puis Gênes. C'est dans cette dernière ville que, selon la Legenda minore, elle aurait de nouveau rencontré Grégoire XI. Le pape poursuit son voyage jusqu'à Rome en passant par Corneto où il parvient le 6 décembre 1376, puis il arrive à Rome le <hl> 16 janvier 1377 <hl> en remontant le Tibre.",
  'paragraph_sentence': "Quant à Catherine, elle part par voie terrestre en passant par Saint-Tropez, Varazze, puis Gênes. C'est dans cette dernière ville que, selon la Legenda minore, elle aurait de nouveau rencontré Grégoire XI. <hl> Le pape poursuit son voyage jusqu'à Rome en passant par Corneto où il parvient le 6 décembre 1376, puis il arrive à Rome le 16 janvier 1377 en remontant le Tibre. <hl>"
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
|17543|    3188  |3188 |


## Citation Information

```
@inproceedings{ushio-etal-2022-generative,
    title = "{G}enerative {L}anguage {M}odels for {P}aragraph-{L}evel {Q}uestion {G}eneration: {A} {U}nified {B}enchmark and {E}valuation",
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