---
license: creativeml-openrail-m
task_categories:
- summarization
language:
- az
pretty_name: Azerbaijani News Summary Dataset Card
---

# Azerbaijani News Summary Dataset Card

## Dataset Summary

I present __az-news-summary__, a comprehensive and diverse dataset comprising __143k (143,448)__ Azerbaijani news articles extracted using a set of carefully designed heuristics. The dataset covers common topics for news reports include war, government, politics, education, health, the environment, economy, business, fashion, entertainment, and sport, as well as quirky or unusual events. 

The dataset is prepared for Abstractive/Extractive summarization tasks. It can also be used in other scopes like Text Generation, Title Generation and etc.

## Dataset Structure

One example from the dataset is given below in JSON format.

```json
{'id': 33885080,

 'title': 'İsmayıllı silkələndi - Zəlzələ',

 'summary': 'Avqustun 11-də İsmayıllı rayonu ərazisində zəlzələ baş verib',

 'text': 'Azərbaycan milli elmlər akademiyası nəzdində respublika seysmoloji
          xidmət mərkəzindən  bildirilib ki, ilkin məlumatlara əsasən yeraltı təkanlar
          yerli vaxtla saat 23:03:11-də pirquludan 11 kilometr qərbdə i̇smayıllı ərazisində
          qeydə alınıb.ocağı 9 kilometr dərinlikdə yerləşən zəlzələ episentrdə 4 bal,
          ətraf rayonlarda isə 3 bala qədər hiss olunub.'}
```

## Data Fields

- `id`: ID of the news.
- `title`: The title of the news.
- `summary`:  The summary of the news.
- `text`:  The body of the news.

##  Data Splits

This dataset has 3 splits: _train_, _validation_, and _test_. \
Token counts are white space based.

| Dataset Split | Number of Instances |     Size (MB)         |
| ------------- | --------------------|:----------------------|
| Train         | 100,413             |      150              |
| Validation    | 14,344              |      21.3             |
| Test          | 28,691              |      42.8             |

## Usage

Usage is easy and takes only a few minutes. Firstly, you need to use install datasets library as follows:
```python
!pip install datasets
```
To load the dataset from the library, you need to pass the file name on the load_dataset() function. In this case:
```python
from datasets import load_dataset
dataset = load_dataset("nijatzeynalov/azerbaijani-multi-news")
```

## Dataset Curator

This dataset was curated by [Nijat Zeynalov](https://www.linkedin.com/in/nijat-zeynalov-064163142/)

#  Citation Information

```bibtex
@misc {nijatzeynalov_2023,
	author       = { {NijatZeynalov} },
	title        = { azerbaijani-multi-news (Revision 2afa300) },
	year         = 2023,
	url          = { https://huggingface.co/datasets/nijatzeynalov/azerbaijani-multi-news },
	doi          = { 10.57967/hf/0312 },
	publisher    = { Hugging Face }
}
```