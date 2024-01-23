Dataset Summary
The Common Voice dataset consists of a unique MP3 and corresponding text file. Many of the 9,283 recorded hours in the dataset also include demographic metadata like age, sex, and accent that can help train the accuracy of speech recognition engines.

The dataset currently consists of 7,335 validated hours in 60 languages, but were always adding more voices and languages. Take a look at our Languages page to request a language or start contributing.

Supported Tasks and Leaderboards
[Needs More Information]

Languages
English

Dataset Structure
Data Instances
A typical data point comprises the path to the audio file, called path and its sentence. Additional fields include accent, age, client_id, up_votes down_votes, gender, locale and segment.

{'accent': 'netherlands', 'age': 'fourties', 'client_id': 'bbbcb732e0f422150c30ff3654bbab572e2a617da107bca22ff8b89ab2e4f124d03b6a92c48322862f60bd0179ae07baf0f9b4f9c4e11d581e0cec70f703ba54', 'down_votes': 0, 'gender': 'male', 'locale': 'nl', 'path': 'nl/clips/common_voice_nl_23522441.mp3', 'segment': "''", 'sentence': 'Ik vind dat een dubieuze procedure.', 'up_votes': 2, 'audio': {'path':nl/clips/common_voice_nl_23522441.mp3', 'array': array([-0.00048828, -0.00018311, -0.00137329, ..., 0.00079346, 0.00091553, 0.00085449], dtype=float32), 'sampling_rate': 48000} `

Data Fields
client_id: An id for which client (voice) made the recording

path: The path to the audio file

audio: A dictionary containing the path to the downloaded audio file, the decoded audio array, and the sampling rate. Note that when accessing the audio column: dataset[0]["audio"] the audio file is automatically decoded and resampled to dataset.features["audio"].sampling_rate. Decoding and resampling of a large number of audio files might take a significant amount of time. Thus it is important to first query the sample index before the "audio" column, i.e. dataset[0]["audio"] should always be preferred over dataset["audio"][0].

sentence: The sentence the user was prompted to speak

up_votes: How many upvotes the audio file has received from reviewers

down_votes: How many downvotes the audio file has received from reviewers

age: The age of the speaker.

gender: The gender of the speaker

accent: Accent of the speaker

locale: The locale of the speaker

segment: Usually empty field

Data Splits
The speech material has been subdivided into portions for dev, train, test, validated, invalidated, reported and other.

The validated data is data that has been validated with reviewers and recieved upvotes that the data is of high quality.

The invalidated data is data has been invalidated by reviewers and recieved downvotes that the data is of low quality.

The reported data is data that has been reported, for different reasons.

The other data is data that has not yet been reviewed.

The dev, test, train are all data that has been reviewed, deemed of high quality and split into dev, test and train.

Dataset Creation
Curation Rationale
[Needs More Information]

Source Data
Initial Data Collection and Normalization
[Needs More Information]

Who are the source language producers?
[Needs More Information]

Annotations
Annotation process
[Needs More Information]

Who are the annotators?
[Needs More Information]

Personal and Sensitive Information
The dataset consists of people who have donated their voice online. You agree to not attempt to determine the identity of speakers in the Common Voice dataset.

Considerations for Using the Data
Social Impact of Dataset
The dataset consists of people who have donated their voice online. You agree to not attempt to determine the identity of speakers in the Common Voice dataset.

Discussion of Biases
[More Information Needed]

Other Known Limitations
[More Information Needed]

Additional Information
Dataset Curators
[More Information Needed]

Licensing Information
Public Domain, CC-0

Citation Information
@inproceedings{commonvoice:2020,
  author = {Ardila, R. and Branson, M. and Davis, K. and Henretty, M. and Kohler, M. and Meyer, J. and Morais, R. and Saunders, L. and Tyers, F. M. and Weber, G.},
  title = {Common Voice: A Massively-Multilingual Speech Corpus},
  booktitle = {Proceedings of the 12th Conference on Language Resources and Evaluation (LREC 2020)},
  pages = {4211--4215},
  year = 2020
}
