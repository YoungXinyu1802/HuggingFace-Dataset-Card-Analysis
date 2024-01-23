---
annotations_creators:
- expert-generated
language_creators:
- expert-generated
language:
- pl
license:
- cc-by-nc-sa-4.0
multilinguality:
- monolingual
pretty_name: 'CDSC-E'
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- text-classification
task_ids:
- natural-language-inference
---

# klej-cdsc-e

## Description

Polish CDSCorpus consists of 10K Polish sentence pairs which are human-annotated for semantic relatedness (**CDSC-R**) and entailment (**CDSC-E**). The dataset may be used to evaluate compositional distributional semantics models of Polish. The dataset was presented at ACL 2017. 

Although the SICK corpus inspires the main design of the dataset, it differs in detail. As in SICK, the sentences come from image captions, but the set of chosen images is much more diverse as they come from 46 thematic groups.


## Tasks (input, output, and metrics)

The entailment relation between two sentences is labeled with *entailment*, *contradiction*, or *neutral*. The task is to predict if the premise entails the hypothesis (entailment), negates the hypothesis (contradiction), or is unrelated (neutral).

b **entails** a (a **wynika z** b) – if a situation or an event described by sentence b occurs, it is recognized that a situation or an event described by a occurs as well, i.e., a and b refer to the same event or the same situation;  

**Input**: ('sentence_A', 'sentence_B'): sentence pair

**Output** ('entailment_judgment' column): one of the possible entailment relations (*entailment*, *contradiction*, *neutral*)

**Domain:** image captions

**Measurements**: Accuracy

**Example:**

Input: `Żaden mężczyzna nie stoi na przystanku autobusowym.`  ; `Mężczyzna z żółtą i białą reklamówką w ręce stoi na przystanku obok autobusu.`

Input (translated by DeepL): `No man standing at the bus stop.` ;  `A man with a yellow and white bag in his hand stands at a bus stop next to a bus.` 

Output: `entailment`

## Data splits

| Subset        | Cardinality |
| ------------- | ----------: |
| train         | 8000        |
| validation    | 1000        |
| test          | 1000        |


## Class distribution

| Class         |   train |   validation |   test |
|:--------------|--------:|-------------:|-------:|
| NEUTRAL       |   0.744 |        0.741 |  0.744 |
| ENTAILMENT    |   0.179 |        0.185 |  0.190 |
| CONTRADICTION |   0.077 |        0.074 |  0.066 |

## Citation

```
@inproceedings{wroblewska-krasnowska-kieras-2017-polish,
    title = "{P}olish evaluation dataset for compositional distributional semantics models",
    author = "Wr{\'o}blewska, Alina  and
      Krasnowska-Kiera{\'s}, Katarzyna",
    booktitle = "Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = jul,
    year = "2017",
    address = "Vancouver, Canada",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/P17-1073",
    doi = "10.18653/v1/P17-1073",
    pages = "784--792",
    abstract = "The paper presents a procedure of building an evaluation dataset. for the validation of compositional distributional semantics models estimated for languages other than English. The procedure generally builds on steps designed to assemble the SICK corpus, which contains pairs of English sentences annotated for semantic relatedness and entailment, because we aim at building a comparable dataset. However, the implementation of particular building steps significantly differs from the original SICK design assumptions, which is caused by both lack of necessary extraneous resources for an investigated language and the need for language-specific transformation rules. The designed procedure is verified on Polish, a fusional language with a relatively free word order, and contributes to building a Polish evaluation dataset. The resource consists of 10K sentence pairs which are human-annotated for semantic relatedness and entailment. The dataset may be used for the evaluation of compositional distributional semantics models of Polish.",
}
```

## License

```
Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)
```

## Links

[HuggingFace](https://huggingface.co/datasets/allegro/klej-cdsc-e)

[Source](http://zil.ipipan.waw.pl/Scwad/CDSCorpus)

[Paper](https://aclanthology.org/P17-1073.pdf)

## Examples

### Loading

```python
from pprint import pprint

from datasets import load_dataset

dataset = load_dataset("allegro/klej-cdsc-e")
pprint(dataset["train"][0])

# {'entailment_judgment': 'NEUTRAL',
#  'pair_ID': 1,
#  'sentence_A': 'Chłopiec w czerwonych trampkach skacze wysoko do góry '
#                'nieopodal fontanny .',
#  'sentence_B': 'Chłopiec w bluzce w paski podskakuje wysoko obok brązowej '
#                'fontanny .'}
```

### Evaluation

```python
import random
from pprint import pprint

from datasets import load_dataset, load_metric

dataset = load_dataset("allegro/klej-cdsc-e")
dataset = dataset.class_encode_column("entailment_judgment")
references = dataset["test"]["entailment_judgment"]

# generate random predictions
predictions = [random.randrange(max(references) + 1) for _ in range(len(references))]

acc = load_metric("accuracy")
f1 = load_metric("f1")

acc_score = acc.compute(predictions=predictions, references=references)
f1_score = f1.compute(predictions=predictions, references=references, average="macro")

pprint(acc_score)
pprint(f1_score)

# {'accuracy': 0.325}
# {'f1': 0.2736171695141161}
```