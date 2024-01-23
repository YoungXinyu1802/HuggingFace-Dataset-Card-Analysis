TODO: Add YAML tags here. Copy-paste the tags obtained with the online tagging app: https://huggingface.co/spaces/huggingface/datasets-tagging
---
annotations_creators:
- no-annotation
language_creators:
- found
language:
- en
license:
- unknown
multilinguality:
- monolingual
size_categories:
- 30k<n<50k
source_datasets:
- original
task_categories:
- text-classification
task_ids:
- fact-checking
- intent-classification
pretty_name: GonzaloA / Fake News
---

# Dataset Card for [Fake_News_TFG]

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

- **Homepage:**
- **Repository:** [GonzaloA / fake_news]
- **Paper:** [Título del TFG]
- **Leaderboard:**
- **Point of Contact:** [Gonzalo Álvarez Hervás](mailto:g.alvarez.2018@alumnos.urjc.es)

### Dataset Summary

The GonzaloA / Fake_News_TFG Dataset repository is an English-language dataset containing just over 45k unique news articles. This articles are classified as true (1) or false (0). The current version is the first of the study the Fake News identification using Transformers models.

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

The dataset is code for English as generally spoken in the United States is en-US

## Dataset Structure

The structure of this dataSet is composed by 40587 fields about News. This fields are composed by three types of fields; title of the news, the text or content of the news, and finally, the value of the news, who said if the new are fake (0) or true (1).

### Data Instances

For each instance, there is a string for the title, a string for the article and a label to mark if it's true or false. See the [CNN / Daily Mail dataset viewer](https://huggingface.co/datasets/viewer/?dataset=fake_news&config=3.0.0) to explore more examples.

```
{'id': '1',
'title': Palestinians switch off Christmas lights in Bethlehem in anti-Trump protest'
'text': 'RAMALLAH, West Bank (Reuters) - Palestinians switched off Christmas lights at Jesus  traditional birthplace in Bethlehem on Wednesday night in protest at U.S. President Donald Trump s decision to recognize Jerusalem as Israel s capital. A Christmas tree adorned with lights outside Bethlehem s Church of the Nativity, where Christians believe Jesus was born, and another in Ramallah, next to the burial site of former Palestinian leader Yasser Arafat, were plunged into darkness.  The Christmas tree was switched off on the order of the mayor today in protest at Trump s decision,  said Fady Ghattas, Bethlehem s municipal media officer.  He said it was unclear whether the illuminations would be turned on again before the main Christmas festivities. In a speech in Washington, Trump said he had decided to recognize Jerusalem as Israel s capital and move the U.S. embassy to the city. Israeli Prime Minister Benjamin Netanyahu said Trump s move  marked the beginning of a new approach to the Israeli-Palestinian conflict and said it was an  historic landmark . Arabs and Muslims across the Middle East condemned the U.S. decision, calling it an incendiary move in a volatile region and the European Union and United Nations also voiced alarm at the possible repercussions for any chances of reviving Israeli-Palestinian peacemaking.'
'label': '1'}
```

### Data Fields

- `id`: an integer value to count the rows in the dataset
- `title`: a string that summarize the article
- `text`: a string that contains the article
- `label`: a boolean that mark the article true or false

### Data Splits

The GonzaloA/FakeNews dataset has 3 splits: train, evaluation, and test. Below are the statistics for the version 1.0 of the dataset:

| Dataset Split | Number of Instances in Split                |
| ------------- | ------------------------------------------- |
| Train         | 24,353                                      |
| Validation    | 8,117                                       |
| Test          | 8,117                                       |

## Dataset Creation

This dataset was created with python, using pandas library as the main processing data. Also, this dataset are the mix of other datasets which are the same scope, the Fake News. All of the process is available in this repository: https://github.com/G0nz4lo-4lvarez-H3rv4s/FakeNewsDetection

### Source Data
The source data is a mix of multiple fake_news datasets in Kaggle, a platform for train your skills and learnings about Artificial Intelligence. The main datasets who are based this dataset are: 

#### Initial Data Collection and Normalization

Version 1.0.0 aimed to support supervised neural methodologies for deep learning and study the new Transformers models in the Natural Language Processing with News of the United States. 

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data
This Dataset is compose for 3 types: Training phase, for training your model of NLP, validation phase, because we need to validate if the training was successful or our model has overfitting, and train phase, who count the probability and the mistakes in the model fine-tuning.

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

[More Information Needed]

### Licensing Information

[More Information Needed]

### Citation Information

[More Information Needed]

### Contributions

Thanks to [@github-username](https://github.com/<github-username>) for adding this dataset.