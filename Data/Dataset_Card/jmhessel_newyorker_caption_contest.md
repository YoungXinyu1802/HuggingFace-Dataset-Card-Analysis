---
annotations_creators:
- expert-generated
- crowdsourced
- found
language:
- en
language_creators:
- crowdsourced
- expert-generated
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: newyorker_caption_contest
size_categories:
- 1K<n<10K
source_datasets:
- original
tags:
- humor
- caption contest
- new yorker
task_categories:
- image-to-text
- multiple-choice
- text-classification
- text-generation
- visual-question-answering
- other
- text2text-generation
task_ids:
- multi-class-classification
- language-modeling
- visual-question-answering
- explanation-generation
---

# Dataset Card for New Yorker Caption Contest Benchmarks

## Table of Contents
- [Table of Contents](#table-of-contents)
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

- **Homepage:** [capcon.dev](https://www.capcon.dev)
- **Repository:** [https://github.com/jmhessel/caption_contest_corpus](https://github.com/jmhessel/caption_contest_corpus)
- **Paper:** [Do Androids Laugh at Electric Sheep? Humor "Understanding" Benchmarks from The New Yorker Caption Contest](https://arxiv.org/abs/2209.06293)
- **Leaderboard:** No official leaderboard (yet).
- **Point of Contact:** jackh@allenai.org

### Dataset Summary

Data from:
[Do Androids Laugh at Electric Sheep? Humor "Understanding" Benchmarks from The New Yorker Caption Contest](https://arxiv.org/abs/2209.06293)

```
@article{hessel2022androids,
  title={Do Androids Laugh at Electric Sheep? Humor "Understanding" Benchmarks from The New Yorker Caption Contest},
  author={Hessel, Jack and Marasovi{\'c}, Ana and Hwang, Jena D and Lee, Lillian and Da, Jeff and Zellers, Rowan and Mankoff, Robert and Choi, Yejin},
  journal={arXiv preprint arXiv:2209.06293},
  year={2022}
}
```

If you use this dataset, we would appreciate you citing our work, but also -- several other papers that we build this corpus upon. See [Citation Information](#citation-information).

We challenge AI models to "demonstrate understanding" of the
sophisticated multimodal humor of The New Yorker Caption Contest.
Concretely, we develop three carefully circumscribed tasks for which
it suffices (but is not necessary) to grasp potentially complex and
unexpected relationships between image and caption, and similarly
complex and unexpected allusions to the wide varieties of human
experience.


### Supported Tasks and Leaderboards

Three tasks are supported:

- "Matching:" a model must recognize a caption written about a cartoon (vs. options that were not);
- "Quality ranking:" a model must evaluate the quality of a caption by scoring it more highly than a lower quality option from the same contest;
- "Explanation:" a model must explain why a given joke is funny.

There are no official leaderboards (yet).

### Languages

English

## Dataset Structure

Here's an example instance from Matching:
```
{'caption_choices': ['Tell me about your childhood very quickly.',
                     "Believe me . . . it's what's UNDER the ground that's "
                     'most interesting.',
                     "Stop me if you've heard this one.",
                     'I have trouble saying no.',
                     'Yes, I see the train but I think we can beat it.'],
 'contest_number': 49,
 'entities': ['https://en.wikipedia.org/wiki/Rule_of_three_(writing)',
              'https://en.wikipedia.org/wiki/Bar_joke',
              'https://en.wikipedia.org/wiki/Religious_institute'],
 'from_description': 'scene: a bar description: Two priests and a rabbi are '
                     'walking into a bar, as the bartender and another patron '
                     'look on. The bartender talks on the phone while looking '
                     'skeptically at the incoming crew. uncanny: The scene '
                     'depicts a very stereotypical "bar joke" that would be '
                     'unlikely to be encountered in real life; the skepticism '
                     'of the bartender suggests that he is aware he is seeing '
                     'this trope, and is explaining it to someone on the '
                     'phone. entities: Rule_of_three_(writing), Bar_joke, '
                     'Religious_institute. choices A: Tell me about your '
                     "childhood very quickly. B: Believe me . . . it's what's "
                     "UNDER the ground that's most interesting. C: Stop me if "
                     "you've heard this one. D: I have trouble saying no. E: "
                     'Yes, I see the train but I think we can beat it.',
 'image': <PIL.JpegImagePlugin.JpegImageFile image mode=L size=323x231 at 0x7F34F283E9D0>,
 'image_description': 'Two priests and a rabbi are walking into a bar, as the '
                      'bartender and another patron look on. The bartender '
                      'talks on the phone while looking skeptically at the '
                      'incoming crew.',
 'image_location': 'a bar',
 'image_uncanny_description': 'The scene depicts a very stereotypical "bar '
                              'joke" that would be unlikely to be encountered '
                              'in real life; the skepticism of the bartender '
                              'suggests that he is aware he is seeing this '
                              'trope, and is explaining it to someone on the '
                              'phone.',
 'instance_id': '21125bb8787b4e7e82aa3b0a1cba1571',
 'label': 'C',
 'n_tokens_label': 1,
 'questions': ['What is the bartender saying on the phone in response to the '
               'living, breathing, stereotypical bar joke that is unfolding?']}
```

The label "C" indicates that the 3rd choice in the `caption_choices` is correct.

Here's an example instance from Ranking (in the from pixels setting --- though, this is also available in the from description setting)
```
{'caption_choices': ['I guess I misunderstood when you said long bike ride.',
                     'Does your divorce lawyer have any other cool ideas?'],
 'contest_number': 582,
 'image': <PIL.JpegImagePlugin.JpegImageFile image mode=L size=600x414 at 0x7F8FF9F96610>,
 'instance_id': 'dd1c214a1ca3404aa4e582c9ce50795a',
 'label': 'A',
 'n_tokens_label': 1,
 'winner_source': 'official_winner'}
```
the label indicates that the first caption choice ("A", here) in the `caption_choices` list was more highly rated.


Here's an example instance from Explanation:
```
{'caption_choices': 'The classics can be so intimidating.',
 'contest_number': 752,
 'entities': ['https://en.wikipedia.org/wiki/Literature',
              'https://en.wikipedia.org/wiki/Solicitor'],
 'from_description': 'scene: a road description: Two people are walking down a '
                     'path. A number of giant books have surrounded them. '
                     'uncanny: There are book people in this world. entities: '
                     'Literature, Solicitor. caption: The classics can be so '
                     'intimidating.',
 'image': <PIL.JpegImagePlugin.JpegImageFile image mode=L size=800x706 at 0x7F90003D0BB0>,
 'image_description': 'Two people are walking down a path. A number of giant '
                      'books have surrounded them.',
 'image_location': 'a road',
 'image_uncanny_description': 'There are book people in this world.',
 'instance_id': 'eef9baf450e2fab19b96facc128adf80',
 'label': 'A play on the word intimidating --- usually if the classics (i.e., '
          'classic novels) were to be intimidating, this would mean that they '
          'are intimidating to read due to their length, complexity, etc. But '
          'here, they are surrounded by anthropomorphic books which look '
          'physically intimidating, i.e., they are intimidating because they '
          'may try to beat up these people.',
 'n_tokens_label': 59,
 'questions': ['What do the books want?']}
```
The label is an explanation of the joke, which serves as the autoregressive target.

### Data Instances

See above

### Data Fields

See above

### Data Splits

Data splits can be accessed as:
```
from datasets import load_dataset
dset = load_dataset("jmhessel/newyorker_caption_contest", "matching")
dset = load_dataset("jmhessel/newyorker_caption_contest", "ranking")
dset = load_dataset("jmhessel/newyorker_caption_contest", "explanation")
```

Or, in the from pixels setting, e.g.,
```
from datasets import load_dataset
dset = load_dataset("jmhessel/newyorker_caption_contest", "ranking_from_pixels")
```

Because the dataset is small, we reported in 5-fold cross-validation setting initially. The default splits are split 0. You can access the other splits, e.g.:

```
from datasets import load_dataset

# the 4th data split
dset = load_dataset("jmhessel/newyorker_caption_contest", "explanation_4")
```

## Dataset Creation

Full details are in the paper.

### Curation Rationale

See the paper for rationale/motivation.

### Source Data

See citation below. We combined 3 sources of data, and added significant annotations of our own.

#### Initial Data Collection and Normalization

Full details are in the paper.

#### Who are the source language producers?

We paid crowdworkers $15/hr to annotate the corpus.
In addition, significant annotation efforts were conducted by the authors of this work.

### Annotations

Full details are in the paper.

#### Annotation process

Full details are in the paper.

#### Who are the annotators?

A mix of crowdworks and authors of this paper.

### Personal and Sensitive Information

Has been redacted from the dataset. Images are published in the New Yorker already.

## Considerations for Using the Data

### Social Impact of Dataset

It's plausible that humor could perpetuate negative stereotypes. The jokes in this corpus are a mix of crowdsourced entries that are highly rated, and ones published in the new yorker.

### Discussion of Biases

Humor is subjective, and some of the jokes may be considered offensive. The images may contain adult themes and minor cartoon nudity.

### Other Known Limitations

More details are in the paper

## Additional Information

### Dataset Curators

The dataset was curated by researchers at AI2

### Licensing Information

The annotations we provide are CC-BY-4.0. See www.capcon.dev for more info.

### Citation Information


```
@article{hessel2022androids,
  title={Do Androids Laugh at Electric Sheep? Humor "Understanding" Benchmarks from The New Yorker Caption Contest},
  author={Hessel, Jack and Marasovi{\'c}, Ana and Hwang, Jena D and Lee, Lillian and Da, Jeff and Zellers, Rowan and Mankoff, Robert and Choi, Yejin},
  journal={arXiv preprint arXiv:2209.06293},
  year={2022}
}
```

Our data contributions are:

- The cartoon-level annotations;
- The joke explanations;
- and the framing of the tasks

We release these data we contribute under CC-BY (see DATASET_LICENSE). If you find this data useful in your work, in addition to citing our contributions, please also cite the following, from which the cartoons/captions in our corpus are derived:

```
@misc{newyorkernextmldataset,
  author={Jain, Lalit  and Jamieson, Kevin and Mankoff, Robert and Nowak, Robert and Sievert, Scott},
  title={The {N}ew {Y}orker Cartoon Caption Contest Dataset},
  year={2020},
  url={https://nextml.github.io/caption-contest-data/}
}

@inproceedings{radev-etal-2016-humor,
  title = "Humor in Collective Discourse: Unsupervised Funniness Detection in The {New Yorker} Cartoon Caption Contest",
  author = "Radev, Dragomir  and
      Stent, Amanda  and
      Tetreault, Joel  and
      Pappu, Aasish  and
      Iliakopoulou, Aikaterini  and
      Chanfreau, Agustin  and
      de Juan, Paloma  and
      Vallmitjana, Jordi  and
      Jaimes, Alejandro  and
      Jha, Rahul  and
      Mankoff, Robert",
  booktitle = "LREC",
  year = "2016",
}

@inproceedings{shahaf2015inside,
  title={Inside jokes: Identifying humorous cartoon captions},
  author={Shahaf, Dafna and Horvitz, Eric and Mankoff, Robert},
  booktitle={KDD},
  year={2015},
}
```