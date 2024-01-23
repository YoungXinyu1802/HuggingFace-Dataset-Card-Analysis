---
annotations_creators:
- no-annotation
language_creators:
- found
language:
- en
license:
- agpl-3.0
multilinguality:
- monolingual
pretty_name: A Lot of NLI
size_categories:
- 100K<n<1M
source_datasets:
- snli
- multi_nli
- anli
task_categories:
- text-classification
task_ids:
- natural-language-inference
viewer: true
---

# Repo

Github Repo: [thamognya/TBertNLI](https://github.com/thamognya/TBertNLI) specifically in the [src/data directory](https://github.com/thamognya/TBertNLI/tree/master/src/data).

# Sample

```                                             premise                          hypothesis  label
0  this church choir sings to the masses as they ...      the church is filled with song      0
1  this church choir sings to the masses as they ...  a choir singing at a baseball game      2
2  a woman with a green headscarf blue shirt and ...                  the woman is young      1
3  a woman with a green headscarf blue shirt and ...             the woman is very happy      0
4  a woman with a green headscarf blue shirt and ...             the woman has been shot      2
```

# Datsets Origin

As of now the marked datasets have been used to make this dataset and the other ones are todo

- [x] SNLI
- [x] MultiNLI
- SuperGLUE
- FEVER
- WIKI-FACTCHECK
- [x] ANLI
- more from huggingface

# Reasons

Just for finetuning of NLI models and purely made for NLI (not zero shot classification)

