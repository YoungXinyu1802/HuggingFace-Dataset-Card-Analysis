---
language:
- sr
pretty_name: cc100-sr derivation by JeRTeh
---

As the title suggests, this dataset is a derivative of the cc100-sr common-crawl based dataset for Serbian. 
It was deduplicated on the sentence level, and transliterated into latin alphabet.

Dataset is constituted of JSON files, where the textual sentences are located in the "sents" attribute of the object root and can be obtianed via:

```python
from json import load

with open("cc100-sr-ded") as jf:
  sentences = load(jf)["sents"]
```