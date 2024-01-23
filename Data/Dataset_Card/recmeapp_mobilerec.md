---
# For reference on model card metadata, see the spec: https://github.com/huggingface/hub-docs/blob/main/datasetcard.md?plain=1
# Doc / guide: https://huggingface.co/docs/hub/datasets-cards
{}
---

# Dataset Card for Dataset Name

## Dataset Description

- **Homepage:**
- https://github.com/mhmaqbool/mobilerec
- **Repository:**
- https://github.com/mhmaqbool/mobilerec
- **Paper:**
- MobileRec: A Large-Scale Dataset for Mobile Apps Recommendation
- **Point of Contact:**
- M.H. Maqbool (hasan.khowaja@gmail.com)
- Abubakar Siddique (abubakar.ucr@gmail.com)

### Dataset Summary

MobileRec is a large-scale app recommendation dataset. There are 19.3 million user\item interactions. This is a 5-core dataset. 
User\item interactions are sorted in ascending chronological order. There are 0.7 million users who have had at least five distinct interactions.
There are 10173 apps in total.

### Supported Tasks and Leaderboards

Sequential Recommendation

### Languages
English

## How to use the dataset?
```
from datasets import load_dataset
import pandas as pd

# load the dataset and meta_data 
mbr_data = load_dataset('recmeapp/mobilerec', data_dir='interactions')
mbr_meta = load_dataset('recmeapp/mobilerec', data_dir='app_meta')

# Save dataset to .csv file for creating pandas dataframe
mbr_data['train'].to_csv('./mbr_data.csv') 

# Convert to pandas dataframe
mobilerec_df = pd.read_csv('./mbr_data.csv')

# How many interactions are there in the MobileRec dataset?
print(f'There are {len(mobilerec_df)} interactions in mobilerec dataset.')

# How many unique app_packages (apps or items) are there?
print(f'There are {len(mobilerec_df["app_package"].unique())} unique apps in mobilerec dataset.')

# How many unique users are there in the mobilerec dataset?
print(f'There are {len(mobilerec_df["uid"].unique())} unique users in mobilerec dataset.')

# How many categoris are there?
print(f'There are {len(mobilerec_df["app_category"].unique())} unique categories in mobilerec dataset.')
```

[More Information Needed]

## Dataset Structure

### Data Instances

[More Information Needed]

### Data Fields

[More Information Needed]

### Data Splits

[More Information Needed]

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

[More Information Needed]

### Licensing Information

[More Information Needed]

### Citation Information

[More Information Needed]

### Contributions

[More Information Needed]