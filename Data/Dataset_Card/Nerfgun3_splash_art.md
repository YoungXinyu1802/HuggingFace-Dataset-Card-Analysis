---
language:
- en
license: creativeml-openrail-m
thumbnail: "https://huggingface.co/datasets/Nerfgun3/splash_art/resolve/main/splashart.jpg"
tags:
- stable-diffusion
- text-to-image
- image-to-image
inference: false
---

# Splash Art Style Embedding / Textual Inversion

<img alt="Showcase" src="https://huggingface.co/datasets/Nerfgun3/splash_art/resolve/main/splashart.jpg"/>

## Usage

I uploaded two different versions. Both embeddings create splash art images, although the splash_art2 is more consistent, splash_art generates more generic images than splash_art2. Enjoy! 

To use this embedding you have to download the file aswell as drop it into the "\stable-diffusion-webui\embeddings" folder

To use it in a prompt: ```"splash_art"``` or ```"splash_art2"``` depending on which version you use

Personally, I would recommend to use my embeddings with a strength of 0.8, like ```"(splash_art:0.8)"``` or ```"(splash_art2:0.8)"```

I trained the embedding two epochs until 6800 steps.

I hope you enjoy the embedding. If you have any questions, you can ask me anything via Discord: "Nerfgun3#7508"

## License

This embedding is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

1. You can't use the embedding to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the embedding commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)