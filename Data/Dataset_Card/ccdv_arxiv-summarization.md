---
language:
- en
multilinguality:
- monolingual
size_categories:
- 100K<n<1M
task_categories:
- summarization
- text-generation
task_ids: []
tags:
- conditional-text-generation
train-eval-index:
- config: document
  task: summarization
  task_id: summarization
  splits:
    eval_split: test
  col_mapping:
    article: text
    abstract: target
---

# Arxiv dataset for summarization

Dataset for summarization of long documents.\
Adapted from this [repo](https://github.com/armancohan/long-summarization).\
Note that original data are pre-tokenized so this dataset returns " ".join(text) and add "\n" for paragraphs. \
This dataset is compatible with the [`run_summarization.py`](https://github.com/huggingface/transformers/tree/master/examples/pytorch/summarization) script from Transformers if you add this line to the `summarization_name_mapping` variable:
```python
"ccdv/arxiv-summarization": ("article", "abstract")
```

### Data Fields

- `id`: paper id
- `article`: a string containing the body of the paper
- `abstract`: a string containing the abstract of the paper

### Data Splits

This dataset has 3 splits: _train_, _validation_, and _test_. \
Token counts are white space based.

| Dataset Split | Number of Instances |     Avg. tokens       |
| ------------- | --------------------|:----------------------|
| Train         | 203,037             |      6038 / 299       |
| Validation    | 6,436               |      5894 / 172       |
| Test          | 6,440               |      5905 / 174       |


# Cite original article
```
@inproceedings{cohan-etal-2018-discourse,
  title = "A Discourse-Aware Attention Model for Abstractive Summarization of Long Documents",
  author = "Cohan, Arman  and
    Dernoncourt, Franck  and
    Kim, Doo Soon  and
    Bui, Trung  and
    Kim, Seokhwan  and
    Chang, Walter  and
    Goharian, Nazli",
  booktitle = "Proceedings of the 2018 Conference of the North {A}merican Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 2 (Short Papers)",
  month = jun,
  year = "2018",
  address = "New Orleans, Louisiana",
  publisher = "Association for Computational Linguistics",
  url = "https://aclanthology.org/N18-2097",
  doi = "10.18653/v1/N18-2097",
  pages = "615--621",
  abstract = "Neural abstractive summarization models have led to promising results in summarizing relatively short documents. We propose the first model for abstractive summarization of single, longer-form documents (e.g., research papers). Our approach consists of a new hierarchical encoder that models the discourse structure of a document, and an attentive discourse-aware decoder to generate the summary. Empirical results on two large-scale datasets of scientific papers show that our model significantly outperforms state-of-the-art models.",
}
```

