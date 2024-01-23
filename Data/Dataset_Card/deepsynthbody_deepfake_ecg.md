---
license: cc-by-4.0
language:
- en
tags:
- generation
- ECG generation
pretty_name: DeepFake-ECG
size_categories:
- 10B<n<100B
---


## DeepFake electrocardiograms: the beginning of the end for privacy issues in medicine

[Paper](https://www.nature.com/articles/s41598-021-01295-2) 
[GitHub](https://github.com/vlbthambawita/deepfake-ecg) 
[Original-data-source](https://osf.io/6hved/) 
[PyPI](https://pypi.org/project/deepfake-ecg/)

## How to download

### Option 1
``` python
from datasets import load_dataset
dataset = load_dataset("deepsynthbody/deepfake_ecg")
```

### Option 2
```bash
git lfs install
git clone https://huggingface.co/datasets/deepsynthbody/deepfake_ecg

# if you want to clone without large files – just their pointers
# prepend your git clone with the following env var:
GIT_LFS_SKIP_SMUDGE=1
```

## Demo of using the generator used to generate this dataset

https://huggingface.co/spaces/deepsynthbody/deepfake-ecg-generator


### Content

Big data is needed to implement personalized medicine, but privacy issues are a prevalent problem for collecting data and sharing them between researchers. A solution is synthetic data generated to represent real dataset carrying similar information. Here, we present generative adversarial networks (GANs) capable of generating realistic synthetic DeepFake 12-lead 10-sec electrocardiograms (ECGs). We have developed and compare two methods, namely WaveGAN* and Pulse2Pulse GAN. We trained the GANs with 7,233 real normal ECG to produce 121,977 DeepFake normal ECGs. By verifying the ECGs using a commercial ECG interpretation program (MUSE 12SL, GE Healthcare), we demonstrate that the Pulse2Pulse GAN was superior to the WaveGAN to produce realistic ECGs. ECG intervals and amplitudes were similar between the DeepFake and real ECGs. These synthetic ECGs are fully anonymous and cannot be referred to any individual, hence they may be used freely. The synthetic dataset will be available as open access for researchers at OSF.io and the DeepFake generator available at the Python Package Index (PyPI) for generating synthetic ECGs. In conclusion, we were able to generate realistic synthetic ECGs using adversarial neural networks on normal ECGs from two population studies, i.e., there by solving the relevant privacy issues in medical datasets.



### Citation (cite this paper to use this dataset in your research)
```latex
@article{thambawita2021deepfake,
  title={DeepFake electrocardiograms using generative adversarial networks are the beginning of the end for privacy issues in medicine},
  author={Thambawita, Vajira and Isaksen, Jonas L and Hicks, Steven A and Ghouse, Jonas and Ahlberg, Gustav and Linneberg, Allan and Grarup, Niels and Ellervik, Christina and Olesen, Morten Salling and Hansen, Torben and others},
  journal={Scientific reports},
  volume={11},
  number={1},
  pages={1--8},
  year={2021},
  publisher={Nature Publishing Group}
}
```