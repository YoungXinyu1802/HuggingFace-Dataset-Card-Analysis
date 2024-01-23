---


---
# download zenodo datasets using huggingface datasets

```python
from datasets import load_dataset
dataset = load_dataset("zenodo", "10.5281/zenodo.4285300")
```

or download the dataset to a desired directory

```python
from datasets import load_dataset
dataset = load_dataset("zenodo", "10.5281/zenodo.4285300", data_dir="path/to/dataset")
```



