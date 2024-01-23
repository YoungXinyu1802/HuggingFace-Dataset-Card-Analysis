---
language:
- en
license:
- other
multilinguality:
- monolingual
size_categories:
- 1<n<1K
pretty_name: Relation Mapping
---
# Dataset Card for "relbert/relation_mapping"
## Dataset Description
- **Repository:** [RelBERT](https://github.com/asahi417/relbert)
- **Paper:** [https://www.jair.org/index.php/jair/article/view/10583](https://www.jair.org/index.php/jair/article/view/10583)
- **Dataset:** Relation Mapping

### Dataset Summary
Relation Mapping is a task to choose optimal combination of word pairs (see more detail in the [paper](https://www.jair.org/index.php/jair/article/view/10583)).


Relation mapping `M` is the set of bijective map in between two sets of terms (`A` and `B`):
```
[set `A`]: ("solar system", "sun", "planet", "mass", "attracts", "revolves", "gravity")
[set `B`]: ("atom", "nucleus", "electron", "charge", "attracts", "revolves", "electromagnetism")

[Relation Mapping `M`]
* "solar system"   -> "atom"
* "sun"            -> "nucleus"
* "planet"         -> "electron"
* "mass"           -> "charge"
* "attracts"       -> "attracts"
* "revolves"       -> "revolves"
* "gravity"        -> "electromagnetism"
```

***[Relation Mapping Problem](https://www.jair.org/index.php/jair/article/view/10583)*** is the task to identify the mapping `M` given the sets of terms `A` and `B`.


## Dataset Structure
### Data Instances
An example looks as follows.
```
{
 "id": "m10",
 "reference": ["seeing", "understanding"],
 "source": ["seeing", "light", "illuminating", "darkness", "view", "hidden"],
 "target": ["understanding", "knowledge", "explaining", "confusion", "interpretation", "secret"],
 "agreement": [68.2, 77.3, 86.4, 86.4, 68.2, 86.4],
 "pos": ["vbg", "nn", "vbg", "nn", "nn", "jj"],
 "target_random": ["knowledge", "interpretation", "explaining", "confusion", "understanding", "secret"]
}
```

- `source`: A list of terms, which is the source of the relation mapping from.
- `target_random`: A list of terms, where we want to find a mapping from `source` to.
- `target`: A correctly ordered `target_random` that aligns with the `source`.

Given `source` and `target_random`, the task is to predict the correct order of `target_random` so that it matches `target`.
In average 7 terms are in the set, so the total number of possible order is 5040.


### Data Splits
|  name   |test|
|---------|----:|
|relation_mapping| 20 |


### Citation Information
```
@article{turney2008latent,
  title={The latent relation mapping engine: Algorithm and experiments},
  author={Turney, Peter D},
  journal={Journal of Artificial Intelligence Research},
  volume={33},
  pages={615--655},
  year={2008}
}
```