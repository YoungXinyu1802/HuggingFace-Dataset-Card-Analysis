## Dataset Summary

A dataset for benchmarking keyphrase extraction and generation techniques from abstracts of english scientific papers. For more details about the dataset please refer the original paper - [https://aclanthology.org/D14-1150.pdf](https://aclanthology.org/D14-1150.pdf)
Original source of the data - []()


## Dataset Structure


### Data Fields

- **id**: unique identifier of the document.
- **document**: Whitespace separated list of words in the document.
- **doc_bio_tags**: BIO tags for each word in the document. B stands for the beginning of a keyphrase and I stands for inside the keyphrase. O stands for outside the keyphrase and represents the word that isn't a part of the keyphrase at all.
- **extractive_keyphrases**: List of all the present keyphrases.
- **abstractive_keyphrase**: List of all the absent keyphrases.


### Data Splits

|Split| #datapoints  |
|--|--|
| Test | 755 |

- Percentage of keyphrases that are named entities: 56.99% (named entities detected using scispacy - en-core-sci-lg model)
- Percentage of keyphrases that are noun phrases: 54.99% (noun phrases detected using spacy en-core-web-lg after removing determiners)

## Usage

### Full Dataset

```python
from datasets import load_dataset

# get entire dataset
dataset = load_dataset("midas/kdd", "raw")

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
Tokenized Document:  ['Discovering', 'roll-up', 'dependencies']
Document BIO Tags:  ['O', 'O', 'O']
Extractive/present Keyphrases:  []
Abstractive/absent Keyphrases:  ['logical design']

-----------

```

### Keyphrase Extraction
```python
from datasets import load_dataset

# get the dataset only for keyphrase extraction
dataset = load_dataset("midas/kdd", "extraction")

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
dataset = load_dataset("midas/kdd", "generation")

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
