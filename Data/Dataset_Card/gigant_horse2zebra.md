---
license: cc
task_categories:
- image-to-image
task_ids: []
pretty_name: Horse2Zebra
tags:
- GAN
- unpaired-image-to-image-translation
---
## Dataset Description
- **Homepage:** https://people.eecs.berkeley.edu/~taesung_park/CycleGAN/datasets/
- **Paper:** https://arxiv.org/abs/1703.10593

### Dataset Summary

This dataset was obtained from the original CycleGAN Datasets directory available on [Berkeley's website](https://people.eecs.berkeley.edu/~taesung_park/CycleGAN/datasets/).


For more details about the dataset you can refer to the [original CycleGAN publication](https://arxiv.org/abs/1703.10593).

### How to use

You can easily load the dataset with the following lines :

```python
from datasets import load_dataset

data_horses = load_dataset("gigant/horse2zebra", name="horse", split="train")
data_zebras = load_dataset("gigant/horse2zebra", name="zebra", split="train")
```
Two splits are available, `"train"` and `"test"`

### Citation Information

```
@inproceedings{CycleGAN2017,
  title={Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks},
  author={Zhu, Jun-Yan and Park, Taesung and Isola, Phillip and Efros, Alexei A},
  booktitle={Computer Vision (ICCV), 2017 IEEE International Conference on},
  year={2017}
}
```