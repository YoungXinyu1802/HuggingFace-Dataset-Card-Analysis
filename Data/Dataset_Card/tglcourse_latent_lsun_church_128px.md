---
dataset_info:
  features:
  - name: label
    dtype:
      class_label:
        names:
          0: '0'
          1: '1'
          2: '2'
          3: '3'
          4: '4'
          5: '5'
          6: '6'
          7: '7'
          8: '8'
          9: '9'
          10: a
          11: b
          12: c
          13: d
          14: e
          15: f
  - name: latent
    sequence:
      sequence:
        sequence: float32
  splits:
  - name: test
    num_bytes: 27646560
    num_examples: 6312
  - name: train
    num_bytes: 525227700
    num_examples: 119915
  download_size: 527167710
  dataset_size: 552874260
---
# Dataset Card for "latent_lsun_church_128px"

Each image is cropped to 128px square and encoded to a 4x16x16 latent representation using the same VAE as that employed by Stable Diffusion

Decoding
```python
from diffusers import AutoencoderKL
from datasets import load_dataset
from PIL import Image
import numpy as np
import torch
# load the dataset
dataset = load_dataset('tglcourse/latent_lsun_church_128px')
# Load the VAE (requires access - see repo model card for info)
vae = AutoencoderKL.from_pretrained("CompVis/stable-diffusion-v1-4", subfolder="vae")
latent = torch.tensor([dataset['train'][0]['latent']]) # To tensor (bs, 4, 16, 16)
latent = (1 / 0.18215) * latent # Scale to match SD implementation
with torch.no_grad():
    image = vae.decode(latent).sample[0] # Decode 
image = (image / 2 + 0.5).clamp(0, 1) # To (0, 1)
image = image.detach().cpu().permute(1, 2, 0).numpy() # To numpy, channels lsat
image = (image * 255).round().astype("uint8") # (0, 255) and type uint8
image = Image.fromarray(image) # To PIL
image # The resulting PIL image
```