---
task_categories:
- feature-extraction
- image-classification
- zero-shot-image-classification
pretty_name: Perturbed Faces
size_categories:
- 1K<n<10K
---

# Perturbed Faces

This dataset contains 1000 images from [CelebA dataset](!https://www.kaggle.com/datasets/jessicali9530/celeba-dataset). For each of the thousand images dataset also has [LowKey](https://openreview.net/forum?id=hJmtwocEqzc) perturbed version and [Fawkes](https://sandlab.cs.uchicago.edu/fawkes/) perturbed version. 
LowKey and Fawkes perturbed images have _attacked & _cloaked at the end of the filename respectively.


| File Name           | Version                  |
|---------------------|--------------------------|
| 000001.jpg          | Original                 |
| 000001_cloaked.png  | Fawkes perturbed version |
| 000001_attacked.png | LowKey perturbed version |


The Fawkes perturbed images are created using CLI provided in the [github repository](https://github.com/Shawn-Shan/fawkes) with protection mode set to mid. The LowKey version of
images are created using Python code provided with the paper.


## Citation
If you found this work helpful for your research, please cite it as following:
```
@misc{2301.07315,
Author = {Aaditya Bhat and Shrey Jain},
Title = {Face Recognition in the age of CLIP & Billion image datasets},
Year = {2023},
Eprint = {arXiv:2301.07315},
}
```