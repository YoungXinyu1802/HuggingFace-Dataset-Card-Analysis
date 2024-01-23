---
annotations_creators:
- expert-generated
language:
- pl
language_creators:
- expert-generated
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: NKJP1M
size_categories:
- 10K<n<100K
source_datasets:
- original
tags:
- National Corpus of Polish
- Narodowy Korpus Języka Polskiego
task_categories:
- token-classification
task_ids:
- part-of-speech
- lemmatization
dataset_info:
  features:
  - name: nkjp_text
    dtype: string
  - name: nkjp_par
    dtype: string
  - name: nkjp_sent
    dtype: string
  - name: tokens
    sequence: string
  - name: lemmas
    sequence: string
  - name: cposes
    sequence:
      class_label:
        names:
          0: A
          1: Adv
          2: Comp
          3: Conj
          4: Dig
          5: Interj
          6: N
          7: Num
          8: Part
          9: Prep
          10: Punct
          11: V
          12: X
  - name: poses
    sequence:
      class_label:
        names:
          0: adj
          1: adja
          2: adjc
          3: adjp
          4: adv
          5: aglt
          6: bedzie
          7: brev
          8: comp
          9: conj
          10: depr
          11: dig
          12: fin
          13: frag
          14: ger
          15: imps
          16: impt
          17: inf
          18: interj
          19: interp
          20: num
          21: numcomp
          22: pact
          23: pacta
          24: pant
          25: part
          26: pcon
          27: ppas
          28: ppron12
          29: ppron3
          30: praet
          31: pred
          32: prep
          33: romandig
          34: siebie
          35: subst
          36: sym
          37: winien
          38: xxs
          39: xxx
  - name: tags
    sequence:
      class_label:
        names:
          0: adj:pl:acc:f:com
          1: adj:pl:acc:f:pos
          2: adj:pl:acc:f:sup
          3: adj:pl:acc:m1:com
          4: adj:pl:acc:m1:pos
          5: adj:pl:acc:m1:sup
          6: adj:pl:acc:m2:com
          7: adj:pl:acc:m2:pos
          8: adj:pl:acc:m2:sup
          9: adj:pl:acc:m3:com
          10: adj:pl:acc:m3:pos
          11: adj:pl:acc:m3:sup
          12: adj:pl:acc:n:com
          13: adj:pl:acc:n:pos
          14: adj:pl:acc:n:sup
          15: adj:pl:dat:f:com
          16: adj:pl:dat:f:pos
          17: adj:pl:dat:f:sup
          18: adj:pl:dat:m1:com
          19: adj:pl:dat:m1:pos
          20: adj:pl:dat:m1:sup
          21: adj:pl:dat:m2:pos
          22: adj:pl:dat:m3:com
          23: adj:pl:dat:m3:pos
          24: adj:pl:dat:n:pos
          25: adj:pl:dat:n:sup
          26: adj:pl:gen:f:com
          27: adj:pl:gen:f:pos
          28: adj:pl:gen:f:sup
          29: adj:pl:gen:m1:com
          30: adj:pl:gen:m1:pos
          31: adj:pl:gen:m1:sup
          32: adj:pl:gen:m2:com
          33: adj:pl:gen:m2:pos
          34: adj:pl:gen:m2:sup
          35: adj:pl:gen:m3:com
          36: adj:pl:gen:m3:pos
          37: adj:pl:gen:m3:sup
          38: adj:pl:gen:n:com
          39: adj:pl:gen:n:pos
          40: adj:pl:gen:n:sup
          41: adj:pl:inst:f:com
          42: adj:pl:inst:f:pos
          43: adj:pl:inst:f:sup
          44: adj:pl:inst:m1:com
          45: adj:pl:inst:m1:pos
          46: adj:pl:inst:m1:sup
          47: adj:pl:inst:m2:pos
          48: adj:pl:inst:m3:com
          49: adj:pl:inst:m3:pos
          50: adj:pl:inst:m3:sup
          51: adj:pl:inst:n:com
          52: adj:pl:inst:n:pos
          53: adj:pl:inst:n:sup
          54: adj:pl:loc:f:com
          55: adj:pl:loc:f:pos
          56: adj:pl:loc:f:sup
          57: adj:pl:loc:m1:com
          58: adj:pl:loc:m1:pos
          59: adj:pl:loc:m1:sup
          60: adj:pl:loc:m2:pos
          61: adj:pl:loc:m3:com
          62: adj:pl:loc:m3:pos
          63: adj:pl:loc:m3:sup
          64: adj:pl:loc:n:com
          65: adj:pl:loc:n:pos
          66: adj:pl:loc:n:sup
          67: adj:pl:nom:f:com
          68: adj:pl:nom:f:pos
          69: adj:pl:nom:f:sup
          70: adj:pl:nom:m1:com
          71: adj:pl:nom:m1:pos
          72: adj:pl:nom:m1:sup
          73: adj:pl:nom:m2:com
          74: adj:pl:nom:m2:pos
          75: adj:pl:nom:m2:sup
          76: adj:pl:nom:m3:com
          77: adj:pl:nom:m3:pos
          78: adj:pl:nom:m3:sup
          79: adj:pl:nom:n:com
          80: adj:pl:nom:n:pos
          81: adj:pl:nom:n:sup
          82: adj:pl:voc:f:pos
          83: adj:pl:voc:m1:pos
          84: adj:pl:voc:m2:pos
          85: adj:pl:voc:n:pos
          86: adj:sg:acc:f:com
          87: adj:sg:acc:f:pos
          88: adj:sg:acc:f:sup
          89: adj:sg:acc:m1:com
          90: adj:sg:acc:m1:pos
          91: adj:sg:acc:m1:sup
          92: adj:sg:acc:m2:com
          93: adj:sg:acc:m2:pos
          94: adj:sg:acc:m2:sup
          95: adj:sg:acc:m3:com
          96: adj:sg:acc:m3:pos
          97: adj:sg:acc:m3:sup
          98: adj:sg:acc:n:com
          99: adj:sg:acc:n:pos
          100: adj:sg:acc:n:sup
          101: adj:sg:dat:f:com
          102: adj:sg:dat:f:pos
          103: adj:sg:dat:f:sup
          104: adj:sg:dat:m1:com
          105: adj:sg:dat:m1:pos
          106: adj:sg:dat:m1:sup
          107: adj:sg:dat:m2:pos
          108: adj:sg:dat:m3:com
          109: adj:sg:dat:m3:pos
          110: adj:sg:dat:m3:sup
          111: adj:sg:dat:n:com
          112: adj:sg:dat:n:pos
          113: adj:sg:dat:n:sup
          114: adj:sg:gen:f:com
          115: adj:sg:gen:f:pos
          116: adj:sg:gen:f:sup
          117: adj:sg:gen:m1:com
          118: adj:sg:gen:m1:pos
          119: adj:sg:gen:m1:sup
          120: adj:sg:gen:m2:pos
          121: adj:sg:gen:m2:sup
          122: adj:sg:gen:m3:com
          123: adj:sg:gen:m3:pos
          124: adj:sg:gen:m3:sup
          125: adj:sg:gen:n:com
          126: adj:sg:gen:n:pos
          127: adj:sg:gen:n:sup
          128: adj:sg:inst:f:com
          129: adj:sg:inst:f:pos
          130: adj:sg:inst:f:sup
          131: adj:sg:inst:m1:com
          132: adj:sg:inst:m1:pos
          133: adj:sg:inst:m1:sup
          134: adj:sg:inst:m2:com
          135: adj:sg:inst:m2:pos
          136: adj:sg:inst:m2:sup
          137: adj:sg:inst:m3:com
          138: adj:sg:inst:m3:pos
          139: adj:sg:inst:m3:sup
          140: adj:sg:inst:n:com
          141: adj:sg:inst:n:pos
          142: adj:sg:inst:n:sup
          143: adj:sg:loc:f:com
          144: adj:sg:loc:f:pos
          145: adj:sg:loc:f:sup
          146: adj:sg:loc:m1:com
          147: adj:sg:loc:m1:pos
          148: adj:sg:loc:m1:sup
          149: adj:sg:loc:m2:com
          150: adj:sg:loc:m2:pos
          151: adj:sg:loc:m3:com
          152: adj:sg:loc:m3:pos
          153: adj:sg:loc:m3:sup
          154: adj:sg:loc:n:com
          155: adj:sg:loc:n:pos
          156: adj:sg:loc:n:sup
          157: adj:sg:nom:f:com
          158: adj:sg:nom:f:pos
          159: adj:sg:nom:f:sup
          160: adj:sg:nom:m1:com
          161: adj:sg:nom:m1:pos
          162: adj:sg:nom:m1:sup
          163: adj:sg:nom:m2:com
          164: adj:sg:nom:m2:pos
          165: adj:sg:nom:m2:sup
          166: adj:sg:nom:m3:com
          167: adj:sg:nom:m3:pos
          168: adj:sg:nom:m3:sup
          169: adj:sg:nom:n:com
          170: adj:sg:nom:n:pos
          171: adj:sg:nom:n:sup
          172: adj:sg:voc:f:pos
          173: adj:sg:voc:f:sup
          174: adj:sg:voc:m1:pos
          175: adj:sg:voc:m1:sup
          176: adj:sg:voc:m2:pos
          177: adj:sg:voc:m3:pos
          178: adj:sg:voc:n:pos
          179: adja
          180: adjc
          181: adjp:dat
          182: adjp:gen
          183: adv
          184: adv:com
          185: adv:pos
          186: adv:sup
          187: aglt:pl:pri:imperf:nwok
          188: aglt:pl:sec:imperf:nwok
          189: aglt:sg:pri:imperf:nwok
          190: aglt:sg:pri:imperf:wok
          191: aglt:sg:sec:imperf:nwok
          192: aglt:sg:sec:imperf:wok
          193: bedzie:pl:pri:imperf
          194: bedzie:pl:sec:imperf
          195: bedzie:pl:ter:imperf
          196: bedzie:sg:pri:imperf
          197: bedzie:sg:sec:imperf
          198: bedzie:sg:ter:imperf
          199: brev:npun
          200: brev:pun
          201: comp
          202: conj
          203: depr:pl:acc:m2
          204: depr:pl:nom:m2
          205: depr:pl:voc:m2
          206: dig
          207: fin:pl:pri:imperf
          208: fin:pl:pri:perf
          209: fin:pl:sec:imperf
          210: fin:pl:sec:perf
          211: fin:pl:ter:imperf
          212: fin:pl:ter:perf
          213: fin:sg:pri:imperf
          214: fin:sg:pri:perf
          215: fin:sg:sec:imperf
          216: fin:sg:sec:perf
          217: fin:sg:ter:imperf
          218: fin:sg:ter:perf
          219: frag
          220: ger:pl:acc:n:imperf:aff
          221: ger:pl:acc:n:perf:aff
          222: ger:pl:dat:n:perf:aff
          223: ger:pl:gen:n:imperf:aff
          224: ger:pl:gen:n:perf:aff
          225: ger:pl:inst:n:imperf:aff
          226: ger:pl:inst:n:perf:aff
          227: ger:pl:loc:n:imperf:aff
          228: ger:pl:loc:n:perf:aff
          229: ger:pl:nom:n:imperf:aff
          230: ger:pl:nom:n:perf:aff
          231: ger:sg:acc:n:imperf:aff
          232: ger:sg:acc:n:imperf:neg
          233: ger:sg:acc:n:perf:aff
          234: ger:sg:acc:n:perf:neg
          235: ger:sg:dat:n:imperf:aff
          236: ger:sg:dat:n:perf:aff
          237: ger:sg:dat:n:perf:neg
          238: ger:sg:gen:n:imperf:aff
          239: ger:sg:gen:n:imperf:neg
          240: ger:sg:gen:n:perf:aff
          241: ger:sg:gen:n:perf:neg
          242: ger:sg:inst:n:imperf:aff
          243: ger:sg:inst:n:imperf:neg
          244: ger:sg:inst:n:perf:aff
          245: ger:sg:inst:n:perf:neg
          246: ger:sg:loc:n:imperf:aff
          247: ger:sg:loc:n:imperf:neg
          248: ger:sg:loc:n:perf:aff
          249: ger:sg:loc:n:perf:neg
          250: ger:sg:nom:n:imperf:aff
          251: ger:sg:nom:n:imperf:neg
          252: ger:sg:nom:n:perf:aff
          253: ger:sg:nom:n:perf:neg
          254: imps:imperf
          255: imps:perf
          256: impt:pl:pri:imperf
          257: impt:pl:pri:perf
          258: impt:pl:sec:imperf
          259: impt:pl:sec:perf
          260: impt:sg:pri:imperf
          261: impt:sg:sec:imperf
          262: impt:sg:sec:perf
          263: inf:imperf
          264: inf:perf
          265: interj
          266: interp
          267: num:pl:acc:f:congr:ncol
          268: num:pl:acc:f:rec
          269: num:pl:acc:f:rec:ncol
          270: num:pl:acc:m1:rec
          271: num:pl:acc:m1:rec:col
          272: num:pl:acc:m1:rec:ncol
          273: num:pl:acc:m2:congr:ncol
          274: num:pl:acc:m2:rec
          275: num:pl:acc:m2:rec:ncol
          276: num:pl:acc:m3:congr
          277: num:pl:acc:m3:congr:ncol
          278: num:pl:acc:m3:rec
          279: num:pl:acc:m3:rec:ncol
          280: num:pl:acc:n:congr:ncol
          281: num:pl:acc:n:rec
          282: num:pl:acc:n:rec:col
          283: num:pl:acc:n:rec:ncol
          284: num:pl:dat:f:congr
          285: num:pl:dat:f:congr:ncol
          286: num:pl:dat:m1:congr
          287: num:pl:dat:m1:congr:col
          288: num:pl:dat:m1:congr:ncol
          289: num:pl:dat:m2:congr
          290: num:pl:dat:m3:congr:ncol
          291: num:pl:dat:n:congr
          292: num:pl:dat:n:congr:ncol
          293: num:pl:gen:f:congr
          294: num:pl:gen:f:congr:ncol
          295: num:pl:gen:f:rec
          296: num:pl:gen:f:rec:ncol
          297: num:pl:gen:m1:congr
          298: num:pl:gen:m1:congr:ncol
          299: num:pl:gen:m1:rec
          300: num:pl:gen:m1:rec:col
          301: num:pl:gen:m2:congr
          302: num:pl:gen:m2:congr:ncol
          303: num:pl:gen:m2:rec
          304: num:pl:gen:m3:congr
          305: num:pl:gen:m3:congr:ncol
          306: num:pl:gen:m3:rec
          307: num:pl:gen:m3:rec:ncol
          308: num:pl:gen:n:congr
          309: num:pl:gen:n:congr:ncol
          310: num:pl:gen:n:rec
          311: num:pl:gen:n:rec:col
          312: num:pl:inst:f:congr
          313: num:pl:inst:f:congr:ncol
          314: num:pl:inst:m1:congr
          315: num:pl:inst:m1:congr:ncol
          316: num:pl:inst:m1:rec:col
          317: num:pl:inst:m2:congr
          318: num:pl:inst:m2:congr:ncol
          319: num:pl:inst:m3:congr
          320: num:pl:inst:m3:congr:ncol
          321: num:pl:inst:n:congr
          322: num:pl:inst:n:congr:ncol
          323: num:pl:inst:n:rec:col
          324: num:pl:loc:f:congr
          325: num:pl:loc:f:congr:ncol
          326: num:pl:loc:m1:congr
          327: num:pl:loc:m1:congr:ncol
          328: num:pl:loc:m2:congr
          329: num:pl:loc:m2:congr:ncol
          330: num:pl:loc:m3:congr
          331: num:pl:loc:m3:congr:ncol
          332: num:pl:loc:n:congr
          333: num:pl:loc:n:congr:ncol
          334: num:pl:nom:f:congr:ncol
          335: num:pl:nom:f:rec
          336: num:pl:nom:f:rec:ncol
          337: num:pl:nom:m1:congr:ncol
          338: num:pl:nom:m1:rec
          339: num:pl:nom:m1:rec:col
          340: num:pl:nom:m1:rec:ncol
          341: num:pl:nom:m2:congr:ncol
          342: num:pl:nom:m2:rec
          343: num:pl:nom:m2:rec:ncol
          344: num:pl:nom:m3:congr:ncol
          345: num:pl:nom:m3:rec
          346: num:pl:nom:m3:rec:ncol
          347: num:pl:nom:n:congr
          348: num:pl:nom:n:congr:ncol
          349: num:pl:nom:n:rec
          350: num:pl:nom:n:rec:col
          351: num:pl:nom:n:rec:ncol
          352: num:sg:acc:f:rec
          353: num:sg:acc:f:rec:ncol
          354: num:sg:acc:m1:rec:ncol
          355: num:sg:acc:m2:rec
          356: num:sg:acc:m3:rec
          357: num:sg:acc:m3:rec:ncol
          358: num:sg:acc:n:rec
          359: num:sg:gen:f:rec
          360: num:sg:gen:m3:rec
          361: num:sg:gen:n:rec
          362: num:sg:inst:m3:rec
          363: num:sg:loc:f:rec
          364: num:sg:loc:m3:congr
          365: num:sg:loc:m3:rec
          366: num:sg:nom:f:rec
          367: num:sg:nom:m2:rec
          368: num:sg:nom:m3:rec
          369: num:sg:nom:m3:rec:ncol
          370: num:sg:nom:n:rec
          371: numcomp
          372: pact:pl:acc:f:imperf:aff
          373: pact:pl:acc:f:imperf:neg
          374: pact:pl:acc:m1:imperf:aff
          375: pact:pl:acc:m2:imperf:aff
          376: pact:pl:acc:m3:imperf:aff
          377: pact:pl:acc:m3:imperf:neg
          378: pact:pl:acc:n:imperf:aff
          379: pact:pl:acc:n:imperf:neg
          380: pact:pl:dat:f:imperf:aff
          381: pact:pl:dat:m1:imperf:aff
          382: pact:pl:dat:m2:imperf:aff
          383: pact:pl:dat:m3:imperf:aff
          384: pact:pl:dat:n:imperf:aff
          385: pact:pl:gen:f:imperf:aff
          386: pact:pl:gen:f:imperf:neg
          387: pact:pl:gen:m1:imperf:aff
          388: pact:pl:gen:m1:imperf:neg
          389: pact:pl:gen:m2:imperf:aff
          390: pact:pl:gen:m3:imperf:aff
          391: pact:pl:gen:m3:imperf:neg
          392: pact:pl:gen:n:imperf:aff
          393: pact:pl:inst:f:imperf:aff
          394: pact:pl:inst:m1:imperf:aff
          395: pact:pl:inst:m2:imperf:aff
          396: pact:pl:inst:m3:imperf:aff
          397: pact:pl:inst:m3:imperf:neg
          398: pact:pl:inst:n:imperf:aff
          399: pact:pl:inst:n:imperf:neg
          400: pact:pl:loc:f:imperf:aff
          401: pact:pl:loc:m1:imperf:aff
          402: pact:pl:loc:m3:imperf:aff
          403: pact:pl:loc:m3:imperf:neg
          404: pact:pl:loc:n:imperf:aff
          405: pact:pl:loc:n:imperf:neg
          406: pact:pl:nom:f:imperf:aff
          407: pact:pl:nom:f:imperf:neg
          408: pact:pl:nom:m1:imperf:aff
          409: pact:pl:nom:m2:imperf:aff
          410: pact:pl:nom:m3:imperf:aff
          411: pact:pl:nom:n:imperf:aff
          412: pact:pl:nom:n:imperf:neg
          413: pact:pl:voc:f:imperf:aff
          414: pact:sg:acc:f:imperf:aff
          415: pact:sg:acc:f:imperf:neg
          416: pact:sg:acc:m1:imperf:aff
          417: pact:sg:acc:m2:imperf:aff
          418: pact:sg:acc:m3:imperf:aff
          419: pact:sg:acc:n:imperf:aff
          420: pact:sg:acc:n:imperf:neg
          421: pact:sg:dat:f:imperf:aff
          422: pact:sg:dat:m1:imperf:aff
          423: pact:sg:dat:m2:imperf:aff
          424: pact:sg:dat:m3:imperf:aff
          425: pact:sg:dat:n:imperf:aff
          426: pact:sg:gen:f:imperf:aff
          427: pact:sg:gen:f:imperf:neg
          428: pact:sg:gen:m1:imperf:aff
          429: pact:sg:gen:m1:imperf:neg
          430: pact:sg:gen:m2:imperf:aff
          431: pact:sg:gen:m3:imperf:aff
          432: pact:sg:gen:m3:imperf:neg
          433: pact:sg:gen:n:imperf:aff
          434: pact:sg:gen:n:imperf:neg
          435: pact:sg:inst:f:imperf:aff
          436: pact:sg:inst:f:imperf:neg
          437: pact:sg:inst:m1:imperf:aff
          438: pact:sg:inst:m1:imperf:neg
          439: pact:sg:inst:m2:imperf:aff
          440: pact:sg:inst:m2:imperf:neg
          441: pact:sg:inst:m3:imperf:aff
          442: pact:sg:inst:m3:imperf:neg
          443: pact:sg:inst:n:imperf:aff
          444: pact:sg:loc:f:imperf:aff
          445: pact:sg:loc:f:imperf:neg
          446: pact:sg:loc:m1:imperf:aff
          447: pact:sg:loc:m2:imperf:aff
          448: pact:sg:loc:m3:imperf:aff
          449: pact:sg:loc:m3:imperf:neg
          450: pact:sg:loc:n:imperf:aff
          451: pact:sg:loc:n:imperf:neg
          452: pact:sg:nom:f:imperf:aff
          453: pact:sg:nom:f:imperf:neg
          454: pact:sg:nom:m1:imperf:aff
          455: pact:sg:nom:m1:imperf:neg
          456: pact:sg:nom:m2:imperf:aff
          457: pact:sg:nom:m3:imperf:aff
          458: pact:sg:nom:m3:imperf:neg
          459: pact:sg:nom:n:imperf:aff
          460: pact:sg:nom:n:imperf:neg
          461: pact:sg:voc:m1:imperf:aff
          462: pacta
          463: pant:perf
          464: part
          465: part:nwok
          466: part:wok
          467: pcon:imperf
          468: ppas:pl:acc:f:imperf:aff
          469: ppas:pl:acc:f:perf:aff
          470: ppas:pl:acc:f:perf:neg
          471: ppas:pl:acc:m1:imperf:aff
          472: ppas:pl:acc:m1:imperf:neg
          473: ppas:pl:acc:m1:perf:aff
          474: ppas:pl:acc:m1:perf:neg
          475: ppas:pl:acc:m2:imperf:aff
          476: ppas:pl:acc:m2:perf:aff
          477: ppas:pl:acc:m3:imperf:aff
          478: ppas:pl:acc:m3:perf:aff
          479: ppas:pl:acc:m3:perf:neg
          480: ppas:pl:acc:n:imperf:aff
          481: ppas:pl:acc:n:imperf:neg
          482: ppas:pl:acc:n:perf:aff
          483: ppas:pl:acc:n:perf:neg
          484: ppas:pl:dat:f:imperf:aff
          485: ppas:pl:dat:f:perf:aff
          486: ppas:pl:dat:f:perf:neg
          487: ppas:pl:dat:m1:imperf:aff
          488: ppas:pl:dat:m1:perf:aff
          489: ppas:pl:dat:m1:perf:neg
          490: ppas:pl:dat:m2:imperf:aff
          491: ppas:pl:dat:m3:imperf:aff
          492: ppas:pl:dat:m3:perf:aff
          493: ppas:pl:dat:n:imperf:aff
          494: ppas:pl:dat:n:perf:aff
          495: ppas:pl:gen:f:imperf:aff
          496: ppas:pl:gen:f:imperf:neg
          497: ppas:pl:gen:f:perf:aff
          498: ppas:pl:gen:f:perf:neg
          499: ppas:pl:gen:m1:imperf:aff
          500: ppas:pl:gen:m1:imperf:neg
          501: ppas:pl:gen:m1:perf:aff
          502: ppas:pl:gen:m1:perf:neg
          503: ppas:pl:gen:m2:imperf:aff
          504: ppas:pl:gen:m2:perf:aff
          505: ppas:pl:gen:m3:imperf:aff
          506: ppas:pl:gen:m3:imperf:neg
          507: ppas:pl:gen:m3:perf:aff
          508: ppas:pl:gen:m3:perf:neg
          509: ppas:pl:gen:n:imperf:aff
          510: ppas:pl:gen:n:perf:aff
          511: ppas:pl:gen:n:perf:neg
          512: ppas:pl:inst:f:imperf:aff
          513: ppas:pl:inst:f:perf:aff
          514: ppas:pl:inst:m1:imperf:aff
          515: ppas:pl:inst:m1:perf:aff
          516: ppas:pl:inst:m2:perf:aff
          517: ppas:pl:inst:m3:imperf:aff
          518: ppas:pl:inst:m3:perf:aff
          519: ppas:pl:inst:n:imperf:aff
          520: ppas:pl:inst:n:perf:aff
          521: ppas:pl:loc:f:imperf:aff
          522: ppas:pl:loc:f:imperf:neg
          523: ppas:pl:loc:f:perf:aff
          524: ppas:pl:loc:f:perf:neg
          525: ppas:pl:loc:m1:imperf:aff
          526: ppas:pl:loc:m1:perf:aff
          527: ppas:pl:loc:m2:imperf:aff
          528: ppas:pl:loc:m3:imperf:aff
          529: ppas:pl:loc:m3:perf:aff
          530: ppas:pl:loc:m3:perf:neg
          531: ppas:pl:loc:n:imperf:aff
          532: ppas:pl:loc:n:perf:aff
          533: ppas:pl:loc:n:perf:neg
          534: ppas:pl:nom:f:imperf:aff
          535: ppas:pl:nom:f:imperf:neg
          536: ppas:pl:nom:f:perf:aff
          537: ppas:pl:nom:f:perf:neg
          538: ppas:pl:nom:m1:imperf:aff
          539: ppas:pl:nom:m1:imperf:neg
          540: ppas:pl:nom:m1:perf:aff
          541: ppas:pl:nom:m1:perf:neg
          542: ppas:pl:nom:m2:imperf:aff
          543: ppas:pl:nom:m2:perf:aff
          544: ppas:pl:nom:m3:imperf:aff
          545: ppas:pl:nom:m3:imperf:neg
          546: ppas:pl:nom:m3:perf:aff
          547: ppas:pl:nom:m3:perf:neg
          548: ppas:pl:nom:n:imperf:aff
          549: ppas:pl:nom:n:perf:aff
          550: ppas:pl:nom:n:perf:neg
          551: ppas:pl:voc:f:imperf:aff
          552: ppas:sg:acc:f:imperf:aff
          553: ppas:sg:acc:f:imperf:neg
          554: ppas:sg:acc:f:perf:aff
          555: ppas:sg:acc:f:perf:neg
          556: ppas:sg:acc:m1:imperf:aff
          557: ppas:sg:acc:m1:perf:aff
          558: ppas:sg:acc:m2:imperf:aff
          559: ppas:sg:acc:m2:perf:aff
          560: ppas:sg:acc:m3:imperf:aff
          561: ppas:sg:acc:m3:imperf:neg
          562: ppas:sg:acc:m3:perf:aff
          563: ppas:sg:acc:m3:perf:neg
          564: ppas:sg:acc:n:imperf:aff
          565: ppas:sg:acc:n:perf:aff
          566: ppas:sg:acc:n:perf:neg
          567: ppas:sg:dat:f:imperf:aff
          568: ppas:sg:dat:f:imperf:neg
          569: ppas:sg:dat:f:perf:aff
          570: ppas:sg:dat:f:perf:neg
          571: ppas:sg:dat:m1:imperf:aff
          572: ppas:sg:dat:m1:perf:aff
          573: ppas:sg:dat:m2:perf:aff
          574: ppas:sg:dat:m3:imperf:aff
          575: ppas:sg:dat:m3:perf:aff
          576: ppas:sg:dat:n:perf:aff
          577: ppas:sg:gen:f:imperf:aff
          578: ppas:sg:gen:f:imperf:neg
          579: ppas:sg:gen:f:perf:aff
          580: ppas:sg:gen:f:perf:neg
          581: ppas:sg:gen:m1:imperf:aff
          582: ppas:sg:gen:m1:perf:aff
          583: ppas:sg:gen:m1:perf:neg
          584: ppas:sg:gen:m2:imperf:aff
          585: ppas:sg:gen:m2:perf:aff
          586: ppas:sg:gen:m3:imperf:aff
          587: ppas:sg:gen:m3:imperf:neg
          588: ppas:sg:gen:m3:perf:aff
          589: ppas:sg:gen:m3:perf:neg
          590: ppas:sg:gen:n:imperf:aff
          591: ppas:sg:gen:n:imperf:neg
          592: ppas:sg:gen:n:perf:aff
          593: ppas:sg:gen:n:perf:neg
          594: ppas:sg:inst:f:imperf:aff
          595: ppas:sg:inst:f:imperf:neg
          596: ppas:sg:inst:f:perf:aff
          597: ppas:sg:inst:f:perf:neg
          598: ppas:sg:inst:m1:imperf:aff
          599: ppas:sg:inst:m1:imperf:neg
          600: ppas:sg:inst:m1:perf:aff
          601: ppas:sg:inst:m1:perf:neg
          602: ppas:sg:inst:m2:imperf:aff
          603: ppas:sg:inst:m2:perf:aff
          604: ppas:sg:inst:m3:imperf:aff
          605: ppas:sg:inst:m3:imperf:neg
          606: ppas:sg:inst:m3:perf:aff
          607: ppas:sg:inst:m3:perf:neg
          608: ppas:sg:inst:n:imperf:aff
          609: ppas:sg:inst:n:imperf:neg
          610: ppas:sg:inst:n:perf:aff
          611: ppas:sg:inst:n:perf:neg
          612: ppas:sg:loc:f:imperf:aff
          613: ppas:sg:loc:f:perf:aff
          614: ppas:sg:loc:f:perf:neg
          615: ppas:sg:loc:m1:imperf:aff
          616: ppas:sg:loc:m1:perf:aff
          617: ppas:sg:loc:m2:imperf:aff
          618: ppas:sg:loc:m3:imperf:aff
          619: ppas:sg:loc:m3:imperf:neg
          620: ppas:sg:loc:m3:perf:aff
          621: ppas:sg:loc:m3:perf:neg
          622: ppas:sg:loc:n:imperf:aff
          623: ppas:sg:loc:n:perf:aff
          624: ppas:sg:loc:n:perf:neg
          625: ppas:sg:nom:f:imperf:aff
          626: ppas:sg:nom:f:imperf:neg
          627: ppas:sg:nom:f:perf:aff
          628: ppas:sg:nom:f:perf:neg
          629: ppas:sg:nom:m1:imperf:aff
          630: ppas:sg:nom:m1:imperf:neg
          631: ppas:sg:nom:m1:perf:aff
          632: ppas:sg:nom:m1:perf:neg
          633: ppas:sg:nom:m2:imperf:aff
          634: ppas:sg:nom:m2:perf:aff
          635: ppas:sg:nom:m3:imperf:aff
          636: ppas:sg:nom:m3:imperf:neg
          637: ppas:sg:nom:m3:perf:aff
          638: ppas:sg:nom:m3:perf:neg
          639: ppas:sg:nom:n:imperf:aff
          640: ppas:sg:nom:n:imperf:neg
          641: ppas:sg:nom:n:perf:aff
          642: ppas:sg:nom:n:perf:neg
          643: ppas:sg:voc:m1:perf:aff
          644: ppas:sg:voc:m2:imperf:aff
          645: ppas:sg:voc:m3:perf:aff
          646: ppron12:pl:acc:f:pri
          647: ppron12:pl:acc:f:sec
          648: ppron12:pl:acc:m1:pri
          649: ppron12:pl:acc:m1:sec
          650: ppron12:pl:acc:m2:sec
          651: ppron12:pl:acc:n:sec
          652: ppron12:pl:dat:f:pri
          653: ppron12:pl:dat:f:sec
          654: ppron12:pl:dat:m1:pri
          655: ppron12:pl:dat:m1:sec
          656: ppron12:pl:dat:m3:sec
          657: ppron12:pl:gen:f:pri
          658: ppron12:pl:gen:f:sec
          659: ppron12:pl:gen:m1:pri
          660: ppron12:pl:gen:m1:sec
          661: ppron12:pl:gen:m2:pri
          662: ppron12:pl:inst:f:pri
          663: ppron12:pl:inst:m1:pri
          664: ppron12:pl:inst:m1:sec
          665: ppron12:pl:inst:n:pri
          666: ppron12:pl:loc:f:sec
          667: ppron12:pl:loc:m1:pri
          668: ppron12:pl:loc:m1:sec
          669: ppron12:pl:loc:m3:sec
          670: ppron12:pl:nom:f:pri
          671: ppron12:pl:nom:f:sec
          672: ppron12:pl:nom:m1:pri
          673: ppron12:pl:nom:m1:sec
          674: ppron12:pl:nom:m2:pri
          675: ppron12:pl:nom:n:sec
          676: ppron12:pl:voc:m1:sec
          677: ppron12:pl:voc:m2:sec
          678: ppron12:sg:acc:f:pri:akc
          679: ppron12:sg:acc:f:sec:akc
          680: ppron12:sg:acc:f:sec:nakc
          681: ppron12:sg:acc:m1:pri:akc
          682: ppron12:sg:acc:m1:pri:nakc
          683: ppron12:sg:acc:m1:sec:akc
          684: ppron12:sg:acc:m1:sec:nakc
          685: ppron12:sg:acc:m2:pri:akc
          686: ppron12:sg:acc:m2:sec:nakc
          687: ppron12:sg:acc:m3:pri:akc
          688: ppron12:sg:acc:m3:sec:nakc
          689: ppron12:sg:acc:n:pri:akc
          690: ppron12:sg:acc:n:sec:nakc
          691: ppron12:sg:dat:f:pri:akc
          692: ppron12:sg:dat:f:pri:nakc
          693: ppron12:sg:dat:f:sec:akc
          694: ppron12:sg:dat:f:sec:nakc
          695: ppron12:sg:dat:m1:pri:akc
          696: ppron12:sg:dat:m1:pri:nakc
          697: ppron12:sg:dat:m1:sec:akc
          698: ppron12:sg:dat:m1:sec:nakc
          699: ppron12:sg:dat:m2:pri:nakc
          700: ppron12:sg:dat:m2:sec:akc
          701: ppron12:sg:dat:m2:sec:nakc
          702: ppron12:sg:gen:f:pri:akc
          703: ppron12:sg:gen:f:sec:akc
          704: ppron12:sg:gen:f:sec:nakc
          705: ppron12:sg:gen:m1:pri:akc
          706: ppron12:sg:gen:m1:sec:akc
          707: ppron12:sg:gen:m1:sec:nakc
          708: ppron12:sg:gen:m2:pri:akc
          709: ppron12:sg:gen:m2:sec:akc
          710: ppron12:sg:gen:m2:sec:nakc
          711: ppron12:sg:gen:n:pri:akc
          712: ppron12:sg:inst:f:pri
          713: ppron12:sg:inst:f:sec
          714: ppron12:sg:inst:m1:pri
          715: ppron12:sg:inst:m1:pri:nakc
          716: ppron12:sg:inst:m1:sec
          717: ppron12:sg:inst:n:sec
          718: ppron12:sg:loc:f:pri
          719: ppron12:sg:loc:f:sec
          720: ppron12:sg:loc:m1:pri
          721: ppron12:sg:loc:m1:sec
          722: ppron12:sg:loc:m3:pri
          723: ppron12:sg:nom:f:pri
          724: ppron12:sg:nom:f:sec
          725: ppron12:sg:nom:m1:pri
          726: ppron12:sg:nom:m1:pri:nakc
          727: ppron12:sg:nom:m1:sec
          728: ppron12:sg:nom:m2:pri
          729: ppron12:sg:nom:m2:sec
          730: ppron12:sg:nom:m3:pri
          731: ppron12:sg:nom:m3:sec
          732: ppron12:sg:nom:n:sec
          733: ppron12:sg:voc:f:sec
          734: ppron12:sg:voc:m1:sec
          735: ppron12:sg:voc:m2:sec
          736: ppron12:sg:voc:n:sec
          737: ppron3:pl:acc:f:ter:akc:npraep
          738: ppron3:pl:acc:f:ter:akc:praep
          739: ppron3:pl:acc:m1:ter:akc:npraep
          740: ppron3:pl:acc:m1:ter:akc:praep
          741: ppron3:pl:acc:m2:ter:akc:npraep
          742: ppron3:pl:acc:m2:ter:akc:praep
          743: ppron3:pl:acc:m3:ter:akc:npraep
          744: ppron3:pl:acc:m3:ter:akc:praep
          745: ppron3:pl:acc:n:ter:akc:npraep
          746: ppron3:pl:acc:n:ter:akc:praep
          747: ppron3:pl:dat:f:ter:akc:npraep
          748: ppron3:pl:dat:f:ter:akc:praep
          749: ppron3:pl:dat:m1:ter:akc:npraep
          750: ppron3:pl:dat:m1:ter:akc:praep
          751: ppron3:pl:dat:m2:ter:akc:npraep
          752: ppron3:pl:dat:m3:ter:akc:npraep
          753: ppron3:pl:dat:m3:ter:akc:praep
          754: ppron3:pl:dat:n:ter:akc:npraep
          755: ppron3:pl:gen:f:ter:akc:npraep
          756: ppron3:pl:gen:f:ter:akc:praep
          757: ppron3:pl:gen:m1:ter:akc:npraep
          758: ppron3:pl:gen:m1:ter:akc:praep
          759: ppron3:pl:gen:m2:ter:akc:npraep
          760: ppron3:pl:gen:m2:ter:akc:praep
          761: ppron3:pl:gen:m3:ter:akc:npraep
          762: ppron3:pl:gen:m3:ter:akc:praep
          763: ppron3:pl:gen:n:ter:akc:npraep
          764: ppron3:pl:gen:n:ter:akc:praep
          765: ppron3:pl:inst:f:ter:akc:npraep
          766: ppron3:pl:inst:f:ter:akc:praep
          767: ppron3:pl:inst:m1:ter:akc:npraep
          768: ppron3:pl:inst:m1:ter:akc:praep
          769: ppron3:pl:inst:m2:ter:akc:npraep
          770: ppron3:pl:inst:m2:ter:akc:praep
          771: ppron3:pl:inst:m3:ter:akc:npraep
          772: ppron3:pl:inst:m3:ter:akc:praep
          773: ppron3:pl:inst:n:ter:akc:npraep
          774: ppron3:pl:inst:n:ter:akc:praep
          775: ppron3:pl:loc:f:ter:akc:praep
          776: ppron3:pl:loc:m1:ter:akc:praep
          777: ppron3:pl:loc:m2:ter:akc:praep
          778: ppron3:pl:loc:m3:ter:akc:praep
          779: ppron3:pl:loc:n:ter:akc:praep
          780: ppron3:pl:nom:f:ter:akc:npraep
          781: ppron3:pl:nom:f:ter:nakc:npraep
          782: ppron3:pl:nom:m1:ter:akc:npraep
          783: ppron3:pl:nom:m2:ter:akc:npraep
          784: ppron3:pl:nom:m3:ter:akc:npraep
          785: ppron3:pl:nom:n:ter:akc:npraep
          786: ppron3:sg:acc:f:ter:akc:npraep
          787: ppron3:sg:acc:f:ter:akc:praep
          788: ppron3:sg:acc:m1:ter:akc:npraep
          789: ppron3:sg:acc:m1:ter:akc:praep
          790: ppron3:sg:acc:m1:ter:nakc:npraep
          791: ppron3:sg:acc:m1:ter:nakc:praep
          792: ppron3:sg:acc:m2:ter:akc:praep
          793: ppron3:sg:acc:m2:ter:nakc:npraep
          794: ppron3:sg:acc:m2:ter:nakc:praep
          795: ppron3:sg:acc:m3:ter:akc:npraep
          796: ppron3:sg:acc:m3:ter:akc:praep
          797: ppron3:sg:acc:m3:ter:nakc:npraep
          798: ppron3:sg:acc:m3:ter:nakc:praep
          799: ppron3:sg:acc:n:ter:akc:npraep
          800: ppron3:sg:acc:n:ter:akc:praep
          801: ppron3:sg:dat:f:ter:akc:npraep
          802: ppron3:sg:dat:f:ter:akc:praep
          803: ppron3:sg:dat:m1:ter:akc:npraep
          804: ppron3:sg:dat:m1:ter:akc:praep
          805: ppron3:sg:dat:m1:ter:nakc:npraep
          806: ppron3:sg:dat:m2:ter:akc:npraep
          807: ppron3:sg:dat:m2:ter:nakc:npraep
          808: ppron3:sg:dat:m3:ter:akc:npraep
          809: ppron3:sg:dat:m3:ter:akc:praep
          810: ppron3:sg:dat:m3:ter:nakc:npraep
          811: ppron3:sg:dat:n:ter:akc:npraep
          812: ppron3:sg:dat:n:ter:akc:praep
          813: ppron3:sg:dat:n:ter:nakc:npraep
          814: ppron3:sg:gen:f:ter:akc:npraep
          815: ppron3:sg:gen:f:ter:akc:praep
          816: ppron3:sg:gen:m1:ter:akc:npraep
          817: ppron3:sg:gen:m1:ter:akc:praep
          818: ppron3:sg:gen:m1:ter:nakc:npraep
          819: ppron3:sg:gen:m1:ter:nakc:praep
          820: ppron3:sg:gen:m2:ter:akc:npraep
          821: ppron3:sg:gen:m2:ter:akc:praep
          822: ppron3:sg:gen:m2:ter:nakc:npraep
          823: ppron3:sg:gen:m3:ter:akc:npraep
          824: ppron3:sg:gen:m3:ter:akc:praep
          825: ppron3:sg:gen:m3:ter:nakc:npraep
          826: ppron3:sg:gen:m3:ter:nakc:praep
          827: ppron3:sg:gen:n:ter:akc:npraep
          828: ppron3:sg:gen:n:ter:akc:praep
          829: ppron3:sg:gen:n:ter:nakc:npraep
          830: ppron3:sg:inst:f:ter:akc:praep
          831: ppron3:sg:inst:m1:ter:akc:npraep
          832: ppron3:sg:inst:m1:ter:akc:praep
          833: ppron3:sg:inst:m2:ter:akc:npraep
          834: ppron3:sg:inst:m2:ter:akc:praep
          835: ppron3:sg:inst:m3:ter:akc:npraep
          836: ppron3:sg:inst:m3:ter:akc:praep
          837: ppron3:sg:inst:n:ter:akc:npraep
          838: ppron3:sg:inst:n:ter:akc:praep
          839: ppron3:sg:loc:f:ter:akc:praep
          840: ppron3:sg:loc:m1:ter:akc:praep
          841: ppron3:sg:loc:m2:ter:akc:praep
          842: ppron3:sg:loc:m3:ter:akc:praep
          843: ppron3:sg:loc:n:ter:akc:praep
          844: ppron3:sg:nom:f:ter:akc:npraep
          845: ppron3:sg:nom:f:ter:akc:praep
          846: ppron3:sg:nom:m1:ter:akc:npraep
          847: ppron3:sg:nom:m2:ter:akc:npraep
          848: ppron3:sg:nom:m2:ter:akc:praep
          849: ppron3:sg:nom:m3:ter:akc:npraep
          850: ppron3:sg:nom:n:ter:akc:npraep
          851: praet:pl:f:imperf
          852: praet:pl:f:perf
          853: praet:pl:m1:imperf
          854: praet:pl:m1:imperf:agl
          855: praet:pl:m1:perf
          856: praet:pl:m2:imperf
          857: praet:pl:m2:perf
          858: praet:pl:m3:imperf
          859: praet:pl:m3:perf
          860: praet:pl:n:imperf
          861: praet:pl:n:perf
          862: praet:sg:f:imperf
          863: praet:sg:f:imperf:agl
          864: praet:sg:f:imperf:nagl
          865: praet:sg:f:perf
          866: praet:sg:m1:imperf
          867: praet:sg:m1:imperf:agl
          868: praet:sg:m1:imperf:nagl
          869: praet:sg:m1:perf
          870: praet:sg:m1:perf:agl
          871: praet:sg:m1:perf:nagl
          872: praet:sg:m2:imperf
          873: praet:sg:m2:imperf:nagl
          874: praet:sg:m2:perf
          875: praet:sg:m2:perf:nagl
          876: praet:sg:m3:imperf
          877: praet:sg:m3:imperf:nagl
          878: praet:sg:m3:perf
          879: praet:sg:m3:perf:nagl
          880: praet:sg:n:imperf
          881: praet:sg:n:perf
          882: pred
          883: prep:acc
          884: prep:acc:nwok
          885: prep:acc:wok
          886: prep:dat
          887: prep:gen
          888: prep:gen:nwok
          889: prep:gen:wok
          890: prep:inst
          891: prep:inst:nwok
          892: prep:inst:wok
          893: prep:loc
          894: prep:loc:nwok
          895: prep:loc:wok
          896: prep:nom
          897: romandig
          898: siebie:acc
          899: siebie:dat
          900: siebie:gen
          901: siebie:inst
          902: siebie:loc
          903: subst:pl:acc:f
          904: subst:pl:acc:m1
          905: subst:pl:acc:m1:pt
          906: subst:pl:acc:m2
          907: subst:pl:acc:m3
          908: subst:pl:acc:n:col
          909: subst:pl:acc:n:ncol
          910: subst:pl:acc:n:pt
          911: subst:pl:dat:f
          912: subst:pl:dat:m1
          913: subst:pl:dat:m1:pt
          914: subst:pl:dat:m2
          915: subst:pl:dat:m3
          916: subst:pl:dat:n:col
          917: subst:pl:dat:n:ncol
          918: subst:pl:dat:n:pt
          919: subst:pl:gen:f
          920: subst:pl:gen:m1
          921: subst:pl:gen:m1:pt
          922: subst:pl:gen:m2
          923: subst:pl:gen:m3
          924: subst:pl:gen:n:col
          925: subst:pl:gen:n:ncol
          926: subst:pl:gen:n:pt
          927: subst:pl:inst:f
          928: subst:pl:inst:m1
          929: subst:pl:inst:m1:pt
          930: subst:pl:inst:m2
          931: subst:pl:inst:m3
          932: subst:pl:inst:n:col
          933: subst:pl:inst:n:ncol
          934: subst:pl:inst:n:pt
          935: subst:pl:loc:f
          936: subst:pl:loc:m1
          937: subst:pl:loc:m1:pt
          938: subst:pl:loc:m2
          939: subst:pl:loc:m3
          940: subst:pl:loc:n:col
          941: subst:pl:loc:n:ncol
          942: subst:pl:loc:n:pt
          943: subst:pl:nom:f
          944: subst:pl:nom:m1
          945: subst:pl:nom:m1:pt
          946: subst:pl:nom:m2
          947: subst:pl:nom:m3
          948: subst:pl:nom:n:col
          949: subst:pl:nom:n:ncol
          950: subst:pl:nom:n:pt
          951: subst:pl:voc:f
          952: subst:pl:voc:m1
          953: subst:pl:voc:m1:pt
          954: subst:pl:voc:m3
          955: subst:pl:voc:n:col
          956: subst:pl:voc:n:ncol
          957: subst:pl:voc:n:pt
          958: subst:sg:acc:f
          959: subst:sg:acc:m1
          960: subst:sg:acc:m2
          961: subst:sg:acc:m3
          962: subst:sg:acc:n:col
          963: subst:sg:acc:n:ncol
          964: subst:sg:dat:f
          965: subst:sg:dat:m1
          966: subst:sg:dat:m2
          967: subst:sg:dat:m3
          968: subst:sg:dat:n:col
          969: subst:sg:dat:n:ncol
          970: subst:sg:gen:f
          971: subst:sg:gen:m1
          972: subst:sg:gen:m2
          973: subst:sg:gen:m3
          974: subst:sg:gen:n:col
          975: subst:sg:gen:n:ncol
          976: subst:sg:inst:f
          977: subst:sg:inst:m1
          978: subst:sg:inst:m2
          979: subst:sg:inst:m3
          980: subst:sg:inst:n:col
          981: subst:sg:inst:n:ncol
          982: subst:sg:loc:f
          983: subst:sg:loc:m1
          984: subst:sg:loc:m2
          985: subst:sg:loc:m3
          986: subst:sg:loc:n:col
          987: subst:sg:loc:n:ncol
          988: subst:sg:nom:f
          989: subst:sg:nom:m1
          990: subst:sg:nom:m2
          991: subst:sg:nom:m3
          992: subst:sg:nom:n:col
          993: subst:sg:nom:n:ncol
          994: subst:sg:voc:f
          995: subst:sg:voc:m1
          996: subst:sg:voc:m2
          997: subst:sg:voc:m3
          998: subst:sg:voc:n:col
          999: subst:sg:voc:n:ncol
          1000: sym
          1001: winien:pl:f:imperf
          1002: winien:pl:m1:imperf
          1003: winien:pl:m2:imperf
          1004: winien:pl:m3:imperf
          1005: winien:pl:n:imperf
          1006: winien:sg:f:imperf
          1007: winien:sg:m1:imperf
          1008: winien:sg:m2:imperf
          1009: winien:sg:m3:imperf
          1010: winien:sg:n:imperf
          1011: xxs:acc
          1012: xxs:dat
          1013: xxs:gen
          1014: xxs:inst
          1015: xxs:loc
          1016: xxs:nom
          1017: xxs:voc
          1018: xxx
  - name: nps
    sequence: bool
  - name: nkjp_ids
    sequence: string
  config_name: nkjp1m
  splits:
  - name: test
    num_bytes: 8324533
    num_examples: 8964
  - name: train
    num_bytes: 65022406
    num_examples: 68943
  - name: validation
    num_bytes: 7465442
    num_examples: 7755
  download_size: 16167009
  dataset_size: 80812381
---
# Dataset Card for NKJP1M – The manually annotated subcorpus of the National Corpus of Polish

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Homepage:** [NKJP1M](http://clip.ipipan.waw.pl/NationalCorpusOfPolish)
- **Repository:** [NKJP1M-SGJP](http://download.sgjp.pl/morfeusz/current/)
- **Paper:** [NKJP book](http://nkjp.pl/settings/papers/NKJP_ksiazka.pdf)
- **Point of Contact:** mailto:morfeusz@ipipan.waw.pl

### Dataset Summary

This is the official dataset for NKJP1M – the 1-million token balanced subcorpus of the National Corpus of Polish (Narodowy Korpus Języka Polskiego)

Besides the text (divided into paragraphs/samples and sentences) the set contains lemmas and morpho-syntactic tags for all tokens in the corpus.

This release, known as NKJP1M-SGJP, corresponds to the version 1.2 of the corpus with later corrections and improvements. In particular the morpho-syntactic annotation has been aligned with the present version of Morfeusz2 SGJP morphological analyser (as of 2022.12.04).

### Supported Tasks and Leaderboards

The main use of this resource lays in training models for lemmatisation and part of speech tagging of Polish.

### Languages

Polish (monolingual)

## Dataset Structure

### Data Instances

```
{'nkjp_text': 'NKJP_1M_1102000002',
 'nkjp_par': 'morph_1-p',
 'nkjp_sent': 'morph_1.18-s',
 'tokens': ['-', 'Nie', 'mam', 'pieniędzy', ',', 'da', 'mi', 'pani', 'wywiad', '?'],
 'lemmas': ['-', 'nie', 'mieć', 'pieniądz', ',', 'dać', 'ja', 'pani', 'wywiad', '?'],
 'cposes': [8, 11, 10, 9, 8, 10, 9, 9, 9, 8],
 'poses': [19, 25, 12, 35, 19, 12, 28, 35, 35, 19],
 'tags': [266, 464, 213, 923, 266, 218, 692, 988, 961, 266],
 'nps': [False, False, False, False, True, False, False, False, False, True],
 'nkjp_ids': ['morph_1.9-seg', 'morph_1.10-seg', 'morph_1.11-seg', 'morph_1.12-seg', 'morph_1.13-seg', 'morph_1.14-seg', 'morph_1.15-seg', 'morph_1.16-seg', 'morph_1.17-seg', 'morph_1.18-seg']}
```

### Data Fields

- `nkjp_text`, `nkjp_par`, `nkjp_sent` (strings): XML identifiers of the present text (document), paragraph and sentence in NKJP. (These allow to map the data point back to the source corpus and to identify paragraphs/samples.)
- `tokens` (sequence of strings): tokens of the text defined as in NKJP.
- `lemmas` (sequence of strings): lemmas corresponding to the tokens.
- `tags` (sequence of labels): morpho-syntactic tags according to Morfeusz2 tagset (1019 distinct tags).
- `poses` (sequence of labels): flexemic class (detailed part of speech, 40 classes) – the first element of the corresponding tag.
- `cposes` (sequence of labels): coarse part of speech (13 classes): all verbal and deverbal flexemic classes get mapped to a `V`, nominal – `N`, adjectival – `A`, “strange” (abbreviations, alien elements, symbols, emojis…)  – `X`, rest as in `poses`.
- `nps` (sequence of booleans): `True` means that the corresponding token is not preceded by a space in the source text.
- `nkjp_ids` (sequence of strings): XML identifiers of particular tokens in NKJP (probably an overkill).

### Data Splits

|           | Train  | Validation | Test   |
| -----     | ------ | -----      | ----   |
| sentences | 68943  | 7755       |  8964  |
| tokens    | 978368 | 112454     | 125059 |

## Dataset Creation

### Curation Rationale

The National Corpus of Polish (NKJP) was envisioned as the reference corpus of contemporary Polish.

The manually annotated subcorpus (NKJP1M) was thought of as the training data for various NLP tasks.

### Source Data

NKJP is balanced with respect to Polish readership.  The detailed rationale is described in Chapter 3 of the [NKJP book](http://nkjp.pl/settings/papers/NKJP_ksiazka.pdf) (roughly: 50% press, 30% books, 10% speech, 10% other).  The corpus contains texts from the years 1945–2010 (with 80% of the text in the range 1990–2010).  Only original Polish texts were gathered (no translations from other languages). The composition of NKJP1M follows this schema (see Chapter 5).

### Annotations

The rules of morphosyntactic annotation used for NKJP are discussed in Chapter 6 of the [NKJP book](http://nkjp.pl/settings/papers/NKJP_ksiazka.pdf).  Presently (2020), the corpus uses a common tagset with the morphological analyzer [Morfeusz 2](http://morfeusz.sgjp.pl/).

#### Annotation process

The texts were processed with Morfeusz and then the resulting annotations were manually disambiguated and validated/corrected. Each text sample was independently processed by two annotators. In case of annotation conflicts an adjudicator stepped in.

### Licensing Information

![Creative Commons License](https://i.creativecommons.org/l/by/4.0/80x15.png) This work is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).

### Citation Information

Info on the source corpus: [link](http://nkjp.pl/settings/papers/NKJP_ksiazka.pdf)

```
@Book{nkjp:12,
  editor =       "Adam Przepiórkowski and Mirosław Bańko and Rafał
                  L. Górski and Barbara Lewandowska-Tomaszczyk",
  title =        "Narodowy Korpus Języka Polskiego",
  year =         2012,
  address =      "Warszawa",
  pdf =          "http://nkjp.pl/settings/papers/NKJP_ksiazka.pdf",
  publisher =    "Wydawnictwo Naukowe PWN"}
```

Current annotation scheme: [link](https://jezyk-polski.pl/index.php/jp/article/view/72)

```
@article{
    kie:etal:21,
    author = "Kieraś, Witold and Woliński, Marcin and Nitoń, Bartłomiej",
    doi = "https://doi.org/10.31286/JP.101.2.5",
    title = "Nowe wielowarstwowe znakowanie lingwistyczne zrównoważonego {N}arodowego {K}orpusu {J}ęzyka {P}olskiego",
    url = "https://jezyk-polski.pl/index.php/jp/article/view/72",
    journal = "Język Polski",
    number = "2",
    volume = "CI",
    year = "2021",
    pages = "59--70"
}
```

<!--
### Contributions

Thanks to [@github-username](https://github.com/<github-username>) for adding this dataset.
-->