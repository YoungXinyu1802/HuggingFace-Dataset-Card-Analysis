---
annotations_creators:
- machine-generated
language:
- en
- zh
language_creators:
- other
multilinguality:
- multilingual
pretty_name: 'Pokémon BLIP captions'
size_categories:
- 10K
dataset_info:
  features:
  - name: image
    dtype: image
  - name: prompt
    dtype: string
  - name: seed
    dtype: int64
  - name: step
    dtype: int64
  - name: cfg
    dtype: float32
  - name: sampler
    dtype: string
  - name: zh_prompt
    dtype: string
  splits:
  - name: train
    num_bytes: 5826763233.4353
    num_examples: 9841
  download_size: 5829710525
  dataset_size: 5826763233.4353
---
# Dataset Card for "diffusiondb_random_10k_zh_v1"

svjack/diffusiondb_random_10k_zh_v1 is a dataset that random sample 10k English samples from [diffusiondb](https://github.com/poloclub/diffusiondb) and use [NMT](https://en.wikipedia.org/wiki/Neural_machine_translation) translate them into Chinese with some corrections.<br/>

it used to train stable diffusion models in <br/> [svjack/Stable-Diffusion-FineTuned-zh-v0](https://huggingface.co/svjack/Stable-Diffusion-FineTuned-zh-v0)<br/>
[svjack/Stable-Diffusion-FineTuned-zh-v1](https://huggingface.co/svjack/Stable-Diffusion-FineTuned-zh-v1)<br/>
[svjack/Stable-Diffusion-FineTuned-zh-v2](https://huggingface.co/svjack/Stable-Diffusion-FineTuned-zh-v2)<br/>

And is the data support of [https://github.com/svjack/Stable-Diffusion-Chinese-Extend](https://github.com/svjack/Stable-Diffusion-Chinese-Extend) which is a fine tune version of Stable Diffusion model on self-translate 10k diffusiondb Chinese Corpus and "extend" it.


[More Information needed](https://github.com/huggingface/datasets/blob/main/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)