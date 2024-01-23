---
license: cc0-1.0
task_categories:
- summarization
language:
- en
tags:
- superheroes
- heroes
- anime
- manga
- marvel
size_categories:
- 1K<n<10K
---
# Dataset Card for Superheroes

## Dataset Description
1400+ Superheroes history and powers description to apply text mining and NLP [Original source](https://www.kaggle.com/datasets/jonathanbesomi/superheroes-nlp-dataset/code?resource=download)

## Context
The aim of this dataset is to make text analytics and NLP even funnier. All of us have dreamed to be like a superhero and save the world, yet we are still on Kaggle figuring out how python works. Then, why not improve our NLP competences by analyzing Superheros' history and powers?

The particularity of this dataset is that it contains categorical and numerical features such as overall_score, intelligence_score, creator, alignment, gender, eye_color but also text features history_text and powers_text. By combining the two, a lot of interesting insights can be gathered!

## Content
We collected all data from superherodb and cooked for you in a nice and clean tabular format.

The dataset contains 1447 different Superheroes. Each superhero row has:

* overall_score - derivated by superherodb from the power stats features. Can you find the relationship?
* history_text - History of the Superhero (text features)
* powers_text - Description of Superheros' powers (text features)
* intelligence_score, strength_score, speed_score, durability_score, power_score and combat_score. (power stats features)
* "Origin" (full_name, alter_egos, …)
* "Connections" (occupation, base, teams, …)
* "Appareance" (gender, type_race, height, weight, eye_color, …)

## Acknowledgements
The following [Github repository](https://github.com/jbesomi/texthero/tree/master/dataset/Superheroes%20NLP%20Dataset) contains the code used to scrape this Dataset.

