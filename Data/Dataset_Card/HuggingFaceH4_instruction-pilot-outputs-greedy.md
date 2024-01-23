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
    - name: output
      dtype: string
  splits:
  - name: train
    num_bytes: 243208
    num_examples: 375
  download_size: 100726
  dataset_size: 243208
---
# Dataset Card for "instruction-pilot-outputs-greedy"

This dataset contains model outputs generated from the human demonstrations provided in [`HuggingFaceH4/instruction-pilot-prompts`](https://huggingface.co/datasets/HuggingFaceH4/instruction-pilot-prompts). 

To convert each language model into a dialogue agent, we prepended the following [LangChain prompt](https://github.com/hwchase17/langchain/blob/bfabd1d5c0bf536fdd1e743e4db8341e7dfe82a9/langchain/chains/conversation/prompt.py#LL4C21-L9C7) to each input:

```
The following is a friendly conversation between a human and an AI. \
The AI is talkative and provides lots of specific details from its context. \
If the AI does not know the answer to a question, it truthfully says it does not know.

Human: {input}
AI:
```

For reproducibility purposes, we used deterministic text generation (`temperature=0`) and set `max_new_tokens=100` (which is about the mean lenght of the Self-Instruct outputs).