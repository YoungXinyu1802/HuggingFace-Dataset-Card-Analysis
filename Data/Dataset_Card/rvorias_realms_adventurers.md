---
license: other
task_categories:
- text-to-image
language:
- en
tags:
- stable-diffusion
- realms
pretty_name: Realms Adventurers Dataset
size_categories:
- n<1K
---

# Realms Adventurer Dataset for Text-to-Image

This dataset contains annotated image-caption pairs with a specific structure.

## Example

```json
{
    "file_name": "91200682-07_giants.png",
    "sex": "male",
    "race": "giant",
    "class": "mage",
    "inherent_features": "red flowers growing on his skin",
    "clothing": "brown leather pants",
    "accessories": null,
    "background": "between tall red trees",
    "shot": "full",
    "view": "frontal",
    "caption": "a male giant mage with red flowers growing on his skin, wearing brown leather pants, between tall red trees, full, frontal"
}
```

## Usage

```python
import datasets

dataset = datasets.load_dataset("rvorias/realms_adventurers")

dataset["train"][0]
```

## Annotation tooling

Label-studio was used to organize and create annotations.