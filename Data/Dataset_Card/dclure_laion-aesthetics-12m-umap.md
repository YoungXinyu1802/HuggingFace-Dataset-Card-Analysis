---
annotations_creators: []
language:
- en
language_creators:
- found
license:
- mit
multilinguality:
- monolingual
pretty_name: laion-aesthetics-12m-umap
size_categories: []
source_datasets: []
tags:
- laion
- stable-diffuson
- text2img
task_categories: []
task_ids: []
---

# LAION-Aesthetics :: CLIP → UMAP

This dataset is a CLIP (text) → UMAP embedding of the [LAION-Aesthetics dataset](https://laion.ai/blog/laion-aesthetics/) - specifically the [`improved_aesthetics_6plus` version](https://huggingface.co/datasets/ChristophSchuhmann/improved_aesthetics_6plus), which filters the full dataset to images with scores of > 6 under the "aesthetic" filtering model.

Thanks LAION for this amazing corpus!

---

The dataset here includes coordinates for 3x separate UMAP fits using different values for the `n_neighbors` parameter - `10`, `30`, and `60` - which are broken out as separate columns with different suffixes:

- `n_neighbors=10` → (`x_nn10`, `y_nn10`)
- `n_neighbors=30` → (`x_nn30`, `y_nn30`)
- `n_neighbors=60` → (`x_nn60`, `y_nn60`)

### `nn10`

![nn10](https://user-images.githubusercontent.com/814168/189763846-efa9ecc9-3d57-469b-9d4e-02ddc1723265.jpg)

### `nn30`

![nn30](https://user-images.githubusercontent.com/814168/189763863-a67d4bb1-e043-48ec-8c5a-38dce960731b.jpg)

### `nn60`

(The version from [Twitter](https://twitter.com/clured/status/1565399157606580224).)

![nn60](https://user-images.githubusercontent.com/814168/189763872-5847cde5-e03b-45e1-a9be-d95966bc5ded.jpg)

## Pipeline

The script for producing this can be found here:

https://github.com/davidmcclure/loam-viz/blob/laion/laion.py

And is very simple - just using the `openai/clip-vit-base-patch32` model out-of-the-box to encode the text captions:

```python
@app.command()
def clip(
    src: str,
    dst: str,
    text_col: str = 'TEXT',
    limit: Optional[int] = typer.Option(None),
    batch_size: int = typer.Option(512),
):
    """Embed with CLIP."""
    df = pd.read_parquet(src)

    if limit:
        df = df.head(limit)

    tokenizer = CLIPTokenizerFast.from_pretrained('openai/clip-vit-base-patch32')
    model = CLIPTextModel.from_pretrained('openai/clip-vit-base-patch32')

    model = model.to(device)

    texts = df[text_col].tolist()

    embeds = []
    for batch in chunked_iter(tqdm(texts), batch_size):

        enc = tokenizer(
            batch,
            return_tensors='pt',
            padding=True,
            truncation=True,
        )

        enc = enc.to(device)

        with torch.no_grad():
            res = model(**enc)

        embeds.append(res.pooler_output.to('cpu'))

    embeds = torch.cat(embeds).numpy()

    np.save(dst, embeds)

    print(embeds.shape)
```

Then using `cuml.GaussianRandomProjection` to do an initial squeeze to 64d (which gets the embedding tensor small enough to fit onto a single GPU for the UMAP) -

```python
@app.command()
def random_projection(src: str, dst: str, dim: int = 64):
    """Random projection on an embedding matrix."""
    rmm.reinitialize(managed_memory=True)

    embeds = np.load(src)

    rp = cuml.GaussianRandomProjection(n_components=dim)
    embeds = rp.fit_transform(embeds)

    np.save(dst, embeds)
    print(embeds.shape)
```

And then `cuml.UMAP` to get from 64d -> 2d -

```python
@app.command()
def umap(
    df_src: str,
    embeds_src: str,
    dst: str,
    n_neighbors: int = typer.Option(30),
    n_epochs: int = typer.Option(1000),
    negative_sample_rate: int = typer.Option(20),
):
    """UMAP to 2d."""
    rmm.reinitialize(managed_memory=True)

    df = pd.read_parquet(df_src)

    embeds = np.load(embeds_src)

    embeds = embeds.astype('float16')

    print(embeds.shape)
    print(embeds.dtype)

    reducer = cuml.UMAP(
        n_neighbors=n_neighbors,
        n_epochs=n_epochs,
        negative_sample_rate=negative_sample_rate,
        verbose=True,
    )

    x = reducer.fit_transform(embeds)

    df['x'] = x[:,0]
    df['y'] = x[:,1]

    df.to_parquet(dst)
    print(df)
```