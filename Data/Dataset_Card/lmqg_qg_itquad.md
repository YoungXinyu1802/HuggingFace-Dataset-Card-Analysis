---
license: cc-by-4.0
pretty_name: SQuAD-it for question generation
language: it
multilinguality: monolingual
size_categories: 10K<n<100K
source_datasets: squad_es
task_categories:
- text-generation
task_ids:
- language-modeling
tags:
- question-generation
---

# Dataset Card for "lmqg/qg_itquad"

## Dataset Description
- **Repository:** [https://github.com/asahi417/lm-question-generation](https://github.com/asahi417/lm-question-generation)
- **Paper:** [https://arxiv.org/abs/2210.03992](https://arxiv.org/abs/2210.03992)
- **Point of Contact:** [Asahi Ushio](http://asahiushio.com/)

### Dataset Summary
This is a subset of [QG-Bench](https://github.com/asahi417/lm-question-generation/blob/master/QG_BENCH.md#datasets), a unified question generation benchmark proposed in
 ["Generative Language Models for Paragraph-Level Question Generation: A Unified Benchmark and Evaluation, EMNLP 2022 main conference"](https://arxiv.org/abs/2210.03992).
This is a modified version of [SQuAD-it](https://huggingface.co/datasets/squad_it) for question generation (QG) task.
Since the original dataset only contains training/validation set, we manually sample test set from training set, which
has no overlap in terms of the paragraph with the training set.

### Supported Tasks and Leaderboards
* `question-generation`: The dataset is assumed to be used to train a model for question generation.
  Success on this task is typically measured by achieving a high BLEU4/METEOR/ROUGE-L/BERTScore/MoverScore (see our paper for more in detail).

### Languages
Italian (it)

## Dataset Structure
An example of 'train' looks as follows.
```
{
  'answer': 'Carlo III',
  'question': "Il figlio di chi è morto sulla strada per Palermo e vi è sepolto?",
  'sentence': 'Carlo III scelse Palermo per la sua incoronazione come Re di Sicilia.',
  'paragraph': 'Dopo il trattato di Utrecht (1713), la Sicilia fu consegnata ai Savoia, ma nel 1734 fu nuovamente posseduta dai...',
  'sentence_answer': '<hl> Carlo III <hl> scelse Palermo per la sua incoronazione come Re di Sicilia.',
  'paragraph_answer': "Dopo il trattato di Utrecht (1713), la Sicilia fu consegnata ai Savoia, ma nel 1734 fu nuovamente posseduta dai borbonici. <hl> Carlo III <hl> scelse Palermo per la sua incoronazione come Re di Sicilia. Charles fece costruire nuove case per la popolazione in crescita, mentre il commercio e l' industria crebbero. Tuttavia, ormai Palermo era ora solo un' altra città provinciale, dato che la Corte Reale risiedeva a Napoli. Il figlio di Carlo Ferdinando, anche se non gradito dalla popolazione, si rifugiò a Palermo dopo la Rivoluzione francese del 1798. Suo figlio Alberto è morto sulla strada per Palermo ed è sepolto in città. Quando fu fondato il Regno delle Due Sicilie, la capitale originaria era Palermo (1816) ma un anno dopo si trasferì a Napoli.",
  'paragraph_sentence': "Dopo il trattato di Utrecht (1713), la Sicilia fu consegnata ai Savoia, ma nel 1734 fu nuovamente posseduta dai borbonici. <hl> Carlo III scelse Palermo per la sua incoronazione come Re di Sicilia. <hl> Charles fece costruire nuove case per la popolazione in crescita, mentre il commercio e l' industria crebbero. Tuttavia, ormai Palermo era ora solo un' altra città provinciale, dato che la Corte Reale risiedeva a Napoli. Il figlio di Carlo Ferdinando, anche se non gradito dalla popolazione, si rifugiò a Palermo dopo la Rivoluzione francese del 1798. Suo figlio Alberto è morto sulla strada per Palermo ed è sepolto in città. Quando fu fondato il Regno delle Due Sicilie, la capitale originaria era Palermo (1816) ma un anno dopo si trasferì a Napoli."
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
|46550|    7609 |7609|


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