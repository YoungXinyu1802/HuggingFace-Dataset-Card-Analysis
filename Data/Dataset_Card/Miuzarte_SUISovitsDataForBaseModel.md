---
language:
- zh
tags:
- AIvtuber
- VirtuaReal
---
# 岁己SUI的sovits底模数据集

## Dataset Description

- **Homepage:** 
- **Repository:** 
- **Paper:** 
- **Leaderboard:** 
- **Point of Contact:** 

### Dataset Summary

#### ForBaseModel.zip：

数据质量不高，只用于岁己音色的底模训练（洗去G_0.pth和D_0.pth的音色）

采样频率为44.1kHz，使用前请注意预处理

取自岁己22年12月、23年1月的录播（除电台，共计211:13:21），经过以下步骤筛选处理

1. 挑取BGM音量较低的直播片段（20:39:21）_[[LowBGM.zip]](https://huggingface.co/datasets/Miuzarte/SUISovitsDataForBaseModel/blob/main/%E6%9C%89%E7%9A%84%E6%B2%A1%E7%9A%84/LowBGM.zip)

2. [UVR5](https://github.com/Anjok07/ultimatevocalremovergui) VR Architecture 5_HP-Karaoke-UVR统一处理，尽量除去了BGM中的人声（20:39:20，反正确实就是少了1s）_[[UVR-ed.zip]](https://huggingface.co/datasets/Miuzarte/SUISovitsDataForBaseModel/blob/main/%E6%9C%89%E7%9A%84%E6%B2%A1%E7%9A%84/UVR-ed.zip)

3. [Audio Slicer](https://github.com/flutydeer/audio-slicer)切片（12:45:29）_[[Slice-d.zip]](https://huggingface.co/datasets/Miuzarte/SUISovitsDataForBaseModel/blob/main/%E6%9C%89%E7%9A%84%E6%B2%A1%E7%9A%84/Slice-d.zip)

4. [Fish Audio Preprocessor](https://github.com/fishaudio/audio-preprocess)响度标准化并删除过短过长的片段（11:24:06）_[[LoudnessNorm-ed.zip]](https://huggingface.co/datasets/Miuzarte/SUISovitsDataForBaseModel/blob/main/%E6%9C%89%E7%9A%84%E6%B2%A1%E7%9A%84/LoudnessNorm-ed.zip)

5. [Spliter Wav by IceKyrin](https://github.com/IceKyrin)声纹识别稳定数据（06:47:46）_[[ForBaseModel.zip]](https://huggingface.co/datasets/Miuzarte/SUISovitsDataForBaseModel/blob/main/ForBaseModel.zip)

文件结构：

```
ForBaseModel.zip
├── 25788785-20221201-195959-658_01_(Vocals)_1.wav
├── 25788785-20221201-195959-658_01_(Vocals)_3.wav
├── ......
├── 25788785-20230201-005152-235_03_(Vocals)_9.wav
└── 25788785-20230201-005152-235_03_(Vocals)_10.wav
```

#### ForBaseModel_sovits3.0.zip：

ForBaseModel.zip经过预处理后的数据集，可以直接投入sovits3.0_48k使用，采样频率为48kHz

文件结构：

```
ForBaseModel_sovits3.0.zip
├── configs
│   └── config.json
├── dataset
│   └── 48k
│       └── suijiSUI
│           ├── 25788785-20221201-195959-658_01_(Vocals)_1.wav
│           ├── 25788785-20221201-195959-658_01_(Vocals)_1.wav.f0.npy
│           ├── 25788785-20221201-195959-658_01_(Vocals)_1.wav.soft.pt
│           ├── ......
│           ├── 25788785-20230201-005152-235_03_(Vocals)_10.wav
│           ├── 25788785-20230201-005152-235_03_(Vocals)_10.wav.f0.npy
│           └── 25788785-20230201-005152-235_03_(Vocals)_10.wav.soft.pt
└── filelists
    ├── test.txt
    ├── train.txt
    └── val.txt
```

#### ForBaseModel_sovits4.0.zip：

ForBaseModel.zip经过预处理后的数据集，可以直接投入sovits4.0使用，采样频率为44.1kHz

注意：4.0开始config.json中的batch_size默认为6，我又给改回12了

文件结构：

```
ForBaseModel_sovits4.0.zip
├── configs
│   └── config.json
├── dataset
│   └── 44k
│       └── suijiSUI
│           ├── 25788785-20221201-195959-658_01_(Vocals)_1.wav
│           ├── 25788785-20221201-195959-658_01_(Vocals)_1.wav.f0.npy
│           ├── 25788785-20221201-195959-658_01_(Vocals)_1.wav.soft.pt
│           ├── ......
│           ├── 25788785-20230201-005152-235_03_(Vocals)_10.wav
│           ├── 25788785-20230201-005152-235_03_(Vocals)_10.wav.f0.npy
│           └── 25788785-20230201-005152-235_03_(Vocals)_10.wav.soft.pt
└── filelists
    ├── test.txt
    ├── train.txt
    └── val.txt
```

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

Chinese(98%)

English(1%)

Japanese(1%)

[More Information Needed]

## Dataset Structure

### Data Instances

[More Information Needed]

### Data Fields

[More Information Needed]

### Data Splits

[More Information Needed]

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

[More Information Needed]

### Licensing Information

[More Information Needed]

### Citation Information

[More Information Needed]

### Contributions

[More Information Needed]