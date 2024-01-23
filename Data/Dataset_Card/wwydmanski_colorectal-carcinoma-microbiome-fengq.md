---
task_categories:
- tabular-classification
tags:
- microbiome
- tabular
- gut-microbiota
pretty_name: Colorectal Carcinoma Feng Q 2015
size_categories:
- n<1K
---

## Publication Abstract

Colorectal cancer, a commonly diagnosed cancer in the elderly, often develops slowly from benign polyps called adenoma. The gut microbiota is believed to be directly involved in colorectal carcinogenesis. The identity and functional capacity of the adenoma- or carcinoma-related gut microbe(s), however, have not been surveyed in a comprehensive manner. Here we perform a metagenome-wide association study (MGWAS) on stools from advanced adenoma and carcinoma patients and from healthy subjects, revealing microbial genes, strains and functions enriched in each group. An analysis of potential risk factors indicates that high intake of red meat relative to fruits and vegetables appears to associate with outgrowth of bacteria that might contribute to a more hostile gut environment. These findings suggest that faecal microbiome-based strategies may be useful for early diagnosis and treatment of colorectal adenoma or carcinoma.

## Dataset
156 metagenomic shotgun-sequenced faecal samples from colorectal adenoma and carcinoma patients and healthy controls

### Configurations
 - `presence-absence`
 - `CLR`

## Usage
```python
dataset = load_dataset("wwydmanski/colorectal-carcinoma-microbiome-fengq", "presence-absence")
train_dataset, test_dataset = dataset['train'], dataset['test']
X_train = np.array(train_dataset['values'])
y_train = np.array(train_dataset['target'])

X_test = np.array(test_dataset['values'])
y_test = np.array(test_dataset['target'])
```