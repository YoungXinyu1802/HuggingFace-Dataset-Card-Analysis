---
language:
  - English

license: "Apache License 2.0"
---
# Dataset Summary
The repo provides answer,title and sentence expansions for the Natural Questions corpus with gar-T5.

# Dataset Structure
There are dev and test folds

An example data entry of the dev split looks as follows:
```
{
    "id": "1", 
    "predicted_answers": ["312"], "predicted_titles": ["Invisible Man"], "predicted_sentences": ["The Invisible Man First edition Author Ralph Ellison Cover artist M."]
}
```

An example data entry of the test split looks as follows:
```
{
    "id": "1", 
    "predicted_answers": ["May 18 , 2018"], "predicted_titles": ["Deadpool 2 *** Deadpool (film) *** Deadpool 2 (soundtrack) *** X-Men in other media"], "predicted_sentences": ["Deadpool 2 was released on May 18 , 2018 , with Leitch directing from a screenplay by Rhett Reese and Paul Wernick ."]
}
```

# Load Dataset
An example to load the dataset:
```python
data_files = {"dev":"dev/dev.jsonl", "test": "test/test.jsonl"}
dataset = load_dataset('castorini/nq_gar-t5_expansions')
```
