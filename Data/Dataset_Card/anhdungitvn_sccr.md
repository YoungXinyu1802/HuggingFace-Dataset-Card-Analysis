---
license: apache-2.0
---


```python
from datasets import load_dataset
data_name = "anhdungitvn/sccr"
data_files = {"train": "train.tsv", "eval": "eval.tsv"}
sccr = load_dataset(data_name, data_files=data_files)
sccr
```


```python
DatasetDict({
    train: Dataset({
        features: ['text', 'labels'],
        num_rows: 14478
    })
    eval: Dataset({
        features: ['text', 'labels'],
        num_rows: 1609
    })
})
```



### References
  - <a href="https://www.aivivn.com/contests/6">SC: Sentiment Classification (Phân loại sắc thái bình luận)</a>
