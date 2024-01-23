---
dataset_info:
  features:
  - name: image
    dtype: image
  splits:
  - name: train
    num_bytes: 4450242498.020249
    num_examples: 287968
  - name: test
    num_bytes: 234247797.33875093
    num_examples: 15157
  download_size: 4756942293
  dataset_size: 4684490295.359
license: mit
---

# Dataset Card for "lsun-bedrooms"

This is a 20% sample of the bedrooms category in [`LSUN`](https://github.com/fyu/lsun), uploaded as a dataset for convenience.

The license for _this compilation only_ is MIT. The data retains the same license as the original dataset.

This is (roughly) the code that was used to upload this dataset:

```Python
import os
import shutil

from miniai.imports import *
from miniai.diffusion import *

from datasets import load_dataset

path_data = Path('data')
path_data.mkdir(exist_ok=True)
path = path_data/'bedroom'

url = 'https://s3.amazonaws.com/fast-ai-imageclas/bedroom.tgz'
if not path.exists():
    path_zip = fc.urlsave(url, path_data)
    shutil.unpack_archive('data/bedroom.tgz', 'data')

dataset = load_dataset("imagefolder", data_dir="data/bedroom")
dataset = dataset.remove_columns('label')
dataset = dataset['train'].train_test_split(test_size=0.05)
dataset.push_to_hub("pcuenq/lsun-bedrooms")
```
