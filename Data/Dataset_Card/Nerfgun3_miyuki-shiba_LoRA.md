---
language:
- en
license: creativeml-openrail-m
thumbnail: "https://huggingface.co/datasets/Nerfgun3/miyuki-shiba_LoRA/resolve/main/preview/preview%20(1).png"
tags:
- stable-diffusion
- text-to-image
- image-to-image
inference: false
---

# Miyuki Character LoRA

# Use Cases

The LoRA is in itself very compatible with the most diverse model. However, it is most effective when used with Kenshi or AbyssOrangeMix2.

The LoRA itself was trained with the token: ```miyuki```.
I would suggest using the token with AbyssOrangeMix2, but not with Kenshi, since I got better results that way.

The models mentioned right now
1. AbyssOrangeMix2 from [WarriorMama777](https://huggingface.co/WarriorMama777/OrangeMixs)
2. Kenshi Model from [Luna](https://huggingface.co/SweetLuna/Kenshi)

## Strength

I would personally use these strength with the assosiated model:
- 0.6-0.75 for AbyssOrangeMix2
- 0.4-0.65 for Kenshi

# Showcase

**Example 1**

<img alt="Showcase" src="https://huggingface.co/datasets/Nerfgun3/miyuki-shiba_LoRA/resolve/main/preview/preview%20(2).png"/>

```
miyuki,
1girl, (masterpiece:1.2), (best quality:1.2), (sharp detail:1.2), (highres:1.2), (in a graden of flowers), sitting, waving
Steps: 32, Sampler: Euler a, CFG scale: 7
```

**Example 2**
<img alt="Showcase" src="https://huggingface.co/datasets/Nerfgun3/miyuki-shiba_LoRA/resolve/main/preview/preview%20(3).png"/>

```
miyuki, 1girl, (masterpiece:1.2), (best quality:1.2), (sharp detail:1.2), (highres:1.2), (in a graden of flowers), sitting, waving
Steps: 32, Sampler: Euler a, CFG scale: 7
```

**Example 3**
<img alt="Showcase" src="https://huggingface.co/datasets/Nerfgun3/miyuki-shiba_LoRA/resolve/main/preview/preview%20(4).png"/>

```
miyuki, 1girl, (masterpiece:1.2), (best quality:1.2), (sharp detail:1.2), (highres:1.2), (in a graden of flowers), sitting, hands behind her back
Steps: 20, Sampler: DPM++ SDE Karras, CFG scale: 7
```

# License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the embedding commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)