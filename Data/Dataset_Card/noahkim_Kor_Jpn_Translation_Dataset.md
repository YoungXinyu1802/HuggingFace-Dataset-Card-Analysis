---
annotations_creators:
  - expert-generated
language_creators:
  - other
language:
  - kor
  - jpn
license:
  - mit
size_categories:
  - 1K<n<10K
source_datasets:
  - original
task_categories:
  - translation
task_ids:
  - language-modeling
paperswithcode_id: null
pretty_name: Kor-Jpn-Translation
---
# Dataset Card for "Kor_Jpn_Translation_Dataset"

### Dataset Summary

AI-Hub에서 제공하는 한국어-일본어 번역 말뭉치 데이터(https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=127)를 사용하기 쉽게 정제했습니다.

- 제공처 : AI-Hub(https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=127)
- 제목 : 한국어-일본어 문화 분야 이중 말뭉치
- 구축분야 : 문화재/향토/K-Food, K-POP(한류)/대중문화_공연 콘텐츠, IT/컴퓨터/모바일, 금융/증시, 사회/노동/복지, 교육, 특허/기술, 자동차
- 구축량 : 150만 문장쌍
- 응용분야 : 언어모델, 자동번역
- 언어 : 원시어-한국어, 목적어-일본어

### Supported Tasks and Leaderboards

- Translation

### Languages

- Kor
- Jpan

## Dataset Structure

  features:
  - name: KOR
    dtype: string
  - name: JPN
    dtype: string
  splits:
  - name: train
    num_bytes: 294787449
    num_examples: 840000
  - name: val
    num_bytes: 88406929
    num_examples: 252000
  - name: test
    num_bytes: 37964427
    num_examples: 108000
  download_size: 289307354
  dataset_size: 421158805

### Data Splits

  splits:
  - name: train
    num_bytes: 294787449
    num_examples: 840000
  - name: val
    num_bytes: 88406929
    num_examples: 252000
  - name: test
    num_bytes: 37964427
    num_examples: 108000


### Contributions
[More Information needed](https://github.com/huggingface/datasets/blob/main/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)