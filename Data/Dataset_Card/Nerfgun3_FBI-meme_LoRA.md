---
language:
- en
license: creativeml-openrail-m
thumbnail: "https://huggingface.co/datasets/Nerfgun3/FBI-meme_LoRA/resolve/main/preview/Preview%20(4).png"
tags:
- stable-diffusion
- text-to-image
- image-to-image
inference: false
---

# FBI Cap Meme LoRA

# Use Cases

The LoRA is in itself very compatible with the most diverse model. However, it is most effective when used with Kenshi or AbyssOrangeMix2.

The LoRA itself was trained with the token: ```skistyle```.
You most likely want to add ```fbi cap, fbi``` to force the cap.

The models mentioned right now
1. AbyssOrangeMix2 from [WarriorMama777](https://huggingface.co/WarriorMama777/OrangeMixs)
2. Kenshi Model from [Luna](https://huggingface.co/SweetLuna/Kenshi)

## Strength

I would personally use these strength with the assosiated model:

- 0.75-0.85 for AbyssOrangeMix2
- 0.65-0.85 for Kenshi

# Showcase

**Example 1**

<img alt="Showcase" src="https://huggingface.co/datasets/Nerfgun3/FBI-meme_LoRA/resolve/main/preview/Preview%20(1).png"/>

```
skistyle, fbi cap, cap,
a girl, short white hair, grey eyes, masterpiece, highest quality
Steps: 32, Sampler: Euler a, CFG scale: 7
```

**Example 2**
<img alt="Showcase" src="https://huggingface.co/datasets/Nerfgun3/FBI-meme_LoRA/resolve/main/preview/Preview%20(2).png"/>

```
skistyle, fbi cap, cap,
1girl, solo, hat, weapon, sunglasses, gun, baseball cap, braid, red hair, long hair, looking at viewer, spot color, white background, simple background, gloves, jacket, upper body, single braid
Steps: 32, Sampler: Euler a, CFG scale: 7
```

**Example 3**
<img alt="Showcase" src="https://huggingface.co/datasets/Nerfgun3/FBI-meme_LoRA/resolve/main/preview/Preview%20(3).png"/>

```
skistyle, fbi cap, fbi,
1girl, solo, highly detailed, masterpiece
Steps: 32, Sampler: Euler a, CFG scale: 7
```

# License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the embedding commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)