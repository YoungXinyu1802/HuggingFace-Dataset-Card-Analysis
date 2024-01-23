---
dataset_info:
  features:
  - name: INSTRUCTION
    dtype: string
  - name: RESPONSE
    dtype: string
  - name: SOURCE
    dtype: string
  splits:
  - name: train
    num_bytes: 4804916
    num_examples: 8792
  download_size: 2554896
  dataset_size: 4804916
---
# Dataset Card for grade-school-math-instructions

OpenAI's [grade-school-math](https://github.com/openai/grade-school-math) dataset converted into instructions.

## Citation Information
```bibtex
@article{cobbe2021gsm8k,
  title={Training Verifiers to Solve Math Word Problems},
  author={Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},
  journal={arXiv preprint arXiv:2110.14168},
  year={2021}
}
```