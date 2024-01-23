---
license: cc0-1.0
annotations_creators:
- machine-generated
language:
- en
language_creators:
- other
multilinguality:
- monolingual
pretty_name: 'Nouns auto-captioned'
size_categories:
- 10K<n<100K
tags: []
task_categories:
- text-to-image
task_ids: []
---

# Dataset Card for Nouns auto-captioned

_Dataset used to train Nouns text to image model_

Automatically generated captions for Nouns from their attributes, colors and items. Help on the captioning script appreciated!

For each row the dataset contains `image` and `text` keys. `image` is a varying size PIL jpeg, and `text` is the accompanying text caption. Only a train split is provided.


## Citation

If you use this dataset, please cite it as:

```
@misc{piedrafita2022nouns,
      author = {Piedrafita, Miguel},
      title = {Nouns auto-captioned},
      year={2022},
      howpublished= {\url{https://huggingface.co/datasets/m1guelpf/nouns/}}
}
```
