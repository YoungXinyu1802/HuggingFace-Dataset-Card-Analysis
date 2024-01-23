---
license: afl-3.0
---

This dataset is created by Ilja Samoilov. In dataset is tv show subtitles from ERR and transcriptions of those shows created with TalTech ASR.

```
from datasets import load_dataset, load_metric
dataset = load_dataset('csv', data_files={'train': "train.tsv", \
                                          "validation":"val.tsv", \
                                          "test": "test.tsv"}, delimiter='\t')
```