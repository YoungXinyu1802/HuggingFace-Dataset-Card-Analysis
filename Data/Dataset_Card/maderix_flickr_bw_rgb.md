---
license: cc-by-nc-sa-4.0
annotations_creators:
- machine-generated
language:
- en
language_creators:
- other
multilinguality:
- monolingual
pretty_name: 'flickr_bw_rgb'
size_categories:
- n<1K
source_datasets:
- N/A
tags: []
task_categories:
- text-to-image
task_ids: []
---
# Dataset Card for Flickr_bw_rgb
_Dataset A image-caption dataset which stores group of black and white and color images with corresponding
 captions mentioning the content of the image with a 'colorized photograph of' or 'Black and white photograph of' suffix.
 This dataset can then be used for fine-tuning image to text models.. Only a train split is provided.
## Examples
  "train/<filename>.jpg" : containing the images in JPEG format
  "train/metadata.jsonl" : Contains the metadata and the fields.
  Dataset columns:
    "file_name"
    "caption"

## Citation

If you use this dataset, please cite it as:

```
@misc{maderix2022flickrbwrgb,
      author = {maderix: maderix@gmail.com},
      title = {flickr_bw_rgb},
      year={2022},
      howpublished= {\url{https://huggingface.co/datasets/maderix/flickr_bw_rgb/}}
} 
```