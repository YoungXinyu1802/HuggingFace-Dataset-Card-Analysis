# Dataset Card for biomed_squad_es_v2

This Dataset was created as part of the "Extractive QA Biomedicine" project developed during the 2022 [Hackathon](https://somosnlp.org/hackathon) organized by SOMOS NLP.

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

- **Homepage:** [Needs More Information]
- **Repository:** [Needs More Information]
- **Paper:** [Needs More Information]
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [Needs More Information]

### Dataset Summary

This is a subset of the [dev squad_es (v2) dataset](https://huggingface.co/datasets/squad_es) (automatic translation of the Stanford Question Answering Dataset v2 into Spanish) containing questions related to the biomedical domain.

License, distribution and usage conditions of the original Squad_es Dataset apply.

### Languages

Spanish

## Dataset Structure

### Data Fields

```
{'answers': {'answer_start': [343, 343, 343],
  'text': ['diez veces su propio peso',
   'diez veces su propio peso',
   'diez veces su propio peso']},
 'context': 'Casi todos los ctenóforos son depredadores, tomando presas que van desde larvas microscópicas y rotíferos a los adultos de pequeños crustáceos; Las excepciones son los juveniles de dos especies, que viven como parásitos en las salpas en las que los adultos de su especie se alimentan. En circunstancias favorables, los ctenóforos pueden comer diez veces su propio peso en un día. Sólo 100-150 especies han sido validadas, y posiblemente otras 25 no han sido completamente descritas y nombradas. Los ejemplos de libros de texto son cidipidos con cuerpos en forma de huevo y un par de tentáculos retráctiles bordeados con tentilla ("pequeños tentáculos") que están cubiertos con colúnculos, células pegajosas. El filo tiene una amplia gama de formas corporales, incluyendo los platyctenidos de mar profundo, en los que los adultos de la mayoría de las especies carecen de peines, y los beroides costeros, que carecen de tentáculos. Estas variaciones permiten a las diferentes especies construir grandes poblaciones en la misma área, porque se especializan en diferentes tipos de presas, que capturan por una amplia gama de métodos que utilizan las arañas.',
 'id': '5725c337271a42140099d165',
 'question': '¿Cuánta comida come un Ctenophora en un día?',
 'title': 'Ctenophora'}
```

### Data Splits

Validation: 1137 examples


### Citation Information

```
@article{2016arXiv160605250R,
       author = {Casimiro Pio , Carrino and  Marta R. , Costa-jussa and  Jose A. R. , Fonollosa},
        title = "{Automatic Spanish Translation of the SQuAD Dataset for Multilingual
Question Answering}",
      journal = {arXiv e-prints},
         year = 2019,
          eid = {arXiv:1912.05200v1},
        pages = {arXiv:1912.05200v1},
archivePrefix = {arXiv},
       eprint = {1912.05200v2},
}
```

## Team
Santiago Maximo: [smaximo](https://huggingface.co/smaximo)