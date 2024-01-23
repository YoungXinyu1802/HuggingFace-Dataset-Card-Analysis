---
license: cc-by-4.0
language:
- sr
pretty_name: Serbian WikiMedia dataset
---

Dataset contain text from Wikipedia articles in Serbian (obtained in early 2020) totaling in 477473 articles, as well as some of the WikiSource.

Dataset is constituted of JSON files, where the textual sentences are located in the "sents" attribute of the object root and can be obtianed via:

```python
from json import load

with open("WikiKorpus.json") as jf:
  sentences = load(jf)["sents"]
```