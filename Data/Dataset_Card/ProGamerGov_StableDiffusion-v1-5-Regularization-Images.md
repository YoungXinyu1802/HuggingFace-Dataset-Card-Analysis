---
license: mit
---

A collection of regularization / class instance datasets for the [Stable Diffusion v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) model to use for DreamBooth prior preservation loss training. Files labeled with "mse vae" used the [stabilityai/sd-vae-ft-mse](https://huggingface.co/stabilityai/sd-vae-ft-mse) VAE. For ease of use, datasets are stored as zip files containing 512x512 PNG images. The number of images in each zip file is specified at the end of the filename.

There is currently a bug where HuggingFace is incorrectly reporting that the datasets are pickled. They are not picked, they are simple ZIP files containing the images.


Currently this repository contains the following datasets (datasets are named after the prompt they used):

Art Styles

* "**artwork style**": 4125 images generated using 50 DDIM steps and a CFG of 7, using the MSE VAE.

* "**artwork style**": 4200 images generated using 50 DPM++ 2S a Karras steps and a CFG of 7, using the MSE VAE. A negative prompt of "text" was also used for this dataset.

* "**artwork style**": 2750 images generated using 50 DPM++ 2S a Karras steps and a CFG of 7, using the MSE VAE.

* "**illustration style**": 3050 images generated using 50 DDIM steps and a CFG of 7, using the MSE VAE.

* "**erotic photography**": 2760 images generated using 50 DDIM steps and a CFG of 7, using the MSE VAE.

* "**landscape photography**": 2500 images generated using 50 DPM++ 2S a Karras steps and a CFG of 7, using the MSE VAE. A negative prompt of "b&w, text" was also used for this dataset.

People

* "**person**": 2115 images generated using 50 DDIM steps and a CFG of 7, using the MSE VAE.

* "**woman**": 4420 images generated using 50 DDIM steps and a CFG of 7, using the MSE VAE.

* "**guy**": 4820 images generated using 50 DDIM steps and a CFG of 7, using the MSE VAE.

* "**supermodel**": 4411 images generated using 50 DDIM steps and a CFG of 7, using the MSE VAE.

* "**bikini model**": 4260 images generated using 50 DDIM steps and a CFG of 7, using the MSE VAE.

* "**sexy athlete**": 5020 images generated using 50 DDIM steps and a CFG of 7, using the MSE VAE.

* "**femme fatale**": 4725 images generated using 50 DDIM steps and a CFG of 7, using the MSE VAE.

* "**sexy man**": 3505 images generated using 50 DDIM steps and a CFG of 7, using the MSE VAE.

* "**sexy woman**": 3500 images generated using 50 DDIM steps and a CFG of 7, using the MSE VAE.

Animals

* "**kitty**": 5100 images generated using 50 DDIM steps and a CFG of 7, using the MSE VAE.

* "**cat**": 2050 images generated using 50 DDIM steps and a CFG of 7, using the MSE VAE.

Vehicles

* "**fighter jet**": 1600 images generated using 50 DDIM steps and a CFG of 7, using the MSE VAE.

* "**train**": 2669 images generated using 50 DDIM steps and a CFG of 7, using the MSE VAE.

* "**car**": 3150 images generated using 50 DDIM steps and a CFG of 7, using the MSE VAE.

Themes

* "**cyberpunk**": 3040 images generated using 50 DDIM steps and a CFG of 7, using the MSE VAE.


I used the "Generate Forever" feature in [AUTOMATIC1111's WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui) to create thousands of images for each dataset. Every image in a particular dataset uses the exact same settings, with only the seed value being different.

You can use my regularization / class image datasets with: https://github.com/ShivamShrirao/diffusers, https://github.com/JoePenna/Dreambooth-Stable-Diffusion, https://github.com/TheLastBen/fast-stable-diffusion, and any other DreamBooth projects that have support for prior preservation loss.
