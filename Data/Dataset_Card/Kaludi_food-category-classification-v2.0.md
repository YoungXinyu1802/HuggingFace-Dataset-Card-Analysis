---
task_categories:
- image-classification

---
# Dataset for project: food-category-classification-v2.0

## Dataset Description

This dataset for project food-category-classification-v2.0 was scraped with the help of a bulk google image downloader.

## Dataset Structure

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "image": "Image(decode=True, id=None)",
  "target": "ClassLabel(names=['Bread', 'Dairy', 'Dessert', 'Egg', 'Fried Food', 'Fruit', 'Meat', 'Noodles', 'Rice', 'Seafood', 'Soup', 'Vegetable'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follows:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 1200 |
| valid        | 300 |
