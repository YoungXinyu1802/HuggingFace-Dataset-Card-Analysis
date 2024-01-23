# VQGAN (f8, 8192) embeddings for LAION-100M

This dataset contains __VQGAN (f8, 8192)__ embeddings for the images
from the first ~100 million image-text pairs of the [LAION-400M dataset](https://laion.ai/laion-400-open-dataset/).
VQGAN was introduced in the paper
["Taming Transformers for High-Resolution Image Synthesis"](https://github.com/CompVis/taming-transformers)
and adopted for training [DALLE-mini](https://github.com/borisdayma/dalle-mini).

**Warning**: This large-scale dataset is non-curated. It was built for research purposes to enable testing model training on larger scale for broad researcher and other interested communities, and **is not meant for any real-world production or application.**

[VQGAN (f8, 8192)](https://github.com/CompVis/taming-transformers#overview-of-pretrained-models)
is a pretrained model with downsampling factor `f=8`, 8192 codebook entries, and Gumbel quantization.
We did not perform any fine-tuning and used the VQGAN wrapper from the [DALLE-pytorch](https://github.com/lucidrains/DALLE-pytorch) repository for inference. Since LAION-400M contains 256x256 images, the model produces 1024 codes for each image.

The data is provided as `*.parquet` files with the embeddings and meta information:

- The embeddings (`code` column) are represented as binary data that can be decoded
  using `np.frombuffer(data, np.int16).reshape(32, 32)`.
- The meta information (`caption`, `url`, and other columns) is the same as in the `*.parquet` files from LAION-400M
  (see description [here](https://laion.ai/laion-400-open-dataset/)).
- This dataset does not contain the original images.

The data corresponds to the shards `00000`, `00001`, ..., `09999` of LAION-400M.
0.07% of the shards were excluded since they were corrupted in the original dataset.

The LAION-400M dataset is distributed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).
The VQGAN models are distributed under the [MIT license](https://github.com/CompVis/taming-transformers/blob/master/License.txt).
