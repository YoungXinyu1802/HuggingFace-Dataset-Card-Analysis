---
annotations_creators:
- expert-generated
language_creators:
- found
language:
- ru
license:
- cc-by-4.0
multilinguality:
- monolingual
size_categories:
- n<1K
source_datasets:
- original
task_categories:
- text-classification
task_ids:
- fact-checking
- sentiment-classification
paperswithcode_id: rustance
pretty_name: RuStance
tags:
- stance-detection
---

# Dataset Card for "rustance"

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

- **Homepage:** [https://figshare.com/articles/dataset/dataset_csv/7151906](https://figshare.com/articles/dataset/dataset_csv/7151906)
- **Repository:** [https://github.com/StrombergNLP/rustance](https://github.com/StrombergNLP/rustance)
- **Paper:** [https://link.springer.com/chapter/10.1007/978-3-030-14687-0_16](https://link.springer.com/chapter/10.1007/978-3-030-14687-0_16), [https://arxiv.org/abs/1809.01574](https://arxiv.org/abs/1809.01574)
- **Point of Contact:** [Leon Derczynski](https://github.com/leondz)
- **Size of downloaded dataset files:** 212.54 KiB
- **Size of the generated dataset:** 186.76 KiB
- **Total amount of disk used:**  399.30KiB

### Dataset Summary

This is a stance prediction dataset in Russian. The dataset contains comments on news articles,
and rows are a comment, the title of the news article it responds to, and the stance of the comment
towards the article.

Stance detection is a critical component of rumour and fake news identification. It involves the extraction of the stance a particular author takes related to a given claim, both expressed in text. This paper investigates stance classification for Russian. It introduces a new dataset, RuStance, of Russian tweets and news comments from multiple sources, covering multiple stories, as well as text classification approaches to stance detection as benchmarks over this data in this language. As well as presenting this openly-available dataset, the first of its kind for Russian, the paper presents a baseline for stance prediction in the language.

### Supported Tasks and Leaderboards

* Stance Detection: [Stance Detection on RuStance](https://paperswithcode.com/sota/stance-detection-on-rustance)

### Languages

Russian, as spoken on the Meduza website (i.e. from multiple countries) (`bcp47:ru`)

## Dataset Structure

### Data Instances

#### rustance

- **Size of downloaded dataset files:** 349.79 KiB
- **Size of the generated dataset:** 366.11 KiB
- **Total amount of disk used:**  715.90 KiB

An example of 'train' looks as follows.

```
{
  'id': '0', 
  'text': 'Волки, волки!!', 
  'title': 'Минобороны обвинило «гражданского сотрудника» в публикации скриншота из игры вместо фото террористов. И показало новое «неоспоримое подтверждение»', 
  'stance': 3
}
```


### Data Fields

- `id`: a `string` feature.
- `text`: a `string` expressing a stance.
- `title`: a `string` of the target/topic annotated here.
- `stance`: a class label representing the stance the text expresses towards the target. Full tagset with indices:

```
                            0: "support",
                            1: "deny",
                            2: "query",
                            3: "comment",
```

### Data Splits

|  name   |train|
|---------|----:|
|rustance|958 sentences|

## Dataset Creation

### Curation Rationale

Toy data for training and especially evaluating stance prediction in Russian

### Source Data

#### Initial Data Collection and Normalization

The data is comments scraped from a Russian news site not situated in Russia, [Meduza](https://meduza.io/), in 2018.

#### Who are the source language producers?

Russian speakers including from the Russian diaspora, especially Latvia

### Annotations

#### Annotation process

Annotators labelled comments for supporting, denying, querying or just commenting on a news article.

#### Who are the annotators?

Russian native speakers, IT education, male, 20s.

### Personal and Sensitive Information

The data was public at the time of collection. No PII removal has been performed.

## Considerations for Using the Data

### Social Impact of Dataset

There's a risk of misinformative content being in this data. The data has NOT been vetted for any content.

### Discussion of Biases


### Other Known Limitations

The above limitations apply.

## Additional Information

### Dataset Curators

The dataset is curated by the paper's authors.

### Licensing Information

The authors distribute this data under Creative Commons attribution license, CC-BY 4.0. 

### Citation Information

```
@inproceedings{lozhnikov2018stance,
  title={Stance prediction for russian: data and analysis},
  author={Lozhnikov, Nikita and Derczynski, Leon and Mazzara, Manuel},
  booktitle={International Conference in Software Engineering for Defence Applications},
  pages={176--186},
  year={2018},
  organization={Springer}
}
```


### Contributions

Author-added dataset [@leondz](https://github.com/leondz) 
