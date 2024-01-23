---
language:
  - English

license: "Apache License 2.0"
---
# Dataset Summary
The repo provides answer,title and sentence expansions for the Trivia QA corpus with gar-T5.

# Dataset Structure
There are dev and test folds

An example data entry of the dev split looks as follows:
```
{
    "id": "1", 
    "predicted_answers": ["Bz"], "predicted_titles": ["Vehicle registration plates of Belize *** Vehicle registration plate"], "predicted_sentences": ["The international code for Belize is \"\"BZ\"\"."]
}
```

An example data entry of the test split looks as follows:
```
{
    "id": "1", 
    "predicted_answers": ["Taurus"], "predicted_titles": ["Jamie Lee Curtis *** Under the Tuscan Sun *** Angels (Jamie Lee Curtis song) *** Under the Tuscan Sun (film) *** John Michael King *** Robert Earl *** Henry Jones, Sr. *** Jamie Lee (singer) *** Under the Tuscan Sun (1974 film) *** Richard Benjamin"], "predicted_sentences": ["In July 2007, several news outlets reported that the couple had quietly married in December 2007, and that Curtis had taken a liking to one another, sharing \"\"sweet nothings\"\" about their relationship."]
}
```

# Load Dataset
An example to load the dataset:
```python
data_files = {"dev":"dev/dev.jsonl", "test": "test/test.jsonl"}
dataset = load_dataset('castorini/triviaqa_gar-t5_expansions')
```
