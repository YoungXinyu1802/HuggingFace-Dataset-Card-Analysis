---
license: afl-3.0
---
# Telegram News (Farsi - Persian)
## Updated 24 OCT 2022

    bbc.pickle Total News: 139,275 Timespan: 2015-10-13 - 2022-10-24
    
    fars.pickle Total News: 241,346 Timespan: 2015-09-26 - 2022-10-24
    
    farsivoa.pickle Total News: 134,023 Timespan: 2015-10-07 - 2022-10-24
    
    iranint.pickle Total News: 137,459 Timespan: 2017-05-16 - 2022-10-24
    
    irna.pickle Total News: 178,395 Timespan: 2016-07-05 - 2022-10-24
    
    khabar.pickle Total News: 384,922 Timespan: 2016-09-22 - 2022-10-24
    
    Tabnak.pickle Total News: 102,122 Timespan: 2017-05-22 - 2022-10-24

### Helper functions
```py
def getTxt(msg):
    txt=''
    if msg.text:
        txt+=msg.text+' '
    if msg.caption:
        txt+=msg.caption+' '
    if not msg.web_page==None:
        try:
            txt+=msg.web_page.title+' '
            txt+=msg.web_page.description
        except:pass
    txt=txt.lower().replace(u'\u200c', '').replace('\n','').replace('📸','').replace('\xa0','')
    txt=re.sub(r'http\S+', '', txt)
    txt=re.sub(r'[a-z]', '', txt)
    txt=re.sub(r'[^\w\s\d]', '', txt)
    return txt.strip()
```

```py
def getDocs(m):
    txt=getTxt(m)
    if len(txt)>10:
        return {'text':txt,'date':m.date}
    else:
        return ['']
```

```py
def getDate(news):
 return news. Date
```

### Read the Files
```py
with open('bbc.pickle', 'rb') as handle:
    news=pickle.load(handle)
newsText=list(map(getTxt,news))
newsDate=list(map(getDate,news))

```

