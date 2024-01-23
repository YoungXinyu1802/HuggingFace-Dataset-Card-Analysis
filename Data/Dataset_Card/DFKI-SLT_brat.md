---
annotations_creators:
- expert-generated
language_creators:
- found
license: []
task_categories:
- token-classification
task_ids:
- parsing
---

# Information Card for Brat

## Table of Contents
- [Description](#description)
  - [Summary](#summary)
 - [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-instances)
 - [Usage](#usage)
- [Additional Information](#additional-information)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)

## Description

- **Homepage:** https://brat.nlplab.org
- **Paper:** https://aclanthology.org/E12-2021/
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [Needs More Information]

### Summary

Brat is an intuitive web-based tool for text annotation supported by Natural Language Processing (NLP) technology. BRAT has been developed for rich structured annota- tion for a variety of NLP tasks and aims to support manual curation efforts and increase annotator productivity using NLP techniques. brat is designed in particular for structured annotation, where the notes are not free form text but have a fixed form that can be automatically processed and interpreted by a computer.


## Dataset Structure
Dataset annotated with brat format is processed using this script. Annotations created in brat are stored on disk in a standoff format: annotations are stored separately from the annotated document text, which is never modified by the tool. For each text document in the system, there is a corresponding annotation file. The two are associatied by the file naming convention that their base name (file name without suffix) is the same: for example, the file DOC-1000.ann contains annotations for the file DOC-1000.txt. More information can be found [here](https://brat.nlplab.org/standoff.html).
### Data Instances
[Needs More Information]
### Data Fields
```
-context: html content of data file as string
-file_name: a string name of file
-spans: a sequence containing id, type, location and text of a span
-relations: a sequence containing id, type and arguments of a relation
-equivalence_relations: 
-events:
-attributions:
-normalizations:
-notes:
```

### Usage

brat script can be used by calling `load_dataset()` method and passing `kwargs` (arguments to the [BuilderConfig](https://huggingface.co/docs/datasets/v2.2.1/en/package_reference/builder_classes#datasets.BuilderConfig)) which should include at least `url` of the dataset prepared using brat. We provide an example of [SciArg](https://aclanthology.org/W18-5206.pdf) dataset below,

```python
from datasets import load_dataset
kwargs = {
"description" :
  """This dataset is an extension of the Dr. Inventor corpus (Fisas et al., 2015, 2016) with an annotation layer containing
  fine-grained argumentative components and relations. It is the first argument-annotated corpus of scientific
  publications (in English), which allows for joint analyses of argumentation and other rhetorical dimensions of
  scientific writing.""",
"citation" :
  """@inproceedings{lauscher2018b,
    title = {An argument-annotated corpus of scientific publications},
    booktitle = {Proceedings of the 5th Workshop on Mining Argumentation},
    publisher = {Association for Computational Linguistics},
    author = {Lauscher, Anne and Glava\v{s}, Goran and Ponzetto, Simone Paolo},
    address = {Brussels, Belgium},
    year = {2018},
    pages = {40–46}
  }""",
"homepage": "https://github.com/anlausch/ArguminSci",
"url": "http://data.dws.informatik.uni-mannheim.de/sci-arg/compiled_corpus.zip",
"file_name_blacklist": ['A28'],
}

dataset = load_dataset('dfki-nlp/brat', **kwargs)
```

## Additional Information

### Licensing Information

[Needs More Information]

### Citation Information

```
@inproceedings{stenetorp-etal-2012-brat,
    title = "brat: a Web-based Tool for {NLP}-Assisted Text Annotation",
    author = "Stenetorp, Pontus  and
      Pyysalo, Sampo  and
      Topi{\'c}, Goran  and
      Ohta, Tomoko  and
      Ananiadou, Sophia  and
      Tsujii, Jun{'}ichi",
    booktitle = "Proceedings of the Demonstrations at the 13th Conference of the {E}uropean Chapter of the Association for Computational Linguistics",
    month = apr,
    year = "2012",
    address = "Avignon, France",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/E12-2021",
    pages = "102--107",
}
```