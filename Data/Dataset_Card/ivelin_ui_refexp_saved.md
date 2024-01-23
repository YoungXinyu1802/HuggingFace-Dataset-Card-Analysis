---
dataset_info:
  features:
  - name: image
    dtype: image
  - name: image_id
    dtype: string
  - name: image_file_path
    dtype: string
  - name: prompt
    dtype: string
  - name: target_bounding_box
    dtype: string
  splits:
  - name: train
    num_bytes: 1910805137.216
    num_examples: 15624
  - name: validation
    num_bytes: 60403386
    num_examples: 471
  - name: test
    num_bytes: 69078983
    num_examples: 565
  download_size: 1246541216
  dataset_size: 2040287506.216
license: cc-by-4.0
task_categories:
- image-to-text
language:
- en
pretty_name: UIBert Referring Expressions Dataset
size_categories:
- 10K<n<100K
---
# Dataset Card for "ui_refexp_saved_Jan2023"

This is a saved snapshot of the dynamically generated [UI Bert](https://huggingface.co/datasets/ivelin/ui_refexp) dataset. 
Much faster download time than the dynamic version which pulls and filters large data files from remote sources.