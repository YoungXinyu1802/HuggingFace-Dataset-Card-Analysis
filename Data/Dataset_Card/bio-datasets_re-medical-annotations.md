# Dataset Card for re-medical-annotations

## Dataset Description

### Dataset Summary

HuggingFace Dataset from the Inception Medical Annotations project.

This dataset can be used locally with any archive downloaded from Inception that contains relation annotations.

Loading this dataset requires `dkpro-cassis>=0.7.2`.

**Example**: load the dataset from the "RE Temporality POC"

```
import datasets

ds = datasets.load_dataset(
    "bio-datasets/re-medical-annotations",
    data_dir=<Inception Archive path>,
    labels = ["bound"],
)
```

## Dataset Structure

### Data Fields

- `text (str)`: text of the sentence
- `subj_start (int)`: start char of the relation subject mention
- `subj_end (int)`: end char of the relation subject mention, exclusive
- `subj_type (str)`: NER label of the relation subject
- `obj_start (int)`: start char of the relation object mention
- `obj_end (int)`: end char of the relation object mention, exclusive
- `obj_type (str)`: NER label of the relation object
- `relation (str)`: the relation label of this instance
