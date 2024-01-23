---
annotations_creators:
- expert-generated
language_creators:
- other
language:
- pl
license:
- cc-by-sa-3.0
multilinguality:
- monolingual
size_categories:
- 1K<n<10K
source_datasets:
- original
task_categories:
- question-answering
task_ids:
- open-domain-qa
pretty_name: Did you know?
---

# klej-dyk

## Description

The Czy wiesz? (eng. Did you know?) the dataset consists of almost 5k question-answer pairs obtained from Czy wiesz... section of Polish Wikipedia. Each question is written by a Wikipedia collaborator and is answered with a link to a relevant Wikipedia article. In huggingface version of this dataset, they chose the negatives which have the largest token overlap with a question.

## Tasks (input, output, and metrics)

The task is to predict if the answer to the given question is correct or not. 

**Input** ('question sentence', 'answer' columns): question and answer sentences

**Output** ('target' column): 1 if the answer is correct, 0 otherwise. 

**Domain**: Wikipedia

**Measurements**: F1-Score

**Example**:

Input: `Czym zajmowali się świątnicy?` ; `Świątnik – osoba, która dawniej zajmowała się
obsługą kościoła (świątyni).`  

Input (translated by DeepL): `What did the sacristans do?` ; `A sacristan - a person who used to be in charge of the handling the church (temple).`

Output: `1` (the answer is correct)

## Data splits

| Subset      | Cardinality |
| ----------- | ----------: |
| train       | 4154        |
| val         | 0           |
| test        | 1029        |

## Class distribution

|     Class |   train |   validation |   test |
|:----------|--------:|-------------:|-------:|
| incorrect |   0.831 |            - |  0.831 |
|   correct |   0.169 |            - |  0.169 |

## Citation

```
@misc{11321/39,	
 title = {Pytania i odpowiedzi z serwisu wikipedyjnego "Czy wiesz", wersja 1.1},	
 author = {Marci{\'n}czuk, Micha{\l} and Piasecki, Dominik and Piasecki, Maciej and Radziszewski, Adam},	
 url = {http://hdl.handle.net/11321/39},	
 note = {{CLARIN}-{PL} digital repository},	
 year = {2013}	
}
```

## License

```
Creative Commons Attribution ShareAlike 3.0 licence (CC-BY-SA 3.0)
```

## Links

[HuggingFace](https://huggingface.co/datasets/dyk)

[Source](http://nlp.pwr.wroc.pl/en/tools-and-resources/resources/czy-wiesz-question-answering-dataset)
[Source #2](https://clarin-pl.eu/dspace/handle/11321/39) 

[Paper](https://www.researchgate.net/publication/272685895_Open_dataset_for_development_of_Polish_Question_Answering_systems)

## Examples

### Loading

```python
from pprint import pprint

from datasets import load_dataset

dataset = load_dataset("allegro/klej-dyk")
pprint(dataset['train'][100])

#{'answer': '"W wyborach prezydenckich w 2004 roku, Moroz przekazał swoje '
#           'poparcie Wiktorowi Juszczence. Po wyborach w 2006 socjaliści '
#           'początkowo tworzyli ""pomarańczową koalicję"" z Naszą Ukrainą i '
#           'Blokiem Julii Tymoszenko."',
# 'q_id': 'czywiesz4362',
# 'question': 'ile partii tworzy powołaną przez Wiktora Juszczenkę koalicję '
#             'Blok Nasza Ukraina?',
# 'target': 0}
```

### Evaluation

```python
import random
from pprint import pprint

from datasets import load_dataset, load_metric

dataset = load_dataset("allegro/klej-dyk")
dataset = dataset.class_encode_column("target")
references = dataset["test"]["target"]

# generate random predictions
predictions = [random.randrange(max(references) + 1) for _ in range(len(references))]

acc = load_metric("accuracy")
f1 = load_metric("f1")

acc_score = acc.compute(predictions=predictions, references=references)
f1_score = f1.compute(predictions=predictions, references=references, average="macro")

pprint(acc_score)
pprint(f1_score)

# {'accuracy': 0.5286686103012633}
# {'f1': 0.46700507614213194}

```