For the V5 dataset, screenshots are grabbed from the raw B1, B3 and B4 LoK Blu-Rays with a custom VapourSynth script. The short version of procedure is:

- Detect scene changes, and select 2-3 frames from each scene depending on how long it is, at the beginning, middle, and end of the scene.
- Convert the frames to 16-bit RGB.
- Very mildly deblock with Deblock QED, to get rid of the blocking artifacts: https://github.com/HomeOfVapourSynthEvolution/havsfunc
- Very mildly temporally denoise with BM3D, using several adjacent frames, to get rid of other minor artifacts like noise, banding, and to soften whatever blocking is left: https://github.com/HomeOfVapourSynthEvolution/VapourSynth-BM3D
- Write the frames as 16-bit RGB PNGs with imagemagick.
- Optimize the filesize of the resulting frames with Efficient Compression Utility.

This results in 1865 high quality 1920x1080 frames. Book 2 is skipped because the B2 blu-ray is interlaced, which (even with a deinterlacing algorithm) may cause training issues.

The V6 dataset is simply a culled version of the V5 dataset, with frames I deemed redundant or problematic removed. The end result is 753 very high quality frames. 

Previews coming soon.


---
license: wtfpl
---
