---
license: cc-by-4.0
language:
- en
---

# Overview
This repository contains the dataset to the paper ["Causal Reasoning of Entities and Events in Procedural Texts" and the dataset **C**ausal **R**easoning of **E**ntities and **E**vents in **P**rocedural Texts (CREPE)](https://arxiv.org/pdf/2301.10896v2.pdf).

# Files
- `data_dev_v2.json` is the development set of CREPE.
- `data_test_v2.json` is the test set of CREPE.

---

# Explanations of the CREPE dataset
There are 6 columns in the dataset, namely `goal`, `steps`, `event`, `event_answer`, `entity`, `entity_answer`.

- `goal` denotes the goal of a procedure.

- `steps` is a list containing all steps involved in a procedure.

- `event` is an event whose likelihood of happening change due to the events in steps.

- `event_answer` is the ground truth likelihood change. See below for glossary.

- `entity` is the entity that directly relates to the `event`. Its state change will have a direct impact on the likelihood of the `event`

- `entity_answer` is the ground truth entity state change. See below for glossary.

# Glossary
|Label|Literal Mearning|
|---|---|
| 0 | `event`/`entity state` is _less likely_ to happen comparing to the previous step. |
| 1 | `event`/`entity state` is _equally likely_ to happen comparing to the previous step. |
| 2 | `event`/`entity state` is _more likely_ to happen comparing to the previous step. |

---

# Demonstration

`goal`: Clean up kitchen counter

`steps`:
1. Wear rubber gloves.
2. Get towels and wipes.
3. Use wipes to wipe kitchen counter.
4. Use towels to clean kitchen counter.
5. Store the gloves.

`event`: The likelihood that "_My skin makes contact with things I touch_" after the execution of each step.

`ground truth answers`:

|Step Number|Label|Literal Mearning|
|--|------|-------|
|1|0 | "less likely" |
|2|1 | "equally likely" |
|3|1 | "equally likely" |
|4|1 | "equally likely" |
|5|2 | "more likely" |

`entity state`: _hands_ are _covered_

`ground truth answers`:

|Step Number|Label|Literal Mearning|
|--|------|-------|
|5|2 | "more likely" |
|2|1 | "equally likely" |
|3|1 | "equally likely" |
|4|1 | "equally likely" |
|1|0 | "less likely" |