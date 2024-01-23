---
license: cc-by-4.0
annotations_creators:
- found
language:
- en
language_creators:
- found
multilinguality:
- monolingual
pretty_name: FSTDT Quotes
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- text-classification
task_ids:
- hate-speech-detection
---

# Dataset Card for FSTDT Quotes

## Dataset Description

- **Homepage:** 
- **Repository:** 
- **Paper:** 
- **Leaderboard:** 
- **Point of Contact:** 

### Dataset Summary

FSTDT Quotes is a snapshot of the [Fundies Say the Darndest Things](https://fstdt.com/) website taken on 2023/02/03 14:16. It is intended for hate and fringe speech detection and classification.

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

FSTDT Quotes is in English.

## Dataset Structure

### Data Instances

An example instance looks like this:
```
{
  "id": "G",
  "submitter": "anonymous",
  "timestamp": "2005-05-21 00:00:00+00:00",
  "name": "Jack777 ",
  "src_url": "http://www.theologyweb.com/forum/showpost.php?p=1034624&postcount=10",
  "tags": ["#fundie"],
  "quote": "As long as evolutionists deny their theory is a theory and point out ID or whatever is bunk, people like me will pester them til they drop."
}
```

### Data Fields

- `id`: A `string` feature, the ID of the post on FSTDT.
- `submitter`: A `string` feature, the submitter of the post.
- `timestamp`: A `string` feature, the time of submission.
- `name`: A `string` feature, the (user)name of the person who is being quoted.
- `src_url`: A `string` feature, the source URL of the quote.
- `tags`: A sequence of `string` features, the tags the post has been tagged with.
- `quote`: A `string` feature, the quote itself.

### Data Splits

- `train`: 56,448 instances
- `validation`: 7,111 instances
- `test`: 7,131 instances

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

The quotes are collected from all over the internet.

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

The data is annotated by users on FSTDT.

### Personal and Sensitive Information

The dataset contains the usernames of submitters as well as those quoted. However, this information is publicly available.

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

This dataset contains large amounts of hate speech as well as pseudoscience and quackery.

### Other Known Limitations

Some quotes in the dataset are quoted from news articles depicting acts of hate, which could potentially cause misclassifications on models trained on this dataset.

## Additional Information

### Dataset Curators

[More Information Needed]

### Licensing Information

[More Information Needed]

### Citation Information

[More Information Needed]

### Contributions

[More Information Needed]