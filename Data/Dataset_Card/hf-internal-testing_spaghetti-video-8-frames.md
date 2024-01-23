---
---

This is the code that was used to generate this video:

```
from decord import VideoReader, cpu
from huggingface_hub import hf_hub_download
import numpy as np

np.random.seed(0)

def sample_frame_indices(clip_len, frame_sample_rate, seg_len):
    converted_len = int(clip_len * frame_sample_rate)
    end_idx = np.random.randint(converted_len, seg_len)
    start_idx = end_idx - converted_len
    indices = np.linspace(start_idx, end_idx, num=clip_len)
    indices = np.clip(indices, start_idx, end_idx - 1).astype(np.int64)
    return indices

file_path = hf_hub_download(
        repo_id="nielsr/video-demo", filename="eating_spaghetti.mp4", repo_type="dataset"
)
vr = VideoReader(file_path, num_threads=1, ctx=cpu(0))

# sample 8 frames
vr.seek(0)
indices = sample_frame_indices(clip_len=8, frame_sample_rate=1, seg_len=len(vr))
buffer = vr.get_batch(indices).asnumpy()

# create a list of NumPy arrays
video = [buffer[i] for i in range(buffer.shape[0])]

video_numpy = np.array(video)
with open('spaghetti_video_8_frames.npy', 'wb') as f:
    np.save(f, video_numpy)
```