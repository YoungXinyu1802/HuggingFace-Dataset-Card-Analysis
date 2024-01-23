---
task_categories:
- automatic-speech-recognition
dataset_info:
  features:
  - name: id
    dtype: string
  - name: channel
    dtype: string
  - name: channel_id
    dtype: string
  - name: title
    dtype: string
  - name: categories
    sequence: string
  - name: tags
    sequence: string
  - name: description
    dtype: string
  - name: text
    dtype: string
  - name: segments
    list:
    - name: start
      dtype: float64
    - name: end
      dtype: float64
    - name: text
      dtype: string
  splits:
  - name: train
    num_bytes: 177776633.92326075
    num_examples: 5655
  download_size: 100975518
  dataset_size: 177776633.92326075
tags:
- whisper
- whispering
- medium
---
# Dataset Card for "whisper-transcripts-linustechtips"

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
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
  - [Contributions](#contributions)

## Dataset Description

- **Homepage:** [Whispering-GPT](https://github.com/matallanas/whisper_gpt_pipeline)
- **Repository:** [whisper_gpt_pipeline](https://github.com/matallanas/whisper_gpt_pipeline)
- **Paper:** [whisper](https://cdn.openai.com/papers/whisper.pdf) and [gpt](https://s3-us-west-2.amazonaws.com/openai-assets/research-covers/language-unsupervised/language_understanding_paper.pdf)
- **Point of Contact:** [Whispering-GPT organization](https://huggingface.co/Whispering-GPT)

### Dataset Summary

This dataset is created by applying whisper to the videos of the Youtube channel [Linus Tech Tips](https://www.youtube.com/channel/UCXuqSBlHAE6Xw-yeJA0Tunw). The dataset was created a medium size whisper model.

### Languages

- **Language**: English

## Dataset Structure

The dataset 

### Data Fields

The dataset is composed by:
- **id**: Id of the youtube video.
- **channel**: Name of the channel.
- **channel\_id**: Id of the youtube channel.
- **title**: Title given to the video.
- **categories**: Category of the video.
- **description**: Description added by the author.
- **text**: Whole transcript of the video.
- **segments**: A list with the time and transcription of the video.
  - **start**: When started the trancription.
  - **end**: When the transcription ends.
  - **text**: The text of the transcription.

### Data Splits

- Train split.

## Dataset Creation

### Source Data

The transcriptions are from the videos of [Linus Tech Tips Channel](https://www.youtube.com/channel/UCXuqSBlHAE6Xw-yeJA0Tunw)

### Contributions

Thanks to [Whispering-GPT](https://huggingface.co/Whispering-GPT) organization for adding this dataset.