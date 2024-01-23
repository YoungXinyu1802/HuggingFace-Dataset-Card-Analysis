---
annotations_creators:
- found
language_creators:
- found
language:
- es
- pt
license:
- other
multilinguality:
  all_languages:
  - multilingual
  es:
  - monolingual
  pt:
  - monolingual
paperswithcode_id: null
size_categories:
  all_languages:
  - 100K<n<1M
  es:
  - 100K<n<1M
  pt:
  - 100K<n<1M
source_datasets:
- original
task_categories:
- conditional-text-generation
- sequence-modeling
- text-classification
- text-scoring
task_ids:
- language-modeling
- sentiment-classification
- sentiment-scoring
- summarization
- topic-classification
---

# Dataset Card for MeLiSA (Mercado Libre for Sentiment Analysis)

**  **NOTE: THIS CARD IS UNDER CONSTRUCTION** **

**  **NOTE 2: THE RELEASED VERSION OF THIS DATASET IS A DEMO VERSION.** **

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
- **Webpage:** https://github.com/lpsc-fiuba/MeLiSA
- **Paper:** 
- **Point of Contact:** lestienne@fi.uba.ar

[More Information Needed]

### Dataset Summary

We provide a Mercado Libre product reviews dataset for spanish and portuguese text classification. The dataset contains reviews in these two languages collected between August 2020 and January 2021. Each record in the dataset contains the review content and title, the star rating, the country where it was pubilshed and the product category (arts, technology, etc.). The corpus is roughly balanced across stars, so each star rating constitutes approximately 20% of the reviews in each language.

|   || Spanish ||| Portugese ||
|---|:------:|:----------:|:-----:|:------:|:----------:|:-----:|
|   | Train  | Validation | Test  | Train  | Validation | Test  |
| 1 | 88.425 | 4.052      | 5.000 | 50.801 | 4.052      | 5.000 |
| 2 | 88.397 | 4.052      | 5.000 | 50.782 | 4.052      | 5.000 |
| 3 | 88.435 | 4.052      | 5.000 | 50.797 | 4.052      | 5.000 |
| 4 | 88.449 | 4.052      | 5.000 | 50.794 | 4.052      | 5.000 |
| 5 | 88.402 | 4.052      | 5.000 | 50.781 | 4.052      | 5.000 |

Table shows the number of samples per star rate in each split. There is a total of 442.108 training samples in spanish and 253.955 in portuguese. We limited the number of reviews per product to 30 and we perform a ranked inclusion of the downloaded reviews to include those with rich semantic content. In these ranking, the lenght of the review content and the valorization (difference between likes and dislikes) was prioritized. For more details on this process, see (CITATION).

Reviews in spanish were obtained from 8 different Latin Amercian countries (Argentina, Colombia, Peru, Uruguay, Chile, Venezuela and Mexico), and portuguese reviews were extracted from Brasil. To match the language with its respective country, we applied a language detection algorithm based on the works of Joulin et al. (2016a and 2016b) to determine the language of the review text and we removed reviews that were not written in the expected language.

[More Information Needed]

### Languages
The dataset contains reviews in Latin American Spanish and Portuguese.

## Dataset Structure

### Data Instances
Each data instance corresponds to a review. Each split is stored in a separated `.csv` file, so every row in each file consists on a review. For example, here we show a snippet of the spanish training split:
```csv
country,category,review_content,review_title,review_rate
...
MLA,Tecnología y electrónica / Tecnologia e electronica,Todo bien me fue muy util.,Muy bueno,2
MLU,"Salud, ropa y cuidado personal / Saúde, roupas e cuidado pessoal",No fue lo que esperaba. El producto no me sirvió.,No fue el producto que esperé ,2
MLM,Tecnología y electrónica / Tecnologia e electronica,No fue del todo lo que se esperaba.,No me fue muy funcional ahí que hacer ajustes,2
...
```

### Data Fields

- `country`: The string identifier of the country. It could be one of the following: `MLA` (Argentina), `MCO` (Colombia), `MPE` (Peru), `MLU` (Uruguay), `MLC` (Chile), `MLV` (Venezuela), `MLM` (Mexico) or `MLB` (Brasil).
- `category`: String representation of the product's category. It could be one of the following:
    - Hogar / Casa
    - Tecnologı́a y electrónica / Tecnologia e electronica
    - Salud, ropa y cuidado personal / Saúde, roupas e cuidado pessoal
    - Arte y entretenimiento / Arte e Entretenimiento
    - Alimentos y Bebidas / Alimentos e Bebidas
- `review_content`: The text content of the review.
- `review_title`: The text title of the review.
- `review_rate`: An int between 1-5 indicating the number of stars.

### Data Splits
Each language configuration comes with it's own `train`, `validation`, and `test` splits. The `all_languages` split is simply a concatenation of the corresponding split across all languages. That is, the `train` split for `all_languages` is a concatenation of the `train` splits for each of the languages and likewise for `validation` and `test`.


## Dataset Creation

### Curation Rationale
The dataset is motivated by the desire to advance sentiment analysis and text classification in Latin American Spanish and Portuguese. 

### Source Data
#### Initial Data Collection and Normalization
The authors gathered the reviews from the marketplaces in Argentina, Colombia, Peru, Uruguay, Chile, Venezuela and Mexico for the Spanish language and from Brasil for Portuguese. They prioritized reviews that contained relevant semantic content by applying a ranking filter based in the lenght and the valorization (difference betweent the number of likes and dislikes) of the review. They then ensured the correct language by applying a semi-automatic language detection algorithm, only retaining those of the target language. No normalization was applied to the review content or title.

Original products categories were grouped in higher level categories, resulting in five different types of products: "Home" (Hogar / Casa), "Technology and electronics" (Tecnologı́a y electrónica
/ Tecnologia e electronica), "Health, Dress and Personal Care" (Salud, ropa y cuidado personal / Saúde, roupas e cuidado pessoal) and "Arts and Entertainment" (Arte y entretenimiento / Arte e Entretenimiento).

#### Who are the source language producers?
The original text comes from Mercado Libre customers reviewing products on the marketplace across a variety of product categories.

### Annotations
#### Annotation process
Each of the fields included are submitted by the user with the review or otherwise associated with the review. No manual or machine-driven annotation was necessary.
#### Who are the annotators?
N/A

### Personal and Sensitive Information
Mercado Libre Reviews are submitted by users with the knowledge and attention of being public. The reviewer ID's included in this dataset are anonymized, meaning that they are disassociated from the original user profiles. However, these fields would likely be easy to deannoymize given the public and identifying nature of free-form text responses.

## Considerations for Using the Data

### Social Impact of Dataset
Although Spanish and Portuguese languages are relatively high resource, most of the data is collected from European or United State users. This dataset is part of an effort to encourage text classification research in languages other than English and European Spanish and Portuguese. Such work increases the accessibility of natural language technology to more regions and cultures. 

### Discussion of Biases
The data included here are from unverified consumers. Some percentage of these reviews may be fake or contain misleading or offensive language. 

### Other Known Limitations
The dataset is constructed so that the distribution of star ratings is roughly balanced. This feature has some advantages for purposes of classification, but some types of language may be over or underrepresented relative to the original distribution of reviews to acheive this balance.
[More Information Needed]


## Additional Information

### Dataset Curators
Published by Lautaro Estienne, Matías Vera and Leonardo Rey Vega. Managed by the Signal Processing in Comunications Laboratory of the Electronic Department at the Engeneering School of the Buenos Aires University (UBA).

### Licensing Information
Amazon has licensed this dataset under its own agreement, to be found at the dataset webpage here:
https://docs.opendata.aws/amazon-reviews-ml/license.txt

### Citation Information
Please cite the following paper if you found this dataset useful:

(CITATION)
[More Information Needed]

### Contributions

[More Information Needed]
