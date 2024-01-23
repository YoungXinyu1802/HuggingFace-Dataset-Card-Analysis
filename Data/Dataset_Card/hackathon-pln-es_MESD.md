---
license: cc-by-4.0

Duville, Mathilde Marie; Alonso-Valerdi, Luz Maria; Ibarra, David (2022), “Mexican Emotional Speech Database (MESD)”, Mendeley Data, V5, doi: 10.17632/cy34mh68j9.5

---

# Dataset Card for MESD

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-instances)
  - [Data Splits](#data-instances)
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

## Dataset Description

- **Homepage:** https://data.mendeley.com/datasets/cy34mh68j9/5
- **Repository:** [Needs More Information]
- **Paper:** [Needs More Information]
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [Needs More Information]

### Dataset Summary

Contiene los datos de la base MESD procesados para hacer 'finetuning' de un modelo 'Wav2Vec' en el Hackaton organizado por 'Somos NLP'.

Ejemplo de referencia: 
https://colab.research.google.com/github/huggingface/notebooks/blob/master/examples/audio_classification.ipynb

Hemos accedido a la base MESD para obtener ejemplos. 

Breve descripción de los autores de la base MESD:
"La Base de Datos del Discurso Emocional Mexicano (MESD en inglés) proporciona enunciados de una sola palabra para las prosodias afectivas de ira, asco, miedo, felicidad, neutro y tristeza con conformación cultural mexicana. El MESD ha sido pronunciado por actores adultos y niños no profesionales: Se dispone de 3 voces femeninas, 2 masculinas y 6 infantiles. Las palabras de los enunciados emocionales y neutros proceden de dos corpus: (corpus A) compuesto por sustantivos y adjetivos que se repiten a través de prosodias emocionales y tipos de voz (femenina, masculina, infantil), y (corpus B) que consiste en palabras controladas por edad de adquisición, frecuencia de uso, familiaridad, concreción, valencia, excitación y clasificaciones de dimensionalidad de emociones discretas. 

Las grabaciones de audio se realizaron en un estudio profesional con los siguientes materiales (1) un micrófono Sennheiser e835 con una respuesta de frecuencia plana (100 Hz a 10 kHz), (2) una interfaz de audio Focusrite Scarlett 2i4 conectada al micrófono con un cable XLR y al ordenador, y (3) la estación de trabajo de audio digital REAPER (Rapid Environment for Audio Production, Engineering, and Recording). Los archivos de audio se almacenaron como una secuencia de 24 bits con una frecuencia de muestreo de 48000Hz. La amplitud de las formas de onda acústicas se reescaló entre -1 y 1. 

Se crearon dos versiones con reducción de la naturalidad de los locutores a partir de expresiones emocionales humanas para voces femeninas del corpus B. En concreto, la naturalidad se redujo progresivamente de las voces humanas al nivel 1 al nivel 2. En particular, se editaron la duración y el tono medio en las sílabas acentuadas para reducir la diferencia entre las sílabas acentuadas y las no acentuadas. En los enunciados completos, se redujeron las relaciones F2/F1 y F3/F1 editando las frecuencias F2 y F3. También se redujo la intensidad de los armónicos 1 y 4. "


### Supported Tasks and Leaderboards

[Needs More Information]

### Languages

Español

## Dataset Structure

### Data Instances

[Needs More Information]

### Data Fields

Origen: texto que indica si se trata del conjunto de datos MESD original o los casos 'Speaker-embedded naturalness-reduced female voices'  donde los autores han generado de forma sintética nuevos datos transformando algunas de las instancias de los audios originales.

Palabra: texto de la palabra que se ha leído.

Emoción: texto de la emoción a la que representa: Valores: 'Enojo', 'Felicidad', 'Miedo', 'Neutral', 'Disgusto', 'Tristeza'.

InfoActor: texto que indica si la voz es de 'Niño', 'Hombre', 'Mujer'.

AudioArray: audio array, remuestreado a 16 Khz.

### Data Splits

Train: 891 ejemplos, mezcla de casos MESD y 'Speaker-embedded naturalness-reduced female voices'.

Validation: 130 ejemplos, todos casos MESD.

Test: 129 ejemplos, todos casos MESD.

## Dataset Creation

### Curation Rationale

Unir los tres subconjuntos de datos y procesarlos para la tarea de finetuning, acorde al input esperado por el modelo Wav2Vec.

### Source Data

#### Initial Data Collection and Normalization

Acceso a los datos en bruto:
https://data.mendeley.com/datasets/cy34mh68j9/5

Conversión a audio arra y remuestreo a 16 Khz.

#### Who are the source language producers?

Duville, Mathilde Marie; Alonso-Valerdi, Luz Maria; Ibarra, David (2022), “Mexican Emotional Speech Database (MESD)”, Mendeley Data, V5, doi: 10.17632/cy34mh68j9.5

### Annotations

#### Annotation process

[Needs More Information]

#### Who are the annotators?

[Needs More Information]

### Personal and Sensitive Information

[Needs More Information]

## Considerations for Using the Data

### Social Impact of Dataset

[Needs More Information]

### Discussion of Biases

[Needs More Information]

### Other Known Limitations

[Needs More Information]

## Additional Information

### Dataset Curators

[Needs More Information]

### Licensing Information

Creative Commons, [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)

### Citation Information

```
Duville, Mathilde Marie; Alonso-Valerdi, Luz Maria; Ibarra, David (2022), “Mexican Emotional Speech Database (MESD)”, Mendeley Data, V5, doi: 10.17632/cy34mh68j9.5

```
