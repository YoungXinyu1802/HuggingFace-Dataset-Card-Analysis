# CodeParrot 🦜 Dataset Cleaned and filtered (train)

## Dataset Description

A dataset of Python files from Github. It is a more filtered version of the train split [codeparrot-clean-train](https://huggingface.co/datasets/codeparrot/codeparrot-clean-train) of [codeparrot-clean](https://huggingface.co/datasets/codeparrot/codeparrot-clean#codeparrot-%F0%9F%A6%9C-dataset-cleaned). The additional filters aim at detecting configuration and test files, as well as outlier files that are unlikely to help the model learn code. The first three filters are applied with a probability of 0.7:

- files with a mention of "test file" or "configuration file" or similar in the first 5 lines
- files with high occurence of the keywords "test " or "config" 
- files without a mention of the keywords `def`, `for`, `while`  and `class`
- files that use the assignment operator ```=``` less than 5 times 
- files with ratio between number of characters and number of tokens after tokenization < 1.5 

