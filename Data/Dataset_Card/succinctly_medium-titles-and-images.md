---
license: apache-2.0
---
This dataset contains `<title, encoded_image>` pairs from [Medium](https://medium.com) articles. It was processed from the [Medium Articles Dataset (128k): Metadata + Images](https://www.kaggle.com/datasets/succinctlyai/medium-data) dataset on Kaggle.

The original images were processed in the following way:
1. Given an image of size `(w, h)`, we cropped a square of size `(n, n)` from the center of the image, where `n = min(w, h)`.
2. The resulting `(n, n)` image was resized to `(256, 256)`.
3. The resulting `(256, 256)` image was encoded into image tokens via the [dalle-mini/vqgan\_imagenet\_f16\_16384](https://huggingface.co/dalle-mini/vqgan_imagenet_f16_16384) model.

Note that this dataset contains ~128k entries and is too small for training a text-to-image model end to end; it is more suitable for operations on a pre-trained model 
 like [dalle-mini](https://huggingface.co/dalle-mini/dalle-mini) (fine-tuning, [prompt tuning](https://arxiv.org/pdf/2104.08691.pdf), etc.).