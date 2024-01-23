---
dataset_info:
  features:
  - name: text
    dtype: string
  - name: __index_level_0__
    dtype: int64
  splits:
  - name: test
    num_bytes: 12621022
    num_examples: 7187
  - name: train
    num_bytes: 618776029
    num_examples: 352137
  download_size: 409914919
  dataset_size: 631397051
license: mit
language:
- sv
tags:
- historical
- WIP
pretty_name: Kbuhist2
size_categories:
- 1M<n<10M
---
# Dataset Card for mini_cleaned_diachronic_swe
The Swedish Diachronic Corpus is a project funded by [Swe-Clarin](https://sweclarin.se/eng) and provides a corpus of texts covering the time period from Old Swedish.
The dataset has been preprocessed and can be recreated from here: [Src_code](https://github.com/Borg93/kbuhist2/tree/main).

## Dataset Summary
The dataset has been filtered with the metadata:
- Manueally transcribed or post-ocr correction
- No scrambled sentences
- Year of origin: 15-19th centuary

### Data Splits
**This will be further extended!**

| Dataset Split | Number of Instances in Split                |
| ------------- | ------------------------------------------- |
| Train         | 352137                                      |
| Test          | 7187                                        |

## Acknowledgements
We gratefully acknowledge [SWE-clarin](https://sweclarin.se/) for the datasets.

## Citation Information

Eva Pettersson and Lars Borin (2022)
Swedish Diachronic Corpus
In Darja Fišer & Andreas Witt (eds.), CLARIN. The Infrastructure for Language Resources. Berlin: deGruyter. https://degruyter.com/document/doi/10.1515/9783110767377-022/html