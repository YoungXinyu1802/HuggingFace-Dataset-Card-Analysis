---
task_categories:
- token-classification
language:
- el
pretty_name: Semantic Domains of the Greek New Testament (Lemmatized)
size_categories:
- 1K<n<10K
---

# Dataset Card for semantic-domains-greek-lemmatized

## Dataset Description

- **Point of Contact:** https://huggingface.co/ryderwishart / https://github.com/ryderwishart

### Dataset Summary

Semantic domains aligned to tokens, broken down by sentences. Tokens have been lemmatized according to data in [Clear-Bible/macula-greek](https://github.com/Clear-Bible/macula-greek).

Domains are based on Louw and Nida's semantic domains for the Greek New Testament.

### Languages

Greek, Hellenistic Greek, Koine Greek, Greek of the New Testament

## Dataset Structure

### Data Instances

```
DatasetDict({
    train: Dataset({
        features: ['tokens', 'tags', 'labels'],
        num_rows: 6408
    })
    test: Dataset({
        features: ['tokens', 'tags', 'labels'],
        num_rows: 801
    })
    eval: Dataset({
        features: ['tokens', 'tags', 'labels'],
        num_rows: 802
    })
})
```

### Data Fields

`tokens`: plaintext words (only split by whitespace); e.g.,

```
['δέ', 'ὁ', 'ἀποκρίνομαι', 'εἷς', 'αὐτός', 'λέγω', 'ἑταῖρος', 'οὐ', 'ἀδικέω', 'σύ', 'οὐχί', 'δηνάριον', 'συμφωνέω', 'ἐγώ']
```

`tags`: integer IDs for each semantic domain (use these for training the model).

`labels`: label strings for each tag; e.g., 

```
['89.124', '92.24', '33.28', '92.22', '92.11', '33.69', '34.16', '69.3', '88.128 88.22', '92.6', '69.12', '6.75', '31.15', '92.1']
```

### Data Splits

Data split into train (75%), test (12.5%), and evaluation (12.5%) splits.

## Dataset Creation

Greek words are based on the Nestle1904 base text, which is in the public domain.

More information about the meanings of the semantic domain labels can be found online [here](https://www.laparola.net/greco/louwnida.php), or by consulting Louw and Nida's Lexicon.

## Considerations for Using the Data

### Social Impact of Dataset

This data may be used to further Christ's kingdom and glorify God.

### Other Known Limitations

Louw and Nida's semantic domains have some known limitations discussed [in this paper](https://academic.oup.com/ijl/article/31/4/394/5070421).