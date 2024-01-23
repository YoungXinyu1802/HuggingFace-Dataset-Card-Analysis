---
annotations_creators:
- machine-generated
language:
- en
language_creators:
- found
license:
- cc-by-nc-4.0
multilinguality:
- monolingual
pretty_name: Pokemoncards
size_categories:
- 10K<n<100K
source_datasets:
- original
tags: []
task_categories:
- text-to-image
- image-to-text
task_ids:
- image-captioning
---

# Dataset Card for PokemonCards


### Languages

All of the data is in English.

## Dataset Structure

### Data Instances

```json
{
  "id": "pl1-1",
  "image_url": "https://images.pokemontcg.io/pl1/1_hires.png",
  "caption": "A Stage 2 Pokemon Card of type Lightning with the title ""Ampharos"" and 130 HP of rarity ""Rare Holo"" evolved from Flaaffy from the set Platinum and the flavor text: ""None"". It has the attack ""Gigavolt"" with the cost Lightning, Colorless, the energy cost 2 and the damage of 30+ with the description: ""Flip a coin. If heads, this attack does 30 damage plus 30 more damage. If tails, the Defending Pokemon is now Paralyzed."". It has the attack ""Reflect Energy"" with the cost Lightning, Colorless, Colorless, the energy cost 3 and the damage of 70 with the description: ""Move an Energy card attached to Ampharos to 1 of your Benched Pokemon."". It has the ability ""Damage Bind"" with the description: ""Each Pokemon that has any damage counters on it (both yours and your opponent's) can't use any Poke-Powers."". It has weakness against Fighting +30. It has resistance against Metal -20.",
  "name": "Ampharos",
  "hp": "130",
  "set_name": "Platinum"
}
```

### Data Fields

 - `id`: Unique ID of the pokemon card.
 - `image_url`: Static URL for downloading the image associated with the post.
 - `caption`: Caption generated for this card.
 - `name`: Name of the pokemon on that card.
 - `hp`: Health of the pokemon.
 - `set_name`: The name of the set the card is in.

### Data Splits

All the data is contained in training set. The training set has nearly 13k instances.

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

[More Information Needed]

### Licensing Information

[More Information Needed]

### Citation Information

[More Information Needed]

### Contributions