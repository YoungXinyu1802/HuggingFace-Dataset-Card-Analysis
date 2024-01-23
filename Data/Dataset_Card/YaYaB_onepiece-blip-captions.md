---
license: cc-by-nc-sa-4.0
annotations_creators:
- machine-generated
language:
- en
language_creators:
- other
multilinguality:
- monolingual
pretty_name: 'One Piece BLIP captions'
size_categories:
- n<1K
source_datasets:
- YaYaB/onepiece-blip-captions
tags: []
task_categories:
- text-to-image
task_ids: []
---

# Disclaimer
This was inspired from https://huggingface.co/datasets/lambdalabs/pokemon-blip-captions

# Dataset Card for One Piece BLIP captions

_Dataset used to train [One Piece text to image model](https://github.com/LambdaLabsML/examples/tree/main/stable-diffusion-finetuning)_

BLIP generated captions for One piece images collected from the web. Original images were obtained from [Anime Characters](https://www.animecharactersdatabase.com) and captioned with the [pre-trained BLIP model](https://github.com/salesforce/BLIP).

For each row the dataset contains `image` and `text` keys. `image` is a varying size PIL jpeg, and `text` is the accompanying text caption. Only a train split is provided.


## Examples


![pk1.jpg](https://ami.animecharactersdatabase.com/uploads/chars/11076-782139445.jpg)
> a man in a straw hat

![pk10.jpg](https://www.animecharactersdatabase.com/uploads/chars/5457-1977266515.png)
> a man in a green coat holding two swords

![pk100.jpg](https://ami.animecharactersdatabase.com/uploads/chars/12602-925960129.jpg)
> a man with red hair and a black coat

## Citation

If you use this dataset, please cite it as:

```
@misc{yayab2022onepiece,
      author = {YaYaB},
      title = {One Piece BLIP captions},
      year={2022},
      howpublished= {\url{https://huggingface.co/datasets/YaYaB/onepiece-blip-captions/}}
} 
```