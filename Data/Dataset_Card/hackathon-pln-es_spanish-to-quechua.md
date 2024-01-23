---
language:
- es
- qu
task_categories:
- translation
task:
- translation
---

# Spanish to Quechua

## Table of Contents
- [Dataset Description](#dataset-description)
- [Dataset Structure](#dataset-structure)
- [Dataset Creation](#dataset-creation)
- [Considerations for Using the Data](#considerations-for-using-the-data)
- [team members](#team-members)

## Dataset Description

This dataset is a recopilation of webs and others datasets that shows in [dataset creation section](#dataset-creation). This contains translations from spanish (es) to Qechua of Ayacucho (qu).

## Dataset Structure

### Data Fields
- es: The sentence in Spanish.
- qu: The sentence in Quechua of Ayacucho.

### Data Splits
- train: To train the model (102 747 sentences).
- Validation: To validate the model during training (12 844 sentences).
- test: To evaluate the model when the training is finished (12 843 sentences).

## Dataset Creation
### Source Data
This dataset has generated from:
- "Mundo Quechua" by "Ivan Acuña" - [available here](https://mundoquechua.blogspot.com/2006/07/frases-comunes-en-quechua.html)
- "Kuyakuykim (Te quiero): Apps con las que podrías aprender quechua" by "El comercio" - [available here](https://elcomercio.pe/tecnologia/actualidad/traductor-frases-romanticas-quechua-noticia-467022-noticia/)
- "Piropos y frases de amor en quechua" by "Soy Quechua" - [available here](https://www.soyquechua.org/2019/12/palabras-en-quechua-de-amor.html)
- "Corazón en quechua" by "Soy Quechua" - [available here](https://www.soyquechua.org/2020/05/corazon-en-quechua.html)
- "Oraciones en Español traducidas a Quechua" by "Tatoeba" - [available here](https://tatoeba.org/es/sentences/search?from=spa&query=&to=que)
- "AmericasNLP 2021 Shared Task on Open Machine Translation" by "americasnlp2021" - [available here](https://github.com/AmericasNLP/americasnlp2021/tree/main/data/quechua-spanish/parallel_data/es-quy)

### Data cleaning
- The dataset was manually cleaned during compilation, as some words of one language were related to several words of the other language.

## Considerations for Using the Data

This is a first version of the dataset, we expected improve it over time and especially to neutralize the biblical themes.

## Team members
- [Sara Benel](https://huggingface.co/sbenel)
- [Jose Vílchez](https://huggingface.co/JCarlos)