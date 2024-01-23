---
license: cc
task_categories:
- text-classification
language:
- ba
- cv
- sah
- tt
- ky
- kk
- tyv
- krc
- ru

tags:
- wiki
size_categories:
- 10K<n<100K
---

# Cyrillic dataset of 8 Turkic languages spoken in Russia and former USSR

## Dataset Description

The dataset is a part of the [Leipzig Corpora (Wiki) Collection]: https://corpora.uni-leipzig.de/

For the text-classification comparison, Russian has been included to the dataset.

 **Paper:** 
Dirk Goldhahn, Thomas Eckart and Uwe Quasthoff (2012): Building Large Monolingual Dictionaries at the Leipzig Corpora Collection: From 100 to 200 Languages. In: Proceedings of the Eighth International Conference on Language Resources and Evaluation (LREC'12), 2012.

### Dataset Summary


### Supported Tasks and Leaderboards

### Languages

  - ba - Bashkir
  - cv - Chuvash
  - sah - Sakha
  - tt - Tatar
  - ky - Kyrgyz
  - kk - Kazakh
  - tyv - Tuvinian
  - krc - Karachay-Balkar
  - ru - Russian

### Data Splits


    train: Dataset({
        features: ['text', 'label'],
        num_rows: 72000
    })
    
    test: Dataset({
        features: ['text', 'label'],
        num_rows: 9000
    })
    
    validation: Dataset({
        features: ['text', 'label'],
        num_rows: 9000
    })
    

## Dataset Creation

[Link to the notebook](https://github.com/tatiana-merz/YakuToolkit/blob/main/CyrillicTurkicCorpus.ipynb)


### Curation Rationale

[More Information Needed]

### Source Data

## Additional Information

### Dataset Curators

[More Information Needed]

### Licensing Information

[More Information Needed]

### Citation Information

[More Information Needed]

### Contributions

[More Information Needed]