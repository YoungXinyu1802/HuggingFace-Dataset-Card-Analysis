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
pretty_name: 'Pokémon BLIP captions'
size_categories:
- n<1K
source_datasets:
- huggan/few-shot-pokemon
tags: []
task_categories:
- text-to-image
task_ids: []
---

# Dataset Card for Pokémon BLIP captions

_Dataset used to train [Pokémon text to image model](https://github.com/LambdaLabsML/examples/tree/main/stable-diffusion-finetuning)_

BLIP generated captions for Pokémon images from Few Shot Pokémon dataset introduced by _Towards Faster and Stabilized GAN Training for High-fidelity Few-shot Image Synthesis_ (FastGAN). Original images were obtained from [FastGAN-pytorch](https://github.com/odegeasslbc/FastGAN-pytorch) and captioned with the [pre-trained BLIP model](https://github.com/salesforce/BLIP).

For each row the dataset contains `image` and `text` keys. `image` is a varying size PIL jpeg, and `text` is the accompanying text caption. Only a train split is provided.


## Examples


![pk1.jpg](https://s3.amazonaws.com/moonup/production/uploads/1663756580442-62bd5f951e22ec84279820e8.jpeg)
> a drawing of a green pokemon with red eyes

![pk10.jpg](https://s3.amazonaws.com/moonup/production/uploads/1663756580225-62bd5f951e22ec84279820e8.jpeg)
> a green and yellow toy with a red nose

![pk100.jpg](https://s3.amazonaws.com/moonup/production/uploads/1663756579985-62bd5f951e22ec84279820e8.jpeg)
> a red and white ball with an angry look on its face

## Citation

If you use this dataset, please cite it as:

```
@misc{pinkney2022pokemon,
      author = {Pinkney, Justin N. M.},
      title = {Pokemon BLIP captions},
      year={2022},
      howpublished= {\url{https://huggingface.co/datasets/lambdalabs/pokemon-blip-captions/}}
} 
```