---
annotations_creators:
- crowdsourced
language:
- tr
language_creators:
- crowdsourced
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: 'laion2B-multi-turkish-subset'
size_categories:
- 10M<n<100M
task_categories:
- text-to-image
- image-to-text
---

# Dataset Card for laion2B-multi-turkish-subset

## Dataset Description

- **Homepage:** [laion-5b](https://laion.ai/blog/laion-5b/)
- **Huggingface:** [laion/laion2B-multi](https://huggingface.co/datasets/laion/laion2B-multi)
- **Point of Contact:** [mcemilg](mailto:mcg@mcemilg.dev)

### Dataset Summary

[LAION-5B](https://laion.ai/blog/laion-5b/) is a large scale openly accessible image-text dataset contains text from multiple languages. This is a Turkish subset data of [laion/laion2B-multi](https://huggingface.co/datasets/laion/laion2B-multi). It's compatible to be used with [image2dataset](https://github.com/rom1504/img2dataset) to fetch the images at scale.


### Data Structure

```python
DatasetDict({
    train: Dataset({
        features: ['SAMPLE_ID', 'URL', 'TEXT', 'HEIGHT', 'WIDTH', 'LICENSE', 'LANGUAGE', 'NSFW', 'similarity'],
        num_rows: 34638627
    })
})
```

```python
{
   'SAMPLE_ID': Value(dtype='int64', id=None),
   'URL': Value(dtype='string', id=None),
   'TEXT': Value(dtype='string', id=None),
   'HEIGHT': Value(dtype='int64', id=None),
   'WIDTH': Value(dtype='int64', id=None),
   'LICENSE': Value(dtype='string', id=None),
   'LANGUAGE': Value(dtype='string', id=None),
   'NSFW': Value(dtype='string', id=None),
   'similarity': Value(dtype='float64', id=None)
}
```


### Notes

The data was basically processed to drop non-Turkish and irrelevant texts before published. Both [FastText](https://fasttext.cc/docs/en/language-identification.html) and [langdetect](https://pypi.org/project/langdetect/) libraries were used to identify if the text is Turkish or not. The cleaning process can be summarized as follows:

- replace \"\"\" with empty str
- remove URLs in texts
- Drop if both FastText and LangDetect are highly confident with there is no Turkish in text.
- Drop empty text fields.

### License
CC-BY-4.0



