---
license: mit
---

This contains the datasets for the Trojan Detection Challenge NeurIPS 2022 competition. To learn more, please see the [competition website](http://trojandetection.ai/).

# **Trojan Detection**

##### Detect and Analyze Trojan attacks on deep neural networks that are designed to be difficult to detect. 

### **Overview**

Neural Trojans are a growing concern for the security of ML systems, but little is known about the fundamental offense-defense balance of Trojan detection. Early work suggests that standard Trojan attacks may be easy to detect, but recently it has been shown that in simple cases one can design practically undetectable Trojans.

This repository contains code for the **Trojan Detection Challenge (TDC) NeurIPS 2022** [competition](https://trojandetection.ai/).

There are 3 main tracks for this competition:
- **Trojan Detection Track**: Given a dataset of Trojaned and clean networks spanning multiple data sources, build a Trojan detector that classifies a test set of networks with held-out labels (Trojan, clean). For more information, see here.

- **Trojan Analysis Track**: Given a dataset of Trojaned networks spanning multiple data sources, predict various properties of Trojaned networks on a test set with held-out labels. This track has two subtracks: (1) target label prediction, (2) trigger synthesis. For more information, see here.

- **Evasive Trojans Track**: Given a dataset of clean networks and a list of attack specifications, train a small set of Trojaned networks meeting the specifications and upload them to the evaluation server. The server will verify that the attack specifications are met, then train and evaluate a baseline Trojan detector using held-out clean networks and the submitted Trojaned networks. The task is to create Trojaned networks that are hard to detect. For more information, see here.

The competition has two rounds: In the primary round, participants will compete on the three main tracks. In the final round, the solution of the first-place team in the Evasive Trojans track will be used to train a new set of hard-to-detect Trojans, and participants will compete to detect these networks. For more information on the final round, see here.

### **Contents**

There are four folders corresponding to different tracks and subtracks: 1) Trojan Detection, 2) Trojan Analysis (Target Label Prediction), 3) Trojan Analysis (Trigger Synthesis), and 4) Evasive Trojans. We provide starter code for submitting baselines in ```example_submission.ipynb``` under each folder. The ```tdc_datasets``` folder is expected to be under the same parent directory as ```tdc-starter-kit```. The datasets are available [here](https://zenodo.org/record/6894041). You can download them from the Zenodo website or by running ```download_datasets.py```.

The ```utils.py``` file contains helper functions for loading new models, generating new attack specifications, and training clean/Trojaned networks. This is primarily used for the Evasive Trojans Track starter kit. It also contains the load_data function for loading data sources (CIFAR-10/100, GTSRB, MNIST), which may be of general use. To load GTSRB images, unzip ```gtsrb_preprocessed.zip``` in the data folder (NOTE: This folder is only for storing data sources. The network datasets are stored in tdc_datasets, which must be downloaded from Zenodo). You may need to adjust the paths in the load_data function depending on your working directory. The ```wrn.py``` file contains the definition of the Wide Residual Network class used for CIFAR-10 and CIFAR-100 models. When loading networks from the competition datasets, ```wrn.py``` must be in your path. See the example submission notebooks for details.

### **Data**

Unlike standard machine learning tasks, the datasets consist of neural networks. That is, rather than making predictions on input images, goal will be identifying hidden functionality in neural networks. Networks are trained on four standard data sources: MNIST, CIFAR-10, CIFAR-100, and GTSRB. Variants of two standard Trojan attacks are used that are modified to be harder to detect. For the Detection Track, the training, validation, and test sets have 1,000 neural networks each. Networks are split evenly across all four data sources. Half of the networks are Trojaned, and there is a 50/50 split between the two attack types.

## How to Use

**Clone this repository, download the competition [datasets](https://huggingface.co/datasets/n1ghtf4l1/vigilant-fortnight/blob/main/tdc_datasets.zip) from my HuggingFace repository and unzip adjacent to the repository**. Ensure that Jupyter version is up-to-date (fairly recent). To avoid errors with model incompatibility, please use PyTorch version 1.11.0. Run one of the example notebooks or start building your own submission.

### **Additional Information**

#### **Model Architectures and Data Sources**

Networks have been trained on four standard data sources: MNIST, CIFAR-10, CIFAR-100, and GTSRB. GTSRB images are resized to 32x32.

For MNIST, convolutional networks have been used. For CIFAR-10 and CIFAR-100, Wide Residual Networks have been used. For GTSRB, Vision Transformers have been used.

#### **Trojan Attacks**

Trojaned networks have been trained with patch and whole-image attacks. These attacks are variants of the foundational BadNets and blended attacks modified to be harder to detect. These modified attacks use a simple change to the standard Trojan training procedure. Instead of training Trojaned networks from scratch, they were fine-tuned from the starting parameters of clean networks and regularize them with various similarity losses such that they are similar to the distribution of clean networks. Additionally, the networks have been trained to have high specificity for the particular trigger pattern associated with the attack. In extensive experiments, baseline detectors have been verified obtain substantially lower performance on these hard-to-detect Trojans.

All patch attacks in datasets use random trigger patterns sampled from an independent Bernoulli 0/1 distribution for each pixel and color channel (for Trojan detection and target label prediction, patches are black-and-white; for trigger synthesis, patches are colored). Each patch attack uses a different location and size for its trigger mask. All blended attacks in our datasets use random trigger trigger patterns sampled from an independent Uniform(0,1) distribution for each pixel and color channel. All attacks are all-to-one with a random target label. For more details, please see the starter kit. 

MNTD, Neural Cleanse, and ABS has been used as baseline Trojan detectors for participants to improve upon. These are well-known Trojan detectors from the academic literature, each with a distinct approach to Trojan detection. Also a specificity-based detector has been used as a baseline, since Trojan attacks with low specificity can be highly susceptible to such a detector. The specificity detector applies random triggers to inputs from a given data source, then runs these triggered inputs through the network in question. The negative entropy of the average posterior is used as a detection score. This leverages the fact that Trojan attacks without specificity are activated quite frequently by randomly sampled triggers.