---
license: gpl
task_categories:
- text-classification
language:
- en
- zh
- es
- hi
- fr
- de
- ar
- bn
- ru
- pt
- id
- ur
- ja
- pa
- jv
- tr
- ko
- mr
- uk
- sv
- 'no'
size_categories:
- 1K<n<10K
---
SMS Spam Multilingual Collection Dataset

Collection of Multilingual SMS messages tagged as spam or legitimate

About Dataset

Context

The SMS Spam Collection is a set of SMS-tagged messages that have been collected for SMS Spam research. It originally contained one set of SMS messages in English of 5,574 messages, tagged according to being ham (legitimate) or spam and later Machine Translated into Hindi, German and French.

The text has been further translated into Spanish, Chinese, Arabic, Bengali, Russian, Portuguese, Indonesian, Urdu, Japanese, Punjabi, Javanese, Turkish, Korean, Marathi, Ukrainian, Swedish, and Norwegian using M2M100_418M a multilingual encoder-decoder (seq-to-seq) model trained for Many-to-Many multilingual translation created by Facebook AI.

Content

The augmented Dataset contains multilingual text and corresponding labels.
ham- non-spam text
spam- spam text

Acknowledgments

The original English text was taken from- https://www.kaggle.com/uciml/sms-spam-collection-dataset
Hindi, German and French taken from - https://www.kaggle.com/datasets/rajnathpatel/multilingual-spam-data