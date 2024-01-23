# Glue STS-B

This dataset is a port of the official [`sts-b` dataset](https://huggingface.co/datasets/glue/viewer/stsb/validation) on the Hub.
This is not a classification task, so the label_text column is only included for consistency 
Note that the sentence1 and sentence2 columns have been renamed to text1 and text2 respectively.
Also, the test split is not labeled; the label column values are always -1.
