---
annotations_creators:
- no-annotation
language_creators:
- crowdsourced
language:
- ko
license:
- cc-by-sa-4.0
multilinguality:
- monolingual
pretty_name: KcBERT Pre-Training Corpus (Korean News Comments)
size_categories:
- 10M<n<100M
source_datasets:
- original
task_categories:
- fill-mask
- text-generation
task_ids:
- masked-language-modeling
- language-modeling
---

# KcBERT Pre-Training Corpus (Korean News Comments)

## Dataset Description

- **Homepage:** [KcBERT Pre-Training Corpus](https://www.kaggle.com/datasets/junbumlee/kcbert-pretraining-corpus-korean-news-comments)

- **Repository:** [Beomi/KcBERT](https://github.com/Beomi/KcBERT)

- **Paper:** [Needs More Information]

- **Leaderboard:** [Needs More Information]

- **Point of Contact:** [Needs More Information]


## KcBERT
[beomi/kcbert-base](https://huggingface.co/beomi/kcbert-base)

Github KcBERT Repo: [https://github.com/Beomi/KcBERT](https://github.com/Beomi/KcBERT)  
KcBERT is Korean Comments BERT pretrained on this Corpus set.  
(You can use it via Huggingface's Transformers library!)

This Kaggle Dataset contains **CLEANED** dataset preprocessed with the code below.

```python
import re
import emoji
from soynlp.normalizer import repeat_normalize

emojis = ''.join(emoji.UNICODE_EMOJI.keys())
pattern = re.compile(f'[^ .,?!/@$%~％·∼()\x00-\x7Fㄱ-힣{emojis}]+')
url_pattern = re.compile(
    r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)')

def clean(x):
    x = pattern.sub(' ', x)
    x = url_pattern.sub('', x)
    x = x.strip()
    x = repeat_normalize(x, num_repeats=2)
    return x
```

### License
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

## Dataset Structure
### Data Instance
```pycon
>>> from datasets import load_dataset

>>> dataset = load_dataset("Bingsu/KcBERT_Pre-Training_Corpus")
>>> dataset
DatasetDict({
	train: Dataset({
		features: ['text'],
		num_rows: 86246285
	})
})
```

### Data Size

download: 7.90 GiB<br>
generated: 11.86 GiB<br>
total: 19.76 GiB

※ You can download this dataset from [kaggle](https://www.kaggle.com/datasets/junbumlee/kcbert-pretraining-corpus-korean-news-comments), and it's 5 GiB. (12.48 GiB when uncompressed)

### Data Fields

- text: `string`

### Data Splits

|            |   train  |
| ---------- | -------- |
| # of texts | 86246285 |
