---
license: cc-by-nc-sa-4.0
annotations_creators:
- machine-generated
language:
- en
- zh
language_creators:
- other
multilinguality:
- multilingual
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

# Dataset Card for Pokémon BLIP captions with English and Chinese.

Dataset used to train Pokémon text to image model, add a Chinese Column of [Pokémon BLIP captions](https://huggingface.co/datasets/lambdalabs/pokemon-blip-captions)

BLIP generated captions for Pokémon images from Few Shot Pokémon dataset introduced by Towards Faster and Stabilized GAN Training for High-fidelity Few-shot Image Synthesis (FastGAN). Original images were obtained from FastGAN-pytorch and captioned with the pre-trained BLIP model.

For each row the dataset contains image en_text (caption in English) and zh_text (caption in Chinese) keys. image is a varying size PIL jpeg, and text is the accompanying text caption. Only a train split is provided.

The Chinese captions are translated by [Deepl](https://www.deepl.com/translator)