---
language:
- en
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: Gameplay Images
size_categories:
- 1K<n<10K
task_categories:
- image-classification
---
# Gameplay Images
## Dataset Description
- **Homepage:** [kaggle](https://www.kaggle.com/datasets/aditmagotra/gameplay-images)
- **Download Size** 2.50 GiB
- **Generated Size** 1.68 GiB
- **Total Size** 4.19 GiB

A dataset from [kaggle](https://www.kaggle.com/datasets/aditmagotra/gameplay-images).

This is a dataset of 10 very famous video games in the world.

These include

- Among Us
- Apex Legends
- Fortnite
- Forza Horizon
- Free Fire
- Genshin Impact
- God of War
- Minecraft
- Roblox
- Terraria

There are 1000 images per class and all are sized `640 x 360`. They are in the `.png` format.

This Dataset was made by saving frames every few seconds from famous gameplay videos on Youtube.

※ This dataset was uploaded in January 2022. Game content updated after that will not be included.

### License

CC-BY-4.0

## Dataset Structure

### Data Instance

```python
>>> from datasets import load_dataset

>>> dataset = load_dataset("Bingsu/Gameplay_Images")
DatasetDict({
    train: Dataset({
        features: ['image', 'label'],
        num_rows: 10000
    })
})
```
```python
>>> dataset["train"].features
{'image': Image(decode=True, id=None),
 'label': ClassLabel(num_classes=10, names=['Among Us', 'Apex Legends', 'Fortnite', 'Forza Horizon', 'Free Fire', 'Genshin Impact', 'God of War', 'Minecraft', 'Roblox', 'Terraria'], id=None)}
```

### Data Size

download: 2.50 GiB<br>
generated: 1.68 GiB<br>
total: 4.19 GiB

### Data Fields

- image: `Image`
    - A `PIL.Image.Image object` containing the image. size=640x360
    - Note that when accessing the image column: `dataset[0]["image"]` the image file is automatically decoded. Decoding of a large number of image files might take a significant amount of time. Thus it is important to first query the sample index before the "image" column, i.e. `dataset[0]["image"]` should always be preferred over `dataset["image"][0]`.
- label: an int classification label.

Class Label Mappings:

```json
{
    "Among Us": 0,
    "Apex Legends": 1,
    "Fortnite": 2,
    "Forza Horizon": 3,
    "Free Fire": 4,
    "Genshin Impact": 5,
    "God of War": 6,
    "Minecraft": 7,
    "Roblox": 8,
    "Terraria": 9
}
```

```python
>>> dataset["train"][0]
{'image': <PIL.PngImagePlugin.PngImageFile image mode=RGBA size=640x360>,
 'label': 0}
```


### Data Splits

|            |   train  |
| ---------- | -------- |
| # of data  |    10000 |

### Note

#### train_test_split

```python
>>> ds_new = dataset["train"].train_test_split(0.2, seed=42, stratify_by_column="label")
>>> ds_new
DatasetDict({
    train: Dataset({
        features: ['image', 'label'],
        num_rows: 8000
    })
    test: Dataset({
        features: ['image', 'label'],
        num_rows: 2000
    })
})
```
