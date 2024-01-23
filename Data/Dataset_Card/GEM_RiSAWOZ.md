---
annotations_creators:
- crowd-sourced
language_creators:
- unknown
language:
- zh
license:
- cc-by-4.0
multilinguality:
- unknown
size_categories:
- unknown
source_datasets:
- original
task_categories:
- conversational
task_ids: []
pretty_name: RiSAWOZ
tags:
- dialog-response-generation
---

# Dataset Card for GEM/RiSAWOZ

## Dataset Description

- **Homepage:** https://terryqj0107.github.io/RiSAWOZ_webpage
- **Repository:** https://github.com/terryqj0107/RiSAWOZ
- **Paper:** https://aclanthology.org/2020.emnlp-main.67
- **Leaderboard:** N/A
- **Point of Contact:** Deyi Xiong

### Link to Main Data Card

You can find the main data card on the [GEM Website](https://gem-benchmark.com/data_cards/RiSAWOZ).

### Dataset Summary 

RiSAWOZ is a Chinese dialog dataset. It can be used to study various dialogue tasks, such as Dialogue State Tracking, Dialogue Context-to-Text Generation, Coreference Resolution and Unified Generative Ellipsis and Coreference Resolution.

You can load the dataset via:
```
import datasets
data = datasets.load_dataset('GEM/RiSAWOZ')
```
The data loader can be found [here](https://huggingface.co/datasets/GEM/RiSAWOZ).

#### website
[Website](https://terryqj0107.github.io/RiSAWOZ_webpage)

#### paper
[ACL Anthology](https://aclanthology.org/2020.emnlp-main.67)

#### authors
Jun Quan (Soochow University, Suzhou, China), Shian Zhang (Soochow University, Suzhou, China), Qian Cao(Soochow University, Suzhou, China), Zizhong Li (Tianjin University, Tianjin, China), Deyi Xiong (Tianjin University, Tianjin, China)

## Dataset Overview

### Where to find the Data and its Documentation

#### Webpage

<!-- info: What is the webpage for the dataset (if it exists)? -->
<!-- scope: telescope -->
[Website](https://terryqj0107.github.io/RiSAWOZ_webpage)

#### Download

<!-- info: What is the link to where the original dataset is hosted? -->
<!-- scope: telescope -->
[Github](https://github.com/terryqj0107/RiSAWOZ)

#### Paper

<!-- info: What is the link to the paper describing the dataset (open access preferred)? -->
<!-- scope: telescope -->
[ACL Anthology](https://aclanthology.org/2020.emnlp-main.67)

#### BibTex

<!-- info: Provide the BibTex-formatted reference for the dataset. Please use the correct published version (ACL anthology, etc.) instead of google scholar created Bibtex. -->
<!-- scope: microscope -->
```
@inproceedings{quan-etal-2020-risawoz,
    title = "{R}i{SAWOZ}: A Large-Scale Multi-Domain {W}izard-of-{O}z Dataset with Rich Semantic Annotations for Task-Oriented Dialogue Modeling",
    author = "Quan, Jun  and
      Zhang, Shian  and
      Cao, Qian  and
      Li, Zizhong  and
      Xiong, Deyi",
    booktitle = "Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.emnlp-main.67",
    pages = "930--940",
}
```

#### Contact Name

<!-- quick -->
<!-- info: If known, provide the name of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
Deyi Xiong

#### Contact Email

<!-- info: If known, provide the email of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
dyxiong@tju.edu.cn

#### Has a Leaderboard?

<!-- info: Does the dataset have an active leaderboard? -->
<!-- scope: telescope -->
no


### Languages and Intended Use

#### Multilingual?

<!-- quick -->
<!-- info: Is the dataset multilingual? -->
<!-- scope: telescope -->
no

#### Covered Dialects

<!-- info: What dialects are covered? Are there multiple dialects per language? -->
<!-- scope: periscope -->
Only Mandarin Chinese is covered in this dataset.

#### Covered Languages

<!-- quick -->
<!-- info: What languages/dialects are covered in the dataset? -->
<!-- scope: telescope -->
`Mandarin Chinese`

#### License

<!-- quick -->
<!-- info: What is the license of the dataset? -->
<!-- scope: telescope -->
cc-by-4.0: Creative Commons Attribution 4.0 International

#### Intended Use

<!-- info: What is the intended use of the dataset? -->
<!-- scope: microscope -->
RiSAWOZ can be used to support the study under various dialogue tasks, such as Natural Language Understanding, Dialogue State Tracking, Dialogue Context-to-Text Generation, Coreference Resolution and Unified Generative Ellipsis and Coreference Resolution.

#### Primary Task

<!-- info: What primary task does the dataset support? -->
<!-- scope: telescope -->
Dialog Response Generation

#### Communicative Goal

<!-- quick -->
<!-- info: Provide a short description of the communicative goal of a model trained for this task on this dataset. -->
<!-- scope: periscope -->
Generate system response given dialogue context across multiple domains.


### Credit

#### Curation Organization Type(s)

<!-- info: In what kind of organization did the dataset curation happen? -->
<!-- scope: telescope -->
`academic`

#### Curation Organization(s)

<!-- info: Name the organization(s). -->
<!-- scope: periscope -->
Soochow University and Tianjin University

#### Dataset Creators

<!-- info: Who created the original dataset? List the people involved in collecting the dataset and their affiliation(s). -->
<!-- scope: microscope -->
Jun Quan (Soochow University, Suzhou, China), Shian Zhang (Soochow University, Suzhou, China), Qian Cao(Soochow University, Suzhou, China), Zizhong Li (Tianjin University, Tianjin, China), Deyi Xiong (Tianjin University, Tianjin, China)

#### Funding

<!-- info: Who funded the data creation? -->
<!-- scope: microscope -->
the National Key Research and Development Project

#### Who added the Dataset to GEM?

<!-- info: Who contributed to the data card and adding the dataset to GEM? List the people+affiliations involved in creating this data card and who helped integrate this dataset into GEM. -->
<!-- scope: microscope -->
Tianhao Shen (Tianjin University, Tianjin, China), Chaobin You (Tianjin University, Tianjin, China), Deyi Xiong (Tianjin University, Tianjin, China)


### Dataset Structure

#### Data Fields

<!-- info: List and describe the fields present in the dataset. -->
<!-- scope: telescope -->
- gem_id (string): GEM-RiSAWOZ-{split}-{id}
- dialogue_id (string): dialogue ID
- goal (string): natural language descriptions of the user goal
- domains (list of strings): domains mentioned in current dialogue session
- dialogue (list of dicts): dialog turns and corresponding annotations. Each turn includes:
    - turn_id (int): turn ID
    - turn_domain (list of strings): domain mentioned in current turn
    - user_utterance (string): user utterance
    - system_utterance (string): system utterance
    - belief_state (dict): dialogue state, including:
        - inform slot-values (dict): the slots and corresponding values informed until current turn
        - turn_inform (dict): the slots and corresponding values informed in current turn
        - turn request (dict): the slots requested in current turn
    - user_actions (list of lists): user dialogue acts in current turn
    - user_actions (list of lists): system dialogue acts in current turn
    - db_results (list of strings): database search results
    - segmented_user_utterance (string): word segmentation result of user utterance
    - segmented_system_utterance (string): word segmentation result of system utterance

#### Example Instance

<!-- info: Provide a JSON formatted example of a typical instance in the dataset. -->
<!-- scope: periscope -->
```
[
    {
        "dialogue_id": "attraction_goal_4-63###6177",
        "goal": "attraction_goal_4-63: 你是苏州人，但不怎么出去玩。你朋友来苏州找你，你准备带他逛逛“水乡古镇”，你希望客服给你推荐个消费水平“中等”的地方。然后你要问清楚这地方“是否地铁直达”、“特点”、“门票价格”这些信息。最后，你要感谢客服的帮助，然后说再见。",
        "domains": [
            "旅游景点"
        ],
        "dialogue": [
            {
                "turn_id": 0,
                "turn_domain": [
                    "旅游景点"
                ],
                "user_utterance": "你好，我是苏州人，但是不怎么出去玩，我朋友来苏州找我了，我准备带他逛逛水乡古镇，你能帮我推荐一下吗？",
                "system_utterance": "推荐您去周庄古镇。",
                "belief_state": {
                    "inform slot-values": {
                        "旅游景点-景点类型": "水乡 古镇"
                    },
                    "turn_inform": {
                        "旅游景点-景点类型": "水乡 古镇"
                    },
                    "turn request": []
                },
                "user_actions": [
                    [
                        "Inform",
                        "旅游景点",
                        "景点类型",
                        "水乡 古镇"
                    ],
                    [
                        "Greeting",
                        "旅游景点",
                        "",
                        ""
                    ]
                ],
                "system_actions": [
                    [
                        "Recommend",
                        "旅游景点",
                        "名称",
                        "周庄 古镇"
                    ]
                ],
                "db_results": [
                    "数据库检索结果：成功匹配个数为8",
                    "{'名称': '周庄古镇', '区域': '昆山', '景点类型': '水乡古镇', '最适合人群': '朋友出游', '消费': '偏贵', '是否地铁直达': '否', '门票价格': '100元', '电话号码': '400-8282900', '地址': '苏州市昆山市周庄镇全福路43号', '评分': 4.5, '开放时间': '07:30-18:50', '特点': '小桥流水与人家，双桥水巷摇橹船，还有沈万三的足迹待你寻访'}",
                    "{'名称': '同里古镇', '区域': '吴江', '景点类型': '水乡古镇', '最适合人群': '朋友出游', '消费': '偏贵', '是否地铁直达': '否', '门票价格': '100元', '电话号码': '0512-63325728', '地址': '苏州市吴江区同里古镇', '评分': 4.5, '开放时间': '07:30-17:30', '特点': '五湖环抱的江南水乡古镇，走三桥，参观小巧精致的园林退思园。'}",
                    "{'名称': '山塘街', '区域': '姑苏区', '景点类型': '水乡古镇', '最适合人群': '情侣约会', '消费': '中等', '是否地铁直达': '是', '门票价格': '免费', '电话号码': '0512-65314467', '地址': '苏州市姑苏区古城西北', '评分': 4.5, '开放时间': '08:30-21:00', '特点': '欣赏苏州老城风貌，参观会馆等古迹，乘游船，拍摄美丽的夜景。'}",
                    "{'名称': '平江路', '区域': '姑苏区', '景点类型': '水乡古镇', '最适合人群': '情侣约会', '消费': '中等', '是否地铁直达': '是', '门票价格': '免费', '电话号码': '0512-69163907', '地址': '江苏省苏州市姑苏区白塔东路65号', '评分': 4.5, '开放时间': '全天', '特点': '漫步保存完整的古街区，看小桥流水古宅，逛文艺小店，吃美食。'}",
                    "{'名称': '木渎古镇', '区域': '吴中区', '景点类型': '水乡古镇', '最适合人群': '朋友出游', '消费': '便宜', '是否地铁直达': '否', '门票价格': '免费', '电话号码': '0512-66514042', '地址': '苏州市吴中区木渎镇山塘街188号', '评分': 4.4, '开放时间': '08:30-17:00', '特点': '以园林为特色的古镇，游严家花园等古典园林，坐船看小桥流水。'}",
                    "{'名称': '甪直古镇', '区域': '吴中区', '景点类型': '水乡古镇', '最适合人群': '朋友出游', '消费': '便宜', '是否地铁直达': '否', '门票价格': '免费', '电话号码': '0512-66191668', '地址': '苏州市吴中区甪直镇晓市路21号', '评分': 4.3, '开放时间': '07:30-17:30', '特点': '甪直古镇有2500多年历史，甪直境内水流纵横，桥梁密布，有五湖之厅、六泽之冲之称。'}",
                    "{'名称': '千灯古镇', '区域': '昆山', '景点类型': '水乡古镇', '最适合人群': '朋友出游', '消费': '便宜', '是否地铁直达': '否', '门票价格': '免费', '电话号码': '0512-57472155', '地址': '苏州市昆山市千灯古镇尚书路1号', '评分': 4.3, '开放时间': '08:00-17:00', '特点': '千灯古镇，距今已有2500多年的历史，古镇白墙黑瓦，昆韵盎然。'}",
                    "{'名称': '锦溪古镇', '区域': '昆山', '景点类型': '水乡古镇', '最适合人群': '朋友出游', '消费': '中等', '是否地铁直达': '否', '门票价格': '65元', '电话号码': '0512-57224669', '地址': '苏州市昆山市锦溪镇邵甸港路18号', '评分': 4.4, '开放时间': '08:00-17:00', '特点': '锦溪古镇位于昆山南郊的淀山湖畔，是一座有千年历史的江南水乡。'}"
                ],
                "segmented_user_utterance": "你好 ， 我 是 苏州人 ， 但是 不怎么 出去玩 ， 我 朋友 来 苏州 找 我 了 ， 我 准备 带 他 逛逛 水乡 古镇 ， 你 能 帮 我 推荐 一下 吗 ？",
                "segmented_system_utterance": "推荐 您 去 周庄 古镇 。"
            },
            {
                "turn_id": 1,
                "turn_domain": [
                    "旅游景点"
                ],
                "user_utterance": "我希望这个地方消费水平适中的，这个是中等的吗？",
                "system_utterance": "这个不是，我又重新帮您找了一家山塘街。",
                "belief_state": {
                    "inform slot-values": {
                        "旅游景点-景点类型": "水乡 古镇",
                        "旅游景点-消费": "中等"
                    },
                    "turn_inform": {
                        "旅游景点-消费": "中等"
                    },
                    "turn request": []
                },
                "user_actions": [
                    [
                        "Inform",
                        "旅游景点",
                        "消费",
                        "中等"
                    ]
                ],
                "system_actions": [
                    [
                        "Recommend",
                        "旅游景点",
                        "名称",
                        "山塘 街"
                    ]
                ],
                "db_results": [
                    "数据库检索结果：成功匹配个数为3",
                    "{'名称': '山塘街', '区域': '姑苏区', '景点类型': '水乡古镇', '最适合人群': '情侣约会', '消费': '中等', '是否地铁直达': '是', '门票价格': '免费', '电话号码': '0512-65314467', '地址': '苏州市姑苏区古城西北', '评分': 4.5, '开放时间': '08:30-21:00', '特点': '欣赏苏州老城风貌，参观会馆等古迹，乘游船，拍摄美丽的夜景。'}",
                    "{'名称': '平江路', '区域': '姑苏区', '景点类型': '水乡古镇', '最适合人群': '情侣约会', '消费': '中等', '是否地铁直达': '是', '门票价格': '免费', '电话号码': '0512-69163907', '地址': '江苏省苏州市姑苏区白塔东路65号', '评分': 4.5, '开放时间': '全天', '特点': '漫步保存完整的古街区，看小桥流水古宅，逛文艺小店，吃美食。'}",
                    "{'名称': '锦溪古镇', '区域': '昆山', '景点类型': '水乡古镇', '最适合人群': '朋友出游', '消费': '中等', '是否地铁直达': '否', '门票价格': '65元', '电话号码': '0512-57224669', '地址': '苏州市昆山市锦溪镇邵甸港路18号', '评分': 4.4, '开放时间': '08:00-17:00', '特点': '锦溪古镇位于昆山南郊的淀山湖畔，是一座有千年历史的江南水乡。'}"
                ],
                "segmented_user_utterance": "我 希望 这个 地方 消费水平 适中 的 ， 这个 是 中等 的 吗 ？",
                "segmented_system_utterance": "这个 不是 ， 我 又 重新 帮 您 找 了 一家 山塘 街 。"
            },
            {
                "turn_id": 2,
                "turn_domain": [
                    "旅游景点"
                ],
                "user_utterance": "听这地方应该挺好玩，他们家特点是什么？",
                "system_utterance": "特点是欣赏苏州老城风貌，参观会馆等古迹，乘游船，拍摄美丽的夜景。",
                "belief_state": {
                    "inform slot-values": {
                        "旅游景点-景点类型": "水乡 古镇",
                        "旅游景点-消费": "中等",
                        "旅游景点-名称": "山塘 街"
                    },
                    "turn_inform": {
                        "旅游景点-名称": "山塘 街"
                    },
                    "turn request": [
                        "特点"
                    ]
                },
                "user_actions": [
                    [
                        "Inform",
                        "旅游景点",
                        "名称",
                        "山塘 街"
                    ],
                    [
                        "Request",
                        "旅游景点",
                        "特点",
                        ""
                    ]
                ],
                "system_actions": [
                    [
                        "Inform",
                        "旅游景点",
                        "特点",
                        "欣赏 苏州 老城 风貌 ， 参观 会馆 等 古迹 ， 乘 游船 ， 拍摄 美丽 的 夜景"
                    ]
                ],
                "db_results": [
                    "数据库检索结果：成功匹配个数为1",
                    "{'名称': '山塘街', '区域': '姑苏区', '景点类型': '水乡古镇', '最适合人群': '情侣约会', '消费': '中等', '是否地铁直达': '是', '门票价格': '免费', '电话号码': '0512-65314467', '地址': '苏州市姑苏区古城西北', '评分': 4.5, '开放时间': '08:30-21:00', '特点': '欣赏苏州老城风貌，参观会馆等古迹，乘游船，拍摄美丽的夜景。'}"
                ],
                "segmented_user_utterance": "听 这 地方 应该 挺好玩 ， 他们 家 特点 是 什么 ？",
                "segmented_system_utterance": "特点 是 欣赏 苏州 老城 风貌 ， 参观 会馆 等 古迹 ， 乘 游船 ， 拍摄 美丽 的 夜景 。"
            },
            {
                "turn_id": 3,
                "turn_domain": [
                    "旅游景点"
                ],
                "user_utterance": "听起来很不错，他们家门票是多少？",
                "system_utterance": "门票免费。",
                "belief_state": {
                    "inform slot-values": {
                        "旅游景点-景点类型": "水乡 古镇",
                        "旅游景点-消费": "中等",
                        "旅游景点-名称": "山塘 街"
                    },
                    "turn_inform": {},
                    "turn request": [
                        "门票价格"
                    ]
                },
                "user_actions": [
                    [
                        "Request",
                        "旅游景点",
                        "门票价格",
                        ""
                    ]
                ],
                "system_actions": [
                    [
                        "Inform",
                        "旅游景点",
                        "门票价格",
                        "免费"
                    ]
                ],
                "db_results": [
                    "数据库检索结果：成功匹配个数为1",
                    "{'名称': '山塘街', '区域': '姑苏区', '景点类型': '水乡古镇', '最适合人群': '情侣约会', '消费': '中等', '是否地铁直达': '是', '门票价格': '免费', '电话号码': '0512-65314467', '地址': '苏州市姑苏区古城西北', '评分': 4.5, '开放时间': '08:30-21:00', '特点': '欣赏苏州老城风貌，参观会馆等古迹，乘游船，拍摄美丽的夜景。'}"
                ],
                "segmented_user_utterance": "听 起来 很 不错 ， 他们 家 门票 是 多少 ？",
                "segmented_system_utterance": "门票 免费 。"
            },
            {
                "turn_id": 4,
                "turn_domain": [
                    "旅游景点"
                ],
                "user_utterance": "还行，那他们家是否有地铁直达呢？",
                "system_utterance": "嗯嗯，可以地铁直达。",
                "belief_state": {
                    "inform slot-values": {
                        "旅游景点-景点类型": "水乡 古镇",
                        "旅游景点-消费": "中等",
                        "旅游景点-名称": "山塘 街"
                    },
                    "turn_inform": {},
                    "turn request": [
                        "是否地铁直达"
                    ]
                },
                "user_actions": [
                    [
                        "Request",
                        "旅游景点",
                        "是否地铁直达",
                        ""
                    ]
                ],
                "system_actions": [
                    [
                        "Inform",
                        "旅游景点",
                        "是否地铁直达",
                        "是"
                    ]
                ],
                "db_results": [
                    "数据库检索结果：成功匹配个数为1",
                    "{'名称': '山塘街', '区域': '姑苏区', '景点类型': '水乡古镇', '最适合人群': '情侣约会', '消费': '中等', '是否地铁直达': '是', '门票价格': '免费', '电话号码': '0512-65314467', '地址': '苏州市姑苏区古城西北', '评分': 4.5, '开放时间': '08:30-21:00', '特点': '欣赏苏州老城风貌，参观会馆等古迹，乘游船，拍摄美丽的夜景。'}"
                ],
                "segmented_user_utterance": "还 行 ， 那 他们 家 是否 有 地铁 直达 呢 ？",
                "segmented_system_utterance": "嗯 嗯 ， 可以 地铁 直达 。"
            },
            {
                "turn_id": 5,
                "turn_domain": [
                    "通用"
                ],
                "user_utterance": "谢谢你的帮助，再见！",
                "system_utterance": "再见。",
                "belief_state": {
                    "inform slot-values": {
                        "旅游景点-景点类型": "水乡 古镇",
                        "旅游景点-消费": "中等",
                        "旅游景点-名称": "山塘 街"
                    },
                    "turn_inform": {},
                    "turn request": []
                },
                "user_actions": [
                    [
                        "Bye",
                        "通用",
                        "",
                        ""
                    ]
                ],
                "system_actions": [
                    [
                        "Bye",
                        "通用",
                        "",
                        ""
                    ]
                ],
                "db_results": [],
                "segmented_user_utterance": "谢谢 你 的 帮助 ， 再见 ！",
                "segmented_system_utterance": "再见 。"
            }
        ]
    },
    {
        "dialogue_id": "attraction_goal_3-33_v2###7307",
        "goal": "attraction_goal_3-33: 你和朋友一起来苏州出差，顺便想去“苏州乐园森林水世界”逛一逛。因此，你要询问客服这个地方“是否地铁直达”、“评分”、“特点”这些信息。最后，你向客服表示感谢，结束对话。",
        "domains": [
            "旅游景点"
        ],
        "dialogue": [
            {
                "turn_id": 0,
                "turn_domain": [
                    "旅游景点"
                ],
                "user_utterance": "你好，我和朋友一起来苏州出差，顺便想去苏州乐园森林水世界玩玩，能否帮我看看这个地方是否有地铁直达呢？",
                "system_utterance": "稍等，很抱歉，没有地铁能直接到这个景点呢。",
                "belief_state": {
                    "inform slot-values": {
                        "旅游景点-名称": "苏州 乐园 森林 水 世界"
                    },
                    "turn_inform": {
                        "旅游景点-名称": "苏州 乐园 森林 水 世界"
                    },
                    "turn request": [
                        "是否地铁直达"
                    ]
                },
                "user_actions": [
                    [
                        "Inform",
                        "旅游景点",
                        "名称",
                        "苏州 乐园 森林 水 世界"
                    ],
                    [
                        "Request",
                        "旅游景点",
                        "是否地铁直达",
                        ""
                    ],
                    [
                        "Greeting",
                        "旅游景点",
                        "",
                        ""
                    ]
                ],
                "system_actions": [
                    [
                        "Inform",
                        "旅游景点",
                        "是否地铁直达",
                        "否"
                    ]
                ],
                "db_results": [
                    "数据库检索结果：成功匹配个数为1",
                    "{'名称': '苏州乐园森林水世界', '区域': '高新区', '景点类型': '游乐场', '最适合人群': '情侣约会', '消费': '偏贵', '是否地铁直达': '否', '门票价格': '198元', '电话号码': '0512-68717107', '地址': '苏州市高新区阳山东路以西，山神湾路以东', '评分': 4.4, '开放时间': '09:00-17:00', '特点': '各项水上娱乐项目皆具森林特色，被赋予森林主题，让人身处浩瀚森林又能享受到海洋般的舒爽水游乐。'}"
                ],
                "segmented_user_utterance": "你好 ， 我 和 朋友 一 起来 苏州 出差 ， 顺便 想 去 苏州 乐园 森林 水 世界 玩玩 ， 能否 帮 我 看看 这个 地方 是否 有 地铁 直达 呢 ？",
                "segmented_system_utterance": "稍 等 ， 很 抱歉 ， 没有 地铁 能 直接 到 这个 景点 呢 。"
            },
            {
                "turn_id": 1,
                "turn_domain": [
                    "旅游景点"
                ],
                "user_utterance": "你再帮我看看景点的评分好吗？",
                "system_utterance": "这个景点的评分是4.4分。",
                "belief_state": {
                    "inform slot-values": {
                        "旅游景点-名称": "苏州 乐园 森林 水 世界"
                    },
                    "turn_inform": {},
                    "turn request": [
                        "评分"
                    ]
                },
                "user_actions": [
                    [
                        "Request",
                        "旅游景点",
                        "评分",
                        ""
                    ]
                ],
                "system_actions": [
                    [
                        "Inform",
                        "旅游景点",
                        "评分",
                        "4.4"
                    ]
                ],
                "db_results": [
                    "数据库检索结果：成功匹配个数为1",
                    "{'名称': '苏州乐园森林水世界', '区域': '高新区', '景点类型': '游乐场', '最适合人群': '情侣约会', '消费': '偏贵', '是否地铁直达': '否', '门票价格': '198元', '电话号码': '0512-68717107', '地址': '苏州市高新区阳山东路以西，山神湾路以东', '评分': 4.4, '开放时间': '09:00-17:00', '特点': '各项水上娱乐项目皆具森林特色，被赋予森林主题，让人身处浩瀚森林又能享受到海洋般的舒爽水游乐。'}"
                ],
                "segmented_user_utterance": "你 再 帮 我 看看 景点 的 评分 好 吗 ？",
                "segmented_system_utterance": "这个 景点 的 评分 是 4.4 分 。"
            },
            {
                "turn_id": 2,
                "turn_domain": [
                    "旅游景点"
                ],
                "user_utterance": "这个景点有啥特点呢？",
                "system_utterance": "这个景点的特点是各项水上娱乐项目皆具森林特色，被赋予森林主题，让人身处浩瀚森林又能享受到海洋般的舒爽水游乐。",
                "belief_state": {
                    "inform slot-values": {
                        "旅游景点-名称": "苏州 乐园 森林 水 世界"
                    },
                    "turn_inform": {},
                    "turn request": [
                        "特点"
                    ]
                },
                "user_actions": [
                    [
                        "Request",
                        "旅游景点",
                        "特点",
                        ""
                    ]
                ],
                "system_actions": [
                    [
                        "Inform",
                        "旅游景点",
                        "特点",
                        "各项 水上 娱乐 项目 皆 具 森林 特色 ， 被 赋予 森林 主题 ， 让 人 身处 浩瀚 森林 又 能 享受 到 海洋 般的 舒爽 水 游乐 。"
                    ]
                ],
                "db_results": [
                    "数据库检索结果：成功匹配个数为1",
                    "{'名称': '苏州乐园森林水世界', '区域': '高新区', '景点类型': '游乐场', '最适合人群': '情侣约会', '消费': '偏贵', '是否地铁直达': '否', '门票价格': '198元', '电话号码': '0512-68717107', '地址': '苏州市高新区阳山东路以西，山神湾路以东', '评分': 4.4, '开放时间': '09:00-17:00', '特点': '各项水上娱乐项目皆具森林特色，被赋予森林主题，让人身处浩瀚森林又能享受到海洋般的舒爽水游乐。'}"
                ],
                "segmented_user_utterance": "这个 景点 有 啥 特点 呢 ？",
                "segmented_system_utterance": "这个 景点 的 特点 是 各项 水上 娱乐 项目 皆 具 森林 特色 ， 被 赋予 森林 主题 ， 让 人 身处 浩瀚 森林 又 能 享受 到 海洋 般的 舒爽 水 游乐 。"
            },
            {
                "turn_id": 3,
                "turn_domain": [
                    "通用"
                ],
                "user_utterance": "太好了，我觉得我会很喜欢这个地方，哈哈。",
                "system_utterance": "这个景点挺不错的，就是没有地铁需要您乘坐其它交通工具了。",
                "belief_state": {
                    "inform slot-values": {
                        "旅游景点-名称": "苏州 乐园 森林 水 世界"
                    },
                    "turn_inform": {},
                    "turn request": []
                },
                "user_actions": [
                    [
                        "General",
                        "通用",
                        "",
                        ""
                    ]
                ],
                "system_actions": [
                    [
                        "General",
                        "通用",
                        "",
                        ""
                    ]
                ],
                "db_results": [],
                "segmented_user_utterance": "太好了 ， 我 觉得 我会 很 喜欢 这个 地方 ， 哈哈 。",
                "segmented_system_utterance": "这个 景点 挺不错 的 ， 就是 没有 地铁 需要 您 乘坐 其它 交通工具 了 。"
            },
            {
                "turn_id": 4,
                "turn_domain": [
                    "通用"
                ],
                "user_utterance": "我打出租车去吧，就是多花点车费，没事。",
                "system_utterance": "请问您还有其他问题吗？",
                "belief_state": {
                    "inform slot-values": {
                        "旅游景点-名称": "苏州 乐园 森林 水 世界"
                    },
                    "turn_inform": {},
                    "turn request": []
                },
                "user_actions": [
                    [
                        "General",
                        "通用",
                        "",
                        ""
                    ]
                ],
                "system_actions": [
                    [
                        "General",
                        "通用",
                        "",
                        ""
                    ]
                ],
                "db_results": [],
                "segmented_user_utterance": "我 打 出租车 去 吧 ， 就是 多花点 车费 ， 没事 。",
                "segmented_system_utterance": "请问 您 还有 其他 问题 吗 ？"
            },
            {
                "turn_id": 5,
                "turn_domain": [
                    "通用"
                ],
                "user_utterance": "没有了。谢谢你，再见。",
                "system_utterance": "再见。",
                "belief_state": {
                    "inform slot-values": {
                        "旅游景点-名称": "苏州 乐园 森林 水 世界"
                    },
                    "turn_inform": {},
                    "turn request": []
                },
                "user_actions": [
                    [
                        "Bye",
                        "通用",
                        "",
                        ""
                    ]
                ],
                "system_actions": [
                    [
                        "Bye",
                        "通用",
                        "",
                        ""
                    ]
                ],
                "db_results": [],
                "segmented_user_utterance": "没有 了 。 谢谢 你 ， 再见 。",
                "segmented_system_utterance": "再见 。"
            }
        ]
    }
]
```

#### Data Splits

<!-- info: Describe and name the splits in the dataset if there are more than one. -->
<!-- scope: periscope -->
- Train:
    - dialogues: 10000
    - turns: 134580
    - Avg. turns: 13.5
- Valid:
    - dialogues: 600
    - turns: 8116
    - Avg. turns: 13.5
- Test:
    - dialogues: 600
    - turn: 9286
    - Avg. turns: 15.5

#### 

<!-- info: What does an outlier of the dataset in terms of length/perplexity/embedding look like? -->
<!-- scope: microscope -->
the most complex example (i.e. with the most domains):
```
{
    "dialogue_id": "attraction_restaurant_hotel_goal_2-69_v2###8355",
    "goal": "attraction_restaurant_hotel_goal_2-69: 公司派你去苏州出差，你准备抽空旅游一下。第一，你想去一个“山水景区”，消费水平最好是“偏贵”的，你需要问清楚这地方“开放时间”、“门票价格”这些信息。第二，你要找个地方住，让客服给你推荐一家价位“中等”的“商务出行”酒店，并且询问这家酒店的“停车场”、“电话号码”这些信息。第三，你还想拔草美食，问客服有没有价位“中等”的“江浙菜”餐厅推荐，然后了解这家餐厅的“是否地铁直达”、“人均消费”这些信息。最后你要感谢客服的帮助，并说再见。",
    "domains": [
        "旅游景点",
        "餐厅",
        "酒店"
    ],
    "dialogue": [
        {
            "turn_id": 0,
            "turn_domain": [
                "旅游景点"
            ],
            "user_utterance": "你好，来苏州出差，准备抽空旅游一下。我想去山水景区，消费水平偏贵点，帮忙推荐一个。",
            "system_utterance": "你好，向您推荐金鸡湖景区，感受一下苏州现代化的一面。",
            "belief_state": {
                "inform slot-values": {
                    "旅游景点-景点类型": "山水 景区",
                    "旅游景点-消费": "偏贵"
                },
                "turn_inform": {
                    "旅游景点-景点类型": "山水 景区",
                    "旅游景点-消费": "偏贵"
                },
                "turn request": []
            },
            "user_actions": [
                [
                    "Inform",
                    "旅游景点",
                    "景点类型",
                    "山水 景区"
                ],
                [
                    "Inform",
                    "旅游景点",
                    "消费",
                    "偏贵"
                ],
                [
                    "Greeting",
                    "旅游景点",
                    "",
                    ""
                ],
                [
                    "General",
                    "旅游景点",
                    "",
                    ""
                ]
            ],
            "system_actions": [
                [
                    "Greeting",
                    "通用",
                    "",
                    ""
                ],
                [
                    "General",
                    "通用",
                    "",
                    ""
                ],
                [
                    "Recommend",
                    "旅游景点",
                    "名称",
                    "金鸡湖 景区"
                ]
            ],
            "db_results": [
                "数据库检索结果：成功匹配个数为2",
                "{'名称': '金鸡湖景区', '区域': '工业园区', '景点类型': '山水景区', '最适合人群': '情侣约会', '消费': '偏贵', '是否地铁直达': '是', '门票价格': '免费', '电话号码': '400-7558558', '地址': '苏州市工业园区星港街158号', '评分': 4.5, '开放时间': '全天', '特点': '看东方之门等高楼，坐摩天轮，乘船夜游，感受苏州现代化的一面。'}",
                "{'名称': '沙家浜风景区', '区域': '常熟', '景点类型': '山水景区', '最适合人群': '家庭亲子', '消费': '偏贵', '是否地铁直达': '否', '门票价格': '110元', '电话号码': '0512-52500000', '地址': '苏州市常熟市沙家浜镇', '评分': 4.5, '开放时间': '08:00-16:30', '特点': '京剧样板戏《沙家浜》的发源地，访剧中场景，坐船深入芦苇荡。'}"
            ],
            "segmented_user_utterance": "你好 ， 来 苏州 出差 ， 准备 抽空 旅游 一下 。 我 想 去 山水 景区 ， 消费水平 偏 贵点 ， 帮忙 推荐 一个 。",
            "segmented_system_utterance": "你好 ， 向 您 推荐 金鸡湖 景区 ， 感受一下 苏州 现代化 的 一面 。"
        },
        {
            "turn_id": 1,
            "turn_domain": [
                "旅游景点"
            ],
            "user_utterance": "这里开放时间？需要安排一下。",
            "system_utterance": "景区是全天开放的，可以尽情游览！",
            "belief_state": {
                "inform slot-values": {
                    "旅游景点-景点类型": "山水 景区",
                    "旅游景点-消费": "偏贵",
                    "旅游景点-名称": "金鸡湖 景区"
                },
                "turn_inform": {
                    "旅游景点-名称": "金鸡湖 景区"
                },
                "turn request": [
                    "开放时间"
                ]
            },
            "user_actions": [
                [
                    "Inform",
                    "旅游景点",
                    "名称",
                    "金鸡湖 景区"
                ],
                [
                    "Request",
                    "旅游景点",
                    "开放时间",
                    ""
                ],
                [
                    "General",
                    "旅游景点",
                    "",
                    ""
                ]
            ],
            "system_actions": [
                [
                    "Inform",
                    "旅游景点",
                    "开放时间",
                    "全天"
                ]
            ],
            "db_results": [
                "数据库检索结果：成功匹配个数为1",
                "{'名称': '金鸡湖景区', '区域': '工业园区', '景点类型': '山水景区', '最适合人群': '情侣约会', '消费': '偏贵', '是否地铁直达': '是', '门票价格': '免费', '电话号码': '400-7558558', '地址': '苏州市工业园区星港街158号', '评分': 4.5, '开放时间': '全天', '特点': '看东方之门等高楼，坐摩天轮，乘船夜游，感受苏州现代化的一面。'}"
            ],
            "segmented_user_utterance": "这里 开放 时间 ？ 需要 安排 一下 。",
            "segmented_system_utterance": "景区 是 全天 开放 的 ， 可以 尽情 游览 ！"
        },
        {
            "turn_id": 2,
            "turn_domain": [
                "旅游景点"
            ],
            "user_utterance": "门票多少钱？",
            "system_utterance": "这里是免费景区。",
            "belief_state": {
                "inform slot-values": {
                    "旅游景点-景点类型": "山水 景区",
                    "旅游景点-消费": "偏贵",
                    "旅游景点-名称": "金鸡湖 景区"
                },
                "turn_inform": {},
                "turn request": [
                    "门票价格"
                ]
            },
            "user_actions": [
                [
                    "Request",
                    "旅游景点",
                    "门票价格",
                    ""
                ]
            ],
            "system_actions": [
                [
                    "Inform",
                    "旅游景点",
                    "门票价格",
                    "免费"
                ]
            ],
            "db_results": [
                "数据库检索结果：成功匹配个数为1",
                "{'名称': '金鸡湖景区', '区域': '工业园区', '景点类型': '山水景区', '最适合人群': '情侣约会', '消费': '偏贵', '是否地铁直达': '是', '门票价格': '免费', '电话号码': '400-7558558', '地址': '苏州市工业园区星港街158号', '评分': 4.5, '开放时间': '全天', '特点': '看东方之门等高楼，坐摩天轮，乘船夜游，感受苏州现代化的一面。'}"
            ],
            "segmented_user_utterance": "门票 多少 钱 ？",
            "segmented_system_utterance": "这里 是 免费 景区 。"
        },
        {
            "turn_id": 3,
            "turn_domain": [
                "酒店"
            ],
            "user_utterance": "哦，好的。还有酒店，帮我推荐个价位中等的商务酒店！",
            "system_utterance": "推荐苏州金鸡湖李公堤瑞贝庭公寓酒店，在金鸡湖景区附近。",
            "belief_state": {
                "inform slot-values": {
                    "旅游景点-景点类型": "山水 景区",
                    "旅游景点-消费": "偏贵",
                    "旅游景点-名称": "金鸡湖 景区",
                    "酒店-价位": "中等",
                    "酒店-酒店类型": "商务 出行"
                },
                "turn_inform": {
                    "酒店-价位": "中等",
                    "酒店-酒店类型": "商务 出行"
                },
                "turn request": []
            },
            "user_actions": [
                [
                    "Inform",
                    "酒店",
                    "价位",
                    "中等"
                ],
                [
                    "Inform",
                    "酒店",
                    "酒店类型",
                    "商务 出行"
                ],
                [
                    "General",
                    "酒店",
                    "",
                    ""
                ]
            ],
            "system_actions": [
                [
                    "Recommend",
                    "酒店",
                    "名称",
                    "苏州 金鸡湖 李公堤 瑞贝庭 公寓 酒店"
                ],
                [
                    "General",
                    "通用",
                    "",
                    ""
                ]
            ],
            "db_results": [
                "数据库检索结果：成功匹配个数为16",
                "{'名称': '苏州慢享主题酒店', '区域': '姑苏区', '星级': '3', '价位': '中等', '酒店类型': '商务出行', '房型': '大床房', '停车场': '收费', '房费': '266元', '地址': '苏州姑苏区景德路26-64号', '电话号码': '0512-67570999', '评分': 4.7}",
                "{'名称': '苏州慢享主题酒店', '区域': '姑苏区', '星级': '3', '价位': '中等', '酒店类型': '商务出行', '房型': '标准间', '停车场': '收费', '房费': '278元', '地址': '苏州姑苏区景德路26-64号', '电话号码': '0512-67570999', '评分': 4.7}",
                "{'名称': '美锦酒店', '区域': '高新区', '星级': '3', '价位': '中等', '酒店类型': '商务出行', '房型': '大床房', '停车场': '免费', '房费': '308元', '地址': '苏州高新区滨河路999号花样年喜年生活广场5栋1层', '电话号码': '0512-66053331', '评分': 4.8}",
                "{'名称': '美锦酒店', '区域': '高新区', '星级': '3', '价位': '中等', '酒店类型': '商务出行', '房型': '标准间', '停车场': '免费', '房费': '349元', '地址': '苏州高新区滨河路999号花样年喜年生活广场5栋1层', '电话号码': '0512-66053331', '评分': 4.8}",
                "{'名称': '苏州金鸡湖李公堤瑞贝庭公寓酒店', '区域': '工业园区', '星级': '4', '价位': '中等', '酒店类型': '商务出行', '房型': '大床房', '停车场': '免费', '房费': '438元', '地址': '苏州工业园区李公堤三期E区商业街9幢', '电话号码': '0512-69995666', '评分': 4.6}",
                "{'名称': '苏州金鸡湖李公堤瑞贝庭公寓酒店', '区域': '工业园区', '星级': '4', '价位': '中等', '酒店类型': '商务出行', '房型': '标准间', '停车场': '免费', '房费': '438元', '地址': '苏州工业园区李公堤三期E区商业街9幢', '电话号码': '0512-69995666', '评分': 4.6}",
                "{'名称': '苏州途乐酒店公寓', '区域': '工业园区', '星级': '2', '价位': '中等', '酒店类型': '商务出行', '房型': '大床房', '停车场': '收费', '房费': '486元', '地址': '苏州工业园区苏州丰隆城市中心T1楼', '电话号码': '151-5149-7911', '评分': 4.6}",
                "{'名称': '苏州途乐酒店公寓', '区域': '工业园区', '星级': '2', '价位': '中等', '酒店类型': '商务出行', '房型': '标准间', '停车场': '收费', '房费': '486元', '地址': '苏州工业园区苏州丰隆城市中心T1楼', '电话号码': '151-5149-7911', '评分': 4.6}",
                "{'名称': '万悦酒店', '区域': '吴中区', '星级': '3', '价位': '中等', '酒店类型': '商务出行', '房型': '大床房', '停车场': '免费', '房费': '346元', '地址': '苏州吴中区金山路47-2号', '电话号码': '0512-83808380', '评分': 4.5}",
                "{'名称': '万悦酒店', '区域': '吴中区', '星级': '3', '价位': '中等', '酒店类型': '商务出行', '房型': '标准间', '停车场': '免费', '房费': '338元', '地址': '苏州吴中区金山路47-2号', '电话号码': '0512-83808380', '评分': 4.5}",
                "{'名称': '周庄多瓦台临河客栈', '区域': '昆山', '星级': '3', '价位': '中等', '酒店类型': '商务出行', '房型': '大床房', '停车场': '收费', '房费': '279元', '地址': '昆山周庄镇东浜村75号', '电话号码': '181-3619-1632', '评分': 4.8}",
                "{'名称': '周庄多瓦台临河客栈', '区域': '昆山', '星级': '3', '价位': '中等', '酒店类型': '商务出行', '房型': '标准间', '停车场': '收费', '房费': '279元', '地址': '昆山周庄镇东浜村75号', '电话号码': '181-3619-1632', '评分': 4.8}",
                "{'名称': '常熟长江路亚朵酒店', '区域': '常熟', '星级': '4', '价位': '中等', '酒店类型': '商务出行', '房型': '大床房', '停车场': '免费', '房费': '312元', '地址': '常熟长江路268号', '电话号码': '0512-51661666', '评分': 4.8}",
                "{'名称': '常熟长江路亚朵酒店', '区域': '常熟', '星级': '4', '价位': '中等', '酒店类型': '商务出行', '房型': '标准间', '停车场': '免费', '房费': '312元', '地址': '常熟长江路268号', '电话号码': '0512-51661666', '评分': 4.8}",
                "{'名称': '维也纳酒店', '区域': '常熟', '星级': '3', '价位': '中等', '酒店类型': '商务出行', '房型': '大床房', '停车场': '免费', '房费': '322元', '地址': '常熟碧溪镇金港路8号', '电话号码': '0512-52018188', '评分': 4.8}",
                "{'名称': '维也纳酒店', '区域': '常熟', '星级': '3', '价位': '中等', '酒店类型': '商务出行', '房型': '标准间', '停车场': '免费', '房费': '340元', '地址': '常熟碧溪镇金港路8号', '电话号码': '0512-52018188', '评分': 4.8}"
            ],
            "segmented_user_utterance": "哦 ， 好 的 。 还有 酒店 ， 帮 我 推荐 个 价位 中等 的 商务酒店 ！",
            "segmented_system_utterance": "推荐 苏州 金鸡湖 李公堤 瑞贝庭 公寓 酒店 ， 在 金鸡湖 景区 附近 。"
        },
        {
            "turn_id": 4,
            "turn_domain": [
                "酒店"
            ],
            "user_utterance": "你想得真周到!这家酒店有停车场吗？",
            "system_utterance": "酒店配备有一个免费的停车场。",
            "belief_state": {
                "inform slot-values": {
                    "旅游景点-景点类型": "山水 景区",
                    "旅游景点-消费": "偏贵",
                    "旅游景点-名称": "金鸡湖 景区",
                    "酒店-价位": "中等",
                    "酒店-酒店类型": "商务 出行",
                    "酒店-名称": "苏州 金鸡湖 李公堤 瑞贝庭 公寓 酒店"
                },
                "turn_inform": {
                    "酒店-名称": "苏州 金鸡湖 李公堤 瑞贝庭 公寓 酒店"
                },
                "turn request": [
                    "停车场"
                ]
            },
            "user_actions": [
                [
                    "Inform",
                    "酒店",
                    "名称",
                    "苏州 金鸡湖 李公堤 瑞贝庭 公寓 酒店"
                ],
                [
                    "Request",
                    "酒店",
                    "停车场",
                    ""
                ]
            ],
            "system_actions": [
                [
                    "Inform",
                    "酒店",
                    "停车场",
                    "免费"
                ]
            ],
            "db_results": [
                "数据库检索结果：成功匹配个数为2",
                "{'名称': '苏州金鸡湖李公堤瑞贝庭公寓酒店', '区域': '工业园区', '星级': '4', '价位': '中等', '酒店类型': '商务出行', '房型': '大床房', '停车场': '免费', '房费': '438元', '地址': '苏州工业园区李公堤三期E区商业街9幢', '电话号码': '0512-69995666', '评分': 4.6}",
                "{'名称': '苏州金鸡湖李公堤瑞贝庭公寓酒店', '区域': '工业园区', '星级': '4', '价位': '中等', '酒店类型': '商务出行', '房型': '标准间', '停车场': '免费', '房费': '438元', '地址': '苏州工业园区李公堤三期E区商业街9幢', '电话号码': '0512-69995666', '评分': 4.6}"
            ],
            "segmented_user_utterance": "你 想 得 真 周到 ! 这家 酒店 有 停车场 吗 ？",
            "segmented_system_utterance": "酒店 配备 有 一个 免费 的 停车场 。"
        },
        {
            "turn_id": 5,
            "turn_domain": [
                "酒店"
            ],
            "user_utterance": "酒店的电话告诉我一下。",
            "system_utterance": "电话号码：0512-69995666。",
            "belief_state": {
                "inform slot-values": {
                    "旅游景点-景点类型": "山水 景区",
                    "旅游景点-消费": "偏贵",
                    "旅游景点-名称": "金鸡湖 景区",
                    "酒店-价位": "中等",
                    "酒店-酒店类型": "商务 出行",
                    "酒店-名称": "苏州 金鸡湖 李公堤 瑞贝庭 公寓 酒店"
                },
                "turn_inform": {},
                "turn request": [
                    "电话号码"
                ]
            },
            "user_actions": [
                [
                    "Request",
                    "酒店",
                    "电话号码",
                    ""
                ]
            ],
            "system_actions": [
                [
                    "Inform",
                    "酒店",
                    "电话号码",
                    "0512 - 69995666"
                ]
            ],
            "db_results": [
                "数据库检索结果：成功匹配个数为2",
                "{'名称': '苏州金鸡湖李公堤瑞贝庭公寓酒店', '区域': '工业园区', '星级': '4', '价位': '中等', '酒店类型': '商务出行', '房型': '大床房', '停车场': '免费', '房费': '438元', '地址': '苏州工业园区李公堤三期E区商业街9幢', '电话号码': '0512-69995666', '评分': 4.6}",
                "{'名称': '苏州金鸡湖李公堤瑞贝庭公寓酒店', '区域': '工业园区', '星级': '4', '价位': '中等', '酒店类型': '商务出行', '房型': '标准间', '停车场': '免费', '房费': '438元', '地址': '苏州工业园区李公堤三期E区商业街9幢', '电话号码': '0512-69995666', '评分': 4.6}"
            ],
            "segmented_user_utterance": "酒店 的 电话 告诉 我 一下 。",
            "segmented_system_utterance": "电话号码 ： 0512 - 69995666 。"
        },
        {
            "turn_id": 6,
            "turn_domain": [
                "餐厅"
            ],
            "user_utterance": "嗯，我还想拔草美食。有没有价位中等的江浙菜餐厅推荐一个。",
            "system_utterance": "推荐老枫庭。",
            "belief_state": {
                "inform slot-values": {
                    "旅游景点-景点类型": "山水 景区",
                    "旅游景点-消费": "偏贵",
                    "旅游景点-名称": "金鸡湖 景区",
                    "餐厅-菜系": "江浙 菜",
                    "餐厅-价位": "中等",
                    "酒店-价位": "中等",
                    "酒店-酒店类型": "商务 出行",
                    "酒店-名称": "苏州 金鸡湖 李公堤 瑞贝庭 公寓 酒店"
                },
                "turn_inform": {
                    "餐厅-菜系": "江浙 菜",
                    "餐厅-价位": "中等"
                },
                "turn request": []
            },
            "user_actions": [
                [
                    "Inform",
                    "餐厅",
                    "菜系",
                    "江浙 菜"
                ],
                [
                    "Inform",
                    "餐厅",
                    "价位",
                    "中等"
                ],
                [
                    "General",
                    "餐厅",
                    "",
                    ""
                ]
            ],
            "system_actions": [
                [
                    "Recommend",
                    "餐厅",
                    "名称",
                    "老枫庭"
                ]
            ],
            "db_results": [
                "数据库检索结果：成功匹配个数为3",
                "{'名称': '老枫庭', '区域': '吴中区', '菜系': '江浙菜', '价位': '中等', '是否地铁直达': '否', '人均消费': '94元', '地址': '木渎灵天路55号芭提雅休闲娱乐广场5号楼', '电话号码': '0512-66277557', '评分': 4.6, '营业时间': '周一至周日 11:00-13:30 17:00-20:30', '推荐菜': '松鼠桂鱼'}",
                "{'名称': '同里老家', '区域': '吴江', '菜系': '江浙菜', '价位': '中等', '是否地铁直达': '否', '人均消费': '87元', '地址': '同里镇环湖西路318号', '电话号码': '0512-63339777', '评分': 4.5, '营业时间': '周一至周日 10:00-22:00', '推荐菜': '太湖三白'}",
                "{'名称': '周庄花间堂桔梗餐厅', '区域': '昆山', '菜系': '江浙菜', '价位': '中等', '是否地铁直达': '否', '人均消费': '98元', '地址': '周庄镇中市街110号景点迷楼北10米', '电话号码': '138-1289-9961', '评分': 4.5, '营业时间': '周一至周日 07:00-20:30', '推荐菜': '银鱼炒蛋'}"
            ],
            "segmented_user_utterance": "嗯 ， 我 还 想 拔草 美食 。 有没有 价位 中等 的 江浙 菜 餐厅 推荐 一个 。",
            "segmented_system_utterance": "推荐 老枫庭 。"
        },
        {
            "turn_id": 7,
            "turn_domain": [
                "餐厅"
            ],
            "user_utterance": "这家餐厅地铁直达吗？",
            "system_utterance": "抱歉，餐厅没有地铁直达!",
            "belief_state": {
                "inform slot-values": {
                    "旅游景点-景点类型": "山水 景区",
                    "旅游景点-消费": "偏贵",
                    "旅游景点-名称": "金鸡湖 景区",
                    "餐厅-菜系": "江浙 菜",
                    "餐厅-价位": "中等",
                    "餐厅-名称": "老枫庭",
                    "酒店-价位": "中等",
                    "酒店-酒店类型": "商务 出行",
                    "酒店-名称": "苏州 金鸡湖 李公堤 瑞贝庭 公寓 酒店"
                },
                "turn_inform": {
                    "餐厅-名称": "老枫庭"
                },
                "turn request": [
                    "是否地铁直达"
                ]
            },
            "user_actions": [
                [
                    "Inform",
                    "餐厅",
                    "名称",
                    "老枫庭"
                ],
                [
                    "Request",
                    "餐厅",
                    "是否地铁直达",
                    ""
                ]
            ],
            "system_actions": [
                [
                    "Inform",
                    "餐厅",
                    "是否地铁直达",
                    "否"
                ],
                [
                    "General",
                    "通用",
                    "",
                    ""
                ]
            ],
            "db_results": [
                "数据库检索结果：成功匹配个数为1",
                "{'名称': '老枫庭', '区域': '吴中区', '菜系': '江浙菜', '价位': '中等', '是否地铁直达': '否', '人均消费': '94元', '地址': '木渎灵天路55号芭提雅休闲娱乐广场5号楼', '电话号码': '0512-66277557', '评分': 4.6, '营业时间': '周一至周日 11:00-13:30 17:00-20:30', '推荐菜': '松鼠桂鱼'}"
            ],
            "segmented_user_utterance": "这家 餐厅 地铁 直达 吗 ？",
            "segmented_system_utterance": "抱歉 ， 餐厅 没有 地铁 直达 !"
        },
        {
            "turn_id": 8,
            "turn_domain": [
                "餐厅"
            ],
            "user_utterance": "人均消费呢？",
            "system_utterance": "老枫庭人均消费在94元左右。",
            "belief_state": {
                "inform slot-values": {
                    "旅游景点-景点类型": "山水 景区",
                    "旅游景点-消费": "偏贵",
                    "旅游景点-名称": "金鸡湖 景区",
                    "餐厅-菜系": "江浙 菜",
                    "餐厅-价位": "中等",
                    "餐厅-名称": "老枫庭",
                    "酒店-价位": "中等",
                    "酒店-酒店类型": "商务 出行",
                    "酒店-名称": "苏州 金鸡湖 李公堤 瑞贝庭 公寓 酒店"
                },
                "turn_inform": {},
                "turn request": [
                    "人均消费"
                ]
            },
            "user_actions": [
                [
                    "Request",
                    "餐厅",
                    "人均消费",
                    ""
                ]
            ],
            "system_actions": [
                [
                    "Inform",
                    "餐厅",
                    "人均消费",
                    "老枫庭"
                ]
            ],
            "db_results": [
                "数据库检索结果：成功匹配个数为1",
                "{'名称': '老枫庭', '区域': '吴中区', '菜系': '江浙菜', '价位': '中等', '是否地铁直达': '否', '人均消费': '94元', '地址': '木渎灵天路55号芭提雅休闲娱乐广场5号楼', '电话号码': '0512-66277557', '评分': 4.6, '营业时间': '周一至周日 11:00-13:30 17:00-20:30', '推荐菜': '松鼠桂鱼'}"
            ],
            "segmented_user_utterance": "人均 消费 呢 ？",
            "segmented_system_utterance": "老枫庭 人均 消费 在 94 元 左右 。"
        },
        {
            "turn_id": 9,
            "turn_domain": [
                "通用"
            ],
            "user_utterance": "好，所有问题都解决了，谢谢你的帮助！再见！",
            "system_utterance": "不客气！这是我应该做的！再见！",
            "belief_state": {
                "inform slot-values": {
                    "旅游景点-景点类型": "山水 景区",
                    "旅游景点-消费": "偏贵",
                    "旅游景点-名称": "金鸡湖 景区",
                    "餐厅-菜系": "江浙 菜",
                    "餐厅-价位": "中等",
                    "餐厅-名称": "老枫庭",
                    "酒店-价位": "中等",
                    "酒店-酒店类型": "商务 出行",
                    "酒店-名称": "苏州 金鸡湖 李公堤 瑞贝庭 公寓 酒店"
                },
                "turn_inform": {},
                "turn request": []
            },
            "user_actions": [
                [
                    "Bye",
                    "通用",
                    "",
                    ""
                ],
                [
                    "General",
                    "通用",
                    "",
                    ""
                ]
            ],
            "system_actions": [
                [
                    "Bye",
                    "通用",
                    "",
                    ""
                ],
                [
                    "General",
                    "通用",
                    "",
                    ""
                ]
            ],
            "db_results": [],
            "segmented_user_utterance": "好 ， 所有 问题 都 解决 了 ， 谢谢 你 的 帮助 ！ 再见 ！",
            "segmented_system_utterance": "不 客气 ！ 这 是 我 应该 做 的 ！ 再见 ！"
        }
    ]
}
```



## Dataset in GEM

### Rationale for Inclusion in GEM

#### Why is the Dataset in GEM?

<!-- info: What does this dataset contribute toward better generation evaluation and why is it part of GEM? -->
<!-- scope: microscope -->
RiSAWOZ is the first large-scale multi-domain Chinese Wizard-of-Oz dataset with rich semantic annotations.

#### Similar Datasets

<!-- info: Do other datasets for the high level task exist? -->
<!-- scope: telescope -->
yes

#### Unique Language Coverage

<!-- info: Does this dataset cover other languages than other datasets for the same task? -->
<!-- scope: periscope -->
no

#### Difference from other GEM datasets

<!-- info: What else sets this dataset apart from other similar datasets in GEM? -->
<!-- scope: microscope -->
The corpus contains rich semantic annotations, such as ellipsis and coreference, in addition to  traditional dialogue annotations (dialogue states, dialogue acts, etc.), which can be used in various tasks in dialogue system.


#### Ability that the Dataset measures

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: periscope -->
Natural Language Understanding, Dialogue State Tracking, Dialogue Context-to-Text Generation, Coreference Resolution, Unified Generative Ellipsis and Coreference Resolution


### GEM-Specific Curation

#### Modificatied for GEM?

<!-- info: Has the GEM version of the dataset been modified in any way (data, processing, splits) from the original curated data? -->
<!-- scope: telescope -->
no

#### Additional Splits?

<!-- info: Does GEM provide additional splits to the dataset? -->
<!-- scope: telescope -->
no


### Getting Started with the Task

#### Pointers to Resources

<!-- info: Getting started with in-depth research on the task. Add relevant pointers to resources that researchers can consult when they want to get started digging deeper into the task. -->
<!-- scope: microscope -->
[Website](https://terryqj0107.github.io/RiSAWOZ_webpage)

#### Technical Terms

<!-- info: Technical terms used in this card and the dataset and their definitions -->
<!-- scope: microscope -->
- In task-oriented dialogue system, the Natural Language Understanding (NLU) module aims to convert the user utterance into the representation that computer can understand, which includes intent and dialogue act (slot & value) detection.
- Dialogue State Tracking (DST) is a core component in task-oriented dialogue systems, which extracts dialogue states (user goals) embedded in dialogue context. It has progressed toward open-vocabulary or generation-based DST where state-of-the-art models can generate dialogue states from dialogue context directly.
- Context-to-Text Generation: encoding dialogue context to decode system response.
- Coreference Resolution: predict coreference clusters where all mentions are referring to the same entity for each dialogue.
- Unified Generative Ellipsis and Coreference Resolution: generating omitted or referred expressions from the dialogue context.



## Previous Results

### Previous Results

#### Measured Model Abilities

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: telescope -->
Natural Language Understanding, Dialogue State Tracking, Dialogue Context-to-Text Generation, Coreference Resolution, Unified Generative Ellipsis and Coreference Resolution

#### Metrics

<!-- info: What metrics are typically used for this task? -->
<!-- scope: periscope -->
`Other: Other Metrics`

#### Other Metrics

<!-- info: Definitions of other metrics -->
<!-- scope: periscope -->
- Natural Language Understanding:
    - F1 score: F1 score of user intent.
- Dialogue State Tracking:
    - Joint Accuracy: accuracy of turn-level dialogue states.
- Dialogue Context-to-Text Generation:
    - inform rate: measures the percentage that the output contains the appropriate entity the user asks for.
    - success rate: estimates the proportion that all the requested attributes have been answered.
    - BLEU: the BLEU score of generated system response.
    - Combined Score: (inform + success) ∗ 0.5 + BLEU as an overall
    quality.
- Coreference Resolution:
    - MUC F1 Score: a link-based metric. Mentions in the same entity/cluster are considered “linked”. MUC penalizes the missing links and incorrect links, each with the same weight.
    - B3 F1 Score: a mention-based metric.The evaluation score depends on the fraction of the correct mentions included in the response entities (i.e. entities created by the system).
    - CEAFφ4 F1 Score: a metric which assumes each key entity should only be mapped to one response entity, and vice versa. It aligns the key entities (clusters) with the response entities in the best way, and compute scores from that alignment.
    - Average F1 Score: an average F1 score of the above three metrics.
- Unified Generative Ellipsis and Coreference Resolution:
    - Exact Match Rate: measures whether the generated utterances exactly match the ground-truth utterances.
    - BLEU: the BLEU score of generated utterances
    - Resolution F1: comparing machine-generated words with ground-truth words only from the ellipsis/coreference part of user utterances.

#### Proposed Evaluation

<!-- info: List and describe the purpose of the metrics and evaluation methodology (including human evaluation) that the dataset creators used when introducing this task. -->
<!-- scope: microscope -->
see "Definitions of other metrics"

#### Previous results available?

<!-- info: Are previous results available? -->
<!-- scope: telescope -->
yes

#### Other Evaluation Approaches

<!-- info: What evaluation approaches have others used? -->
<!-- scope: periscope -->
same as our dataset

#### Relevant Previous Results

<!-- info: What are the most relevant previous results for this task/dataset? -->
<!-- scope: microscope -->
Joint Accuracy, Inform Rate, Success Rate, BLEU Score and Combined Score on MultiWOZ and CrossWOZ dataset. 



## Dataset Curation

### Original Curation

#### Original Curation Rationale

<!-- info: Original curation rationale -->
<!-- scope: telescope -->
Gather human-to-human dialog in Chinese.

#### Communicative Goal

<!-- info: What was the communicative goal? -->
<!-- scope: periscope -->
Generate system response given dialogue context across multiple domains.

#### Sourced from Different Sources

<!-- info: Is the dataset aggregated from different data sources? -->
<!-- scope: telescope -->
no


### Language Data

#### How was Language Data Obtained?

<!-- info: How was the language data obtained? -->
<!-- scope: telescope -->
`Crowdsourced`

#### Where was it crowdsourced?

<!-- info: If crowdsourced, where from? -->
<!-- scope: periscope -->
`Other crowdworker platform`

#### Topics Covered

<!-- info: Does the language in the dataset focus on specific topics? How would you describe them? -->
<!-- scope: periscope -->
domains: Attraction, Restaurant, Hotel, Flight, Train, Weather, Movie, TV, Computer, Car, Hospital, Courses

#### Data Validation

<!-- info: Was the text validated by a different worker or a data curator? -->
<!-- scope: telescope -->
validated by data curator

#### Was Data Filtered?

<!-- info: Were text instances selected or filtered? -->
<!-- scope: telescope -->
hybrid

#### Filter Criteria

<!-- info: What were the selection criteria? -->
<!-- scope: microscope -->
Rule-based and manual selection criteria


### Structured Annotations

#### Additional Annotations?

<!-- quick -->
<!-- info: Does the dataset have additional annotations for each instance? -->
<!-- scope: telescope -->
crowd-sourced

#### Number of Raters

<!-- info: What is the number of raters -->
<!-- scope: telescope -->
51<n<100

#### Rater Qualifications

<!-- info: Describe the qualifications required of an annotator. -->
<!-- scope: periscope -->
Chinese native speaker

#### Raters per Training Example

<!-- info: How many annotators saw each training example? -->
<!-- scope: periscope -->
3

#### Raters per Test Example

<!-- info: How many annotators saw each test example? -->
<!-- scope: periscope -->
3

#### Annotation Service?

<!-- info: Was an annotation service used? -->
<!-- scope: telescope -->
no

#### Annotation Values

<!-- info: Purpose and values for each annotation -->
<!-- scope: microscope -->
- dialogue_id (string): dialogue ID
- goal (string): natural language descriptions of the user goal
- domains (list of strings): domains mentioned in current dialogue session
- turn_id (int): turn ID
- turn_domain (list of strings): domain mentioned in current turn
- belief_state (dict): dialogue state, including:
    - inform slot-values (dict): the slots and corresponding values informed until current turn
    - turn_inform (dict): the slots and corresponding values informed in current turn
    - turn request (dict): the slots requested in current turn
- user_actions (list of lists): user dialogue acts in current turn
- user_actions (list of lists): system dialogue acts in current turn
- db_results (list of strings): database search results
- segmented_user_utterance (string): word segmentation result of user utterance
- segmented_system_utterance (string): word segmentation result of system utterance

#### Any Quality Control?

<!-- info: Quality control measures? -->
<!-- scope: telescope -->
unknown


### Consent

#### Any Consent Policy?

<!-- info: Was there a consent policy involved when gathering the data? -->
<!-- scope: telescope -->
yes

#### Consent Policy Details

<!-- info: What was the consent policy? -->
<!-- scope: microscope -->
Annotators agree using the dataset for research purpose.

#### Other Consented Downstream Use

<!-- info: What other downstream uses of the data did the original data creators and the data curators consent to? -->
<!-- scope: microscope -->
Any


### Private Identifying Information (PII)

#### Contains PII?

<!-- quick -->
<!-- info: Does the source language data likely contain Personal Identifying Information about the data creators or subjects? -->
<!-- scope: telescope -->
no PII

#### Justification for no PII

<!-- info: Provide a justification for selecting `no PII` above. -->
<!-- scope: periscope -->
The slots and values as well as utterances do not contain any personal information.


### Maintenance

#### Any Maintenance Plan?

<!-- info: Does the original dataset have a maintenance plan? -->
<!-- scope: telescope -->
yes

#### Maintenance Plan Details

<!-- info: Describe the original dataset's maintenance plan. -->
<!-- scope: microscope -->
Building a leaderboard webpage to trace and display the latest results on the [dataset](https://terryqj0107.github.io/RiSAWOZ_webpage/)

#### Maintainer Contact Information

<!-- info: Provide contact information of a person responsible for the dataset maintenance -->
<!-- scope: periscope -->
Deyi Xiong (dyxiong@tju.edu.cn)

#### Any Contestation Mechanism?

<!-- info: Does the maintenance plan include a contestation mechanism allowing individuals to request removal fo content? -->
<!-- scope: periscope -->
contact maintainer

#### Contestation Form Link

<!-- info: Provide the form link or contact information -->
<!-- scope: periscope -->
Deyi Xiong (dyxiong@tju.edu.cn)



## Broader Social Context

### Previous Work on the Social Impact of the Dataset

#### Usage of Models based on the Data

<!-- info: Are you aware of cases where models trained on the task featured in this dataset ore related tasks have been used in automated systems? -->
<!-- scope: telescope -->
no


### Impact on Under-Served Communities

#### Addresses needs of underserved Communities?

<!-- info: Does this dataset address the needs of communities that are traditionally underserved in language technology, and particularly language generation technology? Communities may be underserved for exemple because their language, language variety, or social or geographical context is underepresented in NLP and NLG resources (datasets and models). -->
<!-- scope: telescope -->
yes

#### Details on how Dataset Addresses the Needs

<!-- info: Describe how this dataset addresses the needs of underserved communities. -->
<!-- scope: microscope -->
RiSAWOZ is the first large-scale multi-domain Chinese Wizard-of-Oz dataset with rich semantic annotations.


### Discussion of Biases

#### Any Documented Social Biases?

<!-- info: Are there documented social biases in the dataset? Biases in this context are variations in the ways members of different social categories are represented that can have harmful downstream consequences for members of the more disadvantaged group. -->
<!-- scope: telescope -->
no

#### Are the Language Producers Representative of the Language?

<!-- info: Does the distribution of language producers in the dataset accurately represent the full distribution of speakers of the language world-wide? If not, how does it differ? -->
<!-- scope: periscope -->
yes



## Considerations for Using the Data

### PII Risks and Liability

#### Potential PII Risk

<!-- info: Considering your answers to the PII part of the Data Curation Section, describe any potential privacy to the data subjects and creators risks when using the dataset. -->
<!-- scope: microscope -->
None


### Licenses

#### Copyright Restrictions on the Dataset

<!-- info: Based on your answers in the Intended Use part of the Data Overview Section, which of the following best describe the copyright and licensing status of the dataset? -->
<!-- scope: periscope -->
`open license - commercial use allowed`

#### Copyright Restrictions on the Language Data

<!-- info: Based on your answers in the Language part of the Data Curation Section, which of the following best describe the copyright and licensing status of the underlying language data? -->
<!-- scope: periscope -->
`open license - commercial use allowed`


### Known Technical Limitations

#### Technical Limitations

<!-- info: Describe any known technical limitations, such as spurrious correlations, train/test overlap, annotation biases, or mis-annotations, and cite the works that first identified these limitations when possible. -->
<!-- scope: microscope -->
None

#### Unsuited Applications

<!-- info: When using a model trained on this dataset in a setting where users or the public may interact with its predictions, what are some pitfalls to look out for? In particular, describe some applications of the general task featured in this dataset that its curation or properties make it less suitable for. -->
<!-- scope: microscope -->
Using the trained model on domains that are not included in the 12 domains selected for this dataset.

#### Discouraged Use Cases

<!-- info: What are some discouraged use cases of a model trained to maximize the proposed metrics on this dataset? In particular, think about settings where decisions made by a model that performs reasonably well on the metric my still have strong negative consequences for user or members of the public. -->
<!-- scope: microscope -->
Designing models that leverage unknown bias in the dataset to optimize specific metrics.


