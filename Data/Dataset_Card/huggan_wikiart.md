---
license: unknown
license_details: "Data files © Original Authors"
size_categories:
  - 10K<n<100K 
---

## Dataset Description

- **Homepage:** https://www.wikiart.org/

### Dataset Summary

Dataset containing 81444 pieces of visual art from various artists, taken from WikiArt.org,
along with class labels for each image :

* "artist" : 129 artist classes, including a "Unknown Artist" class
* "genre" : 11 genre classes, including a "Unknown Genre" class
* "style" : 27 style classes

On WikiArt.org, the description for the "Artworks by Genre" page reads :

A genre system divides artworks according to depicted themes and objects. A classical hierarchy of genres was developed in European culture by the 17th century. It ranked genres in high – history painting and portrait, - and low – genre painting, landscape and still life. This hierarchy was based on the notion of man as the measure of all things. Landscape and still life were the lowest because they did not involve human subject matter. History was highest because it dealt with the noblest events of humanity. Genre system is not so much relevant for a contemporary art; there are just two genre definitions that are usually applied to it: abstract or figurative.

The "Artworks by Style" page reads :

A style of an artwork refers to its distinctive visual elements, techniques and methods. It usually corresponds with an art movement or a school (group) that its author is associated with.

## Dataset Structure

* "image" : image
* "artist" : 129 artist classes, including a "Unknown Artist" class
* "genre" : 11 genre classes, including a "Unknown Genre" class
* "style" : 27 style classes

### Source Data

Files taken from this [archive](https://archive.org/download/wikiart-dataset/wikiart.tar.gz), curated from the [WikiArt website](https://www.wikiart.org/).

## Additional Information

Note:

* The WikiArt dataset can be used only for non-commercial research purpose.
* The images in the WikiArt dataset were obtained from WikiArt.org.
* The authors are neither responsible for the content nor the meaning of these images.

By using the WikiArt dataset, you agree to obey the terms and conditions of WikiArt.org.

### Contributions

[`gigant`](https://huggingface.co/gigant) added this dataset to the hub.