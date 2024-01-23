---
annotations_creators:
- crowdsourced
language:
- ko
language_creators:
- found
license:
- cc-by-sa-4.0
multilinguality:
- monolingual
pretty_name: 'K-MHaS'
size_categories:
- 100K<n<1M
source_datasets:
- original
tags:
- K-MHaS
- Korean NLP
- Hate Speech Detection
- Dataset
- Coling2022
task_categories:
- text-classification
task_ids:
- multi-label-classification
- hate-speech-detection
paperswithcode_id: korean-multi-label-hate-speech-dataset
dataset_info:
  features:
  - name: text
    dtype: string
  - name: label
    sequence:
      class_label:
        names:
          0: origin
          1: physical
          2: politics
          3: profanity
          4: age
          5: gender
          6: race
          7: religion
          8: not_hate_speech
  splits:
  - name: train
    num_bytes: 6845463
    num_examples: 78977
  - name: validation
    num_bytes: 748899
    num_examples: 8776
  - name: test
    num_bytes: 1902352
    num_examples: 21939
  download_size: 9496714
  dataset_size: 109692
---

# Dataset Card for K-MHaS

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

## Sample Code
<a href="https://colab.research.google.com/drive/171KhS1_LVBtpAFd_kaT8lcrZmhcz5ehY?usp=sharing"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="base"/></a>


## Dataset Description

- **Homepage:** [K-MHaS](https://github.com/adlnlp/K-MHaS)
- **Repository:** [Korean Multi-label Hate Speech Dataset](https://github.com/adlnlp/K-MHaS)
- **Paper:** [K-MHaS: A Multi-label Hate Speech Detection Dataset in Korean Online News Comment](https://arxiv.org/abs/2208.10684)
- **Point of Contact:** [Caren Han](caren.han@sydney.edu.au)
- **Sample code:** [Colab](https://colab.research.google.com/drive/171KhS1_LVBtpAFd_kaT8lcrZmhcz5ehY?usp=sharing)


### Dataset Summary

The Korean Multi-label Hate Speech Dataset, **K-MHaS**, consists of 109,692 utterances from Korean online news comments, labelled with 8 fine-grained hate speech classes (labels: `Politics`, `Origin`, `Physical`, `Age`, `Gender`, `Religion`, `Race`, `Profanity`) or `Not Hate Speech` class. Each utterance provides from a single to four labels that can handles Korean language patterns effectively. For more details, please refer to our paper about [**K-MHaS**](https://aclanthology.org/2022.coling-1.311), published at COLING 2022.

### Supported Tasks and Leaderboards
Hate Speech Detection

* `binary classification` (labels: `Hate Speech`, `Not Hate Speech`)
* `multi-label classification`: (labels: `Politics`, `Origin`, `Physical`, `Age`, `Gender`, `Religion`, `Race`, `Profanity`, `Not Hate Speech`)

For the multi-label classification, a `Hate Speech` class from the binary classification, is broken down into eight classes, associated with the hate speech category. In order to reflect the social and historical context, we select the eight hate speech classes. For example, the `Politics` class is chosen, due to a significant influence on the style of Korean hate speech.

### Languages

Korean	

## Dataset Structure

### Data Instances

The dataset is provided with train/validation/test set in the txt format. Each instance is a news comment with a corresponding one or more hate speech classes (labels: `Politics`, `Origin`, `Physical`, `Age`, `Gender`, `Religion`, `Race`, `Profanity`) or `Not Hate Speech` class. The label numbers matching in both English and Korean is in the data fields section. 

```python
{'text':'수꼴틀딱시키들이 다 디져야 나라가 똑바로 될것같다..답이 없는 종자들ㅠ'
 'label': [2, 3, 4]
}
```

### Data Fields

* `text`: utterance from Korean online news comment.
* `label`: the label numbers matching with 8 fine-grained hate speech classes and `not hate speech` class are follows.
  * `0`: `Origin`(`출신차별`) hate speech based on place of origin or identity;
  * `1`: `Physical`(`외모차별`) hate speech based on physical appearance (e.g. body, face) or disability;
  * `2`: `Politics`(`정치성향차별`) hate speech based on political stance;
  * `3`: `Profanity`(`혐오욕설`) hate speech in the form of swearing, cursing, cussing, obscene words, or expletives; or an unspecified hate speech category;
  * `4`: `Age`(`연령차별`) hate speech based on age;
  * `5`: `Gender`(`성차별`) hate speech based on gender or sexual orientation (e.g. woman, homosexual);
  * `6`: `Race`(`인종차별`) hate speech based on ethnicity;
  * `7`: `Religion`(`종교차별`) hate speech based on religion;
  * `8`: `Not Hate Speech`(`해당사항없음`).

### Data Splits

In our repository, we provide splitted datasets that have 78,977(train) / 8,776 (validation) / 21,939 (test) samples, preserving the class proportion.

## Dataset Creation

### Curation Rationale

We propose K-MHaS, a large size Korean multi-label hate speech detection dataset that represents Korean language patterns effectively. Most datasets in hate speech research are annotated using a single label classification of particular aspects, even though the subjectivity of hate speech cannot be explained with a mutually exclusive annotation scheme. We propose a multi-label hate speech annotation scheme that allows overlapping labels associated with the subjectivity and the intersectionality of hate speech. 

### Source Data

#### Initial Data Collection and Normalization

Our dataset is based on the Korean online news comments available on Kaggle and Github. The unlabeled raw data was collected between January 2018 and June 2020. Please see the details in our paper [K-MHaS](https://aclanthology.org/2022.coling-1.311) published at COLING2020. 


#### Who are the source language producers?

The language producers are users who left the comments on the Korean online news platform between 2018 and 2020. 

### Annotations

#### Annotation process

We begin with the common categories of hate speech found in literature and match the keywords for each category. After the preliminary round, we investigate the results to merge or remove labels in order to provide the most representative subtype labels of hate speech contextual to the cultural background. Our annotation instructions explain a twolayered annotation to (a) distinguish hate and not hate speech, and (b) the categories of hate speech. Annotators are requested to consider given keywords or alternatives of each category within social, cultural, and historical circumstances. For more details, please refer to the paper [K-MHaS](https://aclanthology.org/2022.coling-1.311).

#### Who are the annotators?

Five native speakers were recruited for manual annotation in both the preliminary and main rounds. 

### Personal and Sensitive Information

This datasets contains examples of hateful language, however, has no personal information.

## Considerations for Using the Data

### Social Impact of Dataset

We propose K-MHaS, a new large-sized dataset for Korean hate speech detection with a multi-label annotation scheme. We provided extensive baseline experiment results, presenting the usability of a dataset to detect Korean language patterns in hate speech.

### Discussion of Biases

All annotators were recruited from a crowdsourcing platform. They were informed about hate speech before handling the data. Our instructions allowed them to feel free to leave if they were uncomfortable with the content. With respect to the potential risks, we note that the subjectivity of human annotation would impact on the quality of the dataset.

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

This dataset is curated by Taejun Lim, Heejun Lee and Bogeun Jo.

### Licensing Information

Creative Commons Attribution-ShareAlike 4.0 International (cc-by-sa-4.0).

### Citation Information

```
@inproceedings{lee-etal-2022-k,
    title = "K-{MH}a{S}: A Multi-label Hate Speech Detection Dataset in {K}orean Online News Comment",
    author = "Lee, Jean  and
      Lim, Taejun  and
      Lee, Heejun  and
      Jo, Bogeun  and
      Kim, Yangsok  and
      Yoon, Heegeun  and
      Han, Soyeon Caren",
    booktitle = "Proceedings of the 29th International Conference on Computational Linguistics",
    month = oct,
    year = "2022",
    address = "Gyeongju, Republic of Korea",
    publisher = "International Committee on Computational Linguistics",
    url = "https://aclanthology.org/2022.coling-1.311",
    pages = "3530--3538",
    abstract = "Online hate speech detection has become an important issue due to the growth of online content, but resources in languages other than English are extremely limited. We introduce K-MHaS, a new multi-label dataset for hate speech detection that effectively handles Korean language patterns. The dataset consists of 109k utterances from news comments and provides a multi-label classification using 1 to 4 labels, and handles subjectivity and intersectionality. We evaluate strong baselines on K-MHaS. KR-BERT with a sub-character tokenizer outperforms others, recognizing decomposed characters in each hate speech class.",
}
```

### Contributions
The contributors of the work are: 
- [Jean Lee](https://jeanlee-ai.github.io/) (The University of Sydney)
- [Taejun Lim](https://github.com/taezun) (The University of Sydney)
- [Heejun Lee](https://bigwaveai.com/) (BigWave AI)
- [Bogeun Jo](https://bigwaveai.com/) (BigWave AI)
- Yangsok Kim (Keimyung University)
- Heegeun Yoon (National Information Society Agency)
- [Soyeon Caren Han](https://drcarenhan.github.io/) (The University of Western Australia and The University of Sydney)
