## Usage

For testing purpose, you can use the hosted dummy dataset (`dummy_data`) as follows:

```
import datasets
ds = datasets.load_dataset("ydshieh/coco_dataset_script", "2017", data_dir="./dummy_data/")
```

For using the COCO dataset (2017), you need to download it manually first:
```
wget http://images.cocodataset.org/zips/train2017.zip
wget http://images.cocodataset.org/zips/val2017.zip
wget http://images.cocodataset.org/zips/test2017.zip
wget http://images.cocodataset.org/annotations/annotations_trainval2017.zip
wget http://images.cocodataset.org/annotations/image_info_test2017.zip
```

Then to load the dataset:
```
COCO_DIR = ...(path to the downloaded dataset directory)...
ds = datasets.load_dataset("ydshieh/coco_dataset_script", "2017", data_dir=COCO_DIR)
```