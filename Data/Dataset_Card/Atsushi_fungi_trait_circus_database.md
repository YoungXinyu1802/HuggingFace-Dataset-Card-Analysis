---
annotations_creators:
- other
language:
- en
- ja
multilinguality:
- multilingual
license:
- cc-by-4.0
source_datasets:
- original
size_categories:
- 100K<n<1M
---
fungi_trait_circus_database  
大菌輪「Trait Circus」データセット（統制形質）  
最終更新日：2022/12/26  
====
### Languages
Japanese and English 
  
Please do not use this dataset for academic purposes for the time being. (casual use only)  
当面の間仮公開とします。学術目的での使用はご遠慮ください。  
  
# 概要
  
Atsushi Nakajima（中島淳志）が個人で運営しているWebサイト[大菌輪](http://mycoscouter.coolblog.jp/daikinrin/) では、菌類の記載文を自然言語処理の手法を利用して半自動的に処理し、菌類の形態、生態などに関する様々な「形質 (traits)」データを抽出して、集計や解析の便宜を図るために、あらかじめ設定された「統制語 (controlled term)」の形でまとめています。  
抽出手法については「ニッチェ・ライフ」誌の[こちらの記事](https://media.niche-life.com/series/008/Niche008_06.pdf)（査読なし）で報告しています。  
自動抽出という性質上、ある程度の誤りが含まれる可能性があることをご承知おきください。  
  
統制語は「要素 (element）」「属性（attribute）」「値（value）」の3つ組からなります。  
例えば「傘_色_黒」はそれぞれ「傘」「色」「黒」の要素/属性/値を持っています。一部の統制語では要素と属性が同一となっています（「生息環境」など）  
参考までに、データ数上位3件は「要素」で「子実体」「傘」「胞子」、「属性」で「色」「形状」「表面性状」、「値」で「褐」「平滑」「黄」です。      
  
また、菌類分類学の学習および同定支援の目的で、そのデータを基にしたインタラクティブな可視化Webアプリ「[Trait Circus](https://tinyurl.com/nrhcfksu)」を提供しています。
本データセットは、そのWebアプリの生データに相当し、容量の都合等でWebアプリに反映されていない情報も含まれています。 

## 関連データセット 
「論文3行まとめ」  
[Atsushi/fungi_indexed_mycological_papers_japanese](https://huggingface.co/datasets/Atsushi/fungi_indexed_mycological_papers_japanese)   
「識別形質まとめ」  
[Atsushi/fungi_diagnostic_chars_comparison_japanese](https://huggingface.co/datasets/Atsushi/fungi_diagnostic_chars_comparison_japanese)     
  
## 各カラムの説明
  
* source … 各情報の出典のURLです。多くは学術文献またはMycoBankの記載文データベースを参照しています。
* hit_term … 抽出された形質の出典中における表現です。
* current_name … その形質を有する菌の現行学名です。MycoBankを参照していますが、最新の情報ではない可能性があります。
* element_j … 「要素」の日本語表記です。
* attribute_j … 「属性」の日本語表記です。
* value_j … 「値」の日本語表記です。
* element … 「要素」の英語表記です。
* attribute … 「属性」の英語表記です。
* value … 「値」の英語表記です。