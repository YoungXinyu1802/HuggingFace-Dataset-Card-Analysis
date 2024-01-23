# Wiki Sentences

A dataset of all english sentences in Wikipedia.

Taken from the OPTIMUS project. https://github.com/ChunyuanLI/Optimus/blob/master/download_datasets.md

The dataset is 11.8GB so best to load it using streaming:

```python
from datasets import load_dataset
dataset = load_dataset("Fraser/wiki_sentences", split='train', streaming=True)
```
