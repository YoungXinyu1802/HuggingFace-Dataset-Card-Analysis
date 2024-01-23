Dataset for API: https://github.com/eleldar/Translation

Test English-Russian dataset:
```
DatasetDict({
    normal: Dataset({
        features: ['en', 'ru'],
        num_rows: 2009
    })
    short: Dataset({
        features: ['en', 'ru'],
        num_rows: 2664
    })
    train: Dataset({
        features: ['en', 'ru'],
        num_rows: 1660
    })
    validation: Dataset({
        features: ['en', 'ru'],
        num_rows: 208
    })
    test: Dataset({
        features: ['en', 'ru'],
        num_rows: 4170
    })
})
```
The dataset get from tables:
* https://github.com/eleldar/Translator/blob/master/test_dataset/flores101_dataset/101_languages.xlsx?raw=true
* https://github.com/eleldar/Translator/blob/master/test_dataset/normal.xlsx?raw=true
* https://github.com/eleldar/Translator/blob/master/test_dataset/corrected_vocab.xlsx?raw=true