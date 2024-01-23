---
language:
- en
license:
- other
multilinguality:
- monolingual
size_categories:
- 1K<n<10K
pretty_name: ConceptNet
---
# Dataset Card for "relbert/conceptnet"
## Dataset Description
- **Repository:** [RelBERT](https://github.com/asahi417/relbert)
- **Paper:** [https://ojs.aaai.org/index.php/AAAI/article/view/11164](https://ojs.aaai.org/index.php/AAAI/article/view/11164)
- **Dataset:** ConceptNet5

### Dataset Summary
ConceptNet5, which compiled to fine-tune [RelBERT](https://github.com/asahi417/relbert) model.

## Dataset Structure
### Data Instances
An example of `train` looks as follows.
```
{
    "relation_type": "AtLocation",
    "positives": [["fish", "water"], ["cloud", "sky"], ["child", "school"], ... ],
    "negatives": [["pen", "write"], ["sex", "fun"], ["soccer", "sport"], ["fish", "school"], ... ]
}
```

### Data Splits
|  name   |train|validation|
|---------|----:|---------:|
|conceptnet| 33 |      25|

### Number of Positive/Negative Word-pairs in each Split

| relation_type    |   positive (train) |   negative (train) |   positive (validation) |   negative (validation) |
|:-----------------|-------------------:|-------------------:|------------------------:|------------------------:|
| Antonym          |               3175 |   206870           |                     703 |         65330           |
| AtLocation       |               6974 |   203071           |                     727 |         65306           |
| CapableOf        |                603 |   209442           |                       0 |             0           |
| Causes           |                906 |   209139           |                      83 |         65950           |
| CausesDesire     |                195 |   209850           |                      30 |         66003           |
| CreatedBy        |                104 |   209941           |                       4 |         66029           |
| DefinedAs        |                 16 |   210029           |                       2 |         66031           |
| Desires          |                374 |   209671           |                       0 |             0           |
| DistinctFrom     |               1552 |   208493           |                     426 |         65607           |
| Entails          |                277 |   209768           |                     118 |         65915           |
| HasA             |                606 |   209439           |                      10 |         66023           |
| HasContext       |               4664 |   205381           |                    1936 |         64097           |
| HasFirstSubevent |                 66 |   209979           |                      17 |         66016           |
| HasLastSubevent  |                 82 |   209963           |                      14 |         66019           |
| HasPrerequisite  |                586 |   209459           |                     123 |         65910           |
| HasProperty      |               1397 |   208648           |                       0 |             0           |
| HasSubevent      |                644 |   209401           |                      64 |         65969           |
| InstanceOf       |                  1 |   210044           |                       0 |             0           |
| IsA              |              54028 |   156017           |                   21122 |         44911           |
| LocatedNear      |                 21 |   210024           |                       3 |         66030           |
| MadeOf           |                221 |   209824           |                      23 |         66010           |
| MannerOf         |               8762 |   201283           |                    3747 |         62286           |
| MotivatedByGoal  |                282 |   209763           |                      35 |         65998           |
| NotCapableOf     |                 17 |   210028           |                       0 |             0           |
| NotDesires       |                235 |   209810           |                       0 |             0           |
| NotHasProperty   |                 74 |   209971           |                      19 |         66014           |
| PartOf           |               6880 |   203165           |                    2629 |         63404           |
| ReceivesAction   |                290 |   209755           |                       0 |             0           |
| RelatedTo        |              61672 |   148373           |                   11356 |         54677           |
| SimilarTo        |                 82 |   209963           |                      36 |         65997           |
| SymbolOf         |                  1 |   210044           |                       0 |             0           |
| Synonym          |              52261 |   157784           |                   22391 |         43642           |
| UsedFor          |               2997 |   207048           |                     415 |         65618           |
| SUM              |             210045 |        6.72144e+06 |                   66033 |             1.58479e+06 |

### Citation Information
```
@inproceedings{speer2017conceptnet,
  title={Conceptnet 5.5: An open multilingual graph of general knowledge},
  author={Speer, Robyn and Chin, Joshua and Havasi, Catherine},
  booktitle={Thirty-first AAAI conference on artificial intelligence},
  year={2017}
}
```