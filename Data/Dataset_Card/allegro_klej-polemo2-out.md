---
annotations_creators: 
- expert-generated 
language_creators: 
- other
language: 
- pl
license: 
- cc-by-sa-4.0
multilinguality: 
- monolingual
pretty_name: 'PolEmo2.0-OUT'
size_categories: 
- 1K<n<10K
source_datasets: 
- original
task_categories: 
- text-classification
task_ids: 
- sentiment-classification
---

# klej-polemo2-out

## Description

The PolEmo2.0 is a dataset of online consumer reviews from four domains: medicine, hotels, products, and university. It is human-annotated on a level of full reviews and individual sentences. It comprises over 8000 reviews, about 85% from the medicine and hotel domains.

We use the PolEmo2.0 dataset to form two tasks. Both use the same training dataset, i.e., reviews from medicine and hotel domains, but are evaluated on a different test set. 

**Out-of-Domain** is the second task, and we test the model on out-of-domain reviews, i.e., from product and university domains. Since the original test sets for those domains are scarce (50 reviews each), we decided to use the original out-of-domain training set of 900 reviews for testing purposes and create a new split of development and test sets. As a result, the task consists of 1000 reviews, comparable in size to the in-domain test dataset of 1400 reviews.

## Tasks (input, output, and metrics)

The task is to predict the correct label of the review.

**Input** ('*text'* column): sentence

**Output** ('*target'* column): label for sentence sentiment ('zero': neutral, 'minus': negative, 'plus': positive, 'amb': ambiguous)

**Domain**: Online reviews

**Measurements**: Accuracy

**Example**:

Input: `Lekarz zalecił mi kurację alternatywną do dotychczasowej , więc jeszcze nie daję najwyższej oceny ( zobaczymy na ile okaże się skuteczna ) . Do Pana doktora nie mam zastrzeżeń : bardzo profesjonalny i kulturalny . Jedyny minus dotyczy gabinetu , który nie jest nowoczesny , co może zniechęcać pacjentki .`

Input (translated by DeepL): `The doctor recommended me an alternative treatment to the current one , so I do not yet give the highest rating ( we will see how effective it turns out to be ) . To the doctor I have no reservations : very professional and cultured . The only minus is about the office , which is not modern , which may discourage patients .`

Output: `amb` (ambiguous)

## Data splits

| Subset     |   Cardinality |
|:-----------|--------------:|
| train      |          5783 |
| test       |           722 |
| validation |           723 |

## Class distribution

| Class | Sentiment | train | validation |  test |
|:------|:----------|------:|-----------:|------:|
| minus | positive  | 0.379 |      0.334 | 0.368 |
| plus  | negative  | 0.271 |      0.332 | 0.302 |
| amb   | ambiguous | 0.182 |      0.332 | 0.328 |
| zero  | neutral   | 0.168 |      0.002 | 0.002 |

## Citation

```
@inproceedings{kocon-etal-2019-multi,
    title = "Multi-Level Sentiment Analysis of {P}ol{E}mo 2.0: Extended Corpus of Multi-Domain Consumer Reviews",
    author = "Koco{\'n}, Jan  and
      Mi{\l}kowski, Piotr  and
      Za{\'s}ko-Zieli{\'n}ska, Monika",
    booktitle = "Proceedings of the 23rd Conference on Computational Natural Language Learning (CoNLL)",
    month = nov,
    year = "2019",
    address = "Hong Kong, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/K19-1092",
    doi = "10.18653/v1/K19-1092",
    pages = "980--991",
    abstract = "In this article we present an extended version of PolEmo {--} a corpus of consumer reviews from 4 domains: medicine, hotels, products and school. Current version (PolEmo 2.0) contains 8,216 reviews having 57,466 sentences. Each text and sentence was manually annotated with sentiment in 2+1 scheme, which gives a total of 197,046 annotations. We obtained a high value of Positive Specific Agreement, which is 0.91 for texts and 0.88 for sentences. PolEmo 2.0 is publicly available under a Creative Commons copyright license. We explored recent deep learning approaches for the recognition of sentiment, such as Bi-directional Long Short-Term Memory (BiLSTM) and Bidirectional Encoder Representations from Transformers (BERT).",
}
```

## License

```
Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)
```

## Links

[HuggingFace](https://huggingface.co/datasets/allegro/klej-polemo2-out)

[Source](https://clarin-pl.eu/dspace/handle/11321/710)

[Paper](https://aclanthology.org/K19-1092/)

## Examples

### Loading

```python
from pprint import pprint

from datasets import load_dataset

dataset = load_dataset("allegro/klej-polemo2-out")
pprint(dataset['train'][0])

# {'sentence': 'Super lekarz i człowiek przez duże C . Bardzo duże doświadczenie '
#              'i trafne diagnozy . Wielka cierpliwość do ludzi starszych . Od '
#              'lat opiekuje się moją Mamą staruszką , i twierdzę , że mamy duże '
#              'szczęście , że mamy takiego lekarza . Naprawdę nie wiem cobyśmy '
#              'zrobili , gdyby nie Pan doktor . Dzięki temu , moja mama żyje . '
#              'Każda wizyta u specjalisty jest u niego konsultowana i uważam , '
#              'że jest lepszy od każdego z nich . Mamy do Niego prawie '
#              'nieograniczone zaufanie . Można wiele dobrego o Panu doktorze '
#              'jeszcze napisać . Niestety , ma bardzo dużo pacjentów , jest '
#              'przepracowany ( z tego powodu nawet obawiam się o jego zdrowie ) '
#              'i dostęp do niego jest trudny , ale zawsze możliwy .',
#  'target': '__label__meta_plus_m'}
```

### Evaluation

```python
import random
from pprint import pprint

from datasets import load_dataset, load_metric

dataset = load_dataset("allegro/klej-polemo2-out")
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

# {'accuracy': 0.2894736842105263}
# {'f1': 0.2484406098784191}
```