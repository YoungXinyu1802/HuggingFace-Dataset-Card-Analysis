## Dataset Summary

A dataset for benchmarking keyphrase extraction and generation techniques from abstract of english scientific articles. For more details about the dataset please refer the original paper - [https://aclanthology.org/D14-1150/](https://aclanthology.org/D14-1150/)

Original source of the data - []()


## Dataset Structure
Table 1: Statistics on the length of the abstractive keyphrases for Test split of www dataset.

|             |  Test  |
|:-----------:|:------:|
| Single word | 28.21% |
|  Two words  | 47.65% |
| Three words | 15.20% |
|  Four words |  8.04% |
|  Five words |  0.65% |
|  Six words  |  0.12% |
| Seven words |  0.05% |
| Eight words |  0.05% |

Table 2: Statistics on the length of the extractive keyphrases for Test split of www dataset.

|             |  Test  |
|:-----------:|:------:|
| Single word | 44.09% |
|  Two words  | 48.07% |
| Three words |  7.20% |
|  Four words |  0.45% |
|  Five words |  0.16% |

Table 3: General statistics about www dataset.

|                 Type of Analysis                 |         Test        |
|:------------------------------------------------:|:-------------------:|
|                  Annotator Type                  | Authors and Readers |
|                   Document Type                  | Scientific Articles |
|                 No. of Documents                 |         1330        |
|           Avg. Document length (words)           |        163.51       |
|            Max Document length (words)           |         587         |
|  Max no. of abstractive keyphrases in a document |          13         |
|  Min no. of abstractive keyphrases in a document |          0          |
| Avg. no. of abstractive keyphrases  per document |         2.98        |
|  Max no. of extractive keyphrases in a document  |          9          |
|  Min no. of extractive keyphrases in a document  |          0          |
|  Avg. no. of extractive keyphrases  per document |         1.81        |


### Data Fields

- **id**: unique identifier of the document.
- **document**: Whitespace separated list of words in the document.
- **doc_bio_tags**: BIO tags for each word in the document. B stands for the beginning of a keyphrase and I stands for inside the keyphrase. O stands for outside the keyphrase and represents the word that isn't a part of the keyphrase at all.
- **extractive_keyphrases**: List of all the present keyphrases.
- **abstractive_keyphrase**: List of all the absent keyphrases.


### Data Splits

|Split| #datapoints  |
|--|--|
| Test | 1330 |


## Usage

### Full Dataset

```python
from datasets import load_dataset

# get entire dataset
dataset = load_dataset("midas/www", "raw")

# sample from the test split
print("Sample from test dataset split")
test_sample = dataset["test"][0]
print("Fields in the sample: ", [key for key in test_sample.keys()])
print("Tokenized Document: ", test_sample["document"])
print("Document BIO Tags: ", test_sample["doc_bio_tags"])
print("Extractive/present Keyphrases: ", test_sample["extractive_keyphrases"])
print("Abstractive/absent Keyphrases: ", test_sample["abstractive_keyphrases"])
print("\n-----------\n")
```
**Output**

```bash
Sample from test data split
Fields in the sample:  ['id', 'document', 'doc_bio_tags', 'extractive_keyphrases', 'abstractive_keyphrases', 'other_metadata']
Tokenized Document:  ['The', 'web', 'of', 'nations', 'In', 'this', 'paper', ',', 'we', 'report', 'on', 'a', 'large-scale', 'study', 'of', 'structural', 'differences', 'among', 'the', 'national', 'webs', '.', 'The', 'study', 'is', 'based', 'on', 'a', 'web-scale', 'crawl', 'conducted', 'in', 'the', 'summer', '2008', '.', 'More', 'specifically', ',', 'we', 'study', 'two', 'graphs', 'derived', 'from', 'this', 'crawl', ',', 'the', 'nation', 'graph', ',', 'with', 'nodes', 'corresponding', 'to', 'nations', 'and', 'edges', '-', 'to', 'links', 'among', 'nations', ',', 'and', 'the', 'host', 'graph', ',', 'with', 'nodes', 'corresponding', 'to', 'hosts', 'and', 'edges', '-', 'to', 'hyperlinks', 'among', 'pages', 'on', 'the', 'hosts', '.', 'Contrary', 'to', 'some', 'of', 'the', 'previous', 'work', '(', '2', ')', ',', 'our', 'results', 'show', 'that', 'webs', 'of', 'different', 'nations', 'are', 'often', 'very', 'different', 'from', 'each', 'other', ',', 'both', 'in', 'terms', 'of', 'their', 'internal', 'structure', ',', 'and', 'in', 'terms', 'of', 'their', 'connectivity', 'with', 'other', 'nations', '.']
Document BIO Tags:  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
Extractive/present Keyphrases:  ['host graph', 'nation graph']
Abstractive/absent Keyphrases:  ['web graph', 'web structure']

-----------

```

### Keyphrase Extraction
```python
from datasets import load_dataset

# get the dataset only for keyphrase extraction
dataset = load_dataset("midas/www", "extraction")

print("Samples for Keyphrase Extraction")

# sample from the test split
print("Sample from test data split")
test_sample = dataset["test"][0]
print("Fields in the sample: ", [key for key in test_sample.keys()])
print("Tokenized Document: ", test_sample["document"])
print("Document BIO Tags: ", test_sample["doc_bio_tags"])
print("\n-----------\n")
```

### Keyphrase Generation
```python
# get the dataset only for keyphrase generation
dataset = load_dataset("midas/www", "generation")

print("Samples for Keyphrase Generation")

# sample from the test split
print("Sample from test data split")
test_sample = dataset["test"][0]
print("Fields in the sample: ", [key for key in test_sample.keys()])
print("Tokenized Document: ", test_sample["document"])
print("Extractive/present Keyphrases: ", test_sample["extractive_keyphrases"])
print("Abstractive/absent Keyphrases: ", test_sample["abstractive_keyphrases"])
print("\n-----------\n")
```

## Citation Information
```
@inproceedings{caragea-etal-2014-citation,
    title = "Citation-Enhanced Keyphrase Extraction from Research Papers: A Supervised Approach",
    author = "Caragea, Cornelia  and
      Bulgarov, Florin Adrian  and
      Godea, Andreea  and
      Das Gollapalli, Sujatha",
    booktitle = "Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing ({EMNLP})",
    month = oct,
    year = "2014",
    address = "Doha, Qatar",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/D14-1150",
    doi = "10.3115/v1/D14-1150",
    pages = "1435--1446",
}


```

## Contributions
Thanks to [@debanjanbhucs](https://github.com/debanjanbhucs), [@dibyaaaaax](https://github.com/dibyaaaaax) and [@ad6398](https://github.com/ad6398) for adding this dataset
