---
annotations_creators:
- machine-generated
language:
- en
license:
- cc-by-nc-4.0
multilinguality:
- monolingual
pretty_name: '1,071 BLIP captioned images of Digimon. '
size_categories:
- 1K<n<10K
source_datasets:
- original
tags:
- digimon
task_categories: []
task_ids: []
---

# Dataset Card for Digimon BLIP captions

This project was inspired by the [labelled Pokemon dataset](https://huggingface.co/datasets/lambdalabs/pokemon-blip-captions).

The captions were generated using the BLIP Model found in the [LAVIS Library for Language-Vision Intelligence](https://github.com/salesforce/LAVIS). 

Like the Pokemon equivalent, each row in the dataset contains the `image` and `text` keys. `Image` is a varying size pixel jpeg, and `text` is the corresponding text caption.

## Citation

If you use this dataset, please cite it as:

```
@misc{clemen2022digimon,
      author = {Kok, Clemen},
      title = {Digimon BLIP captions},
      year={2022},
      howpublished= {\url{https://huggingface.co/datasets/ClemenKok/digimon-lavis-captions/}}
} 
```