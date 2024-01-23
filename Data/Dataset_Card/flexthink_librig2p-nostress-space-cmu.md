# librig2p-nostress - Grapheme-To-Phoneme Dataset

This dataset contains samples that can be used to train a Grapheme-to-Phoneme system **without** stress information.

The dataset is derived from the following pre-existing datasets:

* [LibriSpeech ASR Corpus](https://www.openslr.org/12)
* [LibriSpeech Alignments](https://github.com/CorentinJ/librispeech-alignments)
* [Wikipedia Homograph Disambiguation Data](https://github.com/google/WikipediaHomographData)
* [CMUDict] (http://www.speech.cs.cmu.edu/cgi-bin/cmudict)

This version of the dataset applies a correction to LibriSpeech Alignments phoneme annotations by looking up the pronunciations of known words in CMUDict and replacing them with their CMUDict counterparts only if a perfect unique match is found. This reduces the number of discrepancies between homograph data and LibriSpeech data.