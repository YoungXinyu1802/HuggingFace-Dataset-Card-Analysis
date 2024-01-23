# BinhVQ dedup

**Important**: Please install `lm_dataformat` by `pip install lm_dataformat` before using this dataset

## How to use
```python
import datasets

dataset = datasets.load_dataset("imthanhlv/binhvq_dedup")
```

## Dataset information

This dataset was created from `https://github.com/binhvq/news-corpus` dump with date 21/05/2021. I applied some simple preprocessing:
- Using BeautifulSoup to clean content
- Each record is concatenate of (title + "\n" + sapo + "\n" + content)
- Then perform shuffling + split train & validation + deduplicate (exact match using sha256)