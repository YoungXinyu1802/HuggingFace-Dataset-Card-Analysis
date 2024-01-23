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
A small subset  of [the-stack](https://huggingface.co/datasets/bigcode/the-stack) dataset, with 87 programming languages, each  has 10,000 random samples from the original dataset. 


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
```python
# to load go:
from datasets import load_dataset

load_dataset("bigcode/the-stack-smol-xl", data_dir="data/go")
```
