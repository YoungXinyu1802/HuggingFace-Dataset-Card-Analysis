---
language:
- en
multilinguality:
- monolingual
size_categories:
- 1K<n<10K
task_categories:
- summarization
- text2text-generation
task_ids: []
tags:
- conditional-text-generation
---

# WCEP10 dataset for summarization

Summarization dataset copied from [PRIMERA](https://github.com/allenai/PRIMER)

This dataset is compatible with the [`run_summarization.py`](https://github.com/huggingface/transformers/tree/master/examples/pytorch/summarization) script from Transformers if you add this line to the `summarization_name_mapping` variable:
```python
"ccdv/WCEP-10": ("document", "summary")
```

# Configs
4 possibles configs:
- `roberta` will concatenate documents with "\</s\>" (default)
- `newline` will concatenate documents with "\n"
- `bert` will concatenate documents with "[SEP]"
- `list` will return the list of documents instead of a string

### Data Fields

- `id`: paper id
- `document`: a string/list containing the body of a set of documents
- `summary`: a string containing the abstract of the set

### Data Splits

This dataset has 3 splits: _train_, _validation_, and _test_. \

| Dataset Split | Number of Instances | 
| ------------- | --------------------|
| Train         | 8158                |
| Validation    | 1020                |
| Test          | 1022                |


# Cite original article
```
@article{DBLP:journals/corr/abs-2005-10070,
    author    = {Demian Gholipour Ghalandari and
                Chris Hokamp and
                Nghia The Pham and
                John Glover and
                Georgiana Ifrim},
    title     = {A Large-Scale Multi-Document Summarization Dataset from the Wikipedia
                Current Events Portal},
    journal   = {CoRR},
    volume    = {abs/2005.10070},
    year      = {2020},
    url       = {https://arxiv.org/abs/2005.10070},
    eprinttype = {arXiv},
    eprint    = {2005.10070},
    timestamp = {Fri, 22 May 2020 16:21:28 +0200},
    biburl    = {https://dblp.org/rec/journals/corr/abs-2005-10070.bib},
    bibsource = {dblp computer science bibliography, https://dblp.org}
    }

@article{DBLP:journals/corr/abs-2110-08499,
    author    = {Wen Xiao and
                Iz Beltagy and
                Giuseppe Carenini and
                Arman Cohan},
    title     = {{PRIMER:} Pyramid-based Masked Sentence Pre-training for Multi-document
                Summarization},
    journal   = {CoRR},
    volume    = {abs/2110.08499},
    year      = {2021},
    url       = {https://arxiv.org/abs/2110.08499},
    eprinttype = {arXiv},
    eprint    = {2110.08499},
    timestamp = {Fri, 22 Oct 2021 13:33:09 +0200},
    biburl    = {https://dblp.org/rec/journals/corr/abs-2110-08499.bib},
    bibsource = {dblp computer science bibliography, https://dblp.org}
}
```