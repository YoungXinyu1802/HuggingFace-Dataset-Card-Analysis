---
annotations_creators:
- machine-generated
language:
- en
language_creators:
- machine-generated
license: []
multilinguality:
- monolingual
pretty_name: MovieLens User Ratings
size_categories:
- 100K<n<1M
source_datasets: []
tags:
- movielens
- recommendation
- collaborative filtering
task_categories: []
task_ids: []
---

# MovieLens User Ratings

This dataset contains ~1M user ratings, consisting of ~10k of the most recent movies from the MovieLens 25M dataset, for which over 30k unique users have rated. The dataset is streamed from the MovieLens 25M dataset, filters for the recent movies, and returns the user ratings for those. After a few joins and checks, we get this dataset. Included are the URLs of the respective movie posters.

The dataset is part of an example on [building a movie recommendation engine](https://www.pinecone.io/docs/examples/movie-recommender-system/) with vector search.