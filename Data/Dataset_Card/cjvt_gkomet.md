---
annotations_creators:
- expert-generated
language_creators:
- found
language:
- sl
license:
- cc-by-nc-sa-4.0
multilinguality:
- monolingual
size_categories:
- 1K<n<10K
source_datasets: []
task_categories:
- token-classification
task_ids: []
pretty_name: G-KOMET
tags:
- metaphor-classification
- metonymy-classification
- metaphor-frame-classification
- multiword-expression-detection
---

# Dataset Card for G-KOMET

### Dataset Summary

G-KOMET 1.0 is a corpus of metaphorical expressions in spoken Slovene language, covering around 50,000 lexical units across 5695 sentences. The corpus contains samples from the Gos corpus of spoken Slovene and includes a balanced set of transcriptions of informative, educational, entertaining, private, and public discourse.

It is also annotated with idioms and metonymies. Note that these are both annotated as metaphor types. This is different from the annotations in [KOMET](https://huggingface.co/datasets/cjvt/komet), where these are both considered a type of frame. We keep the data as untouched as possible and let the user decide how they want to handle this. 


### Supported Tasks and Leaderboards

Metaphor detection, metonymy detection, metaphor type classification, metaphor frame classification. 

### Languages

Slovenian.

## Dataset Structure

### Data Instances

A sample instance from the dataset:
```
{
  'document_name': 'G-Komet001.xml', 
  'idx': 3, 
  'idx_paragraph': 0, 
  'idx_sentence': 3, 
  'sentence_words': ['no', 'zdaj', 'samo', 'še', 'za', 'eno', 'orientacijo'], 
  'met_type': [
    {'type': 'MRWi', 'word_indices': [6]}
  ], 
  'met_frame': [
    {'type': 'spatial_orientation', 'word_indices': [6]}
  ]
}
```

The sentence comes from the document `G-Komet001.xml`, is the 3rd sentence in the document and is the 3rd sentence inside the 0th paragraph in the document.
The word "orientacijo" is annotated as an indirect metaphor-related word (`MRWi`).
It is also annotated with the frame "spatial_orientation".

### Data Fields

- `document_name`: a string containing the name of the document in which the sentence appears; 
- `idx`: a uint32 containing the index of the sentence inside its document; 
- `idx_paragraph`: a uint32 containing the index of the paragraph in which the sentence appears;
- `idx_sentence`: a uint32 containing the index of the sentence inside its paragraph;
containing the consecutive number of the paragraph inside the current news article;
- `sentence_words`: words in the sentence;
- `met_type`: metaphors in the sentence, marked by their type and word indices;
- `met_frame`: metaphor frames in the sentence, marked by their type (frame name) and word indices.

## Dataset Creation

The corpus contains samples from the GOS corpus of spoken Slovene and includes a balanced set of transcriptions of informative, educational, entertaining, private, and public discourse. It contains hand-annotated metaphor-related words, i.e. linguistic expressions that have the potential for people to interpret them as metaphors, idioms, i.e. multi-word units in which at least one word has been used metaphorically, and metonymies, expressions that we use to express something else.

For more information, please check out the paper (which is in Slovenian language) or contact the dataset author.

## Additional Information

### Dataset Curators

Špela Antloga.

### Licensing Information

CC BY-NC-SA 4.0

### Citation Information

```
@InProceedings{antloga2022gkomet,
title = {Korpusni pristopi za identifikacijo metafore in metonimije: primer metonimije v korpusu gKOMET},
author={Antloga, \v{S}pela},
booktitle={Proceedings of the Conference on Language Technologies and Digital Humanities (Student papers)},
year={2022},
pages={271-277}
}
```

### Contributions

Thanks to [@matejklemen](https://github.com/matejklemen) for adding this dataset.
