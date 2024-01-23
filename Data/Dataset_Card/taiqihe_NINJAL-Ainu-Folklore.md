---
license: cc-by-sa-4.0
---

# Dataset Card for NINJAL Ainu Folklore

## Dataset Description

- **Original source** [A Glossed Audio Corpus of Ainu folklore](https://ainu.ninjal.ac.jp/folklore/en/)

### Dataset Summary

Ainu is an endangered (nearly extinct) language spoken in Hokkaido, Japan. This dataset contains recordings of 38 traditional Ainu folktales by two Ainu speakers (Mrs. Kimi Kimura and Mrs. Ito Oda), along with their transcriptions (in Latin script), English translations, and underlying and surface gloss forms in English. (For transcriptions in Katakana and translation/gloss in Japanese, please see the original corpus webpage.) In total, there are over 8 hours (~7.7k sentences) of transcribed and glossed speech. 

### Annotations

The glosses in this dataset are the original glosses from the Glossed Audio Corpus, with minor changes to fit the Generalized Glossing Format (e.g. multi-word translations of individual morphemes are now separated by underscores instead of periods). Uncertainty in interpretation by the original annotators is indicated with a question mark (?). Additional notes on the Latin transcriptions in the corpus can be found on the original corpus webpage (under the "Structure, Transcriptions, and Glosses" tab).  

## Additional Information

### Limitations

This dataset has a small number of speakers and a limited domain, and models trained on this dataset might not be suitable for general purpose applications. The audio data contain varying degrees of noise which makes this dataset a poor fit for training TTS models.

### Acknowledgement

We would like to thank the original authors of the Glossed Audio Corpus of Ainu Folklore for their dedication and care in compiling these resources, and kindly ask anyone who uses this dataset to cite them in their work.

### License

Attribution-ShareAlike 4.0 International ([cc-by-sa-4.0](https://creativecommons.org/licenses/by-sa/4.0/))

### Original Source

```
@misc{ninjal-ainu-folklore,
  title={A Glossed Audio Corpus of Ainu Folklore},
  url={https://ainu.ninjal.ac.jp/folklore/},
  author={Nakagawa, Hiroshi and Bugaeva, Anna and Kobayashi, Miki and Yoshikawa, Yoshimi},
  publisher={The National Institute for Japanese Language and Linguistics ({NINJAL})},
  date={2016--2021}
} 
```