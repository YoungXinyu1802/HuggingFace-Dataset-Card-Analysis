---
license: cc-by-4.0
---
---
# For reference on model card metadata, see the spec: https://github.com/huggingface/hub-docs/blob/main/datasetcard.md?plain=1
# Doc / guide: https://huggingface.co/docs/hub/datasets-cards
{}
---

# Dataset Card for Dataset Name

## Dataset Description

- **Homepage:**
- https://github.com/AARSynth/Dataset
- **Repository:**
- https://github.com/AARSynth/Dataset
- **Paper:**
- App-Aware Response Synthesis for User Reviews.
  Umar Farooq, A.B. Siddique, Fuad Jamour, Zahijia Zhao and Vagelis Hristidis, “App-Aware Response Synthesis for User Reviews,” 2020 IEEE International Conference on Big Data (Big Data), 2020, pp. 699-708, DOI: https://doi.org/10.1109/BigData50022.2020.9377983.
- **Point of Contact:**
- Umar Farooq (ufarooq.cs@gmail.com)
- Abubakar Siddique (abubakar.ucr@gmail.com)

### Dataset Summary

AARSynth is a large-scale app review dataset. There are 570K review-response pairs and more than 2 million user
reviews for 103 popular applications. 


### Supported Tasks and Leaderboards

Question Answer
Response Generation

### Languages
English

## How to use the dataset?
```
from datasets import load_dataset
import pandas as pd

# load the dataset 
mbr_data = load_dataset('recmeapp/AARSynth', data_dir='replies')

# Save dataset to .csv file for creating pandas dataframe
mbr_data['train'].to_csv('./mbr_data.csv', sep='***') 

# Convert to pandas dataframe
aarsynth_df = pd.read_csv('./mbr_data.csv', sep='***')

# How many interactions are there in the AARSynth dataset?
print(f'There are {len(aarsynth_df)} interactions in AARSynth dataset.')

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

Umar Farooq and A.B. Siddique

### Licensing Information

[More Information Needed]

### Citation Information

- App-Aware Response Synthesis for User Reviews.
  Umar Farooq, A.B. Siddique, Fuad Jamour, Zahijia Zhao and Vagelis Hristidis, “App-Aware Response Synthesis for User Reviews,” 2020 IEEE International Conference on Big Data (Big Data), 2020, pp. 699-708, DOI: https://doi.org/10.1109/BigData50022.2020.9377983.

### Contributions

[More Information Needed]