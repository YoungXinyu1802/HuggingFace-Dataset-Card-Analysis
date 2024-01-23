---
language:
- en
license: creativeml-openrail-m
thumbnail: "https://huggingface.co/datasets/Nerfgun3/Liang_Xing_LoRA/resolve/main/preview/preview%20(2).png"
tags:
- stable-diffusion
- text-to-image
- image-to-image
inference: false
---

# Liang Xing Artstyle LoRA

# Use Cases

The LoRA is in itself very compatible with the most diverse model. However, it is most effective when used with Kenshi or AbyssOrangeMix2.

The LoRA itself was trained with the token: ```skistyle```.

The model mentioned right now
1. AbyssOrangeMix2 from [WarriorMama777](https://huggingface.co/WarriorMama777/OrangeMixs)
2. Kenshi Model from [Luna](https://huggingface.co/SweetLuna/Kenshi)

## Strength

I would personally use these strength with the assosiated model:
- 0.8-1 for AbyssOrangeMix2
- 0.7-0.85 for Kenshi

# Showcase

**Example 1**

<img alt="Showcase" src="https://huggingface.co/datasets/Nerfgun3/Liang_Xing_LoRA/resolve/main/preview/preview%20(3).png"/>

```
skistyle,
miku hatsune, masterpiece, best quality, 1girl, blush, aqua eyes, cap, closed mouth, earrings, hat, hoop earrings, jewelry, looking at viewer, shirt, simple background, solo, upper body, yellow shirt
Steps: 32, Sampler: Euler a, CFG scale: 7
```

**Example 2**
<img alt="Showcase" src="https://huggingface.co/datasets/Nerfgun3/Liang_Xing_LoRA/resolve/main/preview/preview%20(1).png"/>

```
skistyle,
multiple girls, 7girls, ((maid outfits)), fully clothed, (small breasts:1.2), witch hat, eyepatch, twintails, long hair, hat, hair ornament, blonde hair, black hair, gloves, white hair, looking at viewer, red eyes, sky, elbow gloves, from below, sfw, black gloves, thighs, hairpin, brown hair, hair stick, purple headwear
Steps: 32, Sampler: Euler a, CFG scale: 7
```

**Example 3**
<img alt="Showcase" src="https://huggingface.co/datasets/Nerfgun3/Liang_Xing_LoRA/resolve/main/preview/preview%20(4).png"/>

```
skistyle,
kaya izumi, masterpiece, best quality, 1girl, blush, aqua eyes, cap, blonde hair, closed mouth, earrings, green background, hat, hoop earrings, jewelry, looking at viewer, shirt, short hair, simple background, solo, upper body, yellow shirt
Steps: 20, Sampler: DPM++ SDE Karras, CFG scale: 7
```

# License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the embedding commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)