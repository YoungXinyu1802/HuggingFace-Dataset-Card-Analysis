# CORD: A Consolidated Receipt Dataset for Post-OCR Parsing

CORD dataset is cloned from [clovaai](https://github.com/clovaai/cord) GitHub repo

- Box coordinates are normalized against image width/height
- Labels with very few occurrences are replaced with O:

```
replacing_labels = ['menu.etc', 'menu.itemsubtotal', 
                    'menu.sub_etc', 'menu.sub_unitprice', 
                    'menu.vatyn', 'void_menu.nm', 
                    'void_menu.price', 'sub_total.othersvc_price']
```

Check for more info [Sparrow](https://github.com/katanaml/sparrow)

## Citation

### CORD: A Consolidated Receipt Dataset for Post-OCR Parsing
```
@article{park2019cord,
  title={CORD: A Consolidated Receipt Dataset for Post-OCR Parsing},
  author={Park, Seunghyun and Shin, Seung and Lee, Bado and Lee, Junyeop and Surh, Jaeheung and Seo, Minjoon and Lee, Hwalsuk}
  booktitle={Document Intelligence Workshop at Neural Information Processing Systems}
  year={2019}
}
```
### Post-OCR parsing: building simple and robust parser via BIO tagging

```
@article{hwang2019post,
  title={Post-OCR parsing: building simple and robust parser via BIO tagging},
  author={Hwang, Wonseok and Kim, Seonghyeon and Yim, Jinyeong and Seo, Minjoon and Park, Seunghyun and Park, Sungrae and Lee, Junyeop and Lee, Bado and Lee, Hwalsuk}
  booktitle={Document Intelligence Workshop at Neural Information Processing Systems}
  year={2019}
}
```