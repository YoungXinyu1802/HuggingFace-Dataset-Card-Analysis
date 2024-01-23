---
dataset_info:
  features:
  - name: path
    dtype: string
  - name: sentence
    dtype: string
  - name: duration
    dtype: float32
  - name: audio
    struct:
    - name: bytes
      dtype: binary
    - name: path
      dtype: string
  - name: sentence_processed
    dtype: string
  - name: taxonomy
    dtype: string
  - name: taxonomy_large
    dtype: string
  - name: ssml
    dtype: string
  - name: user
    dtype: string
  splits:
  - name: test
    num_bytes: 164031740
    num_examples: 1822
  - name: train
    num_bytes: 591461783
    num_examples: 6388
  download_size: 580490423
  dataset_size: 755493523
---
# jobs-skills_synth



## Dataset Description



### Dataset Summary

The data files can be found on the illuin gcloud instance at this adress: randstad-techlab-spellings/datasets/jobs-skills_synth 

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

``path`` ``sentence`` ``duration`` ``audio`` ``sentence_processed`` ``taxonomy`` ``taxonomy_large`` ``ssml`` ``user``

#### Sample

```
{   'audio': {   'bytes': "b'RIFF\\x84\\xcb\\x00\\x00WAVEfmt "
                          '\\x10\\x00\\x00\\x00\\x01\\x00\\x01\\x00\\xc0]\\x00\\x00\\x80\\xbb\\x00\\x00\\x02\\x00\\...',
                 'path': None},
    'duration': 1.6200000047683716,
    'path': '8c717ce6-80e6-4ce8-894a-a884ec6dbe10.wav',
    'sentence': 'inventoriste ',
    'sentence_processed': 'inventoriste',
    'ssml': '<speak> inventoriste </speak>',
    'taxonomy': 'job_skill',
    'taxonomy_large': 'job_skill',
    'user': 'fr-FR-Wavenet-E'}
```

### Data Splits

|split|number_of_rows|
|:---:|:---:
|test|1822|
|train|6388|

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
