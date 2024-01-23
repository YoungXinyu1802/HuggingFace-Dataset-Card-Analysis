# Parallel Sentences for 50+ languages

This repository contains parallel sentences (i.e. English + same sentences in other language) for 50+ different languages in a simple tsv.gz format:
```
english_sentences\tsentence_in_other_language
```

Sentences stem from the [OPUS website](https://opus.nlpl.eu/).

The following datasets are included:
- [Europarl](https://opus.nlpl.eu/Europarl.php)
- [GlobalVoices](https://opus.nlpl.eu/GlobalVoices.php)
- [JW300](https://opus.nlpl.eu/JW300.php)
- [MUSE](https://github.com/facebookresearch/MUSE)
- [News-Commentary](https://opus.nlpl.eu/News-Commentary.php)
- [OpenSubtitles](https://opus.nlpl.eu/OpenSubtitles.php)
- [Tatoeba](https://tatoeba.org/)
- Talks - Custom translated transcripts of talks
- [WikiMatrix](https://opus.nlpl.eu/WikiMatrix.php)
- WikiTitles - Custom dataset with parallel Wikipedia titles

## Usage

These sentences can be used to train multi-lingual sentence embedding models. For more details, see [SBERT.net - Multilingual-Model](https://www.sbert.net/examples/training/multilingual/README.html)

**This dataset can not yet be used with Hugging Face dataset library. You must download the individual TSV files.**
