---
language:
- en
license:
- mit
multilinguality:
- translation
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- translation
task_ids: []
language_details: eng and engyay
---
## Dataset Description

- **Homepage:** cdleong.github.io

# Dataset Summary: 
Pig-latin machine and English parallel machine translation corpus. 

Based on [The Project Gutenberg EBook of "De Bello Gallico" and Other Commentaries](https://www.gutenberg.org/ebooks/10657)

Converted to pig-latin with https://github.com/bpabel/piglatin

Blank lines removed.

## Dataset Structure



```
DatasetDict({
    train: Dataset({
        features: ['translation'],
        num_rows: 14778
    })
    validation: Dataset({
        features: ['translation'],
        num_rows: 1000
    })
})
```

### Data Instances
```
{
  'translation': 
  {
    'eng': 'thrown into disorder they returned with more precipitation than is usual', 
    'engyay': 'own-thray into-ay isorder-day ey-thay eturned-ray ith-way ore-may ecipitation-pray an-thay is-ay usual-ay'
  }
}
```

### Data Fields

- `translation`: a dictionary containing two strings paired with a key indicating the corresponding language.

### Data Splits
- `train`: most of the data, 13,232 samples total.
- `dev`: 1k holdout samples, created with the datasets.train_test_split() function