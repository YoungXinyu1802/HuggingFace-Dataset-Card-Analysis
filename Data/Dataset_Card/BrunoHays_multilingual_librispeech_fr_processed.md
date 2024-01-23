# multilingual_librispeech_fr_processed



## Dataset Description



### Dataset Summary

The data files can be found on the illuin gcloud instance at this adress: unknown_url 

This dataset has been processed from Huggingface Hub dataset ``facebook/multilingual_librispeech`` and the config ``french``

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

``audio`` ``sentence`` ``path`` ``taxonomy`` ``taxonomy_large`` ``sentence_processed``

#### Sample

```
{   'audio': {   'array': array([ 2.7465820e-04,  3.3569336e-04,  2.1362305e-04, ...,
       -3.0517578e-05, -3.0517578e-05,  0.0000000e+00], dtype=float32),
                 'path': '/home/brunohays/.cache/huggingface/datasets/downloads/extracted/13f33c266be7d9e111d1bbccdadea34d95cb6456b778bf5e74ba71f49f3caa9a/8778_9061_000897.flac',
                 'sampling_rate': 16000},
    'path': '8778_9061_000897',
    'sentence': 'la carte fut place devant lady helena et chacun se plaa de faon suivre la dmonstration de paganel â ainsi que je vous '
                "l'ai dj appris dit le gographe apr s avoir travers l'amrique du sud le trente septi me degr de latitude rencontre les les "
                "tristan d'acunha",
    'sentence_processed': 'la carte fut place devant lady helena et chacun se plaa de faon suivre la dmonstration de paganel â ainsi que '
                          "je vous l'ai dj appris dit le gographe apr s avoir travers l'amrique du sud le trente septi me degr de latitude "
                          "rencontre les les tristan d'acunha",
    'taxonomy': 'librispeech',
    'taxonomy_large': 'librispeech'}
```

### Data Splits

|split|number_of_rows|
|:---:|:---:
|train|251463|
|test|2393|

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

