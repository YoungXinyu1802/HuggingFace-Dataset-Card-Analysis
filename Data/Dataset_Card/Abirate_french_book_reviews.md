---
annotations_creators:
- expert-generated
language_creators:
- expert-generated
- crowdsourced
language:
- fr
multilinguality:
- monolingual
source_datasets:
- original
task_categories:
- text-classification
task_ids:
- multi-label-classification
---


# ****Dataset Card for French book reviews****
# **I-Dataset Summary**
The majority of review datasets are in English. There are datasets in other languages, but not many. Through this work, I would like to enrich the datasets in the French language(my mother tongue with Arabic).  
The data was retrieved from two French websites: [Babelio](https://www.babelio.com/) and [Critiques Libres](http://www.critiqueslibres.com/)  
Like Wikipedia, these two French sites are made possible by the contributions of volunteers who use the Internet to share their knowledge and reading experiences.  
The French book reviews is a dataset of a huge number of reader reviews on French books that ill be constantly updated over time.


# **II-Supported Tasks and Leaderboards**
- Multi-label text classification : The dataset can be used to train a model for text-classification, which consists of classifying reviews by label value. Success on this task is typically measured by achieving a high or low accuracy.

# **III-Languages**
The texts in the dataset are in French (fr).

# **IV-Dataset Structure**
#### Data Instances 
A JSON-formatted example of a typical instance in the dataset:
```python
{
    "book_title": "La belle histoire des maths",
    "author": "Michel Rousselet",
    "reader_review": "C’est un livre impressionnant, qui inspire le respect 
    par la qualité de sa reliure et son contenu. Je le feuillette et je découvre
    à chaque tour de page un thème distinct magnifiquement illustré. Très beau livre !",
    "rating": 4.0,
    "label": 1
}
  ```
 #### Data Fields
 - **book_title**: The title of the book that received the reader's review,
 - **author** : The author of the book that received the reader's review,
 - **reader_review** : The text of the reader's review,
 - **rating**: A five-star rating system is used to rate the book read,
 - **label** : A post-processed field indicating if the review is positive (1), neutral(0), or negative(-1) based on the rating field. For more details, see the [Notebook of the Dataset creation](https://github.com/Abirate/Dataset_Creation_Scrapy_Project_French_book_reviews/blob/master/scrapyproject_a_to_z_dataset_book_reviews.ipynb)
 
  #### Data Splits
I kept the dataset as one block (train), so it can be shuffled and split by users later using methods of the hugging face dataset library like the (.train_test_split()) method.

# **V-Dataset Creation**
#### Curation Rationale
The majority of review datasets are in English. There are datasets in other languages, but not many. Through this work, I would like to enrich the datasets in the French language (French is my mother tongue with Arabic) and slightly contribute to advancing data science and AI, not only for English NLP tasks but for other languages around the world.  

French is an international language and it is gaining ground. In addition, it is the language of love. The richness of the French language, so appreciated around the world, is largely related to the richness of its culture. The most telling example is French literature, which has many world-famous writers, such as [Gustave Flaubert](https://en.wikipedia.org/wiki/Gustave_Flaubert), [Albert Camus](https://iep.utm.edu/camus/), [Victor Hugo](https://en.wikipedia.org/wiki/Victor_Hugo),  [Molière](https://en.wikipedia.org/wiki/Moli%C3%A8re), [Simone de Beauvoir](https://iep.utm.edu/beauvoir/), [Antoine de Saint-Exupéry](https://en.wikipedia.org/wiki/Antoine_de_Saint-Exup%C3%A9ry): the author of "Le Petit Prince" (The Little Prince), which is still among the most translated books in literary history. And one of the world-famous quotes from this book is: "Voici mon secret. Il est très simple: on ne voit bien qu'avec le coeur. L'essentiel est invisible pour les yeux." etc. 

#### Source Data
The source of Data is: two French websites: [Babelio](https://www.babelio.com/) and [Critiques Libres](http://www.critiqueslibres.com/)

#### Initial Data Collection and Normalization 

The data was collected using web scraping (with Scrapy Framework) and subjected to additional data processing. For more details, see this notebook, which details the dataset creation process. [Notebook of the Dataset creation](https://github.com/Abirate/Dataset_Creation_Scrapy_Project_French_book_reviews/blob/master/scrapyproject_a_to_z_dataset_book_reviews.ipynb)  

**Note**: This dataset will be constantly updated to include the most recent reviews on French books by aggregating the old datasets with the updated ones in order to have a huge dataset over time.
#### Who are the source Data producers ? 
I created the Dataset using web scraping, by building a spider and a crawler to scrape the two french web sites [Babelio](https://www.babelio.com/) and [Critiques Libres](http://www.critiqueslibres.com/)

#### Annotations 
Annotations are part of the initial data collection (see the script above).

# **VI-Additional Informations**
#### Dataset Curators
Abir ELTAIEF 

#### Licensing Information 
This work is licensed under [CC0: Public Domain](https://creativecommons.org/publicdomain/zero/1.0/)
#### Contributions 
Thanks to [@Abirate](https://huggingface.co/Abirate) for creating and adding this dataset.
