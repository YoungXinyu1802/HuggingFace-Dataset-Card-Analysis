---
annotations_creators:
- no-annotation
language_creators:
- crowdsourced
language:
- ko
license:
- cc-by-nc-sa-2.0
multilinguality:
- monolingual
pretty_name: Namuwiki database dump (2021-03-01)
size_categories:
- 100K<n<1M
source_datasets:
- original
task_categories:
- fill-mask
- text-generation
task_ids:
- masked-language-modeling
- language-modeling
---

# Namuwiki database dump (2021-03-01)

## Dataset Description

- **Homepage:** [나무위키:데이터베이스 덤프](https://namu.wiki/w/%EB%82%98%EB%AC%B4%EC%9C%84%ED%82%A4:%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4%20%EB%8D%A4%ED%94%84)
- **Repository:** [Needs More Information]
- **Paper:** [Needs More Information]
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [Needs More Information]

## Namuwiki

https://namu.wiki/

It is a Korean wiki based on the seed engine, established on April 17, 2015 (KST).

## About dataset

All data from Namuwiki collected on 2021-03-01. I filtered data without text(mostly redirecting documents).

You can download the original data converted to csv in [Kaggle](https://www.kaggle.com/datasets/brainer3220/namu-wiki).

## 2022-03-01 dataset

[heegyu/namuwiki](https://huggingface.co/datasets/heegyu/namuwiki)<br>
[heegyu/namuwiki-extracted](https://huggingface.co/datasets/heegyu/namuwiki-extracted)<br>
[heegyu/namuwiki-sentences](https://huggingface.co/datasets/heegyu/namuwiki-sentences)

### Lisence

[CC BY-NC-SA 2.0 KR](https://creativecommons.org/licenses/by-nc-sa/2.0/kr/)

## Data Structure

### Data Instance

```pycon
>>> from datasets import load_dataset

>>> dataset = load_dataset("Bingsu/namuwiki_20210301_filtered")
>>> dataset
DatasetDict({
    train: Dataset({
        features: ['title', 'text'],
        num_rows: 571308
    })
})
```

```pycon
>>> dataset["train"].features
{'title': Value(dtype='string', id=None),
 'text': Value(dtype='string', id=None)}
```

### Data Size

download: 3.26 GiB<br>
generated: 3.73 GiB<br>
total: 6.99 GiB

### Data Field

- title: `string`
- text: `string`

### Data Splits

|            |  train |
| ---------- | ------ |
| # of texts | 571308 |


```pycon
>>> dataset["train"][2323]
{'title': '55번 지방도',
 'text': '55번 국가지원지방도\n해남 ~ 금산\n시점 전라남도 해남군 북평면 남창교차로\n종점 충청남도 금산군 금산읍 우체국사거리\n총 구간 279.2km\n경유지 전라남도 강진군, 장흥군, 영암군 전라남도 나주시, 화순군 광주광역시 동구, 북구 전라남도 담양군 전라북도 순창군, 정읍시, 완주군 전라북도 임실군, 진안군\n개요\n국가지원지방도 제55호선은 전라남도 해남군에서 출발하여 충청남도 금산군까지 이어지는 대한민국의 국가지원지방도이다.\n전라남도 해남군 북평면 - 전라남도 강진군 도암면 구간은 광주광역시, 전라남도 동부권, 영남 지방에서 완도군 완도읍으로 갈 때 주로 이용된다.] 해남 - 완도구간이 확장되기 전에는 그랬다. 강진군, 장흥군은 예외]\n노선\n전라남도\n해남군\n백도로\n북평면 남창교차로에서 13번 국도, 77번 국도와 만나며 출발한다.\n쇄노재\n북일면 북일초교 앞에서 827번 지방도와 만난다.\n강진군\n백도로\n도암면소재지 사거리에서 819번 지방도와 만난다. 819번 지방도는 망호선착장까지만 길이 있으며, 뱃길을 통해 간접적으로 바다 건너의 819번 지방도와 연결된다.\n석문공원\n도암면 계라교차로에서 18번 국도에 합류한다. 우회전하자. 이후 강진읍까지 18번 국도와 중첩되고 장흥군 장흥읍까지 2번 국도와 중첩된다. 그리고 장흥읍부터 영암군을 거쳐 나주시 세지면까지는 23번 국도와 중첩된다.\n나주시\n동창로\n세지면 세지교차로에서 드디어 23번 국도로부터 분기하면서 820번 지방도와 직결 합류한다. 이 길은 2013년 현재 확장 공사 중이다. 확장공사가 완료되면 동창로가 55번 지방도 노선이 된다.\n세남로\n봉황면 덕림리 삼거리에서 820번 지방도와 분기한다.\n봉황면 철천리 삼거리에서 818번 지방도와 합류한다.\n봉황면 송현리 삼거리에서 818번 지방도와 분기한다.\n송림산제길\n동창로\n여기부터 완공된 왕복 4차로 길이다. 이 길을 만들면서 교통량이 늘어났지만 주변 농민들이 이용하는 농로의 교량을 설치하지 않아 문제가 생기기도 했다. #1 #2\n세남로\n남평읍에서 다시 왕복 2차로로 줄어든다.\n남평읍 남평오거리에서 822번 지방도와 만난다.\n산남로\n남평교를 건너고 남평교사거리에서 우회전\n동촌로\n남평역\n화순군\n동촌로\n화순읍 앵남리 삼거리에서 817번 지방도와 합류한다. 좌회전하자.\n앵남역\n지강로\n화순읍 앵남리 앵남교차로에서 817번 지방도와 분기한다. 앵남교차로부터 나주 남평읍까지 55번 지방도의 확장공사가 진행중이다.\n오성로\n여기부터 화순읍 대리사거리까지 왕복 4차선으로 확장 공사를 진행했고, 2015년 8월 말 화순읍 구간은 왕복 4차선으로 확장되었다.\n화순역\n화순읍에서 광주광역시 동구까지 22번 국도와 중첩되고, 동구부터 전라북도 순창군 쌍치면까지는 29번 국도와 중첩된다.\n전라북도\n순창군\n청정로\n29번 국도를 따라가다가 쌍치면 쌍길매삼거리에서 우회전하여 21번 국도로 들어가자. 쌍치면 쌍치사거리에서 21번 국도와 헤어진다. 직진하자.\n정읍시\n청정로\n산내면 산내사거리에서 715번 지방도와 직결하면서 30번 국도에 합류한다. 좌회전하여 구절재를 넘자.\n산외로\n칠보면 시산교차로에서 49번 지방도와 교차되면 우회전하여 49번 지방도와 합류한다. 이제 오랜 시간 동안 49번 지방도와 합류하게 될 것이다.\n산외면 산외교차로에서 715번 지방도와 교차한다.\n엄재터널\n완주군\n산외로\n구이면 상용교차로에서 27번 국도에 합류한다. 좌회전하자.\n구이로\n구이면 백여교차로에서 27번 국도로부터 분기된다.\n구이면 대덕삼거리에서 714번 지방도와 만난다.\n구이면 염암삼거리에서 우회전\n신덕평로\n고개가 있다. 완주군과 임실군의 경계이다.\n임실군\n신덕평로\n신덕면 외량삼거리, 삼길삼거리에서 749번 지방도와 만난다.\n야트막한 고개가 하나 있다.\n신평면 원천리 원천교차로에서 745번 지방도와 교차한다.\n신평면 관촌역 앞에서 17번 국도와 합류한다. 좌회전하자.\n관진로\n관촌면 병암삼거리에서 17번 국도로부터 분기된다.\n순천완주고속도로와 교차되나 연결되지 않는다.\n진안군\n관진로\n성수면 좌산리에서 721번 지방도와 만난다.\n성수면 좌산리 좌산삼거리에서 721번 지방도와 만난다.\n마령면 강정교차로 부근에서 745번 지방도와 만난다.\n익산포항고속도로와 교차되나 연결되지 않는다.\n진안읍 진안연장농공단지 앞에서 26번 국도에 합류한다. 좌회전하자.\n전진로\n부귀면 부귀교차로에서 드디어 49번 지방도를 떠나보낸다. 그러나 아직 26번 국도와 중첩된다.\n완주군\n동상로\n드디어 55번이라는 노선 번호가 눈에 보이기 시작한다. 완주군 소양면에서 26번 국도와 분기된다. 이제부터 꼬불꼬불한 산길이므로 각오하고 운전하자.\n밤치. 소양면과 동상면의 경계가 되는 고개다.\n동상면 신월삼거리에서 732번 지방도와 만난다. 동상저수지에 빠지지 않도록 주의하자.\n동상주천로\n운장산고개를 올라가야 한다. 완주군과 진안군의 경계다. 고개 정상에 휴게소가 있다.\n진안군\n동상주천로\n주천면 주천삼거리에서 725번 지방도와 만난다.\n충청남도\n금산군\n보석사로\n남이면 흑암삼거리에서 635번 지방도와 만난다. 우회전해야 한다. 네이버 지도에는 좌회전해서 좀더 가면 나오는 길을 55번 지방도라고 써놓았는데, 잘못 나온 거다. 다음 지도에는 올바르게 나와있다.\n십이폭포로\n남이면에서 남일면으로 넘어간다.\n남일면에서 13번 국도와 합류한다. 좌회전하자. 이후 구간은 남이면을 거쳐 금산읍까지 13번 국도와 중첩되면서 55번 지방도 구간은 종료된다.'}
```
