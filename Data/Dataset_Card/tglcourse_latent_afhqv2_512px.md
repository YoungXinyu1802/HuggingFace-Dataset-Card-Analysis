---
dataset_info:
  features:
  - name: label
    dtype:
      class_label:
        names:
          0: cat
          1: dog
          2: wild
  - name: latent
    sequence:
      sequence:
        sequence: float32
  splits:
  - name: train
    num_bytes: 1052290164
    num_examples: 15803
  download_size: 1038619876
  dataset_size: 1052290164
---
# Dataset Card for "latent_afhqv2_512px"

Each image is cropped to 512px square and encoded to a 4x64x64 latent representation using the same VAE as that employed by Stable Diffusion

Decoding
```python
from diffusers import AutoencoderKL
from datasets import load_dataset
from PIL import Image
import numpy as np
import torch
# load the dataset
dataset = load_dataset('tglcourse/latent_lsun_church_256px')
# Load the VAE (requires access - see repo model card for info)
vae = AutoencoderKL.from_pretrained("CompVis/stable-diffusion-v1-4", subfolder="vae")
latent = torch.tensor([dataset['train'][0]['latent']]) # To tensor (bs, 4, 64, 3264
latent = (1 / 0.18215) * latent # Scale to match SD implementation
with torch.no_grad():
    image = vae.decode(latent).sample[0] # Decode 
image = (image / 2 + 0.5).clamp(0, 1) # To (0, 1)
image = image.detach().cpu().permute(1, 2, 0).numpy() # To numpy, channels lsat
image = (image * 255).round().astype("uint8") # (0, 255) and type uint8
image = Image.fromarray(image) # To PIL
image # The resulting PIL image
```