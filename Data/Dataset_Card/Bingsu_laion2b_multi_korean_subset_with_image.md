---
annotations_creators:
- crowdsourced
language:
- ko
language_creators:
- crowdsourced
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: 'laion2b multi korean subset with image'
size_categories:
- 1M<n<10M
source_datasets:
- extended|laion/laion2B-multi
tags: []
task_categories:
- feature-extraction
task_ids: []
---

# laion2b_multi_korean_subset_with_image

## Dataset Description
- **Download Size** 342 GB

img2dataset을 통해 다운로드에 성공한 [Bingsu/laion2B-multi-korean-subset](https://huggingface.co/datasets/Bingsu/laion2B-multi-korean-subset) 이미지를 정리한 데이터셋입니다.

이미지는 9,800,137장입니다.

이미지는 짧은 쪽 길이가 256이 되도록 리사이즈 되었으며, 품질 100인 webp파일로 다운로드 되었습니다.

## Usage

### 1. datasets

```python
>>> from datasets import load_dataset

>>> dataset = load_dataset("Bingsu/laion2b_multi_korean_subset_with_image", streaming=True, split="train")

>>> dataset.features
{'image': Image(decode=True, id=None),
 'text': Value(dtype='string', id=None),
 'width': Value(dtype='int32', id=None),
 'height': Value(dtype='int32', id=None)}

>>> next(iter(dataset))
{'image': <PIL.WebPImagePlugin.WebPImageFile image mode=RGB size=256x256>,
 'text': '소닉기어 에어폰5 휴대용 스테레오 블루투스 헤드폰',
 'width': 256,
 'height': 256}
```

### 2. webdataset

이 데이터셋은 [webdataset](https://github.com/webdataset/webdataset)으로 사용할 수 있도록 구성되어있습니다. 데이터를 다운로드하지 않고 스트리밍으로 처리한다면 1번 방법보다 훨씬 빠릅니다.

!! 아래 방법은 Windows에서는 에러가 발생합니다.

```python
>>> import webdataset as wds

>>> url = "https://huggingface.co/datasets/Bingsu/laion2b_multi_korean_subset_with_image/resolve/main/data/{00000..02122}.tar"
>>> dataset = wds.WebDataset(url).shuffle(1000).decode("pil").to_tuple("webp", "json")
```

```python
>>> next(iter(dataset))
...
```

이 글을 작성하는 현재(22-10-18), webp이미지의 자동 디코딩을 지원하지 않고 있기 때문에([PR #215](https://github.com/webdataset/webdataset/pull/215)), 직접 디코딩해야 합니다.

```python
import io
import webdataset as wds
from PIL import Image

def preprocess(data):
    webp, jsn = data
    img = Image.open(io.BytesIO(webp))
    out = {
        "image": img,
        "text": jsn["caption"],
        "width": jsn["width"],
        "height": jsn["height"]
    }
    return out

url = "https://huggingface.co/datasets/Bingsu/laion2b_multi_korean_subset_with_image/resolve/main/data/{00000..02122}.tar"
dataset = wds.WebDataset(url).shuffle(1000).decode("pil").to_tuple("webp", "json").map(preprocess)
```

```python
>>> next(iter(dataset))
{'image': <PIL.WebPImagePlugin.WebPImageFile image mode=RGB size=427x256>,
 'text': '[따블리에]유아동 미술가운, 미술 전신복',
 'width': 427,
 'height': 256}
```

## Note

![tar_image](https://huggingface.co/datasets/Bingsu/laion2b_multi_korean_subset_with_image/resolve/main/tar_example.png)
각각의 tar 파일은 위 처럼 구성되어 있습니다.

다운로드에 실패한 이미지는 건너뛰어져있기 때문에 파일 이름은 완전히 연속적이지는 않습니다.

각각의 json 파일은 다음처럼 되어있습니다.

```json
{
    "caption": "\ub514\uc790\uc778 \uc53d\ud0b9\uacfc \ub514\uc9c0\ud138 \ud2b8\ub79c\uc2a4\ud3ec\uba54\uc774\uc158",
    "url": "https://image.samsungsds.com/kr/insights/dt1.jpg?queryString=20210915031642",
    "key": "014770069",
    "status": "success",
    "error_message": null,
    "width": 649,
    "height": 256,
    "original_width": 760,
    "original_height": 300,
    "exif": "{}"
}
```

txt파일은 json파일의 "caption"을 담고 있습니다.
