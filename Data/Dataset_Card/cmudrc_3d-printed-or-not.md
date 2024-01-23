---
doi: 10.1016/j.dib.2019.104691
annotations_creators:
- expert-generated
language:
- en
language_creators:
- found
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: 3d-Printed Or Not?
size_categories:
- 10K<n<100K
source_datasets:
- original
tags:
- engineering
- additive manufacturing
- 3d printing
task_categories:
- image-classification
task_ids: []
dataset_info:
  features:
  - name: image
    dtype: image
  - name: label
    dtype:
      class_label:
        names:
          '0': 3d_printed
          '1': not_3d_printed
  splits:
  - name: train
    num_bytes: 663853489.6
    num_examples: 51520
  download_size: 497323960
  dataset_size: 663853489.6
---
# `3d-printed-or-not`: An Image Dataset of 3D-printed Prototypes
This dataset is a collection of images that are particularly relevant to engineering and design, consisting of two categories: 3D-printed prototypes, and non-3D-printed prototypes This data was collected through a hybrid approach that entailed both web scraping and direct collection from engineering labs and workspaces at Penn State University. The initial data was then augmented using several data augmentation techniques including rotation, noise, blur, and color shifting. This results in 25,760 images in each class. 
