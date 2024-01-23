text to text implementation basing on https://github.com/salesforce/DocNLI

DatasetDict({
    train: Dataset({
        features: ['idx', 'inputs', 'targets'],
        num_rows: 942314
    })
    validation: Dataset({
        features: ['idx', 'inputs', 'targets'],
        num_rows: 234258
    })
    test: Dataset({
        features: ['idx', 'inputs', 'targets'],
        num_rows: 267086
    })
})