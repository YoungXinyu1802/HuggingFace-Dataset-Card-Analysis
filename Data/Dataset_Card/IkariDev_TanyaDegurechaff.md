---
language:
- en
license: creativeml-openrail-m
thumbnail: ""
tags:
- stable-diffusion
- text-to-image
- image-to-image
inference: false
---

# Sad Atmospheric Embedding / Textual Inversion

<table>
   <tr>
    <td><img src=https://i.ibb.co/Kz90c5m/20221103073574-96971022-masterpiece-best-quality-masterpiece-absurdres-best-quality-tanya-degurechaf.png width=70% height=70%/></td>
    <td><img src=https://i.ibb.co/frXzcMt/20221103073575-96971023-masterpiece-best-quality-masterpiece-absurdres-best-quality-tanya-degurechaf.png width=70% height=70%/></td>
    <td><img src=https://i.ibb.co/VYWmWCL/20221103073578-96971024-masterpiece-best-quality-masterpiece-absurdres-best-quality-tanya-degurechaf.png width=79% height=70%/></td>
   </tr>
</table>

## Usage

To use this embedding you have to download the file as well as drop it into the "\stable-diffusion-webui\embeddings" folder

To use it in a prompt: ```"TanyaDegurechaff"```

Personally, I would recommend using this embedding with a strength of 0.8, like ```"(TanyaDegurechaff:0.8)"```

I strongly advise against going over 1.1, because it will certainly break the embedding!


a good prompt I tried:
```"masterpiece, best quality, masterpiece, absurdres, best quality, tanya degurechaff, blonde hair, ponytail, military uniform, military hat, (short hair:1.1), 1girl, (messy hair:1.1), floating hair, (realistic:1.0), solo, portrait, flat chest, female child, small breasts, ruffling hair, looking at viewer, crazy eyes, (crazy smile:1.1), blue eyes, (TanyaDegurechaff:0.8), green military uniform, (chibi:1.1), (green jacket:0.9), thick eyelashes"```

negative:
```"lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, artist name, crying, blush, (open mouth:0.8), +_+,lipstick,sitting, lying, (close-up:1.1), (simple background:1.1)"```



I trained the embedding based on [Elysium V2](https://huggingface.co/hesw23168/SD-Elysium-Model/blob/main/Elysium_Anime_V2.ckpt) with 45 images until epoch 2, 10200 steps.

If the normal version(TanyaDegurechaff.pt) looks bad, download the file "embeddings.zip". You can test which fits your needs.

I hope you enjoy the embedding. If you have any questions, you can ask me anything via Discord: "IkariDev#9110"

## Credits
Spacial thanks to:

[Trexdel](https://huggingface.co/Trexdel) - Helped prune the dataset from 250 images down to 22.

Everyone on the Stable diffusion anime channel.

## License

This embedding is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

1. You can't use the embedding to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the embedding commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)