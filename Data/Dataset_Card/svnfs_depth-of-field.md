---
license: apache-2.0
annotations_creators:
- Stavros Niafas
sample_number:
- 1200
class_number:
- 2
image_size:
- (200,300,3)
source_dataset:
- unsplash
task_categories:
- image-classification
- image-segmentation
dataset_info:
- config_name: depth-of-field
  features:
  - name: image
    dtype: string
  - name: class
    dtype:
      class_label:
        names:
          0: bokeh
          1: no-bokeh
- config_name: default
  features:
  - name: image
    dtype: image
  - name: label
    dtype:
      class_label:
        names:
          0: '0'
          1: '1'
  splits:
  - name: train
    num_bytes: 192150
    num_examples: 1200
  download_size: 38792692
  dataset_size: 192150
---
## Dataset Summary

Depth-of-Field(DoF) dataset is comprised of 1200 annotated images, binary annotated with(0) and without(1) bokeh effect, shallow or deep depth of field. It is a forked data set from the [Unsplash 25K](https://github.com/unsplash/datasets) data set.

## Dataset Description

- **Repository:** [https://github.com/sniafas/photography-style-analysis](https://github.com/sniafas/photography-style-analysis)
- **Paper:** [More Information Needed](https://www.researchgate.net/publication/355917312_Photography_Style_Analysis_using_Machine_Learning)

### Citation Information
```
@article{sniafas2021,
  title={DoF: An image dataset for depth of field classification},
  author={Niafas, Stavros},
  doi= {10.13140/RG.2.2.29880.62722},
  url= {https://www.researchgate.net/publication/364356051_DoF_depth_of_field_datase}
  year={2021}
}
```
Note that each DoF dataset has its own citation. Please see the source to
get the correct citation for each contained dataset.