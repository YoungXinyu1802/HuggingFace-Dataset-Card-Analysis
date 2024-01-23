**DISCLAIMER:** None of the data here is of my property, but this is rather a extraction and compilation of data from different sources into one common place.

Currently the sources are [spanish CSS10](https://www.kaggle.com/datasets/bryanpark/spanish-single-speaker-speech-dataset) and [this Kaggle Dataset](https://www.kaggle.com/datasets/carlfm01/120h-spanish-speech).

The code used to create combine.zip can be found [here](https://github.com/lopezjuanma96/spanish_voices), it requires you to download the full datasets because the Kaggle API was not working properly, at least for me at the time of creating this: it only allowed me access to the first ~30 files of a dataset when trying to download specifically, the other option was downloading the whole dataset.

The main reason I created this is for my project of adapting [this VITS fine-tuning](https://github.com/Plachtaa/VITS-fast-fine-tuning) script to [spanish](https://github.com/lopezjuanma96/VITS-fast-fine-tuning), therefore the format given to the transcript file and the distribution and amount of audio data, but it can probably be adapted to other formats easily.