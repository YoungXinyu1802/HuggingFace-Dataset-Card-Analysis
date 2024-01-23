# MS MARCO Passages Hard Negatives

[MS MARCO](https://microsoft.github.io/msmarco/) is a large scale information retrieval corpus that was created based on real user search queries using Bing search engine.

This dataset repository contains files that are helpful to train bi-encoder models e.g. using [sentence-transformers](https://www.sbert.net).

## Training Code
You can find here an example how these files can be used to train bi-encoders: [SBERT.net - MS MARCO - MarginMSE](https://www.sbert.net/examples/training/ms_marco/README.html#marginmse)

## cross-encoder-ms-marco-MiniLM-L-6-v2-scores.pkl.gz

This is a pickled dictionary in the format: `scores[qid][pid] -> cross_encoder_score`

It contains 160 million cross-encoder scores for (query, paragraph) pairs using the [cross-encoder/ms-marco-MiniLM-L-6-v2](https://huggingface.co/cross-encoder/ms-marco-MiniLM-L-6-v2) model.

## msmarco-hard-negatives.jsonl.gz
This is a jsonl file: Each line is a JSON object. It has the following format:
```
{"qid": 867436, "pos": [5238393], "neg": {"bm25": [...], ...}}
```

`qid` is the query-ID from MS MARCO, `pos` is a list with paragraph IDs for positive passages. `neg` is a dictionary where we mined hard negatives using different (mainly dense retrieval) systems.

It contains hard negatives mined from BM25 (using ElasticSearch) and the following dense models:
```
msmarco-distilbert-base-tas-b
msmarco-distilbert-base-v3
msmarco-MiniLM-L-6-v3
distilbert-margin_mse-cls-dot-v2
distilbert-margin_mse-cls-dot-v1
distilbert-margin_mse-mean-dot-v1
mpnet-margin_mse-mean-v1
co-condenser-margin_mse-cls-v1
distilbert-margin_mse-mnrl-mean-v1
distilbert-margin_mse-sym_mnrl-mean-v1
distilbert-margin_mse-sym_mnrl-mean-v2
co-condenser-margin_mse-sym_mnrl-mean-v1
```

From each system, 50 most similar paragraphs were mined for a given query.
