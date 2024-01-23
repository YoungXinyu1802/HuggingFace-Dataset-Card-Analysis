---
license: cc-by-2.0
task_categories:
- token-classification
language:
- en
size_categories:
- 1M<n<10M
---

# Dataset Card for Dataset Name

UFSAC: Unification of Sense Annotated Corpora and Tools

## Dataset Description

- **Homepage:** https://github.com/getalp/UFSAC
- **Repository:** https://github.com/getalp/UFSAC
- **Paper:** 
- **Leaderboard:** 
- **Point of Contact:** 

### Dataset Summary


### Supported Tasks and Leaderboards

WSD: Word Sense Disambiguation

### Languages

English

## Dataset Structure

### Data Instances

```
{'lemmas': ['_',
            'be',
            'quite',
            '_',
            'hefty',
            'spade',
            '_',
            '_',
            'bicycle',
            '_',
            'type',
            'handlebar',
            '_',
            '_',
            'spring',
            'lever',
            '_',
            '_',
            'rear',
            '_',
            '_',
            '_',
            'step',
            'on',
            '_',
            'activate',
            '_',
            '_'],
 'pos_tags': ['PRP',
              'VBZ',
              'RB',
              'DT',
              'JJ',
              'NN',
              ',',
              'IN',
              'NN',
              ':',
              'NN',
              'NNS',
              'CC',
              'DT',
              'VBN',
              'NN',
              'IN',
              'DT',
              'NN',
              ',',
              'WDT',
              'PRP',
              'VBP',
              'RP',
              'TO',
              'VB',
              'PRP',
              '.'],
 'sense_keys': ['activate%2:36:00::'],
 'target_idx': 25,
 'tokens': ['It',
            'is',
            'quite',
            'a',
            'hefty',
            'spade',
            ',',
            'with',
            'bicycle',
            '-',
            'type',
            'handlebars',
            'and',
            'a',
            'sprung',
            'lever',
            'at',
            'the',
            'rear',
            ',',
            'which',
            'you',
            'step',
            'on',
            'to',
            'activate',
            'it',
            '.']}
```

### Data Fields

```
{'tokens': Sequence(feature=Value(dtype='string', id=None), length=-1, id=None),
 'lemmas': Sequence(feature=Value(dtype='string', id=None), length=-1, id=None),
 'pos_tags': Sequence(feature=Value(dtype='string', id=None), length=-1, id=None),
 'target_idx': Value(dtype='int32', id=None),
 'sense_keys': Sequence(feature=Value(dtype='string', id=None), length=-1, id=None)}
```

### Data Splits

Not split. Use `train` split directly.
