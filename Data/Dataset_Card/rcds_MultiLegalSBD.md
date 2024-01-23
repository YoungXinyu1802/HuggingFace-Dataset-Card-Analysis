---
dataset_info:
- config_name: fr_Laws
  features:
  - name: text
    dtype: string
  - name: spans
    list:
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: label
      dtype: string
    - name: token_start
      dtype: int64
    - name: token_end
      dtype: int64
  - name: tokens
    list:
    - name: text
      dtype: string
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: id
      dtype: int64
    - name: ws
      dtype: bool
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 8773683
    num_examples: 2131
  download_size: 0
  dataset_size: 8773683
- config_name: it_Laws
  features:
  - name: text
    dtype: string
  - name: spans
    list:
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: label
      dtype: string
    - name: token_start
      dtype: int64
    - name: token_end
      dtype: int64
  - name: tokens
    list:
    - name: text
      dtype: string
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: id
      dtype: int64
    - name: ws
      dtype: bool
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 8130577
    num_examples: 2910
  download_size: 0
  dataset_size: 8130577
- config_name: es_Laws
  features:
  - name: text
    dtype: string
  - name: spans
    list:
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: label
      dtype: string
    - name: token_start
      dtype: int64
    - name: token_end
      dtype: int64
  - name: tokens
    list:
    - name: text
      dtype: string
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: id
      dtype: int64
    - name: ws
      dtype: bool
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 6260211
    num_examples: 677
  download_size: 0
  dataset_size: 6260211
- config_name: en_Laws
  features:
  - name: text
    dtype: string
  - name: spans
    list:
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: label
      dtype: string
    - name: token_start
      dtype: int64
    - name: token_end
      dtype: int64
  - name: tokens
    list:
    - name: text
      dtype: string
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: id
      dtype: int64
    - name: ws
      dtype: bool
  - name: source
    dtype: string
  splits:
  - name: train
  download_size: 0
  dataset_size: 0
- config_name: de_Laws
  features:
  - name: text
    dtype: string
  - name: spans
    list:
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: label
      dtype: string
    - name: token_start
      dtype: int64
    - name: token_end
      dtype: int64
  - name: tokens
    list:
    - name: text
      dtype: string
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: id
      dtype: int64
    - name: ws
      dtype: bool
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 13792836
    num_examples: 13
  download_size: 0
  dataset_size: 13792836
- config_name: fr_Judgements
  features:
  - name: text
    dtype: string
  - name: spans
    list:
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: label
      dtype: string
    - name: token_start
      dtype: int64
    - name: token_end
      dtype: int64
  - name: tokens
    list:
    - name: text
      dtype: string
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: id
      dtype: int64
    - name: ws
      dtype: bool
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 8788244
    num_examples: 315
  download_size: 0
  dataset_size: 8788244
- config_name: fr_all
  features:
  - name: text
    dtype: string
  - name: spans
    list:
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: label
      dtype: string
    - name: token_start
      dtype: int64
    - name: token_end
      dtype: int64
  - name: tokens
    list:
    - name: text
      dtype: string
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: id
      dtype: int64
    - name: ws
      dtype: bool
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 25977816
    num_examples: 2446
  download_size: 4782672
  dataset_size: 25977816
- config_name: it_Judgements
  features:
  - name: text
    dtype: string
  - name: spans
    list:
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: label
      dtype: string
    - name: token_start
      dtype: int64
    - name: token_end
      dtype: int64
  - name: tokens
    list:
    - name: text
      dtype: string
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: id
      dtype: int64
    - name: ws
      dtype: bool
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 8989061
    num_examples: 243
  download_size: 0
  dataset_size: 8989061
- config_name: it_all
  features:
  - name: text
    dtype: string
  - name: spans
    list:
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: label
      dtype: string
    - name: token_start
      dtype: int64
    - name: token_end
      dtype: int64
  - name: tokens
    list:
    - name: text
      dtype: string
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: id
      dtype: int64
    - name: ws
      dtype: bool
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 25097560
    num_examples: 3153
  download_size: 4610540
  dataset_size: 25097560
- config_name: es_Judgements
  features:
  - name: text
    dtype: string
  - name: spans
    list:
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: label
      dtype: string
    - name: token_start
      dtype: int64
    - name: token_end
      dtype: int64
  - name: tokens
    list:
    - name: text
      dtype: string
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: id
      dtype: int64
    - name: ws
      dtype: bool
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 9460558
    num_examples: 190
  download_size: 0
  dataset_size: 9460558
- config_name: es_all
  features:
  - name: text
    dtype: string
  - name: spans
    list:
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: label
      dtype: string
    - name: token_start
      dtype: int64
    - name: token_end
      dtype: int64
  - name: tokens
    list:
    - name: text
      dtype: string
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: id
      dtype: int64
    - name: ws
      dtype: bool
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 23090629
    num_examples: 867
  download_size: 4438716
  dataset_size: 23090629
- config_name: en_Judgements
  features:
  - name: text
    dtype: string
  - name: spans
    list:
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: label
      dtype: string
    - name: token_start
      dtype: int64
    - name: token_end
      dtype: int64
  - name: tokens
    list:
    - name: text
      dtype: string
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: id
      dtype: int64
    - name: ws
      dtype: bool
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 18401754
    num_examples: 80
  download_size: 0
  dataset_size: 18401754
- config_name: en_all
  features:
  - name: text
    dtype: string
  - name: spans
    list:
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: label
      dtype: string
    - name: token_start
      dtype: int64
    - name: token_end
      dtype: int64
  - name: tokens
    list:
    - name: text
      dtype: string
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: id
      dtype: int64
    - name: ws
      dtype: bool
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 27363914
    num_examples: 80
  download_size: 5448700
  dataset_size: 27363914
- config_name: de_Judgements
  features:
  - name: text
    dtype: string
  - name: spans
    list:
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: label
      dtype: string
    - name: token_start
      dtype: int64
    - name: token_end
      dtype: int64
  - name: tokens
    list:
    - name: text
      dtype: string
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: id
      dtype: int64
    - name: ws
      dtype: bool
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 14082173
    num_examples: 131
  download_size: 0
  dataset_size: 14082173
- config_name: de_all
  features:
  - name: text
    dtype: string
  - name: spans
    list:
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: label
      dtype: string
    - name: token_start
      dtype: int64
    - name: token_end
      dtype: int64
  - name: tokens
    list:
    - name: text
      dtype: string
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: id
      dtype: int64
    - name: ws
      dtype: bool
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 40429185
    num_examples: 144
  download_size: 7883640
  dataset_size: 40429185
- config_name: fr_laws
  features:
  - name: text
    dtype: string
  - name: spans
    list:
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: label
      dtype: string
    - name: token_start
      dtype: int64
    - name: token_end
      dtype: int64
  - name: tokens
    list:
    - name: text
      dtype: string
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: id
      dtype: int64
    - name: ws
      dtype: bool
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 12924503
    num_examples: 2131
  download_size: 2201568
  dataset_size: 12924503
- config_name: fr_judgements
  features:
  - name: text
    dtype: string
  - name: spans
    list:
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: label
      dtype: string
    - name: token_start
      dtype: int64
    - name: token_end
      dtype: int64
  - name: tokens
    list:
    - name: text
      dtype: string
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: id
      dtype: int64
    - name: ws
      dtype: bool
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 13053313
    num_examples: 315
  download_size: 2581104
  dataset_size: 13053313
- config_name: it_laws
  features:
  - name: text
    dtype: string
  - name: spans
    list:
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: label
      dtype: string
    - name: token_start
      dtype: int64
    - name: token_end
      dtype: int64
  - name: tokens
    list:
    - name: text
      dtype: string
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: id
      dtype: int64
    - name: ws
      dtype: bool
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 11869343
    num_examples: 2910
  download_size: 2048828
  dataset_size: 11869343
- config_name: it_judgements
  features:
  - name: text
    dtype: string
  - name: spans
    list:
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: label
      dtype: string
    - name: token_start
      dtype: int64
    - name: token_end
      dtype: int64
  - name: tokens
    list:
    - name: text
      dtype: string
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: id
      dtype: int64
    - name: ws
      dtype: bool
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 13228218
    num_examples: 243
  download_size: 2561712
  dataset_size: 13228218
- config_name: es_laws
  features:
  - name: text
    dtype: string
  - name: spans
    list:
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: label
      dtype: string
    - name: token_start
      dtype: int64
    - name: token_end
      dtype: int64
  - name: tokens
    list:
    - name: text
      dtype: string
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: id
      dtype: int64
    - name: ws
      dtype: bool
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 9183057
    num_examples: 677
  download_size: 1753376
  dataset_size: 9183057
- config_name: es_judgements
  features:
  - name: text
    dtype: string
  - name: spans
    list:
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: label
      dtype: string
    - name: token_start
      dtype: int64
    - name: token_end
      dtype: int64
  - name: tokens
    list:
    - name: text
      dtype: string
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: id
      dtype: int64
    - name: ws
      dtype: bool
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 13907572
    num_examples: 190
  download_size: 2685340
  dataset_size: 13907572
- config_name: en_laws
  features:
  - name: text
    dtype: string
  - name: spans
    list:
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: label
      dtype: string
    - name: token_start
      dtype: int64
    - name: token_end
      dtype: int64
  - name: tokens
    list:
    - name: text
      dtype: string
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: id
      dtype: int64
    - name: ws
      dtype: bool
  - name: source
    dtype: string
  splits:
  - name: train
  download_size: 0
  dataset_size: 0
- config_name: en_judgements
  features:
  - name: text
    dtype: string
  - name: spans
    list:
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: label
      dtype: string
    - name: token_start
      dtype: int64
    - name: token_end
      dtype: int64
  - name: tokens
    list:
    - name: text
      dtype: string
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: id
      dtype: int64
    - name: ws
      dtype: bool
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 27363914
    num_examples: 80
  download_size: 5448700
  dataset_size: 27363914
- config_name: de_laws
  features:
  - name: text
    dtype: string
  - name: spans
    list:
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: label
      dtype: string
    - name: token_start
      dtype: int64
    - name: token_end
      dtype: int64
  - name: tokens
    list:
    - name: text
      dtype: string
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: id
      dtype: int64
    - name: ws
      dtype: bool
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 19935635
    num_examples: 13
  download_size: 3745480
  dataset_size: 19935635
- config_name: de_judgements
  features:
  - name: text
    dtype: string
  - name: spans
    list:
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: label
      dtype: string
    - name: token_start
      dtype: int64
    - name: token_end
      dtype: int64
  - name: tokens
    list:
    - name: text
      dtype: string
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: id
      dtype: int64
    - name: ws
      dtype: bool
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 20493550
    num_examples: 131
  download_size: 4138160
  dataset_size: 20493550
- config_name: pt_laws
  features:
  - name: text
    dtype: string
  - name: spans
    list:
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: label
      dtype: string
    - name: token_start
      dtype: int64
    - name: token_end
      dtype: int64
  - name: tokens
    list:
    - name: text
      dtype: string
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: id
      dtype: int64
    - name: ws
      dtype: bool
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 1005902
    num_examples: 58
  download_size: 209128
  dataset_size: 1005902
- config_name: pt_judgements
  features:
  - name: text
    dtype: string
  - name: spans
    list:
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: label
      dtype: string
    - name: token_start
      dtype: int64
    - name: token_end
      dtype: int64
  - name: tokens
    list:
    - name: text
      dtype: string
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: id
      dtype: int64
    - name: ws
      dtype: bool
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 812282
    num_examples: 10
  download_size: 173424
  dataset_size: 812282
- config_name: pt_all
  features:
  - name: text
    dtype: string
  - name: spans
    list:
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: label
      dtype: string
    - name: token_start
      dtype: int64
    - name: token_end
      dtype: int64
  - name: tokens
    list:
    - name: text
      dtype: string
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: id
      dtype: int64
    - name: ws
      dtype: bool
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 1818184
    num_examples: 68
  download_size: 382552
  dataset_size: 1818184
- config_name: all_laws
  features:
  - name: text
    dtype: string
  - name: spans
    list:
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: label
      dtype: string
    - name: token_start
      dtype: int64
    - name: token_end
      dtype: int64
  - name: tokens
    list:
    - name: text
      dtype: string
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: id
      dtype: int64
    - name: ws
      dtype: bool
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 54918438
    num_examples: 5789
  download_size: 9958380
  dataset_size: 54918438
- config_name: all_judgements
  features:
  - name: text
    dtype: string
  - name: spans
    list:
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: label
      dtype: string
    - name: token_start
      dtype: int64
    - name: token_end
      dtype: int64
  - name: tokens
    list:
    - name: text
      dtype: string
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: id
      dtype: int64
    - name: ws
      dtype: bool
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 88858845
    num_examples: 969
  download_size: 17588440
  dataset_size: 88858845
- config_name: all_all
  features:
  - name: text
    dtype: string
  - name: spans
    list:
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: label
      dtype: string
    - name: token_start
      dtype: int64
    - name: token_end
      dtype: int64
  - name: tokens
    list:
    - name: text
      dtype: string
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: id
      dtype: int64
    - name: ws
      dtype: bool
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 143777284
    num_examples: 6758
  download_size: 27546820
  dataset_size: 143777284
task_categories:
- token-classification
language:
- en
- es
- de
- it
- pt
- fr
pretty_name: 'MultiLegalSBD: A Multilingual Legal Sentence Boundary Detection Dataset'
size_categories:
- 100K<n<1M
---

# Dataset Card for Dataset Name

## Dataset Description

- **Homepage:**
- **Repository:**
- **Paper:**
- **Leaderboard:**
- **Point of Contact:**

### Dataset Summary

This is a multilingual dataset containing ~130k annotated sentence boundaries. It contains laws and court decision in 6 different languages.

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

English, French, Italian, German, Portuguese, Spanish

## Dataset Structure

It is structured in the following format: {language}\_{type}\_{shard}.jsonl.xz

type is one of the following:
- laws
- judgements

Use the the dataset like this:
```
from datasets import load_dataset
config = 'fr_laws' #{language}_{type} | to load all languages and/or all types, use 'all_all'
dataset = load_dataset('rdcs/MultiLegalSBD', config)
```

### Data Instances

[More Information Needed]

### Data Fields

- text: the original text
- spans:
  - start: offset of the first character
  - end: offset of the last character
  - label: One label only -> Sentence
  - token_start: id of the first token
  - token_end: id of the last token
- tokens:
  - text: token text
  - start: offset of the first character
  - end: offset of the last character
  - id: token id
  - ws: whether the token is followed by whitespace
  

### Data Splits

There is only one split available

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