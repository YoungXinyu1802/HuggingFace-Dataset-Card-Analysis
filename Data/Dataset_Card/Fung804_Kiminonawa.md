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

![1504107193.png](https://s3.amazonaws.com/moonup/production/uploads/1669389067220-637dbe8c6281ea1fcc4e2670.png)
> a green and yellow toy with a red nose
![1504107197.png](https://s3.amazonaws.com/moonup/production/uploads/1669389067217-637dbe8c6281ea1fcc4e2670.png)
> a green and yellow toy with a red nose
![1504107198.png](https://s3.amazonaws.com/moonup/production/uploads/1669389067649-637dbe8c6281ea1fcc4e2670.png)
> a green and yellow toy with a red nose
![1504107202.jpg](https://s3.amazonaws.com/moonup/production/uploads/1669389066994-637dbe8c6281ea1fcc4e2670.jpeg)
> a green and yellow toy with a red nose
![1504107203.png](https://s3.amazonaws.com/moonup/production/uploads/1669389067651-637dbe8c6281ea1fcc4e2670.png)
> a green and yellow toy with a yellow nose

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