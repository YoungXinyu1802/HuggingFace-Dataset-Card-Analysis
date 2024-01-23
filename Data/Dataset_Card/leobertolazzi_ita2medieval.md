---
task_categories:
- text2text-generation
language:
- it
size_categories:
- 1K<n<10K
---

## ita2medieval
The **ita2medieval** dataset contains sentences from medieval italian along with paraphrases in contemporary italian (approximately 6.5k pairs in total). The medieval italian sentences are extracted from texts by Dante, Petrarca, Guinizelli and Cavalcanti.

It is intended to perform text-style-transfer from contemporary to medieval italian and vice-versa.

## Loading the dataset

```
from datasets import load_dataset

dataset = load_dataset("leobertolazzi/ita2medieval")
```

Note: due to the small size of the dataset there are no predefined train and test splits.

## Dataset creation

**ita2medieval** was created by scraping [letteritaliana.weebly.com](https://letteritaliana.weebly.com/).