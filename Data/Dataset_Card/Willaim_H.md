from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("bigscience/bloom")

model = AutoModel.from_pretrained("bigscience/bloom")