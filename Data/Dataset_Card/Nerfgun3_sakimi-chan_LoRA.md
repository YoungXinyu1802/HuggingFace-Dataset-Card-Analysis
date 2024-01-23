---
language:
- en
license: creativeml-openrail-m
thumbnail: "https://huggingface.co/datasets/Nerfgun3/sakimi-chan_LoRA/resolve/main/preview/Preview.png"
tags:
- stable-diffusion
- text-to-image
- image-to-image
inference: false
---

# Sakimi-chan LoRA

## Who is Sakimi-chan?

Sakimi-chan is a Canadian artist best known for her digital paintings and unique style. She mainly draws fanart of games and popular characters and creates gifs for her fans with voiceovers.
Patreon: https://www.patreon.com/sakimichan

# Use Cases

The LoRA is in itself very compatible with the most diverse model. However, it is most effective when used with Kenshi or AbyssOrangeMix2.

The LoRA itself was trained with the token: ```skistyle```.
I would suggest using the token with AbyssOrangeMix2, but not with Kenshi, since I got better results that way.

The model mentioned right now
1. AbyssOrangeMix2 from [WarriorMama777](https://huggingface.co/WarriorMama777/OrangeMixs)
2. Kenshi Model from [Luna](https://huggingface.co/SweetLuna/Kenshi)

## Strength

I would personally use these strength with the assosiated model:
- 0.8-0.85 for AbyssOrangeMix2
- 0.65-0.75 for Kenshi

# Showcase

**Example 1**

<img alt="Showcase" src="https://huggingface.co/datasets/Nerfgun3/sakimi-chan_LoRA/resolve/main/preview/Preview%20(1).png"/>

```
skistyle,
1girl, solo, blonde hair, armor, gauntlets, ahoge, green eyes, armored dress, ribbon, puffy sleeves, dress, braid, hair ribbon, looking at viewer, weapon, long sleeves, juliet sleeves, sword, blue ribbon, lips, sidelocks, hair bun, hand on hilt, excalibur (fate/stay night), breastplate, bangs
Steps: 32, Sampler: Euler a, CFG scale: 7
```

**Example 2**
<img alt="Showcase" src="https://huggingface.co/datasets/Nerfgun3/sakimi-chan_LoRA/resolve/main/preview/Preview%20(2).png"/>

```
skistyle,
1girl, best quality, (masterpiece:1.3), (white eyelashes:1.2), (albino:1.2), [black eyeshadow], bangs, closed mouth, cowboy shot, dress shirt, hair between eyes, long hair, looking at viewer, red eyes, shirt, simple background, sleeves past wrists, white hair, white shirt, wing collar, black skirt, (upper body:1.3), (highly detailed face:1.3)
Steps: 32, Sampler: Euler a, CFG scale: 7
```

**Example 3**
<img alt="Showcase" src="https://huggingface.co/datasets/Nerfgun3/sakimi-chan_LoRA/resolve/main/preview/Preview%20(3).png"/>

```
skistyle,
(extremely detailed CG unity 8k wallpaper), (ultra-detailed), masterpiece, best quality, raiden shogun, 1girl, breasts, solo
Steps: 20, Sampler: DPM++ SDE Karras, CFG scale: 7
```

**Example 4**
<img alt="Showcase" src="https://huggingface.co/datasets/Nerfgun3/sakimi-chan_LoRA/resolve/main/preview/Preview%20(4).png"/>

```
1girl, solo, long hair, blue eyes, small breasts, hair over one eye, breast curtain, looking at viewer, braid, blush, shoulder cutout, hair ornament, large breasts, smile, upper body, tassel, parted lips, white hair, clothing cutout, bodysuit, braided ponytail, bangs, bare shoulders, eyes visible through hair, gold trim, earrings, jewelry, very long hair, white background, (masterpiece:1.2), ((best quality)), (ultra-detailed)
Steps: 20, Sampler: DPM++ SDE Karras, CFG scale: 7
```

# License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the embedding commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)