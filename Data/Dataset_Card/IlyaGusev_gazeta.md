---
annotations_creators:
- expert-generated
- found
language_creators:
- expert-generated
- found
task_categories:
- summarization
language:
- ru
size_categories:
- 10K<n<100K
license:
- unknown
multilinguality:
- monolingual
source_datasets:
- original
paperswithcode_id: gazeta
---

# Dataset Card for Gazeta

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
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Homepage:** https://github.com/IlyaGusev/gazeta
- **Paper:** [Dataset for Automatic Summarization of Russian News](https://arxiv.org/abs/2006.11063)
- **Leaderboard:** https://paperswithcode.com/sota/text-summarization-on-gazeta
- **Point of Contact:** [Ilya Gusev](ilya.gusev@phystech.edu)

### Dataset Summary

Dataset for automatic summarization of Russian news. News and their summaries are from the Gazeta website. Summaries were parsed as the content of an HTML tag with “description” property. Additional selection of good summaries was performed. There are two versions of this dataset.

### Supported Tasks and Leaderboards

Leaderboard on Papers With Code: [text-summarization-on-gazeta](https://paperswithcode.com/sota/text-summarization-on-gazeta).

Please use the original [evaluation script](https://github.com/IlyaGusev/summarus/blob/master/evaluate.py) with the same parameters. Example:
```
python3 evaluate.py --predicted-path predictions.txt --gold-path targets.txt --language ru --tokenize-after --lower
```

### Languages

The dataset is in Russian.

### Usage

Loading version 1.0:
```python
from datasets import load_dataset
dataset = load_dataset('IlyaGusev/gazeta', revision="v1.0")
```

Loading version 2.0:
```python
from datasets import load_dataset
dataset = load_dataset('IlyaGusev/gazeta', revision="v2.0")
```

### Other datasets
Other Russian summarization datasets:
  * Russian part of [XL-Sum](https://huggingface.co/datasets/csebuetnlp/xlsum), parsed from www.bbc.com/russian, 77803 samples
  * Russian part of [MLSUM](https://huggingface.co/datasets/mlsum), parsed from www.mk.ru, 27063 samples

## Dataset Structure

### Data Instances
For each instance, there is a string for the article, a string for the summary, and a string for the url. Additionally, a string for the title and a date are provided.

```
{
  'date': '2019-10-01 15:14:05',
  'url': 'https://www.gazeta.ru/tech/2019/10/01/12698923/whatsapp_pls.shtml',
  'title': 'На последнем издыхании: у кого отключится WhatsApp',
  'summary': 'Мессенджер WhatsApp перестанет работать на ряде смартфонов — речь идет о гаджетах на базе операционных систем Android 2.3.7 и iOS 8, которые считаются устаревшими. В компании отмечают, что сервис на этих устройствах может отключиться в любой момент, поэтому будет целесообразно сменить устройство либо обновить ОС.',
  'text': 'На официальном сайте мессенджера WhatsApp появилось сообщение о том, что с 1 февраля 2020 года сервис прекратит свою работу на некоторых устаревших смартфонах. Речь идет об устройствах, работающих на базе операционных систем Android 2.3.7 и iOS 8. При этом руководство WhatsApp предупреждает, что даже до обозначенного выше дедлайна функционал мессенджера на этих ОС может быть ограничен. «В связи с тем, что мы не планируем обновлять данные операционные системы, некоторые функции могут перестать работать на них в любое время», — говорится в пресс-релизе компании. Чтобы сохранить возможность пользоваться мессенджером без проблем, следует обновить версию прошивки или приобрести новое, более современное устройство. Сообщается, что на старых версиях операционных систем уже не получится завести новый аккаунт WhatsApp или верифицировать уже существующий. При этом в WhatsApp порекомендовали пользоваться устройствами с Android 4.0.3 и более поздними версиями, а также iOS 9 и более поздними версиями. Ранее стало известно о том, что с 31 декабря 2019 года WhatsApp прекращает поддержку устройств на базе операционной системы Windows Phone, от разработки которой пришлось отказаться. Впрочем, если верить статистике , эти меры вряд ли затронут большое количество пользователей. По состоянию на май 2019 года лишь 0,3% всех владельцев Android все еще пользуются ОС версий 2.3.3–2.3.7. Что же касается iOS, то версия под номером «10» или старше установлена на 5% устройств Apple. Как уже упоминалось выше, выпуск новых гаджетов на Windows Phone и вовсе прекращен ее создателем. В середине сентября экс-сотрудник АНБ Эдвард Сноуден раскритиковал WhatsApp за несовершенную систему защиты, порекомендовав политикам пользоваться другими средствами связи. Журналист французской радиостанции France Inter отметил, что президент Франции Эмманюэль Макрон для связи использует Telegram, а премьер-министр страны Эдуар Филипп — WhatsApp. Сноуден назвал такое решение «большой ошибкой», учитывая серьезные посты, которые занимают Макрон и Филипп. По словам Сноудена, эти сервисы безопаснее обычных SMS-сообщений, но все еще «чрезвычайно опасны, если вы премьер-министр». Больше всего претензий у информатора к WhatsApp, который стал частью активов корпорации Facebook в 2014 году. Эдвард Сноуден отметил, что после приобретения мессенджера Facebook «слой за слоем» снимает различные уровни защиты сервиса, чтобы при необходимости читать переписку своих пользователей. Ранее с критикой в адрес WhatsApp выступил и глава Telegram Павел Дуров. По словам предпринимателя, после устранения одной «дыры» в мессенджере тут же появляются новые. «Все выявленные проблемы позволяют вести слежку, выглядят и функционируют как бэкдоры», — заявил Дуров. При этом Дуров подчеркнул, что WhatsApp мог быть вынужден установить бэкдоры по указанию ФБР. В июне руководство WhatsApp заявило о том, что их сервис готов судиться с юзерами за нарушение правил пользования. В список нарушений входит использование программы «не в личных целях» и применение автоматической рассылки сообщений. По данным пресс-службы WhatsApp, уже сейчас обнаружены и заморожены «миллионы аккаунтов», пойманных на «злоупотреблении». «Наша платформа изначально создавалась, чтобы помогать людям общаться с их друзьями и любимыми... Используя информацию приложения, мы нашли и заблокировали миллионы злоупотребляющих аккаунтов от использования нашей сети», – заявили в WhatsApp. В частности, нарушение происходит, если компания публично заявляет о возможности использовать WhatsApp, нарушая при этом правила пользования мессенджером. «Ничто в этом объявлении не ограничивает право WhatsApp от применения своих условий с использованием технологий. Классификаторы на основе machine learning нам в этом помогают, и мы продолжим их использовать», – добавили в команде приложения.',
}
```

Some dataset statistics are below:

| Feature | Mean Token Count | Mean Sentence Count |
|:---------|:---------|--------------------------------------------------|
| Text  | 767 | 37 |
| Summary | 50 | 3 |

### Data Splits

| Dataset Split | v1, Number of Instances in Split | v2, Number of Instances in Split |
|:---------|:---------|:---------|
| Train | 52,400 | 60,964 |
| Validation | 5,265 | 6,369 |
| Test | 5,770 | 6,793 |

## Dataset Creation

### Curation Rationale

When the first version of the dataset was collected, there were no other datasets for Russian text summarization. Even now, it is one of the few datasets for this task.

### Source Data

#### Initial Data Collection and Normalization

* The source of data is the [Gazeta](https://www.gazeta.ru/) website.
* Parsing scripts are [here](https://github.com/IlyaGusev/gazeta/tree/master/parser). 
* Cleaning and normalization Colab notebook is [here](https://colab.research.google.com/drive/1Ed_chVrslp_7vJNS3PmRC0_ZJrRQYv0C)

#### Who are the source language producers?

Texts and summaries were written by journalists at [Gazeta](https://www.gazeta.ru/).

### Annotations

#### Annotation process

[N/A]

#### Who are the annotators?

[N/A]

### Personal and Sensitive Information

The dataset is not anonymized, so individuals' names can be found in the dataset. Information about the original author is not included in the dataset.

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

It is a dataset from a single source. Thus it has a constrained text style and event perspective.

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

The data was collected by Ilya Gusev.

### Licensing Information

Legal basis for distribution of the dataset: https://www.gazeta.ru/credits.shtml, paragraph 2.1.2. All rights belong to "www.gazeta.ru". Usage of this dataset is possible only for personal purposes on a non-commercial basis.

### Citation Information

```bibtex
@InProceedings{10.1007/978-3-030-59082-6_9,
    author="Gusev, Ilya",
    editor="Filchenkov, Andrey and Kauttonen, Janne and Pivovarova, Lidia",
    title="Dataset for Automatic Summarization of Russian News",
    booktitle="Artificial Intelligence and Natural Language",
    year="2020",
    publisher="Springer International Publishing",
    address="Cham",
    pages="122--134",
    isbn="978-3-030-59082-6"
}
```

### Contributions

[N/A]