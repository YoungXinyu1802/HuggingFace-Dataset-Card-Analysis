## Summary
Metadata information of all the models uploaded on [HuggingFace modelhub](https://huggingface.co/models)
Dataset was last updated on 15th June 2021. Contains information on 10,354 models (v1).
Only `train` dataset is provided

#### Update: v1.0.2: Added downloads_last_month and library data
Same dataset is available in [kaggle](https://www.kaggle.com/crazydiv/huggingface-modelhub)

## Loading data
```python
from datasets import load_dataset
modelhub_dataset = load_dataset("dk-crazydiv/huggingface-modelhub")
```
### Useful commands:
```python
modelhub_dataset["train"] # Access train subset  (the only subset available)
modelhub_dataset["train"][0] # Access the dataset elements by index 
modelhub_dataset["train"].features # Get the columns present in the dataset.
```
### Sample dataset:
```json
{
  "downloads_last_month": 7474,
  "files": [
    ".gitattributes",
    "README.md",
    "config.json",
    "pytorch_model.bin",
    "spiece.model",
    "tf_model.h5",
    "tokenizer.json",
    "with-prefix-tf_model.h5"
  ],
  "lastModified": "2021-01-13T15:08:24.000Z",
  "library": "transformers",
  "modelId": "albert-base-v1",
  "pipeline_tag": "fill-mask",
  "publishedBy": "huggingface",
  "tags": [
    "pytorch",
    "tf",
    "albert",
    "masked-lm",
    "en",
    "dataset:bookcorpus",
    "dataset:wikipedia",
    "arxiv:1909.11942",
    "transformers",
    "exbert",
    "license:apache-2.0",
    "fill-mask"
  ],
  "modelCard": "Readme sample data..."
}
```
## Bugs:
Please report any bugs/improvements to me on [twitter](https://twitter.com/kartik_godawat)