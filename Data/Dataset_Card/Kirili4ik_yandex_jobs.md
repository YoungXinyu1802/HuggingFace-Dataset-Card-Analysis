---
annotations_creators:
- expert-generated
language:
- ru
language_creators:
- found
license:
- unknown
multilinguality:
- monolingual
paperswithcode_id: climate-fever
pretty_name: yandex_jobs
size_categories:
- n<1K
source_datasets:
- original
tags:
- vacancies
- jobs
- ru
- yandex
task_categories:
- text-generation
- summarization
- multiple-choice
task_ids:
- language-modeling
---

# Dataset Card for Yandex_Jobs

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
- [Considerations for Using the Data](#considerations-for-using-the-data)
- [Contributions](#contributions)

## Dataset Description
   
### Dataset Summary

This is a dataset of more than 600 IT vacancies in Russian from parsing telegram channel https://t.me/ya_jobs. All the texts are perfectly structured, no missing values.

### Supported Tasks and Leaderboards

`text-generation` with the 'Raw text column'. 

`summarization` as for getting from all the info the header. 

`multiple-choice` as for the hashtags (to choose multiple from all available in the dataset)

### Languages

The text in the dataset is in only in Russian. The associated BCP-47 code is `ru`.
## Dataset Structure

### Data Instances

The data is parsed from a vacancy of Russian IT company [Yandex](https://ya.ru/).

An example from the set looks as follows:
```
{'Header': 'Разработчик интерфейсов в группу разработки спецпроектов',
 'Emoji': '🎳',
 'Description': 'Конструктор лендингов — это инструмент Яндекса, который позволяет пользователям создавать лендинги и турбо-лендинги для Яндекс.Директа. Турбо — режим ускоренной загрузки страниц для показа на мобильных. У нас современный стек, смелые планы и высокая динамика.\nМы ищем опытного и открытого новому фронтенд-разработчика.',
 'Requirements': '• отлично знаете JavaScript
• разрабатывали на Node.js, применяли фреймворк Express
• умеете создавать веб-приложения на React + Redux
• знаете HTML и CSS, особенности их отображения в браузерах',
 'Tasks': '• разрабатывать интерфейсы',
 'Pluses': '• писали интеграционные, модульные, функциональные или браузерные тесты
• умеете разворачивать и администрировать веб-сервисы: собирать Docker-образы, настраивать мониторинги, выкладывать в облачные системы, отлаживать в продакшене
• работали с реляционными БД PostgreSQL',
 'Hashtags': '#фронтенд #турбо #JS',
 'Link': 'https://ya.cc/t/t7E3UsmVSKs6L',
 'Raw text': 'Разработчик интерфейсов в группу разработки спецпроектов🎳

Конструктор лендингов — это инструмент Яндекса, который позволяет пользователям создавать лендинги и турбо-лендинги для Яндекс.Директа. Турбо — режим ускоренной загрузки страниц для показа на мобильных. У нас современный стек, смелые планы и высокая динамика.
Мы ищем опытного и открытого новому фронтенд-разработчика.

Мы ждем, что вы:
• отлично знаете JavaScript
• разрабатывали на Node.js, применяли фреймворк Express
• умеете создавать веб-приложения на React + Redux
• знаете HTML и CSS, особенности их отображения в браузерах

Что нужно делать:
• разрабатывать интерфейсы

Будет плюсом, если вы:
• писали интеграционные, модульные, функциональные или браузерные тесты
• умеете разворачивать и администрировать веб-сервисы: собирать Docker-образы, настраивать мониторинги, выкладывать в облачные системы, отлаживать в продакшене
• работали с реляционными БД PostgreSQL

https://ya.cc/t/t7E3UsmVSKs6L

#фронтенд #турбо #JS'
}
```

### Data Fields

- `Header`: A string with a position title (str)
- `Emoji`: Emoji that is used at the end of the title position (usually asosiated with the position) (str)
- `Description`: Short description of the vacancy (str)
- `Requirements`: A couple of required technologies/programming languages/experience (str)
- `Tasks`: Examples of the tasks of the job position (str)
- `Pluses`: A couple of great points for the applicant to have (technologies/experience/etc)
- `Hashtags`: A list of hashtags assosiated with the job (usually programming languages) (str)
- `Link`: A link to a job description (there may be more information, but it is not checked) (str)
- `Raw text`: Raw text with all the formatiing from the channel. Created with other fields. (str)

### Data Splits

There is not enough examples yet to split it to train/test/val in my opinion. 

## Dataset Creation

It downloaded and parsed from telegram channel https://t.me/ya_jobs 03.09.2022. All the unparsed examples and the ones missing any field are deleted (from 1600 vacancies to only 600 without any missing fields like emojis or links) 

## Considerations for Using the Data

These vacancies are for only one IT company (yandex). This means they can be pretty specific and probably can not be generalized as any vacancies or even any IT vacancies.

## Contributions

- **Point of Contact and Author:** [Kirill Gelvan](telegram: @kirili4ik)