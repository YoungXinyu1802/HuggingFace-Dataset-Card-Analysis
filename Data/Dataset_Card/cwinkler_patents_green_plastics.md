---
dataset_info:
  features:
  - name: abstract
    dtype: string
  - name: label
    dtype: int64
  splits:
  - name: train
    num_bytes: 8088461
    num_examples: 11196
  download_size: 4025753
  dataset_size: 8088461
language:
- en
size_categories:
- 10K<n<100K
---
# Dataset Card for "Patents_Green_Plastics"

    number of rows: 11.196
    features: [title, label]
    label: 0, 1

The dataset contains patent abstracts that are labeled as 1 (="Green Plastics") and 0 (="Not Green Plastics").

# Dataset Creation

The [BIGPATENT](https://huggingface.co/datasets/big_patent) dataset is the source for this dataset.

In a first step, abstracts of BIGPATENT were filtered by the terms "plastics" and "polymer". The resulting "Plastics" dataset contained 64.372 samples.

In a second step, the 64.372 samples were filtered by terms which define "green plastics". 

"Green Plastics" are defined by the list of terms: 
"degrada", "recycl", "bio", "compost", "bact", "waste recovery", "zero waste", "sustainab", "Bio-Based", "Bio-Degradable", "Renewable", "Green Plastics", "Renewable",  "Degradable", "Compostable", "Bio-resorbable", "Bio-soluble", "Cellulose", "Biodegradable","Mycelium", "Recyclability", "Degradability", "Bio-Polymer", "reuse", "reusable",  "reusing", "Degradation", "Multiple Use", "Bioplastic", "Polyhydroxyalkanoates", "PHA", "Polylactide", "PLA", "Polyglycolide", "PGA"
(some terms might repeat)

The group of "Green Plastics" containing 5.598 rows was labeled as 1. 

An equal amount of samples (=5.598 rows) was randomly chosen from the "Plastics" dataset, defined as "Not Green Plastics" and labeled as 0. 

Both groups ("Green Plastics" and "Not Green Plastics") were merged together.