---
license: cc-by-2.0
task_categories:
- text-classification
language:
- en
size_categories:
- 100K<n<1M
---

# PLANE Out-of-Distribution Sets

PLANE (phrase-level adjective-noun entailment) is a benchmark to test models on fine-grained compositional inference. 
The current dataset contains five sampled splits, used in the supervised experiments of [Bertolini et al., 22](https://aclanthology.org/2022.coling-1.359/). 

## Data Structure

The `dataset` is organised around five `Train/test_split#`, each containing a training and test set of circa 60K and 2K.

### Features

Each entrance has 6 features: `seq, label, Adj_Class, Adj, Nn, Hy`
- `seq`:test sequense
- `label`: ground truth (1:entialment, 0:no-entailment)
- `Adj_Class`: the class of the sequence adjectives
- `Adj`: the adjective of the sequence (I: intersective, S: subsective, O: intensional)
- `N`n: the noun
- `Hy`: the noun's hypericum

Each sample in `seq` can take one of three forms (or inference types, in paper):

- An *Adjective-Noun* is a *Noun* (e.g. A red car is a car)
- An *Adjective-Noun* is a *Hypernym(Noun)* (e.g. A red car is a vehicle)
- An *Adjective-Noun* is a *Adjective-Hypernym(Noun)* (e.g. A red car is a red vehicle)

Please note that, as specified in the paper, the ground truth is automatically assigned based on the linguistic rule that governs the interaction between each adjective class and inference type – see the paper for more detail. 

### Trained Model

You can find a tuned BERT-base model (tuned and validated using the 2nd split) [here](https://huggingface.co/lorenzoscottb/bert-base-cased-PLANE-ood-2?text=A+fake+smile+is+a+smile).

### Cite

If you use PLANE for your work, please cite the main COLING 2022 paper.
```
@inproceedings{bertolini-etal-2022-testing,
    title = "Testing Large Language Models on Compositionality and Inference with Phrase-Level Adjective-Noun Entailment",
    author = "Bertolini, Lorenzo  and
      Weeds, Julie  and
      Weir, David",
    booktitle = "Proceedings of the 29th International Conference on Computational Linguistics",
    month = oct,
    year = "2022",
    address = "Gyeongju, Republic of Korea",
    publisher = "International Committee on Computational Linguistics",
    url = "https://aclanthology.org/2022.coling-1.359",
    pages = "4084--4100",
}

```