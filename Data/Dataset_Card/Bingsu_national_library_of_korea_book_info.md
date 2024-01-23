---
language:
- ko
license:
- other
multilinguality:
- monolingual
pretty_name: national_library_of_korea_book_info
size_categories:
- 1M<n<10M
---
# national_library_of_korea_book_info

## Dataset Description
- **Homepage** [문화 빅데이터 플랫폼](https://www.culture.go.kr/bigdata/user/data_market/detail.do?id=63513d7b-9b87-4ec1-a398-0a18ecc45411)
- **Download Size** 759 MB
- **Generated Size** 2.33 GB
- **Total Size** 3.09 GB

국립중앙도서관에서 배포한, 국립중앙도서관에서 보관중인 도서 정보에 관한 데이터.

### License

other ([KOGL](https://www.kogl.or.kr/info/license.do#05-tab) (Korea Open Government License) Type-1)

![KOGL_image](https://www.kogl.or.kr/images/front/sub/img_opencode1_m_en.jpg)

- According to above KOGL, user can use public works freely and without fee regardless of its commercial use, and can change or modify to create secondary works when user complies with the terms provided as follows:

<details>
<summary>KOGL Type 1</summary>

1. Source Indication Liability

- Users who use public works shall indicate source or copyright as follows:
- EX : “000(public institution's name)'s public work is used according to KOGL”
- The link shall be provided when online hyperlink for the source website is available.
- Marking shall not be used to misguide the third party that the user is sponsored by public institution or user has a special relationship with public institutions.

2. Use Prohibited Information

- Personal information that is protected by Personal Information Protection Act, Promotion for Information Network Use and Information Protection Act, etc.
- Credit information protected by the Use and Protection of Credit Information Act, etc.
- Military secrets protected by Military Secret Protection Act, etc.
- Information that is the object of other rights such as trademark right, design right, design right or patent right, etc., or that is owned by third party's copyright.
- Other information that is use prohibited information according to other laws.

3. Public Institution's Liability Exemption

- Public institution does not guarantee the accuracy or continued service of public works.
- Public institution and its employees do not have any liability for any kind of damage or disadvantage that may arise by using public works.

4. Effect of Use Term Violation

- The use permission is automatically terminated when user violates any of the KOGL's Use Terms, and the user shall immediately stop using public works.

</details>

## Data Structure

### Data Instance

```python
>>> from datasets import load_dataset
>>>
>>> ds = load_dataset("Bingsu/national_library_of_korea_book_info", split="train")
>>> ds
Dataset({
    features: ['isbn13', 'vol', 'title', 'author', 'publisher', 'price', 'img_url', 'description'],
    num_rows: 7919278
})
```

```python
>>> ds.features
{'isbn13': Value(dtype='string', id=None),
 'vol': Value(dtype='string', id=None),
 'title': Value(dtype='string', id=None),
 'author': Value(dtype='string', id=None),
 'publisher': Value(dtype='string', id=None),
 'price': Value(dtype='string', id=None),
 'img_url': Value(dtype='string', id=None),
 'description': Value(dtype='string', id=None)}
```

or

```python
>>> import pandas as pd
>>>
>>> url = "https://huggingface.co/datasets/Bingsu/national_library_of_korea_book_info/resolve/main/train.csv.gz"
>>> df = pd.read_csv(url, low_memory=False)
```

```python
>>> df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 7919278 entries, 0 to 7919277
Data columns (total 8 columns):
 #   Column       Dtype
---  ------       -----
 0   isbn13       object
 1   vol          object
 2   title        object
 3   author       object
 4   publisher    object
 5   price        object
 6   img_url      object
 7   description  object
dtypes: object(8)
memory usage: 483.4+ MB
```

### Null data

```python
>>> df.isnull().sum()
isbn13            3277
vol            5933882
title            19662
author          122998
publisher      1007553
price          3096535
img_url        3182882
description    4496194
dtype: int64
```

### Note

```python
>>> df[df["description"].str.contains("[해외주문원서]", regex=False) == True].head()["description"]
10773    [해외주문원서] 고객님의 요청으로 수입 주문하는 도서이므로, 주문취소 및 반품이 불...
95542    [해외주문원서] 고객님의 요청으로 수입 주문하는 도서이므로, 주문취소 및 반품이 불...
95543    [해외주문원서] 고객님의 요청으로 수입 주문하는 도서이므로, 주문취소 및 반품이 불...
96606    [해외주문원서] 고객님의 요청으로 수입 주문하는 도서이므로, 주문취소 및 반품이 불...
96678    [해외주문원서] 고객님의 요청으로 수입 주문하는 도서이므로, 주문취소 및 반품이 불...
Name: description, dtype: object
```
