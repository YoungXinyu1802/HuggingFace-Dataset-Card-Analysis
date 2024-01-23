---
license: mit
---
This repository contains the intermediate checkpoints for the model https://huggingface.co/laion/CLIP-ViT-H-14-laion2B-s32B-b79K.
Each "epoch" corresponds to an additional 32B/256 samples seen.
The purpose of releasing these checkpoints and optimizer states is to enable analysis.
For the first 121 "epcohs", training was done with float16 mixed precision before switching to bfloat16 after a loss blow up.