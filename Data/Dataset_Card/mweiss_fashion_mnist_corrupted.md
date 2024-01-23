---
annotations_creators:
- expert-generated
- machine-generated
language_creators:
- machine-generated
language:
- en
license:
- mit
multilinguality:
- monolingual
pretty_name: fashion-mnist-corrupted
size_categories:
- 10K<n<100K
source_datasets:
- extended|fashion_mnist
task_categories:
- image-classification
task_ids: []
---

# Fashion-Mnist-C (Corrupted Fashion-Mnist)

A corrupted Fashion-MNIST benchmark for testing out-of-distribution robustness of computer vision models, which were trained on Fashion-Mmnist.

[Fashion-Mnist](https://github.com/zalandoresearch/fashion-mnist) is a drop-in replacement for MNIST and Fashion-Mnist-C is a corresponding drop-in replacement for [MNIST-C](https://arxiv.org/abs/1906.02337).

## Corruptions
The following corruptions are applied to the images, equivalently to MNIST-C:

- **Noise** (shot noise and impulse noise)
- **Blur** (glass and motion blur)
- **Transformations** (shear, scale, rotate, brightness, contrast, saturate, inverse)

In addition, we apply various **image flippings and turnings**: For fashion images, flipping the image does not change its label,
and still keeps it a valid image. However, we noticed that in the nominal fmnist dataset, most images are identically oriented 
(e.g. most shoes point to the left side). Thus, flipped images provide valid OOD inputs.

Most corruptions are applied at a randomly selected level of *severity*, s.t. some corrupted images are really hard to classify whereas for others the corruption, while present, is subtle.

## Examples

| Turned  | Blurred | Rotated | Noise | Noise | Turned |
| ------------- | ------------- | --------| --------- | -------- | --------- |
| <img src="https://github.com/testingautomated-usi/fashion-mnist-c/raw/main/generated/png-examples/single_0.png" width="100" height="100">   | <img src="https://github.com/testingautomated-usi/fashion-mnist-c/raw/main/generated/png-examples/single_1.png" width="100" height="100"> |  <img src="https://github.com/testingautomated-usi/fashion-mnist-c/raw/main/generated/png-examples/single_6.png" width="100" height="100"> |  <img src="https://github.com/testingautomated-usi/fashion-mnist-c/raw/main/generated/png-examples/single_3.png" width="100" height="100"> |  <img src="https://github.com/testingautomated-usi/fashion-mnist-c/raw/main/generated/png-examples/single_4.png" width="100" height="100"> |  <img src="https://github.com/testingautomated-usi/fashion-mnist-c/raw/main/generated/png-examples/single_5.png" width="100" height="100"> |



## Citation
If you use this dataset, please cite the following paper:

```
@inproceedings{Weiss2022SimpleTechniques,
  title={Simple Techniques Work Surprisingly Well for Neural Network Test Prioritization and Active Learning},
  author={Weiss, Michael and Tonella, Paolo},
  booktitle={Proceedings of the 31th ACM SIGSOFT International Symposium on Software Testing and Analysis},
  year={2022}
}
```

Also, you may want to cite FMNIST and MNIST-C.

## Credits
- Fashion-Mnist-C is inspired by Googles MNIST-C and our repository is essentially a clone of theirs. See their [paper](https://arxiv.org/abs/1906.02337) and [repo](https://github.com/google-research/mnist-c).
- Find the nominal (i.e., non-corrupted) Fashion-MNIST dataset [here](https://github.com/zalandoresearch/fashion-mnist).
