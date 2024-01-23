---
annotations_creators:
- expert-generated
language:
- pt
language_creators:
- found
license: []
multilinguality:
- monolingual
pretty_name: HateBR - Offensive Language and Hate Speech Dataset in Brazilian Portuguese
size_categories:
- 1K<n<10K
source_datasets:
- original
tags:
- instagram
task_categories:
- text-classification
task_ids:
- hate-speech-detection
---
# Dataset Card for HateBR - Offensive Language and Hate Speech Dataset in Brazilian Portuguese

## Dataset Description

- **Homepage:** http://143.107.183.175:14581/
- **Repository:** https://github.com/franciellevargas/HateBR
- **Paper:** https://aclanthology.org/2022.lrec-1.777/
- **Leaderboard:** 
- **Point of Contact:** https://franciellevargas.github.io/

### Dataset Summary

HateBR is the first large-scale expert annotated corpus of Brazilian Instagram comments for hate speech and offensive language detection on the web and social media. The HateBR corpus was collected from Brazilian Instagram comments of politicians and manually annotated by specialists. It is composed of 7,000 documents annotated according to three different layers: a binary classification (offensive versus non-offensive comments), offensiveness-level (highly, moderately, and slightly offensive messages), and nine hate speech groups (xenophobia, racism, homophobia, sexism, religious intolerance, partyism, apology for the dictatorship, antisemitism, and fatphobia). Each comment was annotated by three different annotators and achieved high inter-annotator agreement. Furthermore, baseline experiments were implemented reaching 85% of F1-score outperforming the current literature models for the Portuguese language. Accordingly, we hope that the proposed expertly annotated corpus may foster research on hate speech and offensive language detection in the Natural Language Processing area.

**Relevant Links:**

* [**Demo: Brasil Sem Ódio**](http://143.107.183.175:14581/)
* [**MOL - Multilingual Offensive Lexicon Annotated with Contextual Information**](https://github.com/franciellevargas/MOL)

### Supported Tasks and Leaderboards

Hate Speech Detection

### Languages

Portuguese

## Dataset Structure

### Data Instances

```
{'instagram_comments': 'Hipocrita!!',
 'offensive_language': True,
 'offensiveness_levels': 2,
 'antisemitism': False,
 'apology_for_the_dictatorship': False,
 'fatphobia': False,
 'homophobia': False,
 'partyism': False,
 'racism': False,
 'religious_intolerance': False,
 'sexism': False,
 'xenophobia': False,
 'offensive_&_non-hate_speech': True,
 'non-offensive': False,
 'specialist_1_hate_speech': False,
 'specialist_2_hate_speech': False,
 'specialist_3_hate_speech': False
}
```

### Data Fields

* **instagram_comments**: Instagram comments.
* **offensive_language**: A classification of comments as either offensive (True) or non-offensive (False).
* **offensiveness_levels**: A classification of comments based on their level of offensiveness, including highly offensive (3), moderately offensive (2), slightly offensive (1) and non-offensive (0).
* **antisemitism**: A classification of whether or not the comment contains antisemitic language.
* **apology_for_the_dictatorship**: A classification of whether or not the comment praises the military dictatorship period in Brazil.
* **fatphobia**: A classification of whether or not the comment contains language that promotes fatphobia.
* **homophobia**: A classification of whether or not the comment contains language that promotes homophobia.
* **partyism**: A classification of whether or not the comment contains language that promotes partyism.
* **racism**: A classification of whether or not the comment contains racist language.
* **religious_intolerance**: A classification of whether or not the comment contains language that promotes religious intolerance.
* **sexism**: A classification of whether or not the comment contains sexist language.
* **xenophobia**: A classification of whether or not the comment contains language that promotes xenophobia.
* **offensive_&_no-hate_speech**: A classification of whether or not the comment is offensive but does not contain hate speech.
* **specialist_1_hate_speech**: A classification of whether or not the comment was annotated by the first specialist as hate speech.
* **specialist_2_hate_speech**: A classification of whether or not the comment was annotated by the second specialist as hate speech.
* **specialist_3_hate_speech**: A classification of whether or not the comment was annotated by the third specialist as hate speech.
  
### Data Splits

The original authors of the dataset did not propose a standard data split. To address this, we use the [multi-label data stratification technique](http://scikit.ml/stratification.html) implemented at the scikit-multilearn library to propose a train-validation-test split. This method considers all classes for hate speech in the data and attempts to balance the representation of each class in the split.

|  name   |train|validation|test|
|---------|----:|----:|----:|
|hatebr|4480|1120|1400|

## Considerations for Using the Data

### Discussion of Biases

Please refer to [the HateBR paper](https://aclanthology.org/2022.lrec-1.777/) for a discussion of biases.

### Citation Information

```
@inproceedings{vargas2022hatebr,
  title={HateBR: A Large Expert Annotated Corpus of Brazilian Instagram Comments for Offensive Language and Hate Speech Detection},
  author={Vargas, Francielle and Carvalho, Isabelle and de G{\'o}es, Fabiana Rodrigues and Pardo, Thiago and Benevenuto, Fabr{\'\i}cio},
  booktitle={Proceedings of the Thirteenth Language Resources and Evaluation Conference},
  pages={7174--7183},
  year={2022}
}
```

### Contributions

Thanks to [@ruanchaves](https://github.com/ruanchaves) for adding this dataset.