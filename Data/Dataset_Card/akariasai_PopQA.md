# Dataset Card for PopQA 

## Dataset Summary 
PopQA is a large-scale open-domain question answering (QA) dataset, consisting of 14k entity-centric QA pairs. Each question is created by converting a knowledge tuple retrieved from Wikidata using a template. Each question come with the original `subject_entitiey`, `object_entity`and `relationship_type` annotation, as well as Wikipedia monthly page views.  

## Languages
The dataset contains samples in English only.

## Dataset Structure
### Data Instances
- Size of downloaded dataset file: 5.2 MB

## Data Fields
- `id`: question id
- `subj`: subject entity name
- `prop`: relationship type
- `obj`: object entity name
- `subj_id`: Wikidata ID of the subject entity
- `prop_id`: Wikidata relationship type ID
- `obj_id`: Wikidata ID of the object entity
- `s_aliases`: aliases of the subject entity
- `o_aliases`: aliases of the object entity
- `s_uri`: Wikidata URI of the subject entity   
- `o_uri`: Wikidata URI of the object entity
- `s_wiki_title`: Wikipedia page title of the subject entity
- `o_wiki_title`: Wikipedia page title of the object entity
- `s_pop`: Wikipedia monthly pageview of the subject entity
- `o_pop`: Wikipedia monthly pageview of the object entity
- `question`: PopQA question
- `possible_answers`: a list of the gold answers.

## Citation Information
```
@article{ mallen2023llm_memorization ,
  title={When Not to Trust Language Models: Investigating Effectiveness and Limitations of Parametric and Non-Parametric Memories },
  author={ Mallen, Alex and Asai,Akari and  Zhong, Victor and Das, Rajarshi and Hajishirzi, Hannaneh and Khashabi, Daniel},
  journal={ arXiv preprint },
  year={ 2022 }
}
```
