---
annotations_creators:
- expert-generated

language:
- bn

multilinguality:
- multilingual

size_categories: []
source_datasets: []
tags: []

task_categories:
- text-retrieval

license:
- apache-2.0

task_ids:
- document-retrieval
---

# MIRACL (bn) embedded with cohere.ai `multilingual-22-12` encoder

We encoded the [MIRACL dataset](https://huggingface.co/miracl) using the [cohere.ai](https://txt.cohere.ai/multilingual/) `multilingual-22-12` embedding model.

The query embeddings can be found in [Cohere/miracl-bn-queries-22-12](https://huggingface.co/datasets/Cohere/miracl-bn-queries-22-12) and the corpus embeddings can be found in [Cohere/miracl-bn-corpus-22-12](https://huggingface.co/datasets/Cohere/miracl-bn-corpus-22-12).

For the orginal datasets, see [miracl/miracl](https://huggingface.co/datasets/miracl/miracl) and [miracl/miracl-corpus](https://huggingface.co/datasets/miracl/miracl-corpus).


Dataset info:
> MIRACL 🌍🙌🌏 (Multilingual Information Retrieval Across a Continuum of Languages) is a multilingual retrieval dataset that focuses on search across 18 different languages, which collectively encompass over three billion native speakers around the world.
>
> The corpus for each language is prepared from a Wikipedia dump, where we keep only the plain text and discard images, tables, etc. Each article is segmented into multiple passages using WikiExtractor based on natural discourse units (e.g., `\n\n` in the wiki markup). Each of these passages comprises a "document" or unit of retrieval. We preserve the Wikipedia article title of each passage.

## Embeddings
We compute for `title+" "+text` the embeddings using our `multilingual-22-12` embedding model, a state-of-the-art model that works for semantic search in 100 languages.  If you want to learn more about this model, have a look at [cohere.ai multilingual embedding model](https://txt.cohere.ai/multilingual/).


## Loading the dataset

In [miracl-bn-corpus-22-12](https://huggingface.co/datasets/Cohere/miracl-bn-corpus-22-12) we provide the corpus embeddings. Note, depending on the selected split, the respective files can be quite large.

You can either load the dataset like this:
```python
from datasets import load_dataset
docs = load_dataset(f"Cohere/miracl-bn-corpus-22-12", split="train")
```

Or you can also stream it without downloading it before:
```python
from datasets import load_dataset
docs = load_dataset(f"Cohere/miracl-bn-corpus-22-12", split="train", streaming=True)

for doc in docs:
	docid = doc['docid']
	title = doc['title']
	text = doc['text']
	emb = doc['emb']
```

## Search

Have a look at [miracl-bn-queries-22-12](https://huggingface.co/datasets/Cohere/miracl-bn-queries-22-12) where we provide the query embeddings for the MIRACL dataset.

To search in the documents, you must use **dot-product**. 


And then compare this query embeddings either with a vector database (recommended) or directly computing the dot product.

A full search example:
```python
# Attention! For large datasets, this requires a lot of memory to store
# all document embeddings and to compute the dot product scores.
# Only use this for smaller datasets. For large datasets, use a vector DB

from datasets import load_dataset
import torch

#Load documents + embeddings
docs = load_dataset(f"Cohere/miracl-bn-corpus-22-12", split="train")
doc_embeddings = torch.tensor(docs['emb'])

# Load queries 
queries = load_dataset(f"Cohere/miracl-bn-queries-22-12", split="dev")

# Select the first query as example
qid = 0
query = queries[qid]
query_embedding = torch.tensor(queries['emb'])

# Compute dot score between query embedding and document embeddings
dot_scores = torch.mm(query_embedding, doc_embeddings.transpose(0, 1))
top_k = torch.topk(dot_scores, k=3)

# Print results
print("Query:", query['query'])
for doc_id in top_k.indices[0].tolist():
    print(docs[doc_id]['title'])
    print(docs[doc_id]['text'])
```

You can get embeddings for new queries using our API:
```python
#Run: pip install cohere
import cohere
co = cohere.Client(f"{api_key}")  # You should add your cohere API Key here :))
texts = ['my search query']
response = co.embed(texts=texts, model='multilingual-22-12')
query_embedding = response.embeddings[0] # Get the embedding for the first text
```

## Performance

In the following table we compare the cohere multilingual-22-12 model with Elasticsearch version 8.6.0 lexical search (title and passage indexed as independent fields). Note that Elasticsearch doesn't support all languages that are part of the MIRACL dataset.


We compute nDCG@10 (a ranking based loss), as well as hit@3: Is at least one relevant document in the top-3 results. We find that hit@3 is easier to interpret, as it presents the number of queries for which a relevant document is found among the top-3 results.

Note: MIRACL only annotated a small fraction  of passages (10 per query) for relevancy. Especially for larger Wikipedias (like English), we often found many more relevant passages. This is know as annotation holes. Real nDCG@10 and hit@3 performance is likely higher than depicted.  


| Model | cohere multilingual-22-12 nDCG@10 | cohere multilingual-22-12 hit@3 | ES 8.6.0 nDCG@10 | ES 8.6.0 acc@3 |
|---|---|---|---|---|
| miracl-ar | 64.2 | 75.2 | 46.8 | 56.2 |
| miracl-bn | 61.5 | 75.7 | 49.2 | 60.1 |
| miracl-de | 44.4 | 60.7 | 19.6 | 29.8 |
| miracl-en | 44.6 | 62.2 | 30.2 | 43.2 |
| miracl-es | 47.0 | 74.1 | 27.0 | 47.2 |
| miracl-fi | 63.7 | 76.2 | 51.4 | 61.6 |
| miracl-fr | 46.8 | 57.1 | 17.0 | 21.6 |
| miracl-hi | 50.7 | 62.9 | 41.0 | 48.9 |
| miracl-id | 44.8 | 63.8 | 39.2 | 54.7 |
| miracl-ru | 49.2 | 66.9 | 25.4 | 36.7 |
| **Avg** | 51.7 | 67.5 | 34.7 | 46.0 |

Further languages (not supported by Elasticsearch):
| Model | cohere multilingual-22-12 nDCG@10 | cohere multilingual-22-12 hit@3 |
|---|---|---|
| miracl-fa | 44.8 | 53.6 |
| miracl-ja | 49.0 | 61.0 |
| miracl-ko | 50.9 | 64.8 |
| miracl-sw | 61.4 | 74.5 |
| miracl-te | 67.8 | 72.3 |
| miracl-th | 60.2 | 71.9 |
| miracl-yo | 56.4 | 62.2 |
| miracl-zh | 43.8 | 56.5 |
| **Avg** | 54.3 | 64.6 |

