---
language: ar
datasets: flickr8k
---

# Flickr8k Image Features

Flickr8k image features are extracted using the ResNeXt-152 C4 architecture ([found here](https://github.com/microsoft/scene_graph_benchmark)) and can be used as input for the [OSCAR](https://github.com/microsoft/Oscar) learning method. Arabic captions and splits are provided by [ElJundi et al.](https://github.com/ObeidaElJundi/Arabic-Image-Captioning)

## Dev-split
+ **dev-arabic.yaml** Yaml configure file with Arabic object tags
+ **dev.feature.tsv** Extracted image features
+ **dev.label.arabic.tsv** Arabic labels
+  **dev.label.tsv** English labels
+ **dev.yaml** Yaml configure file with English object tags
+ **dev_caption.json** Arabic captions for training
+ **dev_caption_coco_format.json** Arabic captions for validation

## Test-split
+ **test-arabic.yaml** Yaml configure file with Arabic object tags
+ **test.feature.tsv** Extracted image features
+ **test.label.arabic.tsv** Arabic labels
+  **test.label.tsv** English labels
+ **test.yaml** Yaml configure file with English object tags
+ **test_caption.json** Arabic captions for training
+ **test_caption_coco_format.json** Arabic captions for validation

## Train-split
+ **train-arabic.yaml** Yaml configure file with Arabic object tags
+ **train.feature.tsv** Extracted image features
+ **train.label.arabic.tsv** Arabic labels
+  **train.label.tsv** English labels
+ **train.yaml** Yaml configure file with English object tags
+ **train_caption.json** Arabic captions for training
+ **train_caption_coco_format.json** Arabic captions for validation