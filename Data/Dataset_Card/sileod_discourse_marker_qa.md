---
annotations_creators:
- expert-generated
language_creators:
- crowdsourced
language:
- en
license:
- apache-2.0
multilinguality:
- monolingual
pretty_name: 'discourse_marker_qa'
size_categories:
- n<1K
source_datasets:
- original
task_categories:
- question-answering
- multiple-choice
task_ids:
- open-domain-qa
- multiple-choice-qa
---

# Dataset for evaluation of (zero-shot) discourse marker prediction with language models

This is the Big-Bench version of our discourse marker prediction dataset, [Discovery](https://huggingface.co/datasets/discovery)

Design considerations:
<https://github.com/google/BIG-bench/tree/main/bigbench/benchmark_tasks/discourse_marker_prediction>

GPT2 has to zero-shot 15% accuracy with on this multiple-choice task based on language modeling perplexity. As a comparison, a fully supervised model, trained with 10k examples per marker with ROBERTA and default hyperparameters with one epoch, leads to an accuracy of 30% with 174 possible markers. This shows that this task is hard for GPT2 and that the model didn't memorize the discourse markers, but that high accuracies are still possible.

# Citation
```
@inproceedings{sileo-etal-2019-mining,
    title = "Mining Discourse Markers for Unsupervised Sentence Representation Learning",
    author = "Sileo, Damien  and
      Van De Cruys, Tim  and
      Pradel, Camille  and
      Muller, Philippe",
    booktitle = "Proceedings of the 2019 Conference of the North {A}merican Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers)",
    month = jun,
    year = "2019",
    address = "Minneapolis, Minnesota",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/N19-1351",
    doi = "10.18653/v1/N19-1351",
    pages = "3477--3486",
}
```