---
license: cc-by-4.0
pretty_name: Synthetic QA dataset.
language: en
multilinguality: monolingual
size_categories: 10K<n<100K
source_datasets:
- extended|wikipedia
task_categories:
- question-answering
task_ids:
- extractive-qa
---

# Dataset Card for "lmqg/qa_harvesting_from_wikipedia_pseudo"

## Dataset Description
- **Repository:** [https://github.com/asahi417/lm-question-generation](https://github.com/asahi417/lm-question-generation)
- **Paper:** [https://arxiv.org/abs/2210.03992](https://arxiv.org/abs/2210.03992)
- **Point of Contact:** [Asahi Ushio](http://asahiushio.com/)

### Dataset Summary
This is a synthetic QA dataset generated with fine-tuned QG models over [`lmqg/qa_harvesting_from_wikipedia`](https://huggingface.co/datasets/lmqg/qa_harvesting_from_wikipedia), 1 million paragraph and answer pairs collected in [Du and Cardie, 2018](https://aclanthology.org/P18-1177/), made for question-answering based evaluation (QAE) for question generation model proposed by [Zhang and Bansal, 2019](https://aclanthology.org/D19-1253/).
The `train` split is the synthetic data and the `validation` split is the original validation set of [SQuAD](https://rajpurkar.github.io/SQuAD-explorer/), where the model should be evaluate on.

This contains synthetic QA datasets created with the following QG models:
- [lmqg/bart-base-squad](https://huggingface.co/lmqg/bart-base-squad)
- [lmqg/bart-large-squad](https://huggingface.co/lmqg/bart-large-squad)
- [lmqg/t5-small-squad](https://huggingface.co/lmqg/t5-small-squad)
- [lmqg/t5-base-squad](https://huggingface.co/lmqg/t5-base-squad)
- [lmqg/t5-large-squad](https://huggingface.co/lmqg/t5-large-squad)

See more detail about the QAE at [https://github.com/asahi417/lm-question-generation/tree/master/misc/qa_based_evaluation](https://github.com/asahi417/lm-question-generation/tree/master/misc/emnlp_2022/qa_based_evaluation).

### Supported Tasks and Leaderboards
* `question-answering`

### Languages
English (en)

## Dataset Structure

### Data Fields
The data fields are the same among all splits.

#### plain_text

- `id`: a `string` feature of id
- `title`: a `string` feature of title of the paragraph 
- `context`: a `string` feature of paragraph 
- `question`: a `string` feature of question
- `answers`: a `json` feature of answers

### Data Splits

|train    |validation|
|--------:|---------:|
|1,092,142|   10,570 |

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