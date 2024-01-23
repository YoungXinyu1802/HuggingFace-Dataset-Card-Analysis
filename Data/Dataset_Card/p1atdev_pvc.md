---
license: cc0-1.0
---

# PVC figure products dataset
This dataset contains product information for figure images scraped from multiple Web sites.

## myethos.json

PVC figure images and information from [www.myethos.cn](http://www.myethos.cn).

```ts
interface Myethos {
  id: number
  image_urls: string[]
  descriptions: Record<string, string>
}
```

Preview

```json
[
  ...
  {
      "id": 107,
      "image_urls": [
          "http://www.myethos.cn/upload/image/20160414/570f46082398c.jpg",
          ...
      ],
      "descriptions": {
          "Product Name": "FairyTale-Another-Snow White",
          "Scale": "1/8 (Approximately 245mm in height with stand included)",
          "Specifications": "Pre-painted ABS&PVC figure",
          "List Price": "8800 JPY",
          "Release Date": "2015/01"
      }
  },
  ...
]
```

## tokyofigure.json

PVC figure products information from [tokyofigure.jp](https://tokyofigure.jp).

```ts
interface Tokyofigure {
  id: number
  name: string
  price: string
  points: string
  descriptions: Record<string, string>
  comment: string
  image_urls: string[]
}
```

e.g.

```json
[
  ...
  {
      "id": 323,
      "name": "Genshin Impact \"It's not emergency food!\" Paimon Gourmet Series Trading Figures 6 pieces BOX",
      "price": "9,240",
      "points": "84",
      "descriptions": {
          "Product Categories": "Bishoujo (Beautiful Girls)",
          "JAN code": "6974096536047",
          "Release Date": "May. 2023 TBD",
          "Series": "Video Game",
          "Distributor:": "miHoYo",
          "Material:": "PVC & ABS Painted Finished Figures"
      },
      "comment": "All 6 types are available by purchasing 1BOX.\n\u3010lineup\u3011Paimon, Ripe Tomato Meat SaucePaimon Meat TsumitsumiPaimon Fisherman ToastPaimon/Kusaku Farmer's CuisinePaimon/Sen JumpPaimon Gogo no Pancake",
      "meta": {
          "Manufacturer": "miHoYo",
          "Original": "Genshin"
      },
      "image_urls": [
          "https://tokyofigure.jp/upload/save_image/12231522_63a54929240b3.jpg",
          ...
      ]
  },
  ...
]
```

## kotobukiya.json

PVC figure products information from [en.kotobukiya.co.jp](https://en.kotobukiya.co.jp).

```ts
interface Kotobukiya {
  id: string
  title: string
  copyrights: string[]
  tags: string[]
  specification: Record<string, string>
  images: string[]
  descriptions: string[]
}
```

e.g.

```json
[
  {
      "id": "0000004744",
      "title": "Ange Katrina",
      "copyrights": [
          "Pre-Painted PVC Figure",
          "NIJISANJI"
      ],
      "tags": [
          "Figure"
      ],
      "specification": {
          "Month of Release": "Sep, 2023",
          "Scale": "1/7",
          "Product Size": "264mm tall",
          "Specification": "Pre-Painted PVC Figure",
          "Material": "PVC (Phthalate-free)\u30fbABS",
          "Sculptor": "Rico"
      },
      "images": [
          "https://en.kotobukiya.co.jp/wp-content/uploads/2023/01/4327d953cc3a863ab3ec7f476e291abf3f8ae4a4.jpg",
          ...
      ],
      "descriptions": [
          "The virtual Youtuber and NIJISANJI member Ange Katrina is being made into a 1/7 scale figure!",
          "She comes to life in a pose based on her promotional visual, with her signature cheerful smile being the highlight of this figure!",
          "Extra care was paid to bringing out even the minute details, such as the volume in her thick coat and detailing on her boots.",
          "Clear parts were used on her crimson hair to achieve a light and delicate finish with a sense of transparency. Her gold hairpin has also been perfectly sculpted.",
          "Enjoy her even more with the option of displaying her with the included winking face part!",
          "Recreate Sanbaka by displaying her alongside Lize Helesta and the upcoming Inui Toko! Add her to your collection today!"
      ]
  },
  ...
]
```

## goodsmile

```ts
interface GoodSmile {
  id: string
  title: string
  details: Record<string, string>
  image_urls: string[]
}
```

### Figma

Figma products information from [www.goodsmile.info](https://www.goodsmile.info/en/).

e.g.

```json
[
    {
        "id": "13881",
        "title": "figma Sophia F. Shirring: Bikini Armor ver.",
        "details": {
            "Product Name": "figma Sophia F. Shirring: Bikini Armor ver.",
            "Series": "BUNNY SUIT PLANNING",
            "Manufacturer": "Max Factory",
            "Category": "figma",
            "Price": "\u00a512,800",
            "Release Date": "2024/01",
            "Specifications": "Painted plastic non-scale articulated figure with stand included. Approximately 170mm in height (150mm in height to top of head).",
            "Sculptor": "Max Factory (Jun Yamaoka)/PINPOINT",
            "Cooperation": "Masaki Apsy",
            "Released by": "Max Factory",
            "Distributed by": "Good Smile Company"
        },
        "image_urls": [
            "https://images.goodsmile.info/cgm/images/product/20230126/13881/110758/large/3c43cba93a10884cc52c63850b1e89dc.jpg",
            ...
        ]
    },
  ...
```

### Nendoroid

Nendoroid products information from [www.goodsmile.info](https://www.goodsmile.info/en/).

e.g.

```json
[
    {
        "id": "13943",
        "title": "Nendoroid Doll Marin Kitagawa",
        "details": {
            "Product Name": "Nendoroid Doll Marin Kitagawa",
            "Series": "My Dress-Up Darling",
            "Manufacturer": "Good Smile Company",
            "Category": "Nendoroid Doll",
            "Price": "\u00a58,500",
            "Release Date": "2023/11",
            "Specifications": "Painted non-scale articulated doll made with cloth, magnets and plastic with stand included. Approximately 140mm in height.",
            "Sculptor": "Shichibee (Matsuda Model), Nendoron",
            "Cooperation": "Sawada Koubou, Nendoron",
            "Outfit/Pattern Design": "Mieko Akimoto"
        },
        "image_urls": [
            "https://images.goodsmile.info/cgm/images/product/20230208/13943/111351/large/05550ad6dbbb6e4f9a6622e30610fe96.jpg",
            ...
        ]
    },
    ...
```

## spiritale.json

Spiritale products information from [spiritale.jp](https://spiritale.jp).

e.g.

```json
[
    {
        "id": "50101200",
        "title": "\u521d\u97f3\u30df\u30af 39's Special Day 1/7\u30b9\u30b1\u30fc\u30eb\u30d5\u30a3\u30ae\u30e5\u30a2\u3010\u5b8c\u5168\u53d7\u6ce8\u751f\u7523\u30fb\u30bf\u30a4\u30c8\u30fc\u30d7\u30ed\u30c0\u30af\u30c4\u30aa\u30f3\u30e9\u30a4\u30f3\u30b9\u30c8\u30a2\u9650\u5b9a\u3011",
        "images": [
            "https://spiritale.jpimg/items/2302_39miku/02_31008.jpg",
            ...
        ],
        "price": "\uffe535,200"
    },
    ...
```
