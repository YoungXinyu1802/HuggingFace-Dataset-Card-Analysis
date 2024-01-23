---
layout: default
title: "Name Entity Recognition of DiffusionDB"
nav_order: 1
has_children: false

language_creators:
    - found
language:
    - en
license:
    - cc-by-3.0
multilinguality:
    - monolingual
pretty_name: NER-DiffusionDB
size_categories:
    - 100M<n<1G
source_datasets:
    - poloclub/diffusiondb
tags:
    - stable diffusion
    - prompt engineering
    - prompts
    - research paper
---

![](https://www.selas.ai/assets/logo-selas.86b7b0b6.svg)

### Description

Extended dataset infered by the name entity recognition model [en_ner_prompting](https://huggingface.co/teo-sanchez/en_ner_prompting). This model has been trained on hand-annotated prompts from [poloclub/diffusiondb](https://huggingface.co/datasets/poloclub/diffusiondb).
This dataset is hence infered by this model and can comprise mistakes, especially on certain categories (cf. model card).

  The entities comprise 7 main categories and 11 subcategories for a total of 16 categories, extracted from a topic analysis made with [BERTopic](https://maartengr.github.io/BERTopic/index.html).
  The topic analysis can be explored [the following visualization](https://teo-sanchez.github.io/projects/prompting_map.html).

```
  ├── medium/
  │   ├── photography
  │   ├── painting
  │   ├── rendering
  │   └── illustration
  ├── influence/
  │   ├── artist
  │   ├── genre
  │   ├── artwork
  │   └── repository
  ├── light
  ├── color
  ├── composition
  ├── detail
  └── context/
      ├── era
      ├── weather
      └── emotion
```

### Label Scheme

<details>

<summary>View label scheme (16 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`ner`** | `color`, `composition`, `context/emotion`, `context/era`, `context/weather`, `detail`, `influence/artist`, `influence/artwork`, `influence/genre`, `influence/repository`, `light`, `medium/illustration`, `medium/painting`, `medium/photography`, `medium/rendering`, `subject` |

</details>