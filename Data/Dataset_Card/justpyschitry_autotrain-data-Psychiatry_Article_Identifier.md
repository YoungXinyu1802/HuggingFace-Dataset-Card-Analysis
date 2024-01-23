---
task_categories:
- text-classification

---
# AutoTrain Dataset for project: Psychiatry_Article_Identifier

## Dataset Descritpion

This dataset has been automatically processed by AutoTrain for project Psychiatry_Article_Identifier.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "text": "diffuse actinic keratinocyte dysplasia",
    "target": 15
  },
  {
    "text": "cholesterol atheroembolism",
    "target": 8
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "text": "Value(dtype='string', id=None)",
  "target": "ClassLabel(num_classes=20, names=['Certain infectious or parasitic diseases', 'Developmental anaomalies', 'Diseases of the blood or blood forming organs', 'Diseases of the genitourinary system', 'Mental behavioural or neurodevelopmental disorders', 'Neoplasms', 'certain conditions originating in the perinatal period', 'conditions related to sexual health', 'diseases of the circulatroy system', 'diseases of the digestive system', 'diseases of the ear or mastoid process', 'diseases of the immune system', 'diseases of the musculoskeletal system or connective tissue', 'diseases of the nervous system', 'diseases of the respiratory system', 'diseases of the skin', 'diseases of the visual system', 'endocrine  nutritional or metabolic diseases', 'pregnanacy  childbirth or the puerperium', 'sleep-wake disorders'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 9828 |
| valid        | 2468 |
