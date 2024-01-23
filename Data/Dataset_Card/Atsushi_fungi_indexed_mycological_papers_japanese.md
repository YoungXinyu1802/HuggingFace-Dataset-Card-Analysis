---
annotations_creators:
- other
language:
- ja
license:
- cc-by-4.0
multilinguality:
- monolingual
source_datasets:
- original
size_categories:
- 1K<n<10K
---
fungi_indexed_mycological_papers_japanese
大菌輪「論文3行まとめ」データセット  
最終更新日：2022/12/26（R3-10180まで）  
====
### Languages
Japanese  
  
This dataset is available in Japanese only.  
  
# 概要
  
Atsushi Nakajima（中島淳志）が個人で運営しているWebサイト[大菌輪](http://mycoscouter.coolblog.jp/daikinrin/) では、数千件以上の菌類分類学論文を「論文3行まとめ」という形で要約および索引付け（インデキシング）した情報を提供しています。  
本データセットは、「論文3行まとめ」のコンテンツに含まれる各論文の3行抄録、タグ（索引）、掲載種一覧、比較種一覧をまとめたものです。
「論文3行まとめ」は毎日更新していますが、本データセットの更新はおおむね1ヶ月に一度とする予定です。  
また、本データセットを可視化したWebアプリを[Observableで公開](https://tinyurl.com/2tvryz8u)しています。
  
## 関連データセット 
「識別形質まとめ」  
[Atsushi/fungi_diagnostic_chars_comparison_japanese](https://huggingface.co/datasets/Atsushi/fungi_diagnostic_chars_comparison_japanese)   
「Trait Circusデータセット」（統制形質）
[Atsushi/fungi_trait_circus_database](https://huggingface.co/datasets/Atsushi/fungi_trait_circus_database)  
  
## 各カラムの説明
  
* R3ID … 大菌輪「論文3行まとめ」のIDです。
* ja_title_provisional_translate（仮訳和文題名） … 作成者が翻訳したタイトルです。一部、日本語の原題があるものはそれをそのまま使用しています。
* original_title（原文題名）
* published_year（出版年）
* journal_title（雑誌名）
* source（文献リンク） … 各情報の 出典（文献）のURLです。
* daikinrin_url … 大菌輪「論文3行まとめ」のURLです。
* tags … 作成者が論文を全文読んだ上で独自に付与した索引です。カンマ+半角空白区切りです。形態形質、宿主/基質、実験器具/実験手法/試薬、地理的分布、生理/生化学などを幅広く索引しています。
* R3summary_1 … 3行抄録の「1行目」です。
* R3summary_2 … 3行抄録の「2行目」です。
* R3summary_3 … 3行抄録の「3行目」です。
* species_reported（報告種一覧） … 当該論文内で掲載された種の一覧です。「半角空白+半角スラッシュ+半角空白」区切りです。記号の意味は以下の通りです。
  * ★＝新種（新亜種・新品種・新変種）
  * ■＝ 新産種
  * ▲＝新組み合わせ
  * ◆＝新学名
  * ●＝新階級
  * （無印）＝その他
* species_compared（比較種一覧） … いずれかの報告種と論文中で何らかの比較がなされた種の一覧です。「半角空白+半角スラッシュ+半角空白」区切りです。詳細は「識別形質まとめ」データセット（[Atsushi/fungi_diagnostic_chars_comparison_japanese](https://huggingface.co/datasets/Atsushi/fungi_diagnostic_chars_comparison_japanese)）を参照してください。
* taxon_reported（分類群一覧） … 報告種に対応する上位分類群をまとめたものです。カンマ+半角空白区切りです。MycoBankの情報を基に付与していますが、最新でない可能性があります。