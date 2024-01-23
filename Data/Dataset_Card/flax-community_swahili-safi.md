# Swahili-Safi Dataset

A relatively clean dataset for Swahili language modeling, built by combining and cleaning several existing datasets.

Sources include:
```
mc4-sw
oscar-sw
swahili_news
IWSLT
XNLI
flores 101
swahili-lm
gamayun-swahili-minikit
broadcastnews-sw
subset of wikipedia-en translated (using m2m100) to sw
```

In total this dataset is ~3.5 GB in size with over 21 million lines of text.

## Usage

This dataset can be downloaded and used as follows:

```python
from datasets import load_dataset
ds = load_dataset("flax-community/swahili-safi")
```
