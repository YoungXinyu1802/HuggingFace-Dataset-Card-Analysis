---
license: creativeml-openrail-m
tags:
- stable-diffusion
- embedding
- text-to-image
- image-to-image
- art
- artistic
---

# Princess Jai Lee Embedding

Fine-tuned textual inversion based on a character from [3ee Games](https://3ee.com), Princess Jai Lee.

![Detailed Samples](https://huggingface.co/datasets/zuleo/princess-jai-lee/resolve/main/princess.png)

## Embedding Usage

Use the token ```jaileefunkprincess```

All sample images also use the bad prompt embedding: https://huggingface.co/datasets/Nerfgun3/bad_prompt#version-2

---

☕ If you enjoy this model, buy me a coffee [![Buy a coffee](https://badgen.net/badge/icon/kofi?icon=kofi&amp;label=buy%20us%20a%20coffee)](https://ko-fi.com/3eegames)

---


## 🧾 Prompt example:

**The queen has returned**

```Perfectly-centered close up portrait of a real life godly woman (jaileefunkprincess :1.1)with long purple hair and wearing shining armor descending from heaven, lifelike, super highly detailed, professional digital painting, artstation, concept art, Unreal Engine 5, Photorealism, HD quality, 8k resolution, cinema 4d, 3D, beautiful, cinematic, art by artgerm and greg rutkowski and alphonse mucha and loish and WLOP, dynamic pose```

Negative prompt:

```(bad_prompt_version2:0.8), lowres, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, ((ugly)), ((duplicate)), ((morbid)), ((mutilated)), out of frame, extra fingers, mutated hands, ((poorly drawn hands)), ((poorly drawn face)), (((mutation))), (((deformed))), ((bad anatomy)), (((bad proportions))), ((extra limbs)), cloned face, (((disfigured))), extra limbs, gross proportions, (malformed limbs), ((missing arms)), ((missing legs)), (((extra arms))), (((extra legs))), mutated hands, (fused fingers), (too many fingers), (((long neck)))```

_Steps: 80, Sampler: DPM adaptive, CFG scale: 10.5, Seed: 945244310, Size: 512x512, Model hash: d0b457ae_ (Model hash: protogen-x53-photorealism-official-release -  https://civitai.com/models/3816/protogen-x53-photorealism-official-release)

---

## License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

-  You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
-  The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
-  You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)