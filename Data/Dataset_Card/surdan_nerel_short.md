---
language: ru
multilinguality: monolingual
task_ids:
- named-entity-recognition
---

### About DataSet

The dataset based on NEREL corpus.

For more information about original data, please visit this [source](https://github.com/dialogue-evaluation/RuNNE)

Example of preparing original data illustrated in <Prepare_original_data.ipynb> 

### Additional info

The dataset consist 29 entities, each of them can be as beginner part of entity "B-" as inner "I-".

Frequency for each entity:

- I-AGE: 284
- B-AGE: 247
- B-AWARD: 285
- I-AWARD: 466
- B-CITY: 1080
- I-CITY: 39
- B-COUNTRY: 2378
- I-COUNTRY: 128
- B-CRIME: 214
- I-CRIME: 372
- B-DATE: 2701
- I-DATE: 5437
- B-DISEASE: 136
- I-DISEASE: 80
- B-DISTRICT: 98
- I-DISTRICT: 73
- B-EVENT: 3369
- I-EVENT: 2524
- B-FACILITY: 376
- I-FACILITY: 510
- B-FAMILY: 27
- I-FAMILY: 22
- B-IDEOLOGY: 271
- I-IDEOLOGY: 20
- B-LANGUAGE: 32
- I-LAW: 1196
- B-LAW: 297
- B-LOCATION: 242
- I-LOCATION: 139
- B-MONEY: 147
- I-MONEY: 361
- B-NATIONALITY: 437
- I-NATIONALITY: 41
- B-NUMBER: 1079
- I-NUMBER: 328
- B-ORDINAL: 485
- I-ORDINAL: 6
- B-ORGANIZATION: 3339
- I-ORGANIZATION: 3354
- B-PENALTY: 73
- I-PENALTY: 104
- B-PERCENT: 51
- I-PERCENT: 37
- B-PERSON: 5148
- I-PERSON: 3635
- I-PRODUCT: 48
- B-PRODUCT: 197
- B-PROFESSION: 3869
- I-PROFESSION: 2598
- B-RELIGION: 102
- I-RELIGION: 1
- B-STATE_OR_PROVINCE: 436
- I-STATE_OR_PROVINCE: 154
- B-TIME: 187
- I-TIME: 529
- B-WORK_OF_ART: 133
- I-WORK_OF_ART: 194

You can find mapper for entity ids in <id_to_label_map.pickle> file:

```python
import pickle

with open('id_to_label_map.pickle', 'rb') as f:
    mapper = pickle.load(f)
```