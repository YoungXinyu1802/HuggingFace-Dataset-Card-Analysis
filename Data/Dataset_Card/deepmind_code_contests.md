---
annotations_creators:
- found
language_creators:
- found
language:
- en
license:
- cc-by-4.0
multilinguality:
- monolingual
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- translation
task_ids: []
paperswithcode_id: codecontests
pretty_name: CodeContests
---

# Dataset Card for CodeContests

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Repository:** https://github.com/deepmind/code_contests/
- **Paper:** [Competition-Level Code Generation with AlphaCode](https://arxiv.org/abs/2203.07814v1)
- **Leaderboard:** [Code Generation on CodeContests](https://paperswithcode.com/sota/code-generation-on-codecontests)
- **Point of Contact:** [David Choi](mailto:david.hu.choi@gmail.com)

### Dataset Summary

CodeContests is a competitive programming dataset for machine-learning. This
dataset was used when training [AlphaCode](https://deepmind.com/blog/article/Competitive-programming-with-AlphaCode).

It consists of programming problems, from a variety of sources:

Site        | URL                         | Source
----------- | --------------------------- | ------
Aizu        | https://judge.u-aizu.ac.jp  | [CodeNet](https://github.com/IBM/Project_CodeNet)
AtCoder     | https://atcoder.jp          | [CodeNet](https://github.com/IBM/Project_CodeNet)
CodeChef    | https://www.codechef.com    | [description2code](https://github.com/ethancaballero/description2code)
Codeforces  | https://codeforces.com      | [description2code](https://github.com/ethancaballero/description2code) and Codeforces
HackerEarth | https://www.hackerearth.com | [description2code](https://github.com/ethancaballero/description2code)

Problems include test cases in the form of paired inputs and outputs, as well as both correct and incorrect human solutions in a variety of languages.

### Supported Tasks and Leaderboards

- `translation` - the competitive programming code generation problem can be viewed as a sequence-to-sequence translation task: given a problem description 𝑋 in natural language, produce a corresponding solution 𝑌 in a programming language. The metric used for evaluation is "percentage of problems solved using 𝑛 submissions from 𝑘 samples per problem", denoted as 𝑛@𝑘. More information on the evaluation of AlphaCode can be found in Section 2.2. and Appendix A.3. of the paper. The leaderboard for this task is available [here](https://paperswithcode.com/sota/code-generation-on-codecontests).

### Languages

English.

## Dataset Structure

### Data Instances

A data point corresponds to a singular contest problem:

```
{
  'name': '76_B. Mice',
  'description': 'Modern researches has shown that a flock of hungry mice '
                 'searching for a piece of...',
  'public_tests': {'input': ['3 2 0 2\n0 1 3\n2 5\n'], 'output': ['1\n']},
  'private_tests': {'input': ['20 18 1 2\n'
                              '-9999944 -9999861 -9999850 -9999763 -9999656 '
                              '-9999517 -9999375 -999927...',
                              ...,
                              '7 11 10 20\n'
                              '6 18 32 63 66 68 87\n'
                              '6 8 15 23 25 41 53 59 60 75 90\n'],
                    'output': ['2\n', ..., '1\n']},
  'generated_tests': {'input': ['7 11 10 5\n'
                                '6 18 32 63 66 68 87\n'
                                '6 8 15 23 25 41 53 59 60 75 90\n',
                                ...,
                                '7 11 10 4\n'
                                '6 18 46 63 85 84 87\n'
                                '6 8 15 18 25 41 53 59 60 75 90\n'],
                      'output': ['1\n', ..., '2\n']},
  'source': 2,
  'difficulty': 8,
  'solutions': {'language': [2, Ellipsis, 2],
                'solution': ['#include <bits/stdc++.h>\n'
                             'using namespace std;\n'
                             'int n, m;\n'
                             'int data[2][100010], t[1...',
                             ...,
                             '#include <bits/stdc++.h>\n'
                             'using namespace std;\n'
                             'int n, m, pos[100100], food[100100...']},
  'incorrect_solutions': {'language': [2, Ellipsis, 2],
                          'solution': ['#include <bits/stdc++.h>\n'
                                       'using namespace std;\n'
                                       'vector<pair<int, int> > v[100010];...',
                                       ...,
                                       '#include <bits/stdc++.h>\n'
                                       'using namespace std;\n'
                                       'vector<pair<int, int> > v[100010];...']},
  'cf_contest_id': 76,
  'cf_index': 'B',
  'cf_points': 0.0,
  'cf_rating': 2100,
  'cf_tags': ['greedy', 'two pointers'],
  'is_description_translated': False,
  'untranslated_description': '',
  'time_limit': {'seconds': 0, 'nanos': 500000000},
  'memory_limit_bytes': 256000000,
  'input_file': '',
  'output_file': ''
}
```

### Data Fields

- `name`: The name of the contest. Note that names could agree between different sources.
- `description`: A natural language description of a programming problem.
- `public_tests`: Public tests are those that are available before submitting a solution, typically as part of the description itself. Represented as a paired `input` and `output` that can be used to test potential solutions. They are therefore acceptable inputs to a model.
- `private_tests`: Private tests are not visible before submitting a solution, so should not be made available as inputs to a model. 
- `generated_tests`: Generated tests are automatically generated by modifying inputs from public and private tests and validating using known correct solutions.
- `source`: The original source of the problem, with possible values including `UNKNOWN_SOURCE` (0),`CODECHEF` (1), `CODEFORCES` (2), `HACKEREARTH` (3), `CODEJAM` (4), `ATCODER` (5) and `AIZU` (6).
- `difficulty`: A representation of the difficulty of the problem with possible values including `UNKNOWN_DIFFICULTY` (0), `EASY` (1), `MEDIUM` (2), `HARD` (3), `HARDER` (4), `HARDEST` (5), `EXTERNAL` (6), `A` (7), `B` (8), `C` (9), `D` (10), `E` (11), `F` (12), `G` (13), `H` (14), `I` (15), `J` (16), `K` (17), `L` (18), `M` (19), `N` (20), `O` (21), `P` (22), `Q` (23), `R` (24), `S` (25), `T` (26), `U` (27) and `V` (28). Note that different sources use different, non-comparable gradings. For Codeforces problems, `cf_rating` is a more reliable measure of difficulty when available.
- `solutions`: Correct solutions to the problem. Contrast with `incorrect_solutions` below.
- `incorrect_solutions`: Incorrect solutions.
- `cf_contest_id`: The Contest ID. Note that Contest ID is not monotonic with respect to time.
- `cf_index`: Problem index, e.g. `"A"` or `"B"` or `"C"`.
- `cf_points`: Points for the problem, e.g. `1000.0`
- `cf_rating`: Problem rating (difficulty), e.g. `1100`
- `cf_tags`: Problem tags, e.g. `['greedy', 'math']`
- `is_description_translated`: Whether the problem was translated to English.
- `untranslated_description`: The untranslated description is only available for translated problems.
- `time_limit`: The time limit constraint to use when executing solutions. Represented as a dictionary with two keys, `seconds` and `nanos`. This field is None if not defined.
- `memory_limit_bytes`: The memory limit constraint to use when executing solutions.
- `input_file`: Most problems use stdin for IO. Some problems expect specific files to be used instead.
- `output_file`: Most problems use stdout for IO. Some problems expect specific files to be used instead.

All tests are represented as a paired `input` and `output` that can be used to test potential solutions and all solutions and all solutions comprise a `language`, with possible values including `UNKNOWN_LANGUAGE` (0), `PYTHON` (1) (solutions written in PYTHON2), `CPP` (2), `PYTHON3` (3) and `JAVA` (4), and a `solution` string written in the `language`. The fields preceded with `cf_` denote extra meta-data for Codeforces problems. 

### Data Splits

The data is split into training, validation and test set. The training set contains 13328 samples, the validation set 117 samples and the test set 165 samples.

## Dataset Creation

### Curation Rationale

This dataset was created for fine-tuning AlphaCode models:
> Models pre-trained on GitHub can generate good code and solve simple programming problems, but
as shown in Appendix B.3 they can solve very few competitive programming problems. Fine-tuning
the model on a dedicated competitive programming dataset is critical for performance.

### Source Data

#### Initial Data Collection and Normalization

The information on the data collection and normalization procedures can found in Section 3.2. and Appendinx B.2. of the paper.

#### Who are the source language producers?

The problems are scraped from the following platforms: [Aizu](https://judge.u-aizu.ac.jp), [AtCoder](https://atcoder.jp ), [CodeChef](https://www.codechef.com), [Codeforces](https://codeforces.com) and [HackerEarch](https://www.hackerearth.com). Additionally, some data from the existing public competitive programming dataset Description2Code ([Caballero et al., 2016](https://github.com/ethancaballero/description2code)) and CodeNet ([(Puri et al., 2021](https://arxiv.org/pdf/2105.12655.pdf)) is mixed into the training set.

### Annotations

#### Annotation process

The solutions are scapred alongside the problem descriptions.

#### Who are the annotators?

Same as the source data creators.

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

Yujia Li, David Choi, Junyoung Chung, Nate Kushman, Julian Schrittwieser, Rémi Leblond, Tom Eccles, James Keeling, Felix Gimeno, Agustin Dal Lago, Thomas Hubert, Peter Choy, Cyprien de Masson d'Autume, Igor Babuschkin, Xinyun Chen, Po-Sen Huang, Johannes Welbl, Sven Gowal, Alexey Cherepanov, James Molloy, Daniel J. Mankowitz, Esme Sutherland Robson, Pushmeet Kohli, Nando de Freitas, Koray Kavukcuoglu and Oriol Vinyals.

### Licensing Information

This dataset is made available under the terms of the CC BY
4.0 license ([Creative Commons Attribution 4.0 International license](https://creativecommons.org/licenses/by/4.0/legalcode)).

Additional acknowledged contributions:

*   Codeforces materials are sourced from http://codeforces.com.
*   Description2Code materials are sourced from:
    [Description2Code Dataset](https://github.com/ethancaballero/description2code),
    licensed under the
    [MIT open source license](https://opensource.org/licenses/MIT), copyright
    not specified.
*   CodeNet materials are sourced from:
    [Project_CodeNet](https://github.com/IBM/Project_CodeNet), licensed under
    [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0), copyright not
    specified.

### Citation Information

```bibtex
@article{li2022competition,
  title={Competition-Level Code Generation with AlphaCode},
    author={Li, Yujia and Choi, David and Chung, Junyoung and Kushman, Nate and
    Schrittwieser, Julian and Leblond, R{\'e}mi and Eccles, Tom and
    Keeling, James and Gimeno, Felix and Dal Lago, Agustin and
    Hubert, Thomas and Choy, Peter and de Masson d'Autume, Cyprien and
    Babuschkin, Igor and Chen, Xinyun and Huang, Po-Sen and Welbl, Johannes and
    Gowal, Sven and Cherepanov, Alexey and Molloy, James and
    Mankowitz, Daniel and Sutherland Robson, Esme and Kohli, Pushmeet and
    de Freitas, Nando and Kavukcuoglu, Koray and Vinyals, Oriol},
  journal={arXiv preprint arXiv:2203.07814},
  year={2022}
}
```

### Contributions

Thanks to [@mariosasko](https://github.com/mariosasko) for adding this dataset.