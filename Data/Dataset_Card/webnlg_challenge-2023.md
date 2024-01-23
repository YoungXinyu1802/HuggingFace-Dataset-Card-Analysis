---
annotations_creators:
- found
language_creators:
- crowdsourced
language:
- br
- cy
- ga
- mt
- ru
license:
- cc-by-sa-3.0
- cc-by-nc-sa-4.0
- gfdl
multilinguality:
- multilingual
size_categories:
- 10K<n<100K
source_datasets:
- extended|other-db_pedia
- original
task_categories:
- tabular-to-text
task_ids:
- rdf-to-text
paperswithcode_id: null
pretty_name: WebNLG 2023 challenge
dataset_info:
- config_name: br
  features:
  - name: category
    dtype: string
  - name: size
    dtype: int32
  - name: eid
    dtype: string
  - name: original_triple_sets
    sequence:
    - name: otriple_set
      sequence: string
  - name: modified_triple_sets
    sequence:
    - name: mtriple_set
      sequence: string
  - name: shape
    dtype: string
  - name: shape_type
    dtype: string
  - name: lex
    sequence:
    - name: comment
      dtype: string
    - name: lid
      dtype: string
    - name: text
      dtype: string
    - name: lang
      dtype: string
  splits:
  - name: train
    num_bytes: 14841422
    num_examples: 13211
  - name: validation
    num_bytes: 1394620
    num_examples: 1399
  download_size: 10954332
  dataset_size: 16236042
- config_name: cy
  features:
  - name: category
    dtype: string
  - name: size
    dtype: int32
  - name: eid
    dtype: string
  - name: original_triple_sets
    sequence:
    - name: otriple_set
      sequence: string
  - name: modified_triple_sets
    sequence:
    - name: mtriple_set
      sequence: string
  - name: shape
    dtype: string
  - name: shape_type
    dtype: string
  - name: lex
    sequence:
    - name: comment
      dtype: string
    - name: lid
      dtype: string
    - name: text
      dtype: string
    - name: lang
      dtype: string
  splits:
  - name: train
    num_bytes: 15070109
    num_examples: 13211
  - name: validation
    num_bytes: 1605315
    num_examples: 1665
  download_size: 10954332
  dataset_size: 16675424
- config_name: ga
  features:
  - name: category
    dtype: string
  - name: size
    dtype: int32
  - name: eid
    dtype: string
  - name: original_triple_sets
    sequence:
    - name: otriple_set
      sequence: string
  - name: modified_triple_sets
    sequence:
    - name: mtriple_set
      sequence: string
  - name: shape
    dtype: string
  - name: shape_type
    dtype: string
  - name: lex
    sequence:
    - name: comment
      dtype: string
    - name: lid
      dtype: string
    - name: text
      dtype: string
    - name: lang
      dtype: string
  splits:
  - name: train
    num_bytes: 15219249
    num_examples: 13211
  - name: validation
    num_bytes: 1621527
    num_examples: 1665
  download_size: 10954332
  dataset_size: 16840776
- config_name: mt
  features:
  - name: category
    dtype: string
  - name: size
    dtype: int32
  - name: eid
    dtype: string
  - name: original_triple_sets
    sequence:
    - name: otriple_set
      sequence: string
  - name: modified_triple_sets
    sequence:
    - name: mtriple_set
      sequence: string
  - name: shape
    dtype: string
  - name: shape_type
    dtype: string
  - name: lex
    sequence:
    - name: comment
      dtype: string
    - name: lid
      dtype: string
    - name: text
      dtype: string
    - name: lang
      dtype: string
  splits:
  - name: train
    num_bytes: 15281045
    num_examples: 13211
  - name: validation
    num_bytes: 1611988
    num_examples: 1665
  download_size: 10954332
  dataset_size: 16893033
- config_name: ru
  features:
  - name: category
    dtype: string
  - name: size
    dtype: int32
  - name: eid
    dtype: string
  - name: original_triple_sets
    sequence:
    - name: otriple_set
      sequence: string
  - name: modified_triple_sets
    sequence:
    - name: mtriple_set
      sequence: string
  - name: shape
    dtype: string
  - name: shape_type
    dtype: string
  - name: lex
    sequence:
    - name: comment
      dtype: string
    - name: lid
      dtype: string
    - name: text
      dtype: string
    - name: lang
      dtype: string
  splits:
  - name: train
    num_bytes: 8145815
    num_examples: 5573
  - name: validation
    num_bytes: 1122090
    num_examples: 790
  download_size: 10954332
  dataset_size: 9267905
---

# Dataset Card for WebNLG

## Table of Contents
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

- **Homepage:** [WebNLG 2023 challenge](https://synalp.gitlabpages.inria.fr/webnlg-challenge/challenge_2023/)
- **Repository:** [GitHub repository](https://github.com/WebNLG/2023-Challenge)
- **Paper:**
- **Leaderboard:**
- **Point of Contact:** [webnlg-challenge@inria.fr](mailto:webnlg-challenge@inria.fr)

### Dataset Summary

The WebNLG 2023 challenge focuses on four under-resourced languages which are severely under-represented in research on
text generation, namely Maltese, Irish, Breton and Welsh. In addition, WebNLG 2023 once again includes Russian, which
was first featured in WebNLG 2020.

The challenge focuses on RDF-to-text generation, similarly to WebNLG 2017 but targeting Breton, Irish, Maltese, Welsh,
and Russian;

The challenge consists in mapping data to text. The training data consists of Data/Text pairs where the data is a set of
triples extracted from DBpedia and the text is a verbalisation of these triples. 

For instance, given the 4 RDF triples:
```
<entry category="Company" eid="Id21" shape="(X (X) (X) (X) (X))" shape_type="sibling" size="4">
    <modifiedtripleset>
        <mtriple>Trane | foundingDate | 1913-01-01</mtriple>
        <mtriple>Trane | location | Ireland</mtriple>
        <mtriple>Trane | foundationPlace | La_Crosse,_Wisconsin</mtriple>
        <mtriple>Trane | numberOfEmployees | 29000</mtriple>
    </modifiedtripleset>
</entry>
```
the aim is to generate a text such as (English text):
```
Trane, which was founded on January 1st 1913 in La Crosse, Wisconsin, is based in Ireland. It has 29,000 employees.
```
or (Russian text):
```
Компания "Тране", основанная 1 января 1913 года в Ла-Кроссе в штате Висконсин, находится в Ирландии. В компании работают 29 тысяч человек.
```

As the example illustrates, the task involves specific NLG subtasks such as sentence segmentation
(how to chunk the input data into sentences), lexicalisation (of the DBpedia properties),
aggregation (how to avoid repetitions) and surface realisation
(how to build a syntactically correct and natural sounding text).

### Supported Tasks and Leaderboards

The dataset supports a Structured to Text task which requires a model takes a set of RDF (Resource Description Format)
triples from a database (DBpedia) of the form (subject, property, object) as input and write out a natural language
sentence expressing the information contained in the triples. 

The dataset is used in the [WebNLG 2023](https://synalp.gitlabpages.inria.fr/webnlg-challenge/challenge_2023/)
challenge. 

Results are evaluated with automatic metrics: [BLEU](https://huggingface.co/metrics/bleu),
[METEOR](https://huggingface.co/metrics/meteor), [ChrF++](https://huggingface.co/metrics/chrf),
[TER](https://huggingface.co/metrics/ter) and [BERTscore](https://huggingface.co/metrics/bertscore).
Additionally, result are assessed according to criteria such as grammaticality/correctness, appropriateness/adequacy,
fluency/naturalness, etc., by native speakers.

### Languages

The dataset comprises Breton (`br`), Welsh (`cy`), Irish (`ga`), Maltese (`mt`) and Russian (`ru`) languages.

## Dataset Structure

### Data Instances

A typical example contains the original RDF triples in the set, a modified version which presented to crowd workers,
and a set of possible verbalizations for this set of triples:
```
{'category': 'Airport',
 'size': 1,
 'eid': '1',
 'original_triple_sets': {'otriple_set': [['Aarhus_Airport | cityServed | "Aarhus, Denmark"@en']]},
 'modified_triple_sets': {'mtriple_set': [['Aarhus_Airport | cityServed | "Aarhus, Denmark"']]},
 'shape': '(X (X))',
 'shape_type': 'NA',
 'lex': {'comment': ['good', 'good', '', ''],
  'lid': ['Id1', 'Id2', 'Id3', 'Id3'],
  'text': ['Aarhus a zo an aro-vezh Aarhus.',
   "Aarhus a servijit ar c'hêr Aarhus.",
   'The Aarhus is the airport of Aarhus, Denmark.',
   'Aarhus Airport serves the city of Aarhus, Denmark.'],
  'lang': ['br', 'br', 'en', 'en']}}
```

### Data Fields

The following fields can be found in the instances:
- `category`: the category of the DBpedia entities present in the RDF triples.
- `eid`: an example ID, only unique per split per category.
- `size`: number of RDF triples in the set.
- `shape`: (since v2) Each set of RDF-triples is a tree, which is characterised by its shape and shape type. `shape` is a string representation of the tree with nested parentheses where X is a node (see [Newick tree format](https://en.wikipedia.org/wiki/Newick_format))
- `shape_type`: (since v2) is a type of the tree shape, which can be: `chain` (the object of one triple is the subject of the other); `sibling` (triples with a shared subject); `mixed` (both chain and sibling types present).
- `test_category`: (for `webnlg_challenge_2017` and `v3`) tells whether the set of RDF triples was present in the training set or not. Several splits of the test set are available: with and without references, and for RDF-to-text generation / for semantic parsing.
- `lex`: the lexicalizations, with:
  - `text`: the text to be predicted.
  - `lid`: a lexicalization ID, unique per example.
  - `comment`: the lexicalizations were rated by crowd workers are either `good` or `bad`
  - `lang`: (for `release_v3.0_ru`) the language used because original English texts were kept in the Russian version.

### Data Splits

The dataset is split into train and validation:

| language | train | validation |
|----------|------:|-----------:|
| br       | 13211 |       1399 |
| cy       | 13211 |       1665 |
| ga       | 13211 |       1665 |
| mt       | 13211 |       1665 |
| ru       |  5573 |        790 |

## Dataset Creation

### Curation Rationale

The WebNLG dataset was created to promote the development _(i)_ of RDF verbalisers and _(ii)_ of microplanners able to handle a wide range of linguistic constructions. The dataset aims at covering knowledge in different domains ("categories"). The same properties and entities can appear in several categories.

### Source Data

The data was compiled from raw DBpedia triples. [This paper](https://www.aclweb.org/anthology/C16-1141/) explains how the triples were selected.

#### Initial Data Collection and Normalization

Initial triples extracted from DBpedia were modified in several ways. See [official documentation](https://webnlg-challenge.loria.fr/docs/) for the most frequent changes that have been made. An original tripleset and a modified tripleset usually represent a one-to-one mapping. However, there are cases with many-to-one mappings when several original triplesets are mapped to one modified tripleset.

Entities that served as roots of RDF trees are listed in [this file](https://gitlab.com/shimorina/webnlg-dataset/-/blob/master/supplementary/entities_dict.json).

The English WebNLG 2020 dataset (v3.0) for training comprises data-text pairs for 16 distinct DBpedia categories:
- The 10 seen categories used in the 2017 version: Airport, Astronaut, Building, City, ComicsCharacter, Food, Monument, SportsTeam, University, and WrittenWork.
- The 5 unseen categories of 2017, which are now part of the seen data: Athlete, Artist, CelestialBody, MeanOfTransportation, Politician.
- 1 new category: Company.

The Russian dataset (v3.0) comprises data-text pairs for 9 distinct categories: Airport, Astronaut, Building, CelestialBody, ComicsCharacter, Food, Monument, SportsTeam, and University.

#### Who are the source language producers?

There are no source texts, all textual material was compiled during the annotation process.

### Annotations

#### Annotation process

Annotators were first asked to create sentences that verbalise single triples. In a second round, annotators were asked to combine single-triple sentences together into sentences that cover 2 triples. And so on until 7 triples. Quality checks were performed to ensure the quality of the annotations. See Section 3.3 in [the dataset paper](https://www.aclweb.org/anthology/P17-1017.pdf).

Russian data was translated from English with an MT system and then was post-edited by crowdworkers. See Section 2.2 of [this paper](https://webnlg-challenge.loria.fr/files/2020.webnlg-papers.7.pdf).

#### Who are the annotators?

All references were collected through crowdsourcing platforms (CrowdFlower/Figure 8 and Amazon Mechanical Turk). For Russian, post-editing was done using the Yandex.Toloka crowdsourcing platform.

### Personal and Sensitive Information

Neither the dataset as published or the annotation process involves the collection or sharing of any kind of personal / demographic information.

## Considerations for Using the Data

### Social Impact of Dataset

We do not foresee any negative social impact in particular from this dataset or task.

Positive outlooks: Being able to generate good quality text from RDF data would permit, e.g., making this data more accessible to lay users, enriching existing text with information drawn from knowledge bases such as DBpedia or describing, comparing and relating entities present in these knowledge bases.

### Discussion of Biases

This dataset is created using DBpedia RDF triples which naturally exhibit biases that have been found to exist in Wikipedia such as some forms of, e.g., gender bias.

The choice of [entities](https://gitlab.com/shimorina/webnlg-dataset/-/blob/master/supplementary/entities_dict.json), described by RDF trees, was not controlled. As such, they may contain gender biases; for instance, all the astronauts described by RDF triples are male. Hence, in texts, pronouns _he/him/his_ occur more often. Similarly, entities can be related to the Western culture more often than to other cultures.

### Other Known Limitations

The quality of the crowdsourced references is limited, in particular in terms of fluency/naturalness of the collected texts.

Russian data was machine-translated and then post-edited by crowdworkers, so some examples may still exhibit issues related to bad translations.

## Additional Information

### Dataset Curators

The principle curator of the dataset is Anastasia Shimorina (Université de Lorraine / LORIA, France). Throughout the WebNLG releases, several people contributed to their construction: Claire Gardent (CNRS / LORIA, France), Shashi Narayan (Google, UK), Laura Perez-Beltrachini (University of Edinburgh, UK), Elena Khasanova, and Thiago Castro Ferreira (Federal University of Minas Gerais, Brazil).
The dataset construction was funded by the French National Research Agency (ANR).

### Licensing Information

The dataset uses the `cc-by-nc-sa-4.0` license. The source DBpedia project uses the `cc-by-sa-3.0` and `gfdl-1.1` licenses.

### Citation Information

If you use the WebNLG corpus, cite:
```
@inproceedings{web_nlg,
  author    = {Claire Gardent and
               Anastasia Shimorina and
               Shashi Narayan and
               Laura Perez{-}Beltrachini},
  editor    = {Regina Barzilay and
               Min{-}Yen Kan},
  title     = {Creating Training Corpora for {NLG} Micro-Planners},
  booktitle = {Proceedings of the 55th Annual Meeting of the Association for Computational
               Linguistics, {ACL} 2017, Vancouver, Canada, July 30 - August 4, Volume
               1: Long Papers},
  pages     = {179--188},
  publisher = {Association for Computational Linguistics},
  year      = {2017},
  url       = {https://doi.org/10.18653/v1/P17-1017},
  doi       = {10.18653/v1/P17-1017}
}
```

### Contributions

Thanks to [@albertvillanova](https://huggingface.co/albertvillanova) for adding this dataset.