---
license: cc-by-nc-sa-2.0
language:
- ko
language_creators:
- other
multilinguality:
- monolingual
size_categories:
- 100K<n<1M
task_categories:
- other
---
# namu.wiki database dump
##
https://namu.wiki/ database dump 2022/03/01<br/>
- 571308rows
- download size: 2.19GB

## 주의사항
namu-wiki-extractor를 이용하여 전처리, 추가로 아래 전처리를 수행했습니다
1. 헤더 제거 `== 개요 ==`
1. 테이블 제거
1. `[age(1997-01-01)]` 는 전처리 시점 기준으로 적용(2022년 10월 2일)
1. `[math(a / b + c)]` 는 제거하지 않음.
1. math 마크다운이 각주 내에 있을 경우, 각주가 전처리되지 않은 문제 있음.


## Usage
```bash
pip install datasets
```

```python
from datasets import load_dataset
dataset = load_dataset("heegyu/namuwiki-extracted")
print(dataset["train"][0])
```
```
{
'title': '!!아앗!!', 
'text': '！！ああっと！！ ▲신 세계수의 미궁 2에서 뜬 !!아앗!! 세계수의 미궁 시리즈에 전통으로 등장하는 대사. 2편부터 등장했으며 훌륭한 사망 플래그의 예시이다. 세계수의 모험가들이 탐험하는 던전인 수해의 구석구석에는 채취/벌채/채굴 포인트가 있으며, 이를 위한 채집 스킬에 ...', 
'contributors': '110.46.34.123,kirby10,max0243,218.54.117.149,ruby3141,121.165.63.239,iviyuki,1.229.200.194,anatra95,kiri47,175.127.134.2,nickchaos71,chkong1998,kiwitree2,namubot,huwieblusnow', 
'namespace': ''
}
```