---
annotations_creators:
- machine-generated
language:
- en
language_creators:
- machine-generated
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: Machine Paraphrase Dataset (SpinnerChief/SpinBot)
size_categories:
- 100K<n<1M
source_datasets:
- original
tags:
- spinbot
- spinnerchief
- plagiarism
- paraphrase
- academic integrity
- arxiv
- wikipedia
- theses
task_categories:
- text-classification
- text-generation
task_ids: []
paperswithcode_id: identifying-machine-paraphrased-plagiarism
dataset_info:
- split: train
  download_size: 393224
  dataset_size: 393224
- split: test
  download_size: 655376
  dataset_size: 655376
---

# Dataset Card for Machine Paraphrase Dataset (MPC)

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

- **Repository:** https://github.com/jpwahle/iconf22-paraphrase
- **Paper:** https://link.springer.com/chapter/10.1007/978-3-030-96957-8_34
- **Total size:** 533 MB
- **Train size:** 340 MB
- **Test size:** 193 MB

### Dataset Summary

The Machine Paraphrase Corpus (MPC) consists of ~200k examples of original, and paraphrases using two online paraphrasing tools.
It uses two paraphrasing tools (SpinnerChief, SpinBot) on three source texts (Wikipedia, arXiv, student theses).
The examples are **not** aligned, i.e., we sample different paragraphs for originals and paraphrased versions.

### How to use it
You can load the dataset using the `load_dataset` function:

```python
from datasets import load_dataset

ds = load_dataset("jpwahle/machine-paraphrase-dataset")
print(ds[0])

#OUTPUT:
{
 'text': 'The commemoration was revealed on Whit Monday 16 May 1921 by the Prince of Wales later King Edward VIII with Lutyens in participation At the divulging function Lord Fortescue gave a discourse in which he evaluated that 11600 people from Devon had been slaughtered while serving in the war He later expressed that somewhere in the range of 63700 8000 regulars 36700 volunteers and 19000 recruits had served in the military The names of the fallen were recorded on a move of respect of which three duplicates were made one for Exeter Cathedral one to be held by the district chamber and one which the Prince of Wales put in an empty in the base of the war dedication The rulers visit created impressive energy in the zone A large number of individuals lined the road to welcome his motorcade and shops on the High Street hung out pennants with inviting messages After the uncovering Edward went through ten days visiting the neighborhood ',
 'label': 1,
 'dataset': 'wikipedia',
 'method': 'spinbot'
}
```

### Supported Tasks and Leaderboards

Paraphrase Identification

### Languages

English

## Dataset Structure

### Data Instances

```json
{
 'text': 'The commemoration was revealed on Whit Monday 16 May 1921 by the Prince of Wales later King Edward VIII with Lutyens in participation At the divulging function Lord Fortescue gave a discourse in which he evaluated that 11600 people from Devon had been slaughtered while serving in the war He later expressed that somewhere in the range of 63700 8000 regulars 36700 volunteers and 19000 recruits had served in the military The names of the fallen were recorded on a move of respect of which three duplicates were made one for Exeter Cathedral one to be held by the district chamber and one which the Prince of Wales put in an empty in the base of the war dedication The rulers visit created impressive energy in the zone A large number of individuals lined the road to welcome his motorcade and shops on the High Street hung out pennants with inviting messages After the uncovering Edward went through ten days visiting the neighborhood ',
 'label': 1,
 'dataset': 'wikipedia',
 'method': 'spinbot'
 }
```

### Data Fields

| Feature | Description |
| --- | --- |
| `text` | The unique identifier of the paper. |
| `label` | Whether it is a paraphrase (1) or the original (0). |
| `dataset` | The source dataset (Wikipedia, arXiv, or theses). |
| `method` | The method used (SpinBot, SpinnerChief, original). |

### Data Splits

- train (Wikipedia x Spinbot)
- test ([Wikipedia, arXiv, theses] x [SpinBot, SpinnerChief])

## Dataset Creation

### Curation Rationale

Providing a resource for testing against machine-paraprhased plagiarism.

### Source Data

#### Initial Data Collection and Normalization

- Paragraphs from `featured articles` from the English Wikipedia dump
- Paragraphs from full-text pdfs of arXMLiv
- Paragraphs from full-text pdfs of Czech student thesis (bachelor, master, PhD).

#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

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

[Jan Philip Wahle](https://jpwahle.com/)

### Licensing Information

The Machine Paraphrase Dataset is released under CC BY-NC 4.0. By using this corpus, you agree to its usage terms.

### Citation Information

```bib
@inproceedings{10.1007/978-3-030-96957-8_34,
	title        = {Identifying Machine-Paraphrased Plagiarism},
	author       = {Wahle, Jan Philip and Ruas, Terry and Folt{\'y}nek, Tom{\'a}{\v{s}} and Meuschke, Norman and Gipp, Bela},
	year         = 2022,
	booktitle    = {Information for a Better World: Shaping the Global Future},
	publisher    = {Springer International Publishing},
	address      = {Cham},
	pages        = {393--413},
	isbn         = {978-3-030-96957-8},
	editor       = {Smits, Malte},
	abstract     = {Employing paraphrasing tools to conceal plagiarized text is a severe threat to academic integrity. To enable the detection of machine-paraphrased text, we evaluate the effectiveness of five pre-trained word embedding models combined with machine learning classifiers and state-of-the-art neural language models. We analyze preprints of research papers, graduation theses, and Wikipedia articles, which we paraphrased using different configurations of the tools SpinBot and SpinnerChief. The best performing technique, Longformer, achieved an average F1 score of 80.99{\%} (F1 = 99.68{\%} for SpinBot and F1 = 71.64{\%} for SpinnerChief cases), while human evaluators achieved F1 = 78.4{\%} for SpinBot and F1 = 65.6{\%} for SpinnerChief cases. We show that the automated classification alleviates shortcomings of widely-used text-matching systems, such as Turnitin and PlagScan.}
}
```

### Contributions

Thanks to [@jpwahle](https://github.com/jpwahle) for adding this dataset.