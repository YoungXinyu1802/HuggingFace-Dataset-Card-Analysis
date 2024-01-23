---
language: 
  - af
  - am
  - arz
  - ha
  - ig
  - ary
  - nso
  - sn
  - so
  - sw
  - ti
  - tw
  - wo
  - yo
  - zu

    
multilinguality:
  - multilingual   
   
task_categories:
  - text-retrieval
license: apache-2.0

viewer: true
---

# Dataset Summary
AfriCLIRMatrix is a test collection for cross-lingual information retrieval research in 15 diverse African languages. This resource comprises English queries with query–document relevance judgments in 15 African languages automatically mined from Wikipedia

This dataset stores documents of AfriCLIRMatrix. To access the queries and judgments, please refer to [castorini/africlirmatrix](https://github.com/castorini/africlirmatrix).

# Dataset Structure
The only configuration here is the `language`.

An example of document data entry looks as follows:
```
{
  'id': '62443', 
  'contents': 'Acyloin condensation jẹ́ ìyọkúrò àsopọ̀ àwọn carboxylic ester pẹ̀lú lílò metalic sodium lati ṣèdá α-hydroxyketone, tí wọ́n tún mọ̀ sí. Àdàpọ̀ ṣisẹ́ yìí jẹ́ èyí tó ...'
}

```
# Load Dataset
An example to load the dataset:
```
language = 'yoruba'
dataset = load_dataset('castorini/africlirmatrix', language, 'train')
```
# Citation Information

```
coming soon
```