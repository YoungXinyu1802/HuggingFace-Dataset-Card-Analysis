---
license: unknown
---


### FrenchHateSpeechSuperset

This dataset is a superset of multiple datasets including hate speech, harasment, sexist, racist, etc...messages from various platforms.

Included datasets :

- MLMA dataset
- CAA dataset
- FTR dataset
- "An Annotated Corpus for Sexism Detection in French Tweets" dataset
- UC-Berkeley-Measuring-Hate-Speech dataset (translated from english*)


#### References

```
@inproceedings{chiril2020annotated,
  title={An Annotated Corpus for Sexism Detection in French Tweets},
  author={Chiril, Patricia and Moriceau, V{\'e}ronique and Benamara, Farah and Mari, Alda and Origgi, Gloria and Coulomb-Gully, Marl{\`e}ne},
  booktitle={Proceedings of The 12th Language Resources and Evaluation Conference},
  pages={1397--1403},
  year={2020}
}
```

```
@inproceedings{ousidhoum-etal-multilingual-hate-speech-2019,
		title = "Multilingual and Multi-Aspect Hate Speech Analysis",
		author = "Ousidhoum, Nedjma
         		and Lin, Zizheng
         		and Zhang, Hongming
        		and Song, Yangqiu
        		and Yeung, Dit-Yan",
			booktitle = "Proceedings of EMNLP",
		year = "2019",
		publisher =	"Association for Computational Linguistics",
}
```

```
Vanetik, N.; Mimoun, E. Detection of Racist Language in French Tweets. Information 2022, 13, 318. https://doi.org/10.3390/info13070318
```

```
@article{kennedy2020constructing,
  title={Constructing interval variables via faceted Rasch measurement and multitask deep learning: a hate speech application},
  author={Kennedy, Chris J and Bacon, Geoff and Sahn, Alexander and von Vacano, Claudia},
  journal={arXiv preprint arXiv:2009.10277},
  year={2020}
}
```

```
Anaïs Ollagnier, Elena Cabrio, Serena Villata, Catherine Blaya. CyberAgressionAdo-v1: a Dataset of Annotated Online Aggressions in French Collected through a Role-playing Game. Language Resources and Evaluation Conference, Jun 2022, Marseille, France. ⟨hal-03765860⟩
```

### Translation

French datasets for hate speech are quite rare. To augment current dataset, messages from other languages (english only for now) have been integrated.
To integrate other languages dataset, MT model were used and manually selected for each dataset.

- UC-Berkeley-Measuring-Hate-Speech dataset : Abelll/marian-finetuned-kde4-en-to-fr

### Language verification

Since MT models are not perfect, some messages are not entirely translated or not translated at all.
To check for obvious errors in pipeline, a general language detection model is used to prune non french texts.

Language detection model : papluca/xlm-roberta-base-language-detection

### Annotation

Since "hate speech" dimension is highly subjective, and datasets comes with different annotations types, a conventional labeling stategy is required.

Each sample is annotated with "0" if negative sample and "1" if positive sample.

### Filtering rules :

- FTR dataset : [wip]
- MLMA dataset : [wip]
- CAA dataset : [wip]
- "Annotated Corpus" dataset : [wip]
- UC-Berkeley Measuring Hate Speech dataset : average hate_speech_score > 0 -> 1
