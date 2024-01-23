---
annotations_creators:
  - crowdsourced
language:
  - cs
language_creators:
  - crowdsourced
license:
  - cc-by-sa-4.0
multilinguality:
  - monolingual
pretty_name: CSFD movie reviews (Czech)
size_categories:
  - 10K<n<100K
source_datasets:
  - original
tags:
  - movie reviews
  - rating prediction
task_categories:
  - text-classification
task_ids:
  - sentiment-classification
---



# Dataset Card for CSFD movie reviews (Czech)


## Dataset Description

The dataset contains user reviews from Czech/Slovak movie databse website <https://csfd.cz>.
Each review contains text, rating, date, and basic information about the movie (or TV series).
The dataset has in total (train+validation+test) 30,000 reviews. The data is balanced - each rating has approximately the same frequency.


## Dataset Features

Each sample contains:
- `review_id`: unique string identifier of the review.
- `rating_str`: string representation of the rating (from "0/5" to "5/5")
- `rating_int`: integer representation of the rating (from 0 to 5)
- `date`: date of publishing the review (just date, no time nor timezone)
- `comment_language`: language of the review (always "cs")
- `comment`: the string of the review
- `item_title`: title of the reviewed item
- `item_year`: publishing year of the item (string, can also be a range)
- `item_kind`: kind of the item - either "film" or "seriál"
- `item_genres`: list of genres of the item
- `item_directors`: list of director names of the item
- `item_screenwriters`: list of screenwriter names of the item
- `item_cast`: list of actors and actress in the item


## Dataset Source

The data was mined and sampled from the <https://csfd.cz> website.
Make sure to comply with the terms of conditions of the website operator when using the data.

