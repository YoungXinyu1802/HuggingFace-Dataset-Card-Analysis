---
license:
- cc0-1.0
converted_from: kaggle
kaggle_id: succinctlyai/midjourney-texttoimage
---

# Dataset Card for Midjourney User Prompts & Generated Images (250k)

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Homepage:** https://kaggle.com/datasets/succinctlyai/midjourney-texttoimage
- **Repository:**
- **Paper:**
- **Leaderboard:**
- **Point of Contact:**

### Dataset Summary

General Context
===
[Midjourney](https://midjourney.com) is an independent research lab whose broad mission is to "explore new mediums of thought". In 2022, they launched a text-to-image service that, given a natural language prompt, produces visual depictions that are faithful to the description. Their service is accessible via a public [Discord server](https://discord.com/invite/midjourney), where users interact with a [Midjourney bot](https://midjourney.gitbook.io/docs/#create-your-first-image). When issued a query in natural language, the bot returns four low-resolution images and offers further options like upscaling or re-generating a variation of the original images.

This dataset was obtained by scraping messages from the public Discord server over a period of four weeks (June 20, 2002 - July 17, 2022). The authors have no affiliation with Midjourney and are releasing this data with the sole purpose of enabling research on text-to-image model prompting (see the Sample Use Case section below).

Midjourney's Discord Server
---
Here is what the interaction with the Midjourney bot looks like on Discord:
1. Issuing an initial prompt:
![Screenshot showing how to issue an initial prompt](https://drive.google.com/uc?export=view&id=1k6BuaJNWThCr1x2Ezojx3fAmDIyeZhbp "Result of issuing an initial prompt")

2. Upscaling the bottom-left image:
![Screenshot showing how to request upscaling an image](https://drive.google.com/uc?export=view&id=15Y65Fe0eVKVPK5YOul0ZndLuqo4Lg4xk "Result of upscaling an image")

3. Requesting variations of the bottom-left image:
![Screenshot showing how to request a variation of a generated image](https://drive.google.com/uc?export=view&id=1-9kw69PgM5eIM5n1dir4lQqGCn_hJfOA "Result of requesting a variation of an image")

Dataset Format
===
The dataset was produced by scraping ten public Discord channels in the "general" category (i.e., with no dedicated topic) over four weeks. Filenames follow the pattern `channel-name_yyyy_mm_dd.json`. The `"messages"` field in each JSON file contains a list of [Message](https://discord.com/developers/docs/resources/channel#message-object) objects, one per user query. A message includes information such as the user-issued prompt, a link to the generated image, and other metadata. See [the companion notebook](https://www.kaggle.com/succinctlyai/midjourney-prompt-analysis) with utilities for extracting such information.

| User Prompt | Generated Image URL |
| --- | --- |
| anatomical heart fill with deers, neon, pastel, artstation | https://cdn.discordapp.com/attachments/985204969722486814/989673529102463016/f14d5cb4-aa4d-4060-b017-5ee6c1db42d6_Ko_anatomical_heart_fill_with_deers_neon_pastel_artstation.png |
| anatomical heart fill with jumping running deers, neon, pastel, artstation | https://cdn.discordapp.com/attachments/985204969722486814/989675045439815721/1d7541f2-b659-4a74-86a3-ae211918723c_Ko_anatomical_heart_fill_with_jumping_running_deers_neon_pastel_artstation.png |
| https://s.mj.run/UlkFmVAKfaE cat with many eyes floating in colorful glowing swirling whisps, occult inspired, emerging from the void, shallow depth of field | https://cdn.discordapp.com/attachments/982990243621908480/988957623229501470/6116dc5f-64bb-4afb-ba5f-95128645c247_MissTwistedRose_cat_with_many_eyes_floating_in_colorful_glowing_swirling_whisps_occult_inspired_emerging_from_the_vo.png |

Dataset Stats
===
The dataset contains:
- **268k** messages from 10 public Discord channel collected over 28 days.
- **248k** user-generated prompts and their associated generated images, out of which:
	+ 60% are requests for new images (initial or variation requests for a previously-generated image), and
	+ 40% are requests for upscaling previously-generated images.
	
Prompt Analysis
===
Here are the most prominent phrases among the user-generated text prompts:
![word cloud](https://drive.google.com/uc?export=view&id=1J432wrecf2zibDFU5sT3BXFxqmt3PJ-P)

Prompt lengths span from 1 to 60 whitespace-separated tokens, with the mode around 15 tokens:
![prompt lengths](https://drive.google.com/uc?export=view&id=1fFObFvcWwOEGJ3k47G4fzIHZXmxS3RiW)

See the [the companion notebook](https://www.kaggle.com/succinctlyai/midjourney-prompt-analysis) for an in-depth analysis of how users control various aspects of the generated images (lighting, resolution, photographic elements, artistic style, etc.).

Sample Use Case
===
One way of leveraging this dataset is to help address the [prompt engineering](https://www.wired.com/story/dalle-art-curation-artificial-intelligence/) problem: artists that use text-to-image models in their work spend a significant amount of time carefully crafting their text prompts. We built an additional model for prompt autocompletion by learning from the queries issued by Midjourney users. [This notebook](https://www.kaggle.com/code/succinctlyai/midjourney-text-prompts-huggingface) shows how to extract the natural language prompts from the Discord messages and create a HuggingFace dataset to be used for training. The processed dataset can be found at [succinctly/midjourney-prompts](https://huggingface.co/datasets/succinctly/midjourney-prompts), and the prompt generator (a GPT-2 model fine-tuned on prompts) is located at [succinctly/text2image-prompt-generator](https://huggingface.co/succinctly/text2image-prompt-generator).

Here is how our model can help brainstorm creative prompts and speed up prompt engineering:
![prompt autocomplete model](https://drive.google.com/uc?export=view&id=1JqZ-CaWNpQ4iO0Qcd3b8u_QnBp-Q0PKu)

Authors
===
This project was a collaboration between [Iulia Turc](https://twitter.com/IuliaTurc) and [Gaurav Nemade](https://twitter.com/gaurav_nemade15). We recently left Google Research to work on something new. Feel free to Tweet at us, or follow our journey at [succinctly.ai](https://succinctly.ai). 


Interesting Finds
===
Here are some of the generated images that drew our attention:

| User Prompt | Generated Image |
| --- | --- |
| https://s.mj.run/JlwNbH Historic Ensemble of the Potala Palace Lhasa, japanese style painting,trending on artstation, temple, architecture, fiction, sci-fi, underwater city, Atlantis , cyberpunk style, 8k revolution, Aokigahara fall background , dramatic lighting, epic, photorealistic, in his lowest existential moment with high detail, trending on artstation,cinematic light, volumetric shading ,high radiosity , high quality, form shadow, rim lights , concept art of architecture, 3D,hyper deatiled,very high quality,8k,Maxon cinema,visionary,imaginary,realistic,as trending on the imagination of Gustave Doré idea,perspective view,ornate light --w 1920 --h 1024 | ![palace](https://drive.google.com/uc?export=view&id=1xl2Gr1TSWCh0p_8o_wJnQIsO1qxW02Z_) |
| a dark night with fog in a metropolis of tomorrow by hugh ferriss:, epic composition, maximum detail, Westworld, Elysium space station, space craft shuttle, star trek enterprise interior, moody, peaceful, hyper detailed, neon lighting, populated, minimalist design, monochromatic, rule of thirds, photorealistic, alien world, concept art, sci-fi, artstation, photorealistic, arch viz , volumetric light moody cinematic epic, 3d render, octane render, trending on artstation, in the style of dylan cole + syd mead + by zaha hadid, zaha hadid architecture + reaction-diffusion + poly-symmetric + parametric modelling, open plan, minimalist design 4k --ar 3:1 | ![metropolis](https://drive.google.com/uc?export=view&id=16A-VtlbSZCaUFiA6CZQzevPgBGyBiXWI) |
| https://s.mj.run/qKj8n0 fantasy art, hyperdetailed, panoramic view, foreground is a crowd of ancient Aztec robots are doing street dance battle , main part is middleground is majestic elegant Gundam mecha robot design with black power armor and unsettling ancient Aztec plumes and decorations scary looking with two magical neon swords combat fighting::2 , background is at night with nebula eruption, Rembrandt lighting, global illumination, high details, hyper quality, unreal negine, octane render, arnold render, vray render, photorealistic, 8k --ar 3:1 --no dof,blur,bokeh | ![ancient](https://drive.google.com/uc?export=view&id=1a3jI3eiQwLbulaSS2-l1iGJ6-kokMMvc) |
| https://s.mj.run/zMIhrKBDBww in side a Amethyst geode cave, 8K symmetrical portrait, trending in artstation, epic, fantasy, Klimt, Monet, clean brush stroke, realistic highly detailed, wide angle view, 8k post-processing highly detailed, moody lighting rendered by octane engine, artstation,cinematic lighting, intricate details, 8k detail post processing, --no face --w 512 --h 256 | ![cave](https://drive.google.com/uc?export=view&id=1gUx-3drfCBBFha8Hoal4Ly4efDXSrxlB) |
| https://s.mj.run/GTuMoq whimsically designed gothic, interior of a baroque cathedral in fire with moths and birds flying, rain inside, with angels, beautiful woman dressed with lace victorian and plague mask, moody light, 8K photgraphy trending on shotdeck, cinema lighting, simon stålenhag, hyper realistic octane render, octane render, 4k post processing is very detailed, moody lighting, Maya+V-Ray +metal art+ extremely detailed, beautiful, unreal engine, lovecraft, Big Bang cosmology in LSD+IPAK,4K, beatiful art by Lêon François Comerre, ashley wood, craig mullins, ,outer space view, William-Adolphe Bouguereau, Rosetti --w 1040 --h 2080 | ![gothic](https://drive.google.com/uc?export=view&id=1nmsTEdPEbvDq9SLnyjjw3Pb8Eb-C1WaP) |

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

[More Information Needed]

## Dataset Structure

### Data Instances

[More Information Needed]

### Data Fields

[More Information Needed]

### Data Splits

[More Information Needed]

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

This dataset was shared by [@succinctlyai](https://kaggle.com/succinctlyai)

### Licensing Information

The license for this dataset is cc0-1.0

### Citation Information

```bibtex
[More Information Needed]
```

### Contributions

[More Information Needed]