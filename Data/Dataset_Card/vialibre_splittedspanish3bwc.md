---

language:
- 'es'
multilinguality:
- monolingual
pretty_name: "Unannotated Spanish 3 Billion Words Corpora"
license:
- mit
---

# Dataset Card for Unannotated Spanish 3 Billion Words Corpora

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Languages](#languages)
  - [Source Data](#source-data)
  - [Data Subset](#data-subset)
- [Additional Information](#additional-information)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)


## Dataset Description
- **Repository:** https://github.com/josecannete/spanish-corpora
- **Paper:** https://users.dcc.uchile.cl/~jperez/papers/pml4dc2020.pdf

### Dataset Summary
* Number of lines: 300904000 (300M)
* Number of tokens: 2996016962 (3B)
* Number of chars: 18431160978 (18.4B)

### Languages
* Spanish

### Source Data
* Available to download here: [Zenodo](https://doi.org/10.5281/zenodo.3247731)

### Data Subset
* Spanish Wikis: Wich include Wikipedia, Wikinews, Wikiquotes and more. These were first processed with wikiextractor (https://github.com/josecannete/wikiextractorforBERT) using the wikis dump of 20/04/2019.
* ParaCrawl: Spanish portion of ParaCrawl (http://opus.nlpl.eu/ParaCrawl.php)
* EUBookshop: Spanish portion of EUBookshop (http://opus.nlpl.eu/EUbookshop.php)
* MultiUN: Spanish portion of MultiUN (http://opus.nlpl.eu/MultiUN.php)
* OpenSubtitles: Spanish portion of OpenSubtitles2018 (http://opus.nlpl.eu/OpenSubtitles-v2018.php)
* DGC: Spanish portion of DGT (http://opus.nlpl.eu/DGT.php)
* DOGC: Spanish portion of DOGC (http://opus.nlpl.eu/DOGC.php)
* ECB: Spanish portion of ECB (http://opus.nlpl.eu/ECB.php)
* EMEA: Spanish portion of EMEA (http://opus.nlpl.eu/EMEA.php)
* Europarl: Spanish portion of Europarl (http://opus.nlpl.eu/Europarl.php)
* GlobalVoices: Spanish portion of GlobalVoices (http://opus.nlpl.eu/GlobalVoices.php)
* JRC: Spanish portion of JRC (http://opus.nlpl.eu/JRC-Acquis.php)
* News-Commentary11: Spanish portion of NCv11 (http://opus.nlpl.eu/News-Commentary-v11.php)
* TED: Spanish portion of TED (http://opus.nlpl.eu/TED2013.php)
* UN: Spanish portion of UN (http://opus.nlpl.eu/UN.php)

## Additional Information

### Licensing Information

* [MIT Licence](https://github.com/josecannete/spanish-corpora/blob/master/LICENSE)

### Citation Information

```
@dataset{jose_canete_2019_3247731,
  author       = {José Cañete},
  title        = {Compilation of Large Spanish Unannotated Corpora},
  month        = may,
  year         = 2019,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.3247731},
  url          = {https://doi.org/10.5281/zenodo.3247731}
}

@inproceedings{CaneteCFP2020,
  title={Spanish Pre-Trained BERT Model and Evaluation Data},
  author={Cañete, José and Chaperon, Gabriel and Fuentes, Rodrigo and Ho, Jou-Hui and Kang, Hojin and Pérez, Jorge},
  booktitle={PML4DC at ICLR 2020},
  year={2020}
}
```