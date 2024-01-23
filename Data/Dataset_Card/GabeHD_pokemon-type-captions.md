---
dataset_info:
  features:
  - name: image
    dtype: image
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 19372532.0
    num_examples: 898
  download_size: 0
  dataset_size: 19372532.0
---
# Dataset Card for Pokémon type captions

Contains official artwork and type-specific caption for Pokémon #1-898 (Bulbasaur-Calyrex). 
Each Pokémon is represented once by the default form from [PokéAPI](https://pokeapi.co/)

Each row contains `image` and `text` keys:
- `image` is a 475x475 PIL jpg of the Pokémon's official artwork. 
- `text` is a label describing the Pokémon by its type(s)

## Attributions

_Images and typing information pulled from [PokéAPI](https://pokeapi.co/)_

_Based on the [Lambda Labs Pokémon Blip Captions Dataset](https://huggingface.co/datasets/lambdalabs/pokemon-blip-captions)_
