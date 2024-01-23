# AI Stage MRC task

## Version Info

### v4.1.1
- v3.2.3데이터 (train_dataset_aug)에 punctuation추가한 데이터셋, both train and validation
- train_aug_punctuation에 있음
- v4.1.0의 오류 해결

### v4.1.0
- v3.2.2데이터(train_dataset_aug)에 punctuation추가한 데이터셋, both train and validation
- train_data_aug에 있음
- answers 잘못 labeling된 데이터

### v4.0.1
- punctuation추가한 데이터셋, both train and validation
- answers type 정상

### v4.0.0
- punctuation추가한 데이터셋, only train 
- answers type 오류

### v3.2.3
- `v3.2.2`에서 잘못된 [ANSWER] 위치 수정

### v3.2.2
- `v3.2.1`에서 special token([TITLE]) 제거

### v3.2.1
- `v3.2.0`에서 special token([ANSWER]) 추가

### v3.2.0
- `v1.3.1`에서 special tokens([TITLE], #) 추가

### v3.1.0
- `v3.0.0`에서 Question 뒤에 NER 모델로 찾은 Entity 단어 추가

### v3.0.0
- `v1.0.0`에서 태욱님 answer, sentence split 토큰 추가

### v2.1.1
- `v2.1.0`에서 `v3.2.3`의 augmentation 데이터와 concat
- bt_context_extractive_final폴더에 train, validation사용

### v2.1.0
- extractive모델을 위한 pororo context augmentation
- context내에 answer가 유일한 데이터만 증강, answer위치 조정 완료
- context_bt_for_extracive폴더에 train, validation 추가

### v2.0.1
- `v2.0.0`에서 context내 answer가 손상된 데이터 제거

### v2.0.0
- 채은님 context backtranslation 추가한 데이터셋

### v1.6.4
- `v1.6.3`에서 `train_dataset_curri` 폴더 내 구성 변경
  - `train_level_1` & `train_level_2`-> `train_level_1`
  - `train_level_3` -> `train_level_2`
  - `train_level_#`을 모두 합친 `train_total`

### v1.6.3
- `v1.6.2`에서 `train_dataset_curri` 폴더 추가, 샘플별 스코어링하여 `level0` ~ `level3`으로 구성
- 사용 데이터셋 : `train`, `train_perm01`, `train_perm02`, `train_perm04`, `train_mask_2`, `train_hard_mask`, `pororo_aug_ver2_len_context_easy`,  `pororo_aug_ver2_len_context_normal`, `pororo_aug_ver2_len_context_hard`

### v1.6.2
- `v1.6.1`에서 `train_dataset` 폴더에 `train_mask_2`, `train_hard_mask` 데이터 추가

### v1.6.1
- `v1.6.0`에서 `train_dataset` 폴더에
  - `train_pororo_aug_ver2`의 context length 기준으로 curriculum-learning 데이터셋 추가
    - easy : `len < 673`
    - normal : `673 <= len < 935`
    - hard : `935 <= len`
  - `v1.4.1`의 업데이트 데이터셋 반영

### v1.6.0
- `v1.3.2`에서 `train_dataset` 폴더에 permutation ratio 0.1, 0.2, 0.4의 sentence permutation 데이터 추가

### v1.5.0
- `v1.4.1`에서 헷갈리는 단어, 날짜 정보 Masking datsets 추가

### v1.4.4
- `v1.4.1`에서 증강 데이터(train, valid pororo ver1 포함) concat, shuffled concat 추가

### v1.4.3
- `v1.4.1`에서 증강 데이터(train, valid pororo ver1 제외) concat, shuffled concat 추가

### v1.4.2
- `v1.4.1`에서 Question 뒤에 NER 모델로 찾은 Entity 단어 추가

### v1.4.1
- 대웅님께서 공유해주신 질문유형을 반영하여 기존의 질문을 7개에서 45개로 늘려 pororo aug 적용하여 pororo aug ver2 추가

### v1.3.2
- 'v1.3.1'에 'train_dataset_aeda'에 preprocessing 이 누락 되어 처리

### v1.3.1
- `v.1.3.0`에 `train_dataset_aug` 폴더 추가(question에 대한 조사 제거, Back Translation, AEDA, pororo aug ver1을 concatenate함)

### v1.3.0
- `v1.2.0`에서 `wiki_documents.json`을 pororo aug를 활용해 50,531건의 증강 데이터 추가

### v1.2.0
- `v1.1.0`에서 question에 대한 조사 제거, Back Translation, AEDA Augmentation 추가(pororo aug엔 적용하지 않음)

### v1.1.0
- `v1.0.0`에서 Question 뒤에 NER 모델로 찾은 Entity 단어 추가

### v1.0.0
- `v0.1.1`에서 context에 전처리

### v0.2.2
- `train_dataset`의 `train`, `validation` 셋에서 문제 및 정답오류 수정

### v0.2.1
- `train_pororo_aug`, `validation_pororo_aug`에도 동일한 summary 추가
- `context_bullet`에서 발견된 오류 수정(`context`와 관련 없는 문장이 생성되는 오류)

### v0.2.0
- 대웅님 pororo context summary 추가한 데이터셋

### v0.1.1
- 영재님 pororo augmenation 추가한 데이터셋
- `train_dataset`의 `train`, `validation` 셋에서 문제 및 정답오류 수정

### v0.1.0
- 영재님 pororo augmenation 추가한 데이터셋

### v0.0.0
- 대회에서 제공해주신 기본 데이터셋

## LICENSE
- CC-BY-2.0
- 모든 저작권은 AI Stage에게 있습니다!
- https://stages.ai/
