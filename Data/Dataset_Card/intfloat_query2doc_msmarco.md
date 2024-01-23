---
license: cc-by-4.0
language:
- en
size_categories:
- 100K<n<1M
---

### Dataset Summary

This dataset contains GPT-3.5 (`text-davinci-003`) generations from MS-MARCO queries.

[Query2doc: Query Expansion with Large Language Models](https://arxiv.org/pdf/2303.07678.pdf) Liang Wang, Nan Yang and Furu Wei

### Data Instances

An example looks as follows.
```
{
  "query_id": "1030303",
  "query": "who is aziz hashim",
  "pseudo_doc": "Aziz Hashim is a renowned entrepreneur, business leader, and one of the most successful restaurant franchise operators in the US. He is the founder of NRD Capital, a private equity firm focused on investments in multi-unit restaurant franchised businesses. Hashim has built a formidable track record of success in the franchise industry, with brands such as Outback Steakhouse and Jamba Juice. His accomplishments and philanthropic initiatives have earned him numerous awards, including the prestigious Ernst and Young Entrepreneur of the Year award."
}
```

### Data Fields

- `query_id`: a `string` feature.
- `query`: a `string` feature.
- `pseudo_doc`: a `string` feature.

### Data Splits

| train  |   dev |  test |  trec_dl2019 | trec_dl2020 |
|--------|------:|------:|------:|------:|
| 502939 | 6980 | 6837 | 43 | 54 |

### How to use this dataset

```python
from datasets import load_dataset
dataset = load_dataset('intfloat/query2doc_msmarco')

print(dataset['trec_dl2019'][0])
```

### Reproducing our results

We provide a python script [repro_bm25.py](https://huggingface.co/datasets/intfloat/query2doc_msmarco/blob/main/repro_bm25.py) to reproduce our results with BM25 retrieval.

First install some python dependency packages:

```
pip install pyserini==0.15.0 pytrec_eval datasets tqdm
```

Then download and run the python code:

```
python repro_bm25.py
```

This script utilizes the pre-built Lucene index from [Pyserini](https://github.com/castorini/pyserini/blob/pyserini-0.15.0/docs/prebuilt-indexes.md)
and might yield slightly different results compared to the paper.

### Citation Information

```
@inproceedings{Wang2023Query2docQE,
  title={Query2doc: Query Expansion with Large Language Models},
  author={Liang Wang and Nan Yang and Furu Wei},
  year={2023}
}
```
