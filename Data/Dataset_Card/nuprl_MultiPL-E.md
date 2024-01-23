---
annotations_creators:
- machine-generated
language:
- en
language_creators:
- machine-generated
- expert-generated
license:
- mit
multilinguality:
- monolingual
pretty_name: MultiPLE-E
size_categories:
- 1K<n<10K
source_datasets:
- original
- extended|openai_humaneval
- extended|mbpp
tags: []
task_categories: []
task_ids: []
---

# Dataset Card for MultiPL-E

## Dataset Description

- **Homepage:**  https://nuprl.github.io/MultiPL-E/
- **Repository:**  https://github.com/nuprl/MultiPL-E
- **Paper:** https://arxiv.org/abs/2208.08227
- **Point of Contact:** carolyn.anderson@wellesley.edu, mfeldman@oberlin.edu, a.guha@northeastern.edu

## Dataset Summary

MultiPL-E is a dataset for evaluating large language models for code
generation that supports 18 programming languages. It takes the OpenAI 
"HumanEval" and the MBPP Python benchmarks and uses little compilers to
translate them  to other languages. It is easy to add support for new languages 
and benchmarks.

## Subsets

For most purposes, you should use the variations called *SRCDATA-LANG*, where
*SRCDATA* is either "humaneval" or "mbpp" and *LANG* is one of the supported
languages. We use the canonical file extension for each language to identify
the language, e.g., "py" for Python, "cpp" for C++, "lua" for Lua, and so on.

We also provide a few other variations:

- *SRCDATA-LANG-keep* is the same as *SRCDATA-LANG*, but the text of the prompt
  is totally unchanged. If the original prompt had Python doctests, they remain
  as Python instead of being translated to *LANG*. If the original prompt had 
  Python-specific terminology, e.g., "list", it remains "list", instead of 
  being translated, e.g., to "vector" for C++.

- *SRCDATA-LANG-transform* transforms the doctests to *LANG* but leaves
  the natural language text of the prompt unchanged.

- *SRCDATA-LANG-removed* removes the doctests from the prompt.

Note that MBPP does not have any doctests, so the "removed" and "transform"
variations are not available for MBPP.

## Example

The following script uses the Salesforce/codegen model to generate Lua
and MultiPL-E to produce a script with unit tests for luaunit.

```python
import datasets
from transformers import AutoTokenizer, AutoModelForCausalLM

LANG = "lua"
MODEL_NAME = "Salesforce/codegen-350M-multi"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME).half().cuda()
problems = datasets.load_dataset("nuprl/MultiPL-E", f"humaneval-{LANG}")

def stop_at_stop_token(decoded_string, problem):
    """
    Truncates the output at stop tokens, taking care to skip the prompt
    which may have stop tokens.
    """
    min_stop_index = len(decoded_string)
    for stop_token in problem["stop_tokens"]:
        stop_index = decoded_string.find(stop_token)
        if stop_index != -1 and stop_index > len(problem["prompt"]) and stop_index < min_stop_index:
            min_stop_index = stop_index
    return decoded_string[:min_stop_index]

for problem in problems["test"]:
    input_ids = tokenizer(
        problem["prompt"],
        return_tensors="pt",
    ).input_ids.cuda()
    generated_ids = model.generate(
        input_ids, max_length=512, pad_token_id=tokenizer.eos_token_id + 2
    )
    truncated_string = stop_at_stop_token(tokenizer.decode(generated_ids[0]), problem)
    filename = problem["name"] + "." + LANG
    with open(filename, "w") as f:
        print(f"Created {filename}")
        f.write(truncated_string)
        f.write("\n")
        f.write(problem["tests"])
```