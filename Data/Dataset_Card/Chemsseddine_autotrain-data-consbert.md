---
task_categories:
- text-classification

---
# AutoTrain Dataset for project: consbert

## Dataset Description

This dataset has been automatically processed by AutoTrain for project consbert.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "text": "DECLARATION OF PERFORMANCE fermacell Screws 1. unique identification code of the product type 2. purpose of use 3. manufacturer 5. system(s) for assessment and verification of constancy of performance 6. harmonised standard Notified body(ies) 7. Declared performance Essential feature Reaction to fire Tensile strength Length Corrosion protection (Reis oeueelt Nr. FC-0103 A FC-0103 A Drywall screws type TSN for fastening gypsum fibreboards James Hardie Europe GmbH Bennigsen- Platz 1 D-40474 Disseldorf Tel. +49 800 3864001 E-Mail fermacell jameshardie.de System 4 DIN EN 14566:2008+A1:2009 Stichting Hout Research (2590) Performance Al fulfilled <63mm Phosphated - Class 48 The performance of the above product corresponds to the declared performance(s). The manufacturer mentioned aboveis solely responsible for the preparation of the declaration of performancein accordance with Regulation (EU) No. 305/2011. Signed for the manufacturer and on behalf of the manufacturerof: Dusseldorf, 01.01.2020 2020 James Hardie Europe GmbH. and designate registered and incorporated trademarks of James Hardie Technology Limited Dr. J\u00e9rg Brinkmann (CEO) AESTUVER Seite 1/1  ",
    "target": 1
  },
  {
    "text": "DERBIGUM\u201d MAKING BUILDINGS SMART 9 - Performances d\u00e9clar\u00e9es selon EN 13707 : 2004 + A2: 2009 Caract\u00e9ristiques essentielles Performances Unit\u00e9s R\u00e9sistance a un feu ext\u00e9rieur (Note 1) FRoof (t3) - R\u00e9action au feu F - Etanch\u00e9it\u00e9 a l\u2019eau Conforme - Propri\u00e9t\u00e9s en traction : R\u00e9sistance en traction LxT* 900 x 700(+4 20%) N/50 mm Allongement LxT* 45 x 45 (+ 15) % R\u00e9sistance aux racines NPD** - R\u00e9sistance au poinconnementstatique (A) 20 kg R\u00e9sistance au choc (A et B) NPD** mm R\u00e9sistance a la d\u00e9chirure LxT* 200 x 200 (+ 20%) N R\u00e9sistance des jonctions: R\u00e9sistance au pelage NPD** N/50 mm R\u00e9sistance au cisaillement NPD** N/50 mm Durabilit\u00e9 : Sous UV, eau et chaleur Conforme - Pliabilit\u00e9 a froid apr\u00e9s vieillissement a la -10 (+ 5) \u00b0C chaleur Pliabilit\u00e9 a froid -18 \u00b0C Substances dangereuses (Note 2) - * L signifie la direction longitudinale, T signifie la direction transversale **NPD signifie Performance Non D\u00e9termin\u00e9e Note 1: Aucune performance ne peut \u00e9tre donn\u00e9e pourle produit seul, la performance de r\u00e9sistance a un feu ext\u00e9rieur d\u2019une toiture d\u00e9pend du syst\u00e9me complet Note 2: En l\u2019absence de norme d\u2019essai europ\u00e9enne harmonis\u00e9e, aucune performanceli\u00e9e au comportementa la lixiviation ne peut \u00e9tre d\u00e9clar\u00e9e, la d\u00e9claration doit \u00e9tre \u00e9tablie selon les dispositions nationales en vigueur. 10 - Les performances du produit identifi\u00e9 aux points 1 et 2 ci-dessus sont conformes aux performances d\u00e9clar\u00e9es indiqu\u00e9es au point 9. La pr\u00e9sente d\u00e9claration des performances est \u00e9tablie sous la seule responsabilit\u00e9 du fabricant identifi\u00e9 au point 4 Sign\u00e9 pourle fabricant et en son nom par: Mr Steve Geubels, Group Operations Director Perwez ,30/09/2016 Page 2 of 2  ",
    "target": 8
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "text": "Value(dtype='string', id=None)",
  "target": "ClassLabel(num_classes=9, names=['0', '1', '2', '3', '4', '5', '6', '7', '8'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 59 |
| valid        | 18 |
