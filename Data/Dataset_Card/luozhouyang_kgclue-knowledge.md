# KgCLUE-Knowledge

The original data is from [CLUEbenchmark/KgCLUE](https://github.com/CLUEbenchmark/KgCLUE).

Here is a JSON version of the original knowledge base.

## Usage

```bash
from datasets import load_dataset

dataset = load_dataset("luozhouyang/kgclue-knowledge")

# or select files
dataset = load_dataset("luozhouyang/kgclue-knowledge", data_files=["kgclue.knowledge00.jsonl"])

```
