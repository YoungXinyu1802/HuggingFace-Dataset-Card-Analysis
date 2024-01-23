## Dataset Summary

A dataset for benchmarking keyphrase extraction and generation techniques from english news articles. For more details about the dataset please refer the original paper - [https://dl.acm.org/doi/10.5555/1620163.1620205](https://dl.acm.org/doi/10.5555/1620163.1620205)

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
| Test | 308 |


## Usage

### Full Dataset

```python
from datasets import load_dataset

# get entire dataset
dataset = load_dataset("midas/duc2001", "raw")

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
Tokenized Document:  ['Here', ',', 'at', 'a', 'glance', ',', 'are', 'developments', 'today', 'involving', 'the', 'crash', 'of', 'Pan', 'American', 'World', 'Airways', 'Flight', '103', 'Wednesday', 'night', 'in', 'Lockerbie', ',', 'Scotland', ',', 'that', 'killed', 'all', '259', 'people', 'aboard', 'and', 'more', 'than', '20', 'people', 'on', 'the', 'ground', ':']
Document BIO Tags:  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'B', 'I', 'I', 'I', 'I', 'I', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
Extractive/present Keyphrases:  ['pan american world airways flight 103', 'crash', 'lockerbie']
Abstractive/absent Keyphrases:  ['terrorist threats', 'widespread wreckage', 'radical palestinian faction', 'terrorist bombing', 'bomb threat', 'sabotage']

-----------
```

### Keyphrase Extraction
```python
from datasets import load_dataset

# get the dataset only for keyphrase extraction
dataset = load_dataset("midas/duc2001", "extraction")

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
dataset = load_dataset("midas/duc2001", "generation")

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
@inproceedings{10.5555/1620163.1620205,
author = {Wan, Xiaojun and Xiao, Jianguo},
title = {Single Document Keyphrase Extraction Using Neighborhood Knowledge},
year = {2008},
isbn = {9781577353683},
publisher = {AAAI Press},
booktitle = {Proceedings of the 23rd National Conference on Artificial Intelligence - Volume 2},
pages = {855–860},
numpages = {6},
location = {Chicago, Illinois},
series = {AAAI'08}
}
```

## Contributions
Thanks to [@debanjanbhucs](https://github.com/debanjanbhucs), [@dibyaaaaax](https://github.com/dibyaaaaax) and [@ad6398](https://github.com/ad6398) for adding this dataset
