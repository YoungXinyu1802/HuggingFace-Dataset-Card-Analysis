---
license: creativeml-openrail-m
task_categories:
- text-generation
language:
- en
size_categories:
- 100K<n<1M
---

For more info on data collection and the preprocessing algorithm, please see [Fast Anime PromptGen](https://huggingface.co/FredZhang7/anime-anything-promptgen-v2).


## 80K unique prompts
- `safebooru_clean`: Cleaned prompts with upscore ≥ 8 from the Safebooru API

---

For disclaimers about the Danbooru data, please see [Danbooru Tag Generator](https://huggingface.co/FredZhang7/danbooru-tag-generator).

## 100K unique prompts (each)
- `danbooru_raw`: Raw prompts with upscore ≥ 3 from Danbooru API
- `danbooru_clean`: Cleaned prompts with upscore ≥ 3 from Danbooru API

---

## Python

Download and save the dataset to anime_prompts.csv locally.

```bash
pip install datasets
```
```python
import csv
import datasets

dataset = datasets.load_dataset("FredZhang7/anime-prompts-180K")

train = dataset["train"]
safebooru_clean = train["safebooru_clean"]
danbooru_clean = train["danbooru_clean"]
danbooru_raw = train["danbooru_raw"]

with open("anime_prompts.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["safebooru_clean", "danbooru_clean", "danbooru_raw"])
    for i in range(len(safebooru_clean)):
        writer.writerow([safebooru_clean[i], danbooru_clean[i], danbooru_raw[i]])
```