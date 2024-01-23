# BAYƐLƐMABAGA: Parallel French - Bambara Dataset for Machine Learning

## Overview
The Bayelemabaga dataset is a collection of 44562 aligned machine translation ready Bambara-French lines, originating from [Corpus Bambara de Reference](http://cormande.huma-num.fr/corbama/run.cgi/first_form). The dataset is constitued of text extracted from **264** text files, varing from periodicals, books, short stories, blog posts, part of the Bible and the Quran.  

## Snapshot: 46976
|    |    |
|:---|---:|
| **Lines** | **46976** |
| French Tokens (spacy) | 691312 |
| Bambara Tokens (daba) | 660732 |
| French Types | 32018 |
| Bambara Types | 29382 |
| Avg. Fr line length | 77.6 |
| Avg. Bam line length | 61.69 |
| Number of text sources | 264 |

## Data Splits
|       |     |       |
|:-----:|:---:|------:|
| Train | 80% | 37580 |
| Valid | 10% | 4698  |
| Test  | 10% | 4698  |
||

## Remarks

* We are working on resolving some last minute misalignment issues.

### Maintenance

* This dataset is supposed to be actively maintained.

### Benchmarks:

- `Coming soon`

### Sources

- [`sources`](./bayelemabaga/sources.txt)

### To note: 
- ʃ => (sh/shy) sound: Symbol left in the dataset, although not a part of bambara orthography nor French orthography.

## License

- `CC-BY-SA-4.0`

## Version

- `1.0.1`

## Citation

```
@misc{bayelemabagamldataset2022
    title={Machine Learning Dataset Development for Manding Languages},
    author={
        Valentin Vydrin and
        Jean-Jacques Meric and
        Kirill Maslinsky and
        Andrij Rovenchak and
        Allashera Auguste Tapo and
        Sebastien Diarra and
        Christopher Homan and
        Marco Zampieri and
        Michael Leventhal
    },
    howpublished = {url{https://github.com/robotsmali-ai/datasets}},
    year={2022}
}
```

## Contacts
- `sdiarra <at> robotsmali.org`
- `aat3261 <at> rit.edu`
