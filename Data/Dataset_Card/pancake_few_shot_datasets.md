---
license: mit
---
# Five standard datasets for few-shot classification
- *miniImageNet*. It contains 100 classes with 600 images in each class, which are built upon the ImageNet dataset. The 100 classes are divided into 64, 16, 20 for meta-training, meta-validation and meta-testing, respectively.
- *tieredImageNet*. TieredImageNet is also a subset of ImageNet, which includes 608 classes from 34 super-classes. Compared with miniImageNet, the splits of meta-training(20), meta-validation(6) and meta-testing(8) are set according to the super-classes to enlarge the domain difference between training and testing phase. The dataset also include more images for training and evaluation.
- *CIFAR-FS*. CIFAR-FS is divided from CIFAR-100, which consists of 60,000 images in 100 categories. The CIFAR-FS is divided into 64, 16 and 20 for training, validation, and evaluation, respectively.
- *FC100*. FC100 is also divided from CIFAR-100, which is more difficult because it is more diverse. The FC100 uses a split similar to tieredImageNet, where train, validation, and test splits contain 60, 20, and 20 classes. 
- *CUB*. CUB-200-2011 (CUB) is a fine-grained dataset of 200 bird species with total 11,788 images. It is is randomly divided into three disjoint sets of the training set (100 classes), validation set (50 classes), and testing set (50 classes).