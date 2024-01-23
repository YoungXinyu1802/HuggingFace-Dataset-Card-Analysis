---
task_categories:
- conditional-text-generation
- paraphrase
- gpt-3
- crowdsourced

---
# MF Rocket Paraphrase Corpus (MFRPC) - A State of the Art Paraphrasing Solution

## Dataset Description

MF Rocket Paraphrase Corpus (MFRPC) ) is a corpus consisting of 10,000 sentence pairs. Each sentence pair contains a source sentence and the paraphrased version of the source sentence. The source sentences are created manually and are intended to represent typical sentences found in online articles. They are limited to general topics and are not restricted to a specific domain. The paraphrased sentences were created partly using GPT-3 and partly manually. In this way, we hope to investigate the performance of GPT-3 in a typical real-world setting and improve the quality of the paraphrased sentences through manual corrections.

By finetuning a model we Pegasus with this data, we create a paraphraser that performs very well. The results are indistinguishable from human parahrased sentences in a blind test. 

We are currently working on a data set with complete paragraphs or articles. 

For more information, our Contact form can be used at https://mf-rocket.de. 

### Languages

The BCP-47 code for the dataset's language is en.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "text": "To overcome these difficulties, you must select an activity or goal that you are enthusiastic about [...]",
    "target": "To overcome these challenges, you need to find an activity or goal that you are passionate about and[...]"
  },
  {
    "text": "If you are unsure about what to do next, seek advice from a close friend or family member you can tr[...]",
    "target": "If you are feeling lost, ask a trusted friend or family member for their opinion about what you shou[...]"
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "text": "Value(dtype='string', id=None)",
  "target": "Value(dtype='string', id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 8000 |
| valid        | 2000 |
