---
license: cc-by-4.0
task_categories:
- text-classification
size_categories:
- 100K<n<1M
language:
- en
multilinguality:
- monolingual
pretty_name: MultiGLUE
source_datasets:
- extended|glue
language_creators:
- found
annotations_creators:
- found
---

# Dataset Card for MultiGLUE

## Dataset Description

- **Homepage:** 
- **Repository:** 
- **Paper:** 
- **Leaderboard:** 
- **Point of Contact:** 

### Dataset Summary

This dataset is a combination of the cola, mrpc, qnli, qqp, rte, sst2, and wnli subsets of the GLUE dataset. Its intended use is to benchmark language models on multitask binary classification.

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

Like the GLUE dataset, this dataset is in English.

## Dataset Structure

### Data Instances

An example instance looks like this:
```
{
  "label": 1,
  "task": "cola",
  "sentence1": "The sailors rode the breeze clear of the rocks.",
  "sentence2": null
}
```

### Data Fields

- `task`: A `string` feature, indicating the GLUE task the instance is from.
- `sentence1`: A `string` feature.
- `sentence2`: A `string` feature.
- `label`: A classification label, either 0 or 1.

### Data Splits

- `train`: 551,282 instances
- `validation`: 48,564 instances
- `test`: 404,183 instances, no classification label (same as GLUE)

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

This dataset is created by combining the cola, mrpc, qnli, qqp, rte, sst2, and wnli subsets of the GLUE dataset.

#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

[More Information Needed]

### Licensing Information

[More Information Needed]

### Citation Information

[More Information Needed]

### Contributions

[More Information Needed]