---
annotations_creators:
- expert-generated
language:
- hu
language_creators:
- other
license: []
multilinguality:
- monolingual
paperswithcode_id: null
pretty_name: SzegedNER
size_categories:
- 1K<n<10K
source_datasets:
- original
tags:
- hungarian
- szeged
- ner
task_categories:
- token-classification
task_ids:
- named-entity-recognition
---

# Introduction

The recognition and classification of proper nouns and names in plain text is of key importance in Natural Language Processing (NLP) as it has a beneficial effect on the performance of various types of applications, including Information Extraction, Machine Translation, Syntactic Parsing/Chunking, etc.

## Corpus of Business Newswire Texts (business)

The Named Entity Corpus for Hungarian is a subcorpus of the Szeged Treebank, which contains full syntactic annotations done manually by linguist experts. A significant part of these texts has been annotated with Named Entity class labels in line with the annotation standards used on the CoNLL-2003 shared task.

Statistical data on Named Entities occurring in the corpus:

```
       | tokens | phrases
------ | ------ | -------
non NE | 200067 | 	 
PER    | 1921   | 982
ORG    | 20433  | 10533
LOC    | 1501   | 1294
MISC   | 2041   | 1662
```

### Reference

> György Szarvas, Richárd Farkas, László Felföldi, András Kocsor, János Csirik: Highly accurate Named Entity corpus for Hungarian. International Conference on Language Resources and Evaluation 2006, Genova (Italy)

## Criminal NE corpus (criminal)

The Hungarian National Corpus and its Heti Világgazdaság (HVG) subcorpus provided the basis for corpus text selection: articles related to the topic of financially liable offences were selected and annotated for the categories person, organization, location and miscellaneous.
There are two annotated versions of the corpus. When preparing the tag-for-meaning annotation, our linguists took into consideration the context in which the Named Entity under investigation occurred, thus, it was not the primary sense of the Named Entity that determined the tag (e.g. Manchester=LOC) but its contextual reference (e.g. Manchester won the Premier League=ORG). As for tag-for-tag annotation, these cases were not differentiated: tags were always given on the basis of the primary sense.

Statistical data on Named Entities occurring in the corpus:

```
       | tag-for-meaning | tag-for-tag
------ | --------------- | -----------
non NE | 200067          | 	 
PER    | 8101            | 8121
ORG    | 8782            | 9480
LOC    | 5049            | 5391
MISC   | 1917            | 854
```

## Metadata

dataset_info:
- config_name: business
  features:
  - name: id
    dtype: string
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          0: O
          1: B-PER
          2: I-PER
          3: B-ORG
          4: I-ORG
          5: B-LOC
          6: I-LOC
          7: B-MISC
          8: I-MISC
  - name: document_id
    dtype: string
  - name: sentence_id
    dtype: string
  splits:
  - name: original
    num_bytes: 4452207
    num_examples: 9573
  - name: test
    num_bytes: 856798
    num_examples: 1915
  - name: train
    num_bytes: 3171931
    num_examples: 6701
  - name: validation
    num_bytes: 423478
    num_examples: 957
  download_size: 0
  dataset_size: 8904414
- config_name: criminal
  features:
  - name: id
    dtype: string
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          0: O
          1: B-PER
          2: I-PER
          3: B-ORG
          4: I-ORG
          5: B-LOC
          6: I-LOC
          7: B-MISC
          8: I-MISC
  - name: document_id
    dtype: string
  - name: sentence_id
    dtype: string
  splits:
  - name: original
    num_bytes: 2807970
    num_examples: 5375
  - name: test
    num_bytes: 520959
    num_examples: 1089
  - name: train
    num_bytes: 1989662
    num_examples: 3760
  - name: validation
    num_bytes: 297349
    num_examples: 526
  download_size: 0
  dataset_size: 5615940

