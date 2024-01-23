# Pretokenized GitHub Code Dataset

## Dataset Description
This is a pretokenized version of the Python files of the [GitHub Code dataset](https://huggingface.co/datasets/lvwerra/github-code), that consists of 115M code files from GitHub in 32 programming languages. We tokenized the dataset using BPE Tokenizer trained on code, available in this [repo](https://huggingface.co/lvwerra/codeparrot). Having a pretokenized dataset can speed up the training loop by not having to tokenize data at each batch call. We also include `ratio_char_token` which gives the ratio between the number of characters in a file and the number of tokens we get after tokenization, this ratio can be a good filter to detect outlier files.
 
### How to use it
To avoid downloading the whole dataset, you can make use of the streaming API of `datasets`. You can load and iterate through the dataset with the following two lines of code:
```python
from datasets import load_dataset

ds = load_dataset("loubnabnl/tokenized-github-code-python", streaming=True, split="train")
print(next(iter(ds)))
#OUTPUT:
{'input_ids': [504, 1639, 492,...,199, 504, 1639],
 'ratio_char_token': 3.560888252148997
}
```