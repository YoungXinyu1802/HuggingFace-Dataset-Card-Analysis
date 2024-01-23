
---
tags:
- langchain
- prompt
---

# Description of LLM Bash

Prompt designed to convert natural language to bash command.



## Inputs

This is a description of the inputs that the prompt expects.

question: User question to be answered by writing a bash command.



## Usage

Below is a code snippet for how to use the prompt.

```
from langchain.prompts import load_prompt
from langchain.chains import LLMBashChain

llm = ...
prompt = load_prompt('lc://prompts/llm_bash/<file-name>')
chain = LLMBashChain(llm=llm, prompt=prompt)
```

