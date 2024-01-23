---
annotations_creators:
- expert-generated
- found
language:
- en
- sl
language_creators:
- crowdsourced
license:
- cc-by-sa-4.0
multilinguality:
- translation
pretty_name: RSDO4 en-sl parallel corpus
size_categories:
- 100K<n<1M
source_datasets: []
tags:
- parallel data
- rsdo
task_categories:
- translation
- text2text-generation
- text-generation
task_ids: []
---

# Dataset Card for RSDO4 en-sl parallel corpus

### Dataset Summary

The RSDO4 parallel corpus of English-Slovene and Slovene-English translation pairs was collected as part of work package 4 of the Slovene in the Digital Environment project. It contains texts collected from public institutions and texts submitted by individual donors through the text collection portal created within the project. The corpus consists of 964433 translation pairs (extracted from standard translation formats (TMX, XLIFF) or manually aligned) in randomized order which can be used for machine translation training.

### Supported Tasks and Leaderboards

Machine translation. 

### Languages

English, Slovenian.

## Dataset Structure

### Data Instances

A sample instance from the dataset:
```
{
  'en_seq': 'the total value of its assets exceeds EUR 30000000000;', 
  'sl_seq': 'skupna vrednost njenih sredstev presega 30000000000 EUR'
}
```

### Data Fields

- `en_seq`: a string containing the English sequence; 
- `sl_seq`: a string containing the Slovene sequence.

## Additional Information

### Dataset Curators

Andraž Repar and Iztok Lebar Bajec. 

### Licensing Information

CC BY-SA 4.0.

### Citation Information

```
@misc{rsdo4_en_sl,
 title = {Parallel corpus {EN}-{SL} {RSDO4} 1.0},
 author = {Repar, Andra{\v z} and Lebar Bajec, Iztok},
 url = {http://hdl.handle.net/11356/1457},
 year = {2021}
}
```

### Contributions

Thanks to [@matejklemen](https://github.com/matejklemen) for adding this dataset.
