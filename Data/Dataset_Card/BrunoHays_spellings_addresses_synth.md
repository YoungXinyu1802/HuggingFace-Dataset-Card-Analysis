---
dataset_info:
  features:
  - name: path
    dtype: string
  - name: sentence
    dtype: string
  - name: user
    dtype: string
  - name: entity
    dtype: string
  - name: taxonomy
    dtype: string
  - name: audio
    dtype:
      audio:
        sampling_rate: 16000
  - name: sentence_processed
    dtype: string
  - name: taxonomy_large
    dtype: string
  - name: sentence_gold
    dtype: string
  - name: ssml
    dtype: string
  splits:
  - name: test
    num_bytes: 65424240.0
    num_examples: 183
  - name: train
    num_bytes: 222858789.0
    num_examples: 646
  download_size: 234350603
  dataset_size: 288283029.0
---
# spellings_addresses_synth



## Dataset Description



### Dataset Summary

The data files can be found on the illuin gcloud instance at this adress: randstad-techlab-spellings/datasets/spellings_addresses_synth 

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

[More Information Needed]

## Dataset Structure



### Data Instances

[More Information Needed]

### Data Fields

[More Information Needed]

#### Columns

``path`` ``sentence`` ``user`` ``entity`` ``taxonomy`` ``audio`` ``sentence_processed`` ``taxonomy_large`` ``sentence_gold`` ``ssml``

#### Sample

```
{   'audio': {   'array': array([0.0000000e+00, 0.0000000e+00, 0.0000000e+00, ..., 2.5915553e-05,
       3.5547255e-05, 0.0000000e+00], dtype=float32),
                 'path': 'clips_synth/0ca75c9c-f39d-46ff-8d26-a655786580b2.wav',
                 'sampling_rate': 16000},
    'entity': '30 Rue de la Ravinelle 54000 Nancy',
    'path': '0ca75c9c-f39d-46ff-8d26-a655786580b2.wav',
    'sentence': '30 rue de la ravinelle R A V I N E 2 L E 64000 nancy N A N C Y',
    'sentence_gold': '30 rue de la RAVINELLE 64000 NANCY',
    'sentence_processed': 'trente rue de la ravinelle R A V I N E deux L E soixante-quatre mille nancy N A N C Y ',
    'ssml': "<speak> <break strength='weak'/> trente rue de la ravinelle <break strength='weak'/> R A V I N E <br...",
    'taxonomy': 'address',
    'taxonomy_large': 'address',
    'user': 'fr-FR-Wavenet-C'}
```

### Data Splits

|split|number_of_rows|
|:---:|:---:
|test|183|
|train|646|

## Dataset Creation



### Curation Rationale

[More Information Needed]

### Source Data

[More Information Needed]

### Annotations

[More Information Needed]

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the dataset



### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information



### Dataset Curators

[More Information Needed]

### Licensing Information

Property of Illuin Technology

### Contributions

This dataset has been pushed using the repo [illuin-hf-dataset-pusher](https://gitlab.illuin.tech/data-science/ml/libraries/illuin-hf-dataset-pusher) 
