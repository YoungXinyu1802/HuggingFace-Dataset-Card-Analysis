---
license: apache-2.0
language:
- en
multilinguality:
- monolingual
pretty_name: multi text2image prompts a dataset collection
source_datasets:
- bartman081523/stable-diffusion-discord-prompts
- succinctly/midjourney-prompts
- Gustavosta/Stable-Diffusion-Prompts
tags:
- text generation
---


# text2image multi-prompt(s): a dataset collection

- collection of several text2image prompt datasets
- data was cleaned/normalized with the goal of removing "model specific APIs" like the "--ar" for Midjourney and so on
- data de-duplicated on a basic level: exactly duplicate prompts were dropped (_after cleaning and normalization_)


## contents

```
DatasetDict({
    train: Dataset({
        features: ['text', 'src_dataset'],
        num_rows: 3551734
    })
    test: Dataset({
        features: ['text', 'src_dataset'],
        num_rows: 399393
    })
})
```

_NOTE: as the other two datasets did not have a `validation` split, the validation split of `succinctly/midjourney-prompts` was merged into `train`._