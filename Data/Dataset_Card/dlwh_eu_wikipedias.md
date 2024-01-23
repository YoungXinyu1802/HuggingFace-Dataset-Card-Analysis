---
annotations_creators:
- no-annotation
language_creators:
- crowdsourced
pretty_name: Wikipedia
paperswithcode_id: null
license:
- cc-by-sa-3.0
- gfdl
task_categories:
- text-generation
- fill-mask
task_ids:
- language-modeling
- masked-language-modeling
source_datasets:
- original
multilinguality:
- multilingual
size_categories:
- n<1K
- 1K<n<10K
- 10K<n<100K
- 100K<n<1M
- 1M<n<10M
language:
   - bg
   - cs
   - da
   - de
   - el
   - en
   - es
   - et
   - fi
   - fr
   - ga
   - hr
   - hu
   - it
   - lt
   - lv
   - mt
   - nl
   - pl
   - pt
   - ro
   - sk
   - sl
   - sv
---

# Dataset Card for Wikipedia

This repo is a wrapper around [olm/wikipedia](https://huggingface.co/datasets/olm/wikipedia) that just concatenates data from the EU languages.
Please refer to it for a complete data card.

The EU languages we include are:
   - bg
   - cs
   - da
   - de
   - el
   - en
   - es
   - et
   - fi
   - fr
   - ga
   - hr
   - hu
   - it
   - lt
   - lv
   - mt
   - nl
   - pl
   - pt
   - ro
   - sk
   - sl
   - sv


As with `olm/wikipedia` you will need to install a few dependencies:


```
pip install mwparserfromhell==0.6.4 multiprocess==0.70.13
```

```python
from datasets import load_dataset

load_dataset("dlwh/eu_wikipedias", date="20221101")
```

Please refer to the original olm/wikipedia for a complete data card.
