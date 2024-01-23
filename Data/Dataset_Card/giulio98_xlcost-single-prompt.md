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
pretty_name: xlcost-single-prompt
---
# XLCost for text-to-code synthesis
## Dataset Description
This is a subset of [XLCoST benchmark](https://github.com/reddy-lab-code-research/XLCoST), for text-to-code generation at program level for **2** programming languages: `Python, C++`. This dataset is based on [codeparrot/xlcost-text-to-code](https://huggingface.co/datasets/codeparrot/xlcost-text-to-code) with the following improvements:
* NEWLINE, INDENT and DEDENT were replaced with the corresponding ASCII codes.
* the code text has been reformatted using autopep8 for Python and clang-format for cpp.
* new columns have been introduced to allow evaluation using pass@k metric.
* programs containing more than one function call in the driver code were removed
## Languages
The dataset contains text in English and its corresponding code translation. The text contains a set of concatenated code comments that allow to synthesize the program.
## Dataset Structure
To load the dataset you need to specify the language(Python or C++). 
```python
from datasets import load_dataset
load_dataset("giulio98/xlcost-single-prompt", "Python")
DatasetDict({
    train: Dataset({
        features: ['text', 'context', 'code', 'test', 'output', 'fn_call'],
        num_rows: 8306
    })
    test: Dataset({
        features: ['text', 'context', 'code', 'test', 'output', 'fn_call'],
        num_rows: 812
    })
    validation: Dataset({
        features: ['text', 'context', 'code', 'test', 'output', 'fn_call'],
        num_rows: 427
    })
})
```
## Data Fields
* text: natural language description.
* context: import libraries/global variables.
* code: code at program level.
* test: test function call.
* output: expected output of the function call.
* fn_call: name of the function to call.
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