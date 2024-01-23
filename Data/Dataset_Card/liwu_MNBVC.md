---
annotations_creators:
- other
language:
- zh
language_creators:
- other
license:
- mit
multilinguality:
- monolingual
pretty_name: MNBVC
size_categories:
- unknown
source_datasets:
- original
task_categories:
- text-generation
- fill-mask
task_ids:
- language-modeling
- masked-language-modeling
---

# Dataset Card for [Dataset Name]

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Homepage:** http://mnbvc.253874.net/
- **Repository:** https://github.com/esbatmop/MNBVC
- **Paper:** N/A
- **Leaderboard:** N/A
- **Point of Contact:** N/A

### Dataset Summary

中文互联网上最古老最神秘(没有之一)的里屋社区于2023.1.1庄重宣布:

MNBVC项目组在英明神武的里屋管子带领下，决心发挥社区所长(哪都长)，帮助开源社区长期更新一份最大的中文互联网语料集。

MNBVC数据集不但包括主流文化，也包括各个小众文化甚至火星文的数据。MNBVC数据集包括新闻、作文、小说、书籍、杂志、论文、台词、帖子、wiki、古诗、歌词、商品介绍、笑话、糗事、聊天记录等一切形式的纯文本中文数据。数据均来源于互联网收集。

可以使用如下脚本加载：

```python
from datasets import load_dataset
dataset = load_dataset("liwu/MNBVC", 'law_judgement', split='train', streaming=True)

next(iter(dataset))  # get the first line
```

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

MNBVC数据集为中文数据集

## Dataset Structure

### Data Instances

#### law_judgement

```json
{
  "text": "黑龙江省齐齐哈尔市梅里斯达斡尔区人民法院 民 事 判 决 书 （2016）黑0208民初1497号 原告王某某，男，1996年6月5日出生，汉族，农民。 委托代理人王某某，系黑龙江发达律师事务所律师。 被告中国人民财产保险股份有限公司齐齐哈尔市梅里斯达斡尔族区支公司，住所地黑龙江省齐齐哈尔市梅里斯达斡尔族区城镇。 代表人王某某，系该公司经理。 委托代理人李某某，系黑龙江宇恒律师事务所律师。 委托代理人张某某，系黑龙江宇恒律师事务所律师。 被告吕某，男，1987年2月6日出生，汉族，农民。 原告王某某与被告中国人民财产保险股份有限公司齐齐哈尔市梅里斯达斡尔族区支公司[以下简称人保财险梅里斯支公司]、吕某机动车交通事故责任纠纷一案,原告于2016年9月14日向本院提起诉讼，本院受理后，依法适用普通程序由审判员马国富担任审判长，与人民陪审员毕从志、吴淑霞共同组成合议庭，于2016年10月19日公开开庭进行了审理。原告王某某委托代理人王某某、被告人保财险梅里斯支公司委托代理人张某某到庭参加了诉讼。被告吕某经本院传票传唤无正当理由未到庭参加诉讼。本案现已缺席审理终结。 原告王某某诉称，2014年5月24日16时许，被告吕某驾驶黑BV86**号轿车，在梅里斯区育德街与碾北公路交叉口由北向东左转弯时，与沿碾北公路由西向东原告驾驶的无号牌两轮摩托车相撞，造成双方车辆损坏，原告受伤的后果。原告在齐齐哈尔市公安医院住院治疗7天，出院诊断为：1、急性闭合性颅脑损伤；2、左颞顶部硬膜外血肿；3、左颞顶固骨折；4、左颞头皮下血肿伴擦皮伤；5、右肘擦皮伤；住院期间，一级护理4天、二级护理3天。经齐齐哈尔市梅里斯区交通警察大队《道路交通事故认定书》（简易程序）第2302083201400018号认定：被告吕某对该起事故负主要责任。被告吕某驾驶的肇事车辆在人保财险梅里斯支公司处投保了交强险，且事故发生在保险期间内。现要求被告人保财险梅里斯支公司在机动车强制保险责任范围内赔偿原告医药费8993.00元、护理费1573.00元、交通费200.00元、误工费1001.00元、伙食补助费700.00元，合计12467.00元，并要求被告吕某承担连带赔偿责任。 原告为证明其诉讼主张，提供了如下证据： 1、交通事故责任认定书； 2、齐齐哈尔市公安医院医疗费用明细单； 3、医疗费票据； 4、陪护证明； 5、住院诊断书； 6、住院病案； 7、误工证明。 被告人保财险梅里斯支公司辩称，被告吕某驾驶的肇事车辆在我公司投保交强险属实，事故发生在保险期间内，同意在交强险各项赔偿限额内对原告合理损失予以赔偿。交通费原告未提供有效票据，拒绝赔偿。 被告人保财险梅里斯支公司未向法庭提供证据。 被告吕某未到庭应诉、未答辩亦未向法庭提供证据。 在开庭审理过程中，被告人保财险梅里斯支公司对原告提供的证据表示无异议。 结合原、被告的陈述、辩论及对证据的质证意见，本院经审核后认为，原告提供的证据符合证据的要求，本院认定其对本案的证明效力。 根据以上确认的证据和双方当事人的陈述，可以认定如下事实：2014年5月24日16时许，吕某驾驶黑BV86**号轿车，在梅里斯区育德街与碾北公路交叉口由北向东左转弯时，与沿碾北公路由西向东王某某驾驶的无号牌两轮摩托车相撞，造成双方车辆损坏，王某某受伤的后果。经齐齐哈尔市公安局交警支队梅里斯交通警察大队“道路交通事故认定书”认定：吕某驾驶机动车左转弯未让直行车辆先行，负事故主要责任；王某某未依法取得机动车驾驶证，驾驶无号牌机动车，遇情况采取措施不当，未确保安全，负事故次要责任。2014年5月24日，原告王某某在齐齐哈尔市公安医院住院治疗，于2014年5月30日出院，经诊断为：1、急性闭合性颅脑损伤；2、左颞顶部硬膜外血肿；3、左颞顶固骨折；4、左颞头皮下血肿伴擦皮伤；5、右肘擦皮伤；住院期间，一级护理4天、二级护理3天。 被告吕某驾驶的黑BV86**号轿车在人保财险梅里斯支公司投保了机动车第三者责任强制保险，死亡伤残赔偿限额为110000.00元；医疗费用赔偿限额为10000.00元；财产损失赔偿限额为2000.00元。 原告王某某因此次交通事故所产生的损失为：1、医疗费8993.00元；2、住院伙食补助费700.00元［100.00元/天（2015年黑龙江省国家机关工作人员出差补助标准）×7日］；3、误工费966.00元［50275.00元/年（2015年黑龙江省居民服务和其他服务业就业人员工资）×7日］；4、护理费1518.00元［50275.00元/年（2015年黑龙江省居民服务和其他服务业就业人员工资）×4日×2人＋50275.00元/年（2015年黑龙江省居民服务和其他服务业就业人员工资）×3日×1人］；5、交通费21.00元（3.00元/日×7日），以上合计12198.00元。 据以上事实，本院认为，我国法律规定，公民的生命健康权依法应当予以保护。被告吕某驾驶的事故车辆在被告人保财险梅里斯支公司投保了机动车第三者责任强制保险，在此次交通事故中，吕某负事故主要责任，原告要求赔偿损失金额在人保财险梅里斯支公司机动车第三者责任强制保险责任限额内，故原告要求被告人保财险梅里斯支公司承担赔偿责任的诉讼请求应予支持。为了保护原告人的合法权益，依照《中华人民共和国道路交通安全法》第七十六条和《中华人民共和国民事诉讼法》第一百四十二条、一百四十四条的规定，判决如下： 一、被告人保财险梅里斯支公司赔偿原告王某某医疗费、住院伙食补助费、误工费、护理费、交通费计12198.00元，此款于本判决生效后10日内付清； 二、驳回原告其他诉讼请求。 如果被告人保财险梅里斯支公司未按本判决指定的期间履行给付金钱的义务，应当依照《中华人民共和国民事诉讼法》第二百五十三条的规定，加倍支付迟延履行期间的债务利息。 案件受理费112.00元由被告人保财险梅里斯支公司负担。 如果不服本判决，可在判决书送达之日起十五日内，向本院递交上诉状，并按对方当事人的人数提出副本，上诉于齐齐哈尔市中级人民法院。 申请执行期间为二年。 审 判 长 马国富 人民陪审员 毕从志 人民陪审员 吴淑霞 二〇一六年十月二十四日 书 记 员 多艳霞",
  "meta": "{"分卷名": "02", "案件id": "1"}",
}
```

### Data Fields

#### free_law
- text (str): 文本内容。
- meta (dict): 其他多余字段。

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

Thanks to the [Liwu community](http://mnbvc.253874.net/) for constructing this dataset.
Thanks to [silver](https://github.com/silverriver) for adding this dataset.