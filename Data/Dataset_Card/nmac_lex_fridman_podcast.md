---
task_categories:
- automatic-speech-recognition
- sentence-similarity
language:
- en
tags:
- podcast
- whisper
size_categories:
- 100K<n<1M
---
# Dataset Card for "lex_fridman_podcast"

### Dataset Summary

This dataset contains transcripts from the [Lex Fridman podcast](https://www.youtube.com/playlist?list=PLrAXtmErZgOdP_8GztsuKi9nrraNbKKp4) (Episodes 1 to 325).
The transcripts were generated using [OpenAI Whisper](https://github.com/openai/whisper) (large model) and made publicly available at: https://karpathy.ai/lexicap/index.html.


### Languages

- English


## Dataset Structure

The dataset contains around 803K entries, consisting of audio transcripts generated from episodes 1 to 325 of the [Lex Fridman podcast](https://www.youtube.com/playlist?list=PLrAXtmErZgOdP_8GztsuKi9nrraNbKKp4).  In addition to the transcript text, the dataset includes other metadata such as episode id and title, guest name, and start and end timestamps for each transcript.

### Data Fields

The dataset schema is as follows:
- **id**: Episode id.
- **guest**: Name of the guest interviewed.
- **title:** Title of the episode.
- **text:** Text of the transcription.
- **start:** Timestamp (`HH:mm:ss.mmm`) indicating the beginning of the trancription.
- **end:** Timestamp (`HH:mm:ss.mmm`) indicating the end of the trancription.


### Source Data

Source data provided by Andrej Karpathy at: https://karpathy.ai/lexicap/index.html

### Contributions

Thanks to [nmac](https://huggingface.co/nmac) for adding this dataset.