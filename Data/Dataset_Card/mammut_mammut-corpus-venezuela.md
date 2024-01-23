---
annotations_creators:
- no-annotation
language_creators:
- expert-generated
language:
- es
language_bcp47:
- es-VE
license:
- cc-by-nc-nd-4.0
multilinguality:
- monolingual
pretty_name: mammut-corpus-venezuela
size_categories:
- unknown
source_datasets:
- original
task_categories:
- sequence-modeling
task_ids:
- language-modeling
---

# mammut-corpus-venezuela

HuggingFace Dataset

## 1. How to use

How to load this dataset directly with the datasets library:

`>>> from datasets import load_dataset`   
`>>> dataset = load_dataset("mammut-corpus-venezuela")`  

## 2. Dataset Summary

**mammut-corpus-venezuela** is a dataset for Spanish language modeling. This dataset comprises a large number of Venezuelan and Latin-American Spanish texts, manually selected and collected in 2021. The data was collected by a process of web scraping from different portals, downloading of Telegram group chats' history, and selecting of Venezuelan and Latin-American Spanish corpus available online. The texts come from Venezuelan Spanish speakers, subtitlers, journalists, politicians, doctors, writers, and online sellers. Social biases may be present, and a percentage of the texts may be fake or contain misleading or offensive language.

Each record in the dataset contains the author of the text (anonymized for conversation authors), the date on which the text entered in the corpus, the text which was automatically tokenized at sentence level for sources other than conversations, the source of the text, the title of the text, the number of tokens (excluding punctuation marks) of the text, and the linguistic register of the text.

The dataset counts with a train split and a test split.

## 3. Supported Tasks and Leaderboards

This dataset can be used for language modeling.

## 4. Languages

The dataset contains Venezuelan and Latin-American Spanish.

## 5. Dataset Structure

Dataset structure features.

### 5.1 Data Instances

An example from the dataset:
  
  
    "AUTHOR":"author in title",     
    "TITLE":"Luis Alberto Buttó: Hecho en socialismo",         
    "SENTENCE":"Históricamente, siempre fue así.",
    "DATE":"2021-07-04 07:18:46.918253",      
    "SOURCE":"la patilla",      
    "TOKENS":"4",      
    "TYPE":"opinion/news",   


The average word token count are provided below:

### 5.2 Total of tokens (no spelling marks)

Train: 92,431,194.    
Test: 4,876,739 (in another file).   

### 5.3 Data Fields

The data have several fields:

  AUTHOR: author of the text. It is anonymized for conversation authors.   
  DATE: date on which the text was entered in the corpus.    
  SENTENCE: text. It was automatically tokenized for sources other than conversations.    
  SOURCE: source of the texts.    
  TITLE: title of the text from which SENTENCE originates.    
  TOKENS: number of tokens (excluding punctuation marks) of SENTENCE.     
  TYPE: linguistic register of the text.     

### 5.4 Data Splits

The mammut-corpus-venezuela dataset has 2 splits: train and test. Below are the statistics:

Number of Instances in Split.  

Train: 2,983,302.   
Test: 157,011.   

## 6. Dataset Creation

### 6.1 Curation Rationale

The purpose of the mammut-corpus-venezuela dataset is language modeling. It can be used for pre-training a model from scratch or for fine-tuning on another pre-trained model.

### 6.2 Source Data

**6.2.1 Initial Data Collection and Normalization**

The data consists of opinion articles and text messages. It was collected by a process of web scraping from different portals, downloading of Telegram group chats’ history and selecting of Venezuelan and Latin-American Spanish corpus available online.

The text from the web scraping process was separated in sentences and was automatically tokenized for sources other than conversations.

An arrow parquet file was created.

Text sources: El Estímulo (website), cinco8 (website), csm-1990 (oral speaking corpus), "El atajo más largo" (blog), El Pitazo (website), La Patilla (website), Venezuelan movies subtitles, Preseea Mérida (oral speaking corpus), Prodavinci (website), Runrunes (website), and Telegram group chats.

**6.2.2 Who are the source language producers?**

The texts come from Venezuelan Spanish speakers, subtitlers, journalists, politicians, doctors, writers, and online sellers.

## 6.3 Annotations

**6.3.1 Annotation process**

At the moment the dataset does not contain any additional annotations.

**6.3.2 Who are the annotators?**

Not applicable.

### 6.4 Personal and Sensitive Information

The data is partially anonymized. Also, there are messages from Telegram selling chats, some percentage of these messages may be fake or contain misleading or offensive language.

## 7. Considerations for Using the Data

### 7.1 Social Impact of Dataset

The purpose of this dataset is to help the development of language modeling models (pre-training or fine-tuning) in Venezuelan Spanish.

### 7.2 Discussion of Biases

Most of the content comes from political, economical and sociological opinion articles. Social biases may be present.

### 7.3 Other Known Limitations

(If applicable, description of the other limitations in the data.)

Not applicable.

## 8. Additional Information

### 8.1 Dataset Curators

The data was originally collected by Lino Urdaneta and Miguel Riveros from Mammut.io.

### 8.2 Licensing Information

Not applicable.

### 8.3 Citation Information

Not applicable.

### 8.4 Contributions

Not applicable.
