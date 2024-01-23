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
task_categories:
- text-classification
task_ids:
- multi-class-classification
size_categories:
- 100K<n<1M
---

fungi_diagnostic_chars_comparison_japanese  
大菌輪「識別形質まとめ」データセット  
最終更新日：2022/12/26（R3-10180まで）  
====

### Languages

Japanese  
  
This dataset is available in Japanese only.  
  
# 概要
  
Atsushi Nakajima（中島淳志）が個人で運営しているWebサイト[大菌輪](http://mycoscouter.coolblog.jp/daikinrin/) では、数千件以上の菌類分類学論文を「論文3行まとめ」という形で要約および索引付け（インデキシング）した情報を提供しています。  
その一環として、ある菌と別の菌の「共通する」あるいは「異なる」識別形質 (diagnostic characters) に関する記述を人手で抽出しています。  
本データセットは、抽出された識別形質の一覧に、「色/color」、「形状/shape」などのカテゴリを半自動的に付与して集積したものです。  
「論文3行まとめ」は毎日更新していますが、本データセットの更新はおおむね1ヶ月に一度とする予定です。  
  
## 関連データセット 
「論文3行まとめ」  
[Atsushi/fungi_indexed_mycological_papers_japanese](https://huggingface.co/datasets/Atsushi/fungi_indexed_mycological_papers_japanese)   
「Trait Circusデータセット」（統制形質）
[Atsushi/fungi_trait_circus_database](https://huggingface.co/datasets/Atsushi/fungi_trait_circus_database)   
  
## 各カラムの説明
  
* R3ID … 大菌輪「論文3行まとめ」のIDです。
* No … 各識別文を一意のIDで区別するために、各R3IDにおいてナンバリングしたものです。
* comparison_source … 比較元の分類群（学名）です。
* comparison_target … 比較先の分類群（学名）です。 
* sentence … 識別文です。全て日本語です。
* label …半自動的に付与されたカテゴリです（人手で修正していますが、ダブルチェックは行っていないので誤分類もあると思います）。以下の25のカテゴリが存在します。
  * サイズ/size
  * 分子系統解析/molecular_phylogenetic_analysis
  * 形状/shape
  * 色/color
  * 地理的分布/geographical_distribution
  * 生息環境/habitat
  * 表面性状/surface_characteristics
  * 構造/structure
  * 有無/presence
  * 形態全般/general_morphology
  * 位置/position
  * 二次代謝産物/secondary_metabolite
  * 呈色反応/chemical_reaction
  * 数量/amount
  * 発達/development
  * 生理学的形質/physiological_characters
  * 分類/classification
  * 資化・発酵能/assimilation_and_fermentation
  * 質感/texture
  * 味・臭い/taste_and_smell
  * 病害・病原性関連/disease_and_pathogenecity
  * 全般/general_characters
  * 耐性・感受性/resistance_and_susceptibility
  * 栄養摂取様式/nutrition_style
  * 未分類/unclassified
* common_or_different … 共通する形質は「1」、異なる形質は「0」です。
* data_source … 各情報の 出典（文献）のURLです。