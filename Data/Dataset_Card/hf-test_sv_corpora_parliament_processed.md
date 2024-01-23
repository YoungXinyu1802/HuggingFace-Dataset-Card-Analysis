Swedish text corpus created by extracting the `"text"` from `dataset = load_dataset("europarl_bilingual", lang1="en", lang2="sv", split="train")` and processing it with:

```python
import re

def extract_text(batch):
  text = batch["translation"]["sv"]
  batch["text"] = re.sub(chars_to_ignore_regex, "", text.lower())
  return batch
```