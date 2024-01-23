---
annotations_creators:
- machine-generated
- expert-generated
language:
- en
language_creators:
- found
license:
- mit
multilinguality:
- monolingual
pretty_name: KQA-Pro
size_categories:
- 10K<n<100K
source_datasets:
- original
tags:
- knowledge graph
- freebase
task_categories:
- question-answering
task_ids:
- open-domain-qa
---

# Dataset Card for KQA Pro

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Configs](#data-configs)
  - [Data Splits](#data-splits)
- [Additional Information](#additional-information)
  - [How to run SPARQLs and programs](#how-to-run-sparqls-and-programs)
  - [Knowledge Graph File](#knowledge-graph-file)
  - [How to Submit to Leaderboard](#how-to-submit-results-of-test-set)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Homepage:** http://thukeg.gitee.io/kqa-pro/
- **Repository:** https://github.com/shijx12/KQAPro_Baselines
- **Paper:** [KQA Pro: A Dataset with Explicit Compositional Programs for Complex Question Answering over Knowledge Base](https://aclanthology.org/2022.acl-long.422/)
- **Leaderboard:** http://thukeg.gitee.io/kqa-pro/leaderboard.html
- **Point of Contact:** shijx12 at gmail dot com

### Dataset Summary

KQA Pro is a large-scale dataset of complex question answering over knowledge base. The questions are very diverse and challenging, requiring multiple reasoning capabilities including compositional reasoning, multi-hop reasoning, quantitative comparison, set operations, and etc. Strong supervisions of SPARQL and program are provided for each question.

### Supported Tasks and Leaderboards

It supports knowlege graph based question answering. Specifically, it provides SPARQL and *program* for each question.

### Languages

English

## Dataset Structure

**train.json/val.json**
```
[
    {
        'question': str,
        'sparql': str, # executable in our virtuoso engine
        'program': 
        [
            {
                'function': str,  # function name
                'dependencies': [int],  # functional inputs, representing indices of the preceding functions
                'inputs': [str],  # textual inputs
            }
        ],
        'choices': [str],  # 10 answer choices
        'answer': str,  # golden answer
    }
]
```

**test.json**
```
[
    {
        'question': str,
        'choices': [str],  # 10 answer choices
    }
]
```

### Data Configs

This dataset has two configs: `train_val` and `test` because they have different available fields. Please specify this like `load_dataset('drt/kqa_pro', 'train_val')`.

### Data Splits

train, val, test


## Additional Information

### Knowledge Graph File

You can find the knowledge graph file `kb.json` in the original github repository. It comes with the format:

```json
{
    'concepts':
    {
        '<id>':
        {
            'name': str,
            'instanceOf': ['<id>', '<id>'], # ids of parent concept
        }
    },
    'entities': # excluding concepts
    {
        '<id>': 
        {
            'name': str,
            'instanceOf': ['<id>', '<id>'], # ids of parent concept
            'attributes':
            [
                {
                    'key': str, # attribute key
                    'value':  # attribute value
                    {
                        'type': 'string'/'quantity'/'date'/'year',
                        'value': float/int/str, # float or int for quantity, int for year, 'yyyy/mm/dd' for date
                        'unit': str,  # for quantity
                    },
                    'qualifiers':
                    {
                        '<qk>':  # qualifier key, one key may have multiple corresponding qualifier values
                        [
                            {
                                'type': 'string'/'quantity'/'date'/'year',
                                'value': float/int/str,
                                'unit': str,
                            }, # the format of qualifier value is similar to attribute value
                        ]
                    }
                },
            ]
            'relations':
            [
                {
                    'predicate': str,
                    'object': '<id>', # NOTE: it may be a concept id
                    'direction': 'forward'/'backward',
                    'qualifiers':
                    {
                        '<qk>':  # qualifier key, one key may have multiple corresponding qualifier values
                        [
                            {
                                'type': 'string'/'quantity'/'date'/'year',
                                'value': float/int/str,
                                'unit': str,
                            }, # the format of qualifier value is similar to attribute value
                        ]
                    }
                },
            ]
        }
    }
}
```



### How to run SPARQLs and programs

We implement multiple baselines in our [codebase](https://github.com/shijx12/KQAPro_Baselines), which includes a supervised SPARQL parser and program parser.

In the SPARQL parser, we implement a query engine based on [Virtuoso](https://github.com/openlink/virtuoso-opensource.git).
You can install the engine based on our [instructions](https://github.com/shijx12/KQAPro_Baselines/blob/master/SPARQL/README.md), and then feed your predicted SPARQL to get the answer.

In the program parser, we implement a rule-based program executor, which receives a predicted program and returns the answer.
Detailed introductions of our functions can be found in our [paper](https://arxiv.org/abs/2007.03875).

### How to submit results of test set
You need to predict answers for all questions of test set and write them in a text file **in order**, one per line.
Here is an example:
```
Tron: Legacy
Palm Beach County
1937-03-01
The Queen
...
```

Then you need to send the prediction file to us by email <caosl19@mails.tsinghua.edu.cn>, we will reply to you with the performance as soon as possible.
To appear in the learderboard, you need to also provide following information:

- model name
- affiliation
- open-ended or multiple-choice
- whether use the supervision of SPARQL in your model or not
- whether use the supervision of program in your model or not
- single model or ensemble model
- (optional) paper link
- (optional) code link

### Licensing Information

MIT License

### Citation Information

If you find our dataset is helpful in your work, please cite us by

```
@inproceedings{KQAPro,
  title={{KQA P}ro: A Large Diagnostic Dataset for Complex Question Answering over Knowledge Base},
  author={Cao, Shulin and Shi, Jiaxin and Pan, Liangming and Nie, Lunyiu and Xiang, Yutong and Hou, Lei and Li, Juanzi and He, Bin and Zhang, Hanwang},
  booktitle={ACL'22},
  year={2022}
}
```

### Contributions

Thanks to [@happen2me](https://github.com/happen2me) for adding this dataset.
