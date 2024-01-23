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
    <td><img src=https://i.ibb.co/YNB4xJk/20221103073134-3583436956-masterpiece-absurdres-best-quality-megumin-1-1-brown-hair-short-hair-1-1-1.png width=100% height=100%/></td>
    <td><img src=https://i.ibb.co/6sw75jp/20221103073137-3583436957-masterpiece-absurdres-best-quality-megumin-1-1-brown-hair-short-hair-1-1-1.png width=100% height=100%/></td>
    <td><img src=https://i.ibb.co/7407r5c/20221103073138-3583436958-masterpiece-absurdres-best-quality-megumin-1-1-brown-hair-short-hair-1-1-1.png width=100% height=100%/></td>
   </tr>
   <tr>
    <td><img src=https://i.ibb.co/2KXr9tp/20221103073135-3583436957-masterpiece-absurdres-best-quality-megumin-1-1-brown-hair-short-hair-1-1-1.png width=100% height=100%/></td>
    <td><img src=https://i.ibb.co/RBbjyP7/20221103073136-3583436958-masterpiece-absurdres-best-quality-megumin-1-1-brown-hair-short-hair-1-1-1.png width=100% height=100%/></td>
    <td><img src=https://i.ibb.co/tYX4s77/20221103073133-3583436955-masterpiece-absurdres-best-quality-megumin-1-1-brown-hair-short-hair-1-1-1.png width=100% height=100%/></td>
   </tr>
</table>

## Usage

To use this embedding you have to download the file as well as drop it into the "\stable-diffusion-webui\embeddings" folder

To use it in a prompt: ```"sad_atmospheric"```

Personally, I would recommend using this embedding with a strength of 0.8, like ```"(sad_atmospheric:0.8)"```

If you want to have a darker(more "sad", and better) scene, add this to your prompt ```"(sad_atmospheric:0.8), (night:1.4), wide shot, (dark:1.4), (realistic:1.2)"```

I strongly advise against going over 1.1, because it will certainly break the embedding!


a good prompt I tried:
```"masterpiece, absurdres, best quality, (megumin:1.1), brown hair, (short hair:1.1), 1girl, (messy hair:1.1), floating hair, (sidelocks:1.1), choker, blunt bangs, realistic, (detached sleeves:1.1), (bare shoulders:1.1), solo, portrait, red eyes, smooth, red dress, (loli:1.1), (chibi:1.1), flat chest, female child, small breasts, ruffling hair, looking at viewer, collarbone, arms behind back, head tilt, expressionless, (sad_atmospheric:0.8), city, cityscape, (night:1.4), wide shot, (dark:1.4), (street:1.1), lamppost, monochrome, on ground, sidewalk, car, people, crowd, cyberpunk, science fiction, (realistic:1.2)"```

negative:
```"lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, artist name, backlighting, (day:1.1), glowing, light. lights, sunlight, caustics, angry, happy, sad, blush,close-up, breasts, nude, turtleneck, hood, hat, witch hat, (close-up:1.1)"```



I trained the embedding based on [Elysium V2](https://huggingface.co/hesw23168/SD-Elysium-Model/blob/main/Elysium_Anime_V2.ckpt) with 50 images until epoch 1, 9700 steps.

If the normal version(sad_atmospheric.pt) looks bad, download the file "embeddings.zip". You can test which fits your needs.

I hope you enjoy the embedding. If you have any questions, you can ask me anything via Discord: "IkariDev#9110"

## Credits
Spacial thanks to:

[Trexdel](https://huggingface.co/Trexdel) - Helped prune the dataset from 231 images down to 50.

Everyone on the Stable diffusion anime channel.

## License

This embedding is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

1. You can't use the embedding to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the embedding commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)