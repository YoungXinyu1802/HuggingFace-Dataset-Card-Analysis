A dataset for benchmarking keyphrase extraction and generation techniques from abstracts of English scientific papers. For more details about the dataset please refer the original paper - [http://memray.me/uploads/acl17-keyphrase-generation.pdf](http://memray.me/uploads/acl17-keyphrase-generation.pdf).

Data source - [https://github.com/memray/seq2seq-keyphrase](https://github.com/memray/seq2seq-keyphrase)

## Dataset Summary
  

## Dataset Structure

## Dataset Statistics 


### Data Fields

- **id**: unique identifier of the document.
- **document**: Whitespace separated list of words in the document.
- **doc_bio_tags**: BIO tags for each word in the document. B stands for the beginning of a keyphrase and I stands for inside the keyphrase. O stands for outside the keyphrase and represents the word that isn't a part of the keyphrase at all.
- **extractive_keyphrases**: List of all the present keyphrases.
- **abstractive_keyphrase**: List of all the absent keyphrases.


### Data Splits

|Split| No. of datapoints  |
|--|--|
| Train | 530,809 |
| Test | 20,000|
| Validation | 20,000|

## Usage

### Full Dataset

```python
from datasets import load_dataset

# get entire dataset
dataset = load_dataset("midas/kp20k", "raw")

# sample from the train split
print("Sample from training dataset split")
train_sample = dataset["train"][0]
print("Fields in the sample: ", [key for key in train_sample.keys()])
print("Tokenized Document: ", train_sample["document"])
print("Document BIO Tags: ", train_sample["doc_bio_tags"])
print("Extractive/present Keyphrases: ", train_sample["extractive_keyphrases"])
print("Abstractive/absent Keyphrases: ", train_sample["abstractive_keyphrases"])
print("\n-----------\n")

# sample from the validation split
print("Sample from validation dataset split")
validation_sample = dataset["validation"][0]
print("Fields in the sample: ", [key for key in validation_sample.keys()])
print("Tokenized Document: ", validation_sample["document"])
print("Document BIO Tags: ", validation_sample["doc_bio_tags"])
print("Extractive/present Keyphrases: ", validation_sample["extractive_keyphrases"])
print("Abstractive/absent Keyphrases: ", validation_sample["abstractive_keyphrases"])
print("\n-----------\n")

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
dataset = load_dataset("midas/kp20k", "extraction")

print("Samples for Keyphrase Extraction")

# sample from the train split
print("Sample from training data split")
train_sample = dataset["train"][0]
print("Fields in the sample: ", [key for key in train_sample.keys()])
print("Tokenized Document: ", train_sample["document"])
print("Document BIO Tags: ", train_sample["doc_bio_tags"])
print("\n-----------\n")

# sample from the validation split
print("Sample from validation data split")
validation_sample = dataset["validation"][0]
print("Fields in the sample: ", [key for key in validation_sample.keys()])
print("Tokenized Document: ", validation_sample["document"])
print("Document BIO Tags: ", validation_sample["doc_bio_tags"])
print("\n-----------\n")

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
dataset = load_dataset("midas/kp20k", "generation")

print("Samples for Keyphrase Generation")

# sample from the train split
print("Sample from training data split")
train_sample = dataset["train"][0]
print("Fields in the sample: ", [key for key in train_sample.keys()])
print("Tokenized Document: ", train_sample["document"])
print("Extractive/present Keyphrases: ", train_sample["extractive_keyphrases"])
print("Abstractive/absent Keyphrases: ", train_sample["abstractive_keyphrases"])
print("\n-----------\n")

# sample from the validation split
print("Sample from validation data split")
validation_sample = dataset["validation"][0]
print("Fields in the sample: ", [key for key in validation_sample.keys()])
print("Tokenized Document: ", validation_sample["document"])
print("Extractive/present Keyphrases: ", validation_sample["extractive_keyphrases"])
print("Abstractive/absent Keyphrases: ", validation_sample["abstractive_keyphrases"])
print("\n-----------\n")

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
Please cite the works below if you use this dataset in your work.

```
@InProceedings{meng-EtAl:2017:Long,
  author    = {Meng, Rui  and  Zhao, Sanqiang  and  Han, Shuguang  and  He, Daqing  and  Brusilovsky, Peter  and  Chi, Yu},
  title     = {Deep Keyphrase Generation},
  booktitle = {Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  month     = {July},
  year      = {2017},
  address   = {Vancouver, Canada},
  publisher = {Association for Computational Linguistics},
  pages     = {582--592},
  url       = {http://aclweb.org/anthology/P17-1054}
}
```


## Contributions
Thanks to [@debanjanbhucs](https://github.com/debanjanbhucs), [@dibyaaaaax](https://github.com/dibyaaaaax), [@UmaGunturi](https://github.com/UmaGunturi) and [@ad6398](https://github.com/ad6398) for adding this dataset
