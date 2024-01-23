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
- 10K<n<100K
source_datasets: []
task_categories:
- token-classification
task_ids: []
pretty_name: KOMET
tags:
- metaphor-classification
- metaphor-frame-classification
- multiword-expression-detection
---

# Dataset Card for KOMET

### Dataset Summary

KOMET 1.0 is a hand-annotated Slovenian corpus of metaphorical expressions which contains about 200 000 words (across 13 963 sentences) from Slovene journalistic, fiction and online texts. 

### Supported Tasks and Leaderboards

Metaphor detection, metaphor type classification, metaphor frame classification. 

### Languages

Slovenian.

## Dataset Structure

### Data Instances

A sample instance from the dataset:
```
{
  'document_name': 'komet49.div.xml', 
  'idx': 60, 
  'idx_paragraph': 24, 
  'idx_sentence': 1, 
  'sentence_words': ['Morda', 'zato', ',', 'ker', 'resnice', 'nočete', 'sprejeti', ',', 'in', 'nadaljujete', 'po', 'svoje', '.'], 
  'met_type': [{'type': 'MRWi', 'word_indices': [10]}], 
  'met_frame': [{'type': 'spatial_orientation', 'word_indices': [10]}, {'type': 'adverbial_phrase', 'word_indices': [10, 11]}]}
```

The sentence comes from the document `komet49.div.xml`, is the 60th sentence in the document and is the 1st sentence inside the 24th paragraph in the document.
The word "po" is annotated as an indirect metaphor-related word (`MRWi`).
The phrase "po svoje" is annotated with the frame "adverbial phrase" and the word "po" is additionally annotated with the frame "spatial_orientation".

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

The texts were sampled from the Corpus of Slovene youth literature MAKS (journalistic, fiction and online texts). 
Initially, words whose meaning deviates from their primary meaning in the Dictionary of the standard Slovene Language were marked as metaphors.
Then, their type was determined, i.e. whether they are an indirect (MRWi), direct (MRWd), borderline (WIDLI) metaphor or a metaphor flag (signal, marker; MFlag).

For more information, please check out the paper (which is in Slovenian language) or contact the dataset author

## Additional Information

### Dataset Curators

Špela Antloga.

### Licensing Information

CC BY-NC-SA 4.0

### Citation Information

```
@InProceedings{antloga2020komet,
  title = {Korpus metafor KOMET 1.0},
  author={Antloga, \v{S}pela},
  booktitle={Proceedings of the Conference on Language Technologies and Digital Humanities (Student abstracts)},
  year={2020},
  pages={167-170}
}
```

### Contributions

Thanks to [@matejklemen](https://github.com/matejklemen) for adding this dataset.
