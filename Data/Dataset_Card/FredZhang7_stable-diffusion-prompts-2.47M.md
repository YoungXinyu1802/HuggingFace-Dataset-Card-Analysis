---
license: creativeml-openrail-m
task_categories:
- text-generation
language:
- en
pretty_name: SDP-2.47M
size_categories:
- 1M<n<10M
---

## Source

Combined text-only dataset from
- poloclub/diffusiondb
- Gustavosta/Stable-Diffusion-Prompts
- bartman081523/stable-diffusion-discord-prompts
- FredZhang7/krea-ai-prompts

For preprocessing methods, please see [Fast GPT2 PromptGen](https://huggingface.co/FredZhang7/distilgpt2-stable-diffusion-v2).


## Python

Download and save the dataset to `all_prompts.txt` locally.
```bash
pip install datasets
```
```python
import datasets

dataset = datasets.load_dataset("FredZhang7/stable-diffusion-prompts-2.47M")

train = dataset["train"]
prompts = train["text"]

with open("all_prompts.txt", "w") as f:
    for prompt in prompts:
        f.write(prompt + "\n")
```