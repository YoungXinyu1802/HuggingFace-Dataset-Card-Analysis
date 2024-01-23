---
license: agpl-3.0
---
# Help!!
We have a ton of still (non-moving) videos in the dataset. If you could somehow get rid of them please let me know!!!
# v0.1 Stats:
- Count: 11,300 gifs
- Extracted from: 40 anime videos
- Size: 250-ish MB

# Samples:
Directory View:

![Directory View](https://i.imgur.com/QfyNonS.png)

Individual:
<img src="https://huggingface.co/datasets/chavinlo/anime-face-video-dataset/resolve/main/garbage1.gif" alt="1" width="128" height="128"/> <img src="https://huggingface.co/datasets/chavinlo/anime-face-video-dataset/resolve/main/gabarge2.gif" alt="2" width="128" height="128"/> 

# Info:
A dataset in GIF format for training [chavinlo/anime-video-diffusion](https://huggingface.co/chavinlo/anime-video-diffusion)

The data is in 64x64, 20 total frames format.

The original data was in MKV form, which was later croped using a [modified version of LAFD](https://github.com/chavinlo/light-anime-face-detector) to only include the faces. After that it was converted once again with mkv to limit the size, and total frame count, while mantaining duration length.

# Format:
The dataset is provided in two formats
- ZIP file
- Directory

# Issues:
There were two main issues found during the processing of the dataset:
## Shaky videos
Due to the face detector nature, the box had issues mantaining integrity and very often resized very quickly. This could be fixed by limiting the framerate of it (?).
## Still videos
The dataset has a lot of still videos which basically would serve no purpose as they are not moving.