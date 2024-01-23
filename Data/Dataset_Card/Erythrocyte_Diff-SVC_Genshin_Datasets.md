---
tags:
- Diff-SVC
- Genshin
- Genshin Impact
- Voice Data
- Voice Dataset
---

# Genshin Datasets for Diff-SVC

## 仓库地址

|                            仓库                            |                            传送门                            |
| :--------------------------------------------------------: | :----------------------------------------------------------: |
|                          Diff-SVC                          |      [点此传送](https://github.com/prophesier/diff-svc)      |
|                       44.1KHz声码器                        |        [点此传送](https://openvpi.github.io/vocoders)        |
|                       原神语音数据集                       |      [点此传送](https://github.com/w4123/GenshinVoice)       |
| 训练用底模（如果想用这个数据集自己训练，非原神模型也可用） | [点此传送](https://huggingface.co/Erythrocyte/Diff-SVC_Pre-trained_Models) |
|         已训练原神 Diff-SVC 模型（可用于二创整活）         | [点此传送](https://huggingface.co/Erythrocyte/Diff-SVC_Genshin_Models) |

## 介绍

该数据集为训练 Diff-SVC 原神模型的数据集，上传的数据集均已进行 `长音频切割` 、`响度匹配`。可以 `直接用来预处理并训练`，由于每个角色数据集规模不够，训练时候建议配合 `预训练模型` 训练。预训练模型见上表，并且提供了 `详细的教程` 以及 `多种可选预训练模型`。

## 使用教程（以下操作均需要在Diff-SVC目录下进行）

### Windows平台

1. 下载自己需要的数据集

2. 解压到 Diff-SVC 根目录，如果提示覆盖，请直接覆盖。

4. 依次输入如下指令进行预处理

   ```bash
   set PYTHONPATH=.
   set CUDA_VISIBLE_DEVICES=0 
   python preprocessing/binarize.py --config training/config_nsf.yaml
   ```

5. 按照教程进行加载预训练模型并训练：

   教程地址：https://huggingface.co/Erythrocyte/Diff-SVC_Pre-trained_Models

### Linux平台

1. 输入如下命令下载需要的数据集（这里以纳西妲为例，其它角色可以从下表右击链接复制）

   ```bash
   wget https://huggingface.co/datasets/Erythrocyte/Diff-SVC_Genshin_Datasets/resolve/main/Sumeru/nahida.zip
   ```

2. 输入如下命令解压到 Diff-SVC 根目录，如果提示覆盖请输入 y

   ```bash
   unzip nahida.zip
   ```

4. 依次输入如下指令进行预处理

   ```bash
   export PYTHONPATH=.
   CUDA_VISIBLE_DEVICES=0 python preprocessing/binarize.py --config training/config_nsf.yaml
   ```

5. 按照教程进行加载预训练模型并训练：

   教程地址：https://huggingface.co/Erythrocyte/Diff-SVC_Pre-trained_Models

## 下载地址

| 地区 |    角色名    |                           下载地址                           |
| :--: | :----------: | :----------------------------------------------------------: |
| 蒙德 |     优菈     | [eula.zip](https://huggingface.co/datasets/Erythrocyte/Diff-SVC_Genshin_Datasets/resolve/main/Mondstadt/eula.zip) |
| 蒙德 |    阿贝多    | [albedo.zip](https://huggingface.co/datasets/Erythrocyte/Diff-SVC_Genshin_Datasets/resolve/main/Mondstadt/albedo.zip) |
| 蒙德 |     温迪     | [venti.zip](https://huggingface.co/datasets/Erythrocyte/Diff-SVC_Genshin_Datasets/resolve/main/Mondstadt/venti.zip) |
| 蒙德 |     莫娜     | [mona.zip](https://huggingface.co/datasets/Erythrocyte/Diff-SVC_Genshin_Datasets/resolve/main/Mondstadt/mona.zip) |
| 蒙德 |     可莉     | [klee.zip](https://huggingface.co/datasets/Erythrocyte/Diff-SVC_Genshin_Datasets/resolve/main/Mondstadt/klee.zip) |
| 蒙德 |      琴      | [jean.zip](https://huggingface.co/datasets/Erythrocyte/Diff-SVC_Genshin_Datasets/resolve/main/Mondstadt/jean.zip) |
| 蒙德 |    迪卢克    | [diluc.zip](https://huggingface.co/datasets/Erythrocyte/Diff-SVC_Genshin_Datasets/resolve/main/Mondstadt/diluc.zip) |
| 璃月 |     钟离     | [zhongli.zip](https://huggingface.co/datasets/Erythrocyte/Diff-SVC_Genshin_Datasets/resolve/main/Liyue/zhongli.zip) |
| 稻妻 |   雷电将军   | [raiden.zip](https://huggingface.co/datasets/Erythrocyte/Diff-SVC_Genshin_Datasets/resolve/main/Inazuma/raiden.zip) |
| 须弥 | 流浪者(散兵) | [wanderer.zip](https://huggingface.co/datasets/Erythrocyte/Diff-SVC_Genshin_Datasets/resolve/main/Sumeru/wanderer.zip) |
| 须弥 |    纳西妲    | [nahida.zip](https://huggingface.co/datasets/Erythrocyte/Diff-SVC_Genshin_Datasets/resolve/main/Sumeru/nahida.zip) |
