---
language:
- pl
license:
- cc-by-nc-sa-4.0
multilinguality:
- monolingual
size_categories:
- 10K<n<100K
task_categories:
- text-classification
task_ids:
- topic-classification
- multi-class-classification
pretty_name: 8TAGS
dataset_info:
  features:
  - name: sentence
    dtype: string
  - name: label
    dtype:
      class_label:
        names:
          0: film
          1: history
          2: food
          3: medicine
          4: motorization
          5: work
          6: sport
          7: technology
  splits:
  - name: train
  - name: validation
  - name: test
---

# 8TAGS

### Dataset Summary

A Polish topic classification dataset consisting of headlines from social media posts. It contains about 50,000 sentences annotated with 8 topic labels: film, history, food, medicine, motorization, work, sport and technology. This dataset was created automatically by extracting sentences from headlines and short descriptions of articles posted on Polish social networking site **wykop.pl**. The service allows users to annotate articles with one or more tags (categories). Dataset represents a selection of article sentences from 8 popular categories. The resulting corpus contains cleaned and tokenized, unambiguous sentences (tagged with only one of the selected categories), and longer than 30 characters.

### Data Instances

Example instance:
```
{
  "sentence": "Kierowca był nieco zdziwiony że podróżując sporo ponad 200 km / h zatrzymali go policjanci.", 
  "label": "4"
}
```

### Data Fields

- sentence: sentence text
- label: label identifier corresponding to one of 8 topics

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
