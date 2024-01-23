---
license: mit
---
---
language_creators:
- other
license:
- mit
multilinguality:
- monolingual
pretty_name: narrative-arc
size_categories: []
source_datasets: []
tags: []
task_categories:
- text-classification
task_ids: []
---

# Dataset Card for [narrative-arc]

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
- **Repository:**
- **Paper:**
- **Leaderboard:**
- **Point of Contact:**

### Dataset Summary

Dataset of stories used for Narrative Arc post-processing. An instance of a story in this dataset will include the original text and its metadata, the transformer model used to make the embeddings, the model's checkpoint, the window indices of the stored embeddings, and the embeddings.

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

[More Information Needed]

## Dataset Structure

### Data Instances

[More Information Needed]

### Data Fields

An example story will look like the following:

    {
      "book name": "",
        "book meta data": "",
        "full text": "",
        "model": {
            "distilbert-base-cased": {
                     "window indices": (first_index, last_index),
                     "embeddings": [[]] },
    
            "distilbert-base-uncased": {
                      "window indices": (first_index, last_index),
                      "embeddings": [[]] 
            }
            },
        }
      ...
    }

### Data Splits

[More Information Needed]

## Dataset Creation

### Curation Rationale

The processed text needs to be stored somewhere that is both accessible and can accomodate the large amount of data generated. 

### Source Data

#### Initial Data Collection and Normalization

The data were sourced from the Project Gutenberg[https://www.gutenberg.org/] library.

#### Who are the source language producers?

Each instance in the dataset represents a text written by a human author. At present, data selected for processing are English-language short stories.

### Personal and Sensitive Information

Not applicable.

## Considerations for Using the Data

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