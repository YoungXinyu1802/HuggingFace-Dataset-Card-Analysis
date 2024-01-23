---
language:
- en

---
# Dataset for project: eurekaqa

This dataset has been trained for project eurekaQA.

### Languages

The BCP-47 code for the dataset's language is en.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "context": "Colquhoun's utilitarian approach to the problem \u2013 using a cost-benefit argument to obtain support from businesses standing to benefit \u2013 allowed him to achieve what Henry and John Fielding failed for their Bow Street detectives. Unlike the stipendiary system at Bow Street, the river police were full-time, salaried officers prohibited from taking private fees. His other contribution was the concept of preventive policing; his police were to act as a highly visible deterrent to crime by their permanent presence on the Thames. Colquhoun's innovations were a critical development leading up to Robert Peel's \"new\" police three decades later.",
    "question": "How did the Thames River Police pay their employees?",
    "answers.text": [
      "full-time, salaried officers prohibited from taking private fees"
    ],
    "answers.answer_start": [
      295
    ]
  },
  {
    "context": "The small woolen dolls called Maniae, hung on the Compitalia shrines, were thought a symbolic replacement for child-sacrifice to Mania, as Mother of the Lares. The Junii took credit for its abolition by their ancestor L. Junius Brutus, traditionally Rome's Republican founder and first consul. Political or military executions were sometimes conducted in such a way that they evoked human sacrifice, whether deliberately or in the perception of witnesses; Marcus Marius Gratidianus was a gruesome example.",
    "question": "Who was Mania in Roman religion?",
    "answers.text": [
      "Mother of the Lares"
    ],
    "answers.answer_start": [
      139
    ]
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "context": "Value(dtype='string', id=None)",
  "question": "Value(dtype='string', id=None)",
  "answers.text": "Sequence(feature=Value(dtype='string', id=None), length=-1, id=None)",
  "answers.answer_start": "Sequence(feature=Value(dtype='int32', id=None), length=-1, id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 8996 |
| valid        | 998 |
