---
author: Juan Alberto López Cavallotti
date: Jan 6, 2023
license: apache-2.0
task_categories:
- translation
language:
- en
- es
- fr
- de
tags:
- grammar
- gec
- multi language
- language detection
pretty_name: Multi Lingual Grammar Error Correction Dataset
size_categories:
- 100K<n<1M
---

# Dataset Card for Multilingual Grammar Error Correction

## Dataset Description

- **Homepage:** https://juancavallotti.com
- **Paper:** https://blog.juancavallotti.com/2023/01/06/training-a-multi-language-grammar-error-correction-system/
- **Point of Contact:** Juan Alberto López Cavallotti

### Dataset Summary

This dataset can be used to train a transformer model (we used T5) to correct grammar errors in simple sentences written in English, Spanish, French, or German. 
This dataset was developed as a component for the [Squidigies](https://squidgies.app/) platform.

### Supported Tasks and Leaderboards

* **Grammar Error Correction:** By appending the prefix *fix grammar:* to the prrompt.
* **Language Detection:** By appending the prefix: *language:* to the prompt.

### Languages

* English
* Spanish
* French
* German

## Dataset Structure

### Data Instances

The dataset contains the following instances for each language:
* German 32282 sentences.
* English 51393 sentences.
* Spanish 67672 sentences.
* French 67157 sentences.

### Data Fields

* `lang`: The language of the sentence
* `sentence`: The original sentence. 
* `modified`: The corrupted sentence.
* `transformation`: The primary transformation used by the synthetic data generator.
* `sec_transformation`: The secondary transformation (if any) used by the synthetic data generator.

### Data Splits

* `train`: There isn't a specific split defined. I recommend using 1k sentences sampled randomly from each language, combined with the SacreBleu metric.

## Dataset Creation

### Curation Rationale

This dataset was generated synthetically through code with the help of information of common grammar errors harvested throughout the internet.

### Source Data

#### Initial Data Collection and Normalization

The source grammatical sentences come from various open-source datasets, such as Tatoeba.

#### Who are the source language producers?

* Juan Alberto López Cavallotti

### Annotations

#### Annotation process

The annotation is automatic and produced by the generation script.

#### Who are the annotators?

* Data generation script by Juan Alberto López Cavallotti

### Other Known Limitations

The dataset doesn't cover all the possible grammar errors but serves as a starting point that generates fair results.

## Additional Information

### Dataset Curators

* Juan Alberto López Cavallotti

### Licensing Information

This dataset is distributed under the [Apache 2 License](https://www.apache.org/licenses/LICENSE-2.0)

### Citation Information

Please mention this original dataset and the author **Juan Alberto López Cavallotti**

### Contributions

* Juan Alberto López Cavallotti