---
annotations_creators:
- crowdsourced
- expert-generated
language:
- en
multilinguality:
- monolingual
size_categories:
- 100M<n<1B
task_categories:
- other
---

Preprocessed version of Super-Natural-Instructions from https://github.com/allenai/natural-instructions/tree/master/splits. The same inputs may appear with different outputs, thus to avoid duplicate inputs, you can deduplicate by the `id` or the `inputs` field.

This is modified from https://huggingface.co/datasets/Muennighoff/natural-instructions

with a few improvements:

1. Adds positive/negative examples, outputs, explanations for each task, to
    support different task definitions.
2. Adds an "eval" field which which is True for the first 100 examples of each
    test task (119 * 100 = 11900 examples). This field indicates whether an example
    is part of the abbreviated + balanced test split. See
    https://github.com/allenai/natural-instructions/blob/master/src/reorder_instances_for_testing.py.
3. Adds an "eval" field to the training dataset, which can be used as an
    in-domain evaluation set. To do so, we sample a balanced set the first 15
    examples of each train split (757 * 15 = 11355 examples) and mark the "eval"
    field as true.
