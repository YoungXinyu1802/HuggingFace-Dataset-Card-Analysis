
## Dataset Summary

Scotch is a dataset of about 19 million functions collected from open-source repositiories from GitHub with permissive licenses. Each function has its corresponding code context and about 4 million functions have corresponding docstrings.

### Languages
The dataset includes functions written in programming languages Python, Java, Javascript, and Go.

## Statistics

### Split
The functions with docstrings is splitted into train, valid, and test set of 3200626, 400077, 400080 functions respectively.

## Features

Each function consists of following features:

* repository_name: Name of the repository the function belongs to.
* function_path: Path of the function within the repository.
* function_identifier: Function name/identifier.
* language: Programming language the function is written in.
* function: Function string.
* docstring: Function docstring.
* function_url: URL to the function code.
* context: Code context.
* license: License info of the repository (includes only repositories with permissive licenses).

## Data Collection

The dataset is collected from GitHub repositories of respective languages with 5 or more stars. Such repositories are listed using [SEART](https://seart-ghs.si.usi.ch/). Functions are parsed using a lightweight parser build on top of function parser from [CodeSearchNet dataset](https://github.com/github/CodeSearchNet/tree/master/function_parser) and repositories were collected with help of [github-downloader from EleutherAI](https://github.com/EleutherAI/github-downloader).

### Data Processing
All the code without permissive licenses are removed and deduplication is performed on the remaining set of functions. Afterwards, all the functions with single line of code, whose docstring contains non-English characters are removed. Files with multiple same functions are excluded. This results in about 19M functions. To obtain a dataset of NL-Code pairs, functions with no docstrings or doctrings less than 3 tokens separated by white-space are excluded. Following CodeSearchNet, functions with 'test' keyword in their name are excluded.

## License

This dataset is under MIT License. However, the repositories the functions are collected from may have several permissive licenses. Those licenses include MIT License, Apache License 2.0, BSD 3-Clause “New” or “Revised” License, BSD 2-Clause “Simplified” License, and ISC License.