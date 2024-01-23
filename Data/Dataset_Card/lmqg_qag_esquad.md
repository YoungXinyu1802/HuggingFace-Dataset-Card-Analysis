---
license: cc-by-sa-4.0
pretty_name: SQuAD for question generation
language: es
multilinguality: monolingual
size_categories: 1k<n<10K
source_datasets: lmqg/qg_esquad
task_categories:
- text-generation
task_ids:
- language-modeling
tags:
- question-generation
---

# Dataset Card for "lmqg/qag_esquad"


## Dataset Description
- **Repository:** [https://github.com/asahi417/lm-question-generation](https://github.com/asahi417/lm-question-generation)
- **Paper:** [https://arxiv.org/abs/2210.03992](https://arxiv.org/abs/2210.03992)
- **Point of Contact:** [Asahi Ushio](http://asahiushio.com/)

### Dataset Summary
This is the question & answer generation dataset based on the ESQuAD.

### Supported Tasks and Leaderboards
* `question-answer-generation`: The dataset is assumed to be used to train a model for question & answer generation.
  Success on this task is typically measured by achieving a high BLEU4/METEOR/ROUGE-L/BERTScore/MoverScore (see our paper for more in detail).

### Languages
Spanish (es)

## Dataset Structure
An example of 'train' looks as follows.
```
{
  "paragraph": ""4 Minutes" fue lanzado como el primer sencillo del álbum y alcanzó el número tres en el Billboard Hot 100. Fue el 37º hit top-ten de Madonna en la lista, empujando a Madonna más allá de Elvis Presley como el artista con más éxitos entre los diez primeros. En el Reino Unido mantuvo su récord de más sencillos número uno para una artista femenina; "4 Minutes" se convierte en su decimotercera. En el 23 Japan Gold Disc Awards, Madonna recibió su quinto trofeo de Artista del Año de la Recording Industry Association of Japan, la mayor cantidad para cualquier artista. Para promover aún más el álbum, Madonna se embarcó en el Sticky & Sweet Tour; Su primera gran empresa con Live Nation. Con una recaudación de $280 millones, se convirtió en la gira más taquillera de un artista en solitario entonces, superando el récord anterior que Madonna estableció con la gira Confessions Tour; Más tarde fue superado por The Wall Live de Roger Waters. Se amplió al año siguiente, añadiendo nuevas fechas europeas, y después de que terminó, la recaudación total fue de $408 millones.",
  "questions": [ "¿Cuál es el nombre de la primera gira con Live Nation?", "4 minutos se convirtió en la canción número uno de Madonna en el Reino Unido.", "¿Cuál sencillo fue lanzado como el primer sencillo del álbum?", "¿Cuánto recaudaron Stick y Sweet Tour?", "Madonna superó a qué artista con más éxitos entre los diez primeros." ],
  "answers": [ "Sticky & Sweet Tour", "decimotercera", "\"4 Minute", "$280 millones,", "Elvis Presley" ]
  "questions_answers": "question: ¿Cuál es el nombre de la primera gira con Live Nation?, answer: Sticky & Sweet Tour | question: 4 minutos se convirtió en la canción número uno de Madonna en el Reino Unido., answer: decimotercera | question: ¿Cuál sencillo fue lanzado como el primer sencillo del álbum?, answer: "4 Minute | question: ¿Cuánto recaudaron Stick y Sweet Tour?, answer: $280 millones, | question: Madonna superó a qué artista con más éxitos entre los diez primeros., answer: Elvis Presley"
  }
```
The data fields are the same among all splits.
- `questions`: a `list` of `string` features. 
- `answers`: a `list` of `string` features.
- `paragraph`: a `string` feature.
- `questions_answers`: a `string` feature.

## Data Splits

|train|validation|test |
|----:|---------:|----:|
|18829|     2067 | 8234|


## Citation Information

```
@inproceedings{ushio-etal-2022-generative,
    title = "{G}enerative {L}anguage {M}odels for {P}aragraph-{L}evel {Q}uestion {G}eneration",
    author = "Ushio, Asahi  and
        Alva-Manchego, Fernando  and
        Camacho-Collados, Jose",
    booktitle = "Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing",
    month = dec,
    year = "2022",
    address = "Abu Dhabi, U.A.E.",
    publisher = "Association for Computational Linguistics",
}
```