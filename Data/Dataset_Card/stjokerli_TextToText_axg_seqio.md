# text-to-text format from superglue axg

# Note that RTE train and val set has been added

axg: DatasetDict({
        test: Dataset({
            features: ['idx', 'inputs', 'targets'],
            num_rows: 356
        })
        train: Dataset({
            features: ['idx', 'inputs', 'targets'],
            num_rows: 2490
        })
        validation: Dataset({
            features: ['idx', 'inputs', 'targets'],
            num_rows: 277
        })
    })