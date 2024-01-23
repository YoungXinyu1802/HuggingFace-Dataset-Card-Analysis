---
annotations_creators: []
language_creators: []
language:
- en
license:
- cc-by-sa-3.0
multilinguality:
- monolingual
pretty_name: VitaminC
size_categories:
- 100K<n<1M
source_datasets: []
task_categories:
- text-classification
task_ids:
- fact-checking
- natural-language-inference
---

# Details
Fact Verification dataset created for [Get Your Vitamin C! Robust Fact Verification with Contrastive Evidence](https://aclanthology.org/2021.naacl-main.52/) (Schuster et al., NAACL 21`) based on Wikipedia edits (revisions).

For more details see: https://github.com/TalSchuster/VitaminC

When using this dataset, please cite the paper:

# BibTeX entry and citation info

```bibtex
@inproceedings{schuster-etal-2021-get,
    title = "Get Your Vitamin {C}! Robust Fact Verification with Contrastive Evidence",
    author = "Schuster, Tal  and
      Fisch, Adam  and
      Barzilay, Regina",
    booktitle = "Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies",
    month = jun,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.naacl-main.52",
    doi = "10.18653/v1/2021.naacl-main.52",
    pages = "624--643",
    abstract = "Typical fact verification models use retrieved written evidence to verify claims. Evidence sources, however, often change over time as more information is gathered and revised. In order to adapt, models must be sensitive to subtle differences in supporting evidence. We present VitaminC, a benchmark infused with challenging cases that require fact verification models to discern and adjust to slight factual changes. We collect over 100,000 Wikipedia revisions that modify an underlying fact, and leverage these revisions, together with additional synthetically constructed ones, to create a total of over 400,000 claim-evidence pairs. Unlike previous resources, the examples in VitaminC are contrastive, i.e., they contain evidence pairs that are nearly identical in language and content, with the exception that one supports a given claim while the other does not. We show that training using this design increases robustness{---}improving accuracy by 10{\%} on adversarial fact verification and 6{\%} on adversarial natural language inference (NLI). Moreover, the structure of VitaminC leads us to define additional tasks for fact-checking resources: tagging relevant words in the evidence for verifying the claim, identifying factual revisions, and providing automatic edits via factually consistent text generation.",
}
```