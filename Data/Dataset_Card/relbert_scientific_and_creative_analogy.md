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
# Dataset Card for "relbert/scientific_and_creative_analogy"
## Dataset Description
- **Repository:** [https://github.com/taczin/SCAN_analogies](https://github.com/taczin/SCAN_analogies)
- **Paper:** [https://arxiv.org/abs/2211.15268](https://arxiv.org/abs/2211.15268)
- **Dataset:** Relation Mapping

### Dataset Summary
A dataset for relation mapping task, which is a task to choose optimal combination of word pairs (see more detail in the [paper](https://www.jair.org/index.php/jair/article/view/10583)).


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
 "id": "0",
 "reference": ["buying an item", "accepting a belief"],
 "source": ["buying an item", "buyer", "merchandise", "buying", "selling", "returning", "valuable", "worthless"],
 "target": ["accepting a belief", "believer", "belief", "accepting", "advocating", "rejecting", "true", "false"],
 "target_random": ["rejecting", "true", "false", "accepting a belief", "believer", "advocating", "belief", "accepting"],
 "type": "metaphor"
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
|relation_mapping| 45 |


### Citation Information
```
@article{czinczoll2022scientific,
  title={Scientific and Creative Analogies in Pretrained Language Models},
  author={Czinczoll, Tamara and Yannakoudakis, Helen and Mishra, Pushkar and Shutova, Ekaterina},
  journal={arXiv preprint arXiv:2211.15268},
  year={2022}
}
```