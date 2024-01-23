---
license: cc-by-4.0
language:
- sr
pretty_name: Serbian Literary Text Collection
size_categories:
- 1M<n<10M
---

SrpELTeC is a corpus of old Serbian novels for the first time published in the period 1840-1920. years of digitized within COST ACTION CO16204: Distant Reading for European Literary History, 2018-2022.

The corpus includes 120 novels with 5,263.071 words, 22700 pages, 2557 chapters, 158,317 passages, 567 songs, 2972 verses, 803 segments in foreign language and 949 mentioned works.

Dataset is constituted of JSON files, where the textual sentences are located in the "sents" attribute of the object root and can be obtianed via:

```python
from json import load

with open("ELTeC.json") as jf:
  sentences = load(jf)["sents"]
```
