---
license: bigscience-openrail-m
---
This dataset is designed to be used in testing. It's derived from general-pmd/localized_narratives__ADE20k dataset


The current splits are: `['100.unique', '100.repeat', '300.unique', '300.repeat', '1k.unique', '1k.repeat', '10k.unique', '10k.repeat']`.

The `unique` ones ensure uniqueness across `text` entries.

The `repeat` ones are repeating the same 10 unique records: - these are useful for memory leaks debugging as the records are always the same and thus remove the record variation from the equation.

The default split is `100.unique`

The full process of this dataset creation, including which records were used to build it, is documented inside [general-pmd-synthetic-testing.py](https://huggingface.co/datasets/HuggingFaceM4/general-pmd-synthetic-testing/blob/main/general-pmd-synthetic-testing.py)
