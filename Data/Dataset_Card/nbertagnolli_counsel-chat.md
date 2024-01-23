# Dataset Card for [Dataset Name]

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

- **Homepage: https://towardsdatascience.com/counsel-chat-bootstrapping-high-quality-therapy-data-971b419f33da**
- **Repository: https://github.com/nbertagnolli/counsel-chat**
- **Paper: https://towardsdatascience.com/counsel-chat-bootstrapping-high-quality-therapy-data-971b419f33da**
- **Leaderboard: NA**
- **Point of Contact: nbertagnolli**

### Dataset Summary

Scrape of Counselchat.com's forum. CounselChat.com is an example of an expert community.
It is a platform to help counselors build their reputation and make meaningful contact with potential clients. 
On the site, therapists respond to questions posed by clients, and users can like responses that they find most helpful. 
It’s a nice idea and lends itself to some interesting data.  This data contains expert responses by licensed clinicialns
to questions posed by individuals.

### Supported Tasks and Leaderboards

NA

### Languages

English

## Dataset Structure

### Data Instances

[More Information Needed]

### Data Fields

* questionID — A unique question identifier which is distinct for every question

* questionTitle — The title of the question on counsel chat
* questionText — The body of the individual’s question to counselors
* questionLink — A URL to the last location of that question (might not still be active)
* topic — The topic the question was listed under
* therapistInfo — The summary of each therapist, usually a name and specialty
* therapistURL — a link to the therapist’s bio on counselchat
* answerText — The therapist response to the question
* upvotes — The number of upvotes the answerText received
* split — The data split for training, validation, and testing.

### Data Splits

[More Information Needed]

## Dataset Creation

### Curation Rationale

There is a lack of high quality open source mental health data available for study in NLP. Most datasets revolve around
forums like Reddit, which can provide great insights, but don't capture the type of language often used by counselors. 
This dataset seeks to help bridge that gap and provide some additional data of counselors interacting with patients in 
need.

### Source Data
The dataset was scraped on 20220401 from counselchat.com. 

#### Initial Data Collection and Normalization

The dataset was scraped on 20220401 from counselchat.com.  The data is in it's raw form and has not been normalized.

#### Who are the source language producers?

The text was written by licensed counselors in the United States and annonymous individuals.

### Annotations
The dataset does not contain any additional annotations.

### Personal and Sensitive Information

This data is not anonymized, so individuals' names can be found in the dataset.  CounselChat.com allows therapists to advertise for their clinics
by providing sound publicly available advise. The therapist names have been kept as part of the original dataset.

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

nicolas bertagnolli

### Licensing Information

MIT

### Citation Information

Bertagnolli, N. Counsel Chat: Bootstrapping High-Quality Therapy Data. Available online: https://towardsdatascience.com/counsel-chat-bootstrapping-high-quality-therapy-data-971b419f33da

### Contributions

Thanks to [@nbertagnolli](https://github.com/nbertagnolli) for adding this dataset.
