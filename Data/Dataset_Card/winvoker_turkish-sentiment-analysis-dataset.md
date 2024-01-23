---
annotations_creators:
- crowdsourced
- expert-generated
language_creators:
- crowdsourced
language:
- tr
license:
- cc-by-sa-4.0
multilinguality:
- monolingual
pretty_name: Turkish Sentiment Dataset
size_categories:
- unknown
source_datasets: []
task_categories:
- text-classification
task_ids:
- sentiment-classification
---

# Dataset
This dataset contains positive , negative and notr sentences from several data sources given in the references. In the most sentiment models , there are only two labels; positive and negative. However , user input can be totally notr sentence. For such cases there were no data I could find. Therefore I created this dataset with 3 class. Positive and negative sentences are listed below. Notr examples are extraced from turkish wiki dump. In addition, added some random text inputs like "Lorem ipsum dolor sit amet.".

There are 492.782 labeled sentences. %10 of them used for testing.

# Türkçe Duygu Analizi Veriseti
Bu veriseti , farklı kaynaklardan derlenmiş pozitif , negatif ve nötr sınıflardan örnekler içerir. Bir çok verisetinde sadece pozitif ve negatif bulunur. Fakat kullanıcı input'u nötr olabilir. Bu tarz durumlar için türkçe bir dataset bulmakta zorlandım. Dolayısıyla , 3 sınıftan oluşan bu dataseti oluşturdum. Pozitif ve negatif örnekleri aldığın kaynaklar referans kısmında listelenmiştir. Nötr cümleler ise wikipedia datasından alınmıştır. Ek olarak bazı rastgele inputlar nötr olarak eklenmiştir. Örneğin: "Lorem ipsum dolor sit amet.".

There are 492.782 labeled sentences. %10 of them used for testing.

# References 
- https://www.kaggle.com/burhanbilenn/duygu-analizi-icin-urun-yorumlari
- https://github.com/fthbrmnby/turkish-text-data
- https://www.kaggle.com/mustfkeskin/turkish-wikipedia-dump
- https://github.com/ezgisubasi/turkish-tweets-sentiment-analysis
- http://humirapps.cs.hacettepe.edu.tr/