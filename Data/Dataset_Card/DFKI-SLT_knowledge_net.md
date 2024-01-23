---
annotations_creators:
- expert-generated
language:
- en
language_creators:
- found
license: []
multilinguality:
- monolingual
pretty_name: KnowledgeNet is a dataset for automatically populating a knowledge base
size_categories:
- 10K<n<100K
source_datasets: []
tags:
- knowledgenet
task_categories:
- text-classification
task_ids:
- multi-class-classification
- entity-linking-classification
dataset_info:
- config_name: knet
  features:
  - name: fold
    dtype: int32
  - name: documentId
    dtype: string
  - name: source
    dtype: string
  - name: documentText
    dtype: string
  - name: passages
    sequence:
    - name: passageId
      dtype: string
    - name: passageStart
      dtype: int32
    - name: passageEnd
      dtype: int32
    - name: passageText
      dtype: string
    - name: exhaustivelyAnnotatedProperties
      sequence:
      - name: propertyId
        dtype: string
      - name: propertyName
        dtype: string
      - name: propertyDescription
        dtype: string
    - name: facts
      sequence:
      - name: factId
        dtype: string
      - name: propertyId
        dtype: string
      - name: humanReadable
        dtype: string
      - name: annotatedPassage
        dtype: string
      - name: subjectStart
        dtype: int32
      - name: subjectEnd
        dtype: int32
      - name: subjectText
        dtype: string
      - name: subjectUri
        dtype: string
      - name: objectStart
        dtype: int32
      - name: objectEnd
        dtype: int32
      - name: objectText
        dtype: string
      - name: objectUri
        dtype: string
  splits:
  - name: train
    num_bytes: 10161415
    num_examples: 3977
  download_size: 14119313
  dataset_size: 10161415
- config_name: knet_tokenized
  features:
  - name: doc_id
    dtype: string
  - name: passage_id
    dtype: string
  - name: fact_id
    dtype: string
  - name: tokens
    sequence: string
  - name: subj_start
    dtype: int32
  - name: subj_end
    dtype: int32
  - name: subj_type
    dtype:
      class_label:
        names:
          '0': O
          '1': PER
          '2': ORG
          '3': LOC
          '4': DATE
  - name: subj_uri
    dtype: string
  - name: obj_start
    dtype: int32
  - name: obj_end
    dtype: int32
  - name: obj_type
    dtype:
      class_label:
        names:
          '0': O
          '1': PER
          '2': ORG
          '3': LOC
          '4': DATE
  - name: obj_uri
    dtype: string
  - name: relation
    dtype:
      class_label:
        names:
          '0': NO_RELATION
          '1': DATE_OF_BIRTH
          '2': DATE_OF_DEATH
          '3': PLACE_OF_RESIDENCE
          '4': PLACE_OF_BIRTH
          '5': NATIONALITY
          '6': EMPLOYEE_OR_MEMBER_OF
          '7': EDUCATED_AT
          '8': POLITICAL_AFFILIATION
          '9': CHILD_OF
          '10': SPOUSE
          '11': DATE_FOUNDED
          '12': HEADQUARTERS
          '13': SUBSIDIARY_OF
          '14': FOUNDED_BY
          '15': CEO
  splits:
  - name: train
    num_bytes: 4511963
    num_examples: 10895
  download_size: 14119313
  dataset_size: 4511963
- config_name: knet_re
  features:
  - name: documentId
    dtype: string
  - name: passageId
    dtype: string
  - name: factId
    dtype: string
  - name: passageText
    dtype: string
  - name: humanReadable
    dtype: string
  - name: annotatedPassage
    dtype: string
  - name: subjectStart
    dtype: int32
  - name: subjectEnd
    dtype: int32
  - name: subjectText
    dtype: string
  - name: subjectType
    dtype:
      class_label:
        names:
          '0': O
          '1': PER
          '2': ORG
          '3': LOC
          '4': DATE
  - name: subjectUri
    dtype: string
  - name: objectStart
    dtype: int32
  - name: objectEnd
    dtype: int32
  - name: objectText
    dtype: string
  - name: objectType
    dtype:
      class_label:
        names:
          '0': O
          '1': PER
          '2': ORG
          '3': LOC
          '4': DATE
  - name: objectUri
    dtype: string
  - name: relation
    dtype:
      class_label:
        names:
          '0': NO_RELATION
          '1': DATE_OF_BIRTH
          '2': DATE_OF_DEATH
          '3': PLACE_OF_RESIDENCE
          '4': PLACE_OF_BIRTH
          '5': NATIONALITY
          '6': EMPLOYEE_OR_MEMBER_OF
          '7': EDUCATED_AT
          '8': POLITICAL_AFFILIATION
          '9': CHILD_OF
          '10': SPOUSE
          '11': DATE_FOUNDED
          '12': HEADQUARTERS
          '13': SUBSIDIARY_OF
          '14': FOUNDED_BY
          '15': CEO
  splits:
  - name: train
    num_bytes: 6098219
    num_examples: 10895
  download_size: 14119313
  dataset_size: 6098219
---
# Dataset Card for "KnowledgeNet"
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
- **Repository:** [knowledge-net](https://github.com/diffbot/knowledge-net)
- **Paper:** [KnowledgeNet: A Benchmark Dataset for Knowledge Base Population](https://aclanthology.org/D19-1069/)
- **Size of downloaded dataset files:** 12.59 MB
- **Size of the generated dataset:** 6.1 MB
### Dataset Summary
KnowledgeNet is a benchmark dataset for the task of automatically populating a knowledge base (Wikidata) with facts 
expressed in natural language text on the web. KnowledgeNet provides text exhaustively annotated with facts, thus 
enabling the holistic end-to-end evaluation of knowledge base population systems as a whole, unlike previous benchmarks 
that are more suitable for the evaluation of individual subcomponents (e.g., entity linking, relation extraction).

For instance, the dataset contains text expressing the fact (Gennaro Basile; RESIDENCE; Moravia), in the passage: 
"Gennaro Basile was an Italian painter, born in Naples but active in the German-speaking countries. He settled at Brünn, 
in Moravia, and lived about 1756..."

For a description of the dataset and baseline systems, please refer to their 
[EMNLP paper](https://github.com/diffbot/knowledge-net/blob/master/knowledgenet-emnlp-cameraready.pdf).

Note: This Datasetreader currently only supports the `train` split and does not contain negative examples.
In addition to the original format this repository also provides two version (`knet_re`, `knet_tokenized`) that are 
easier to use for simple relation extraction. You can load them with 
`datasets.load_dataset("DFKI-SLT/knowledge_net", name="<config>")`.

### Supported Tasks and Leaderboards
[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Languages
The language in the dataset is English.

## Dataset Structure
### Data Instances
#### knet
- **Size of downloaded dataset files:** 12.59 MB
- **Size of the generated dataset:** 10.16 MB

An example of 'train' looks as follows:
```json
{
  "fold": 2,
  "documentId": "8313",
  "source": "DBpedia Abstract",
  "documentText": "Gennaro Basile\n\nGennaro Basile was an Italian painter, born in Naples but active in the German-speaking countries. He settled at Brünn, in Moravia, and lived about 1756. His best picture is the altar-piece in the chapel of the chateau at Seeberg, in Salzburg. Most of his works remained in Moravia.",
  "passages": [
    {
      "passageId": "8313:16:114",
      "passageStart": 16,
      "passageEnd": 114,
      "passageText": "Gennaro Basile was an Italian painter, born in Naples but active in the German-speaking countries.",
      "exhaustivelyAnnotatedProperties": [
        {          
          "propertyId": "12",
          "propertyName": "PLACE_OF_BIRTH",
          "propertyDescription": "Describes the relationship between a person and the location where she/he was born."
        }
      ],
      "facts": [
        {
          "factId": "8313:16:30:63:69:12",
          "propertyId": "12",
          "humanReadable": "<Gennaro Basile> <PLACE_OF_BIRTH> <Naples>",
          "annotatedPassage": "<Gennaro Basile> was an Italian painter, born in <Naples> but active in the German-speaking countries.",
          "subjectStart": 16,
          "subjectEnd": 30,
          "subjectText": "Gennaro Basile",
          "subjectUri": "http://www.wikidata.org/entity/Q19517888",
          "objectStart": 63,
          "objectEnd": 69,
          "objectText": "Naples",
          "objectUri": "http://www.wikidata.org/entity/Q2634"
        }
      ]
    },
    {
      "passageId": "8313:115:169",
      "passageStart": 115,
      "passageEnd": 169,
      "passageText": "He settled at Brünn, in Moravia, and lived about 1756.",
      "exhaustivelyAnnotatedProperties": [
        {
          "propertyId": "11",
          "propertyName": "PLACE_OF_RESIDENCE",
          "propertyDescription": "Describes the relationship between a person and the location where she/he lives/lived."
        },
        {
          "propertyId": "12",
          "propertyName": "PLACE_OF_BIRTH",
          "propertyDescription": "Describes the relationship between a person and the location where she/he was born."
        }
      ],
      "facts": [
        {
          "factId": "8313:115:117:129:134:11",
          "propertyId": "11",
          "humanReadable": "<He> <PLACE_OF_RESIDENCE> <Brünn>",
          "annotatedPassage": "<He> settled at <Brünn>, in Moravia, and lived about 1756.",
          "subjectStart": 115,
          "subjectEnd": 117,
          "subjectText": "He",
          "subjectUri": "http://www.wikidata.org/entity/Q19517888",
          "objectStart": 129,
          "objectEnd": 134,
          "objectText": "Brünn",
          "objectUri": "http://www.wikidata.org/entity/Q14960"
        },
        {
          "factId": "8313:115:117:139:146:11",
          "propertyId": "11",
          "humanReadable": "<He> <PLACE_OF_RESIDENCE> <Moravia>",
          "annotatedPassage": "<He> settled at Brünn, in <Moravia>, and lived about 1756.",
          "subjectStart": 115,
          "subjectEnd": 117,
          "subjectText": "He",
          "subjectUri": "http://www.wikidata.org/entity/Q19517888",
          "objectStart": 139,
          "objectEnd": 146,
          "objectText": "Moravia",
          "objectUri": "http://www.wikidata.org/entity/Q43266"
        }
      ]
    }
  ]
}
```

#### knet_re
- **Size of downloaded dataset files:** 12.59 MB
- **Size of the generated dataset:** 6.1 MB

An example of 'train' looks as follows:
```json
{
  "documentId": "7", 
  "passageId": "7:23:206", 
  "factId": "7:23:44:138:160:1", 
  "passageText": "Tata Chemicals Europe (formerly Brunner Mond (UK) Limited) is a UK-based chemicals company that is a subsidiary of Tata Chemicals Limited, itself a part of the India-based Tata Group.", 
  "humanReadable": "<Tata Chemicals Europe> <SUBSIDIARY_OF> <Tata Chemicals Limited>", 
  "annotatedPassage": "<Tata Chemicals Europe> (formerly Brunner Mond (UK) Limited) is a UK-based chemicals company that is a subsidiary of <Tata Chemicals Limited>, itself a part of the India-based Tata Group.", 
  "subjectStart": 0, 
  "subjectEnd": 21, 
  "subjectText": "Tata Chemicals Europe", 
  "subjectType": 2, 
  "subjectUri": "", 
  "objectStart": 115, 
  "objectEnd": 137, 
  "objectText": "Tata Chemicals Limited", 
  "objectType": 2, 
  "objectUri": "http://www.wikidata.org/entity/Q2331365", 
  "relation": 13
}
```

#### knet_tokenized
- **Size of downloaded dataset files:** 12.59 MB
- **Size of the generated dataset:** 4.5 MB

An example of 'train' looks as follows:
```json
{
  "doc_id": "7", 
  "passage_id": "7:23:206", 
  "fact_id": "7:162:168:183:205:1", 
  "tokens": ["Tata", "Chemicals", "Europe", "(", "formerly", "Brunner", "Mond", "(", "UK", ")", "Limited", ")", "is", "a", "UK", "-", "based", "chemicals", "company", "that", "is", "a", "subsidiary", "of", "Tata", "Chemicals", "Limited", ",", "itself", "a", "part", "of", "the", "India", "-", "based", "Tata", "Group", "."], 
  "subj_start": 28, 
  "subj_end": 29, 
  "subj_type": 2, 
  "subj_uri": "http://www.wikidata.org/entity/Q2331365", 
  "obj_start": 33, 
  "obj_end": 38, 
  "obj_type": 2, 
  "obj_uri": "http://www.wikidata.org/entity/Q331715", 
  "relation": 13
}
```
### Data Fields

#### knet
- `fold`: the fold, a `int` feature.
- `documentId`: the document id, a `string` feature.
- `source`: the source, a `string` feature.
- `documenText`: the document text, a `string` feature.
- `passages`: the list of passages, a `list` of `dict`.
  - `passageId`: the passage id, a `string` feature.
  - `passageStart`: the passage start, a `int` feature.
  - `passageEnd`: the passage end, a `int` feature.
  - `passageText`: the passage text, a `string` feature.
  - `exhaustivelyAnnotatedProperties`: the list of exhaustively annotated properties, a `list` of `dict`.
    - `propertyId`: the property id, a `string` feature.
    - `propertyName`: the property name, a `string` feature.
    - `propertyDescription`: the property description, a `string` feature.
  - `facts`: the list of facts, a `list` of `dict`.
    - `factId`: the fact id, a `string` feature.
    - `propertyId`: the property id, a `string` feature.
    - `humanReadable`: the human readable annotation, a `string` feature.
    - `annotatedPassage`: the annotated passage, a `string` feature.
    - `subjectStart`: the subject start, a `int` feature.
    - `subjectEnd`: the subject end, a `int` feature.
    - `subjectText`: the subject text, a `string` feature.
    - `subjectUri`: the subject uri, a `string` feature.
    - `objectStart`: the object start, a `int` feature.
    - `objectEnd`: the object end, a `int` feature.
    - `objectText`: the object text, a `string` feature.
    - `objectUri`: the object uri, a `string` feature.

#### knet_re
- `documentId`: the document id, a `string` feature.
- `passageId`: the passage id, a `string` feature.
- `passageText`: the passage text, a `string` feature.
- `factId`: the fact id, a `string` feature.
- `humanReadable`: human-readable annotation, a `string` features.
- `annotatedPassage`: annotated passage, a `string` feature.
- `subjectStart`: the index of the start character of the relation subject mention, an `ìnt` feature.
- `subjectEnd`: the index of the end character of the relation subject mention, exclusive, an `ìnt` feature.
- `subjectText`: the text the subject mention, a `string` feature.
- `subjectType`: the NER type of the subject mention, a `string` classification label.

```json
{"O": 0, "PER": 1, "ORG": 2, "LOC": 3, "DATE": 4}
```

- `subjectUri`: the Wikidata URI of the subject mention, a `string` feature.
- `objectStart`: the index of the start character of the relation object mention, an `ìnt` feature.
- `objectEnd`: the index of the end character of the relation object mention, exclusive, an `ìnt` feature.
- `objectText`: the text the object mention, a `string` feature.
- `objectType`: the NER type of the object mention, a `string` classification label.

```json
{"O": 0, "PER": 1, "ORG": 2, "LOC": 3, "DATE": 4}
```

- `objectUri`: the Wikidata URI of the object mention, a `string` feature.
- `relation`: the relation label of this instance, a `string` classification label.

```json
{"NO_RELATION": 0, "DATE_OF_BIRTH": 1, "DATE_OF_DEATH": 2, "PLACE_OF_RESIDENCE": 3, "PLACE_OF_BIRTH": 4, "NATIONALITY": 5, "EMPLOYEE_OR_MEMBER_OF": 6, "EDUCATED_AT": 7, "POLITICAL_AFFILIATION": 8, "CHILD_OF": 9, "SPOUSE": 10, "DATE_FOUNDED": 11, "HEADQUARTERS": 12, "SUBSIDIARY_OF": 13, "FOUNDED_BY": 14, "CEO": 15}
```

#### knet_tokenized
- `doc_id`: the document id, a `string` feature.
- `passage_id`: the passage id, a `string` feature.
- `factId`: the fact id, a `string` feature.
- `tokens`: the list of tokens of this passage, obtained with spaCy, a `list` of `string` features.
- `subj_start`: the index of the start token of the relation subject mention, an `ìnt` feature.
- `subj_end`: the index of the end token of the relation subject mention, exclusive, an `ìnt` feature.
- `subj_type`: the NER type of the subject mention, a `string` classification label.

```json
{"O": 0, "PER": 1, "ORG": 2, "LOC": 3, "DATE": 4}
```


- `subj_uri`: the Wikidata URI of the subject mention, a `string` feature.
- `obj_start`: the index of the start token of the relation object mention, an `ìnt` feature.
- `obj_end`: the index of the end token of the relation object mention, exclusive, an `ìnt` feature.
- `obj_type`: the NER type of the object mention, a `string` classification label.

```json
{"O": 0, "PER": 1, "ORG": 2, "LOC": 3, "DATE": 4}
```

- `obj_uri`: the Wikidata URI of the object mention, a `string` feature.
- `relation`: the relation label of this instance, a `string` classification label.

```json
{"NO_RELATION": 0, "DATE_OF_BIRTH": 1, "DATE_OF_DEATH": 2, "PLACE_OF_RESIDENCE": 3, "PLACE_OF_BIRTH": 4, "NATIONALITY": 5, "EMPLOYEE_OR_MEMBER_OF": 6, "EDUCATED_AT": 7, "POLITICAL_AFFILIATION": 8, "CHILD_OF": 9, "SPOUSE": 10, "DATE_FOUNDED": 11, "HEADQUARTERS": 12, "SUBSIDIARY_OF": 13, "FOUNDED_BY": 14, "CEO": 15}
```


### Data Splits
[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
## Dataset Creation
### Curation Rationale
[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
### Source Data
#### Initial Data Collection and Normalization
[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
#### Who are the source language producers?
[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
### Annotations
#### Annotation process
[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
are labeled as no_relation.
[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
### Personal and Sensitive Information
[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
## Considerations for Using the Data
### Social Impact of Dataset
[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
### Discussion of Biases
[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
### Other Known Limitations
[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
## Additional Information
### Dataset Curators
[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
### Licensing Information
[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
### Citation Information
```
@inproceedings{mesquita-etal-2019-knowledgenet,
    title = "{K}nowledge{N}et: A Benchmark Dataset for Knowledge Base Population",
    author = "Mesquita, Filipe  and
      Cannaviccio, Matteo  and
      Schmidek, Jordan  and
      Mirza, Paramita  and
      Barbosa, Denilson",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)",
    month = nov,
    year = "2019",
    address = "Hong Kong, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/D19-1069",
    doi = "10.18653/v1/D19-1069",
    pages = "749--758",}
```

### Contributions
Thanks to [@phucdev](https://github.com/phucdev) for adding this dataset.