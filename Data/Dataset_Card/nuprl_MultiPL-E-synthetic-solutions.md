---
dataset_info:
  features:
  - name: name
    dtype: string
  - name: language
    dtype: string
  - name: prompt
    dtype: string
  - name: solution
    dtype: string
  splits:
  - name: train
    num_bytes: 2185285
    num_examples: 2624
  download_size: 891673
  dataset_size: 2185285
license: openrail
language:
- en
pretty_name: MultiPL-E Synthetic Solutions
---

# Dataset Card

This is a dataset of partial solutions to the HumanEval and MBPP code generation benchmarks tranlated into 18+
programming languages. The original benchmark problems were in Python, and we build the dataset as follows:

1. We translate the prompts into a new language using MultiPL-E;
2. We use code-davinci-002 to generate 200 completions for each problem at temperature 0.8;
3. We select a working solution (if one exists) for each problem-language pair.

[This notebook](https://github.com/nuprl/MultiPL-E/blob/main/notebooks/build_synthetic_solutions_dataset.ipynb)
carried out the steps described above.

Note that the dataset does  *not* have solutions for every problem-language pair, since code-davinci-002 cannot
produce a correct solution to every problem.