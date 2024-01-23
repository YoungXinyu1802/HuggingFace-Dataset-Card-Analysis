---
annotations_creators: []
language:
- en
language_creators: []
license: []
multilinguality:
- monolingual
pretty_name: recipe RL roberta base
size_categories: []
source_datasets: []
tags: []
task_categories: []
task_ids: []
---

# Dataset Description

## Structure

- Consists of 5 fields
- Each row corresponds to a policy - sequence of actions, given an initial `<START>` state, and corresponding rewards at each step.

## Fields

`steps`, `step_attn_masks`, `rewards`, `actions`, `dones`

## Field descriptions

- `steps` (List of lists of `Int`s) - tokenized step tokens of all the steps in the policy sequence (here we use the `roberta-base` tokenizer, as `roberta-base` would be used to encode each step of a recipe)
- `step_attn_masks` (List of lists of `Int`s) - Attention masks corresponding to `steps`
- `rewards` (List of `Float`s) - Sequence of rewards (normalized b/w 0 and 1) assigned per step.
- `actions` (List of lists of `Int`s) - Sequence of actions (one-hot encoded, as the action space is discrete). There are `33` different actions possible (we consider the maximum number of steps per recipe = `16`, so the action can vary from `-16` to `+16`; The class label is got by adding 16 to the actual action value)
- `dones` (List of `Bool`) - Sequence of flags, conveying if the work is completed when that step is reached, or not.

## Dataset Size

- Number of rows = `2255673`
- Maximum number of steps per row = `16`