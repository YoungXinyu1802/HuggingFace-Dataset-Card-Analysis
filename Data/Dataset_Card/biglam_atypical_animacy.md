---
annotations_creators:
- expert-generated
language:
- en
language_creators:
- machine-generated
license:
- cc0-1.0
multilinguality:
- monolingual
paperswithcode_id: null
pretty_name: Atypical Animacy
size_categories:
- n<1K
source_datasets:
- original
task_categories:
- text-classification
task_ids:
- sentiment-classification
- intent-classification
---
# Dataset Card for atypical_animacy

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-instances)
  - [Data Splits](#data-instances)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)

## Dataset Description

- **Homepage:** https://bl.iro.bl.uk/concern/datasets/323177af-6081-4e93-8aaf-7932ca4a390a?locale=en
- **Repository:** https://github.com/Living-with-machines/AtypicalAnimacy
- **Paper:** https://arxiv.org/abs/2005.11140
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [Mariona Coll Ardanuy](mailto:mcollardanuy@turing.ac.uk), [Daniel CS Wilson](mailto:dwilson@turing.ac.uk)

### Dataset Summary

Atypical animacy detection dataset, based on nineteenth-century sentences in English extracted from an open dataset of nineteenth-century books digitized by the British Library. This dataset contains 598 sentences containing mentions of machines. Each sentence has been annotated according to the animacy and humanness of the machine in the sentence. 

### Supported Tasks and Leaderboards

- `text-classification` - This dataset can be used to determine if a mention of an entity in a document was humanlike or not
- `entity-recognition` - The dataset can be used to fine tune large models for NER, albeit for a very specific use case

### Languages

The text in the dataset is in English, as written by authors of books digitized by the British Library. The associated BCP-47 code in `en`

## Dataset Structure

The dataset has a single configuration

### Data Instances

An example data point

```
{'id': '002757962_01_184_16', 
'sentence': '100 shows a Cornish boiler improperly seated with one small side flue and a bottom flue.', 
'context': 'Fig.  100 shows a Cornish boiler improperly seated with one small side flue and a bottom flue.  The effect of this on a long boiler is to cause springing and leakage of the seams from the heat being applied to one side of the boiler only.', 
'target': 'boiler', 
'animacy': 0.0, 
'humanness': 1.0, 
'offsets': [20, 26], 
'date': '1893'}
```

### Data Fields

- id: sentence identifier according to internal Living with Machines BL books indexing.
- sentence: sentence where target expression occurs.
- context: sentence where target expression occurs, plus one sentence to the left and one sentence to the right.
- target: target expression
- animacy: animacy of the target expression
- humanness: humanness of the target expression


### Data Splits

Train | 598

## Dataset Creation

The dataset was created by manually annotating books that had been digitized by the British Library. According to the paper's authors, 
> "we provide a basis for examining how machines were imagined during the nineteenth century as everything from lifeless mechanical objects to living beings, or even human-like agents that feel, think, and love. We focus on texts from nineteenth-century Britain, a society being transformed by industrialization, as a good candidate for studying the broader issue"

### Curation Rationale

From the paper: 
> The Stories dataset is largely composed of target expressions that correspond to either typically animate or typically inanimate entities. Even though some cases of unconventional animacy can be found(folktales, in particular, are richer in typically inanimate entities that become animate), these accountfor a very small proportion of the data.6 We decided to create our own dataset (henceforth 19thC Machines dataset) to gain a better sense of the suitability of our method to the problem of atypical animacy detection, with particular attention to the case of animacy of machines in nineteenth-century texts.

### Source Data

#### Initial Data Collection and Normalization

The dataset was generated by manually annotating books that have been digitized by the British Library

#### Who are the source language producers?

The data was originally produced by British authors in the 19th century. The books were then digitzed whcih produces some noise due to the OCR method. The annotators are from The Alan Turing Institute, The British Library, University of Cambridge, University of Exeter and Queen Mary University of London

### Annotations

#### Annotation process
Annotation was carried out in two parts. 
For the intial annotation process, from the paper:
> "For human annotators, even history and literature experts, language subtleties made this task extremely subjective. In the first task, we masked the target word (i.e. the machine) in each sentence and asked the annotator to fill the slot with the most likely entity between ‘human’, ‘horse’, and ‘machine’, representing three levels in the animacy hierarchy: human, animal, and object (Comrie, 1989, 185). We asked annotators to stick to the most literal meaning and avoid metaphorical interpretations when possible. The second task was more straightforwardly related to determining the animacy of the target entity, given the same 100 sentences. We asked annotators to provide a score between -2 and 2, with -2 being definitely inanimate, -1 possibly inanimate, 1 possibly animate, and 2 definitely animate. Neutral judgements were not allowed. "

For the final annotations, from the paper:
> A subgroup of five annotators collaboratively wrote the guidelines based on their experience annotating the first batch of sentences, taking into account common discrepancies. After discussion, it was decided that a machine would be tagged as animate if it is described as having traits distinctive of biologically animate beings or human-specific skills, or portrayed as having feelings, emotions, or a soul. Sentences like the ones in example 2 would be considered animate, but an additional annotation layer would be provided to capture the notion of humanness, which would be true if the machine is portrayed as sentient and capable of specifically human emotions, and false if it used to suggest some degree of dehumanization.

#### Who are the annotators?
 Annotations were carried out by the following people 
- Giorgia Tolfo
- Ruth Ahnert
- Kaspar Beelen
- Mariona Coll Ardanuy
- Jon Lawrence
- Katherine McDonough
- Federico Nanni
- Daniel CS Wilson

### Personal and Sensitive Information

This dataset does not have any personal information since they are digitizations of books from the 19th century. Some passages might be sensitive, but it is not explicitly mentioned in the paper.

## Considerations for Using the Data

### Social Impact of Dataset

[Needs More Information]

### Discussion of Biases

[Needs More Information]

### Other Known Limitations

[Needs More Information]

## Additional Information

### Dataset Curators

The curators for this dataset are:
- Kaspar Beelen
- Mariona Coll Ardanuy
- Federico Nanni
- Giorgia Tolfo


### Licensing Information
CC0 1.0 Universal Public Domain

### Citation Information

```
@article{DBLP:journals/corr/abs-2005-11140,
  author    = {Mariona Coll Ardanuy and
               Federico Nanni and
               Kaspar Beelen and
               Kasra Hosseini and
               Ruth Ahnert and
               Jon Lawrence and
               Katherine McDonough and
               Giorgia Tolfo and
               Daniel C. S. Wilson and
               Barbara McGillivray},
  title     = {Living Machines: {A} study of atypical animacy},
  journal   = {CoRR},
  volume    = {abs/2005.11140},
  year      = {2020},
  url       = {https://arxiv.org/abs/2005.11140},
  eprinttype = {arXiv},
  eprint    = {2005.11140},
  timestamp = {Sat, 23 Jan 2021 01:12:25 +0100},
  biburl    = {https://dblp.org/rec/journals/corr/abs-2005-11140.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```