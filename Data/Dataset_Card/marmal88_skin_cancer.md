---
dataset_info:
  features:
  - name: image
    dtype: image
  - name: image_id
    dtype: string
  - name: lesion_id
    dtype: string
  - name: dx
    dtype: string
  - name: dx_type
    dtype: string
  - name: age
    dtype: float64
  - name: sex
    dtype: string
  - name: localization
    dtype: string
  splits:
  - name: train
    num_bytes: 2490501038.358
    num_examples: 9577
  - name: test
    num_bytes: 351507473.24
    num_examples: 1285
  - name: validation
    num_bytes: 681758880.144
    num_examples: 2492
  download_size: 3693626934
  dataset_size: 3523767391.7419996
task_categories:
- image-classification
- image-segmentation
language:
- en
tags:
- skin_cancer
- HAM10000
pretty_name: HAM10000
size_categories:
- 1K<n<10K
---
# The HAM10000 dataset, a large collection of multi-source dermatoscopic images of common pigmented skin lesions

- Original Paper and Dataset [here](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/DBW86T)
- Kaggle dataset [here](https://www.kaggle.com/datasets/kmader/skin-cancer-mnist-ham10000?resource=download)

# Introduction to datasets
Training of neural networks for automated diagnosis of pigmented skin lesions is hampered by the small size and lack of diversity of available dataset of dermatoscopic images. We tackle this problem by releasing the HAM10000 ("Human Against Machine with 10000 training images") dataset. We collected dermatoscopic images from different populations, acquired and stored by different modalities. The final dataset consists of 10015 dermatoscopic images which can serve as a training set for academic machine learning purposes. Cases include a representative collection of all important diagnostic categories in the realm of pigmented lesions: Actinic keratoses and intraepithelial carcinoma / Bowen's disease (akiec), basal cell carcinoma (bcc), benign keratosis-like lesions (solar lentigines / seborrheic keratoses and lichen-planus like keratoses, bkl), dermatofibroma (df), melanoma (mel), melanocytic nevi (nv) and vascular lesions (angiomas, angiokeratomas, pyogenic granulomas and hemorrhage, vasc).

More than 50% of lesions are confirmed through histopathology (histo), the ground truth for the rest of the cases is either follow-up examination (follow_up), expert consensus (consensus), or confirmation by in-vivo confocal microscopy (confocal). 

The test set is not public, but the evaluation server remains running (see the challenge website). Any publications written using the HAM10000 data should be evaluated on the official test set hosted there, so that methods can be fairly compared.

- Test site can be accessed [here](https://challenge.isic-archive.com/landing/2018/)

# Disclaimer and additional information
This is a contribution to open sourced data in hugging face for image data. Images can be obtained from above links. 

Train test split was done using a stratified splitting by cancer/diagnosis type. The code to stratify the dataset can be obtained on my github [here](https://github.com/marmal88/skin_cancer).

I do not own any rights to above images.

[More Information needed](https://github.com/huggingface/datasets/blob/main/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)