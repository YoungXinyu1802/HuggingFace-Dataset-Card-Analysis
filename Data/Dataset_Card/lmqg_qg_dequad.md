---
license: cc-by-4.0
pretty_name: GermanQuAD for question generation
language: de
multilinguality: monolingual
size_categories: 10K<n<100K
source_datasets: deepset/germanquad
task_categories:
- text-generation
task_ids:
- language-modeling
tags:
- question-generation
---

# Dataset Card for "lmqg/qg_dequad"

## Dataset Description
- **Repository:** [https://github.com/asahi417/lm-question-generation](https://github.com/asahi417/lm-question-generation)
- **Paper:** [https://arxiv.org/abs/2210.03992](https://arxiv.org/abs/2210.03992)
- **Point of Contact:** [Asahi Ushio](http://asahiushio.com/)

### Dataset Summary
This is a subset of [QG-Bench](https://github.com/asahi417/lm-question-generation/blob/master/QG_BENCH.md#datasets), a unified question generation benchmark proposed in
 ["Generative Language Models for Paragraph-Level Question Generation: A Unified Benchmark and Evaluation, EMNLP 2022 main conference"](https://arxiv.org/abs/2210.03992).
This is a modified version of [GermanQuAD](https://huggingface.co/datasets/deepset/germanquad) for question generation (QG) task.
Since the original dataset only contains training/validation set, we manually sample test set from training set, which
has no overlap in terms of the paragraph with the training set.

### Supported Tasks and Leaderboards
* `question-generation`: The dataset is assumed to be used to train a model for question generation.
  Success on this task is typically measured by achieving a high BLEU4/METEOR/ROUGE-L/BERTScore/MoverScore (see our paper for more in detail).

### Languages
Spanish (es)

## Dataset Structure
An example of 'train' looks as follows.
```
{
  'answer': 'elektromagnetischer Linearführungen',                                                                                                                                                                   
  'question': 'Was kann den Verschleiß des seillosen Aufzuges minimieren?',                                                                                                                                          
  'sentence': 'Im Rahmen der Forschungen an dem seillosen Aufzug wird ebenfalls an der Entwicklung elektromagnetischer Linearführungen gearbeitet, um den Verschleiß der seillosen Aufzugsanlage bei hohem Fahrkomfort zu minimieren.',                                   
  'paragraph': "Aufzugsanlage\n\n=== Seilloser Aufzug ===\nAn der RWTH Aachen im Institut für Elektrische Maschinen wurde ein seilloser Aufzug entwickelt und ein Prototyp aufgebaut. Die Kabine wird hierbei durch z..."
  'sentence_answer': "Im Rahmen der Forschungen an dem seillosen Aufzug wird ebenfalls an der Entwicklung <hl> elektromagnetischer Linearführungen <hl> gearbeitet, um den Verschleiß der seillosen Aufzugsanlage bei...",                  
  'paragraph_answer': "Aufzugsanlage === Seilloser Aufzug === An der RWTH Aachen im Institut für Elektrische Maschinen wurde ein seilloser Aufzug entwickelt und ein Prototyp aufgebaut. Die Kabine wird hierbei durc...",
  'paragraph_sentence': "Aufzugsanlage === Seilloser Aufzug === An der RWTH Aachen im Institut für Elektrische Maschinen wurde ein seilloser Aufzug entwickelt und ein Prototyp aufgebaut. Die Kabine wird hierbei du..."  
}
```
## Data Fields
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

|train|validation|test |
|----:|---------:|----:|
|9314 |     2204 | 2204|


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