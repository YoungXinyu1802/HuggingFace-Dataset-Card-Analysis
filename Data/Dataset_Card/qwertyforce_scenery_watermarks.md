---
license: cc-by-nc-4.0
task_categories:
- image-classification
tags:
- watermark
dataset_info:
  features:
  - name: image
    dtype: image
  - name: label
    dtype:
      class_label:
        names:
          '0': no_watermark
          '1': watermark
  splits:
  - name: train
    num_bytes: 1094841327.222
    num_examples: 22762
  download_size: 1057455120
  dataset_size: 1094841327.222
pretty_name: Scenery Watermarks
size_categories:
- 10K<n<100K
---

Dataset for watermark classification (no_watermark/watermark)  
~22k images, 512x512,  manually annotated   
additional info - https://github.com/qwertyforce/scenery_watermarks