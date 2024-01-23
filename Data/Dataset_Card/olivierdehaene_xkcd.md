---
annotations_creators: []
language_creators:
- other
language:
- en
license:
- cc-by-sa-3.0
- other
multilinguality:
- monolingual
pretty_name: XKCD
size_categories:
- 1K<n<10K
source_datasets: []
task_categories:
- image-to-text
- feature-extraction
task_ids: []
---

# Dataset Card for "XKCD"

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
- [Dataset Creation](#dataset-creation)
- [Considerations for Using the Data](#considerations-for-using-the-data)
- [Additional Information](#additional-information)
  - [Licensing Information](#licensing-information)
  - [Contributions](#contributions)

## Dataset Description

- **Homepage:** [https://xkcd.com/](https://xkcd.com/), [https://www.explainxkcd.com](https://www.explainxkcd.com)
- **Repository:** [Hugging Face repository](https://huggingface.co/datasets/olivierdehaene/xkcd/tree/main)

### Dataset Summary

XKCD is an export of all XKCD comics with their transcript and explanation scrapped from 
[https://explainxkcd.com](https://explainxkcd.com).

## Dataset Structure

### Data Instances

- `id`: `1`
- `title`: `Barrel - Part 1`
- `image_title`: `Barrel - Part 1`
- `url`: `https://www.xkcd.com/1`
- `image_url`: `https://imgs.xkcd.com/comics/barrel_cropped_(1).jpg`
- `explained_url`: `https://www.explainxkcd.com/wiki/index.php/1:_Barrel_-_Part_1`
- `transcript`: `[A boy sits in a barrel which is floating in an ocean.] Boy: i wonder where i'll float next?
[A smaller frame with a zoom out of the boy in the barrel seen from afar. The barrel drifts into the distance. Nothing 
else can be seen.]`
- `explanation`: `The comic shows a young boy floating in a barrel in an ocean that doesn't have a visible end. It 
comments on the unlikely optimism and perhaps naïveté people sometimes display. The boy is completely lost and seems 
hopelessly alone, without any plan or control of the situation. Yet, rather than afraid or worried, he is instead 
quietly curious: "I wonder where I'll float next?" Although not necessarily the situation in this comic, this is a 
behavior people often exhibit when there is nothing they can do about a problematic situation for a long time; they may 
have given up hope or developed a cavalier attitude as a coping mechanism. The title text expands on the philosophical 
content, with the boy representing the average human being: wandering through life with no real plan, quietly 
optimistic, always opportunistic and clueless as to what the future may hold. The isolation of the boy may also 
represent the way in which we often feel lost through life, never knowing quite where we are, believing that there is 
no one to whom to turn. This comic could also reflect on Randall's feelings towards creating xkcd in the first place; 
unsure of what direction the web comic would turn towards, but hopeful that it would eventually become the popular web 
comic that we know today. This is the first in a six-part series of comics whose parts were randomly published during 
the first several dozen strips. The series features a character that is not consistent with what would quickly become 
the xkcd stick figure style. The character is in a barrel. In 1110: Click and Drag there is a reference to this comic 
at 1 North, 48 East . After Randall released the full The Boy and his Barrel story on xkcd, it has been clear that the 
original Ferret story should also be included as part of the barrel series. The full series can be found here . They 
are listed below in the order Randall chose for the short story above: `

### Data Fields

- `id`
- `title`
- `url`: xkcd.com URL
- `image_url`
- `explained_url`: explainxkcd.com URL
- `transcript`: english text transcript of the comic
- `explanation`: english explanation of the comic

## Dataset Creation

The dataset was scrapped from both explainxkcd.com and xkcd.com.
The dataset is therefore licensed under the Creative Commons Attribution-ShareAlike 3.0 license for
the `transcript` and `explanation` fields, while the image itself is licensed under the
Creative Commons Attribution-NonCommercial 2.5 license.

See the [Copyrights](https://www.explainxkcd.com/wiki/index.php/explain_xkcd:Copyrights) page from 
explainxkcd.com for more explanations.

### Update

You can update the dataset by using the `scrapper.py` script.
First install the dependencies:

```bash
pip install aiolimiter aiohttp beautifulsoup4 pandas
```

Then run the script:

```bash
python scrapper.py
```

## Considerations for Using the Data

As the data was scrapped, it is entirely possible that some fields are missing part of the original data.

## Additional Information

### Licensing Information

The dataset is licensed under the Creative Commons Attribution-ShareAlike 3.0 license for
the `transcript` and `explanation` fields, while the images are licensed under the
Creative Commons Attribution-NonCommercial 2.5 license.

### Contributions

Thanks to [@OlivierDehaene](https://github.com/OlivierDehaene) for adding this dataset.
