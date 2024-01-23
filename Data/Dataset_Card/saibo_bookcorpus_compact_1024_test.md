---
dataset_info:
  features:
  - name: text
    dtype: string
  - name: concept_with_offset
    dtype: string
  splits:
  - name: train
    num_bytes: 75334225
    num_examples: 6160
  download_size: 38920916
  dataset_size: 75334225
---
# Dataset Card for "bookcorpus_compact_1024_test"


6160 samples randomly sampled from the shard9 of Bookcorpus_compact_1024
```python
from datasets import load_dataset
from datasets import Dataset
corpus_name="xxx"

ds = load_dataset(corpus_name, split="train") 
shuffled_ds = ds.shuffle(seed=42)
test_ds = Dataset.from_dict{shuffled_ds[:6160]} # len(ds)//10
```


[More Information needed](https://github.com/huggingface/datasets/blob/main/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)