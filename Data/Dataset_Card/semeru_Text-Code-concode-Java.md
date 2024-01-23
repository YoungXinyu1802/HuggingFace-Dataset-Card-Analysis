---
license: mit
---
## Dataset is imported from CodeXGLUE and pre-processed using their script.

# Where to find in Semeru:
The dataset can be found at /nfs/semeru/semeru_datasets/code_xglue/text-to-code/concode in Semeru
 

# CodeXGLUE -- Text2Code Generation

Here are the dataset and pipeline for text-to-code generation task.

## Task Definition

Generate source code of class member functions in Java, given natural language description and class environment. Class environment is the programmatic context provided by the rest of the class, including other member variables and member functions in class. Models are evaluated by exact match and BLEU.

It's a challenging task because the desired code can vary greatly depending on the functionality the class provides. Models must (a) have a deep understanding of NL description and map the NL to environment variables, library API calls and user-defined methods in the class, and (b) decide on the structure of the resulting code.


## Dataset

### Concode dataset
We use concode dataset which is a widely used code generation dataset from Iyer's EMNLP 2018 paper [Mapping Language to Code in Programmatic Context](https://www.aclweb.org/anthology/D18-1192.pdf).

We have downloaded his published dataset and followed his preprocessed script. You can find the preprocessed data in `dataset/concode` directory.

Data statistics of concode dataset are shown in the below table:

|         |  #Examples  |
| ------- | :---------: |
|  Train  |   100,000   |
|   Dev   |    2,000    |
|  Test   |    2,000    |

### Data Format

Code corpus are saved in json lines format files. one line is a json object:
```
{
  "nl": "Increment this vector in this place. con_elem_sep double[] vecElement con_elem_sep double[] weights con_func_sep void add(double)",
  "code": "public void inc ( ) { this . add ( 1 ) ; }"
}
```

`nl` combines natural language description and class environment. Elements in class environment are seperated by special tokens like `con_elem_sep` and `con_func_sep`.


## Reference


<pre><code>@article{iyer2018mapping,
  title={Mapping language to code in programmatic context},
  author={Iyer, Srinivasan and Konstas, Ioannis and Cheung, Alvin and Zettlemoyer, Luke},
  journal={arXiv preprint arXiv:1808.09588},
  year={2018}
}</code></pre>
