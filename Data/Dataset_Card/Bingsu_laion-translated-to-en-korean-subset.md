---
annotations_creators:
- crowdsourced
language_creators:
- crowdsourced
language:
- ko
- en
license:
- cc-by-4.0
multilinguality:
- multilingual
pretty_name: laion-translated-to-en-korean-subset
size_categories:
- 10M<n<100M
task_categories:
- feature-extraction
---

# laion-translated-to-en-korean-subset

## Dataset Description
- **Homepage:** [laion-5b](https://laion.ai/blog/laion-5b/)
- **Download Size** 1.40 GiB
- **Generated Size** 3.49 GiB
- **Total Size** 4.89 GiB

## About dataset
a subset data of [laion/laion2B-multi-joined-translated-to-en](https://huggingface.co/datasets/laion/laion2B-multi-joined-translated-to-en) and [laion/laion1B-nolang-joined-translated-to-en](https://huggingface.co/datasets/laion/laion1B-nolang-joined-translated-to-en), including only korean

### Lisence
CC-BY-4.0

## Data Structure

### Data Instance

```py
>>> from datasets import load_dataset
>>> dataset = load_dataset("Bingsu/laion-translated-to-en-korean-subset")
>>> dataset
DatasetDict({
    train: Dataset({
        features: ['hash', 'URL', 'TEXT', 'ENG TEXT', 'WIDTH', 'HEIGHT', 'LANGUAGE', 'similarity', 'pwatermark', 'punsafe', 'AESTHETIC_SCORE'],
        num_rows: 12769693
    })
})
```

```py
>>> dataset["train"].features
{'hash': Value(dtype='int64', id=None),
 'URL': Value(dtype='large_string', id=None),
 'TEXT': Value(dtype='large_string', id=None),
 'ENG TEXT': Value(dtype='large_string', id=None),
 'WIDTH': Value(dtype='int32', id=None),
 'HEIGHT': Value(dtype='int32', id=None),
 'LANGUAGE': Value(dtype='large_string', id=None),
 'similarity': Value(dtype='float32', id=None),
 'pwatermark': Value(dtype='float32', id=None),
 'punsafe': Value(dtype='float32', id=None),
 'AESTHETIC_SCORE': Value(dtype='float32', id=None)}
```

### Data Size

download: 1.40 GiB<br>
generated: 3.49 GiB<br>
total: 4.89 GiB

### Data Field

- 'hash': `int`
- 'URL': `string`
- 'TEXT': `string`
- 'ENG TEXT': `string`, null data are dropped
- 'WIDTH': `int`, null data are filled with 0
- 'HEIGHT': `int`, null data are filled with 0
- 'LICENSE': `string`
- 'LANGUAGE': `string`
- 'similarity': `float32`, CLIP similarity score, null data are filled with 0.0
- 'pwatermark': `float32`, Probability of containing a watermark, null data are filled with 0.0
- 'punsafe': `float32`, Probability of nsfw image, null data are filled with 0.0
- 'AESTHETIC_SCORE': `float32`, null data are filled with 0.0

### Data Splits

|           |    train |
| --------- | -------- |
| # of data | 12769693 |


### polars

```sh
pip install polars[fsspec]
```

```py
import polars as pl
from huggingface_hub import hf_hub_url

url = hf_hub_url("Bingsu/laion-translated-to-en-korean-subset", filename="train.parquet", repo_type="dataset")
# url = "https://huggingface.co/datasets/Bingsu/laion-translated-to-en-korean-subset/resolve/main/train.parquet"
df = pl.read_parquet(url)
```

pandas broke my colab session.