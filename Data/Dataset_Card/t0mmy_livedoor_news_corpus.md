---
license: cc
task_categories:
- text-classification
language:
- ja
pretty_name: livedoor News Corpus
size_categories:
- 1K<n<10K
---
# Dataset Card for "livedoor_news_corpus"

## Dataset Description

- **Homepage:** [ダウンロード - 株式会社ロンウイット](http://www.rondhuit.com/download.html#ldcc)
- **Repository:** 
- **Paper:** 
- **Leaderboard:** 
- **Point of Contact:** [RONDHUIT](mailto:sales@rondhuit.com)

### Dataset Summary

The livedoor News Corpus is a collection of 7k human-written Japanese news stories.

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

The language in the dataset is Japanese. The BCP-47 code for Japanese is ja.

## Dataset Structure

### Data Instances

For each instance, there is a string for the URL, a datetime for the date, a string for the title, a string for the text, and an integer for the label.

```
{'url': 'http://news.livedoor.com/article/detail/6601535/',
 'date': '2012-05-28T12:55:00+0900',
 'title': 'NTTドコモ、2012夏モデル新商品内覧会を東京・名古屋・大阪で開催！DCMXおよびプレミアステージ会員向け',
 'text': '2012夏モデル新商品内覧会が開催！ \n\nNTTドコモは28日、この夏以降に発売予定の新商品を発売前に体験できる「2012 夏モデル新商品内覧会」を東京や名古屋、大阪にてDCMX会員およびプレミアステージ会員（ドコモプレミアクラブ）を対象に実施することをお知らせしています。\n\n事前お申込みは不要で、当日、入場の際にDCMXカードもしくはドコミプレミアクラブ・サイト画面を提示することで、入場できます。\n\nまた、1人の対象者がいれば、知り合いや友だちを連れていっても大丈夫とのことです。なお、DCMX mini会員は対象外となるということです。\n\n開催日時および開催会場は、以下の通りです。ただし、時間帯によっては混雑のために入場制限をする場合があるとのことですので、ご注意ください。\n\n【開催日】\n・東京会場\n2012年6月8日（金）〜10日（日）\n・名古屋会場\n2012年6月15日（金）〜17日（日）\n・大阪会場\n2012年6月16日（土）〜17日（日）\n\n※時間帯によっては混雑のため、入場制限させていただく場合があります。あらかじめご了承願います。\n※お連れ様は何名でもご来場いただけます。\n※会場までの交通費等はお客様ご負担となります。\n※ご来場の際は、公共交通機関をご利用ください。\n\n【東京会場】\n■会場\n東京ドームシティ プリズムホール 1F\n大好評の各機種のメーカー担当者によるプレゼンテーション、スマートフォン講座の他、20周年の感謝の気持ちを込めて、約60機種の歴代ケータイの展示や、歴代ドコモダケ展示など、特別企画も盛りだくさん！ご家族、お友達をお誘いの上、是非ご来場ください。\n\nステージスケジュールは6月1日（金）公開予定！\n■日時\n2012年6月8日（金）午後5：00〜午後9：00\n※最終入場時間：午後8：30\n2011年6月9日（土）・10日（日）午前10：30〜午後6：00\n※最終入場時間：午後5：30\n\n※途中入場可\n※開場時間にご注意ください。\n※当日の様子を取材しホームページ等に掲載する場合があります。なお、当日取材させていただいた画像、コメントなどの肖像権は弊社に帰属するものとさせていただきます。\n■混雑状況\n当日の混雑状況についてご確認いただけます。\n詳しくはこちら\n■住所\n東京都文京区後楽1-3-61\n東京ドームシティ プリズムホール 1F\n■交通アクセス\n・JR中央線・総武線・都営三田線「水道橋駅」徒歩約1分\n・東京メトロ丸ノ内線・南北線「後楽園駅」徒歩約3分\n・都営大江戸線「春日駅」徒歩約5分\n\n\n【名古屋会場】\n■会場\n栄ガスビル5F ガスホール\nスマートフォンのステージイベントを実施予定！モバイルアスキー・アスキードットPC編集部presentsで定番のアプリからおすすめの人気アプリなどを紹介します。\n\nステージスケジュールは6月1日（金）公開予定！\n\nDCMXのカードをご提示いただいた方に抽選で粗品をプレゼントいたします。DCMX会員の皆様は、是非DCMXのカードをご持参ください。\n※6月15日（金）は内覧会は開催されますが、ステージはございません。\n■日時\n2012年6月15日（金）午後6：00〜午後9：00\n※最終入場時間：午後8：30\n2012年6月16日（土）・17日（日）午前11：00〜午後6：00\n※最終入場時間：午後5：30\n\n※途中入場可\n※開催時間にご注意ください。\n■住所\n愛知県名古屋市中区栄3-15-33\n栄ガスホール 5F 栄ガスホール\n■交通アクセス\n・地下鉄東山線・名城線「栄駅」サカエチカ6番出口より徒歩約5分\n・地下鉄名城線「矢場町駅」6番出口より徒歩約2分\n\n\n【大阪会場】\n■会場\nハービスOSAKA B2F ハービスHALL\nスペシャルステージを実施予定！ 各機種のメーカー担当者によるプレゼンテーションの他、メーカー担当者が一堂に会する「スマートフォンサミット」、その他お楽しみ企画もあるよ！\nステージスケジュールは6月1日（金）公開予定！\n\n■日時\n2012年6月16日（土）・17日（日）午前11：00〜午後6：00\n※最終入場時間：午後5：30\n※途中入場可\n※当日の様子を取材しホームページ等に掲載する場合があります。なお、当日取材させていただいた画像、コメントなどの肖像権は弊社に帰属するものとさせていただきます。\n■住所\n大阪府大阪市北区梅田2-5-25\nハービスOSAKA B2F ハービスHALL\n■交通アクセス\n・阪神電車「梅田駅」西改札より徒歩約6分\n・JR線「大阪駅」桜橋口より徒歩約7分\n・地下鉄御堂筋線「梅田駅」南改札より徒歩約10分\n・阪急電車「梅田駅」より徒歩約15分\n\n記事執筆：memn0ck\n\n■関連リンク\n・エスマックス（S-MAX）\n・エスマックス（S-MAX） smaxjp on Twitter\n・DCMX｜ドコモのケータイクレジット\n',
 'label': 6}
```

### Data Fields

- `url`: a string that URL
- `date`: a datetime that date
- `title`: a string that title
- `text`: a string that text
- `label`: an integer whose value may be either 0, indicating that category is Topic News, 1, indicating that category is Sports Watch, 2, indicating that category is IT Life Hack, 3, indicating that category is Appliance Channel, 4, indicating that category is MOVIE ENTER, 5, indicating that category is Single Woman Report, 6, indicating that category is Smax, 7, indicating that category is livedoor HOMME, 8, indicating that category is Peachy.

### Data Splits

The livedoor News Corpus has 1 split: *train*.

| Dataset Split | Number of Instances in Split |
| ------------- | ---------------------------- |
| Train         | 7,367                        |

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

The livedoor News Corpus was developed by [RONDHUIT](https://www.rondhuit.com/en.html).

### Licensing Information

The livedoor News Corpus is licensed under a [Creative Commons Attribution-NoDerivs 2.1 Japan License](https://creativecommons.org/licenses/by-nd/2.1/jp/)

### Citation Information

```
@misc{livedoornewscorpus,
  title={livedoor News Corpus},
  author={RONDHUIT},
  year={2012},
  howpublished={\url{http://www.rondhuit.com/download.html#ldcc}}
}
```

### Contributions

Thanks to [@rondhuit](https://github.com/RONDHUIT) for adding this dataset.