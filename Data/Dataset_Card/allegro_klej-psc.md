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
- 5K
- 1K<n<10K
source_datasets:
- original
task_categories:
- text-classification
task_ids: []
pretty_name: Polish Summaries Corpus
tags:
- paraphrase-classification
---

# klej-psc

## Description

The Polish Summaries Corpus (PSC) is a dataset of summaries for 569 news articles. The human annotators created five extractive summaries for each article by choosing approximately 5% of the original text. A different annotator created each summary. The subset of 154 articles was also supplemented with additional five abstractive summaries each, i.e., not created from the fragments of the original article. In huggingface version of this dataset, summaries of the same article are used as positive pairs, and the most similar summaries of different articles are sampled as negatives.

## Tasks (input, output, and metrics)

The task is to predict whether the extract text and summary are similar.

Based on PSC, we formulate a text-similarity task. We generate the positive pairs (i.e., referring
to the same article) using only those news articles with both extractive and abstractive summaries. We match each extractive summary with two least similar abstractive ones of the same article.  To create negative pairs, we follow a similar procedure. We find two most similar abstractive summaries for each extractive summary, but from different articles.

**Input** (*'extract_text'*, *'summary_text'* columns): extract text and summary text sentences

**Output** (*'label'* column): label: 1 indicates summary is similar, 0 means that it is not similar

**Domain**: News articles

**Measurements**: F1-Score

**Example**:

Input: `Mit o potopie jest prastary, sięga czasów, gdy topniał lodowiec. Na skutek tego wydarzenia w dziejach planety, poziom mórz i oceanów podniósł się o kilkadziesiąt metrów. Potop polodowcowy z całą, naukową pewnością, miał miejsce, ale najprawdopodobniej został przez ludzkość przegapiony. I oto pojawiła się w tej sprawie kolejna glosa. Jej autorami są amerykańscy geofizycy.` ; `Dwójka amerykańskich geofizyków przedstawiła swój scenariusz pochodzenia mitu o potopie. Przed 7500 laty do będącego jeszcze jeziorem Morza Czarnego wlały się wezbrane wskutek topnienia lodowców wody Morza Śródziemnego. Geofizycy twierdzą, że dzięki temu rozkwitło rolnictwo, bo ludzie musieli migrować i szerzyć rolniczy tryb życia. Środowiska naukowe twierdzą jednak, że potop był tylko jednym z czynników ekspansji rolnictwa.`

Input (translated by DeepL): `The myth of the Flood is ancient, dating back to the time when the glacier melted. As a result of this event in the history of the planet, the level of the seas and oceans rose by several tens of meters. The post-glacial flood with all, scientific certainty, took place, but was most likely missed by mankind. And here is another gloss on the matter. Its authors are American geophysicists.` ; `Two American geophysicists presented their scenario of the origin of the Flood myth. 7500 years ago, the waters of the Mediterranean Sea flooded into the Black Sea, which was still a lake, due to the melting of glaciers. Geophysicists claim that this made agriculture flourish because people had to migrate and spread their agricultural lifestyle. However, the scientific community argues that the Flood was only one factor in the expansion of agriculture.`

Output: `1` (summary is similar)

## Data splits

| Subset      | Cardinality |
| ----------- | ----------: |
| train       | 4302        |
| val         | 0           |
| test        | 1078        |

## Class distribution

|   Class     |   train |   validation |   test |
|:------------|--------:|-------------:|-------:|
| not similar |   0.705 |            - |  0.696 |
|     similar |   0.295 |            - |  0.304 |

## Citation
```
@inproceedings{ogro:kop:14:lrec,
title={The {P}olish {S}ummaries {C}orpus},
author={Ogrodniczuk, Maciej and Kope{'c}, Mateusz},
booktitle = "Proceedings of the Ninth International {C}onference on {L}anguage {R}esources and {E}valuation, {LREC}~2014",
year = "2014",
}
```
## License

```
Creative Commons Attribution ShareAlike 3.0 licence (CC-BY-SA 3.0)
```

## Links

[HuggingFace](https://huggingface.co/datasets/allegro/klej-psc)

[Source](http://zil.ipipan.waw.pl/PolishSummariesCorpus)

[Paper](https://aclanthology.org/L14-1145/)

## Examples

### Loading

```python
from pprint import pprint

from datasets import load_dataset

dataset = load_dataset("allegro/klej-psc")
pprint(dataset['train'][100])

#{'extract_text': 'Nowe prawo energetyczne jest zagrożeniem dla  małych '
#                 'producentów energii ze źródeł odnawialnych. Sytuacja się '
#                 'pogarsza wdobie urynkowienia energii. zniosło preferencje '
#                 'wprowadzone dla energetyki wodnej. UE zamierza podwoić '
#                 'udział takich źródeł energetyki jak woda, wiatr, słońce do '
#                 '2010 r.W Polsce 1-1,5 proc. zużycia energii wytwarza się ze '
#                 'źródeł odnawialnych. W krajach Unii udział ten wynosi '
#                 'średnio 5,6 proc.',
# 'label': 1,
# 'summary_text': 'W Polsce w niewielkim stopniu wykorzystuje się elektrownie '
#                 'wodne oraz inne sposoby tworzenia energii ze źródeł '
#                 'odnawialnych. Podczas gdy w innych krajach europejskich jest '
#                 'to średnio 5,6 % w Polsce jest to 1-1,5 %. Powodem jest '
#                 'niska opłacalność posiadania tego typu elektrowni-zakład '
#                 'energetyczny płaci ok. 17 gr. za 1kWh, podczas gdy '
#                 'wybudowanie takiej elektrowni kosztuje ok. 100 tyś. zł.'}
```

### Evaluation

```python
import random
from pprint import pprint

from datasets import load_dataset, load_metric

dataset = load_dataset("allegro/klej-psc")
dataset = dataset.class_encode_column("label")
references = dataset["test"]["label"]

# generate random predictions
predictions = [random.randrange(max(references) + 1) for _ in range(len(references))]

acc = load_metric("accuracy")
f1 = load_metric("f1")

acc_score = acc.compute(predictions=predictions, references=references)
f1_score = f1.compute(predictions=predictions, references=references, average="macro")

pprint(acc_score)
pprint(f1_score)

# {'accuracy': 0.18588469184890655}
# {'f1': 0.17511412402843068}

```