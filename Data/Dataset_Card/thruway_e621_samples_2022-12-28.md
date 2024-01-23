---
extra_gated_heading: Terms of use
extra_gated_button_content: Acknowledge
extra_gated_fields:
  I will use this dataset in a way that does not hinder the ability of artists to make a living from their work: checkbox
  I acknowledge that the content contained within this dataset is the intellectual property of the artists who created it: checkbox
  If I should wish to use this dataset for any commercial purposes, it is my responsibility to obtain the appropriate permissions from the copyright holders: checkbox
dataset_info:
  features:
  - name: id
    dtype: uint32
  - name: created_at
    dtype: timestamp[us]
  - name: updated_at
    dtype: timestamp[us]
  - name: image
    dtype: image
  - name: tags
    sequence: uint32
  - name: rating
    dtype: uint8
  - name: fav_count
    dtype: uint32
  - name: comment_count
    dtype: uint32
  - name: up_score
    dtype: int32
  - name: down_score
    dtype: int32
  splits:
  - name: train
    num_bytes: 384353755927.75
    num_examples: 3065570
  download_size: 382556768725
  dataset_size: 384353755927.75
viewer: false
---

All images of all ratings from e621.net from the date it was generated, at sample resolution where possible.

This includes the following additional metadata:
- post ID
- created at
- updated at
- tags (stored as IDs you can cross-reference from an e621 tags dump)
- rating (0 = safe, 1 = questionable, 2 = explicit)
- favorite count
- comment count
- up score
- down score

Note that this dataset excludes images that are, at the time of scraping:
- pending
- tagged with tags indicating that it is illegal to possess in most jurisdictions

Some files in this dataset may be corrupted. Make sure you're able to handle invalid images in your processing code or you're going to have bad time!