---
YAML tags:

annotations_creators:
- expert-generated
language:
- es
language_creators:
- found
multilinguality:
- monolingual
pretty_name: STS-es
size_categories: []
source_datasets: []
tags: []
task_categories:
- text-classification
task_ids:
- semantic-similarity-scoring
- text-scoring

---


# STS-es

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
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)


## Dataset Description
- **Homepage:** https://alt.qcri.org/semeval2014/task10/ 
- **Point of Contact:** [Aitor Gonzalez](aitor.gonzalez@bsc.es) 


### Dataset Summary

For Semantic Text Similarity, we collected the Spanish test sets from SemEval-2014 (Agirre et al., 2014) and SemEval-2015 (Agirre et al., 2015). Since no training data was provided for the Spanish subtask, we randomly sampled both datasets into 1,321 sentences for the train set, 78 sentences for the development set, and 156 sentences for the test set. To make the task harder for the models, we purposely made the development set smaller than the test set.

We use this corpus as part of the EvalEs Spanish language benchmark. 

### Supported Tasks and Leaderboards

Semantic Text Similarity Scoring

### Languages

The dataset is in Spanish (`es-ES`)

## Dataset Structure

### Data Instances

```
{
  'sentence1': "El "tendón de Aquiles" ("tendo Achillis") o "tendón calcáneo" ("tendo calcaneus") es un tendón de la parte posterior de la pierna."
  'sentence2': "El tendón de Aquiles es la extensión tendinosa de los tres músculos de la pantorrilla: gemelo, sóleo y plantar delgado."
  'label': 2.8
}
```

### Data Fields

- sentence1: String
- sentence2: String
- label: Float

### Data Splits

- train: 1,321 instances
- dev: 78 instances
- test: 156 instances

## Dataset Creation

### Curation Rationale
[N/A] 

### Source Data

The source data came from the Spanish Wikipedia (2013 dump) and texts from Spanish news (2014).

For more information visit the paper from the SemEval-2014 Shared Task [(Agirre et al., 2014)](https://aclanthology.org/S14-2010.pdf) and the SemEval-2015 Shared Task [(Agirre et al., 2015)](https://aclanthology.org/S15-2045.pdf).

#### Initial Data Collection and Normalization

For more information visit the paper from the SemEval-2014 Shared Task [(Agirre et al., 2014)](https://aclanthology.org/S14-2010.pdf) and the SemEval-2015 Shared Task [(Agirre et al., 2015)](https://aclanthology.org/S15-2045.pdf).

#### Who are the source language producers?

Journalists and Wikipedia contributors.

### Annotations

#### Annotation process

For more information visit the paper from the SemEval-2014 Shared Task [(Agirre et al., 2014)](https://aclanthology.org/S14-2010.pdf) and the SemEval-2015 Shared Task [(Agirre et al., 2015)](https://aclanthology.org/S15-2045.pdf).

#### Who are the annotators?

For more information visit the paper from the SemEval-2014 Shared Task [(Agirre et al., 2014)](https://aclanthology.org/S14-2010.pdf) and the SemEval-2015 Shared Task [(Agirre et al., 2015)](https://aclanthology.org/S15-2045.pdf).

### Personal and Sensitive Information

No personal or sensitive information included.

## Considerations for Using the Data

### Social Impact of Dataset

This dataset contributes to the development of language models in Spanish.

### Discussion of Biases

No postprocessing steps were applied to mitigate potential social biases.

## Additional Information


### Citation Information

The following papers must be cited when using this corpus:

```
@inproceedings{agirre2015semeval,
  title={Semeval-2015 task 2: Semantic textual similarity, english, spanish and pilot on interpretability},
  author={Agirre, Eneko and Banea, Carmen and Cardie, Claire and Cer, Daniel and Diab, Mona and Gonzalez-Agirre, Aitor and Guo, Weiwei and Lopez-Gazpio, Inigo and Maritxalar, Montse and Mihalcea, Rada and others},
  booktitle={Proceedings of the 9th international workshop on semantic evaluation (SemEval 2015)},
  pages={252--263},
  year={2015}
}


@inproceedings{agirre2014semeval,
  title={SemEval-2014 Task 10: Multilingual Semantic Textual Similarity.},
  author={Agirre, Eneko and Banea, Carmen and Cardie, Claire and Cer, Daniel M and Diab, Mona T and Gonzalez-Agirre, Aitor and Guo, Weiwei and Mihalcea, Rada and Rigau, German and Wiebe, Janyce},
  booktitle={SemEval@ COLING},
  pages={81--91},
  year={2014}
}

```
