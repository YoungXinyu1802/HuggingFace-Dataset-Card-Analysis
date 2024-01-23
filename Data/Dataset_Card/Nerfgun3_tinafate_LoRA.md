---
language:
- en
license: creativeml-openrail-m
thumbnail: "https://huggingface.co/datasets/Nerfgun3/tinafate_LoRA/resolve/main/preview/preview%20(1).png"
tags:
- stable-diffusion
- text-to-image
- image-to-image
inference: false
---

# TinaFate LoRA

# Use Cases

The LoRA is in itself very compatible with the most diverse model. However, it is most effective when used with Kenshi or AbyssOrangeMix2.

The LoRA itself was trained with the token: ```skistyle```.
I would suggest using the token with AbyssOrangeMix2, but not with Kenshi, since I got better results that way.

The models mentioned right now
1. AbyssOrangeMix2 from [WarriorMama777](https://huggingface.co/WarriorMama777/OrangeMixs)
2. Kenshi Model from [Luna](https://huggingface.co/SweetLuna/Kenshi)

## Strength

I would personally use these strength with the assosiated model:
- 0.6-0.85 for AbyssOrangeMix2
- 0.5-0.75 for Kenshi

# Showcase

**Example 1**

<img alt="Showcase" src="https://huggingface.co/datasets/Nerfgun3/tinafate_LoRA/resolve/main/preview/preview%20(2).png"/>

```
skistyle,
1girl, blonde hair, black hair, navel, long hair, breasts, crop top, smile, large breasts, midriff, pants, red eyes, choker, multicolored hair, white hairband, white background, otoko no ko, japanese clothes, looking at viewer, earrings, sweatdrop, pink nails, denim, blush, simple background, hand on hip, black eyes, blue pants, jewelry, hairband, kimono, tank top, gradient hair, jeans, holding
Steps: 32, Sampler: Euler a, CFG scale: 7
```

**Example 2**
<img alt="Showcase" src="https://huggingface.co/datasets/Nerfgun3/tinafate_LoRA/resolve/main/preview/preview%20(3).png"/>

```
skistyle,
1girl, valkyrie, highly detailed face, feathered wings, wearing ornate viking clothes, horned helmet, (darkness, dark background:1.3), fur trim, holding a short sword with her hand on the handle, a feeling of triumph, (feathers floating around her in a magical vortex:1.15), majestic, imposing beauty, (standing atop the battlements:1.05) a night, (fantasy setting:1.2), dnd, d&d, beautiful 8k wallpaper, superb, extremely detailed, intricate, (artistic brush strokes:1.3)
Steps: 32, Sampler: Euler a, CFG scale: 7
```

**Example 3**
<img alt="Showcase" src="https://huggingface.co/datasets/Nerfgun3/tinafate_LoRA/resolve/main/preview/preview%20(4).png"/>

```
skistyle,
1girl, (green hair:1.1), short hair, pointy ears, wearing a green (tunic:1.2) and shorts, (illustration:1.1), highres, (extremely detailed CG unity 8k wallpaper:1.1), (mid shot:1.1), (full body:1.25), (solo:1.2), plant, tree, (beautiful eyes:1.15), green boots, leaves swirling around the girl, wariza, leaning against tree at night, blue_eyes, (beautiful face:1.15), (((flat background))), (fireflies:1.1), parted lips, highly detailed face, ultra realistic, masterpiece, best quality, the legend of zelda, bokeh, extremely detailed, intricate
Steps: 20, Sampler: DPM++ SDE Karras, CFG scale: 7
```

# License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the embedding commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)