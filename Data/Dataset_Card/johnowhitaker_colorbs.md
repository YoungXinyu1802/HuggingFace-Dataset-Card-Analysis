A synthetic dataset for GAN experiments.

Created with a CLOOB Conditioned Latent Diffusion model (https://github.com/JD-P/cloob-latent-diffusion)

For each color in a list of standard CSS color names, a set of images was generated using the following command:

```
python cfg_sample.py --autoencoder autoencoder_kl_32x32x4\
  --checkpoint yfcc-latent-diffusion-f8-e2-s250k.ckpt\
  --method plms\
  --cond-scale 1.0\
  --seed 34\
  --steps 25\
  -n 36\
  "A glass orb with {color} spacetime fire burning inside"
  ```
  
  