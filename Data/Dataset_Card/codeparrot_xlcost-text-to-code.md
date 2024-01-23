---
annotations_creators: []
language_creators:
- crowdsourced
- expert-generated
language:
- code
license:
- cc-by-sa-4.0
multilinguality:
- multilingual
size_categories:
- unknown
source_datasets: []
task_categories:
- text-generation
task_ids:
- language-modeling
pretty_name: xlcost-text-to-code
---

# XLCost for text-to-code synthesis

## Dataset Description
This is a subset of [XLCoST benchmark](https://github.com/reddy-lab-code-research/XLCoST), for text-to-code generation at snippet level and program level for **7** programming languages: `Python, C, C#, C++, Java, Javascript and PHP`. 

## Languages

The dataset contains text in English and its corresponding code translation. Each program is divided into several code snippets, so the snipppet-level subsets contain these code snippets with their corresponding comments, for program-level subsets, the comments were concatenated in one long description. Moreover, programs in all the languages are aligned at the snippet level and the comment for a particular snippet is the same across all the languages. 

## Dataset Structure
To load the dataset you need to specify a subset among the **14 exiting instances**: `LANGUAGE-snippet-level/LANGUAGE-program-level` for `LANGUAGE` in `[Python, C, Csharp, C++, Java, Javascript and PHP]`. By default `Python-snippet-level` is loaded. 

```python
from datasets import load_dataset
load_dataset("codeparrot/xlcost-text-to-code", "Python-program-level")

DatasetDict({
    train: Dataset({
        features: ['text', 'code'],
        num_rows: 9263
    })
    test: Dataset({
        features: ['text', 'code'],
        num_rows: 887
    })
    validation: Dataset({
        features: ['text', 'code'],
        num_rows: 472
    })
})
```

```python
next(iter(data["train"]))
{'text': 'Maximum Prefix Sum possible by merging two given arrays | Python3 implementation of the above approach ; Stores the maximum prefix sum of the array A [ ] ; Traverse the array A [ ] ; Stores the maximum prefix sum of the array B [ ] ; Traverse the array B [ ] ; Driver code',
 'code': 'def maxPresum ( a , b ) : NEW_LINE INDENT X = max ( a [ 0 ] , 0 ) NEW_LINE for i in range ( 1 , len ( a ) ) : NEW_LINE INDENT a [ i ] += a [ i - 1 ] NEW_LINE X = max ( X , a [ i ] ) NEW_LINE DEDENT Y = max ( b [ 0 ] , 0 ) NEW_LINE for i in range ( 1 , len ( b ) ) : NEW_LINE INDENT b [ i ] += b [ i - 1 ] NEW_LINE Y = max ( Y , b [ i ] ) NEW_LINE DEDENT return X + Y NEW_LINE DEDENT A = [ 2 , - 1 , 4 , - 5 ] NEW_LINE B = [ 4 , - 3 , 12 , 4 , - 3 ] NEW_LINE print ( maxPresum ( A , B ) ) NEW_LINE'}
```
Note that the data undergo some tokenization hence the additional whitespaces and the use of NEW_LINE instead of `\n` and INDENT instead of `\t`, DEDENT to cancel indentation...

## Data Fields

* text: natural language description/comment
* code: code at snippet/program level

## Data Splits

Each subset has three splits: train, test and validation.

## Citation Information

```
@misc{zhu2022xlcost,
     title = {XLCoST: A Benchmark Dataset for Cross-lingual Code Intelligence},
     url = {https://arxiv.org/abs/2206.08474},
     author = {Zhu, Ming and Jain, Aneesh and Suresh, Karthik and Ravindran, Roshan and Tipirneni, Sindhu and Reddy, Chandan K.},
     year = {2022},
     eprint={2206.08474},
     archivePrefix={arXiv}
}
```