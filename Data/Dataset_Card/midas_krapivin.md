## Dataset Summary

A dataset for benchmarking keyphrase extraction and generation techniques from long document english scientific papers. For more details about the dataset please refer the original paper - [https://www.semanticscholar.org/paper/Large-Dataset-for-Keyphrases-Extraction-Krapivin-Autaeu/2c56421ff3c2a69894d28b09a656b7157df8eb83](https://www.semanticscholar.org/paper/Large-Dataset-for-Keyphrases-Extraction-Krapivin-Autaeu/2c56421ff3c2a69894d28b09a656b7157df8eb83)
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
| Test | 2305 |


## Usage

### Full Dataset

```python
from datasets import load_dataset

# get entire dataset
dataset = load_dataset("midas/krapivin", "raw")

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

```

### Keyphrase Extraction
```python
from datasets import load_dataset

# get the dataset only for keyphrase extraction
dataset = load_dataset("midas/krapivin", "extraction")

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
dataset = load_dataset("midas/krapivin", "generation")

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
@inproceedings{Krapivin2009LargeDF,
  title={Large Dataset for Keyphrases Extraction},
  author={Mikalai Krapivin and Aliaksandr Autaeu and Maurizio Marchese},
  year={2009}
}

```

## Contributions
Thanks to [@debanjanbhucs](https://github.com/debanjanbhucs), [@dibyaaaaax](https://github.com/dibyaaaaax) and [@ad6398](https://github.com/ad6398) for adding this dataset
