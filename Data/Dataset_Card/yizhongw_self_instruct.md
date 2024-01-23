---
license: apache-2.0
dataset_info:
- config_name: self_instruct
  features:
  - name: prompt
    dtype: string
  - name: completion
    dtype: string
  splits:
  - name: train
    num_bytes: 20527462
    num_examples: 82612
  download_size: 24113858
  dataset_size: 20527462
- config_name: human_eval
  features:
  - name: id
    dtype: string
  - name: motivation_app
    dtype: string
  - name: instruction
    dtype: string
  - name: instances
    sequence:
    - name: input
      dtype: string
    - name: output
      dtype: string
  splits:
  - name: train
    num_bytes: 151244
    num_examples: 252
  download_size: 170193
  dataset_size: 151244
- config_name: super_natural_instructions
  features:
  - name: prompt
    dtype: string
  - name: completion
    dtype: string
  splits:
  - name: train
    num_bytes: 40352923
    num_examples: 50000
  - name: test
    num_bytes: 9713953
    num_examples: 11810
  download_size: 52975509
  dataset_size: 50066876
- config_name: prompt_source
  features:
  - name: prompt
    dtype: string
  - name: completion
    dtype: string
  splits:
  - name: train
    num_bytes: 57368889
    num_examples: 52657
  download_size: 60126945
  dataset_size: 57368889
- config_name: p3
  features:
  - name: prompt
    dtype: string
  - name: completion
    dtype: string
  splits:
  - name: train
    num_bytes: 57368889
    num_examples: 52657
  download_size: 60126945
  dataset_size: 57368889
---

# Dataset Card for Self Instruct

## Table of Contents
- [Dataset Card for Self Instruct](#dataset-card-for-self-instruct)
  - [Table of Contents](#table-of-contents)
  - [Dataset Description](#dataset-description)
    - [Dataset Summary](#dataset-summary)
    - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
      - [self\_instruct](#self_instruct)
      - [super\_natural\_instructions](#super_natural_instructions)
      - [p3](#p3)
      - [human\_eval](#human_eval)
    - [Languages](#languages)
  - [Dataset Structure](#dataset-structure)
    - [Data Instances](#data-instances)
      - [self\_instruct](#self_instruct-1)
      - [super\_natural\_instructions](#super_natural_instructions-1)
      - [p3](#p3-1)
      - [human\_eval](#human_eval-1)
    - [Data Fields](#data-fields)
      - [self\_instruct](#self_instruct-2)
      - [super\_natural\_instructions](#super_natural_instructions-2)
      - [p3](#p3-2)
      - [human\_eval](#human_eval-2)
    - [Data Splits](#data-splits)
      - [self\_instruct](#self_instruct-3)
      - [super\_natural\_instructions](#super_natural_instructions-3)
      - [p3](#p3-3)
      - [human\_eval](#human_eval-3)
  - [Dataset Creation](#dataset-creation)
    - [Curation Rationale](#curation-rationale)
    - [Source Data](#source-data)
      - [Initial Data Collection and Normalization](#initial-data-collection-and-normalization)
      - [Who are the source language producers?](#who-are-the-source-language-producers)
    - [Annotations](#annotations)
      - [Annotation process](#annotation-process)
      - [Who are the annotators?](#who-are-the-annotators)
    - [Personal and Sensitive Information](#personal-and-sensitive-information)
  - [Considerations for Using the Data](#considerations-for-using-the-data)
    - [Social Impact of Dataset](#social-impact-of-dataset)
    - [Discussion of Biases](#discussion-of-biases)
    - [Other Known Limitations](#other-known-limitations)
  - [Additional Information](#additional-information)
    - [Dataset Curators](#dataset-curators)
    - [Licensing Information](#licensing-information)
    - [Citation Information](#citation-information)

## Dataset Description

- **Homepage:**
- **Repository:** https://github.com/yizhongw/self-instruct
- **Paper:** https://arxiv.org/abs/2212.10560
- **Leaderboard:**
- **Point of Contact:** Yizhong Wang

### Dataset Summary

Self-Instruct is a framework that helps language models improve their ability to follow natural language instructions. It does this by using the model's own generations to create a large collection of instructional data. With Self-Instruct, it is possible to improve the instruction-following capabilities of language models without relying on extensive manual annotation.

A part of this framework, the Self-Instruct authors released a dataset that contains 52k instructions, paired with 82K instance inputs and outputs. This instruction data can be used to conduct instruction-tuning for language models and make the language model follow instruction better.

The authors also released a new set of 252 expert-written tasks and their instructions motivated by user-oriented applications (rather than well-studied NLP tasks). This data is used in the human evaluation section of [the Self Instruct paper](https://arxiv.org/abs/2212.10560).

To enable comparison on public datasets, Self-Instruct also contains 50k examples from the P3 and Super Natural Instructions datasets.

### Supported Tasks and Leaderboards

The datasets in Self-Instruct are designed for _instruction training_ pretrained language models. The following subsets are provided as part of Self Instruct.

#### self_instruct

82k prompts and model completions generated via OpenAI's `davinci` engine.

#### super_natural_instructions

50k expert written instructions and demonstrations sampled from the [Super Natural Instructions dataset](https://arxiv.org/abs/2204.07705)

#### p3

50k crowd-sourced instructions and demonstrations sampled from the [Public Pool of Prompts (P3) dataset](https://huggingface.co/datasets/bigscience/P3)

#### human_eval

252 expert-written tasks and their instructions motivated by user-oriented applications (rather than well-studied NLP tasks). This data is used in the human evaluation section of [the self-instruct paper](https://arxiv.org/abs/2212.10560). Please refer to [the human evaluation information]([human_eval/README.md](https://github.com/yizhongw/self-instruct/blob/main/human_eval/README.md)) for more details.

### Languages

The data in Self Instruct are in English (BCP-47 en).

## Dataset Structure

### Data Instances

#### self_instruct

An example pf "train" looks as follows:

```json
{
    "prompt": "Explain the origin of life on earth. Output:",
    "completion": " Life on Earth is believed to have begun about 3.5 billion years ago, when the planet was still in its early stages of formation. The earliest evidence for life on Earth are fossils of microorganisms (bacteria and archaea) that lived approximately 3.5 billion years ago. These organisms were capable of converting carbon dioxide into organic compounds using sunlight as an energy source. This process is known as photosynthesis.",
}
```

#### super_natural_instructions

An example pf "train" looks as follows:

```json
{
    "prompt": "Write a correct answer for the question. You should reason about prototypical situations and provide the correct answer. Avoid answers that provide incomplete justification for the question.\n\nInput: name something people often buy on credit.\n\nOutput:",
    "completion": " appliances",
}
```


#### p3

An example pf "train" looks as follows:

```json
{
    "prompt": "Determine if the following two sentences paraphrase each other or not.\nSent 1: By adding sufficient oxygen to compensate for the metabolic usage , rebreathing the carbon dioxide and removing the gas , most of the volume is conserved .\nSent 2: By adding sufficient oxygen to compensate for the metabolic consumption , removing the carbon dioxide and reinhaling the gas , most of the volume is conserved .\n",
    "completion": "No",
}
```


#### human_eval

An example pf "train" looks as follows:

```json
{
    "id": "user_oriented_task_136",
    "motivation_app": "Goodreads",
    "instruction": "Choose the best books from the given genre.",
    "instances": {
        "input": ["Crime & Mystery"],
        "output": [
            "1- The Girl with the Dragon Tattoo\n2- And Then There Were None\n3- Angels & Demons\n4- Rebecca\n5- In Cold Blood\n6- The Godfather\n7- The Lovely Bones\n8- Gone Girl\n9- The Name of the Rose\n10- Shutter Island"
        ],
    },
}
```

### Data Fields

The data fields for each configuration are as follows.

#### self_instruct

* `prompt`: The instruction provided to the model or human labeler.
* `completion`: A completion provided by the model or human labeler.

#### super_natural_instructions

* `prompt`: The instruction provided to the model or human labeler.
* `completion`: A completion provided by the model or human labeler.

#### p3

* `prompt`: The instruction provided to the model or human labeler.
* `completion`: A completion provided by the model or human labeler.

#### human_eval

* `id`: The ID associated with the labelling task
* `motivation_app`: The application associated with the task
* `instruction`: The instruction written by the human labeler.
* `instances.input`: The input that forms part of the complete instruction
* `instances.output`: The human written demonstration


### Data Splits

#### self_instruct

|               | train |
|---------------|------:|
| self_instruct | 82612 |

#### super_natural_instructions

|                            | train |  test |
|----------------------------|------:|------:|
| super_natural_instructions | 50000 | 11810 |

#### p3

|    | train |
|----|------:|
| p3 | 52657 |

#### human_eval

|            | train |
|------------|------:|
| human_eval |   252 |

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

The `self_instruct` data is generated by a language model (GPT-3) and inevitably contains some errors or biases. The authors analyzed the data quality on 200 random instructions in our paper, and found that 46% of the data points may have problems. We encourage users to use this data with caution and propose new methods to filter or improve the imperfections.

## Additional Information

### Dataset Curators

[More Information Needed]

### Licensing Information

[More Information Needed]

### Citation Information

```
@misc{selfinstruct,
  title={Self-Instruct: Aligning Language Model with Self Generated Instructions},
  author={Wang, Yizhong and Kordi, Yeganeh and Mishra, Swaroop and Liu, Alisa and Smith, Noah A. and Khashabi, Daniel and Hajishirzi, Hannaneh},
  journal={arXiv preprint arXiv:2212.10560},
  year={2022}
}
```