---
task_categories:
- image-classification
tags:
- roboflow
- roboflow2huggingface
- Gaming
---

<div align="center">
  <img width="640" alt="fcakyon/pokemon-classification" src="https://huggingface.co/datasets/fcakyon/pokemon-classification/resolve/main/thumbnail.jpg">
</div>

### Dataset Labels

```
['Golbat', 'Machoke', 'Omastar', 'Diglett', 'Lapras', 'Kabuto', 'Persian', 'Weepinbell', 'Golem', 'Dodrio', 'Raichu', 'Zapdos', 'Raticate', 'Magnemite', 'Ivysaur', 'Growlithe', 'Tangela', 'Drowzee', 'Rapidash', 'Venonat', 'Pidgeot', 'Nidorino', 'Porygon', 'Lickitung', 'Rattata', 'Machop', 'Charmeleon', 'Slowbro', 'Parasect', 'Eevee', 'Starmie', 'Staryu', 'Psyduck', 'Dragonair', 'Magikarp', 'Vileplume', 'Marowak', 'Pidgeotto', 'Shellder', 'Mewtwo', 'Farfetchd', 'Kingler', 'Seel', 'Kakuna', 'Doduo', 'Electabuzz', 'Charmander', 'Rhyhorn', 'Tauros', 'Dugtrio', 'Poliwrath', 'Gengar', 'Exeggutor', 'Dewgong', 'Jigglypuff', 'Geodude', 'Kadabra', 'Nidorina', 'Sandshrew', 'Grimer', 'MrMime', 'Pidgey', 'Koffing', 'Ekans', 'Alolan Sandslash', 'Venusaur', 'Snorlax', 'Paras', 'Jynx', 'Chansey', 'Hitmonchan', 'Gastly', 'Kangaskhan', 'Oddish', 'Wigglytuff', 'Graveler', 'Arcanine', 'Clefairy', 'Articuno', 'Poliwag', 'Abra', 'Squirtle', 'Voltorb', 'Ponyta', 'Moltres', 'Nidoqueen', 'Magmar', 'Onix', 'Vulpix', 'Butterfree', 'Krabby', 'Arbok', 'Clefable', 'Goldeen', 'Magneton', 'Dratini', 'Caterpie', 'Jolteon', 'Nidoking', 'Alakazam', 'Dragonite', 'Fearow', 'Slowpoke', 'Weezing', 'Beedrill', 'Weedle', 'Cloyster', 'Vaporeon', 'Gyarados', 'Golduck', 'Machamp', 'Hitmonlee', 'Primeape', 'Cubone', 'Sandslash', 'Scyther', 'Haunter', 'Metapod', 'Tentacruel', 'Aerodactyl', 'Kabutops', 'Ninetales', 'Zubat', 'Rhydon', 'Mew', 'Pinsir', 'Ditto', 'Victreebel', 'Omanyte', 'Horsea', 'Pikachu', 'Blastoise', 'Venomoth', 'Charizard', 'Seadra', 'Muk', 'Spearow', 'Bulbasaur', 'Bellsprout', 'Electrode', 'Gloom', 'Poliwhirl', 'Flareon', 'Seaking', 'Hypno', 'Wartortle', 'Mankey', 'Tentacool', 'Exeggcute', 'Meowth']
```


### Number of Images

```json
{'train': 4869, 'test': 732, 'valid': 1390}
```


### How to Use

- Install [datasets](https://pypi.org/project/datasets/):

```bash
pip install datasets
```

- Load the dataset:

```python
from datasets import load_dataset

ds = load_dataset("fcakyon/pokemon-classification", name="full")
example = ds['train'][0]
```

### Roboflow Dataset Page
[https://universe.roboflow.com/robert-demo-qvail/pokedex/dataset/14](https://universe.roboflow.com/robert-demo-qvail/pokedex/dataset/14?ref=roboflow2huggingface)

### Citation

```
@misc{ pokedex_dataset,
    title = { Pokedex Dataset },
    type = { Open Source Dataset },
    author = { Lance Zhang },
    howpublished = { \\url{ https://universe.roboflow.com/robert-demo-qvail/pokedex } },
    url = { https://universe.roboflow.com/robert-demo-qvail/pokedex },
    journal = { Roboflow Universe },
    publisher = { Roboflow },
    year = { 2022 },
    month = { dec },
    note = { visited on 2023-01-14 },
}
```

### License
Public Domain

### Dataset Summary
This dataset was exported via roboflow.com on December 20, 2022 at 5:34 PM GMT

Roboflow is an end-to-end computer vision platform that helps you
* collaborate with your team on computer vision projects
* collect & organize images
* understand unstructured image data
* annotate, and create datasets
* export, train, and deploy computer vision models
* use active learning to improve your dataset over time

It includes 6991 images.
Pokemon are annotated in folder format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 224x224 (Fit (black edges))

No image augmentation techniques were applied.



