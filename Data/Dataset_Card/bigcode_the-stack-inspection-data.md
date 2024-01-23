---
annotations_creators: []
language_creators:
- crowdsourced
language: ["code"]
multilinguality:
- multilingual
size_categories:
- unknown
source_datasets: []
task_categories:
- text-generation
task_ids:
- language-modeling
---

## Dataset Description
A subset  of [the-stack](https://huggingface.co/datasets/bigcode/the-stack) dataset, from 87 programming languages, and 295 extensions. 
Each language is in a separate folder under `data/` and contains folders of its extensions. We select samples from 20,000 random files of the original dataset, and keep a 
maximum of 1,000 files per extension.

Check this [space](https://huggingface.co/spaces/bigcode/the-stack-inspection) for inspecting this dataset.


## Languages

The dataset contains 87 programming languages:
````
'ada', 'agda', 'alloy', 'antlr', 'applescript', 'assembly', 'augeas', 'awk', 'batchfile', 'bison', 'bluespec', 'c',
'c++', 'c-sharp', 'clojure', 'cmake', 'coffeescript', 'common-lisp', 'css', 'cuda', 'dart', 'dockerfile', 'elixir',
'elm', 'emacs-lisp','erlang', 'f-sharp', 'fortran', 'glsl', 'go', 'groovy', 'haskell','html', 'idris', 'isabelle', 'java', 
'java-server-pages', 'javascript', 'julia', 'kotlin', 'lean', 'literate-agda', 'literate-coffeescript', 'literate-haskell',
 'lua', 'makefile', 'maple', 'markdown', 'mathematica', 'matlab', 'ocaml', 'pascal', 'perl', 'php', 'powershell', 'prolog',
  'protocol-buffer', 'python', 'r', 'racket', 'restructuredtext', 'rmarkdown', 'ruby', 'rust', 'sas', 'scala', 'scheme', 
  'shell', 'smalltalk', 'solidity', 'sparql', 'sql', 'stan', 'standard-ml', 'stata', 'systemverilog', 'tcl', 'tcsh', 'tex', 
  'thrift', 'typescript', 'verilog', 'vhdl', 'visual-basic', 'xslt', 'yacc', 'zig'
`````
## Dataset Structure
You can specify which language and extension you want to load:
```python
# to load py extension of python
from datasets import load_dataset

load_dataset("bigcode/the-stack-inspection-data", data_dir="data/python/py")

DatasetDict({
    train: Dataset({
        features: ['content', 'lang', 'size', 'ext', 'max_stars_count', 'avg_line_length', 'max_line_length', 'alphanum_fraction'],
        num_rows: 1000
    })
})
```
