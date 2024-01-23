---
annotations_creators:
- none
language_creators:
- unknown
language:
- zh
license:
- apache-2.0
multilinguality:
- unknown
size_categories:
- unknown
source_datasets:
- original
task_categories:
- conversational
task_ids: []
pretty_name: CrossWOZ
tags:
- dialog-response-generation
---

# Dataset Card for GEM/CrossWOZ

## Dataset Description

- **Homepage:** https://github.com/thu-coai/CrossWOZ
- **Repository:** https://github.com/thu-coai/CrossWOZ
- **Paper:** https://aclanthology.org/2020.tacl-1.19
- **Leaderboard:** N/A
- **Point of Contact:** Qi Zhu

### Link to Main Data Card

You can find the main data card on the [GEM Website](https://gem-benchmark.com/data_cards/CrossWOZ).

### Dataset Summary 

CrossWOZ is a Chinese multi-domain task-oriented dialogue dataset . It contains 6K dialogue sessions and 102K utterances for 5 domains, including hotel, restaurant, attraction, metro, and taxi. About 60{\%} of the dialogues have cross-domain user goals that favor inter-domain dependency and encourage natural transition across domains in conversation.

You can load the dataset via:
```
import datasets
data = datasets.load_dataset('GEM/CrossWOZ')
```
The data loader can be found [here](https://huggingface.co/datasets/GEM/CrossWOZ).

#### website
[Github](https://github.com/thu-coai/CrossWOZ)

#### paper
[ACL Anthology](https://aclanthology.org/2020.tacl-1.19)

#### authors
Qi Zhu, Kaili Huang, Zheng Zhang, Xiaoyan Zhu, and Minlie Huang from CoAI group, Tsinghua University

## Dataset Overview

### Where to find the Data and its Documentation

#### Webpage

<!-- info: What is the webpage for the dataset (if it exists)? -->
<!-- scope: telescope -->
[Github](https://github.com/thu-coai/CrossWOZ)

#### Download

<!-- info: What is the link to where the original dataset is hosted? -->
<!-- scope: telescope -->
[Github](https://github.com/thu-coai/CrossWOZ)

#### Paper

<!-- info: What is the link to the paper describing the dataset (open access preferred)? -->
<!-- scope: telescope -->
[ACL Anthology](https://aclanthology.org/2020.tacl-1.19)

#### BibTex

<!-- info: Provide the BibTex-formatted reference for the dataset. Please use the correct published version (ACL anthology, etc.) instead of google scholar created Bibtex. -->
<!-- scope: microscope -->
```
@article{zhu-etal-2020-crosswoz,
    title = "{C}ross{WOZ}: A Large-Scale {C}hinese Cross-Domain Task-Oriented Dialogue Dataset",
    author = "Zhu, Qi  and
      Huang, Kaili  and
      Zhang, Zheng  and
      Zhu, Xiaoyan  and
      Huang, Minlie",
    journal = "Transactions of the Association for Computational Linguistics",
    volume = "8",
    year = "2020",
    url = "https://aclanthology.org/2020.tacl-1.19",
    doi = "10.1162/tacl_a_00314",
    pages = "281--295",
    abstract = "To advance multi-domain (cross-domain) dialogue modeling as well as alleviate the shortage of Chinese task-oriented datasets, we propose CrossWOZ, the first large-scale Chinese Cross-Domain Wizard-of-Oz task-oriented dataset. It contains 6K dialogue sessions and 102K utterances for 5 domains, including hotel, restaurant, attraction, metro, and taxi. Moreover, the corpus contains rich annotation of dialogue states and dialogue acts on both user and system sides. About 60{\%} of the dialogues have cross-domain user goals that favor inter-domain dependency and encourage natural transition across domains in conversation. We also provide a user simulator and several benchmark models for pipelined task-oriented dialogue systems, which will facilitate researchers to compare and evaluate their models on this corpus. The large size and rich annotation of CrossWOZ make it suitable to investigate a variety of tasks in cross-domain dialogue modeling, such as dialogue state tracking, policy learning, user simulation, etc.",
}
```

#### Contact Name

<!-- quick -->
<!-- info: If known, provide the name of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
Qi Zhu

#### Contact Email

<!-- info: If known, provide the email of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
zhuq96@gmail.com

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

#### Covered Languages

<!-- quick -->
<!-- info: What languages/dialects are covered in the dataset? -->
<!-- scope: telescope -->
`Chinese`

#### License

<!-- quick -->
<!-- info: What is the license of the dataset? -->
<!-- scope: telescope -->
apache-2.0: Apache License 2.0

#### Intended Use

<!-- info: What is the intended use of the dataset? -->
<!-- scope: microscope -->
CrossWOZ is the first large-scale Chinese Cross-Domain Wizard-of-Oz task-oriented dataset. It contains 6K dialogue sessions and 102K utterances for 5 domains, including hotel, restaurant, attraction, metro, and taxi. Moreover, the corpus contains rich annotation of dialogue states and dialogue acts at both user and system sides. We also provide a user simulator and several benchmark models for pipelined taskoriented dialogue systems, which will facilitate researchers to compare and evaluate their models on this corpus.

#### Primary Task

<!-- info: What primary task does the dataset support? -->
<!-- scope: telescope -->
Dialog Response Generation

#### Communicative Goal

<!-- quick -->
<!-- info: Provide a short description of the communicative goal of a model trained for this task on this dataset. -->
<!-- scope: periscope -->
Generate a response according to the dialog context and database search results.


### Credit

#### Curation Organization Type(s)

<!-- info: In what kind of organization did the dataset curation happen? -->
<!-- scope: telescope -->
`academic`

#### Curation Organization(s)

<!-- info: Name the organization(s). -->
<!-- scope: periscope -->
Tsinghua University

#### Dataset Creators

<!-- info: Who created the original dataset? List the people involved in collecting the dataset and their affiliation(s). -->
<!-- scope: microscope -->
Qi Zhu, Kaili Huang, Zheng Zhang, Xiaoyan Zhu, and Minlie Huang from CoAI group, Tsinghua University

#### Funding

<!-- info: Who funded the data creation? -->
<!-- scope: microscope -->
National Science Foundation of China, National Key R&D Program of China 

#### Who added the Dataset to GEM?

<!-- info: Who contributed to the data card and adding the dataset to GEM? List the people+affiliations involved in creating this data card and who helped integrate this dataset into GEM. -->
<!-- scope: microscope -->
Qi Zhu (Tsinghua University)


### Dataset Structure

#### Data Fields

<!-- info: List and describe the fields present in the dataset. -->
<!-- scope: telescope -->
- `gem_id` (string): GEM-CrossWOZ-{split}-{id}
- `dialog_id` (string): dialog ID
- `sys_id` (string): system annotator ID
- `usr_id` (string): user annotation ID
- `type` (string): dialog type
- `task description` (list of strings): natural language descriptions of the user goal
- `goal` (list of tuples), includes:
  - `sub-goal id` (string)
  - `domain name` (string)
  - `slot name` (string)
  - `constraint` if filled, else `requirement` (string)
  - `whether be mentioned in previous turns` (string)
- `messages` (list of dict): dialog turns. Each turn contains:
  - `content` (string): utterance
  - `role` (string): user or system
  - `dialog_act` (list of tuples), includes:
    - `domain` (string)
    - `intent` (string)
    - `slot` (string)
    - `value` (string)
  - `user_state` (list of tuples): same format as "goal", can be viewed as dynamic goal.
  - `sys_state_init` (dict): the first db query emitted, records user constraints faithfully. If the system find no result that matches, he/she may relax the constraints manually and search db multiple times.
    - `domain` (dict): slot(string)-value(string) pairs
    - `selectedResults` (list of string): db search result that would be used in this turn.
  - `sys_state` (dict): the final db query emitted, records the db used by the system in this turn. Same format as sys_state_init. Note that this may not satisfy all user constraints.
- `final_goal` (list of tuples): user state/goal at the end of dialog. same format as "goal".

#### Example Instance

<!-- info: Provide a JSON formatted example of a typical instance in the dataset. -->
<!-- scope: periscope -->
```
{'dialog_id': '2303',
 'final_goal': [['1', '餐馆', '人均消费', '50-100元', 'True'],
  ['1', '餐馆', '推荐菜', "['美食街']", 'True'],
  ['1', '餐馆', '名称', '鲜鱼口老字号美食街', 'True'],
  ['1', '餐馆', '营业时间', '周一至周日 10:00-22:00', 'True'],
  ['1', '餐馆', '周边景点', "['天安门广场', '前门大街', '恭王府', '故宫']", 'True'],
  ['2', '景点', '名称', '故宫', 'True'],
  ['2', '景点', '评分', '4.5分以上', 'True'],
  ['2', '景点', '地址', '北京市东城区景山前街4号', 'True'],
  ['2', '景点', '电话', '010-85007938', 'True'],
  ['3', '酒店', '名称', '桔子水晶酒店(北京安贞店)', 'True'],
  ['3', '酒店', '电话', '010-84273030', 'True']],
 'gem_id': 'GEM-CrossWOZ-test-0',
 'goal': [['1', '餐馆', '人均消费', '50-100元', 'False'],
  ['1', '餐馆', '推荐菜', "['美食街']", 'False'],
  ['1', '餐馆', '名称', '', 'False'],
  ['1', '餐馆', '营业时间', '', 'False'],
  ['1', '餐馆', '周边景点', '[]', 'False'],
  ['2', '景点', '名称', '出现在id=1的周边景点里', 'False'],
  ['2', '景点', '评分', '4.5分以上', 'False'],
  ['2', '景点', '地址', '', 'False'],
  ['2', '景点', '电话', '', 'False'],
  ['3', '酒店', '名称', '桔子水晶酒店(北京安贞店)', 'False'],
  ['3', '酒店', '电话', '', 'False']],
 'messages': {'content': ['你好，我想吃美食街，帮我推荐一个人均消费在50-100元的餐馆，谢谢。',
   '为您推荐鲜鱼口老字号美食街，人均消费75元，有您想吃的美食街哦。',
   '营业时间是什么时间？',
   '周一至周日 10:00-22:00。',
   '他家周边有什么景点吗？',
   '有故宫, 前门大街, 恭王府, 天安门广场。',
   '哦，我想在这些附近景点里找一个4.5分以上的，有吗？',
   '故宫就是哦，4.7分。',
   '好的，电话和地址告诉我一下。',
   '010-85007938；北京市东城区景山前街4号。',
   '好的，麻烦你帮我查一下桔子水晶酒店(北京安贞店)电话呗。',
   '010-84273030。',
   '好的，收到，谢谢你！',
   '不客气。'],
  'dialog_act': [[['General', 'greet', 'none', 'none'],
    ['General', 'thank', 'none', 'none'],
    ['Inform', '餐馆', '人均消费', '50-100元'],
    ['Inform', '餐馆', '推荐菜', '美食街'],
    ['Request', '餐馆', '名称', '']],
   [['Inform', '餐馆', '人均消费', '75元'], ['Inform', '餐馆', '名称', '鲜鱼口老字号美食街']],
   [['Request', '餐馆', '营业时间', '']],
   [['Inform', '餐馆', '营业时间', '周一至周日 10:00-22:00']],
   [['Request', '餐馆', '周边景点', '']],
   [['Inform', '餐馆', '周边景点', '前门大街'],
    ['Inform', '餐馆', '周边景点', '天安门广场'],
    ['Inform', '餐馆', '周边景点', '恭王府'],
    ['Inform', '餐馆', '周边景点', '故宫']],
   [['Inform', '景点', '评分', '4.5分以上'], ['Select', '景点', '源领域', '餐馆']],
   [['Inform', '景点', '名称', '故宫'], ['Inform', '景点', '评分', '4.7分']],
   [['Request', '景点', '地址', ''], ['Request', '景点', '电话', '']],
   [['Inform', '景点', '地址', '北京市东城区景山前街4号'],
    ['Inform', '景点', '电话', '010-85007938']],
   [['Inform', '酒店', '名称', '桔子水晶酒店(北京安贞店)'], ['Request', '酒店', '电话', '']],
   [['Inform', '酒店', '电话', '010-84273030']],
   [['General', 'thank', 'none', 'none']],
   [['General', 'welcome', 'none', 'none']]],
  'role': ['usr',
   'sys',
   'usr',
   'sys',
   'usr',
   'sys',
   'usr',
   'sys',
   'usr',
   'sys',
   'usr',
   'sys',
   'usr',
   'sys'],
  'sys_state': [{'出租': {'selectedResults': [], '出发地': '', '目的地': ''},
    '地铁': {'selectedResults': [], '出发地': '', '目的地': ''},
    '景点': {'selectedResults': [],
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '游玩时间': '',
     '评分': '',
     '门票': ''},
    '酒店': {'selectedResults': [],
     '价格': '',
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '评分': '',
     '酒店类型': '',
     '酒店设施': ''},
    '餐馆': {'selectedResults': [],
     '人均消费': '',
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '推荐菜': '',
     '评分': ''}},
   {'出租': {'selectedResults': [], '出发地': '', '目的地': ''},
    '地铁': {'selectedResults': [], '出发地': '', '目的地': ''},
    '景点': {'selectedResults': [],
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '游玩时间': '',
     '评分': '',
     '门票': ''},
    '酒店': {'selectedResults': [],
     '价格': '',
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '评分': '',
     '酒店类型': '',
     '酒店设施': ''},
    '餐馆': {'selectedResults': ['鲜鱼口老字号美食街'],
     '人均消费': '50-100元',
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '推荐菜': '美食街',
     '评分': ''}},
   {'出租': {'selectedResults': [], '出发地': '', '目的地': ''},
    '地铁': {'selectedResults': [], '出发地': '', '目的地': ''},
    '景点': {'selectedResults': [],
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '游玩时间': '',
     '评分': '',
     '门票': ''},
    '酒店': {'selectedResults': [],
     '价格': '',
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '评分': '',
     '酒店类型': '',
     '酒店设施': ''},
    '餐馆': {'selectedResults': [],
     '人均消费': '',
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '推荐菜': '',
     '评分': ''}},
   {'出租': {'selectedResults': [], '出发地': '', '目的地': ''},
    '地铁': {'selectedResults': [], '出发地': '', '目的地': ''},
    '景点': {'selectedResults': [],
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '游玩时间': '',
     '评分': '',
     '门票': ''},
    '酒店': {'selectedResults': [],
     '价格': '',
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '评分': '',
     '酒店类型': '',
     '酒店设施': ''},
    '餐馆': {'selectedResults': ['鲜鱼口老字号美食街'],
     '人均消费': '50-100元',
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '推荐菜': '美食街',
     '评分': ''}},
   {'出租': {'selectedResults': [], '出发地': '', '目的地': ''},
    '地铁': {'selectedResults': [], '出发地': '', '目的地': ''},
    '景点': {'selectedResults': [],
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '游玩时间': '',
     '评分': '',
     '门票': ''},
    '酒店': {'selectedResults': [],
     '价格': '',
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '评分': '',
     '酒店类型': '',
     '酒店设施': ''},
    '餐馆': {'selectedResults': [],
     '人均消费': '',
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '推荐菜': '',
     '评分': ''}},
   {'出租': {'selectedResults': [], '出发地': '', '目的地': ''},
    '地铁': {'selectedResults': [], '出发地': '', '目的地': ''},
    '景点': {'selectedResults': [],
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '游玩时间': '',
     '评分': '',
     '门票': ''},
    '酒店': {'selectedResults': [],
     '价格': '',
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '评分': '',
     '酒店类型': '',
     '酒店设施': ''},
    '餐馆': {'selectedResults': ['鲜鱼口老字号美食街'],
     '人均消费': '50-100元',
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '推荐菜': '美食街',
     '评分': ''}},
   {'出租': {'selectedResults': [], '出发地': '', '目的地': ''},
    '地铁': {'selectedResults': [], '出发地': '', '目的地': ''},
    '景点': {'selectedResults': [],
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '游玩时间': '',
     '评分': '',
     '门票': ''},
    '酒店': {'selectedResults': [],
     '价格': '',
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '评分': '',
     '酒店类型': '',
     '酒店设施': ''},
    '餐馆': {'selectedResults': [],
     '人均消费': '',
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '推荐菜': '',
     '评分': ''}},
   {'出租': {'selectedResults': [], '出发地': '', '目的地': ''},
    '地铁': {'selectedResults': [], '出发地': '', '目的地': ''},
    '景点': {'selectedResults': ['故宫'],
     '名称': '故宫',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '游玩时间': '',
     '评分': '',
     '门票': ''},
    '酒店': {'selectedResults': [],
     '价格': '',
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '评分': '',
     '酒店类型': '',
     '酒店设施': ''},
    '餐馆': {'selectedResults': [],
     '人均消费': '50-100元',
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '推荐菜': '美食街',
     '评分': ''}},
   {'出租': {'selectedResults': [], '出发地': '', '目的地': ''},
    '地铁': {'selectedResults': [], '出发地': '', '目的地': ''},
    '景点': {'selectedResults': [],
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '游玩时间': '',
     '评分': '',
     '门票': ''},
    '酒店': {'selectedResults': [],
     '价格': '',
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '评分': '',
     '酒店类型': '',
     '酒店设施': ''},
    '餐馆': {'selectedResults': [],
     '人均消费': '',
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '推荐菜': '',
     '评分': ''}},
   {'出租': {'selectedResults': [], '出发地': '', '目的地': ''},
    '地铁': {'selectedResults': [], '出发地': '', '目的地': ''},
    '景点': {'selectedResults': ['故宫'],
     '名称': '故宫',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '游玩时间': '',
     '评分': '',
     '门票': ''},
    '酒店': {'selectedResults': [],
     '价格': '',
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '评分': '',
     '酒店类型': '',
     '酒店设施': ''},
    '餐馆': {'selectedResults': [],
     '人均消费': '50-100元',
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '推荐菜': '美食街',
     '评分': ''}},
   {'出租': {'selectedResults': [], '出发地': '', '目的地': ''},
    '地铁': {'selectedResults': [], '出发地': '', '目的地': ''},
    '景点': {'selectedResults': [],
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '游玩时间': '',
     '评分': '',
     '门票': ''},
    '酒店': {'selectedResults': [],
     '价格': '',
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '评分': '',
     '酒店类型': '',
     '酒店设施': ''},
    '餐馆': {'selectedResults': [],
     '人均消费': '',
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '推荐菜': '',
     '评分': ''}},
   {'出租': {'selectedResults': [], '出发地': '', '目的地': ''},
    '地铁': {'selectedResults': [], '出发地': '', '目的地': ''},
    '景点': {'selectedResults': [],
     '名称': '故宫',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '游玩时间': '',
     '评分': '',
     '门票': ''},
    '酒店': {'selectedResults': ['桔子水晶酒店(北京安贞店)'],
     '价格': '',
     '名称': '桔子水晶酒店(北京安贞店)',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '评分': '',
     '酒店类型': '',
     '酒店设施': ''},
    '餐馆': {'selectedResults': [],
     '人均消费': '50-100元',
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '推荐菜': '美食街',
     '评分': ''}},
   {'出租': {'selectedResults': [], '出发地': '', '目的地': ''},
    '地铁': {'selectedResults': [], '出发地': '', '目的地': ''},
    '景点': {'selectedResults': [],
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '游玩时间': '',
     '评分': '',
     '门票': ''},
    '酒店': {'selectedResults': [],
     '价格': '',
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '评分': '',
     '酒店类型': '',
     '酒店设施': ''},
    '餐馆': {'selectedResults': [],
     '人均消费': '',
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '推荐菜': '',
     '评分': ''}},
   {'出租': {'selectedResults': [], '出发地': '', '目的地': ''},
    '地铁': {'selectedResults': [], '出发地': '', '目的地': ''},
    '景点': {'selectedResults': [],
     '名称': '故宫',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '游玩时间': '',
     '评分': '',
     '门票': ''},
    '酒店': {'selectedResults': [],
     '价格': '',
     '名称': '桔子水晶酒店(北京安贞店)',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '评分': '',
     '酒店类型': '',
     '酒店设施': ''},
    '餐馆': {'selectedResults': [],
     '人均消费': '50-100元',
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '推荐菜': '美食街',
     '评分': ''}}],
  'sys_state_init': [{'出租': {'selectedResults': [], '出发地': '', '目的地': ''},
    '地铁': {'selectedResults': [], '出发地': '', '目的地': ''},
    '景点': {'selectedResults': [],
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '游玩时间': '',
     '评分': '',
     '门票': ''},
    '酒店': {'selectedResults': [],
     '价格': '',
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '评分': '',
     '酒店类型': '',
     '酒店设施': ''},
    '餐馆': {'selectedResults': [],
     '人均消费': '',
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '推荐菜': '',
     '评分': ''}},
   {'出租': {'selectedResults': [], '出发地': '', '目的地': ''},
    '地铁': {'selectedResults': [], '出发地': '', '目的地': ''},
    '景点': {'selectedResults': [],
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '游玩时间': '',
     '评分': '',
     '门票': ''},
    '酒店': {'selectedResults': [],
     '价格': '',
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '评分': '',
     '酒店类型': '',
     '酒店设施': ''},
    '餐馆': {'selectedResults': ['鲜鱼口老字号美食街'],
     '人均消费': '50-100元',
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '推荐菜': '美食街',
     '评分': ''}},
   {'出租': {'selectedResults': [], '出发地': '', '目的地': ''},
    '地铁': {'selectedResults': [], '出发地': '', '目的地': ''},
    '景点': {'selectedResults': [],
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '游玩时间': '',
     '评分': '',
     '门票': ''},
    '酒店': {'selectedResults': [],
     '价格': '',
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '评分': '',
     '酒店类型': '',
     '酒店设施': ''},
    '餐馆': {'selectedResults': [],
     '人均消费': '',
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '推荐菜': '',
     '评分': ''}},
   {'出租': {'selectedResults': [], '出发地': '', '目的地': ''},
    '地铁': {'selectedResults': [], '出发地': '', '目的地': ''},
    '景点': {'selectedResults': [],
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '游玩时间': '',
     '评分': '',
     '门票': ''},
    '酒店': {'selectedResults': [],
     '价格': '',
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '评分': '',
     '酒店类型': '',
     '酒店设施': ''},
    '餐馆': {'selectedResults': ['鲜鱼口老字号美食街'],
     '人均消费': '50-100元',
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '推荐菜': '美食街',
     '评分': ''}},
   {'出租': {'selectedResults': [], '出发地': '', '目的地': ''},
    '地铁': {'selectedResults': [], '出发地': '', '目的地': ''},
    '景点': {'selectedResults': [],
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '游玩时间': '',
     '评分': '',
     '门票': ''},
    '酒店': {'selectedResults': [],
     '价格': '',
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '评分': '',
     '酒店类型': '',
     '酒店设施': ''},
    '餐馆': {'selectedResults': [],
     '人均消费': '',
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '推荐菜': '',
     '评分': ''}},
   {'出租': {'selectedResults': [], '出发地': '', '目的地': ''},
    '地铁': {'selectedResults': [], '出发地': '', '目的地': ''},
    '景点': {'selectedResults': [],
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '游玩时间': '',
     '评分': '',
     '门票': ''},
    '酒店': {'selectedResults': [],
     '价格': '',
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '评分': '',
     '酒店类型': '',
     '酒店设施': ''},
    '餐馆': {'selectedResults': ['鲜鱼口老字号美食街'],
     '人均消费': '50-100元',
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '推荐菜': '美食街',
     '评分': ''}},
   {'出租': {'selectedResults': [], '出发地': '', '目的地': ''},
    '地铁': {'selectedResults': [], '出发地': '', '目的地': ''},
    '景点': {'selectedResults': [],
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '游玩时间': '',
     '评分': '',
     '门票': ''},
    '酒店': {'selectedResults': [],
     '价格': '',
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '评分': '',
     '酒店类型': '',
     '酒店设施': ''},
    '餐馆': {'selectedResults': [],
     '人均消费': '',
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '推荐菜': '',
     '评分': ''}},
   {'出租': {'selectedResults': [], '出发地': '', '目的地': ''},
    '地铁': {'selectedResults': [], '出发地': '', '目的地': ''},
    '景点': {'selectedResults': ['故宫'],
     '名称': '故宫',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '游玩时间': '',
     '评分': '',
     '门票': ''},
    '酒店': {'selectedResults': [],
     '价格': '',
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '评分': '',
     '酒店类型': '',
     '酒店设施': ''},
    '餐馆': {'selectedResults': ['鲜鱼口老字号美食街'],
     '人均消费': '50-100元',
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '推荐菜': '美食街',
     '评分': ''}},
   {'出租': {'selectedResults': [], '出发地': '', '目的地': ''},
    '地铁': {'selectedResults': [], '出发地': '', '目的地': ''},
    '景点': {'selectedResults': [],
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '游玩时间': '',
     '评分': '',
     '门票': ''},
    '酒店': {'selectedResults': [],
     '价格': '',
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '评分': '',
     '酒店类型': '',
     '酒店设施': ''},
    '餐馆': {'selectedResults': [],
     '人均消费': '',
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '推荐菜': '',
     '评分': ''}},
   {'出租': {'selectedResults': [], '出发地': '', '目的地': ''},
    '地铁': {'selectedResults': [], '出发地': '', '目的地': ''},
    '景点': {'selectedResults': ['故宫'],
     '名称': '故宫',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '游玩时间': '',
     '评分': '',
     '门票': ''},
    '酒店': {'selectedResults': [],
     '价格': '',
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '评分': '',
     '酒店类型': '',
     '酒店设施': ''},
    '餐馆': {'selectedResults': [],
     '人均消费': '50-100元',
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '推荐菜': '美食街',
     '评分': ''}},
   {'出租': {'selectedResults': [], '出发地': '', '目的地': ''},
    '地铁': {'selectedResults': [], '出发地': '', '目的地': ''},
    '景点': {'selectedResults': [],
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '游玩时间': '',
     '评分': '',
     '门票': ''},
    '酒店': {'selectedResults': [],
     '价格': '',
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '评分': '',
     '酒店类型': '',
     '酒店设施': ''},
    '餐馆': {'selectedResults': [],
     '人均消费': '',
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '推荐菜': '',
     '评分': ''}},
   {'出租': {'selectedResults': [], '出发地': '', '目的地': ''},
    '地铁': {'selectedResults': [], '出发地': '', '目的地': ''},
    '景点': {'selectedResults': ['故宫'],
     '名称': '故宫',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '游玩时间': '',
     '评分': '',
     '门票': ''},
    '酒店': {'selectedResults': ['桔子水晶酒店(北京安贞店)'],
     '价格': '',
     '名称': '桔子水晶酒店(北京安贞店)',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '评分': '',
     '酒店类型': '',
     '酒店设施': ''},
    '餐馆': {'selectedResults': [],
     '人均消费': '50-100元',
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '推荐菜': '美食街',
     '评分': ''}},
   {'出租': {'selectedResults': [], '出发地': '', '目的地': ''},
    '地铁': {'selectedResults': [], '出发地': '', '目的地': ''},
    '景点': {'selectedResults': [],
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '游玩时间': '',
     '评分': '',
     '门票': ''},
    '酒店': {'selectedResults': [],
     '价格': '',
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '评分': '',
     '酒店类型': '',
     '酒店设施': ''},
    '餐馆': {'selectedResults': [],
     '人均消费': '',
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '推荐菜': '',
     '评分': ''}},
   {'出租': {'selectedResults': [], '出发地': '', '目的地': ''},
    '地铁': {'selectedResults': [], '出发地': '', '目的地': ''},
    '景点': {'selectedResults': [],
     '名称': '故宫',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '游玩时间': '',
     '评分': '',
     '门票': ''},
    '酒店': {'selectedResults': ['桔子水晶酒店(北京安贞店)'],
     '价格': '',
     '名称': '桔子水晶酒店(北京安贞店)',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '评分': '',
     '酒店类型': '',
     '酒店设施': ''},
    '餐馆': {'selectedResults': [],
     '人均消费': '50-100元',
     '名称': '',
     '周边景点': '',
     '周边酒店': '',
     '周边餐馆': '',
     '推荐菜': '美食街',
     '评分': ''}}],
  'user_state': [[['1', '餐馆', '人均消费', '50-100元', 'True'],
    ['1', '餐馆', '推荐菜', "['美食街']", 'True'],
    ['1', '餐馆', '名称', '', 'True'],
    ['1', '餐馆', '营业时间', '', 'False'],
    ['1', '餐馆', '周边景点', '[]', 'False'],
    ['2', '景点', '名称', '出现在id=1的周边景点里', 'False'],
    ['2', '景点', '评分', '4.5分以上', 'False'],
    ['2', '景点', '地址', '', 'False'],
    ['2', '景点', '电话', '', 'False'],
    ['3', '酒店', '名称', '桔子水晶酒店(北京安贞店)', 'False'],
    ['3', '酒店', '电话', '', 'False']],
   [],
   [['1', '餐馆', '人均消费', '50-100元', 'True'],
    ['1', '餐馆', '推荐菜', "['美食街']", 'True'],
    ['1', '餐馆', '名称', '鲜鱼口老字号美食街', 'True'],
    ['1', '餐馆', '营业时间', '', 'True'],
    ['1', '餐馆', '周边景点', '[]', 'False'],
    ['2', '景点', '名称', '出现在id=1的周边景点里', 'False'],
    ['2', '景点', '评分', '4.5分以上', 'False'],
    ['2', '景点', '地址', '', 'False'],
    ['2', '景点', '电话', '', 'False'],
    ['3', '酒店', '名称', '桔子水晶酒店(北京安贞店)', 'False'],
    ['3', '酒店', '电话', '', 'False']],
   [],
   [['1', '餐馆', '人均消费', '50-100元', 'True'],
    ['1', '餐馆', '推荐菜', "['美食街']", 'True'],
    ['1', '餐馆', '名称', '鲜鱼口老字号美食街', 'True'],
    ['1', '餐馆', '营业时间', '周一至周日 10:00-22:00', 'True'],
    ['1', '餐馆', '周边景点', '[]', 'True'],
    ['2', '景点', '名称', '出现在id=1的周边景点里', 'False'],
    ['2', '景点', '评分', '4.5分以上', 'False'],
    ['2', '景点', '地址', '', 'False'],
    ['2', '景点', '电话', '', 'False'],
    ['3', '酒店', '名称', '桔子水晶酒店(北京安贞店)', 'False'],
    ['3', '酒店', '电话', '', 'False']],
   [],
   [['1', '餐馆', '人均消费', '50-100元', 'True'],
    ['1', '餐馆', '推荐菜', "['美食街']", 'True'],
    ['1', '餐馆', '名称', '鲜鱼口老字号美食街', 'True'],
    ['1', '餐馆', '营业时间', '周一至周日 10:00-22:00', 'True'],
    ['1', '餐馆', '周边景点', "['天安门广场', '前门大街', '恭王府', '故宫']", 'True'],
    ['2', '景点', '名称', '出现在id=1的周边景点里', 'True'],
    ['2', '景点', '评分', '4.5分以上', 'True'],
    ['2', '景点', '地址', '', 'False'],
    ['2', '景点', '电话', '', 'False'],
    ['3', '酒店', '名称', '桔子水晶酒店(北京安贞店)', 'False'],
    ['3', '酒店', '电话', '', 'False']],
   [],
   [['1', '餐馆', '人均消费', '50-100元', 'True'],
    ['1', '餐馆', '推荐菜', "['美食街']", 'True'],
    ['1', '餐馆', '名称', '鲜鱼口老字号美食街', 'True'],
    ['1', '餐馆', '营业时间', '周一至周日 10:00-22:00', 'True'],
    ['1', '餐馆', '周边景点', "['天安门广场', '前门大街', '恭王府', '故宫']", 'True'],
    ['2', '景点', '名称', '故宫', 'True'],
    ['2', '景点', '评分', '4.5分以上', 'True'],
    ['2', '景点', '地址', '', 'True'],
    ['2', '景点', '电话', '', 'True'],
    ['3', '酒店', '名称', '桔子水晶酒店(北京安贞店)', 'False'],
    ['3', '酒店', '电话', '', 'False']],
   [],
   [['1', '餐馆', '人均消费', '50-100元', 'True'],
    ['1', '餐馆', '推荐菜', "['美食街']", 'True'],
    ['1', '餐馆', '名称', '鲜鱼口老字号美食街', 'True'],
    ['1', '餐馆', '营业时间', '周一至周日 10:00-22:00', 'True'],
    ['1', '餐馆', '周边景点', "['天安门广场', '前门大街', '恭王府', '故宫']", 'True'],
    ['2', '景点', '名称', '故宫', 'True'],
    ['2', '景点', '评分', '4.5分以上', 'True'],
    ['2', '景点', '地址', '北京市东城区景山前街4号', 'True'],
    ['2', '景点', '电话', '010-85007938', 'True'],
    ['3', '酒店', '名称', '桔子水晶酒店(北京安贞店)', 'True'],
    ['3', '酒店', '电话', '', 'True']],
   [],
   [['1', '餐馆', '人均消费', '50-100元', 'True'],
    ['1', '餐馆', '推荐菜', "['美食街']", 'True'],
    ['1', '餐馆', '名称', '鲜鱼口老字号美食街', 'True'],
    ['1', '餐馆', '营业时间', '周一至周日 10:00-22:00', 'True'],
    ['1', '餐馆', '周边景点', "['天安门广场', '前门大街', '恭王府', '故宫']", 'True'],
    ['2', '景点', '名称', '故宫', 'True'],
    ['2', '景点', '评分', '4.5分以上', 'True'],
    ['2', '景点', '地址', '北京市东城区景山前街4号', 'True'],
    ['2', '景点', '电话', '010-85007938', 'True'],
    ['3', '酒店', '名称', '桔子水晶酒店(北京安贞店)', 'True'],
    ['3', '酒店', '电话', '010-84273030', 'True']],
   []]},
 'sys_id': 96,
 'task description': ['你要去一个餐馆(id=1)用餐。你希望餐馆的人均消费是50-100元的。你想吃的菜肴是美食街。你想知道这个餐馆的名称、营业时间、周边景点。',
  '你要去id=1附近的景点(id=2)游玩。你希望景点的评分是4.5分以上。你想知道这个景点的地址、电话。',
  '你要去名叫桔子水晶酒店(北京安贞店)的酒店(id=3)住宿。你想知道这个酒店的电话。'],
 'type': '不独立多领域',
 'usr_id': 97}
```

#### Data Splits

<!-- info: Describe and name the splits in the dataset if there are more than one. -->
<!-- scope: periscope -->
| Split                 | Train  | Valid | Test  |
| --------------------- | ------ | ----- | ----- |
| \# dialogues          | 5,012  | 500   | 500   |
| \# Turns (utterances) | 84,692 | 8,458 | 8,476 |
| Vocab                 | 12,502 | 5,202 | 5,143 |
| Avg. sub-goals        | 3.24   | 3.26  | 3.26  |
| Avg. semantic tuples  | 14.8   | 14.9  | 15.0  |
| Avg. turns            | 16.9   | 16.9  | 17.0  |
| Avg. tokens per turn  | 16.3   | 16.3  | 16.2  |



## Dataset in GEM

### Rationale for Inclusion in GEM

#### Why is the Dataset in GEM?

<!-- info: What does this dataset contribute toward better generation evaluation and why is it part of GEM? -->
<!-- scope: microscope -->
CrossWOZ is the first large-scale Chinese Cross-Domain Wizard-of-Oz task-oriented dataset.

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
The corpus contains rich annotation of dialogue states and dialogue acts at both user and system sides, which can be used in a wide range of tasks.

#### Ability that the Dataset measures

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: periscope -->
Dialog understanding, dialog policy learning


### GEM-Specific Curation

#### Modificatied for GEM?

<!-- info: Has the GEM version of the dataset been modified in any way (data, processing, splits) from the original curated data? -->
<!-- scope: telescope -->
yes

#### GEM Modifications

<!-- info: What changes have been made to he original dataset? -->
<!-- scope: periscope -->
`other`

#### Modification Details

<!-- info: For each of these changes, described them in more details and provided the intended purpose of the modification -->
<!-- scope: microscope -->
To adapt to hugging face Datasets, we 1) separate user annotators' ID and system annotations' ID; 2) we convert the data type in goal/user state to string.

#### Additional Splits?

<!-- info: Does GEM provide additional splits to the dataset? -->
<!-- scope: telescope -->
no


### Getting Started with the Task

#### Pointers to Resources

<!-- info: Getting started with in-depth research on the task. Add relevant pointers to resources that researchers can consult when they want to get started digging deeper into the task. -->
<!-- scope: microscope -->
[Code](https://github.com/thu-coai/Convlab-2)

#### Technical Terms

<!-- info: Technical terms used in this card and the dataset and their definitions -->
<!-- scope: microscope -->
According to the type of user goal, we group the dialogues in the training set into five categories:
- S: 417 dialogues have only one sub-goal in HAR domains.
- M: 1573 dialogues have multiple sub-goals (2-3) in HAR domains. However, these sub-goals do not have cross-domain informable slots.
- M+T: 691 dialogues have multiple sub-goals in HAR domains and at least one sub-goal in the metro or taxi domain (3-5 sub-goals). The sub-goals in HAR domains do not have cross-domain informable slots.
- CM: 1,759 dialogues have multiple sub-goals (2-5) in HAR domains with cross-domain informable slots.
- CM+T: 572 dialogues have multiple sub-goals in HAR domains with cross-domain informable slots and at least one sub-goal in the metro or taxi domain (3-5 sub-goals).




## Previous Results

### Previous Results

#### Measured Model Abilities

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: telescope -->
Dialog understanding, dialog policy learning

#### Metrics

<!-- info: What metrics are typically used for this task? -->
<!-- scope: periscope -->
`BLEU`

#### Proposed Evaluation

<!-- info: List and describe the purpose of the metrics and evaluation methodology (including human evaluation) that the dataset creators used when introducing this task. -->
<!-- scope: microscope -->
BLEU evaluates the generation quality.

#### Previous results available?

<!-- info: Are previous results available? -->
<!-- scope: telescope -->
yes

#### Other Evaluation Approaches

<!-- info: What evaluation approaches have others used? -->
<!-- scope: periscope -->
Inform rate: how many entities in the gold response appear in the generated response.

#### Relevant Previous Results

<!-- info: What are the most relevant previous results for this task/dataset? -->
<!-- scope: microscope -->
BLEU on MultiWOZ dataset.



## Dataset Curation

### Original Curation

#### Original Curation Rationale

<!-- info: Original curation rationale -->
<!-- scope: telescope -->
Gather human-to-human dialog in Chinese.

#### Communicative Goal

<!-- info: What was the communicative goal? -->
<!-- scope: periscope -->
Generate a response according to the dialog context and database search results.

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
`Participatory experiment`

#### Language Producers

<!-- info: What further information do we have on the language producers? -->
<!-- scope: microscope -->
An usr/sys ID indicates the creator of different data points.

#### Topics Covered

<!-- info: Does the language in the dataset focus on specific topics? How would you describe them? -->
<!-- scope: periscope -->
domains: attraction, hotel, restaurant, metro, taxi

#### Data Validation

<!-- info: Was the text validated by a different worker or a data curator? -->
<!-- scope: telescope -->
validated by data curator

#### Was Data Filtered?

<!-- info: Were text instances selected or filtered? -->
<!-- scope: telescope -->
not filtered


### Structured Annotations

#### Additional Annotations?

<!-- quick -->
<!-- info: Does the dataset have additional annotations for each instance? -->
<!-- scope: telescope -->
none

#### Annotation Service?

<!-- info: Was an annotation service used? -->
<!-- scope: telescope -->
no


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
unlikely

#### Categories of PII

<!-- info: What categories of PII are present or suspected in the data? -->
<!-- scope: periscope -->
`generic PII`

#### Any PII Identification?

<!-- info: Did the curators use any automatic/manual method to identify PII in the dataset? -->
<!-- scope: periscope -->
no identification


### Maintenance

#### Any Maintenance Plan?

<!-- info: Does the original dataset have a maintenance plan? -->
<!-- scope: telescope -->
no



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
CrossWOZ is the first large-scale Chinese Cross-Domain Wizard-of-Oz task-oriented dataset. The corpus contains rich annotation of dialogue states and dialogue acts at both user and system sides, which can be used in a wide range of tasks.


### Discussion of Biases

#### Any Documented Social Biases?

<!-- info: Are there documented social biases in the dataset? Biases in this context are variations in the ways members of different social categories are represented that can have harmful downstream consequences for members of the more disadvantaged group. -->
<!-- scope: telescope -->
no

#### Are the Language Producers Representative of the Language?

<!-- info: Does the distribution of language producers in the dataset accurately represent the full distribution of speakers of the language world-wide? If not, how does it differ? -->
<!-- scope: periscope -->
Yes



## Considerations for Using the Data

### PII Risks and Liability

#### Potential PII Risk

<!-- info: Considering your answers to the PII part of the Data Curation Section, describe any potential privacy to the data subjects and creators risks when using the dataset. -->
<!-- scope: microscope -->
No


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
No

#### Unsuited Applications

<!-- info: When using a model trained on this dataset in a setting where users or the public may interact with its predictions, what are some pitfalls to look out for? In particular, describe some applications of the general task featured in this dataset that its curation or properties make it less suitable for. -->
<!-- scope: microscope -->
Model may not handle unknown values in the dialog

#### Discouraged Use Cases

<!-- info: What are some discouraged use cases of a model trained to maximize the proposed metrics on this dataset? In particular, think about settings where decisions made by a model that performs reasonably well on the metric my still have strong negative consequences for user or members of the public. -->
<!-- scope: microscope -->
Responses can be diverse, which is not captured by BLEU


