see [read_pyarrow.py](https://gist.github.com/csarron/df712e53c9e0dcaad4eb6843e7a3d51c#file-read_pyarrow-py) for how to read one pyarrow file.

example PyTorch dataset:

```python
from torch.utils.data import Dataset

class ImageCaptionArrowDataset(Dataset):
    def __init__(
        self,
        dataset_file,
        tokenizer,
    ):

        import pyarrow as pa

        data = [pa.ipc.open_file(pa.memory_map(f, "rb")).read_all() for f in glob.glob(dataset_file)]
        self.data = pa.concat_tables(data)
        # do other initialization, like init image preprocessing fn, 

    def __getitem__(self, index):
        # item_id = self.data["id"][index].as_py()
        text = self.data["text"][index].as_py() # get text
        if isinstance(text, list):
            text = random.choice(text)

        img_bytes = self.data["image"][index].as_py() # get image bytes
        
        # do some processing with image and text, return the features
        
        
        # img_feat = self.image_bytes_to_tensor(img_bytes)
        # inputs = self.tokenizer(
        #     text,
        #     padding="max_length",
        #     max_length=self.max_text_len,
        #     truncation=True,
        #     return_token_type_ids=True,
        #     return_attention_mask=True,
        #     add_special_tokens=True,
        #     return_tensors="pt",
        # )
        # input_ids = inputs.input_ids.squeeze(0)
        # attention_mask = inputs.attention_mask.squeeze(0)
        # return {
        #     # "item_ids": item_id,
        #     "text_ids": input_ids,
        #     "input_ids": input_ids,
        #     "text_masks": attention_mask,
        #     "pixel_values": img_feat,
        # }
    def __len__(self):
        return len(self.data)


```