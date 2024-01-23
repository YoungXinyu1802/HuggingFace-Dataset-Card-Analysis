---
dataset_info:
  features:
  - name: id
    dtype: int64
  - name: source
    dtype: string
  - name: prompt
    dtype: string
  - name: outputs
    list:
    - name: model
      dtype: string
    - name: outputs
      sequence: string
  splits:
  - name: train
    num_bytes: 1347447
    num_examples: 375
  download_size: 430865
  dataset_size: 1347447
---
# Dataset Card for "instruction-pilot-outputs-sampling"

This dataset contains model outputs generated from the human demonstrations provided in [`HuggingFaceH4/instruction-pilot-prompts`](https://huggingface.co/datasets/HuggingFaceH4/instruction-pilot-prompts). 

To convert each language model into a dialogue agent, we shortened [Anthropic's HHH prompt](https://gist.github.com/jareddk/2509330f8ef3d787fc5aaac67aab5f11/#file-hhh_prompt-txt) and prepended this to each sample provided to the models:

```
Below is a friendly conversation between a human and an AI assistant. \
The AI tries to be helpful, polite, honest, sophisticated, emotionally aware, and humble-but-knowledgeable. \
The assistant is happy to help with almost anything, and will do its best to understand exactly what is needed. \
It also tries to avoid giving false or misleading information, and it caveats when it isn’t entirely sure about the right answer. \
That said, the assistant is practical and really does its best, and doesn’t let caution get too much in the way of being useful.

Human: {input}
AI:
```

The reason to shorten the HHH prompt is because it is over 6,000 tokens long, which far exceeds the maximum context size of most open-source language models. For example, Flan-T5 only has a context window of 512 tokens. It is likely that better outputs could be produced for language models with larger context windows, where some dialogue examples can be included in the promopt.

To generate diverse outputs from each models, we used nucleus sampling with `temperature=0` and `top_p=0.9` and set `max_new_tokens=100` (which is about the mean lenght of the Self-Instruct outputs). For each example, 8 generations were produced per model.