---
license: mit
language:
- en
size_categories:
- 10M<n<100M
task_categories:
- text-generation
- fill-mask
tags:
- language modeling
- masked language modeling
- pretraining
- pile
- DSIR
---
# Dataset Card for DSIR-filtered-pile-50M

## Dataset Description

- **Repository:** https://github.com/p-lambda/dsir
- **Paper:** https://arxiv.org/abs/2302.03169
- **Point of Contact: Sang Michael Xie <xie@cs.stanford.edu>** 

### Dataset Summary

This dataset is a subset of The Pile, selected via the DSIR data selection method. The target distribution for DSIR is the Wikipedia and BookCorpus2 subsets of The Pile.


### Languages

English (EN)

## Dataset Structure

A train set is provided (51M examples) with a small validation and test set (50k examples each).

### Data Instances

```
{"contents": "Hundreds of soul music enthusiasts from the United Kingdom plan to make their way to Detroit this month for a series of concerts.\n\nDetroit A-Go-Go, a festival organized by DJ Phil Dick, will take place Oct. 19-22 with 26 scheduled acts.\n\nThe festival is focused on what Dick calls the northern soul movement.\n\n\"We just love Detroit soul and Motown music,\" Dick said. \"It's been popular in England for decades. Every weekend, thousands of people go out and listen to this music in England.\"\n\nArtists booked for the festival include: The Elgins, Pat Lewis, Melvin Davis, The Velvelettes, The Contours, Kim Weston, Ronnie McNeir, The Capitols, Yvonne Vernee, JJ Barnes, Gino Washington, Spyder Turner, The Adorables, Lorraine Chandler, Eddie Parker, Dusty Wilson, The Precisions, The Professionals, The Tomangoes, The Fabulous Peps andNow that\u2019s a punishment: club vice president sent to train with the reserves!\n\nFor almost an entire year, Gabriel Bostina has been playing a double role for Universitatea Cluj. Unfortunately for him, the position acquired in the club\u2019s board didn\u2019t earn him any favors from the technical staff, who recently punished the central midfielder. Twice. First of all, Bostina lost the armband during one of the training camps from Antalya for some unknown disciplinary problems and now the player & vice president has suffered further embarrassment being sent to train with the reservers \u201cfor an unlimited period\u201d.\n\nCurrently injured, he failed to show up for the weekend training sessions that were going to be supervised by the club\u2019s medical staff, so the former Otelul, Steaua and Dinamo man is now", "metadata": {"pile_set_name": ["OpenWebText2", "Pile-CC"]}, "id": 423}
```

### Data Fields

```
"contents": the text
"metadata": contains information about the source(s) of text that the text comes from. Multiple sources means that the example is concatenated from two sources.
"id": Ignore - a non-unique identifier
```

## Dataset Creation
We first select 102.4M examples then concatenate every two examples to create 51.2M examples.
This ensures that the examples are long enough for a max token length of 512 without much padding.
We train the importance weight estimator for DSIR from The Pile validation set, where the target is Wikipedia + BookCorpus2 + Gutenberg + Books3 and the raw data come from the rest of the data sources in The Pile.
We first select 98.4M examples from non-Wikipedia and book data, then randomly select 2M from Wikipedia and 0.66M each from BookCorpus2, Gutenberg, and Books3. 
After this, we concatenate every two examples.

### Source Data
The Pile

#### Initial Data Collection and Normalization
We select data from The Pile, which comes in 30 random chunks. We reserve chunk 0 for validation purposes and only consider the last 29 chunks.
We first divided the documents in The Pile into chunks of 128 words, according to whitespace tokenization.
These chunks define the examples that we do data selection on, totaling 1.7B examples.
Before DSIR, we first apply a manual quality filter (see paper for details) and only consider the examples that pass the filter.


## Considerations for Using the Data

The dataset is biased towards choosing data from non-Wikipedia and non-Books sources. A balanced approach would be to mix in more data from Wikipedia and books.

### Dataset Curators

Sang Michael Xie, Shibani Santurkar

### Citation Information
Paper: <https://arxiv.org/abs/2302.03169>
```
@article{xie2023data,
  author = {Sang Michael Xie and Shibani Santurkar and Tengyu Ma and Percy Liang},
  journal = {arXiv preprint arXiv:2302.03169},
  title = {Data Selection for Language Models via Importance Resampling},
  year = {2023},
}
```