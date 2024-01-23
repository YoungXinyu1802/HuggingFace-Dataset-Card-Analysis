---
license: cc0-1.0
---

### Dataset description

33.000 transcribed text lines from historical newspapers (before 1878) along with the cropped images of the original scans

Text line based OCR
19.000 text lines in Antiqua
14.000 text lines in Fraktur
Transcribed using double-keying (99.95% accuracy)
Public Domain, CC0 (See copyright notice)
Best for training an OCR engine

The newspapers used are:
- Le Gratis luxembourgeois (1857-1858)
- Luxemburger Volks-Freund (1869-1876)
- L'Arlequin (1848-1848)
- Courrier du Grand-Duché de Luxembourg (1844-1868)
- L'Avenir (1868-1871)
- Der Wächter an der Sauer (1849-1869)
- Luxemburger Zeitung (1844-1845)
- Luxemburger Zeitung = Journal de Luxembourg (1858-1859)
- Der Volksfreund (1848-1849)
- Cäcilia (1862-1871)
- Kirchlicher Anzeiger für die Diözese Luxemburg (1871-1878)
- L'Indépendance luxembourgeoise (1871-1878)
- Luxemburger Anzeiger (1856)
- L'Union (1860-1871)
- Diekircher Wochenblatt (1837-1848)
- Das Vaterland (1869-1870)
- D'Wäschfra (1868-1878)
- Luxemburger Bauernzeitung (1857)
- Luxemburger Wort (1848-1878)

### URL for this dataset

https://data.bnl.lu/data/historical-newspapers/

### Dataset format

Two JSONL files (antiqua.jsonl.gz and fraktur.jsonl.gz) with the follwing fields:
- `font` is either antiqua or fraktur
- `img` is the filename of the associated image for the text
- `text` is the handcorrected double-keyed text transcribed from the image

Sample:
```json
{
  "font": "fraktur",
  "img": "fraktur-000011.png",
  "text": "Vidal die Vollmacht für Paris an. Auch"
}
```

In addition there are two `.zip` files with the associated images

### Dataset modality

Text and associated Images from Scans

### Dataset licence

Creative Commons Public Domain Dedication and Certification

### size of dataset

500MB-2GB

### Contact details for data custodian

opendata@bnl.etat.lu
