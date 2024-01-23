---
license: cc
language:
- ru
tags:
- image
- captcha
---

# Note
Captcha images are presented as base64 string.
All csv files have a "\t" separator.

# Dataset consists of several files
## fssp_*.csv

I am publishing an updated version of the archive of 40,310 pictures, which I have divided into 4 categories:
- 4 symbols on the picture - 6 747 pcs.
- 5 symbols - 18 403 pcs.
- 6 characters - 7,038 pcs.
- 7 characters - 7 589 pcs.

Symbols used in captcha
'б','в','г','д','ж','к','л','м','н','п','р','с','т','2','4','5','6','7','8','9'


## fms.csv

About 15 thousand captcha imgs, which consists of 6 numbers.


## rosreestr.csv

About 10 thousand captcha, which consists of English characters and numbers with a length of 5 elements.

## vk.csv

About 19 thousand captcha, which consists of Russian characters and numbers from 5 to 6 elements long. Images from social network vk.com

# Kaggle

This Dataset is updated by the previous one, which I published on [Kaggle](https://www.kaggle.com/datasets/mrdaniilak/russian-captcha-images-base64)


### Citation

```
@misc{ russian_captcha_dataset,
    title = { Russian Captcha Dataset },
    type = { Open Source Dataset },
    author = { Daniil Agniashvili },
    url = { https://huggingface.co/datasets/daniilak/russian_captcha_images/ },
    note = { visited on 2023-02-24 },
}
```


### License
Public Domain