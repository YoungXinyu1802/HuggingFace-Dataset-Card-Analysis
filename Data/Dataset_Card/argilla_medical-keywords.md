---
language:
- en
size_categories:
- 100K<n<1M
source_datasets:
- original
task_categories:
- token-classification
task_ids:
- keyphrase-extraction
- named-entity-recognition
dataset_info:
  features:
  - name: text
    dtype: string
  - name: tokens
    sequence: string
  - name: prediction
    list:
    - name: end
      dtype: int64
    - name: label
      dtype: string
    - name: score
      dtype: float64
    - name: start
      dtype: int64
  - name: prediction_agent
    dtype: string
  - name: annotation
    dtype: 'null'
  - name: annotation_agent
    dtype: 'null'
  - name: id
    dtype: 'null'
  - name: metadata
    struct:
    - name: medical_specialty
      dtype: string
  - name: status
    dtype: string
  - name: event_timestamp
    dtype: timestamp[us]
  - name: metrics
    dtype: 'null'
  splits:
  - name: train
    num_bytes: 58986555
    num_examples: 148699
  download_size: 17498377
  dataset_size: 58986555
---
# Dataset Card for "medical-keywords"

## Dataset Description

- **Homepage:** Kaggle Challenge
- **Repository:** https://www.kaggle.com/datasets/tboyle10/medicaltranscriptions
- **Paper:** N.A.
- **Leaderboard:** N.A.
- **Point of Contact:** N.A.

### Dataset Summary

Medical transcription data scraped from mtsamples.com
Medical data is extremely hard to find due to HIPAA privacy regulations. This dataset offers a solution by providing medical transcription samples.
This dataset contains sample medical transcriptions for various medical specialties.

### Languages

english 

### Citation Information

Acknowledgements

Medical transcription data scraped from mtsamples.com

### Contributions

Thanks to [@davidberenstein1957](https://github.com/davidberenstein1957) for adding this dataset.