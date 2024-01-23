---
license:
- cc
multilinguality:
- other-music
pretty_name: Mutopia Guitar Dataset
task_categories:
- text-generation
task_ids:
- language-modeling
---

# Mutopia Guitar Dataset

## Table of Contents
- [Dataset Card Creation Guide](#mutopia-guitar-dataset)
  - [Table of Contents](#table-of-contents)
  - [Dataset Description](#dataset-description)
    - [Dataset Summary](#dataset-summary)
    - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Dataset Structure](#dataset-structure)
    - [Data Instances](#data-instances)
    - [Data Fields](#data-fields)
    - [Data Splits](#data-splits)

## Dataset Description

- **Homepage:** [Mutopia Project](https://www.mutopiaproject.org/)
- **Repository implementation of the paper:** [MMM: Exploring Conditional Multi-Track Music Generation with the Transformer and the Johann Sebastian Bach Chorales Dataset](https://github.com/AI-Guru/MMM-JSB)
- **Based on Paper:** [MMM: Exploring Conditional Multi-Track Music Generation with the Transformer](https://arxiv.org/abs/2008.06048)
- **Point of Contact:** [Juan Carlos Piñeros](https://www.linkedin.com/in/juancarlospinerosp/)

### Dataset Summary

Mutopia guitar dataset consists of the soloist guitar pieces of the [Mutopia Project](https://www.mutopiaproject.org/). I encoded the MIDI files into text tokens using the excellent [implementation](https://github.com/AI-Guru/MMM-JSB) of Dr. Tristan Beheren of the paper: [MMM: Exploring Conditional Multi-Track Music Generation with the Transformer](https://arxiv.org/abs/2008.06048). 

The dataset mainly contains guitar music from western classical composers, such as Sor, Aguado, Carcassi, and Giuliani.

### Supported Tasks and Leaderboards

Anyone interested can use the dataset to train a model for symbolic music generation, which consists in treating symbols for music sounds (notes) as text tokens. Then, one can implement a generative model using NLP techniques, such as Transformers.

## Dataset Structure

### Data Instances

Each guitar piece is represented as a line of text that contains a series of tokens, for instance:

PIECE_START: Where the piece begins
PIECE_ENDS: Where the piece ends
TIME_SIGNATURE: Time signature for the piece
BPM: Tempo of the piece
BAR_START: Begining of a new bar
NOTE_ON: Start of a new musical note specifying its MIDI note number
TIME_DELTA: Duration until the next event
NOTE_OFF: End of musical note specifying its MIDI note number

```
{
  'text': PIECE_START TIME_SIGNATURE=2_4 BPM=74 TRACK_START INST=0 DENSITY=4 BAR_START NOTE_ON=52 TIME_DELTA=2.0 NOTE_OFF=52 NOTE_ON=45 NOTE_ON=49 TIME_DELTA=2.0 NOTE_OFF=49 NOTE_ON=52 TIME_DELTA=2.0 NOTE_OFF=45 NOTE_ON=47 NOTE_OFF=52 NOTE_ON=44 TIME_DELTA=2.0,
  ...
}
```

### Data Fields

- `text`: Sequence of tokens that represent the guitar piece as explained in the paper [MMM: Exploring Conditional Multi-Track Music Generation with the Transformer](https://arxiv.org/abs/2008.06048).

### Data Splits

There are, at this moment, 395 MIDI guitar files in the Mutopia Project. I removed files of pieces that were not music for soloist guitar. After this removal, there were 372 MIDI files.

I used an 80/20 split and augmented the training dataset by transposing the piece 1 octave above and below (24 semitones). The final result is then:

**Train dataset:** 7325 pieces
**Test dataset:** 74 pieces