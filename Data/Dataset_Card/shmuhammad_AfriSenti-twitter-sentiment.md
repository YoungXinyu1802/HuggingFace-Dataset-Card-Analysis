---
task_categories:
- text-classification
task_ids:
- sentiment-analysis
- sentiment-classification
- sentiment-scoring
- semantic-similarity-classification
- semantic-similarity-scoring
tags:
- sentiment analysis, Twitter, tweets
- sentiment
multilinguality:
- monolingual
- multilingual
size_categories:
- 100K<n<1M
language:
- amh
- ary
- ar
- arq
- hau
- ibo
- kin
- por
- pcm
- eng
- oro
- swa
- tir
- twi
- tso
- yor
pretty_name: AfriSenti
---

# Dataset Card for AfriSenti Dataset

<p align="center">
<img src="https://raw.githubusercontent.com/afrisenti-semeval/afrisent-semeval-2023/main/images/afrisenti-twitter.png", width="700" height="500">

--------------------------------------------------------------------------------

## Dataset Description


- **Homepage:** https://github.com/afrisenti-semeval/afrisent-semeval-2023
- **Repository:** [GitHub](https://github.com/afrisenti-semeval/afrisent-semeval-2023)
- **Paper:**  [AfriSenti: AfriSenti: A Twitter Sentiment Analysis Benchmark for African Languages](https://arxiv.org/pdf/2302.08956.pdf)
- **Paper:**  [NaijaSenti: A Nigerian Twitter Sentiment Corpus for Multilingual Sentiment Analysis](https://arxiv.org/pdf/2201.08277.pdf)
- **Leaderboard:** N/A
- **Point of Contact:** [shamsuddeen Muhammad](shamsuddeen2004@gmail.com)


### Dataset Summary

 AfriSenti is the largest sentiment analysis dataset for under-represented African languages, covering 110,000+ annotated tweets in 14 African languages (Amharic, Algerian Arabic, Hausa, Igbo, Kinyarwanda, Moroccan Arabic, Mozambican Portuguese, Nigerian Pidgin, Oromo, Swahili, Tigrinya, Twi, Xitsonga, and Yoruba). 
 
 The datasets are used in the first Afrocentric SemEval shared task, SemEval 2023 Task 12: Sentiment analysis for African languages (AfriSenti-SemEval). AfriSenti allows the research community to build sentiment analysis systems for various African languages and enables the study of sentiment and contemporary language use in African languages.


### Supported Tasks and Leaderboards

The AfriSenti can be used for a wide range of sentiment analysis tasks in African languages, such as sentiment classification, sentiment intensity analysis, and emotion detection. This dataset is suitable for training and evaluating machine learning models for various NLP tasks related to sentiment analysis in African languages.
[SemEval 2023 Task 12 : Sentiment Analysis for African Languages](https://codalab.lisn.upsaclay.fr/competitions/7320)


### Languages

14 African languages (Amharic (amh), Algerian Arabic (ary), Hausa(hau), Igbo(ibo), Kinyarwanda(kin), Moroccan Arabic/Darija(arq), Mozambican Portuguese(por), Nigerian Pidgin (pcm), Oromo (oro), Swahili(swa), Tigrinya(tir), Twi(twi), Xitsonga(tso), and Yoruba(yor)). 


## Dataset Structure

### Data Instances

For each instance, there is a string for the tweet and a string for the label. See the AfriSenti [dataset viewer](https://huggingface.co/datasets/shmuhammad/AfriSenti/viewer/shmuhammad--AfriSenti/train) to explore more examples.


```
{
  "tweet": "string",
  "label": "string"
}
```


### Data Fields

The data fields are:

```
tweet: a string feature.
label: a classification label, with possible values including positive, negative and neutral.
```


### Data Splits

The AfriSenti dataset has 3 splits: train, validation, and test. Below are the statistics for Version 1.0.0 of the dataset.

|  | ama | arq | hau | ibo | ary | orm | pcm | pt-MZ | kin | swa | tir | tso | twi | yo |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| train | 5,982 | 1,652 | 14,173 | 10,193  |  5,584| - | 5,122  | 3,064  | 3,303 | 1,811 | - | 805 | 3,482| 8,523 |
| dev | 1,498 | 415 | 2,678 | 1,842 | 1,216 | 397 | 1,282 | 768 | 828 | 454 | 399  | 204 | 389 | 2,091 |
| test | 2,000  | 959 | 5,304 | 3,683 | 2,962 | 2,097  | 4,155  | 3,663 | 1,027 | 749  | 2,001 | 255 | 950 | 4,516 |
| total | 9,483  | 3,062 | 22,155 | 15,718  | 9,762 | 2,494  | 10,559 | 7,495 | 5,158  | 3,014 | 2,400 | 1,264 | 4,821 | 15,130 |

### How to use it


```python
from  datasets  import  load_dataset

# you can load specific languages (e.g., Amharic). This download train, validation and test sets. 
ds = load_dataset("shmuhammad/AfriSenti-twitter-sentiment", "amh")

# train set only
ds = load_dataset("shmuhammad/AfriSenti-twitter-sentiment", "amh", split = "train")

# test set only
ds = load_dataset("shmuhammad/AfriSenti-twitter-sentiment", "amh", split = "test")

# validation set only
ds = load_dataset("shmuhammad/AfriSenti-twitter-sentiment", "amh", split = "validation")


```



## Dataset Creation

### Curation Rationale

AfriSenti Version 1.0.0 aimed to be used in the first Afrocentric SemEval shared task **[SemEval 2023 Task 12: Sentiment analysis for African languages (AfriSenti-SemEval)](https://afrisenti-semeval.github.io)**.


### Source Data

Twitter

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?



[More Information Needed]

### Personal and Sensitive Information

We anonymized the tweets by replacing all *@mentions* by *@user* and removed all URLs.


## Considerations for Using the Data

### Social Impact of Dataset

The Afrisenti dataset has the potential to improve sentiment analysis for African languages, which is essential for understanding and analyzing the diverse perspectives of people in the African continent. This dataset can enable researchers and developers to create sentiment analysis models that are specific to African languages, which can be used to gain insights into the social, cultural, and political views of people in African countries. Furthermore, this dataset can help address the issue of underrepresentation of African languages in natural language processing, paving the way for more equitable and inclusive AI technologies.

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

AfriSenti is an extension of NaijaSenti, a dataset consisting of four Nigerian languages: Hausa, Yoruba, Igbo, and Nigerian-Pidgin. This dataset has been expanded to include other 10 African languages, and was curated with the help of the following:


| Language | Dataset Curators |
|---|---|
| Algerian Arabic (arq) | Nedjma Ousidhoum, Meriem Beloucif | 
| Amharic (ama)  | Abinew Ali Ayele, Seid Muhie Yimam | 
| Hausa (hau) | Shamsuddeen Hassan Muhammad, Idris Abdulmumin, Ibrahim Said, Bello Shehu Bello |  
| Igbo (ibo) | Shamsuddeen Hassan Muhammad, Idris Abdulmumin, Ibrahim Said, Bello Shehu Bello | 
| Kinyarwanda (kin)| Samuel Rutunda | 
| Moroccan Arabic/Darija (ary) | Oumaima Hourrane | 
| Mozambique Portuguese (pt-MZ)  | Felermino Dário Mário António Ali | 
| Nigerian Pidgin (pcm)  | Shamsuddeen Hassan Muhammad, Idris Abdulmumin, Ibrahim Said, Bello Shehu Bello | 
| Oromo (orm)  | Abinew Ali Ayele, Seid Muhie Yimam, Hagos Tesfahun Gebremichael, Sisay Adugna Chala, Hailu Beshada Balcha, Wendimu Baye Messell, Tadesse Belay | 
| Swahili (swa)  | Davis Davis | 
| Tigrinya (tir)  | Abinew Ali Ayele, Seid Muhie Yimam, Hagos Tesfahun Gebremichael, Sisay Adugna Chala, Hailu Beshada Balcha, Wendimu Baye Messell, Tadesse Belay | 
| Twi (twi)  | Salomey Osei, Bernard Opoku, Steven Arthur | 
| Xithonga (tso)  | Felermino Dário Mário António Ali | 
| Yoruba (yor)  | Shamsuddeen Hassan Muhammad, Idris Abdulmumin, Ibrahim Said, Bello Shehu Bello | 
 
  
  


### Licensing Information

This AfriSenti is licensed under a Creative Commons Attribution 4.0 International License




### Citation Information

```
@inproceedings{Muhammad2023AfriSentiAT,
  title={AfriSenti: A Twitter Sentiment Analysis Benchmark for African Languages},
  author={Shamsuddeen Hassan Muhammad and Idris Abdulmumin and Abinew Ali Ayele and Nedjma Ousidhoum and David Ifeoluwa Adelani and Seid Muhie Yimam and Ibrahim Sa'id Ahmad and Meriem Beloucif and Saif Mohammad and Sebastian Ruder and Oumaima Hourrane and Pavel Brazdil and Felermino D'ario M'ario Ant'onio Ali and Davis Davis and Salomey Osei and Bello Shehu Bello and Falalu Ibrahim and Tajuddeen Gwadabe and Samuel Rutunda and Tadesse Belay and Wendimu Baye Messelle and Hailu Beshada Balcha and Sisay Adugna Chala and Hagos Tesfahun Gebremichael and Bernard Opoku and Steven Arthur},
  year={2023}
}
```


```
@inproceedings{muhammad-etal-2023-semeval,
  title="{S}em{E}val-2023 Task 12:  Sentiment Analysis for African Languages ({A}fri{S}enti-{S}em{E}val)",
  author="Muhammad, Shamsuddeen Hassan and
   Yimam, Seid and 
   Abdulmumin, Idris and 
   Ahmad, Ibrahim Sa'id  and 
   Ousidhoum, Nedjma, and
   Ayele, Abinew, and 
   Adelani, David and 
   Ruder, Sebastian and  
   Beloucif, Meriem and 
   Bello, Shehu Bello and 
   Mohammad, Saif M.",
  booktitle="Proceedings of the 17th International Workshop on Semantic Evaluation (SemEval-2023)",
  month=jul,
  year="2023",
}
```


### Contributions

[More Information Needed]