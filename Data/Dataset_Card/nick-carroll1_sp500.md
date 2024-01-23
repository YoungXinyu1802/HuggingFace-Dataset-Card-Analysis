
# Dataset Card for S&P 500 Dataset

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

- **Homepage:**
- **Repository:**
- **Paper:**
- **Leaderboard:**
- **Point of Contact:**

This Dataset was created by combining the daily close prices for each stock in the current (as of 10/29/2022) S&P 500 index dating back to January 1, 1970.  This data came from the Kaggle dataset (https://www.kaggle.com/datasets/paultimothymooney/stock-market-data) and was aggregated using PANDAS before being converted to a HuggingFace Dataset.

### Dataset Summary

This dataset has 407 columns specifying dates and associated close prices of the stocks in the S&P 500 that had data which could be accessed from the above Kaggle dataset. 94 stocks are missing due to issues loading that stock data into the dataset (i.e. stock name changes (like FB to META)).  These items will need further review.   There are many NA values due to stocks that were not in existence as early as 1970.

### Supported Tasks and Leaderboards

[More Information Needed]


## Dataset Structure

### Data Instances

[More Information Needed]

### Data Fields

[More Information Needed]

### Data Splits

No split has currently been created for the dataset.

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

https://www.kaggle.com/datasets/paultimothymooney/stock-market-data

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

[More Information Needed]

### Licensing Information

[More Information Needed]

### Citation Information

[More Information Needed]

### Contributions

Thanks to [@github-username](https://github.com/nick-carroll1) for adding this dataset.

---
dataset_info:
  features:
  - name: MMM
    dtype: float64
  - name: AOS
    dtype: float64
  - name: ABT
    dtype: float64
  - name: ABBV
    dtype: float64
  - name: ABMD
    dtype: float64
  - name: ACN
    dtype: float64
  - name: ATVI
    dtype: float64
  - name: ADM
    dtype: float64
  - name: ADBE
    dtype: float64
  - name: ADP
    dtype: float64
  - name: AAP
    dtype: float64
  - name: A
    dtype: float64
  - name: APD
    dtype: float64
  - name: AKAM
    dtype: float64
  - name: ALK
    dtype: float64
  - name: ALB
    dtype: float64
  - name: ARE
    dtype: float64
  - name: ALGN
    dtype: float64
  - name: ALLE
    dtype: float64
  - name: LNT
    dtype: float64
  - name: GOOG
    dtype: float64
  - name: MO
    dtype: float64
  - name: AMZN
    dtype: float64
  - name: AMD
    dtype: float64
  - name: AEE
    dtype: float64
  - name: AAL
    dtype: float64
  - name: AEP
    dtype: float64
  - name: AXP
    dtype: float64
  - name: AIG
    dtype: float64
  - name: AMT
    dtype: float64
  - name: AWK
    dtype: float64
  - name: AMP
    dtype: float64
  - name: ABC
    dtype: float64
  - name: AME
    dtype: float64
  - name: AMGN
    dtype: float64
  - name: APH
    dtype: float64
  - name: ADI
    dtype: float64
  - name: AON
    dtype: float64
  - name: APA
    dtype: float64
  - name: AAPL
    dtype: float64
  - name: AMAT
    dtype: float64
  - name: ANET
    dtype: float64
  - name: AJG
    dtype: float64
  - name: AIZ
    dtype: float64
  - name: T
    dtype: float64
  - name: ATO
    dtype: float64
  - name: ADSK
    dtype: float64
  - name: AZO
    dtype: float64
  - name: AVB
    dtype: float64
  - name: AVY
    dtype: float64
  - name: BAC
    dtype: float64
  - name: BAX
    dtype: float64
  - name: BDX
    dtype: float64
  - name: WRB
    dtype: float64
  - name: BBY
    dtype: float64
  - name: BIO
    dtype: float64
  - name: BIIB
    dtype: float64
  - name: BLK
    dtype: float64
  - name: BK
    dtype: float64
  - name: BA
    dtype: float64
  - name: BWA
    dtype: float64
  - name: BXP
    dtype: float64
  - name: BSX
    dtype: float64
  - name: BMY
    dtype: float64
  - name: AVGO
    dtype: float64
  - name: BR
    dtype: float64
  - name: BRO
    dtype: float64
  - name: CHRW
    dtype: float64
  - name: CDNS
    dtype: float64
  - name: CZR
    dtype: float64
  - name: CPT
    dtype: float64
  - name: CPB
    dtype: float64
  - name: COF
    dtype: float64
  - name: CAH
    dtype: float64
  - name: KMX
    dtype: float64
  - name: CAT
    dtype: float64
  - name: CBOE
    dtype: float64
  - name: CDW
    dtype: float64
  - name: CNC
    dtype: float64
  - name: CNP
    dtype: float64
  - name: CF
    dtype: float64
  - name: CRL
    dtype: float64
  - name: SCHW
    dtype: float64
  - name: CHTR
    dtype: float64
  - name: CMG
    dtype: float64
  - name: CB
    dtype: float64
  - name: CHD
    dtype: float64
  - name: CINF
    dtype: float64
  - name: CTAS
    dtype: float64
  - name: CSCO
    dtype: float64
  - name: C
    dtype: float64
  - name: CFG
    dtype: float64
  - name: CLX
    dtype: float64
  - name: CME
    dtype: float64
  - name: CMS
    dtype: float64
  - name: KO
    dtype: float64
  - name: CTSH
    dtype: float64
  - name: CL
    dtype: float64
  - name: CMCSA
    dtype: float64
  - name: CAG
    dtype: float64
  - name: COP
    dtype: float64
  - name: ED
    dtype: float64
  - name: COO
    dtype: float64
  - name: CPRT
    dtype: float64
  - name: GLW
    dtype: float64
  - name: CSGP
    dtype: float64
  - name: COST
    dtype: float64
  - name: CCI
    dtype: float64
  - name: CMI
    dtype: float64
  - name: DHI
    dtype: float64
  - name: DRI
    dtype: float64
  - name: DVA
    dtype: float64
  - name: DE
    dtype: float64
  - name: DAL
    dtype: float64
  - name: DVN
    dtype: float64
  - name: DXCM
    dtype: float64
  - name: FANG
    dtype: float64
  - name: DLR
    dtype: float64
  - name: DFS
    dtype: float64
  - name: DISH
    dtype: float64
  - name: DIS
    dtype: float64
  - name: DG
    dtype: float64
  - name: DLTR
    dtype: float64
  - name: D
    dtype: float64
  - name: DPZ
    dtype: float64
  - name: DOV
    dtype: float64
  - name: DOW
    dtype: float64
  - name: DTE
    dtype: float64
  - name: DD
    dtype: float64
  - name: EMN
    dtype: float64
  - name: ETN
    dtype: float64
  - name: EBAY
    dtype: float64
  - name: ECL
    dtype: float64
  - name: EIX
    dtype: float64
  - name: EW
    dtype: float64
  - name: EA
    dtype: float64
  - name: LLY
    dtype: float64
  - name: EMR
    dtype: float64
  - name: ENPH
    dtype: float64
  - name: EOG
    dtype: float64
  - name: EPAM
    dtype: float64
  - name: EFX
    dtype: float64
  - name: EQIX
    dtype: float64
  - name: EQR
    dtype: float64
  - name: ESS
    dtype: float64
  - name: EL
    dtype: float64
  - name: RE
    dtype: float64
  - name: ES
    dtype: float64
  - name: EXC
    dtype: float64
  - name: EXPE
    dtype: float64
  - name: EXPD
    dtype: float64
  - name: EXR
    dtype: float64
  - name: XOM
    dtype: float64
  - name: FFIV
    dtype: float64
  - name: FDS
    dtype: float64
  - name: FAST
    dtype: float64
  - name: FRT
    dtype: float64
  - name: FDX
    dtype: float64
  - name: FITB
    dtype: float64
  - name: FRC
    dtype: float64
  - name: FE
    dtype: float64
  - name: FIS
    dtype: float64
  - name: FISV
    dtype: float64
  - name: FLT
    dtype: float64
  - name: FMC
    dtype: float64
  - name: F
    dtype: float64
  - name: FTNT
    dtype: float64
  - name: FBHS
    dtype: float64
  - name: FOXA
    dtype: float64
  - name: BEN
    dtype: float64
  - name: FCX
    dtype: float64
  - name: GRMN
    dtype: float64
  - name: IT
    dtype: float64
  - name: GNRC
    dtype: float64
  - name: GD
    dtype: float64
  - name: GE
    dtype: float64
  - name: GIS
    dtype: float64
  - name: GM
    dtype: float64
  - name: GPC
    dtype: float64
  - name: GILD
    dtype: float64
  - name: GPN
    dtype: float64
  - name: HAL
    dtype: float64
  - name: HIG
    dtype: float64
  - name: HAS
    dtype: float64
  - name: HCA
    dtype: float64
  - name: HSIC
    dtype: float64
  - name: HSY
    dtype: float64
  - name: HES
    dtype: float64
  - name: HPE
    dtype: float64
  - name: HLT
    dtype: float64
  - name: HOLX
    dtype: float64
  - name: HD
    dtype: float64
  - name: HON
    dtype: float64
  - name: HRL
    dtype: float64
  - name: HST
    dtype: float64
  - name: HPQ
    dtype: float64
  - name: HUM
    dtype: float64
  - name: HBAN
    dtype: float64
  - name: HII
    dtype: float64
  - name: IBM
    dtype: float64
  - name: IEX
    dtype: float64
  - name: IDXX
    dtype: float64
  - name: ITW
    dtype: float64
  - name: ILMN
    dtype: float64
  - name: INCY
    dtype: float64
  - name: IR
    dtype: float64
  - name: INTC
    dtype: float64
  - name: ICE
    dtype: float64
  - name: IP
    dtype: float64
  - name: IPG
    dtype: float64
  - name: IFF
    dtype: float64
  - name: INTU
    dtype: float64
  - name: ISRG
    dtype: float64
  - name: IVZ
    dtype: float64
  - name: IRM
    dtype: float64
  - name: JBHT
    dtype: float64
  - name: JKHY
    dtype: float64
  - name: JNJ
    dtype: float64
  - name: JCI
    dtype: float64
  - name: JPM
    dtype: float64
  - name: JNPR
    dtype: float64
  - name: K
    dtype: float64
  - name: KEY
    dtype: float64
  - name: KEYS
    dtype: float64
  - name: KMB
    dtype: float64
  - name: KIM
    dtype: float64
  - name: KLAC
    dtype: float64
  - name: KHC
    dtype: float64
  - name: KR
    dtype: float64
  - name: LH
    dtype: float64
  - name: LRCX
    dtype: float64
  - name: LVS
    dtype: float64
  - name: LDOS
    dtype: float64
  - name: LNC
    dtype: float64
  - name: LYV
    dtype: float64
  - name: LKQ
    dtype: float64
  - name: LMT
    dtype: float64
  - name: LOW
    dtype: float64
  - name: LYB
    dtype: float64
  - name: MRO
    dtype: float64
  - name: MPC
    dtype: float64
  - name: MKTX
    dtype: float64
  - name: MAR
    dtype: float64
  - name: MMC
    dtype: float64
  - name: MLM
    dtype: float64
  - name: MA
    dtype: float64
  - name: MKC
    dtype: float64
  - name: MCD
    dtype: float64
  - name: MCK
    dtype: float64
  - name: MDT
    dtype: float64
  - name: MRK
    dtype: float64
  - name: MET
    dtype: float64
  - name: MTD
    dtype: float64
  - name: MGM
    dtype: float64
  - name: MCHP
    dtype: float64
  - name: MU
    dtype: float64
  - name: MSFT
    dtype: float64
  - name: MAA
    dtype: float64
  - name: MHK
    dtype: float64
  - name: MOH
    dtype: float64
  - name: TAP
    dtype: float64
  - name: MDLZ
    dtype: float64
  - name: MPWR
    dtype: float64
  - name: MNST
    dtype: float64
  - name: MCO
    dtype: float64
  - name: MOS
    dtype: float64
  - name: MSI
    dtype: float64
  - name: MSCI
    dtype: float64
  - name: NDAQ
    dtype: float64
  - name: NTAP
    dtype: float64
  - name: NFLX
    dtype: float64
  - name: NWL
    dtype: float64
  - name: NEM
    dtype: float64
  - name: NWSA
    dtype: float64
  - name: NEE
    dtype: float64
  - name: NI
    dtype: float64
  - name: NDSN
    dtype: float64
  - name: NSC
    dtype: float64
  - name: NTRS
    dtype: float64
  - name: NOC
    dtype: float64
  - name: NCLH
    dtype: float64
  - name: NRG
    dtype: float64
  - name: NVDA
    dtype: float64
  - name: NVR
    dtype: float64
  - name: NXPI
    dtype: float64
  - name: ORLY
    dtype: float64
  - name: OXY
    dtype: float64
  - name: ODFL
    dtype: float64
  - name: OMC
    dtype: float64
  - name: OKE
    dtype: float64
  - name: PCAR
    dtype: float64
  - name: PKG
    dtype: float64
  - name: PH
    dtype: float64
  - name: PAYX
    dtype: float64
  - name: PAYC
    dtype: float64
  - name: PNR
    dtype: float64
  - name: PEP
    dtype: float64
  - name: PKI
    dtype: float64
  - name: PFE
    dtype: float64
  - name: PM
    dtype: float64
  - name: PSX
    dtype: float64
  - name: PNW
    dtype: float64
  - name: PXD
    dtype: float64
  - name: PNC
    dtype: float64
  - name: POOL
    dtype: float64
  - name: PPG
    dtype: float64
  - name: PFG
    dtype: float64
  - name: PG
    dtype: float64
  - name: PLD
    dtype: float64
  - name: PRU
    dtype: float64
  - name: PEG
    dtype: float64
  - name: PTC
    dtype: float64
  - name: PHM
    dtype: float64
  - name: QRVO
    dtype: float64
  - name: PWR
    dtype: float64
  - name: QCOM
    dtype: float64
  - name: DGX
    dtype: float64
  - name: RL
    dtype: float64
  - name: RJF
    dtype: float64
  - name: O
    dtype: float64
  - name: REG
    dtype: float64
  - name: REGN
    dtype: float64
  - name: RF
    dtype: float64
  - name: RSG
    dtype: float64
  - name: RMD
    dtype: float64
  - name: RHI
    dtype: float64
  - name: ROK
    dtype: float64
  - name: ROL
    dtype: float64
  - name: ROP
    dtype: float64
  - name: ROST
    dtype: float64
  - name: RCL
    dtype: float64
  - name: CRM
    dtype: float64
  - name: SBAC
    dtype: float64
  - name: SLB
    dtype: float64
  - name: STX
    dtype: float64
  - name: SEE
    dtype: float64
  - name: SRE
    dtype: float64
  - name: NOW
    dtype: float64
  - name: SHW
    dtype: float64
  - name: SBNY
    dtype: float64
  - name: SPG
    dtype: float64
  - name: SWKS
    dtype: float64
  - name: SO
    dtype: float64
  - name: LUV
    dtype: float64
  - name: SWK
    dtype: float64
  - name: SBUX
    dtype: float64
  - name: STT
    dtype: float64
  - name: SYK
    dtype: float64
  - name: SIVB
    dtype: float64
  - name: SYF
    dtype: float64
  - name: SNPS
    dtype: float64
  - name: TMUS
    dtype: float64
  - name: TROW
    dtype: float64
  - name: TTWO
    dtype: float64
  - name: TRGP
    dtype: float64
  - name: TEL
    dtype: float64
  - name: TDY
    dtype: float64
  - name: TSLA
    dtype: float64
  - name: TXN
    dtype: float64
  - name: TXT
    dtype: float64
  - name: TMO
    dtype: float64
  - name: TJX
    dtype: float64
  - name: TSCO
    dtype: float64
  - name: TDG
    dtype: float64
  - name: TRV
    dtype: float64
  - name: TYL
    dtype: float64
  - name: TSN
    dtype: float64
  - name: USB
    dtype: float64
  - name: UDR
    dtype: float64
  - name: ULTA
    dtype: float64
  - name: UNP
    dtype: float64
  - name: UAL
    dtype: float64
  - name: UPS
    dtype: float64
  - name: URI
    dtype: float64
  - name: UNH
    dtype: float64
  - name: UHS
    dtype: float64
  - name: VTR
    dtype: float64
  - name: VRSN
    dtype: float64
  - name: VRSK
    dtype: float64
  - name: VZ
    dtype: float64
  - name: VRTX
    dtype: float64
  - name: VFC
    dtype: float64
  - name: V
    dtype: float64
  - name: VMC
    dtype: float64
  - name: WAB
    dtype: float64
  - name: WBA
    dtype: float64
  - name: WMT
    dtype: float64
  - name: WM
    dtype: float64
  - name: WAT
    dtype: float64
  - name: WEC
    dtype: float64
  - name: WFC
    dtype: float64
  - name: WST
    dtype: float64
  - name: WDC
    dtype: float64
  - name: WRK
    dtype: float64
  - name: WY
    dtype: float64
  - name: WHR
    dtype: float64
  - name: WMB
    dtype: float64
  - name: WTW
    dtype: float64
  - name: GWW
    dtype: float64
  - name: WYNN
    dtype: float64
  - name: XEL
    dtype: float64
  - name: XYL
    dtype: float64
  - name: YUM
    dtype: float64
  - name: ZBRA
    dtype: float64
  - name: ZBH
    dtype: float64
  - name: ZION
    dtype: float64
  - name: ZTS
    dtype: float64
  - name: Date
    dtype: timestamp[ns]
  splits:
  - name: train
    num_bytes: 44121086
    num_examples: 13322
  download_size: 0
  dataset_size: 44121086
---
# Dataset Card for "sp500"

[More Information needed](https://github.com/huggingface/datasets/blob/main/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)