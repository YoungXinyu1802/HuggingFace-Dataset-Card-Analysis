---
license: 
- cc-by-4.0
annotations_creators:
- found
- machine-generated
language_creators:
- found
language:
- code
language_details: TypeScript
multilinguality:
- monolingual
size_categories:
- 10M<n<100M
source_datasets:
- original
task_categories:
- structure-prediction
task_ids:
- type-inference
pretty_name: ManyTypes4TypeScript
---
# Models Trained On ManyTypes4TypeScript
- **[CodeBERT]**(https://huggingface.co/kevinjesse/codebert-MT4TS)
- **[GraphCodeBERT]**(https://huggingface.co/kevinjesse/graphcodebert-MT4TS)
- **[CodeBERTa]**(https://huggingface.co/kevinjesse/codeberta-MT4TS)

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits-sample-size)
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

- **Dataset:** [https://doi.org/10.5281/zenodo.6387001](https://doi.org/10.5281/zenodo.6387001)
- **PapersWithCode:** [https://paperswithcode.com/sota/type-prediction-on-manytypes4typescript](https://paperswithcode.com/sota/type-prediction-on-manytypes4typescript)

### Dataset Summary

ManyTypes4TypeScript type inference dataset, available at the DOI link below. [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6387001.svg)](https://doi.org/10.5281/zenodo.6387001)

Given a line of source code, the task is to identify types that correspond with the tokens of code. We treat this as a tagging task similar to NER and POS where the model must predict a structural property of code i.e types. This is a classification task where the labels are the top occurring types in the training dataset. The size type vocabulary can be changed with the scripts found on Github.


### Supported Tasks and Leaderboards

- `multi-class-classification`: The dataset can be used to train a model for predicting types across a sequence.

### Languages

- TypeScript

## Dataset Structure

### Data Instances

An example of 'validation' looks as follows.
```
{
"tokens": ["import", "{", "Component", ",", "ChangeDetectorRef", "}", "from", "'@angular/core'", ";", "import", "{", "Router", "}", "from", "'@angular/router'", ";", "import", "{", "MenuController", "}", "from", "'@ionic/angular'", ";", "import", "{", "Storage", "}", "from", "'@ionic/storage'", ";", "import", "Swiper", "from", "'swiper'", ";", "@", "Component", "(", "{", "selector", ":", "'page-tutorial'", ",", "templateUrl", ":", "'tutorial.html'", ",", "styleUrls", ":", "[", "'./tutorial.scss'", "]", ",", "}", ")", "export", "class", "TutorialPage", "{", "showSkip", "=", "true", ";", "private", "slides", ":", "Swiper", ";", "constructor", "(", "public", "menu", ",", "public", "router", ",", "public", "storage", ",", "private", "cd", ")", "{", "}", "startApp", "(", ")", "{", "this", ".", "router", ".", "navigateByUrl", "(", "'/app/tabs/schedule'", ",", "{", "replaceUrl", ":", "true", "}", ")", ".", "then", "(", "(", ")", "=>", "this", ".", "storage", ".", "set", "(", "'ion_did_tutorial'", ",", "true", ")", ")", ";", "}", "setSwiperInstance", "(", "swiper", ")", "{", "this", ".", "slides", "=", "swiper", ";", "}", "onSlideChangeStart", "(", ")", "{", "this", ".", "showSkip", "=", "!", "this", ".", "slides", ".", "isEnd", ";", "this", ".", "cd", ".", "detectChanges", "(", ")", ";", "}", "ionViewWillEnter", "(", ")", "{", "this", ".", "storage", ".", "get", "(", "'ion_did_tutorial'", ")", ".", "then", "(", "res", "=>", "{", "if", "(", "res", "===", "true", ")", "{", "this", ".", "router", ".", "navigateByUrl", "(", "'/app/tabs/schedule'", ",", "{", "replaceUrl", ":", "true", "}", ")", ";", "}", "}", ")", ";", "this", ".", "menu", ".", "enable", "(", "false", ")", ";", "}", "ionViewDidLeave", "(", ")", "{", "this", ".", "menu", ".", "enable", "(", "true", ")", ";", "}", "}"],
"labels": [null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, "MenuController", null, null, "Router", null, null, "Storage", null, null, "ChangeDetectorRef", null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, "Swiper", null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null],
"url": "https://github.com/ionic-team/ionic-conference-app",
"path": "ionic-conference-app/src/app/pages/tutorial/tutorial.ts",
"commit_hash": "34d97d29369377a2f0173a2958de1ee0dadb8a6e",
"file": "tutorial.ts"}
}
```

### Data Fields

The data fields are the same among all splits.

#### default

|field name. | type        |               description                  |
|------------|-------------|--------------------------------------------|
|tokens      |list[string] | Sequence of tokens (word tokenization)     |
|labels      |list[string] | A list of corresponding types              |
|url         |string       | Repository URL                             |
|path        |string       | Original file path that contains this code |
|commit_hash |string       | Commit identifier in the original project  |
|file        |string       | File name                                  |

### Data Splits

|   name   |  train   |validation|   test  |
|---------:|---------:|---------:|--------:|
|projects  |  75.00%  |  12.5%   |  12.5%  |
|files     |  90.53%  |  4.43%   |  5.04%  |
|sequences |  91.95%  |  3.71%   |  4.34%  |
|types     |  95.33%  |  2.21%   |  2.46%  |

##Types by the Numbers

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

[More Information Needed]

### Annotations

Human annotated types in optionally typed languages and the compiler inferred annotations.

#### Annotation process



#### Who are the annotators?

Developers and TypeScript Compiler.

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

https://github.com/kevinjesse

### Licensing Information

Creative Commons 4.0 (CC) license

### Citation Information

```
```