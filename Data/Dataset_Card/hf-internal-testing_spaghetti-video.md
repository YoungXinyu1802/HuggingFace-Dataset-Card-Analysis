This dataset contains both 8 and 16 sampled frames of the "eating-spaghetti" video of the Kinetics-400 dataset, with the following frame indices being used: 

* 8 frames (`eating_spaghetti_8_frames.npy`): [ 97,  98,  99, 100, 101, 102, 103, 104] (NumPy seed was 1024, clip_len=8, frame_sample_rate=1, seg_len=len(vr))
* 16 frames (`eating_spaghetti.npy`): [164, 168, 172, 176, 181, 185, 189, 193, 198, 202, 206, 210, 215, 219, 223, 227].
* 32 frames (`eating_spaghetti_32_frames.npy`): array([ 47,  51,  55,  59,  63,  67,  71,  75,  80,  84,  88,  92,  96,
       100, 104, 108, 113, 117, 121, 125, 129, 133, 137, 141, 146, 150,
       154, 158, 162, 166, 170, 174]) (NumPy seed was 0, clip_len=32, frame_sample_rate=4, seg_len=len(vr))

This is the code:

```
from decord import VideoReader, cpu
from huggingface_hub import hf_hub_download
import numpy as np

file_path = hf_hub_download(
        repo_id="nielsr/video-demo", filename="eating_spaghetti.mp4", repo_type="dataset"
)
vr = VideoReader(file_path, num_threads=1, ctx=cpu(0))

# get 16 frames
vr.seek(0)
indices = [164 168 172 176 181 185 189 193 198 202 206 210 215 219 223 227]
video = vr.get_batch(indices).asnumpy()

# save as NumPy array
with open('eating_spaghetti.npy', 'wb') as f:
    np.save(f, video)
```