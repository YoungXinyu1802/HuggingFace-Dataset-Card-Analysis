---
dataset_info:
  features:
  - name: id
    dtype: int64
  - name: entity_id
    dtype: int64
  - name: name
    dtype: string
  - name: query
    dtype: string
  - name: relevance
    dtype: float64
  - name: description
    dtype: string
  splits:
  - name: train
    num_bytes: 74803048
    num_examples: 74067
  download_size: 32449185
  dataset_size: 74803048
---
# Dataset Card for "home_depot"

[More Information needed](https://github.com/huggingface/datasets/blob/main/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

[source](https://www.kaggle.com/competitions/home-depot-product-search-relevance)

Dataset Description
This data set contains a number of products and real customer search terms from Home Depot's website. The challenge is to predict a relevance score for the provided combinations of search terms and products. To create the ground truth labels, Home Depot has crowdsourced the search/product pairs to multiple human raters.

The relevance is a number between 1 (not relevant) to 3 (highly relevant). For example, a search for "AA battery" would be considered highly relevant to a pack of size AA batteries (relevance = 3), mildly relevant to a cordless drill battery (relevance = 2), and not relevant to a snow shovel (relevance = 1).

Each pair was evaluated by at least three human raters. The provided relevance scores are the average value of the ratings. There are three additional things to know about the ratings:

The specific instructions given to the raters is provided in relevance_instructions.docx.
Raters did not have access to the attributes.
Raters had access to product images, while the competition does not include images.
Your task is to predict the relevance for each pair listed in the test set. Note that the test set contains both seen and unseen search terms.
