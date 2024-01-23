---
language:
- en
license: creativeml-openrail-m
thumbnail: "https://huggingface.co/datasets/Nerfgun3/ouroboros_embeddings/resolve/main/ouroboros_showcase.jpg"
tags:
- stable-diffusion
- text-to-image
- image-to-image
inference: false
---

# Ouroboros Style Embeddings / Textual Inversion

<img alt="Showcase" src="https://huggingface.co/datasets/Nerfgun3/ouroboros_embeddings/resolve/main/ouroboros_showcase.jpg"/>

## Intro

Both embeddings are quiet similar in style, but were trained on a different dataset.

## Usage

To use my embeddings you have to download the file aswell as drop it into the "\stable-diffusion-webui\embeddings" folder

Personally, I would recommend to use my embeddings with a strength of 0.8, like ```"drawn by (filename:0.8)"```

I trained both embeddings two epochs until 8000 steps.

I hope you enjoy the embedding. If you have any questions, you can ask me anything via Discord: "Nerfgun3#7508"

### Dark ouroboros

This embedding was trained on a dataset with dark backgrounds.

To use it in a prompt: ```"drawn by dark_ouroboros"```

### White ouroboros

This embedding was trained on a dataset with white backgrounds.

To use it in a prompt: ```"drawn by white_ouroboros"```

## License

This embedding is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

1. You can't use the embedding to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the embedding commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)