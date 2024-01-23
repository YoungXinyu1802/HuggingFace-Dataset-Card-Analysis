This is the dataset! Not the .ckpt trained model - the model is located here: https://huggingface.co/0xJustin/Dungeons-and-Diffusion/tree/main

The newest version has manually captioned races and classes, and the model is trained with EveryDream. 30 images each of: aarakocra, aasimar, air_genasi, centaur, dragonborn, drow,
dwarf, earth_genasi, elf, firbolg, fire_genasi, gith, gnome, goblin, goliath, halfling, human, illithid, kenku, kobold, lizardfolk, minotaur, orc, tabaxi, thrikreen, tiefling, tortle, warforged, water_genasi

The original dataset includes ~2500 images of fantasy RPG character art. This dataset has a distribution of races and classes, though only races are annotated right now.


Additionally, BLIP captions were generated for all examples. 
Thus, there are two datasets- one with the human generated race annotation formatted as 'D&D Character, {race}'
BLIP captions are formatted as 'D&D Character, {race} {caption}' for example: 'D&D Character, drow a woman with horns and horns'


Distribution of races:
({'kenku': 31,
  'drow': 162,
  'tiefling': 285,
  'dwarf': 116,  
  'dragonborn': 110,  
  'gnome': 72,  
  'orc': 184,  
  'aasimar': 74,  
  'kobold': 61,  
  'aarakocra': 24,  
  'tabaxi': 123,  
  'genasi': 126,  
  'human': 652,  
  'elf': 190,
  'goblin': 80,
  'halfling': 52,
  'centaur': 22,
  'firbolg': 76,
  'goliath': 35})
  
  
There is a high chance some images are mislabelled! Please feel free to enrich this dataset with whatever attributes you think might be useful!