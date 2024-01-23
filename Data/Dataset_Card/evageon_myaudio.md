---
pretty_name: MGB2
alt_glob: []
alt_sep: ''
dataset_link: https://huggingface.co/datasets/malmarz/test_mgb2/resolve/main/mgb2.test.tar.gz
dataset_name: mgb2_speech
datasets_path: datasets
file_type: wav
header: null
hf_path: ''
json_key: null
label_column_name: ''
level: null
lines: false
local_dir: false
new_columns: ''
pal: false
skiprows: 0
squad: false
xml_columns: ''
dataset_info:
  features:
  - name: audio
    dtype: audio
  - name: transcription
    dtype: string
  splits:
  - name: test
    num_bytes: 384372257.17
    num_examples: 3890
  - name: train
    num_bytes: 1488884786.673
    num_examples: 15559
  download_size: 0
  dataset_size: 1873257043.8430002
---


Please note this dataset is private



### Using the data

You can stream the data data loader:

```python
myaudio = load_dataset(
    "evageon/myaudio",
    use_auth_token=os.environ["HG_USER_TOKEN"], # replace this with your access token
    streaming=True)
```

Then you can iterate over the dataset

```python
# replace test with validation or train depending on split you need
print(next(iter(myaudio["test"])))
```
outputs:
```
{'path': 'CD93A8FF-C3ED-4AD4-95A6-8363CCB93B90_spk-0001_seg-0024467:0025150.wav', 'audio': {'path': 'dataset/test/wav/CD93A8FF-C3ED-4AD4-95A6-8363CCB93B90_spk-0001_seg-0024467:0025150.wav', 'array': array([0.00662231, 0.00497437, 0.00518799, ..., 0.01150513, 0.00708008,
       0.00296021]), 'sampling_rate': 16000}, 'text': 'خطرا على دول الخليج لماذا اعتبرت أن إيران اليوم والخطر الذي تشكله إيران مختلف'}
```