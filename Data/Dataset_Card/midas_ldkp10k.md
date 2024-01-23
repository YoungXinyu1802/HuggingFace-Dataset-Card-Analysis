A dataset for benchmarking keyphrase extraction and generation techniques from long document English scientific papers. For more details about the dataset please refer the original paper - []().

Data source - []()

## Dataset Summary
 

## Dataset Structure


### Data Fields

- **id**: unique identifier of the document.
- **sections**: list of all the sections present in the document.
- **sec_text**: list of white space separated list of words present in each section.
- **sec_bio_tags**: list of BIO tags of white space separated list of words present in each section.
- **extractive_keyphrases**: List of all the present keyphrases.
- **abstractive_keyphrase**: List of all the absent keyphrases.


### Data Splits

|Split| #datapoints  |
|--|--|
| Train-Small | 20,000 |
| Train-Medium | 50,000 |
| Train-Large | 1,296,613 |
| Test | 10,000 |
| Validation | 10,000 |

## Usage

### Small Dataset

```python
from datasets import load_dataset

# get small dataset
dataset = load_dataset("midas/ldkp10k", "small")

def order_sections(sample):
  """
  corrects the order in which different sections appear in the document.
  resulting order is: title, abstract, other sections in the body
  """
  
  sections = []
  sec_text = []
  sec_bio_tags = []

  if "title" in sample["sections"]:
    title_idx = sample["sections"].index("title")
    sections.append(sample["sections"].pop(title_idx))
    sec_text.append(sample["sec_text"].pop(title_idx))
    sec_bio_tags.append(sample["sec_bio_tags"].pop(title_idx))

  if "abstract" in sample["sections"]:
    abstract_idx = sample["sections"].index("abstract")
    sections.append(sample["sections"].pop(abstract_idx))
    sec_text.append(sample["sec_text"].pop(abstract_idx))
    sec_bio_tags.append(sample["sec_bio_tags"].pop(abstract_idx))

  sections += sample["sections"]
  sec_text += sample["sec_text"]
  sec_bio_tags += sample["sec_bio_tags"]

  return sections, sec_text, sec_bio_tags


# sample from the train split
print("Sample from train data split")
train_sample = dataset["train"][0]

sections, sec_text, sec_bio_tags = order_sections(train_sample)
print("Fields in the sample: ", [key for key in train_sample.keys()])
print("Section names: ", sections)
print("Tokenized Document: ", sec_text)
print("Document BIO Tags: ", sec_bio_tags)
print("Extractive/present Keyphrases: ", train_sample["extractive_keyphrases"])
print("Abstractive/absent Keyphrases: ", train_sample["abstractive_keyphrases"])
print("\n-----------\n")

# sample from the validation split
print("Sample from validation data split")
validation_sample = dataset["validation"][0]

sections, sec_text, sec_bio_tags = order_sections(validation_sample)
print("Fields in the sample: ", [key for key in validation_sample.keys()])
print("Section names: ", sections)
print("Tokenized Document: ", sec_text)
print("Document BIO Tags: ", sec_bio_tags)
print("Extractive/present Keyphrases: ", validation_sample["extractive_keyphrases"])
print("Abstractive/absent Keyphrases: ", validation_sample["abstractive_keyphrases"])
print("\n-----------\n")

# sample from the test split
print("Sample from test data split")
test_sample = dataset["test"][0]

sections, sec_text, sec_bio_tags = order_sections(test_sample)
print("Fields in the sample: ", [key for key in test_sample.keys()])
print("Section names: ", sections)
print("Tokenized Document: ", sec_text)
print("Document BIO Tags: ", sec_bio_tags)
print("Extractive/present Keyphrases: ", test_sample["extractive_keyphrases"])
print("Abstractive/absent Keyphrases: ", test_sample["abstractive_keyphrases"])
print("\n-----------\n")

```

**Output**
```bash

```

### Medium Dataset

```python
from datasets import load_dataset

# get medium dataset
dataset = load_dataset("midas/ldkp10k", "medium")
```

### Large Dataset

```python
from datasets import load_dataset

# get large dataset
dataset = load_dataset("midas/ldkp10k", "large")
```

## Citation Information
Please cite the works below if you use this dataset in your work.

```
@article{mahata2022ldkp,
  title={LDKP: A Dataset for Identifying Keyphrases from Long Scientific Documents},
  author={Mahata, Debanjan and Agarwal, Naveen and Gautam, Dibya and Kumar, Amardeep and Parekh, Swapnil and Singla, Yaman Kumar and Acharya, Anish and Shah, Rajiv Ratn},
  journal={arXiv preprint arXiv:2203.15349},
  year={2022}
}
```
```
@article{lo2019s2orc,
  title={S2ORC: The semantic scholar open research corpus},
  author={Lo, Kyle and Wang, Lucy Lu and Neumann, Mark and Kinney, Rodney and Weld, Dan S},
  journal={arXiv preprint arXiv:1911.02782},
  year={2019}
}
```
```
@inproceedings{ccano2019keyphrase,
  title={Keyphrase generation: A multi-aspect survey},
  author={{\c{C}}ano, Erion and Bojar, Ond{\v{r}}ej},
  booktitle={2019 25th Conference of Open Innovations Association (FRUCT)},
  pages={85--94},
  year={2019},
  organization={IEEE}
}
```
```
@article{meng2017deep,
  title={Deep keyphrase generation},
  author={Meng, Rui and Zhao, Sanqiang and Han, Shuguang and He, Daqing and Brusilovsky, Peter and Chi, Yu},
  journal={arXiv preprint arXiv:1704.06879},
  year={2017}
}
```

## Contributions
Thanks to [@debanjanbhucs](https://github.com/debanjanbhucs), [@dibyaaaaax](https://github.com/dibyaaaaax), [@UmaGunturi](https://github.com/UmaGunturi) and [@ad6398](https://github.com/ad6398) for adding this dataset
