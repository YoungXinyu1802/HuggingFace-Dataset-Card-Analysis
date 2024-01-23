---
annotations_creators:
- crowdsourced
language_creators:
- crowdsourced
language:
- ru
license:
- apache-2.0
multilinguality:
- monolingual
pretty_name: The Corpus for the analysis of author profiling in Russian-language texts.
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- text-classification
task_ids:
- multi-class-classification
- multi-label-classification
---

# Dataset Card for [author_profiling]

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
  - [Contributions](#contributions)

## Dataset Description

- **Homepage:** https://github.com/sag111/Author-Profiling
- **Repository:** https://github.com/sag111/Author-Profiling
- **Paper:** [Needs More Information]
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [Sboev Alexander](mailto:sag111@mail.ru)

### Dataset Summary

The corpus for the author profiling analysis contains texts in Russian-language which labeled for 5 tasks:
1) gender -- 13448 texts with the labels, who wrote this: text female or male;

2) age -- 13448 texts with the labels, how old the person who wrote the text. This is a number from 12 to 80. In addition, for the classification task we added 5 age groups: 0-19; 20-29; 30-39; 40-49; 50+;

3) age imitation -- 8460 texts, where crowdsource authors is asked to write three texts: 
  a) in their natural manner, 
  b) imitating the style of someone younger, 
  c) imitating the style of someone older;

4) gender imitation -- 4988 texts, where the crowdsource authors is asked to write texts: in their origin gender and pretending to be the opposite gender;

5) style imitation -- 4988 texts, where crowdsource authors is asked to write a text on behalf of another person of your own gender, with a distortion of the authors usual style.


Dataset is collected sing the Yandex.Toloka service [link](https://toloka.yandex.ru/en).

You can read the data using the following python code:
```
def load_jsonl(input_path: str) -> list:
    """
    Read list of objects from a JSON lines file.
    """
    data = []
    with open(input_path, 'r', encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line.rstrip('\n|\r')))
    print('Loaded {} records from {}/n'.format(len(data), input_path))
    
    return data

path_to_file = "./data/train.jsonl"
data = load_jsonl(path_to_file)
```
or you can use HuggingFace style:
```
from datasets import load_dataset

train_df = load_dataset('sagteam/author_profiling', split='train')
valid_df = load_dataset('sagteam/author_profiling', split='validation')
test_df = load_dataset('sagteam/author_profiling', split='test')
```

#### Here are some statistics:

1. For Train file: 
- No. of documents -- 9564;
- No. of unique texts -- 9553;
- Text length in characters -- min: 197, max: 2984, mean: 500.5;
- No. of documents written -- by men: 4704, by women: 4860;
- No. of unique authors -- 2344; men: 1172, women: 1172;
- Age of the authors -- min: 13, max: 80, mean: 31.2;
- No. of documents by age group -- 0-19: 813, 20-29: 4188, 30-39: 2697, 40-49: 1194, 50+: 672;
- No. of documents with gender imitation: 1215; without gender imitation: 2430; not applicable: 5919;
- No. of documents with age imitation -- younger: 1973; older: 1973; without age imitation: 1973; not applicable: 3645;
- No. of documents with style imitation: 1215; without style imitation: 2430; not applicable: 5919.

2. For Valid file: 
- No. of documents -- 1320;
- No. of unique texts -- 1316;
- Text length in characters -- min: 200, max: 2809, mean: 520.8;
- No. of documents written -- by men: 633, by women: 687;
- No. of unique authors -- 336; men: 168, women: 168;
- Age of the authors -- min: 15, max: 79, mean: 32.2;
- No. of documents by age group -- 1-19: 117, 20-29: 570, 30-39: 339, 40-49: 362, 50+: 132;
- No. of documents with gender imitation: 156; without gender imitation: 312; not applicable: 852;
- No. of documents with age imitation -- younger: 284; older: 284; without age imitation: 284; not applicable: 468;
- No. of documents with style imitation: 156; without style imitation: 312; not applicable: 852.

3. For Test file: 
- No. of documents -- 2564;
- No. of unique texts -- 2561;
- Text length in characters -- min: 199, max: 3981, mean: 515.6;
- No. of documents written -- by men: 1290, by women: 1274;
- No. of unique authors -- 672; men: 336, women: 336;
- Age of the authors -- min: 12, max: 67, mean: 31.8;
- No. of documents by age group -- 1-19: 195, 20-29: 1131, 30-39: 683, 40-49: 351, 50+: 204;
- No. of documents with gender imitation: 292; without gender imitation: 583; not applicable: 1689;
- No. of documents with age imitation -- younger: 563; older: 563; without age imitation: 563; not applicable: 875;
- No. of documents with style imitation: 292; without style imitation: 583; not applicable: 1689.

### Supported Tasks and Leaderboards

This dataset is intended for multi-class and multi-label text classification.

The baseline models currently achieve the following F1-weighted metrics scores (table):

|      Model name     | gender | age_group | gender_imitation | age_imitation | style_imitation | no_imitation | average |
| ------------------- | ------ | --------- | ---------------- | ------------- | --------------- | ------------ | ------- |
| Dummy-stratified    |  0.49  |   0.29    |      0.56        |     0.32      |      0.57       |     0.55     |  0.46   |
| Dummy-uniform       |  0.49  |   0.23    |      0.51        |     0.32      |      0.51       |     0.51     |  0.43   |
| Dummy-most_frequent |  0.34  |   0.27    |      0.53        |     0.17      |      0.53       |     0.53     |  0.40   |
| LinearSVC + TF-IDF  |  0.67  |   0.37    |      0.62        |     0.72      |      0.71       |     0.71     |  0.63   |

### Languages

The text in the dataset is in Russian.

## Dataset Structure

### Data Instances

Each instance is a text in Russian with some author profiling annotations.

An example for an instance from the dataset is shown below:
```
{
  'id': 'crowdsource_4916',
  'text': 'Ты очень симпатичный, Я давно не с кем не встречалась. Ты мне сильно понравился, ты умный интересный и удивительный, приходи ко мне в гости , у меня есть вкусное вино , и приготовлю вкусный ужин, посидим пообщаемся, узнаем друг друга поближе.',
  'account_id': 'account_#1239',
  'author_id': 411,
  'age': 22,
  'age_group': '20-29',
  'gender': 'male',
  'no_imitation': 'with_any_imitation',
  'age_imitation': 'None',
  'gender_imitation': 'with_gender_imitation',
  'style_imitation': 'no_style_imitation'
}
```

### Data Fields

Data Fields includes:
- id -- unique identifier of the sample;

- text -- authors text written by a crowdsourcing user;

- author_id -- unique identifier of the user;

- account_id -- unique identifier of the crowdsource account;

- age -- age annotations;

- age_group -- age group annotations;

- no_imitation -- imitation annotations. 
  Label codes: 
    - 'with_any_imitation' -- there is some imitation in the text;
    - 'no_any_imitation' -- the text is written without any imitation

- age_imitation -- age imitation annotations. 
  Label codes: 
    - 'younger' -- someone younger than the author is imitated in the text;
    - 'older' -- someone older than the author is imitated in the text;
    - 'no_age_imitation' -- the text is written without age imitation;
    - 'None' -- not supported (the text was not written for this task)

- gender_imitation -- gender imitation annotations. 
  Label codes: 
    - 'no_gender_imitation' -- the text is written without gender imitation;
    - 'with_gender_imitation' -- the text is written with a gender imitation;
    - 'None' -- not supported (the text was not written for this task)

- style_imitation -- style imitation annotations. 
  Label codes: 
  - 'no_style_imitation' -- the text is written without style imitation; 
  - 'with_style_imitation' -- the text is written with a style imitation; 
  - 'None' -- not supported (the text was not written for this task).

### Data Splits

The dataset includes a set of train/valid/test splits with 9564, 1320 and 2564 texts respectively. 
The unique authors do not overlap between the splits.

## Dataset Creation

### Curation Rationale

The formed dataset of examples consists of texts in Russian using a crowdsourcing platform. The created dataset can be used to improve the accuracy of supervised classifiers in author profiling tasks.

### Source Data

#### Initial Data Collection and Normalization

Data was collected from crowdsource platform. Each text was written by the author specifically for the task provided.

#### Who are the source language producers?

Russian-speaking Yandex.Toloka users.

### Annotations

#### Annotation process

We used a crowdsourcing platform to collect texts. Each respondent is asked to fill a questionnaire including their gender, age and native language. 

For age imitation task the respondents are to choose a
topic out of a few suggested, and write three texts on it:
1) Text in their natural manner;
2) Text imitating the style of someone younger;
3) Text imitating the style of someone older.

For gender and style imitation task each author wrote three texts in certain different styles: 
1) Text in the authors natural style;
2) Text imitating other gender style;
3) Text in a different style but without gender imitation.

The topics to choose from are the following.
- An attempt to persuade some arbitrary listener to meet the respondent at their place;
- A story about some memorable event/acquisition/rumour or whatever else the imaginary listener is supposed to enjoy;
- A story about oneself or about someone else, aiming to please the listener and win their favour;
- A description of oneself and one’s potential partner for a dating site; 
- An attempt to persuade an unfamiliar person to come;
- A negative tour review.

The task does not pass checking and is considered improper work if it contains:
- Irrelevant answers to the questionnaire;
- Incoherent jumble of words;
- Chunks of text borrowed from somewhere else;
- Texts not conforming to the above list of topics.

Texts checking is performed firstly by automated search for borrowings (by an anti-plagiarism website), and then by manual review of compliance to the task.

#### Who are the annotators?

Russian-speaking Yandex.Toloka users.

### Personal and Sensitive Information

All personal data was anonymized. Each author has been assigned an impersonal, unique identifier.

## Considerations for Using the Data

### Social Impact of Dataset

[Needs More Information]

### Discussion of Biases

[Needs More Information]

### Other Known Limitations

[Needs More Information]

## Additional Information

### Dataset Curators

Researchers at AI technology lab at NRC "Kurchatov Institute". See the [website](https://sagteam.ru/).

### Licensing Information

Apache License 2.0.

### Citation Information

If you have found our results helpful in your work, feel free to cite our publication. 
```
@article{сбоев2022сравнение,
  title={СРАВНЕНИЕ ТОЧНОСТЕЙ МЕТОДОВ НА ОСНОВЕ ЯЗЫКОВЫХ И ГРАФОВЫХ НЕЙРОСЕТЕВЫХ МОДЕЛЕЙ ДЛЯ ОПРЕДЕЛЕНИЯ ПРИЗНАКОВ АВТОРСКОГО ПРОФИЛЯ ПО ТЕКСТАМ НА РУССКОМ ЯЗЫКЕ},
  author={Сбоев, АГ and Молошников, ИА and Рыбка, РБ and Наумов, АВ and Селиванов, АА},
  journal={Вестник Национального исследовательского ядерного университета МИФИ},
  volume={10},
  number={6},
  pages={529--539},
  year={2021},
  publisher={Общество с ограниченной ответственностью МАИК "Наука/Интерпериодика"}
}
```
### Contributions

Thanks to [@naumov-al](https://github.com/naumov-al) for adding this dataset.
