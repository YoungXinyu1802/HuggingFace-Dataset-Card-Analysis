---
language:
- en
license:
- cc-by-nc-4.0
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- text-classification
task_ids:
- sentiment-classification
dataset_info:
  features:
  - name: text
    dtype: string
  - name: inputs
    struct:
    - name: text
      dtype: string
  - name: prediction
    list:
    - name: label
      dtype: string
    - name: score
      dtype: float64
  - name: prediction_agent
    dtype: string
  - name: annotation
    dtype: 'null'
  - name: annotation_agent
    dtype: 'null'
  - name: multi_label
    dtype: bool
  - name: explanation
    dtype: 'null'
  - name: id
    dtype: string
  - name: metadata
    dtype: 'null'
  - name: status
    dtype: string
  - name: event_timestamp
    dtype: timestamp[us]
  - name: metrics
    struct:
    - name: text_length
      dtype: int64
  splits:
  - name: train
    num_bytes: 31840239
    num_examples: 20491
  download_size: 19678149
  dataset_size: 31840239
---
# Dataset Card for "tripadvisor-hotel-reviews"
## Dataset Description
- **Homepage:** Kaggle Challenge
- **Repository:** https://www.kaggle.com/datasets/andrewmvd/trip-advisor-hotel-reviews
- **Paper:** https://zenodo.org/record/1219899
- **Leaderboard:** N.A.
- **Point of Contact:** N.A.
### Dataset Summary
Hotels play a crucial role in traveling and with the increased access to information new pathways of selecting the best ones emerged.
With this dataset, consisting of 20k reviews crawled from Tripadvisor, you can explore what makes a great hotel and maybe even use this model in your travels!
Citations on a scale from 1 to 5.
### Languages
english 
### Citation Information
If you use this dataset in your research, please credit the authors.
Citation
Alam, M. H., Ryu, W.-J., Lee, S., 2016. Joint multi-grain topic sentiment: modeling semantic aspects for online reviews. Information Sciences 339, 206–223.
DOI
License
CC BY NC 4.0
Splash banner
### Contributions
Thanks to [@davidberenstein1957](https://github.com/davidberenstein1957) for adding this dataset.