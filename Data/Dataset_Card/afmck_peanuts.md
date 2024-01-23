---
license: other
task_categories:
- text-to-image
language:
- en
pretty_name: Peanuts Dataset (Snoopy and Co.)
size_categories:
- 10K<n<100K
dataset_info:
  features:
  - name: image
    dtype: image
  - name: panel_name
    dtype: string
  - name: characters
    sequence: string
  - name: themes
    sequence: string
  - name: color
    dtype: string
  - name: year
    dtype: int64
  - name: caption
    dtype: string
  splits:
  - name: train
    num_bytes: 2948640650.848
    num_examples: 77456
  download_size: 4601323640
  dataset_size: 2948640650.848
---

# Peanut Comic Strip Dataset (Snoopy & Co.)

![Peanuts 1999/01/30](preview.png)

This is a dataset Peanuts comic strips from `1950/10/02` to `2000/02/13`.
There are `77,457` panels extracted from `17,816` comic strips. 
The dataset size is approximately `4.4G`.

Each row in the dataset contains the following fields:
- `image`: `PIL.Image` containing the extracted panel.
- `panel_name`: unique identifier for the row.
- `characters`: `tuple[str, ...]` of characters included in the comic strip the panel is part of.
- `themes`: `tuple[str, ...]` of theme in the comic strip the panel is part of.
- `color`: `str` indicating whether the panel is grayscale or in color.
- `caption`: [BLIP-2_OPT_6.7B](https://huggingface.co/docs/transformers/main/model_doc/blip-2) generated caption from the panel.
- `year`: `int` storing the year the specific panel was released.

Character and theme information was extracted from [Peanuts Wiki (Fandom)](https://peanuts.fandom.com/wiki/Peanuts_Wiki) using [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/).
Images were extracted from [Peanuts Search](https://peanuts-search.com/).

Only strips with the following characters were extracted:
```
- "Charlie Brown"
- "Sally Brown"
- "Joe Cool" # Snoopy alter-ego
- "Franklin"
- "Violet Gray"
- "Eudora"
- "Frieda"
- "Marcie"
- "Peppermint Patty"
- "Patty"
- "Pig-Pen"
- "Linus van Pelt"
- "Lucy van Pelt"
- "Rerun van Pelt"
- "Schroeder"
- "Snoopy"
- "Shermy"
- "Spike"
- "Woodstock"
- "the World War I Flying Ace" # Snoopy alter-ego
```

### Extraction Details
Panel detection and extraction was done using the following codeblock:
```python
def check_contour(cnt):
    area = cv2.contourArea(cnt)
    if area < 600:
        return False

    _, _, w, h = cv2.boundingRect(cnt)
    if w / h < 1 / 2: return False
    if w / h > 2 / 1: return False

    return True

def get_panels_from_image(path):
    panels = []
    original_img = cv2.imread(path)
    gray = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
    invert = 255 - opening

    cnts, _ = cv2.findContours(invert, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    idx = 0 
    for cnt in cnts:
        if not check_contour(cnt): continue
        idx += 1
        x,y,w,h = cv2.boundingRect(cnt)
        roi = original_img[y:y+h,x:x+w]
        panels.append(roi)

    return panels
```
`check_contour` will reject panels with `area < 600` or with aspect ratios larger than `2` or smaller than `0.5`.

Grayscale detection was done using the following codeblock:
```python
def is_grayscale(panel):
    LAB_THRESHOLD = 10.
    img = cv2.cvtColor(panel, cv2.COLOR_RGB2LAB)
    _, ea, eb = cv2.split(img)
    de = abs(ea - eb)
    mean_e = np.mean(de)
    return mean_e < LAB_THRESHOLD

```

Captioning was done using the standard BLIP-2 pipeline shown in the [Huggingface docs](https://huggingface.co/docs/transformers/main/model_doc/blip-2) using beam search over 10 beams and a repetition penalty of `2.0`.
Raw captions are extracted and no postprocessing is applied. You may wish to normalise captions (such as replacing "cartoon" with "peanuts cartoon") or incorporate extra metadata into prompts.