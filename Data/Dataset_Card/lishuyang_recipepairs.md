---
annotations_creators: no-annotation
language_creators: found
language: en
license: gpl-3.0
multilinguality: monolingual
size_categories:
- 10K<n<100K
source_datasets: original
task_categories:
- text-generation
pretty_name: RecipePairs
dataset_info:
- config_name: 1.0.0
  splits:
  - name: train
    num_examples: 82707
  - name: validation
    num_examples: 1096
  - name: test
    num_examples: 1011
---

RecipePairs dataset from the 2022 EMNLP paper: ["SHARE: a System for Hierarchical Assistive Recipe Editing"](https://aclanthology.org/2022.emnlp-main.761/) by Shuyang Li, Yufei Li, Jianmo Ni, and Julian McAuley.

If you would like to use this data or found it useful in your work/research, please cite the following papers:
```
@inproceedings{li-etal-2022-share,
    title = "{SHARE}: a System for Hierarchical Assistive Recipe Editing",
    author = "Li, Shuyang  and
      Li, Yufei  and
      Ni, Jianmo  and
      McAuley, Julian",
    booktitle = "Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing",
    month = dec,
    year = "2022",
    address = "Abu Dhabi, United Arab Emirates",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.emnlp-main.761",
    pages = "11077--11090",
    abstract = "The large population of home cooks with dietary restrictions is under-served by existing cooking resources and recipe generation models. To help them, we propose the task of controllable recipe editing: adapt a base recipe to satisfy a user-specified dietary constraint. This task is challenging, and cannot be adequately solved with human-written ingredient substitution rules or existing end-to-end recipe generation models. We tackle this problem with SHARE: a System for Hierarchical Assistive Recipe Editing, which performs simultaneous ingredient substitution before generating natural-language steps using the edited ingredients. By decoupling ingredient and step editing, our step generator can explicitly integrate the available ingredients. Experiments on the novel RecipePairs dataset{---}83K pairs of similar recipes where each recipe satisfies one of seven dietary constraints{---}demonstrate that SHARE produces convincing, coherent recipes that are appropriate for a target dietary constraint. We further show through human evaluations and real-world cooking trials that recipes edited by SHARE can be easily followed by home cooks to create appealing dishes.",
}

@inproceedings{majumder-etal-2019-generating,
    title = "Generating Personalized Recipes from Historical User Preferences",
    author = "Majumder, Bodhisattwa Prasad  and
      Li, Shuyang  and
      Ni, Jianmo  and
      McAuley, Julian",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)",
    month = nov,
    year = "2019",
    address = "Hong Kong, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/D19-1613",
    doi = "10.18653/v1/D19-1613",
    pages = "5976--5982",
    abstract = "Existing approaches to recipe generation are unable to create recipes for users with culinary preferences but incomplete knowledge of ingredients in specific dishes. We propose a new task of personalized recipe generation to help these users: expanding a name and incomplete ingredient details into complete natural-text instructions aligned with the user{'}s historical preferences. We attend on technique- and recipe-level representations of a user{'}s previously consumed recipes, fusing these {`}user-aware{'} representations in an attention fusion layer to control recipe text generation. Experiments on a new dataset of 180K recipes and 700K interactions show our model{'}s ability to generate plausible and personalized recipes compared to non-personalized baselines.",
}
```