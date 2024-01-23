# GEM References

## What is it?

This repository contains all the reference datasets that are used for running evaluation on the GEM benchmark. Some of these datasets were originally hosted as a [GitHub release](https://github.com/GEM-benchmark/GEM-metrics/releases) on the [`GEM-metrics`](https://github.com/GEM-benchmark/GEM-metrics) repository, but have been migrated to the Hugging Face Hub.

## Converting datasets to JSON

We provide a `convert_dataset_to_json.py` conversion script that converts the datasets in the GEM organisation to the JSON format expected by the `GEM-metrics` library. To run the script, first install [`jq`](https://stedolan.github.io/jq/download/) and then install the script's Python dependencies:

```
python -m pip install -r requirements.txt
```

You can then run the script as follows:

```python
python generate_evaluation_datasets.py
```

This script will:

* Download and convert the datasets under the GEM organisation to JSON format
* Validate that the each dataset has the expected columns of `gem_id`, `target`, and `references`

