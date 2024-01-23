---
annotations_creators:
- machine-generated
language_creators:
- machine-generated
language:
- en
license:
- cc-by-sa-4.0
multilinguality:
- monolingual
pretty_name: wikitext_linked
size_categories:
- 1M<n<10M
source_datasets:
- extended|wikitext
task_categories:
- fill-mask
- token-classification
- text-classification
task_ids:
- masked-language-modeling
- named-entity-recognition
- part-of-speech
- lemmatization
- parsing
- entity-linking-classification
---

# Dataset Card for wikitext_linked

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Homepage:** -
- **Repository:** [https://github.com/GabrielKP/svo/](https://github.com/GabrielKP/svo/)
- **Paper:** -
- **Leaderboard:** -
- **Point of Contact:** [gabriel.kressin@dfki.de](mailto:gabriel.kressin@dfki.de)

### Dataset Summary

The WikiText language modeling dataset is a collection of over 100 million tokens extracted from
the set of verified Good and Featured articles on Wikipedia. Dependency Relations, POS, NER tags
are marked with [trankit](https://github.com/nlp-uoregon/trankit), entities are linked with
[entity-fishing](https://nerd.readthedocs.io/en/latest/index.html), which also tags another field
of NER tags. The dataset is available under the Creative Commons Attribution-ShareAlike License.

Compared to the preprocessed version of Penn Treebank (PTB), WikiText-2 is over 2 times larger and
WikiText-103 is over 110 times larger. The WikiText dataset also features a far larger vocabulary
and retains the original case, punctuation and numbers - all of which are removed in PTB. As it is
composed of full articles, the dataset is well suited for models that can take advantage of long
term dependencies.

### Supported Tasks and Leaderboards

- masked-language-modeling
- named-entity-recognition
- part-of-speech
- lemmatization
- parsing
- entity-linking-classification

### Languages

English.

## Dataset Structure

### Data Instances

#### wikitext2

- **Size of downloaded dataset files:** 27.3 MB
- **Size of the generated dataset:** 197.2 MB
- **Total amount of disk used:** 197.2 MB

An example of 'validation' looks as follows.
```json
{
    'text': 'It is closely related to the American lobster , H. americanus .',
    'original_id': 3,
    'tok_span': [[0, 0], [0, 2], [3, 5], [6, 13], [14, 21], [22, 24], [25, 28], [29, 37], [38, 45], [46, 47], [48, 50], [51, 61], [62, 63]],
    'tok_upos': ['root', 'PRON', 'AUX', 'ADV', 'ADJ', 'ADP', 'DET', 'ADJ', 'NOUN', 'PUNCT', 'PROPN', 'PROPN', 'PUNCT'],
    'tok_xpos': ['root', 'PRP', 'VBZ', 'RB', 'JJ', 'IN', 'DT', 'JJ', 'NN', ',', 'NNP', 'NNP', '.'],
    'tok_dephead': [0, 4, 4, 4, 0, 8, 8, 8, 4, 8, 8, 10, 4],
    'tok_deprel': ['root', 'nsubj', 'cop', 'advmod', 'root', 'case', 'det', 'amod', 'obl', 'punct', 'appos', 'flat', 'punct'],
    'tok_lemma': [None, 'it', 'be', 'closely', 'related', 'to', 'the', 'american', 'lobster', ',', 'H.', 'americanus', '.'],
    'tok_ner': [None, 'O', 'O', 'O', 'O', 'O', 'O', 'S-MISC', 'O', 'O', 'O', 'O', 'O'],
    'ent_span': [[29, 45]],
    'ent_wikipedia_external_ref': ['377397'],
    'ent_ner': [None],
    'ent_domains': [['Enterprise']],
}
```

#### wikitext103

- **Size of downloaded dataset files:** 1.11 GB
- **Size of the generated dataset:** 7.82 GB
- **Total amount of disk used:** 7.82 GB

An example of 'train' looks as follows.
```json
{
    'text': 'Vision for the PlayStation Portable .',
    'original_id': 3,
    'tok_span': [[0, 0], [0, 6], [7, 10], [11, 14], [15, 26], [27, 35], [36, 37]],
    'tok_upos': ['root', 'NOUN', 'ADP', 'DET', 'PROPN', 'PROPN', 'PUNCT'],
    'tok_xpos': ['root', 'NN', 'IN', 'DT', 'NNP', 'NNP', '.'],
    'tok_dephead': [0, 0, 5, 5, 5, 1, 1],
    'tok_deprel': ['root', 'root', 'case', 'det', 'compound', 'nmod', 'punct'],
    'tok_lemma': [None, 'vision', 'for', 'the', 'PlayStation', 'Portable', '.'],
    'tok_ner': [None, 'O', 'O', 'O', 'B-MISC', 'E-MISC', 'O'],
    'ent_span': [[15, 35]],
    'ent_wikipedia_external_ref': ['619009'],
    'ent_ner': [None],
    'ent_domains': [['Electronics', 'Computer_Science']]
}
```

Use following code to print the examples nicely:
```py
def print_tokens_entities(example):
    text = example['text']
    print(
        "Text:\n"
        f"   {text}"
        "\nOrig-Id: "
        f"{example['original_id']}"
        "\nTokens:"
    )
    iterator = enumerate(zip(
        example["tok_span"],
        example["tok_upos"],
        example["tok_xpos"],
        example["tok_ner"],
        example["tok_dephead"],
        example["tok_deprel"],
        example["tok_lemma"],
    ))
    print(f"    Id  | {'token':12} | {'upos':8} | {'xpos':8} | {'ner':8}  | {'deph':4} | {'deprel':9} | {'lemma':12} | Id")
    print("---------------------------------------------------------------------------------------------------")
    for idx, (tok_span, upos, xpos, ner, dephead, deprel, lemma) in iterator:
        print(f"    {idx:3} | {text[tok_span[0]:tok_span[1]]:12} | {upos:8} | {xpos:8} | {str(ner):8}  | {str(dephead):4} | {deprel:9} | {str(lemma):12} | {idx}")

    iterator = list(enumerate(zip(
        example.get("ent_span", []),
        example.get("ent_wikipedia_external_ref", []),
        example.get("ent_ner", []),
        example.get("ent_domains", []),
    )))
    if len(iterator) > 0:
        print("Entities")
        print(f"    Id  | {'entity':21} | {'wiki_ref':7} | {'ner':7} | domains")
        print("--------------------------------------------------------------------")
        for idx, ((start, end), wiki_ref, ent_ner, ent_domains) in iterator:
            print(f"    {idx:3} | {text[start:end]:21} | {str(wiki_ref):7} | {str(ent_ner):7} | {ent_domains}")
```

### Data Fields

The data fields are the same among all splits.

* text: string feature.
* original_id: int feature. Mapping to index within original wikitext dataset.
* tok_span: sequence of (int, int) tuples. Denotes token spans (start inclusive, end exclusive)
within each sentence.
**Note that each sentence includes an artificial root node to align dependency relations.**
* tok_upos: string feature. [Universal Dependency POS tag](https://universaldependencies.org/)
tags. Aligned with tok_span. Root node has tag "root".
* tok_xpos: string geature. [XPOS POS tag](https://trankit.readthedocs.io/en/latest/overview.html#token-list).
Aligned with tok_span. Root node has tag "root".
* tok_dephead: int feature.
[Universal Dependency Head Node](https://universaldependencies.org/introduction.html). Int refers
to tokens in tok_span. Root node has head `0` (itself).
* tok_deprel: [Universal Dependency Relation Description](https://universaldependencies.org/introduction.html).
Refers to the relation between this token and head token. Aligned with tok_span. Root node has
dependency relation "root" to itself.
* tok_lemma: string feature. Lemma of token. Aligend with tok_span.
* tok_ner: string feature. NER tag of token. Marked in BIOS schema (e.g. S-MISC, B-LOC, ...)
Aligned with tok_span. Root node has NER tag `None`.
* ent_span: sequence of (int, int) tuples. Denotes entities found by entity-fishing
(start inclusive, end exclusive).
* ent_wikipedia_external_ref: string feature. External Reference to wikipedia page. You can
access the wikipedia page via the url `https://en.wikipedia.org/wiki?curid=<ent_wikipedia_external_ref>`.
Aligend with ent_span. All entities either have this field, or the `ent_ner` field, but not both.
An empty field is denoted by the string `None`. Aligned with ent_span.
* ent_ner: string feature. Denotes NER tags. An empty field is denoted by the string `None`.
Aligned with ent_span.
"ent_domains": sequence of string. Denotes domains of entity. Can be empty sequence. Aligned with
ent_span.

### Data Splits

|       name        | train |validation| test|
|-------------------|------:|---------:|----:|
|wikitext103        |4076530|      8607|10062|
|wikitext2          |  82649|      8606|10062|

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

[https://huggingface.co/datasets/wikitext](https://huggingface.co/datasets/wikitext)

#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

1. Started with `wikitext2-raw-v1` and `wikitext103-raw-v1` from [wikitext](https://huggingface.co/datasets/wikitext)
2. Ran datasets through Trankit. Marked all fields starting with `tok`.

In this step, the texts have been split into sentences. To retain the original text sections
you can accumulate over `original_id` (examples are in order).

3. Ran datasets through entity-fishing. Marked all fields starting with `ent`.

#### Who are the annotators?

Machines powered by [DFKI](https://www.dfki.de/web).

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

[More Information Needed]

### Licensing Information

Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)

### Citation Information

Please cite the original creators of wikitext, and the great people
developing trankit and entity-fishing.
```
@misc{merity2016pointer,
      title={Pointer Sentinel Mixture Models},
      author={Stephen Merity and Caiming Xiong and James Bradbury and Richard Socher},
      year={2016},
      eprint={1609.07843},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}

@inproceedings{nguyen2021trankit,
      title={Trankit: A Light-Weight Transformer-based Toolkit for Multilingual Natural Language Processing},
      author={Nguyen, Minh Van and Lai, Viet Dac and Veyseh, Amir Pouran Ben and Nguyen, Thien Huu},
      booktitle="Proceedings of the 16th Conference of the European Chapter of the Association for Computational Linguistics: System Demonstrations",
      year={2021}
}

@misc{entity-fishing,
    title = {entity-fishing},
    howpublished = {\\url{https://github.com/kermitt2/entity-fishing}},
    publisher = {GitHub},
    year = {2016--2022},
    archivePrefix = {swh},
    eprint = {1:dir:cb0ba3379413db12b0018b7c3af8d0d2d864139c}
}
```

### Contributions

Thanks to [@GabrielKP](https://github.com/GabrielKP) for adding this dataset.
