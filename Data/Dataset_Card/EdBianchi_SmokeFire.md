---
dataset_info:
  features:
  - name: image
    dtype: image
  - name: label
    dtype:
      class_label:
        names:
          '0': Fire
          '1': Normal
          '2': Smoke
  splits:
  - name: train
    num_bytes: 166216842.46
    num_examples: 6060
  - name: test
    num_bytes: 89193578.0
    num_examples: 759
  - name: validation
    num_bytes: 75838884.0
    num_examples: 756
  download_size: 890673915
  dataset_size: 331249304.46000004
---
# Dataset Card for "SmokeFire"
Wildfires or forest fires are unpredictable catastrophic and destructive events that affect rural areas. The impact of these events affects both vegetation and wildlife.
This dataset can be used to train networks able to detect smoke and/or fire in forest environments.

## Data Sources & Description
- **This dataset consist of sample from two datasets hosted on Kaggle:**
  - [Forest Fire](https://www.kaggle.com/datasets/kutaykutlu/forest-fire?select=train_fire)
  - [Forest Fire Images](https://www.kaggle.com/datasets/mohnishsaiprasad/forest-fire-images)
- **The datasets consist of:**
  - 2525 **Fire** samples
  - 2525 **Smoke** samples
  - 2525 **Normal** samples
- **The dataset is splitted into:**
  - Train Set -> 6060 samples
  - Validation Set -> 756 samples
  - Test Set -> 759 samples
