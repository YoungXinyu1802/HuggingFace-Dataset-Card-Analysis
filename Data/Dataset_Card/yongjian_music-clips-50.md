---
pretty_name: music-clips-50
multilinguality:
- other-music
language:
- en
- zh
---

There are 50 music clips(of 3~5 seconds).
You can load them by the following code:

```python
from datasets import load_dataset
dataset = load_dataset('yongjian/music-clips-50')

clips = dataset['train'] # all 50 music clips
music_1_np_array = clips[0]['audio']['array'] # numpy array of shape=[N,]
```

Or you can directly download them from Google Drive: [music-clips-50.tar.gz](https://drive.google.com/file/d/154y_Z9p1Sfhrwzj7jc46UMbTaAmI17AT/view?usp=sharing).