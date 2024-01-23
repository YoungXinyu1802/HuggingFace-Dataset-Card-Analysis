# VietAI assignment: Vietnamese Inverse Text Normalization dataset

## Dataset Description

Inverse text normalization (ITN) is the task that transforms spoken to written styles. It is particularly useful in automatic speech recognition (ASR) systems where proper names are often miss-recognized by their pronunciations instead of the written forms. By applying ITN, we can improve the readability of the ASR system’s output significantly. This dataset provides data for doing ITN task in the Vietnamese language.

For example:

| Spoken                                           | Written      | Types                      |
|--------------------------------------------------|--------------|----------------------------|
| tám giờ chín phút ngày ba tháng tư năm hai nghìn | 8h9 3/4/2000 | time and date              |
| tám mét khối năm mươi ki lô gam                  | 8m3 50 kg    | number and unit of measure |
| không chín sáu hai bảy bảy chín chín không bốn   | 0962779904   | phone number               |


### Data Splits
The ITN dataset has 3 splits: _train_, _validation_, and _test_. In _train_, _validation_ splits, the input (src) and their label (tgt) are provided. In the _test_ splits, only the input (src) is provided.

| Dataset Split | Number of Instances in Split |
| ------------- |----------------------------- |
| Train         | 500,000                      |
| Validation    | 2,500                       |
| Test          | 2,500                       |

