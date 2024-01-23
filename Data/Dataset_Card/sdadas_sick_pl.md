---
language:
- pl
license:
- cc-by-nc-sa-3.0
multilinguality:
- monolingual
size_categories:
- 1K<n<10K
source_datasets:
- sick
task_categories:
- text-classification
task_ids:
- natural-language-inference
- semantic-similarity-scoring
pretty_name: Sentences Involving Compositional Knowledge (Polish)
dataset_info:
  features:
  - name: pair_ID
    dtype: string
  - name: sentence_A
    dtype: string
  - name: sentence_B
    dtype: string
  - name: relatedness_score
    dtype: float32
  - name: entailment_judgment
    dtype: string 
  splits:
  - name: train
  - name: validation
  - name: test
---

# SICK_PL - Sentences Involving Compositional Knowledge (Polish)

### Dataset Summary

This dataset is a manually translated version of popular English natural language inference (NLI) corpus consisting of 10,000 sentence pairs. NLI is the task of determining whether one statement (premise) semantically entails other statement (hypothesis). Such relation can be classified as entailment (if the first sentence entails second sentence), neutral (the first statement does not determine the truth value of the second statement), or contradiction (if the first sentence is true, the second is false). Additionally, the original SICK dataset contains semantic relatedness scores for the sentence pairs as real numbers ranging from 1 to 5. When translating the corpus to Polish, we tried to be as close as possible to the original meaning. In some cases, however, two different English sentences had an identical translation in Polish. Such instances were slightly modified in order to preserve both the meaning and the syntactic differences in sentence pair.

### Data Instances

Example instance:
```
{
  "pair_ID": "122",
  "sentence_A": "Pięcioro dzieci stoi blisko siebie , a jedno dziecko ma pistolet",
  "sentence_B": "Pięcioro dzieci stoi blisko siebie i żadne z nich nie ma pistoletu",
  "relatedness_score": 3.7,
  "entailment_judgment": "CONTRADICTION"
}
```

### Data Fields

- pair_ID: sentence pair ID
- sentence_A: sentence A
- sentence_B: sentence B
- entailment_judgment: textual entailment gold label: entailment (0), neutral (1) or contradiction (2)
- relatedness_score: semantic relatedness gold score (on a 1-5 continuous scale)

### Citation Information

```
@inproceedings{dadas-etal-2020-evaluation,
  title = "Evaluation of Sentence Representations in {P}olish",
  author = "Dadas, Slawomir  and Pere{\l}kiewicz, Micha{\l} and Po{\'s}wiata, Rafa{\l}",
  booktitle = "Proceedings of the 12th Language Resources and Evaluation Conference",
  month = may,
  year = "2020",
  address = "Marseille, France",
  publisher = "European Language Resources Association",
  url = "https://aclanthology.org/2020.lrec-1.207",
  pages = "1674--1680",
  language = "English",
  ISBN = "979-10-95546-34-4",
}
```