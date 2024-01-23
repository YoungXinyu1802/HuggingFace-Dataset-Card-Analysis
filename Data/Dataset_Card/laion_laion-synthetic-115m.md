# laion-synthetic-115m

![](https://huggingface.co/datasets/laion/laion-synthetic-115m/resolve/main/figure_6.png)
This dataset is a version of [laion-400m](https://laion.ai/laion-400-open-dataset/) with filtering/replacement of noisy/inaccurate captions with captions generated via the BLIP model. Provided by salesforce in [BLIP](https://github.com/salesforce/BLIP). Modified to be compatible with `img2dataset` tool.

## Download captioned images

Note: you may want to change some of the keyword arguments depending on your specific needs.

```sh
# Download parquet file containing mapping of image-URL's -> captions
wget -c https://huggingface.co/datasets/laion/laion-synthetic-115m/resolve/main/laion_synthetic_filtered_large.parquet
pip install img2dataset
# Download as many URL's as possible into webdataset (tars of txt/jpg files). Can also specify `files` instead.
img2dataset laion_synthetic_filtered_large.parquet --image_size 320 --resize_mode 'keep_ratio' --caption_col 'caption'--input_format parquet --output_format webdataset

> Downloading starting now, check your bandwidth speed (with bwm-ng)your cpu (with htop), and your disk usage (with iotop)!
```