**Pexel Videos**

*358,551 video urls, average length 19.5s, and associated metadata from pexels.com.*

Data was extracted from their video sitemaps (pexels.com/robots.txt) on 01/08/2022.

Data is stored in PexelVideos.parquet.gzip as a gzipped parquet

To get this data ensure you have git installed and do !git lfs clone https://huggingface.co/datasets/Corran/pexelvideos/

In python the reccomended reading is by opening the file with pandas. 

!pip install pandas <br>
import pandas <br>
data=pd.read_parquet('PexelVideos.parquet.gzip') <br>

Get a specific url and its metadata using data.iloc[0], read this like a python dict

e.g to get the url for index i run
url= df.iloc[i]["content_loc"] 

https://pandas.pydata.org/pandas-docs/version/1.1/getting_started/index.html#getting-started

**Explore this dataset using Open-Clip**
https://colab.research.google.com/drive/1m3_KfPKOC_oivqoruaseiNUlP-_MqqyX#scrollTo=bNngcd8UAOma

**License**

According to Pexels licensing, these videos are free to use for personal or commercial purposes, attribution is polite but not required however,

-Identifiable people may not appear in a bad light or in a way that is offensive. <br>
-Don't sell unaltered copies of a photo or video, e.g. as a poster, print or on a physical product without modifying it first. <br>
-Don't imply endorsement of your product by people or brands on the imagery. <br>
-Don't redistribute or sell the photos and videos on other stock photo or wallpaper platforms. <br>

license https://www.pexels.com/license/
