---
language: 
  - nl
tags:
- text-classification
- sentiment-analysis
datasets:
- train
- test
- validation
---

## Dataset overview
This is a dataset that contains restaurant reviews gathered in 2019 using a webscraping tool in Python. Reviews on restaurant visits and restaurant features were collected for Dutch restaurants. 
The dataset is formatted using the 🤗[DatasetDict](https://huggingface.co/docs/datasets/index) format and contains the following indices:
- train, 116693 records
- test, 14587 records
- validation, 14587 records

The dataset holds both information of the restaurant level as well as the review level and contains the following features:
- [restaurant_ID] > unique restaurant ID
- [restaurant_review_ID] > unique review ID
- [michelin_label] > indicator whether this restaurant was awarded one (or more) Michelin stars prior to 2020
- [score_total] > restaurant level total score
- [score_food] > restaurant level food score
- [score_service] > restaurant level service score
- [score_decor] > restaurant level decor score
- [fame_reviewer] > label for how often a reviewer has posted a restaurant review
- [reviewscore_food] > review level food score
- [reviewscore_service] > review level service score
- [reviewscore_ambiance] > review level ambiance score
- [reviewscore_waiting] > review level waiting score
- [reviewscore_value] > review level value for money score
- [reviewscore_noise] > review level noise score
- [review_text] > the full review that was written by the reviewer for this restaurant
- [review_length] > total length of the review (tokens)

## Purpose
The restaurant reviews submitted by visitor can be used to model the restaurant scores (food, ambiance etc) or used to model Michelin star holders. In [this blog series](https://medium.com/broadhorizon-cmotions/natural-language-processing-for-predictive-purposes-with-r-cb65f009c12b) we used the review texts to predict next Michelin star restaurants, using R. 