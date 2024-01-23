---
license: unknown
---

# Ngữ liệu tiếng Việt đã tiền xử lý để huấn luyện mô hình ngôn ngữ lớn

1. __OSCAR-2201-vi__: 99G jsonl > 50G plain text > 35G lọc
  - File `00112131415061718191.*` to `09192939495969708990.*`

2. __Thịnh Laws__: 5G text > 4G lọc
  - Sử dụng metatags: `<id>`id văn bản`</i>`, `<title>`tiêu đề văn bản`</title>`
  - File `thinh-laws.*`

3. __Roots Wikipedia Vi__:0.5G text > 0.3G lọc
  - File `roots-wikipedia-vi.*`

4. __TruongNews__: 74G text > 60G lọc
  - File `truongnews*`


## .txt to .utf8

```
\nHotline: 0942.66.46.46\nChỉ phát hành, sao chép thông tin từ Tạp chí điện tử Petrotimes khi có sự đồng ý bằng văn bản của Ban biên tập
```
=>
```
\n Hotline: 0942.66.46.46 \n ^chỉ phát hành , sao chép thông tin từ ^tạp chí điện tử Petrotimes khi có sự đồng ý bằng văn bản của ^ban biên tập
```

## Nguồn

1. https://huggingface.co/datasets/oscar-corpus/OSCAR-2201/tree/main/compressed/vi_meta
2. https://huggingface.co/datasets/th1nhng0/vietnamese_legal_corpus
3. https://huggingface.co/datasets/bigscience-data/roots_vi_wikipedia
4. https://huggingface.co/datasets/truongpdd/vietnews-dataset