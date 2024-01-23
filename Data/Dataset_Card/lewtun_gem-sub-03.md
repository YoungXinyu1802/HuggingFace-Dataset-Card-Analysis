---
benchmark: gem
type: prediction
submission_name: T5-base (Baseline)
---

# GEM submissions for gem-sub-03

## Submitting to the benchmark

FILL ME IN

### Submission file format

Please follow this format for your `submission.json` file:

```json
{
  "submission_name": "An identifying name of your system",
  "param_count": 123, # the number of parameters your system has.
  "description": "An optional brief description of the system that will be shown on the website",
  "tasks":
    {
      "dataset_identifier": {
        "values": ["output1", "output2", "..."], # A list of system outputs
        # Optionally, you can add the keys which are part of an example to ensure that there is no shuffling mistakes.
        "keys": ["key-0", "key-1", ...]
        }
    }
}
```

In this case, `dataset_identifier` is the identifier of the dataset followed by an identifier of the set the outputs were created from, for example `_validation` or `_test`. That means, the `mlsum_de` test set would have the identifier `mlsum_de_test`.

The `keys` field can be set to avoid accidental shuffling to impact your metrics. Simply add a list of the `gem_id` for each output example in the same order as your values.

### Validate your submission

To ensure that your submission files are correctly formatted, run the following command from the root of the repository:

```
python cli.py validate
```

If everything is correct, you should see the following message:

```
All submission files validated! ✨ 🚀 ✨
Now you can make a submission 🤗
```

### Push your submission to the Hugging Face Hub!

The final step is to commit your files and push them to the Hub:

```
python cli.py submit
```

If there are no errors, you should see the following message:

```
Submission successful! 🎉 🥳 🎉
Your submission will be evaulated on Sunday 05 September 2021 ⏳
```

where the evaluation is run every Sunday and your results will be visible on the leaderboard.