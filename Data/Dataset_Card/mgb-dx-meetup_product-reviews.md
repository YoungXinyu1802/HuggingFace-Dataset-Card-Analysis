---
dataset_info:
  features:
  - name: review_id
    dtype: string
  - name: product_id
    dtype: string
  - name: reviewer_id
    dtype: string
  - name: stars
    dtype: int32
  - name: review_body
    dtype: string
  - name: review_title
    dtype: string
  - name: language
    dtype: string
  - name: product_category
    dtype: string
  splits:
  - name: test
    num_bytes: 454952.85
    num_examples: 1500
  - name: train
    num_bytes: 6073361.466666667
    num_examples: 20000
  download_size: 4034850
  dataset_size: 6528314.316666666
---
# Dataset Card for Product Reviews

Customer reviews of Amazon products, categorised by the number of stars assigned to each product. The dataset consists of several thousand reviews in English, German, and French. 

## Licensing information

This datasets is based on the [`amazon_reviews_multi`](https://huggingface.co/datasets/amazon_reviews_multi) dataset.