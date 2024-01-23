This repository contains the mapping from integer id's to actual label names (in HuggingFace Transformers typically called `id2label`) for several datasets.

Current datasets include:
- ImageNet-1k
- ImageNet-22k (also called ImageNet-21k as there are 21,843 classes)
- COCO detection 2017
- COCO panoptic 2017
- ADE20k (actually, the [MIT Scene Parsing benchmark](http://sceneparsing.csail.mit.edu/), which is a subset of ADE20k)
- Cityscapes
- VQAv2
- Kinetics-700
- RVL-CDIP
- PASCAL VOC
- Kinetics-400
- ...

You can read in a label file as follows (using the `huggingface_hub` library):

```
from huggingface_hub import hf_hub_download
import json

repo_id = "huggingface/label-files"
filename = "imagenet-22k-id2label.json"
id2label = json.load(open(hf_hub_download(repo_id, filename, repo_type="dataset"), "r"))
id2label = {int(k):v for k,v in id2label.items()}
```

To add an `id2label` mapping for a new dataset, simply define a Python dictionary, and then save that dictionary as a JSON file, like so:
```
import json

# simple example
id2label = {0: 'cat', 1: 'dog'}

with open('cats-and-dogs-id2label.json', 'w') as fp:
    json.dump(id2label, fp)
```
You can then upload it to this repository (assuming you have write access).
