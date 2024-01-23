# Dataset Card for Naruto BLIP captions

_Dataset used to train [TBD](TBD)._

The original images were obtained from [narutopedia.com](https://naruto.fandom.com/wiki/Narutopedia) and captioned with the [pre-trained BLIP model](https://github.com/salesforce/BLIP).

For each row the dataset contains `image` and `text` keys. `image` is a varying size PIL jpeg, and `text` is the accompanying text caption. Only a train split is provided.


## Example stable diffusion outputs

![pk1.jpg](https://staticassetbucket.s3.us-west-1.amazonaws.com/outputv2_grid.png)
> "Bill Gates with a hoodie", "John Oliver with Naruto style", "Hello Kitty with Naruto style", "Lebron James with a hat", "Mickael Jackson as a ninja", "Banksy Street art of ninja"

## Citation

If you use this dataset, please cite it as:

```
@misc{cervenka2022naruto2,
      author = {Cervenka, Eole},
      title = {Naruto BLIP captions},
      year={2022},
      howpublished= {\url{https://huggingface.co/datasets/lambdalabs/naruto-blip-captions/}}
} 
```