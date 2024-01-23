---
task_categories:
- image-classification

---
# AutoTrain Dataset for project: data-image

## Dataset Description

This dataset has been automatically processed by AutoTrain for project data-image.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "image": "<600x825 RGB PIL image>",
    "target": 0,
    "feat_name": "Alakazam",
    "feat_supertype": "Pok\u00e9mon",
    "feat_subtypes_1": "Stage 2",
    "feat_level": 42.0,
    "feat_hp": 80.0,
    "feat_types_1": "Psychic",
    "feat_evolvesFrom": "Kadabra",
    "feat_abilities_1_name": "Damage Swap",
    "feat_abilities_1_text": "As often as you like during your turn (before your attack), you may move 1 damage counter from 1 of your Pok\u00e9mon to another as long as you don't Knock Out that Pok\u00e9mon. This power can't be used if Alakazam is Asleep, Confused, or Paralyzed.",
    "feat_abilities_1_type": "Pok\u00e9mon Power",
    "feat_attacks_1_name": "Confuse Ray",
    "feat_attacks_1_cost_1": "Psychic",
    "feat_attacks_1_cost_2": "Psychic",
    "feat_attacks_1_cost_3": "Psychic",
    "feat_attacks_1_convertedEnergyCost": 3.0,
    "feat_attacks_1_damage": "30",
    "feat_attacks_1_text": "Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused.",
    "feat_weaknesses_1_type": "Psychic",
    "feat_weaknesses_1_value": "\u00d72",
    "feat_retreatCost_1": "Colorless",
    "feat_retreatCost_2": "Colorless",
    "feat_retreatCost_3": "Colorless",
    "feat_convertedRetreatCost": 3.0,
    "feat_number": 1,
    "feat_artist": "Ken Sugimori",
    "feat_rarity": "Rare Holo",
    "feat_flavorText": "Its brain can outperform a supercomputer. Its intelligence quotient is said to be 5000.",
    "feat_nationalPokedexNumbers_1": 65.0,
    "feat_legalities_unlimited": "Legal",
    "feat_images_small": "https://images.pokemontcg.io/base1/1.png",
    "feat_images_large": "https://images.pokemontcg.io/base1/1_hires.png",
    "feat_evolvesTo_1": null,
    "feat_attacks_2_name": null,
    "feat_attacks_2_cost_1": null,
    "feat_attacks_2_cost_2": null,
    "feat_attacks_2_cost_3": null,
    "feat_attacks_2_cost_4": null,
    "feat_attacks_2_convertedEnergyCost": null,
    "feat_attacks_2_damage": null,
    "feat_attacks_2_text": null,
    "feat_resistances_1_type": null,
    "feat_resistances_1_value": null,
    "feat_attacks_1_cost_4": null,
    "feat_evolvesTo_2": null,
    "feat_legalities_expanded": null,
    "feat_rules_1": null,
    "feat_legalities_standard": null
  },
  {
    "image": "<600x825 RGB PIL image>",
    "target": 14,
    "feat_name": "Blastoise",
    "feat_supertype": "Pok\u00e9mon",
    "feat_subtypes_1": "Stage 2",
    "feat_level": 52.0,
    "feat_hp": 100.0,
    "feat_types_1": "Water",
    "feat_evolvesFrom": "Wartortle",
    "feat_abilities_1_name": "Rain Dance",
    "feat_abilities_1_text": "As often as you like during your turn (before your attack), you may attach 1 Water Energy card to 1 of your Water Pok\u00e9mon. (This doesn't use up your 1 Energy card attachment for the turn.) This power can't be used if Blastoise is Asleep, Confused, or Paralyzed.",
    "feat_abilities_1_type": "Pok\u00e9mon Power",
    "feat_attacks_1_name": "Hydro Pump",
    "feat_attacks_1_cost_1": "Water",
    "feat_attacks_1_cost_2": "Water",
    "feat_attacks_1_cost_3": "Water",
    "feat_attacks_1_convertedEnergyCost": 3.0,
    "feat_attacks_1_damage": "40+",
    "feat_attacks_1_text": "Does 40 damage plus 10 more damage for each Water Energy attached to Blastoise but not used to pay for this attack's Energy cost. Extra Water Energy after the 2nd doesn't count.",
    "feat_weaknesses_1_type": "Lightning",
    "feat_weaknesses_1_value": "\u00d72",
    "feat_retreatCost_1": "Colorless",
    "feat_retreatCost_2": "Colorless",
    "feat_retreatCost_3": "Colorless",
    "feat_convertedRetreatCost": 3.0,
    "feat_number": 2,
    "feat_artist": "Ken Sugimori",
    "feat_rarity": "Rare Holo",
    "feat_flavorText": "A brutal Pok\u00e9mon with pressurized water jets on its shell. They are used for high-speed tackles.",
    "feat_nationalPokedexNumbers_1": 9.0,
    "feat_legalities_unlimited": "Legal",
    "feat_images_small": "https://images.pokemontcg.io/base1/2.png",
    "feat_images_large": "https://images.pokemontcg.io/base1/2_hires.png",
    "feat_evolvesTo_1": null,
    "feat_attacks_2_name": null,
    "feat_attacks_2_cost_1": null,
    "feat_attacks_2_cost_2": null,
    "feat_attacks_2_cost_3": null,
    "feat_attacks_2_cost_4": null,
    "feat_attacks_2_convertedEnergyCost": null,
    "feat_attacks_2_damage": null,
    "feat_attacks_2_text": null,
    "feat_resistances_1_type": null,
    "feat_resistances_1_value": null,
    "feat_attacks_1_cost_4": null,
    "feat_evolvesTo_2": null,
    "feat_legalities_expanded": null,
    "feat_rules_1": null,
    "feat_legalities_standard": null
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "image": "Image(decode=True, id=None)",
  "target": "ClassLabel(names=['base1-1', 'base1-10', 'base1-100', 'base1-101', 'base1-102', 'base1-11', 'base1-12', 'base1-13', 'base1-14', 'base1-15', 'base1-16', 'base1-17', 'base1-18', 'base1-19', 'base1-2', 'base1-20', 'base1-21', 'base1-22', 'base1-23', 'base1-24', 'base1-25', 'base1-26', 'base1-27', 'base1-28', 'base1-29', 'base1-3', 'base1-30', 'base1-31', 'base1-32', 'base1-33', 'base1-34', 'base1-35', 'base1-36', 'base1-37', 'base1-38', 'base1-39', 'base1-4', 'base1-40', 'base1-41', 'base1-42', 'base1-43', 'base1-44', 'base1-45', 'base1-46', 'base1-47', 'base1-48', 'base1-49', 'base1-5', 'base1-50', 'base1-51', 'base1-52', 'base1-53', 'base1-54', 'base1-55', 'base1-56', 'base1-57', 'base1-58', 'base1-59', 'base1-6', 'base1-60', 'base1-61', 'base1-62', 'base1-63', 'base1-64', 'base1-65', 'base1-66', 'base1-67', 'base1-68', 'base1-69', 'base1-7', 'base1-70', 'base1-71', 'base1-72', 'base1-73', 'base1-74', 'base1-75', 'base1-76', 'base1-77', 'base1-78', 'base1-79', 'base1-8', 'base1-80', 'base1-81', 'base1-82', 'base1-83', 'base1-84', 'base1-85', 'base1-86', 'base1-87', 'base1-88', 'base1-89', 'base1-9', 'base1-90', 'base1-91', 'base1-92', 'base1-93', 'base1-94', 'base1-95', 'base1-96', 'base1-97', 'base1-98', 'base1-99'], id=None)",
  "feat_name": "Value(dtype='string', id=None)",
  "feat_supertype": "Value(dtype='string', id=None)",
  "feat_subtypes_1": "Value(dtype='string', id=None)",
  "feat_level": "Value(dtype='float64', id=None)",
  "feat_hp": "Value(dtype='float64', id=None)",
  "feat_types_1": "Value(dtype='string', id=None)",
  "feat_evolvesFrom": "Value(dtype='string', id=None)",
  "feat_abilities_1_name": "Value(dtype='string', id=None)",
  "feat_abilities_1_text": "Value(dtype='string', id=None)",
  "feat_abilities_1_type": "Value(dtype='string', id=None)",
  "feat_attacks_1_name": "Value(dtype='string', id=None)",
  "feat_attacks_1_cost_1": "Value(dtype='string', id=None)",
  "feat_attacks_1_cost_2": "Value(dtype='string', id=None)",
  "feat_attacks_1_cost_3": "Value(dtype='string', id=None)",
  "feat_attacks_1_convertedEnergyCost": "Value(dtype='float64', id=None)",
  "feat_attacks_1_damage": "Value(dtype='string', id=None)",
  "feat_attacks_1_text": "Value(dtype='string', id=None)",
  "feat_weaknesses_1_type": "Value(dtype='string', id=None)",
  "feat_weaknesses_1_value": "Value(dtype='string', id=None)",
  "feat_retreatCost_1": "Value(dtype='string', id=None)",
  "feat_retreatCost_2": "Value(dtype='string', id=None)",
  "feat_retreatCost_3": "Value(dtype='string', id=None)",
  "feat_convertedRetreatCost": "Value(dtype='float64', id=None)",
  "feat_number": "Value(dtype='int64', id=None)",
  "feat_artist": "Value(dtype='string', id=None)",
  "feat_rarity": "Value(dtype='string', id=None)",
  "feat_flavorText": "Value(dtype='string', id=None)",
  "feat_nationalPokedexNumbers_1": "Value(dtype='float64', id=None)",
  "feat_legalities_unlimited": "Value(dtype='string', id=None)",
  "feat_images_small": "Value(dtype='string', id=None)",
  "feat_images_large": "Value(dtype='string', id=None)",
  "feat_evolvesTo_1": "Value(dtype='string', id=None)",
  "feat_attacks_2_name": "Value(dtype='string', id=None)",
  "feat_attacks_2_cost_1": "Value(dtype='string', id=None)",
  "feat_attacks_2_cost_2": "Value(dtype='string', id=None)",
  "feat_attacks_2_cost_3": "Value(dtype='string', id=None)",
  "feat_attacks_2_cost_4": "Value(dtype='string', id=None)",
  "feat_attacks_2_convertedEnergyCost": "Value(dtype='float64', id=None)",
  "feat_attacks_2_damage": "Value(dtype='string', id=None)",
  "feat_attacks_2_text": "Value(dtype='string', id=None)",
  "feat_resistances_1_type": "Value(dtype='string', id=None)",
  "feat_resistances_1_value": "Value(dtype='float64', id=None)",
  "feat_attacks_1_cost_4": "Value(dtype='string', id=None)",
  "feat_evolvesTo_2": "Value(dtype='string', id=None)",
  "feat_legalities_expanded": "Value(dtype='string', id=None)",
  "feat_rules_1": "Value(dtype='string', id=None)",
  "feat_legalities_standard": "Value(dtype='string', id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 102 |
| valid        | 2 |
