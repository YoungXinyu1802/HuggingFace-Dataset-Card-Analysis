---
language:
- zh
tags:
- AIvtuber
- VirtuaReal
---
# 岁己SUI的sovits歌声模型数据集

## Dataset Description

- **Homepage:** 
- **Repository:** 
- **Paper:** 
- **Leaderboard:** 
- **Point of Contact:** 

### Dataset Summary

#### ForSingingModel.zip：

数据质量一般，不建议用于diff-svc等对数据质量要求较高的项目

采样频率为44.1kHz，使用前请注意预处理

取自岁己22年12月、23年1月、23年2月1-17日的录播（除电台，共计268:07:43）、岁己的投稿、[A1in_sy](https://space.bilibili.com/89636742)11月及以前的歌切，经过以下步骤筛选处理

1. 挑取音频码率较高、伴奏音量较低、UVR可较干净去除伴奏的片段（09:31:44）_[[Usable.zip]](https://huggingface.co/datasets/Miuzarte/SUISovitsDataForSingingModel/blob/main/%E6%9C%89%E7%9A%84%E6%B2%A1%E7%9A%84/Usable.zip)

2. [UVR5](https://github.com/Anjok07/ultimatevocalremovergui) VR Architecture 3_HP-Vocal-UVR、4_HP-Vocal-UVR、5_HP-Karaoke-UVR分别处理，尽量除去了BGM中的人声、和声（09:31:43）

3. Adobe Audition手动修剪无用、瑕疵片段（06:58:14）_[[UVR-ed.zip]](https://huggingface.co/datasets/Miuzarte/SUISovitsDataForSingingModel/blob/main/%E6%9C%89%E7%9A%84%E6%B2%A1%E7%9A%84/UVR-ed.zip)

4. [Audio Slicer](https://github.com/flutydeer/audio-slicer)切片并删除过短过长的片段（06:08:52）_[[Slice-d.zip]](https://huggingface.co/datasets/Miuzarte/SUISovitsDataForSingingModel/blob/main/%E6%9C%89%E7%9A%84%E6%B2%A1%E7%9A%84/Slice-d.zip)

5. [Fish Audio Preprocessor](https://github.com/fishaudio/audio-preprocess)响度标准化（06:08:52）_[[ForSingingModel.zip]](https://huggingface.co/datasets/Miuzarte/SUISovitsDataForSingingModel/blob/main/ForSingingModel.zip)

文件结构：

```
ForSingingModel.zip
├── 1.wav
├── ......
├── 911.wav
├── 25788785-20221210-200143-856_01_(Vocals)_0_0.wav
├── ......
└── 25788785-20230217-230042-820_02_(Vocals)_13.wav
```

#### ForSingingModel_sovits3.0.zip：

ForSingingModel.zip经过预处理后的数据集，可以直接投入sovits3.0_48k使用，采样频率为48kHz

文件结构：

```
ForBaseModel_sovits.zip
├── configs
│   └── config.json
├── dataset
│   └── 48k
│       └── suijiSUI
│           ├── 1.wav
│           ├── 1.wav.f0.npy
│           ├── 1.wav.soft.pt
│           ├── ......
│           ├── 25788785-20230217-230042-820_02_(Vocals)_13.wav
│           ├── 25788785-20230217-230042-820_02_(Vocals)_13.wav.f0.npy
│           └── 25788785-20230217-230042-820_02_(Vocals)_13.wav.soft.pt
└── filelists
    ├── test.txt
    ├── train.txt
    └── val.txt
```

#### ForSingingModel_sovits4.0.zip：

ForSingingModel.zip经过预处理后的数据集，可以直接投入sovits4.0使用，采样频率为44.1kHz

注意：4.0开始config.json中的batch_size默认为6，我又给改回12了

文件结构：

```
ForBaseModel_sovits.zip
├── configs
│   └── config.json
├── dataset
│   └── 44k
│       └── suijiSUI
│           ├── 1.wav
│           ├── 1.wav.f0.npy
│           ├── 1.wav.soft.pt
│           ├── ......
│           ├── 25788785-20230217-230042-820_02_(Vocals)_13.wav
│           ├── 25788785-20230217-230042-820_02_(Vocals)_13.wav.f0.npy
│           └── 25788785-20230217-230042-820_02_(Vocals)_13.wav.soft.pt
└── filelists
    ├── test.txt
    ├── train.txt
    └── val.txt
```

用到的视频av号：
```
|迷幻慵懒浪漫氛围歌曲| 深夜卧室的氛围感-wait a minute _ av431181253
“整个夏天，想和你环游世界” 试图抓住夏天的尾巴 _ av984968322
3秒带你重回十年前，当年“血洗”qq空间的歌曲，你还记得吗 _ av815358458
3秒让你直呼老公！《I wanna be your slave》 _ av558796317
当我躺在床上摆烂时写的歌 _ av344838098
身体倒是很诚实呢 _ av221246263
试着像楪祈一样温柔地唱“Departures 〜献给你的爱之歌 〜”罪恶王冠ED _ av303334059
试着用治愈的声音唱了《ハレハレヤ》- 朗朗晴天 _ av345498614
【岁己】 366日 _ av561787823
【岁己】 City of Stars _ av561703608
【岁己】 Ghost of a smile _ av689168602
【岁己】 Mela! _ av346648893
【岁己】 Rainbow Girl _ av561705190
【岁己】 The Loneliest Girl _ av732870463
【岁己】 Zzz _ av562589180
【岁己】 ごはんはおかず / 米饭是菜 _ av732063178
【岁己】 たばこ / 烟草 _ av562079329
【岁己】 たばこ _ av473902821
【岁己】 カタオモイ / 单相思 _ av604002659
【岁己】 ギターと孤独と蒼い惑星 / 吉他与孤独与蓝色星球 _ av732714359
【岁己】 万物生 _ av304499468
【岁己】 与你有关 _ av902626120
【岁己】 你的猫咪 _ av346808966
【岁己】 光 _ av219087863
【岁己】 匆匆那年 _ av944906256
【岁己】 唯一 _ av902191203
【岁己】 大风吹 _ av944120506
【岁己】 小半 _ av219092542
【岁己】 左手指月 _ av816979713
【岁己】 干花 _ av773894772
【岁己】 心墙 _ av986376224
【岁己】 忘我 _ av388983298
【岁己】 想和你迎着台风去看海 _ av389690921
【岁己】 摇篮曲 _ av516342753
【岁己】 昨日青空 _ av817017904
【岁己】 暗号 _ av346525048
【岁己】 月牙湾 _ av901604367
【岁己】 有你的快乐 _ av689087340
【岁己】 杀死那个石家庄人 _ av732149102
【岁己】 歌舞伎町の女王 _ av262050432
【岁己】 残酷な天使のテーゼ _ av901194411
【岁己】 流年 _ av987548313
【岁己】 浴室 _ av561382034
【岁己】 理想情人 _ av520236739
【岁己】 白金DISCO _ av646240416
【岁己】 砂糖之歌与苦味舞步 _ av986766899
【岁己】 糸 _ av774272827
【岁己】 红豆 _ av816694580
【岁己】 致姗姗来迟的你 _ av520099130
【岁己】 若把你 _ av562184161
【岁己】 落日 _ av219066825
【岁己】 走马 _ av816599983
【岁己】 远旅休憩中的邂逅 _ av689278570
【岁己】 迷迭香 _ av901800711
【岁己】 逆光 _ av901580501
【岁己】 钻石裂痕 _ av558645765
【岁己】 香格里拉 _ av346809187
```

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

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