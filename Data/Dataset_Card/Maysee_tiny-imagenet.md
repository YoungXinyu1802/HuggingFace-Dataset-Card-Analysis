---
annotations_creators:
- crowdsourced
extra_gated_prompt: "By clicking on \u201CAccess repository\u201D below, you also\
  \ agree to ImageNet Terms of Access:\n[RESEARCHER_FULLNAME] (the \"Researcher\"\
  ) has requested permission to use the ImageNet database (the \"Database\") at Princeton\
  \ University and Stanford University. In exchange for such permission, Researcher\
  \ hereby agrees to the following terms and conditions:\n1. Researcher shall use\
  \ the Database only for non-commercial research and educational purposes.\n2. Princeton\
  \ University, Stanford University and Hugging Face make no representations or warranties\
  \ regarding the Database, including but not limited to warranties of non-infringement\
  \ or fitness for a particular purpose.\n3. Researcher accepts full responsibility\
  \ for his or her use of the Database and shall defend and indemnify the ImageNet\
  \ team, Princeton University, Stanford University and Hugging Face, including their\
  \ employees, Trustees, officers and agents, against any and all claims arising from\
  \ Researcher's use of the Database, including but not limited to Researcher's use\
  \ of any copies of copyrighted images that he or she may create from the Database.\n\
  4. Researcher may provide research associates and colleagues with access to the\
  \ Database provided that they first agree to be bound by these terms and conditions.\n\
  5. Princeton University, Stanford University and Hugging Face reserve the right\
  \ to terminate Researcher's access to the Database at any time.\n6. If Researcher\
  \ is employed by a for-profit, commercial entity, Researcher's employer shall also\
  \ be bound by these terms and conditions, and Researcher hereby represents that\
  \ he or she is fully authorized to enter into this agreement on behalf of such employer.\n\
  7. The law of the State of New Jersey shall apply to all disputes under this agreement."
language:
- en
language_creators:
- crowdsourced
license: []
multilinguality:
- monolingual
paperswithcode_id: imagenet
pretty_name: Tiny-ImageNet
size_categories:
- 100K<n<1M
source_datasets:
- extended|imagenet-1k
task_categories:
- image-classification
task_ids:
- multi-class-image-classification
---

# Dataset Card for tiny-imagenet

## Dataset Description

- **Homepage:** https://www.kaggle.com/c/tiny-imagenet
- **Repository:** [Needs More Information]
- **Paper:** http://cs231n.stanford.edu/reports/2017/pdfs/930.pdf
- **Leaderboard:** https://paperswithcode.com/sota/image-classification-on-tiny-imagenet-1

### Dataset Summary

Tiny ImageNet contains 100000 images of 200 classes (500 for each class) downsized to 64×64 colored images. Each class has 500 training images, 50 validation images, and 50 test images.

### Languages

The class labels in the dataset are in English.

## Dataset Structure

### Data Instances

```json
{
  'image': <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=64x64 at 0x1A800E8E190,
  'label': 15
}
```

### Data Fields

- image: A PIL.Image.Image object containing the image. Note that when accessing the image column: dataset[0]["image"] the image file is automatically decoded. Decoding of a large number of image files might take a significant amount of time. Thus it is important to first query the sample index before the "image" column, i.e. dataset[0]["image"] should always be preferred over dataset["image"][0].
- label: an int classification label. -1 for test set as the labels are missing. Check `classes.py` for the map of numbers & labels.

### Data Splits

|              | Train  | Valid |
| ------------ | ------ | ----- |
| # of samples | 100000 | 10000 |

## Usage

### Example

#### Load Dataset
```python
def example_usage():
    tiny_imagenet = load_dataset('Maysee/tiny-imagenet', split='train')
    print(tiny_imagenet[0])

if __name__ == '__main__':
    example_usage()
```