---
license: mit
dataset_info:
  features:
  - name: image
    dtype: image
  - name: label
    dtype:
      class_label:
        names:
          '0': green
          '1': others
  splits:
  - name: train
    num_bytes: 3106612.0
    num_examples: 50
  download_size: 2598455
  dataset_size: 3106612.0
---

![](https://huggingface.co/datasets/TrpFrog/trpfrog-icons/resolve/main/logo.jpg)

# trpfrog-icons Dataset

This is a dataset of [TrpFrog](https://trpfrog.net)'s icons. By the way, what do you use this for? 🤔

## How to use

```py
from datasets import load_dataset

dataset = load_dataset("TrpFrog/trpfrog-icons")
```

```py
# print all data
for data in dataset["train"]:
    print(data)

# remove not green icons
dataset = dataset.filter(lambda x: x["label"] == 0)
```

## License

MIT License