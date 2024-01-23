---
annotations_creators:
- found
language:
- pt
language_creators:
- found
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: B2W-Reviews01
size_categories:
- 100M<n<1B
source_datasets:
- original
tags:
- reviews
task_categories:
- text-classification
task_ids:
- sentiment-analysis
- sentiment-scoring
- intent-classification
- topic-classification
---

# Dataset Card for Dataset Name

## Dataset Description

- **Repository:** https://github.com/americanas-tech/b2w-reviews01
- **Paper:** http://comissoes.sbc.org.br/ce-pln/stil2019/proceedings-stil-2019-Final-Publicacao.pdf
- **Point of Contact:** Livy Real

### Dataset Summary

B2W-Reviews01 is an open corpus of product reviews. It contains more than 130k e-commerce customer reviews, collected from the Americanas.com website between January and May, 2018. B2W-Reviews01 offers rich information about the reviewer profile, such as gender, age, and geographical location. The corpus also has two different review rates:

* the usual 5-point scale rate, represented by stars in most e-commerce websites,
* a "recommend to a friend" label, a "yes or no" question representing the willingness of the customer to recommend the product to someone else.

### Supported Tasks and Leaderboards

* Sentiment Analysis
* Topic Modeling

### Languages

* Portuguese

## Dataset Structure

### Data Instances

```
{'submission_date': '2018-01-02 06:23:22',
 'reviewer_id': '6adc7901926fc1697d34181fbd88895976b4f3f31f0102d90217d248a1fad156',
 'product_id': '123911277',
 'product_name': 'Triciclo Gangorra Belfix Cabeça Cachorro Rosa',
 'product_brand': 'belfix',
 'site_category_lv1': 'Brinquedos',
 'site_category_lv2': 'Mini Veículos',
 'review_title': 'O produto não foi entregue',
 'overall_rating': 1,
 'recommend_to_a_friend': 'Yes',
 'review_text': 'Incrível o descaso com o consumidor. O produto não chegou, apesar de já ter sido pago. Não recebo qualquer informação sobre onde se encontra o produto, ou qualquer compensação do vendedor.  Não recomendo.',
 'reviewer_birth_year': 1981,
 'reviewer_gender': 'M',
 'reviewer_state': 'RJ'}
```

### Data Fields

* **submission_date**: the date and time when the review was submitted. `"%Y-%m-%d %H:%M:%S"`.
* **reviewer_id**: a unique identifier for the reviewer.
* **product_id**: a unique identifier for the product being reviewed.
* **product_name**: the name of the product being reviewed.
* **product_brand**: the brand of the product being reviewed.
* **site_category_lv1**: the highest level category for the product on the site where the review is being submitted.
* **site_category_lv2**: the second level category for the product on the site where the review is being submitted.
* **review_title**: the title of the review.
* **overall_rating**: the overall star rating given by the reviewer on a scale of 1 to 5.
* **recommend_to_a_friend**: whether or not the reviewer would recommend the product to a friend (Yes/No).
* **review_text**: the full text of the review.
* **reviewer_birth_year**: the birth year of the reviewer.
* **reviewer_gender**: the gender of the reviewer (F/M).
* **reviewer_state**: the Brazilian state of the reviewer (e.g. RJ).

### Data Splits

|  name   |train|
|---------|----:|
|b2w-reviews01|132373|

### Citation Information

```
@inproceedings{real2019b2w,
  title={B2W-reviews01: an open product reviews corpus},
  author={Real, Livy and Oshiro, Marcio and Mafra, Alexandre},
  booktitle={STIL-Symposium in Information and Human Language Technology},
  year={2019}
}
```

### Contributions

Thanks to [@ruanchaves](https://github.com/ruanchaves) for adding this dataset.