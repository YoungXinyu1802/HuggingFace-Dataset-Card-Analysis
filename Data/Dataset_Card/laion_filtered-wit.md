# Filtered WIT, an Image-Text Dataset.
A reliable Dataset to run Image-Text models.

You can find WIT, Wikipedia Image Text Dataset, [here](https://github.com/google-research-datasets/wit)
Data was taken from [dalle-mini/wit](https://huggingface.co/datasets/dalle-mini/wit)

## Author
 - [Aarush Katta](https://github.com/ARKseal)

## Data Structure
The data is stored as tars, containing 10,000 samples per tar.
The parquets contain the metadata of each tar, which was crated using [this script](https://huggingface.co/datasets/laion/filtered-wit/blob/main/wit_create_meta.py)
Each tar contains a `.jpg`, `.txt`, and `.json`.
The image is stored in `.jpg`, the caption in `.txt.` and the metadata in `.json`
The preferred method to read the data is [WebDataset](https://github.com/webdataset/webdataset)
Here's an example:
```python
import webdataset as wds

dataset = wds.WebDataset('data/00000.tar').to_tuple('txt', 'jpg', 'json')

for text, image, meta in dataset:
    print(
      text[:50],
      image[:50],
      meta[:50]
    )
```

## Filteration
Each sample has 8 possible captions which were compared to the image using [CLIP ViT-B32](https://arxiv.org/abs/2103.00020)
The text was encoded using [multilingual CLIP text encoder](https://huggingface.co/sentence-transformers/clip-ViT-B-32-multilingual-v1)
Each possible caption was compared to the encoded image using Cosine Similarity
and kept if the sim was greater than `0.26`
Then the new caption was the filtered captions concatenated, and samples with no filtered caption were dropped.
The script used is [filter_wit.py](https://huggingface.co/datasets/laion/filtered-wit/blob/main/filter_wit.py)
