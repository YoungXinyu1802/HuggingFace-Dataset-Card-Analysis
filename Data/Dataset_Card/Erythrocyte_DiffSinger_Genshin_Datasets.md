---
tags:
- DiffSinger
- Genshin
- Genshin Impact
- Voice Data
- Voice Dataset
---

# Genshin Datasets for DiffSinger

## 仓库地址

|      仓库      |                      传送门                       |
| :------------: | :-----------------------------------------------: |
|   DiffSinger   | [点此传送](https://github.com/openvpi/DiffSinger) |
| 44.1KHz声码器  |  [点此传送](https://openvpi.github.io/vocoders)   |
| 原神语音数据集 | [点此传送](https://github.com/w4123/GenshinVoice) |

## 介绍

该数据集为训练 DiffSinger 原神声库的数据集，上传的数据集均已进行 `长音频切割` 、`响度匹配`。可以 `直接用来预处理并训练`，**该数据集仅可用于二次创作和训练模型，不得进行任何商业用途！该数据集所用的语音数据的所有权均归《原神》以及 米哈游 所有！**

## 使用教程

### Windows&Linux平台

1. 下载自己需要的数据集。
2. 按照压缩包里面给的 `train_cmd.txt` 的提示进行训练。

## 下载地址（不定时更新）

| 地区 |     角色名     |                           下载地址                           |                           备注                           |
| :--: | :------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
| 须弥 |      坎蒂丝      | [点我下载](https://huggingface.co/datasets/Erythrocyte/DiffSinger_Genshin_Datasets/resolve/main/candace.zip) | - |
| 须弥 |      柯莱      | [点我下载](https://huggingface.co/datasets/Erythrocyte/DiffSinger_Genshin_Datasets/resolve/main/collei.zip) | - |
| 须弥 |      赛诺     | [点我下载](https://huggingface.co/datasets/Erythrocyte/DiffSinger_Genshin_Datasets/resolve/main/cyno.zip) | - |
| 须弥 |      多莉      | [点我下载](https://huggingface.co/datasets/Erythrocyte/DiffSinger_Genshin_Datasets/resolve/main/dori.zip) | - |
| 须弥 |      珐露珊     | [点我下载](https://huggingface.co/datasets/Erythrocyte/DiffSinger_Genshin_Datasets/resolve/main/faruzan.zip) | 缺音素 |
| 须弥 |   莱依拉   | [点我下载](https://huggingface.co/datasets/Erythrocyte/DiffSinger_Genshin_Datasets/resolve/main/layla.zip) | - |
| 须弥 |   纳西妲   | [点我下载](https://huggingface.co/datasets/Erythrocyte/DiffSinger_Genshin_Datasets/resolve/main/nahida.zip) | - |
| 须弥 |     妮露     | [点我下载](https://huggingface.co/datasets/Erythrocyte/DiffSinger_Genshin_Datasets/resolve/main/nilou.zip) | - |
| 须弥 |     提纳里     | [点我下载](https://huggingface.co/datasets/Erythrocyte/DiffSinger_Genshin_Datasets/resolve/main/tighnari.zip) | - |
| 须弥 |     流浪者(散兵)     | [点我下载](https://huggingface.co/datasets/Erythrocyte/DiffSinger_Genshin_Datasets/resolve/main/wanderer.zip) | - |
> 注：缺音素的数据集只可在多说话人版DiffSinger和其他说话人一起训练，单独训练会报错