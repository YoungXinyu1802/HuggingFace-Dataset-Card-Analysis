---
license: agpl-3.0
---

## Description

The Pixiv Niji Journey dataset is a collection of 9766 images with accompanying metadata, scraped from the online art platform Pixiv. The images were collected using the `gallery-dl` Python package, with the search term "nijijourney" on Pixiv. The collection period for the dataset was from November 6, 2022 to December 27, 2022.

The dataset is divided into two variants: `raw` and `preprocessed`. The `raw` variant contains the pure dataset resulting from the scraping of Pixiv, while the `preprocessed` variant contains the same dataset but with additional preprocessing steps applied. These preprocessing steps include converting the images from RGB to RGBA, labeling the dataset with captions using the BLIP tool, and providing Danbooru tags using the wd-v1-4-vit-tagger tool. The `preprocessed` variant has also been carefully cleaned and filtered to remove any low quality or irrelevant images.

The images in the dataset are in JPG and PNG format, and the metadata is provided in JSON format, while the preprocessed metadata is provided in `.txt` and `.caption` format. The metadata includes information about the images such as their captions, tags, and other metadata provided by Pixiv. The structure of the raw and preprocessed variants of the dataset is described in the `File Structure` section below.

The Pixiv Niji Journey dataset is primarily intended for use in machine learning tasks related to image classification and caption generation. It can also be used as a dataset for image generation models such as stable diffusion. However, users should be aware that the dataset may contain biases or limitations, such as the bias of the Pixiv platform or the specific search term used to collect the data.

## File Structure

The structure of the raw files is as follows:

```
  nijijourney_pixiv_2022110620221222_raw.zip/
  ├╴nijijourney/
  │ ├╴images.png
  │ ├╴images.png.json
  │ └╴...
```
while the structure of the preprocessed files is:
```
  nijijourney_pixiv_2022110620221222_preprocessed.zip/
  ├╴dataset/
  │ ├╴images.png
  │ ├╴images.png.json
  │ ├╴images.txt
  │ ├╴images.caption
  │ └╴...
  ├╴meta_cap.json
  ├╴meta_dd.json
  ├╴meta_clean.json
```

## Usage 

- Access: the dataset is available for download from the Hugging Face dataset collection
- Format: the dataset is provided in ZIP format, with images in PNG format and metadata in JSON format
- Requirements: the dataset requires no specific requirements or dependencies for use

## Data Quality

- Number of images: 9766
- Image sizes: vary, but all images are in PNG format
- Class balance: the distribution of classes in the dataset is not known
- Quality: the dataset has been carefully cleaned and filtered to remove low quality or irrelevant images

## Limitations

While the Pixiv Niji Journey dataset has been carefully cleaned and preprocessed to ensure high quality and consistency, it is important to be aware of certain limitations and biases that may be present in the dataset. Some potential limitations of the dataset include:

- Bias of the Pixiv platform: Pixiv is an online art platform that may have its own biases in terms of the content that is available and the users who contribute to it. This could potentially introduce biases into the dataset.

- Search term bias: The dataset was collected using the search term "nijijourney" on Pixiv, which may have introduced biases into the dataset depending on the popularity and prevalence of this term on the platform.

- Limited scope: The dataset only includes images scraped from Pixiv, and therefore may not be representative of a wider range of images or artistic styles.

- Potential errors or inconsistencies in the metadata: While every effort has been made to ensure the accuracy of the metadata, there may be errors or inconsistencies present in the data.

It is important to be aware of these limitations and to consider them when using the Pixiv Niji Journey dataset for research or other purposes.

## License

The Pixiv Niji Journey dataset is made available under the terms of the AGPL-3.0 license. This license is a copyleft license that allows users to freely use, modify, and distribute the dataset, as long as any modified versions are also made available under the same terms.

Under the terms of the AGPL-3.0 license, users are allowed to:
- Use the dataset for any purpose, commercial or non-commercial
- Modify the dataset as needed for their purposes
- Distribute copies of the dataset, either modified or unmodified

However, users must also follow the following conditions:
- Any modified versions of the dataset must be made available under the same AGPL-3.0 license
- If the dataset is used to provide a service to others (such as through a website or API), the source code for the service must be made available to users under the AGPL-3.0 license

It is important to carefully review the terms of the AGPL-3.0 license and ensure that you understand your rights and obligations when using the Pixiv Niji Journey dataset. 

## Citation

If you use this dataset in your work, please cite it as follows:
```
@misc{pixiv_niji_journey,
  author = {Linaqruf},
  title = {Pixiv Niji Journey},
  year = {2022},
  publisher = {Hugging Face},
  url = {https://huggingface.co/datasets/Linaqruf/pixiv-niji-journey},
}
```

