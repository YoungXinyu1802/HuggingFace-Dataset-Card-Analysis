# Dataset Card for FIG-Loneliness

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
- **Homepage:** [FIG-Loneliness](https://ojs.aaai.org/index.php/ICWSM/article/view/19302)
- **Paper:** [Many Ways to be Lonely](https://ojs.aaai.org/index.php/ICWSM/article/view/19302/19074)
- **Point of Contact:** [Sherry Yueyi Jiang](mailto:yujiang@ucsd.edu)


### Dataset Summary

FIG-Loneliness is a dataset for fine-grained loneliness characterization and model training. This dataset consists of 2633 lonely and 3000 non-lonely Reddit posts annotated by trained human annotators. For the lonely posts, we provide fine-grained category labels for the forms of loneliness including duration, context and interpersonal relationships, and for the coping strategies of the authors including reaching out, seeking advice, seeking validation and non-directed interaction.

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

The language supported is English.

## Dataset Structure

### Loading
To load the dataset, first clone this dataset repo:
```bash
git clone https://huggingface.co/datasets/FIG-Loneliness/FIG-Loneliness
```

Then we can load datasets using Huggingface Datasets API:
```python
import os
import datasets as hf_ds


ROOT = "dir/to/data/repo"

# load datasets
train_set = hf_ds.load_from_disk(os.path.join(ROOT, "train_set"))
dev_set = hf_ds.load_from_disk(os.path.join(ROOT, "dev_set"))
test_set = hf_ds.load_from_disk(os.path.join(ROOT, "test_set"))
```

### Data Instances

The `train_set` split contains 3,943 instances. The `dev_set` split contains 1,126. The `test_set` split contains 564 instances.

### Data Fields
Each instance contains 8 fields: `idx`, `unique_id`, `text`, `lonely`, `temporal`, `interaction`, `context_pri`, and `interpersonal_pri`.

| Field |                                                                                             Meaning                                                                                              |
|:---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| `idx` |                                                                  Integer index of this instance from our scrapped Reddit posts.                                                                  |
| `unique_id` |                                                                                  Unique ID of this Reddit post.                                                                                  |
| `text` |                                                                               Textual content of the Reddit post.                                                                                |
| `lonely` |                                                                     2-len one-hot vector, representing [non-lonely, lonely].                                                                     |
| `temporal` |                                      **Duration**. 4-len vector summarizing human annotators' votings in the order of [transient, enduring, ambiguous, NA].                                      |
| `interaction` | **Interaction**. 5-len vector summarizing human annotators' votings in the order of [seeking advice, providing help, seeking validation and affirmation, reaching out, non directed interaction] |
| `context_pri` |                                    **Context**. 5-len vector summarizing human annotators' votings in the order of [social, physical, somatic, romantic, N/A]                                    |
| `interpersonal_pri` |                              **Interpersonal**. 5-len vector summarizing human annotators' votings in the order of [romantic, friendship, family, colleagues, N/A]                               |

### Data Splits

The entire dataset is split into 3,943 training instances, 1,126 dev instances, and 564 test instances.

## Dataset Creation

### Curation Rationale

The data curation rationale is to capture **loneliness expressions** not only from a wider user base but also from users who specifically belong to the young adult age group (a vulnerable group for loneliness). We sampled data from Reddit and subsequently annotated the data with loneliness labels.

### Source Data

#### Initial Data Collection and Normalization

By using Reddit’s Pushshift API, we collected all posts from two loneliness specific subreddits (*r/loneliness*, *r/lonely*) and two subreddits for young adults (*r/youngadults*, *r/college*) from 2018 to 2020.

#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Who are the annotators?

Annotation labels were provided by trained undergraduate research assistants and Amazon’s Mechanical Turk workers (MTurkers) with a Master certification.

#### Annotation process

For the potential lonely samples: 
We had research assistants labeled the sampled potential lonely posts. Each post was labeled by three of research assistants. A posts was first labeled on whether it contains an expression on self-disclosure of loneliness. If the majority of the annotators labeled a post as not containing such expression, the post would be discarded, otherwise it is further labeled according to a codebook that contains the following categories: (1) *duration*: the duration of the loneliness experience (transient, enduring, and ambiguous), (2) *context*: the contexts of the experience (social, physical, somatic, and romantic), (3) *interpresonal*: the interpersonal relationships involved in the experience (romantic, family, friendship, and peers), and (4) *interaction*: user interaction styles (seeking advice, providing support, seeking validation/affirmation, reaching out and non-directed interaction). The codebook is intended for dissecting different forms of loneliness and users’ coping strategies in the loneliness discourse. We also included a ‘not applicable’ (NA) label to accommodate situations that are not suitable for classification. For each category, the annotators gave *one value* which they think would best capture the source of loneliness in the post or the poster’s interaction intent.

For the potential non-lonely samples: 
MTurkers were instructed to classify whether the Reddit posters express loneliness. Each post was annotated by three MTurkers, and only posts labeled as non-lonely by the majority would remain in the final annotated dataset.

All the labeled posts and annotations were included in FIG-Loneliness, which consists of roughly 3000 lonely and 3000 non-lonely posts. 

#### Dataset Codebook

See code rule and example posts for the category labels [here](https://drive.google.com/file/d/1J6i72qyqirAIC40jWuJvDN-ZWU87XttH/view).
 
### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

See **Limitation and Data Disclaimer** [here](https://ojs.aaai.org/index.php/ICWSM/article/view/19302/19074)

## Additional Information

### Dataset Curator   

[More Information Needed]

### Licensing Information

[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)

### Citation Information

Jiang, Y., Jiang, Y., Leqi, L., & Winkielman, P. (2022). Many Ways to Be Lonely: Fine-Grained Characterization of Loneliness and Its Potential Changes in COVID-19. Proceedings of the International AAAI Conference on Web and Social Media, 16(1), 405-416. Retrieved from https://ojs.aaai.org/index.php/ICWSM/article/view/19302