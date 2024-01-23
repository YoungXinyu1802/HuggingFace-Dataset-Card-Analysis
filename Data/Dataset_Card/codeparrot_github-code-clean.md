---
license: apache-2.0
---
This is a cleaner version of [Github-code dataset](https://huggingface.co/datasets/codeparrot/github-code), we add the following filters:
* Average line length < 100
* Alpha numeric characters fraction > 0.25
* Remove auto-generated files (keyword search)

3.39M files are removed making up 2.94% of the dataset.