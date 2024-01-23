# Dataset Card for NBAiLab/bokmaal_admin

## Table of Contents
- [Dataset Description](#dataset-description)
- [Dataset Summary](#dataset-summary)
- [Data Fields](#data-fiels)
- [Dataset Creation](#dataset-creation)
- [Statistics](#statistics)
- [Document Types](#document-types)
- [Languages](#languages)
- [Publish Periode](#publish-periode)
- [Considerations for Using the Data](#considerations-for-using-the-data)
- [Social Impact of Dataset](#social-impact-of-dataset)
- [Discussion of Biases](#discussion-of-biases)
- [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
- [Dataset Curators](#dataset-curators)
- [Licensing Information](#licensing-information)
- [Citation Information](#citation-information)

## Dataset Description
- **Homepage:** https://github.com/NBAiLab/notram
- **Repository:** https://github.com/NBAiLab/notram
- **Paper:** https://arxiv.org/abs/2104.09617
- **Point of Contact:** [Freddy Wetjen][mailto:freddy.wetjen@nb.no]

## How to Use
```
from datasets import load_dataset
data = load_dataset("NBAiLab/bokmaal_admin")
```

### Dataset Summary
The bokmaal_admin dataset contains json lines with language training data. Here is an example json line:
```
{"id": "1006205", "doc_type": "cc100", "publish_year": 2021, "lang_fasttext": "no", "lang_fasttext_conf": "0.641", "text": "Eg har en PLAN! KOS deg og ha en fortryllende herlig pinse :)"}
```
## Data Fields
**id:** String with id to source of line and a unique identifier
**doc_type:** String describing type of media text extracted from (I.e. book,newspaper etc)
**publish_year:** String with year text published
**lang_fasttext:** String. Language of text identified by FastText
**lang_fasttext_conf:** String. Confidence calculated by FastText
**text:** String. The complete utf-8 document. If longer than 1M characters it is split.

### Dataset Creation
We are providing a **train** and a **validation** split. The standard size of the validation is a single 1GB file, while train is sharded in 1GB chunks. All files are gzipped.

Build date: 20211112 05:25

#### Initial Data Collection and Curation
The procedure for the dataset creation is described in detail in our paper.

## Statistics
### Document Types
| Source                                | Words         | Documents   | Words/Document   |
|--------------------------------------:|--------------:|------------:|-----------------:|
| books                                 | 6,380,459,425 | 179,928     | 35,461           |
| newspaper_ocr                         | 3,430,315,600 | 17,800,434  | 192              |
| newspaper_pdf                         | 1,322,713,993 | 2,578,379   | 513              |
| parliament                            | 505,936,380   | 3,772       | 134,129          |
| mc4                                   | 335,731,602   | 629,305     | 533              |
| maalfrid_regjeringen                  | 247,343,698   | 569,556     | 434              |
| facebook                              | 224,240,379   | 6,029,317   | 37               |
| newspapers_online_nb                  | 202,484,169   | 1,550,434   | 130              |
| cc100                                 | 178,306,026   | 415,438     | 429              |
| lovdata_transfer                      | 151,683,287   | 2,455,158   | 61               |
| wikipedia_download_nbo                | 67,973,672    | 337,685     | 201              |
| publicreports                         | 60,688,239    | 2,485       | 24,421           |
| maalfrid_fylkesmannen                 | 59,961,218    | 225,748     | 265              |
| maalfrid_ssb                          | 52,430,231    | 161,640     | 324              |
| maalfrid_uio                          | 51,941,921    | 205,859     | 252              |
| maalfrid_nve                          | 36,914,989    | 134,307     | 274              |
| lovdata_cd_odelsting_2005             | 30,759,585    | 1,512       | 20,343           |
| maalfrid_ntnu                         | 28,396,799    | 91,801      | 309              |
| government_nb                         | 26,180,035    | 1,778       | 14,724           |
| maalfrid_skatteetaten                 | 19,959,092    | 50,433      | 395              |
| maalfrid_vegvesen                     | 17,211,017    | 72,632      | 236              |
| maalfrid_fhi                          | 15,255,348    | 60,886      | 250              |
| maalfrid_uib                          | 14,942,918    | 54,175      | 275              |
| maalfrid_forskningsradet              | 14,842,039    | 41,564      | 357              |
| Published_article                     | 13,672,349    | 8,641       | 1,582            |
| maalfrid_domstol                      | 12,358,434    | 32,931      | 375              |
| maalfrid_nasjonalparkstyre            | 11,843,995    | 46,622      | 254              |
| maalfrid_nav                          | 9,860,610     | 35,635      | 276              |
| maalfrid_banenor                      | 9,418,904     | 33,241      | 283              |
| maalfrid_landbruksdirektoratet        | 9,306,807     | 29,919      | 311              |
| maalfrid_helsedirektoratet            | 8,846,278     | 30,601      | 289              |
| maalfrid_udir                         | 7,174,012     | 25,639      | 279              |
| maalfrid_nokut                        | 7,129,990     | 25,355      | 281              |
| oscar                                 | 6,645,855     | 20,520      | 323              |
| maalfrid_distriktssenteret            | 6,615,310     | 24,369      | 271              |
| maalfrid_patentstyret                 | 6,532,768     | 15,936      | 409              |
| maalfrid_oslomet                      | 6,179,568     | 16,991      | 363              |
| maalfrid_nmbu                         | 6,111,332     | 21,911      | 278              |
| maalfrid_difi                         | 5,906,257     | 22,634      | 260              |
| maalfrid_ptil                         | 5,417,850     | 19,492      | 277              |
| maalfrid_ks                           | 5,291,586     | 18,458      | 286              |
| maalfrid_nord                         | 5,220,333     | 22,139      | 235              |
| maalfrid_miljodirektoratet            | 5,057,030     | 16,276      | 310              |
| lovdata_cd_somb_rundskriv_2005        | 4,877,892     | 2,913       | 1,674            |
| maalfrid_kulturradet                  | 4,765,528     | 13,438      | 354              |
| maalfrid_hi                           | 4,371,332     | 14,953      | 292              |
| maalfrid_khrono                       | 4,334,418     | 13,657      | 317              |
| maalfrid_havarikommisjonen            | 4,324,589     | 13,785      | 313              |
| maalfrid_helsetilsynet                | 4,139,780     | 11,949      | 346              |
| maalfrid_veiviseren                   | 4,026,354     | 12,641      | 318              |
| maalfrid_kystverket                   | 3,986,569     | 15,948      | 249              |
| maalfrid_fiskeridir                   | 3,917,471     | 13,931      | 281              |
| maalfrid_imdi                         | 3,876,903     | 11,910      | 325              |
| maalfrid_klagenemndssekretariatet     | 3,627,643     | 9,907       | 366              |
| maalfrid_mattilsynet                  | 3,570,296     | 11,399      | 313              |
| maalfrid_jernbanedirektoratet         | 3,249,132     | 10,901      | 298              |
| maalfrid_husbanken                    | 3,205,560     | 9,956       | 321              |
| maalfrid_inn                          | 3,180,435     | 15,942      | 199              |
| maalfrid_ehelse                       | 3,169,426     | 13,781      | 229              |
| maalfrid_moreforsk                    | 3,149,028     | 11,288      | 278              |
| maalfrid_dibk                         | 3,075,479     | 10,192      | 301              |
| maalfrid_dsb                          | 2,931,468     | 9,116       | 321              |
| maalfrid_uia                          | 2,875,875     | 10,161      | 283              |
| maalfrid_hivolda                      | 2,825,217     | 8,503       | 332              |
| maalfrid_konkurransetilsynet          | 2,761,569     | 6,937       | 398              |
| maalfrid_riksrevisjonen               | 2,758,645     | 7,474       | 369              |
| lovdata_cd_sentrale_forskrifter_2005  | 2,730,182     | 4,952       | 551              |
| maalfrid_hiof                         | 2,700,988     | 11,976      | 225              |
| maalfrid_bufdir                       | 2,697,466     | 8,398       | 321              |
| maalfrid_forsvarsbygg                 | 2,683,162     | 9,920       | 270              |
| maalfrid_udi                          | 2,664,169     | 7,842       | 339              |
| maalfrid_norad                        | 2,574,013     | 6,832       | 376              |
| maalfrid_politiet                     | 2,540,239     | 7,562       | 335              |
| maalfrid_arkivverket                  | 2,540,064     | 8,338       | 304              |
| maalfrid_vkm                          | 2,539,216     | 8,036       | 315              |
| maalfrid_sdir                         | 2,370,087     | 7,819       | 303              |
| maalfrid_norges-bank                  | 2,240,269     | 6,157       | 363              |
| maalfrid_ngu                          | 2,237,688     | 9,121       | 245              |
| maalfrid_legemiddelverket             | 2,188,175     | 8,378       | 261              |
| maalfrid_hjelpemiddeldatabasen        | 2,159,289     | 12,899      | 167              |
| maalfrid_vetinst                      | 2,060,618     | 5,974       | 344              |
| maalfrid_seniorporten                 | 1,964,793     | 5,735       | 342              |
| maalfrid_aldringoghelse               | 1,829,458     | 4,715       | 388              |
| maalfrid_sykkelbynettverket           | 1,736,925     | 6,595       | 263              |
| maalfrid_bioteknologiradet            | 1,718,372     | 3,983       | 431              |
| maalfrid_riksantikvaren               | 1,648,807     | 5,549       | 297              |
| maalfrid_arbeidstilsynet              | 1,615,239     | 4,189       | 385              |
| maalfrid_custompublish                | 1,612,284     | 5,460       | 295              |
| maalfrid_nlr                          | 1,538,129     | 6,949       | 221              |
| maalfrid_dsa                          | 1,537,797     | 5,546       | 277              |
| maalfrid_sjt                          | 1,524,515     | 6,280       | 242              |
| maalfrid_dfo                          | 1,444,746     | 5,686       | 254              |
| maalfrid_sprakradet                   | 1,395,100     | 4,908       | 284              |
| maalfrid_kartverket                   | 1,377,475     | 6,001       | 229              |
| maalfrid_uis                          | 1,367,221     | 4,047       | 337              |
| maalfrid_ldo                          | 1,340,466     | 4,945       | 271              |
| maalfrid_nkom                         | 1,326,479     | 4,093       | 324              |
| maalfrid_kompetansenorge              | 1,316,195     | 5,409       | 243              |
| maalfrid_diskrimineringsnemnda        | 1,309,432     | 3,369       | 388              |
| maalfrid_arbeidsretten                | 1,284,610     | 4,106       | 312              |
| maalfrid_naku                         | 1,275,346     | 3,528       | 361              |
| maalfrid_forbrukerradet               | 1,247,911     | 4,339       | 287              |
| maalfrid_toll                         | 1,180,475     | 4,396       | 268              |
| maalfrid_himolde                      | 1,169,805     | 5,882       | 198              |
| maalfrid_artsdatabanken               | 1,123,755     | 3,043       | 369              |
| maalfrid_medietilsynet                | 1,120,669     | 4,219       | 265              |
| maalfrid_dirmin                       | 1,106,085     | 3,560       | 310              |
| maalfrid_usn                          | 1,079,920     | 3,964       | 272              |
| maalfrid_naturfag                     | 1,074,980     | 3,442       | 312              |
| maalfrid_forskningsetikk              | 1,050,995     | 2,835       | 370              |
| maalfrid_nibio                        | 1,018,312     | 4,418       | 230              |
| maalfrid_npd                          | 983,147       | 3,023       | 325              |
| maalfrid_fellesstudentsystem          | 979,009       | 6,086       | 160              |
| maalfrid_nhh                          | 959,716       | 3,547       | 270              |
| maalfrid_miljopakken                  | 921,711       | 3,876       | 237              |
| maalfrid_nyemetoder                   | 912,371       | 3,571       | 255              |
| maalfrid_nbim                         | 905,006       | 2,871       | 315              |
| lovdata_cd_lokaleforskrifter_2005     | 865,182       | 5,737       | 150              |
| maalfrid_unit                         | 863,597       | 4,278       | 201              |
| government                            | 863,481       | 15          | 57,565           |
| lovdata_cd_rtv_rundskriv_2005         | 851,334       | 5,557       | 153              |
| maalfrid_sykehuspartner               | 844,623       | 3,551       | 237              |
| maalfrid_statsbygg                    | 837,396       | 2,847       | 294              |
| lovdata_cd_skatt_rundskriv_2005       | 834,700       | 280         | 2,981            |
| maalfrid_diku                         | 820,160       | 3,060       | 268              |
| maalfrid_folketrygdfondet             | 817,411       | 2,403       | 340              |
| maalfrid_anskaffelser                 | 806,237       | 3,281       | 245              |
| maalfrid_godeidrettsanlegg            | 798,087       | 2,945       | 270              |
| maalfrid_hvl                          | 763,706       | 3,342       | 228              |
| maalfrid_kriminalitetsforebygging     | 750,695       | 2,811       | 267              |
| maalfrid_fiskeridirektoratet          | 703,340       | 2,139       | 328              |
| maalfrid_met                          | 689,904       | 3,894       | 177              |
| lovdata_cd_norgeslover_2005           | 654,973       | 545         | 1,201            |
| maalfrid_aho                          | 638,050       | 2,638       | 241              |
| maalfrid_barneombudet                 | 625,833       | 1,579       | 396              |
| maalfrid_luftfartstilsynet            | 608,528       | 2,218       | 274              |
| maalfrid_datatilsynet                 | 603,203       | 1,791       | 336              |
| maalfrid_xn--miljlftet-o8ab           | 586,635       | 2,217       | 264              |
| maalfrid_matematikksenteret           | 585,609       | 2,632       | 222              |
| maalfrid_sykehusinnkjop               | 549,824       | 2,653       | 207              |
| maalfrid_spesialenheten               | 533,643       | 1,241       | 430              |
| maalfrid_helsenorge                   | 520,386       | 1,670       | 311              |
| maalfrid_naturfagsenteret             | 512,334       | 1,777       | 288              |
| maalfrid_lottstift                    | 492,579       | 1,849       | 266              |
| maalfrid_sshf                         | 489,791       | 1,462       | 335              |
| maalfrid_nih                          | 480,388       | 2,313       | 207              |
| maalfrid_une                          | 442,146       | 935         | 472              |
| maalfrid_ceres                        | 417,870       | 1,623       | 257              |
| maalfrid_khio                         | 417,364       | 1,654       | 252              |
| maalfrid_skrivesenteret               | 408,989       | 1,876       | 218              |
| maalfrid_pasientsikkerhetsprogrammet  | 406,202       | 2,468       | 164              |
| maalfrid_nodnett                      | 400,250       | 1,581       | 253              |
| maalfrid_nhn                          | 380,617       | 1,989       | 191              |
| maalfrid_vestlandfylke                | 347,841       | 1,690       | 205              |
| maalfrid_nsm                          | 347,481       | 1,175       | 295              |
| maalfrid_spk                          | 338,368       | 1,087       | 311              |
| maalfrid_samordnaopptak               | 337,615       | 1,208       | 279              |
| lovdata_cd_rundskriv_lovavdeling_2005 | 334,659       | 320         | 1,045            |
| maalfrid_kriminalomsorgen             | 326,604       | 1,055       | 309              |
| maalfrid_fordelingsutvalget           | 320,403       | 1,180       | 271              |
| maalfrid_stami                        | 312,943       | 799         | 391              |
| maalfrid_mareano                      | 305,826       | 1,482       | 206              |
| maalfrid_nysgjerrigper                | 299,481       | 1,570       | 190              |
| maalfrid_natursekken                  | 297,159       | 2,187       | 135              |
| maalfrid_nidsenter                    | 296,232       | 855         | 346              |
| maalfrid_justervesenet                | 295,738       | 896         | 330              |
| maalfrid_matportalen                  | 270,759       | 920         | 294              |
| maalfrid_kunstkultursenteret          | 266,393       | 805         | 330              |
| maalfrid_digdir                       | 249,544       | 1,245       | 200              |
| maalfrid_kjonnsforskning              | 248,296       | 756         | 328              |
| maalfrid_forsvaret                    | 243,755       | 799         | 305              |
| maalfrid_gjenopptakelse               | 243,459       | 904         | 269              |
| maalfrid_forbrukertilsynet            | 241,234       | 766         | 314              |
| maalfrid_romsenter                    | 232,686       | 698         | 333              |
| maalfrid_geonorge                     | 220,003       | 1,062       | 207              |
| maalfrid_nupi                         | 206,031       | 726         | 283              |
| maalfrid_universell                   | 199,461       | 1,294       | 154              |
| maalfrid_ovf                          | 187,196       | 540         | 346              |
| maalfrid_vea-fs                       | 185,860       | 957         | 194              |
| maalfrid_nfi                          | 183,915       | 572         | 321              |
| maalfrid_ombudsmann                   | 181,429       | 313         | 579              |
| maalfrid_valgdirektoratet             | 176,937       | 659         | 268              |
| maalfrid_bibliotekutvikling           | 173,659       | 828         | 209              |
| maalfrid_nasjonalmuseet               | 173,044       | 426         | 406              |
| maalfrid_politihogskolen              | 168,943       | 724         | 233              |
| maalfrid_nb                           | 154,850       | 570         | 271              |
| maalfrid_regionaleforskningsfond      | 152,294       | 748         | 203              |
| maalfrid_opplaringslovutvalget        | 148,285       | 399         | 371              |
| maalfrid_beccle                       | 147,160       | 542         | 271              |
| maalfrid_jernbanemagasinet            | 141,276       | 280         | 504              |
| maalfrid_energimerking                | 138,944       | 530         | 262              |
| maalfrid_samas                        | 138,706       | 527         | 263              |
| maalfrid_pkh                          | 135,365       | 453         | 298              |
| maalfrid_traumebevisst                | 126,587       | 1,027       | 123              |
| maalfrid_npe                          | 124,648       | 531         | 234              |
| maalfrid_realfagsloyper               | 123,279       | 498         | 247              |
| maalfrid_vinmonopolet                 | 116,011       | 288         | 402              |
| maalfrid_nafkam                       | 115,290       | 335         | 344              |
| maalfrid_helfo                        | 109,740       | 517         | 212              |
| maalfrid_giek                         | 104,748       | 315         | 332              |
| maalfrid_polarhistorie                | 102,152       | 265         | 385              |
| maalfrid_okokrim                      | 91,030        | 274         | 332              |
| maalfrid_koro                         | 86,691        | 270         | 321              |
| maalfrid_politietssikkerhetstjeneste  | 83,250        | 246         | 338              |
| maalfrid_lokforerskolen               | 82,092        | 410         | 200              |
| maalfrid_konfliktraadet               | 81,638        | 236         | 345              |
| maalfrid_sismo                        | 81,184        | 186         | 436              |
| maalfrid_radetfordyreetikk            | 78,270        | 297         | 263              |
| maalfrid_squarespace                  | 77,333        | 255         | 303              |
| maalfrid_riksmekleren                 | 76,636        | 352         | 217              |
| maalfrid_brreg                        | 71,766        | 331         | 216              |
| maalfrid_riksteatret                  | 69,415        | 308         | 225              |
| maalfrid_generaladvokaten             | 63,969        | 195         | 328              |
| maalfrid_sivilforsvaret               | 63,303        | 280         | 226              |
| maalfrid_lanekassen                   | 62,069        | 174         | 356              |
| maalfrid_ffi                          | 60,454        | 144         | 419              |
| maalfrid_uit                          | 53,943        | 283         | 190              |
| maalfrid_akkreditert                  | 53,878        | 235         | 229              |
| maalfrid_lektor2                      | 48,998        | 278         | 176              |
| maalfrid_nynorsksenteret              | 47,745        | 207         | 230              |
| maalfrid_omsorgsforskning             | 46,908        | 196         | 239              |
| maalfrid_riksadvokaten                | 46,891        | 113         | 414              |
| maalfrid_nlb                          | 43,425        | 142         | 305              |
| maalfrid_unknown                      | 43,077        | 174         | 247              |
| maalfrid_dekom                        | 42,214        | 610         | 69               |
| maalfrid_kulturminnefondet            | 40,957        | 209         | 195              |
| maalfrid_varsom                       | 39,362        | 165         | 238              |
| maalfrid_openaccess                   | 36,978        | 107         | 345              |
| maalfrid_lokalhistorie                | 35,629        | 141         | 252              |
| maalfrid_sivilrett                    | 34,831        | 98          | 355              |
| maalfrid_denkulturelleskolesekken     | 34,167        | 156         | 219              |
| maalfrid_unesco                       | 32,206        | 97          | 332              |
| maalfrid_finansportalen               | 30,756        | 128         | 240              |
| maalfrid_htu                          | 29,233        | 108         | 270              |
| maalfrid_dep                          | 28,746        | 88          | 326              |
| maalfrid_yrkesfisker                  | 28,629        | 194         | 147              |
| maalfrid_ssn                          | 25,958        | 131         | 198              |
| maalfrid_informasjonskompetanse       | 24,635        | 159         | 154              |
| maalfrid_helseklage                   | 24,477        | 82          | 298              |
| maalfrid_forbrukereuropa              | 22,901        | 102         | 224              |
| maalfrid_kulturped                    | 21,673        | 61          | 355              |
| maalfrid_kulturoghelse                | 21,192        | 115         | 184              |
| maalfrid_nbsk                         | 20,379        | 124         | 164              |
| maalfrid_nyinorge                     | 20,353        | 43          | 473              |
| maalfrid_matogindustri                | 19,957        | 113         | 176              |
| maalfrid_fug                          | 19,910        | 66          | 301              |
| maalfrid_sinn                         | 19,682        | 87          | 226              |
| maalfrid_transport21                  | 19,666        | 62          | 317              |
| maalfrid_vergemal                     | 18,784        | 54          | 347              |
| maalfrid_konkursradet                 | 17,890        | 50          | 357              |
| maalfrid_xn--kvinneligomskjring-1ub   | 17,578        | 71          | 247              |
| maalfrid_feide                        | 16,493        | 115         | 143              |
| maalfrid_digidel                      | 15,548        | 91          | 170              |
| maalfrid_skattefunn                   | 15,185        | 50          | 303              |
| maalfrid_xn--tilbakefring-2jb         | 14,974        | 39          | 383              |
| maalfrid_memu                         | 14,965        | 65          | 230              |
| maalfrid_russamtalen                  | 14,672        | 53          | 276              |
| maalfrid_pts                          | 14,672        | 46          | 318              |
| maalfrid_regjeringsadvokaten          | 14,565        | 36          | 404              |
| maalfrid_nasjonaleturistveger         | 13,564        | 55          | 246              |
| maalfrid_samfunnskunnskap             | 12,499        | 46          | 271              |
| maalfrid_skeivtarkiv                  | 11,599        | 44          | 263              |
| maalfrid_forbrukerklageutvalget       | 11,415        | 39          | 292              |
| maalfrid_ah                           | 11,363        | 33          | 344              |
| maalfrid_fordelingsutvalet            | 11,329        | 21          | 539              |
| maalfrid_xn--forskerfr-t8a            | 11,062        | 81          | 136              |
| maalfrid_nettvett                     | 10,135        | 37          | 273              |
| maalfrid_laudim                       | 8,732         | 63          | 138              |
| maalfrid_uh-it                        | 7,131         | 126         | 56               |
| maalfrid_valg                         | 7,089         | 36          | 196              |
| maalfrid_mhfa                         | 6,287         | 52          | 120              |
| maalfrid_spinn-inn                    | 6,286         | 24          | 261              |
| maalfrid_npolar                       | 6,200         | 22          | 281              |
| maalfrid_bastoyfengsel                | 6,194         | 40          | 154              |
| maalfrid_miljoklagenemnda             | 5,432         | 23          | 236              |
| maalfrid_prosjektveiviseren           | 5,154         | 15          | 343              |
| maalfrid_voldsoffererstatning         | 5,129         | 21          | 244              |
| maalfrid_aldersvennlig                | 4,540         | 23          | 197              |
| maalfrid_hjelpelinjen                 | 4,514         | 18          | 250              |
| maalfrid_sevuppt                      | 4,491         | 16          | 280              |
| maalfrid_barentswatch                 | 4,099         | 26          | 157              |
| maalfrid_global                       | 4,079         | 16          | 254              |
| maalfrid_kk-utvalget                  | 3,813         | 14          | 272              |
| maalfrid_forsvaretsmuseer             | 3,768         | 33          | 114              |
| maalfrid_utdanningiverden             | 2,876         | 7           | 410              |
| maalfrid_fmfiavo@fylkesmannen         | 2,830         | 33          | 85               |
| maalfrid_iearth                       | 2,747         | 15          | 183              |
| maalfrid_pst                          | 2,667         | 12          | 222              |
| maalfrid_altinn                       | 2,600         | 10          | 260              |
| maalfrid_overgangsbolig               | 2,580         | 16          | 161              |
| maalfrid_designavgang                 | 2,541         | 20          | 127              |
| maalfrid_kantinekurset                | 2,319         | 17          | 136              |
| maalfrid_velgekte                     | 2,269         | 10          | 226              |
| maalfrid_okopark                      | 2,261         | 7           | 323              |
| maalfrid_musikkbasertmiljobehandling  | 2,118         | 13          | 162              |
| maalfrid_arkitektur                   | 1,922         | 9           | 213              |
| maalfrid_agropub                      | 1,875         | 6           | 312              |
| maalfrid_alleteller                   | 1,511         | 7           | 215              |
| maalfrid_norskpetroleum               | 1,355         | 20          | 67               |
| maalfrid_lykillinn                    | 1,349         | 4           | 337              |
| maalfrid_oslofengsel                  | 1,159         | 5           | 231              |
| maalfrid_hjorteviltregisteret         | 910           | 2           | 455              |
| maalfrid_umb                          | 875           | 5           | 175              |
| maalfrid_webhuset                     | 849           | 3           | 283              |
| maalfrid_anleggsregisteret            | 702           | 3           | 234              |
| maalfrid_utdanning                    | 687           | 5           | 137              |
| maalfrid_mangfoldsprisen              | 538           | 2           | 269              |
| maalfrid_nynorskbok                   | 464           | 4           | 116              |
| maalfrid_mammapresenterer             | 447           | 2           | 223              |
| maalfrid_ringerikefengsel             | 435           | 3           | 145              |
| maalfrid_romerikefengsel              | 252           | 2           | 126              |
| maalfrid_indreostfoldfengsel          | 215           | 3           | 71               |
| wikipedia_huggingface                 | 209           | 4           | 52               |
| maalfrid_yr                           | 209           | 1           | 209              |
| maalfrid_xn--kroppsvingsforskning-gcc | 162           | 1           | 162              |
| maalfrid_retttilaalese                | 160           | 2           | 80               |
| maalfrid_grunderskolen                | 117           | 1           | 117              |
| maalfrid_nodsms                       | 98            | 1           | 98               |
| maalfrid_karriereveiledning           | 32            | 3           | 10               |
| maalfrid_sikkerhverdag                | 19            | 1           | 19               |

### Languages
| Language   | Words          | Documents   |   Words/Document |
|-----------:|---------------:|------------:|-----------------:|
| no         | 13,827,935,821 | 34,804,446  |              397 |

### Publish Periode
|   Decade | Words         | Documents   | Words/Document   |
|---------:|--------------:|------------:|-----------------:|
|     2020 | 2,627,953,523 | 8,645,421   | 710              |
|     2010 | 4,313,046,574 | 17,265,618  | 2,802            |
|     2000 | 2,749,348,382 | 4,303,662   | 8,388            |
|     1990 | 2,847,964,191 | 3,290,177   | 8,828            |
|     1980 | 1,289,623,151 | 1,299,568   | 10,006           |

## Considerations for Using the Data
This corpus contains data under copyright and is not allowed to be used outide the National Library of Norway. The dataset should not be distributed.

### Discussion of Biases
Please refer to our paper.

### Dataset Curators
Freddy.wetjen@nb.no
Per.Kummervold@nb.no

### Licensing Information
Not lisenced for use outside the National Library of Norway.

### Citation Information
We are preparing an article with detailed information about this corpus. Until it is published, please cite out paper discussing the first version of this corpus:
```
@inproceedings{kummervold-etal-2021-operationalizing,
title = {Operationalizing a National Digital Library: The Case for a {N}orwegian Transformer Model},
author = {Kummervold, Per E  and
De la Rosa, Javier  and
Wetjen, Freddy  and
Brygfjeld, Svein Arne",
booktitle = {Proceedings of the 23rd Nordic Conference on Computational Linguistics (NoDaLiDa)},
year = "2021",
address = "Reykjavik, Iceland (Online)",
publisher = {Link{"o}ping University Electronic Press, Sweden},
url = "https://aclanthology.org/2021.nodalida-main.3",
pages = "20--29",
abstract = "In this work, we show the process of building a large-scale training set from digital and digitized collections at a national library. The resulting Bidirectional Encoder Representations from Transformers (BERT)-based language model for Norwegian outperforms multilingual BERT (mBERT) models in several token and sequence classification tasks for both Norwegian Bokm{aa}l and Norwegian Nynorsk. Our model also improves the mBERT performance for other languages present in the corpus such as English, Swedish, and Danish. For languages not included in the corpus, the weights degrade moderately while keeping strong multilingual properties. Therefore, we show that building high-quality models within a memory institution using somewhat noisy optical character recognition (OCR) content is feasible, and we hope to pave the way for other memory institutions to follow.",
}
```
