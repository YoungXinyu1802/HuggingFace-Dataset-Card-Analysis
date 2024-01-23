# Dataset Card for ConcluGen

## Table of Contents
- [Dataset Card for ConcluGen](#dataset-card-for-conclugen)
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

- **Homepage:** https://zenodo.org/record/4818134
- **Repository:** https://github.com/webis-de/acl21-informative-conclusion-generation
- **Paper:** [Generating Informative Conclusions for Argumentative Texts](https://aclanthology.org/2021.findings-acl.306.pdf)
- **Leaderboard:** [N/A]
- **Point of Contact:** [Shahbaz Syed](mailto:shahbaz.syed@uni-leipzig.de)

### Dataset Summary

The ConcluGen corpus is constructed for the task of argument summarization. It consists of 136,996 pairs of argumentative texts and their conclusions collected from the ChangeMyView subreddit, a web portal for argumentative discussions on controversial topics.

The corpus has three variants: topics, aspects, and targets. Each variation encodes the corresponding information via control codes. These provide additional argumentative knowledge for generating more informative conclusions. 

### Supported Tasks and Leaderboards

Argument Summarization, Conclusion Generation

### Languages

English ('en') as spoken by Reddit users on the [r/changemyview](https://old.reddit.com/r/changemyview/) subreddits. 

## Dataset Structure

### Data Instances

An example consists of a unique 'id', an 'argument', and its 'conclusion'. 

**base** 

Contains only the argument and its conclusion.
```
{'id': 'ee11c116-23df-4795-856e-8b6c6626d5ed',
 'argument': "In my opinion, the world would be a better place if alcohol was illegal. I've done a little bit of research to get some numbers, and I was quite shocked at what I found. Source On average, one in three people will be involved in a drunk driving crash in their lifetime. In 2011, 9,878 people died in drunk driving crashes Drunk driving costs each adult in this country almost 500 per year. Drunk driving costs the United States 132 billion a year. Every day in America, another 27 people die as a result of drunk driving crashes. Almost every 90 seconds, a person is injured in a drunk driving crash. These are just the driving related statistics. They would each get reduced by at least 75 if the sale of alcohol was illegal. I just don't see enough positives to outweigh all the deaths and injuries that result from irresponsible drinking. Alcohol is quite literally a drug, and is also extremely addicting. It would already be illegal if not for all these pointless ties with culture. Most people wouldn't even think to live in a world without alcohol, but in my opinion that world would be a better, safer, and more productive one. , or at least defend the fact that it's legal.",
 'conclusion': 'I think alcohol should be illegal.'}
 ```

**topic**

Argument encoded with the discussion topic.
```
{"id":"b22272fd-00d2-4373-b46c-9c1d9d21e6c2","argument":"<|TOPIC|>Should Planned Parenthood Be Defunded?<|ARGUMENT|>Even the best contraceptive methods such as surgical sterilisation can fail, and even with perfect use the pill may not work.<|CONCLUSION|>","conclusion":"Even with the best intentions and preparation, contraceptives can and do fail."}

```

**aspects** 

Argument encoded with the discussion topic and argument's aspects.

```
{"id":"adc92826-7892-42d4-9405-855e845bf027","argument":"<|TOPIC|>Gender Neutral Bathrooms: Should They be Standard?<|ARGUMENT|>Men's toilets and women's urine have different odours due to hormone differences in each biological sex. As a result, the urine of one sex may smell much worse to the other sex and vice versa, meaning that it is logical to keep their toilet facilities separate.<|ASPECTS|>hormone differences, urine, separate, facilities, different odours, smell much worse<|CONCLUSION|>","conclusion":"Men and women, because of their different biological characteristics, each need a different type of bathroom. Gender-segregated bathrooms reflect and honour these differences."}


```
**targets**

Argument encoded with the discussion topic and possible conclusion targets.

```
{"id":"c9a87a03-edda-42be-9c0d-1e7d2d311816","argument":"<|TOPIC|>Australian republic vs. monarchy<|ARGUMENT|>The monarchy is a direct reflection of Australia's past as a British colony and continues to symbolize Australia's subservience to the British crown. Such symbolism has a powerfully negative effect on Australians' sense of independence and identity. Ending the monarchy and establishing a republic would constitute a substantial stride in the direction of creating a greater sense of independence and national pride and identity.<|TARGETS|>Such symbolism, The monarchy, Ending the monarchy and establishing a republic<|CONCLUSION|>","conclusion":"Ending the monarchy would foster an independent identity in Australia"}

```


### Data Fields

- `id`: a string identifier for each example.
- `argument`: the argumentative text.
- `conclusion`: the conclusion of the argumentative text.


### Data Splits

The data is split into train, validation, and test splits for each variation of the dataset (including base). 

|         	| Train   	| Validation 	| Test 	|
|---------	|---------	|------------	|------	|
| Base    	| 116,922 	| 12,224     	| 1373 	|
| Aspects 	| 120,142 	| 12,174     	| 1357 	|
| Targets 	| 109,376 	| 11,053     	| 1237 	|
| Topic   	| 121,588 	| 12,335     	| 1372 	|


## Dataset Creation

### Curation Rationale

ConcluGen was built as a first step towards argument summarization technology. The [rules of the subreddit](https://old.reddit.com/r/changemyview/wiki/rules) ensure high quality data suitable for the task. 

### Source Data

#### Initial Data Collection and Normalization

Reddit [ChangeMyView](https://old.reddit.com/r/changemyview/) 

#### Who are the source language producers?

Users of the subreddit [r/changemyview](https://old.reddit.com/r/changemyview/). Further demographic information is unavailable from the data source.

### Annotations

The dataset is augmented with automatically extracted knowledge such as the argument's aspects, the discussion topic, and possible conclusion targets. 

#### Annotation process

[N/A]

#### Who are the annotators?

[N/A]

### Personal and Sensitive Information

Only the argumentative text and its conclusion are provided. No personal information of the posters is included.

## Considerations for Using the Data

### Social Impact of Dataset

[Needs More Information]

### Discussion of Biases

[Needs More Information]

### Other Known Limitations

[Needs More Information]

## Additional Information

### Dataset Curators

[Needs More Information]

### Licensing Information

The licensing status of the dataset hinges on the legal status of the [Pushshift.io](https://files.pushshift.io/reddit/) data which is unclear.

### Citation Information

```
@inproceedings{syed:2021,
  author    = {Shahbaz Syed and
               Khalid Al Khatib and
               Milad Alshomary and
               Henning Wachsmuth and
               Martin Potthast},
  editor    = {Chengqing Zong and
               Fei Xia and
               Wenjie Li and
               Roberto Navigli},
  title     = {Generating Informative Conclusions for Argumentative Texts},
  booktitle = {Findings of the Association for Computational Linguistics: {ACL/IJCNLP}
               2021, Online Event, August 1-6, 2021},
  pages     = {3482--3493},
  publisher = {Association for Computational Linguistics},
  year      = {2021},
  url       = {https://doi.org/10.18653/v1/2021.findings-acl.306},
  doi       = {10.18653/v1/2021.findings-acl.306}
}
```

