---
license: mit
---

## Dataset Description
A dataset of pairs of TypeScript code to appropriate type declarations.

## Language
TypeScript only.

## To Load
```python
from datasets import load_dataset

load_dataset("noahshinn024/ts-code2td")
```

## Distribution of type declaration code lengths
- uses the tokenizer from [bigcode/santacoder](https://huggingface.co/bigcode/santacoder)
![](./media/declaration_token_distr.png)
