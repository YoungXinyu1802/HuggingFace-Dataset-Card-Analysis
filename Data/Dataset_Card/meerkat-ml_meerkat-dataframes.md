### imagenette-160px-facebook-convnext-tiny-224.mk.tar.gz

```python
data = mk.get("imagenette", version="160px")
df = 
mk.DataFrame.read("https://huggingface.co/datasets/meerkat-ml/meerkat-dataframes/resolve/main/imagenette-160px-facebook-convnext-tiny-224.mk.tar.gz")
df = data.merge(df[["img_id", "logits", "pred"]], on="img_id")
```
