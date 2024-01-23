## Latin part of cc100 corpus
This dataset contains parts of the Latin part of the [cc100](http://data.statmt.org/cc-100/) dataset. It was used to train a [RoBERTa-based LM model](https://huggingface.co/pstroe/roberta-base-latin-cased) with huggingface.

### Preprocessing

I undertook the following preprocessing steps:

  - Removal of all "pseudo-Latin" text ("Lorem ipsum ...").
  - Use of [CLTK](http://www.cltk.org) for sentence splitting and normalisation.
  - Retaining only lines containing letters of the Latin alphabet, numerals, and certain punctuation (--> `grep -P '^[A-z0-9ÄÖÜäöüÆæŒœᵫĀāūōŌ.,;:?!\- Ęę]+$' la.nolorem.tok.txt`
  - deduplication of the corpus

The result is a corpus of ~390 million tokens.

### Structure
The dataset is structured the following way:
```
{
  "train": {
              "text": "Solventibus autem illis pullum , dixerunt domini ejus ad illos : Quid solvitis pullum ?",
              "text": "Errare humanum est ."
              ...
           }
  "test":  {
              "text": "Alia iacta est ."
              ...
           }
}
```

### Contact

For contact, reach out to Phillip Ströbel [via mail](mailto:pstroebel@cl.uzh.ch) or [via Twitter](https://twitter.com/CLingophil).