---
dataset_info:
  features:
  - name: image
    dtype: image
  - name: image_seg
    dtype: image
  - name: landmarks
    dtype: string
  splits:
  - name: train
    num_bytes: 33730885609.0
    num_examples: 100000
  download_size: 34096881533
  dataset_size: 33730885609.0
---
# Dataset Card for `face_synthetics`

This is a copy of [Microsoft FaceSynthetics dataset](https://github.com/microsoft/FaceSynthetics), uploaded to Hugging Face Datasets for convenience.

Please, refer to the original [license](LICENSE.txt), which we replicate in this repo.

The dataset was uploaded using the following code, which assumes the original `zip` file was uncompressed to `/data/microsoft_face_synthetics`:

```Python
from datasets import Dataset
from pathlib import Path
from PIL import Image

face_synthetics = Path("/data/microsoft_face_synthetics")

def entry_for_id(entry_id):
    if type(entry_id) == int:
        entry_id = f"{entry_id:06}"
    image = Image.open(face_synthetics/f"{entry_id}.png")
    image_seg = Image.open(face_synthetics/f"{entry_id}_seg.png")
    with open(face_synthetics/f"{entry_id}_ldmks.txt") as f:
        landmarks = f.read()
    return {
        "image": image,
        "image_seg": image_seg,
        "landmarks": landmarks,
    }

def generate_entries():
    for x in range(100000):
        yield entry_for_id(x)

ds = Dataset.from_generator(generate_entries)
ds.push_to_hub('pcuenq/face_synthetics')
```

Note that `image_seg`, the segmented images, appear to be black because each pixel contains a number between `0` to `18` corresponging to the different categories, see the [original README]() for details. We haven't created visualization code yet.
