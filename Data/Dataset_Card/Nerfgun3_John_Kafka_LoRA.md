---
language:
- en
license: creativeml-openrail-m
thumbnail: "https://huggingface.co/datasets/Nerfgun3/John_Kafka_LoRA/resolve/main/preview/preview%20(1).png"
tags:
- stable-diffusion
- text-to-image
- image-to-image
inference: false
---

# John Kafka Artstyle LoRA

# Use Cases

The LoRA is in itself very compatible with the most diverse model. However, it is most effective when used with Kenshi or AbyssOrangeMix2.

The LoRA itself was trained with the token: ```skistyle```.

The models mentioned right now
1. AbyssOrangeMix2 from [WarriorMama777](https://huggingface.co/WarriorMama777/OrangeMixs)
2. Kenshi Model from [Luna](https://huggingface.co/SweetLuna/Kenshi)

## Strength

I would personally use these strength with the assosiated model:

Soft-Version:
- 0.85-1 for AbyssOrangeMix2
- 0.75-0.9 for Kenshi

Hard-Version:
- 0.6-0.8 for AbyssOrangeMix2
- 0.55-0.75 for Kenshi

# Showcase

**Example 1**

<img alt="Showcase" src="https://huggingface.co/datasets/Nerfgun3/John_Kafka_LoRA/resolve/main/preview/preview%20(2).png"/>

```
skistyle,
1girl, small cute red nose, animal_ears, artist_name, bangs, some freckles, black_hair, black_skirt, blue_ribbon, smiling, solo, looking at viewer, collared_shirt, flower, fox_ears, grey_flower, hair_flower, hair_ornament, highres, league_of_legends, long_hair, looking_at_viewer, neck_ribbon, orange_eyes, pleated_skirt, ribbon, shirt, sitting, skirt, solo, white_shirt, shy
Steps: 32, Sampler: Euler a, CFG scale: 7
```

**Example 2**
<img alt="Showcase" src="https://huggingface.co/datasets/Nerfgun3/John_Kafka_LoRA/resolve/main/preview/preview%20(3).png"/>

```
skistyle,
1girl, small cute red nose, animal_ears, artist_name, bangs, some freckles, black_hair, black_skirt, blue_ribbon, smiling, solo, looking at viewer, collared_shirt, flower, fox_ears, grey_flower, hair_flower, hair_ornament, highres, league_of_legends, long_hair, looking_at_viewer, neck_ribbon, orange_eyes, pleated_skirt, ribbon, shirt, sitting, skirt, solo, white_shirt, shy
Steps: 32, Sampler: Euler a, CFG scale: 7
```

**Example 3**
<img alt="Showcase" src="https://huggingface.co/datasets/Nerfgun3/John_Kafka_LoRA/resolve/main/preview/preview%20(4).png"/>

```
skistyle,
1girl, (masterpiece:1.2), (highly detailed), ((best quality)), (ultra-detailed)
Steps: 32, Sampler: Euler a, CFG scale: 7
```

# License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the embedding commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)