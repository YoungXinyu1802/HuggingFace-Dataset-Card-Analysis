---
annotations_creators:
- expert-generated
language_creators:
- other
language:
- pl
license:
- gpl-3.0
multilinguality:
- monolingual
size_categories:
- unknown
source_datasets:
- original
task_categories:
- other
task_ids:
- part-of-speech
pretty_name: nkjp-pos
tags:
- structure-prediction
---

# nkjp-pos

## Description

NKJP-POS is a part the National Corpus of Polish (*Narodowy Korpus Języka Polskiego*). Its objective is part-of-speech tagging, e.g. nouns, verbs, adjectives, adverbs, etc. During the creation of corpus, texts of were annotated by humans from various sources, covering many domains and genres.

## Tasks (input, output and metrics)

Part-of-speech tagging (POS tagging) - tagging words in text with their corresponding part of speech.

**Input** ('*tokens'* column): sequence of tokens

**Output** ('*pos_tags'* column): sequence of predicted tokens’ classes (35 possible classes, described in detail in the annotation guidelines)

**Measurements**: F1-score (seqeval)

**Example***:*

Input: `['Zarejestruj', 'się', 'jako', 'bezrobotny', '.']`

Input (translated by DeepL): `Register as unemployed.`

Output:  `['impt', 'qub', 'conj', 'subst', 'interp']`

## Data splits

| Subset      | Cardinality (sentences) |
| ----------- | ----------------------: |
| train       | 78219                   |
| dev         | 0                       |
| test        | 7444                    |


## Class distribution


| Class   |   train | dev   |    test |
|:--------|--------:|------:|--------:|
| subst   | 0.27345 | -     | 0.27656 |
| interp  | 0.18101 | -     | 0.17944 |
| adj     | 0.10611 | -     | 0.10919 |
| prep    | 0.09567 | -     | 0.09547 |
| qub     | 0.05670 | -     | 0.05491 |
| fin     | 0.04939 | -     | 0.04648 |
| praet   | 0.04409 | -     | 0.04348 |
| conj    | 0.03711 | -     | 0.03724 |
| adv     | 0.03512 | -     | 0.03333 |
| inf     | 0.01591 | -     | 0.01547 |
| comp    | 0.01476 | -     | 0.01439 |
| num     | 0.01322 | -     | 0.01436 |
| ppron3  | 0.01111 | -     | 0.01018 |
| ppas    | 0.01086 | -     | 0.01085 |
| ger     | 0.00961 | -     | 0.01050 |
| brev    | 0.00856 | -     | 0.01181 |
| ppron12 | 0.00670 | -     | 0.00665 |
| aglt    | 0.00629 | -     | 0.00602 |
| pred    | 0.00539 | -     | 0.00540 |
| pact    | 0.00454 | -     | 0.00452 |
| bedzie  | 0.00229 | -     | 0.00243 |
| pcon    | 0.00218 | -     | 0.00189 |
| impt    | 0.00203 | -     | 0.00226 |
| siebie  | 0.00177 | -     | 0.00158 |
| imps    | 0.00174 | -     | 0.00177 |
| interj  | 0.00131 | -     | 0.00102 |
| xxx     | 0.00070 | -     | 0.00048 |
| adjp    | 0.00069 | -     | 0.00065 |
| winien  | 0.00068 | -     | 0.00057 |
| adja    | 0.00048 | -     | 0.00058 |
| pant    | 0.00012 | -     | 0.00018 |
| burk    | 0.00011 | -     | 0.00006 |
| numcol  | 0.00011 | -     | 0.00013 |
| depr    | 0.00010 | -     | 0.00004 |
| adjc    | 0.00007 | -     | 0.00008 |


## Citation

```
@book{przepiorkowski_narodowy_2012,
title = {Narodowy korpus języka polskiego},
isbn = {978-83-01-16700-4},
language = {pl},
publisher = {Wydawnictwo Naukowe PWN},
editor = {Przepiórkowski, Adam and Bańko, Mirosław and Górski, Rafał L. and Lewandowska-Tomaszczyk, Barbara},
year = {2012}
}
```

## License

```
GNU GPL v.3
```

## Links

[HuggingFace](https://huggingface.co/datasets/clarin-pl/nkjp-pos)

[Source](http://clip.ipipan.waw.pl/NationalCorpusOfPolish)

[Paper](http://nkjp.pl/settings/papers/NKJP_ksiazka.pdf)

## Examples

### Loading

```python
from pprint import pprint

from datasets import load_dataset

dataset = load_dataset("clarin-pl/nkjp-pos")
pprint(dataset['train'][5000])

# {'id': '130-2-900005_morph_49.49-s',
#  'pos_tags': [16, 4, 3, 30, 12, 18, 3, 16, 14, 6, 14, 26, 1, 30, 12],
#  'tokens': ['Najwyraźniej',
#             'źle',
#             'ocenił',
#             'odległość',
#             ',',
#             'bo',
#             'zderzył',
#             'się',
#             'z',
#             'jadącą',
#             'z',
#             'naprzeciwka',
#             'ciężarową',
#             'scanią',
#             '.']}
```

### Evaluation

```python
import random
from pprint import pprint

from datasets import load_dataset, load_metric

dataset = load_dataset("clarin-pl/nkjp-pos")
references = dataset["test"]["pos_tags"]

# generate random predictions
predictions = [
    [
        random.randrange(dataset["train"].features["pos_tags"].feature.num_classes)
        for _ in range(len(labels))
    ]
    for labels in references
]

# transform to original names of labels
references_named = [
    [dataset["train"].features["pos_tags"].feature.names[label] for label in labels]
    for labels in references
]
predictions_named = [
    [dataset["train"].features["pos_tags"].feature.names[label] for label in labels]
    for labels in predictions
]

# transform to BILOU scheme
references_named = [
    [f"U-{label}" if label != "O" else label for label in labels]
    for labels in references_named
]
predictions_named = [
    [f"U-{label}" if label != "O" else label for label in labels]
    for labels in predictions_named
]

# utilise seqeval to evaluate
seqeval = load_metric("seqeval")
seqeval_score = seqeval.compute(
    predictions=predictions_named,
    references=references_named,
    scheme="BILOU",
    mode="strict",
)

pprint(seqeval_score, depth=1)

# {'adj': {...},
#  'adja': {...},
#  'adjc': {...},
#  'adjp': {...},
#  'adv': {...},
#  'aglt': {...},
#  'bedzie': {...},
#  'brev': {...},
#  'burk': {...},
#  'comp': {...},
#  'conj': {...},
#  'depr': {...},
#  'fin': {...},
#  'ger': {...},
#  'imps': {...},
#  'impt': {...},
#  'inf': {...},
#  'interj': {...},
#  'interp': {...},
#  'num': {...},
#  'numcol': {...},
#  'overall_accuracy': 0.027855061488566583,
#  'overall_f1': 0.027855061488566583,
#  'overall_precision': 0.027855061488566583,
#  'overall_recall': 0.027855061488566583,
#  'pact': {...},
#  'pant': {...},
#  'pcon': {...},
#  'ppas': {...},
#  'ppron12': {...},
#  'ppron3': {...},
#  'praet': {...},
#  'pred': {...},
#  'prep': {...},
#  'qub': {...},
#  'siebie': {...},
#  'subst': {...},
#  'winien': {...},
#  'xxx': {...}}
```