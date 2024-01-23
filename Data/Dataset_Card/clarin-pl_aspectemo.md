---
annotations_creators: 
- expert-generated 
language_creators: 
- other
language: 
- pl
license: 
- mit
multilinguality: 
- monolingual
pretty_name: 'AspectEmo'
size_categories: 
- 1K
- 1K<n<10K
source_datasets: 
- original
task_categories: 
- token-classification
task_ids: 
- sentiment-classification
---

# AspectEmo

## Description

AspectEmo Corpus is an extended version of a publicly available PolEmo 2.0 corpus of Polish customer reviews used in many projects on the use of different methods in sentiment analysis. The AspectEmo corpus consists of four subcorpora, each containing online customer reviews from the following domains: school, medicine, hotels, and products. All documents are annotated at the aspect level with six sentiment categories: strong negative (minus_m), weak negative (minus_s), neutral (zero), weak positive (plus_s), strong positive (plus_m).
## Versions

| version | config name | description                    | default | notes            |
|---------|-------------|--------------------------------|---------|------------------|
| 1.0     | "1.0"       | The version used in the paper. | YES     |                  |
| 2.0     | -           | Some bugs fixed.               | NO      | work in progress |

## Tasks (input, output and metrics)

Aspect-based sentiment analysis (ABSA) is a text analysis method that categorizes data by  aspects and identifies the sentiment assigned to each aspect. It is the sequence tagging task. 

**Input** ('*tokens'* column): sequence of tokens

**Output** ('*labels'* column): sequence of predicted tokens’ classes ("O" + 6 possible classes:  strong negative (a_minus_m), weak negative (a_minus_s), neutral (a_zero), weak positive (a_plus_s), strong positive (a_plus_m),  ambiguous (a_amb) )

**Domain**: school, medicine, hotels and products

**Measurements**: F1-score (seqeval)

**Example***:* 

Input: `['Dużo', 'wymaga', ',', 'ale', 'bardzo', 'uczciwy', 'i', 'przyjazny', 'studentom', '.', 'Warto', 'chodzić', 'na', 'konsultacje', '.', 'Docenia', 'postępy', 'i', 'zaangażowanie', '.', 'Polecam', '.']`

Input (translated by DeepL): `'Demands a lot , but very honest and student friendly . Worth going to consultations . Appreciates progress and commitment . I recommend .'`

Output: `['O', 'a_plus_s', 'O', 'O', 'O', 'a_plus_m', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'a_zero', 'O', 'a_plus_m', 'O', 'O', 'O', 'O', 'O', 'O']`

## Data splits

| Subset | Cardinality (sentences) |
|:-------|------------------------:|
| train  |                    1173 |
| val    |                       0 |
| test   |                     292 |

## Class distribution(without "O") 

| Class     |   train |   validation |   test |
|:----------|--------:|-------------:|-------:|
| a_plus_m  |   0.359 |            - |  0.369 |
| a_minus_m |   0.305 |            - |  0.377 |
| a_zero    |   0.234 |            - |  0.182 |
| a_minus_s |   0.037 |            - |  0.024 |
| a_plus_s  |   0.037 |            - |  0.015 |
| a_amb     |   0.027 |            - |  0.033 |

## Citation

```
@misc{11321/849,	
 title = {{AspectEmo} 1.0: Multi-Domain Corpus of Consumer Reviews for Aspect-Based Sentiment Analysis},	
 author = {Koco{\'n}, Jan and Radom, Jarema and Kaczmarz-Wawryk, Ewa and Wabnic, Kamil and Zaj{\c a}czkowska, Ada and Za{\'s}ko-Zieli{\'n}ska, Monika},	
 url = {http://hdl.handle.net/11321/849},	
 note = {{CLARIN}-{PL} digital repository},	
 copyright = {The {MIT} License},	
 year = {2021}	
}
```

## License

```
The MIT License
```

## Links

[HuggingFace](https://huggingface.co/datasets/clarin-pl/aspectemo)

[Source](https://clarin-pl.eu/dspace/handle/11321/849)

[Paper](https://sentic.net/sentire2021kocon.pdf)

## Examples

### Loading

```python
from pprint import pprint

from datasets import load_dataset

dataset = load_dataset("clarin-pl/aspectemo")
pprint(dataset['train'][20])

# {'labels': [0, 4, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 3, 0, 5, 0, 0, 0, 0, 0, 0],
#  'tokens': ['Dużo',
#             'wymaga',
#             ',',
#             'ale',
#             'bardzo',
#             'uczciwy',
#             'i',
#             'przyjazny',
#             'studentom',
#             '.',
#             'Warto',
#             'chodzić',
#             'na',
#             'konsultacje',
#             '.',
#             'Docenia',
#             'postępy',
#             'i',
#             'zaangażowanie',
#             '.',
#             'Polecam',
#             '.']}
```

### Evaluation

```python
import random
from pprint import pprint

from datasets import load_dataset, load_metric

dataset = load_dataset("clarin-pl/aspectemo")
references = dataset["test"]["labels"]

# generate random predictions
predictions = [
    [
        random.randrange(dataset["train"].features["labels"].feature.num_classes)
        for _ in range(len(labels))
    ]
    for labels in references
]

# transform to original names of labels
references_named = [
    [dataset["train"].features["labels"].feature.names[label] for label in labels]
    for labels in references
]
predictions_named = [
    [dataset["train"].features["labels"].feature.names[label] for label in labels]
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

pprint(seqeval_score)

# {'a_amb': {'f1': 0.00597237775289287,
#            'number': 91,
#            'precision': 0.003037782418834251,
#            'recall': 0.17582417582417584},
#  'a_minus_m': {'f1': 0.048306148055207034,
#                'number': 1039,
#                'precision': 0.0288551620760727,
#                'recall': 0.1482194417709336},
#  'a_minus_s': {'f1': 0.004682997118155619,
#                'number': 67,
#                'precision': 0.0023701002734731083,
#                'recall': 0.19402985074626866},
#  'a_plus_m': {'f1': 0.045933014354066985,
#               'number': 1015,
#               'precision': 0.027402473834443386,
#               'recall': 0.14187192118226602},
#  'a_plus_s': {'f1': 0.0021750951604132683,
#               'number': 41,
#               'precision': 0.001095690284879474,
#               'recall': 0.14634146341463414},
#  'a_zero': {'f1': 0.025159400310184387,
#             'number': 501,
#             'precision': 0.013768389287061486,
#             'recall': 0.14570858283433133},
#  'overall_accuracy': 0.13970115681233933,
#  'overall_f1': 0.02328248652368391,
#  'overall_precision': 0.012639312620633834,
#  'overall_recall': 0.14742193173565724}
```