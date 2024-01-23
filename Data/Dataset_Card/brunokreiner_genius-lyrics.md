---
# For reference on model card metadata, see the spec: https://github.com/huggingface/hub-docs/blob/main/datasetcard.md?plain=1
# Doc / guide: https://huggingface.co/docs/hub/datasets-cards
{}
---

# Dataset Card for Dataset Name

## Dataset Description

- **Homepage:** 
- **Repository:** 
- **Paper:** 
- **Leaderboard:** 
- **Point of Contact:** 

### Dataset Summary

This dataset consists of roughly 480k english (classified using nltk language classifier) lyrics with some more meta data. The meta data was taken from the million playlist challenge @ AICrowd. The lyrics were crawled using the song and artist name with the lyricsgenius python package. There is no guarantee that the lyrics are the correct one though the data was cleaned and verified. The lyrics crawled came with the song name in its payload, if the song names in the payload and from our side don't match (using the package fuzzywuzzy string matching with a score of under 60) then it wasn't included in this set of lyrics. Still some lyrics might be wrong due to the nature of the data.
49'985 rows have a list of genres, crawled from the official Spotify API. This list of genres are from the artist of the song since spotify doesn't provide genres for every individual song. 

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

[More Information Needed]

## Dataset Structure

### Data Instances

[More Information Needed]

### Data Fields

[More Information Needed]

### Data Splits

[More Information Needed]

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

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

[More Information Needed]

### Licensing Information

[More Information Needed]

### Citation Information

[More Information Needed]

### Contributions

[More Information Needed]