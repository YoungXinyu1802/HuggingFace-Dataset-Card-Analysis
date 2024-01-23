---
annotations_creators:
- no-annotation
language_creators:
- found
language:
- en
license:
- cc-by-nc-sa-4.0
multilinguality:
- monolingual
pretty_name: pile-of-law
size_categories:
- 10M<n<100M
source_datasets: []
task_categories:
- fill-mask
task_ids:
- masked-language-modeling
viewer: false
---

# Dataset Card for Pile of Law

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

- **Homepage:** https://huggingface.co/datasets/pile-of-law/pile-of-law
- **Repository:** https://huggingface.co/datasets/pile-of-law/pile-of-law
- **Paper:** https://arxiv.org/abs/2207.00220

### Dataset Summary

We curate a large corpus of legal and administrative data. The utility of this data is twofold: (1) to aggregate legal and administrative data sources that demonstrate different norms and legal standards for data filtering; (2) to collect a dataset that can be used in the future for pretraining legal-domain language models, a key direction in access-to-justice initiatives.

### Supported Tasks and Leaderboards

See paper for details.

### Languages

Mainly English, but some other languages may appear in some portions of the data.

## Dataset Structure

### Data Instances

**courtListener_docket_entry_documents** : Docket entries in U.S. federal courts, including filed briefs from CourtListener RECAP archive.

**courtListener_opinions** : U.S. court opinions from CourtListener (synchronized as of 12/31/2022).

**atticus_contracts**: Unannotated contracts from the Atticus Project.

**federal_register**: The U.S. federal register where agencies file draft rulemaking.

**bva_opinions**: Bureau of Veterans Appeals opinions.

**us_bills**: Draft Bills from the United States Congress.

**cc_casebooks**: Educational Casebooks released under open CC licenses.

**tos**: Unannotated Terms of Service contracts.

**euro_parl**: European parliamentary debates.

**nlrb_decisions**: Decisions from the U.S. National Labor Review Board.

**scotus_oral_arguments**: U.S. Supreme Court Oral Arguments

**cfr**: U.S. Code of Federal Regulations

**state_codes**: U.S. State Codes

**scotus_filings**: Briefs and filings with the U.S. Supreme Court.

**exam_outlines**: Exam outlines available openly on the web.

**edgar**: Contracts filed with the SEC and made available on the SEC's Edgar tool.

**cfpb_creditcard_contracts**: Credit Card Contracts compiled by the U.S. Consumer Finance Protection Bureau.

**constitutions** : The World's constitutions.

**congressional_hearings** : U.S. Congressional hearing transcripts and statements.

**oig**: U.S. Office of Inspector general reports.

**olc_memos**: U.S. Office of Legal Counsel memos.

**uscode**: The United States Code (laws).

**founding_docs**: Letters from U.S. founders.

**ftc_advisory_opinions**: Advisory opinions by the Federal Trade Commission.

**echr** : European Court of Human Rights opinions.

**eurlex**: European Laws.

**tax_rulings**: Rulings from U.S. Tax court.

**un_debates**: U.N. General Debates

**fre**: U.S. Federal Rules of Evidence

**frcp** : U.S. Federal Rules of Civil Procedure

**canadian_decisions**: Canadian Court Opinions from ON and BC.

**eoir**: U.S. Executive Office for Immigration Review Immigration and Nationality Precedential Decisions

**dol_ecab**: Department of Labor Employees' Compensation Appeals Board decisions after 2006

**r_legaladvice** : Filtered data from the r/legaladvice and r/legaladviceofftopic subreddits in the format. 
Title: [Post Title]
Question: [Post Content]
Topic: [Post Flair]
Answer \#[N]: [Top Answers]...

**acus_reports** : Reports from the Administrative Conference of the United States from 2010-2022.

**ed_policy_guidance** : Policy guidance documents from the U.S. Department of Education (2001-2022).

**uspto_office_actions** : Office Actions from the U.S. Patent and Trademark Office from 2019-2022.

**icj-pcij** : International Court of Justice and Permanent Court of International Justice opinions.

**hhs_alj_opinions** : Opinions from the U.S. Department of Health and Human Services Administrative Law Judges from 1985-2019.

**sec_administrative_proceedings**: Significant pleadings, orders and decisions for administrative proceedings from the U.S. Securities and Exchange Commission from 2005-2022.

**fmshrc_bluebooks**: Bluebooks from the U.S. Federal Mine Safety and Health Review Commission from 1979 (March) - 2022 (August).

**resource_contracts**: Resource Contracts collected by ResourceContracts.org

**medicaid_policy_guidance**: Policy guidance documents from the U.S. Department of Health and Human Services (1994-2022).

**irs_legal_advice_memos**: Legal Advice Memos and Chief Counsel Notices from the U.S. Internal Revenue Service.

**doj_guidance**: Guidance documents from the U.S. Department of Justice (2020-2022).

**1/23 update**: Data updated in 2023 included: syncing courtListener opinions, adding ACUS reports, USPTO office actions, Ed Policy Guidance, HHS ALJ opinions, SEC administrative proceedings, FMSHRC Bluebooks, Resource Contracts, and ICJ/PCIJ legal opinions. We also fixed OLC opinions which had some formatting inconsistencies and merged exam outlines into one file, adding some additional exam outlines.

On-disk sizes might vary due to caching and compression, but should be approximately as follows as of 1/7/2023. 


```bash
 % xz --list data/*.xz                      
Strms  Blocks   Compressed Uncompressed  Ratio  Check   Filename
  183     181  9,631.2 KiB     35.0 MiB  0.268  CRC64   data/train.acus_reports.jsonl.xz
    1       1  1,024.1 MiB  6,804.7 MiB  0.150  CRC64   data/train.atticus_contracts.0.jsonl.xz
    1       1  1,024.1 MiB  6,781.1 MiB  0.151  CRC64   data/train.atticus_contracts.1.jsonl.xz
    1       1  1,024.1 MiB  6,790.1 MiB  0.151  CRC64   data/train.atticus_contracts.2.jsonl.xz
    1       1  1,024.1 MiB  6,759.2 MiB  0.152  CRC64   data/train.atticus_contracts.3.jsonl.xz
    1       1    139.9 MiB    925.0 MiB  0.151  CRC64   data/train.atticus_contracts.4.jsonl.xz
    1       1  1,564.6 MiB     12.5 GiB  0.123  CRC64   data/train.bva.jsonl.xz
    1       1     29.8 MiB    154.3 MiB  0.193  CRC64   data/train.canadian_decisions.jsonl.xz
    1       1     18.5 MiB     82.6 MiB  0.224  CRC64   data/train.cc_casebooks.jsonl.xz
    1       1  3,427.3 KiB     67.2 MiB  0.050  CRC64   data/train.cfpb_cc.jsonl.xz
    1       1     72.7 MiB    582.6 MiB  0.125  CRC64   data/train.cfr.jsonl.xz
    1       1  1,056.1 MiB  4,941.9 MiB  0.214  CRC64   data/train.congressional_hearings.jsonl.xz
    1       1  3,272.4 KiB     21.3 MiB  0.150  CRC64   data/train.constitutions.jsonl.xz
    1       1  1,024.1 MiB     13.0 GiB  0.077  CRC64   data/train.courtlistenerdocketentries.0.jsonl.xz
    1       1  1,024.3 MiB     13.3 GiB  0.075  CRC64   data/train.courtlistenerdocketentries.1.jsonl.xz
    1       1  1,024.1 MiB     12.4 GiB  0.080  CRC64   data/train.courtlistenerdocketentries.2.jsonl.xz
    1       1    635.2 MiB  8,671.6 MiB  0.073  CRC64   data/train.courtlistenerdocketentries.3.jsonl.xz
    1       1    953.7 MiB  4,575.7 MiB  0.208  CRC64   data/train.courtlisteneropinions.0.jsonl.xz
    1       1    953.7 MiB  4,356.2 MiB  0.219  CRC64   data/train.courtlisteneropinions.1.jsonl.xz
    1       1    953.7 MiB  4,315.6 MiB  0.221  CRC64   data/train.courtlisteneropinions.10.jsonl.xz
    1       1    953.7 MiB  4,650.3 MiB  0.205  CRC64   data/train.courtlisteneropinions.11.jsonl.xz
    1       1    953.7 MiB  4,836.3 MiB  0.197  CRC64   data/train.courtlisteneropinions.12.jsonl.xz
    1       1    953.7 MiB  4,644.9 MiB  0.205  CRC64   data/train.courtlisteneropinions.13.jsonl.xz
    1       1    953.7 MiB  4,657.5 MiB  0.205  CRC64   data/train.courtlisteneropinions.14.jsonl.xz
    1       1    539.2 MiB  2,621.8 MiB  0.206  CRC64   data/train.courtlisteneropinions.15.jsonl.xz
    1       1    953.7 MiB  4,335.3 MiB  0.220  CRC64   data/train.courtlisteneropinions.2.jsonl.xz
    1       1    953.7 MiB  4,352.0 MiB  0.219  CRC64   data/train.courtlisteneropinions.3.jsonl.xz
    1       1    953.7 MiB  4,575.9 MiB  0.208  CRC64   data/train.courtlisteneropinions.4.jsonl.xz
    1       1    953.7 MiB  4,382.6 MiB  0.218  CRC64   data/train.courtlisteneropinions.5.jsonl.xz
    1       1    953.7 MiB  4,352.3 MiB  0.219  CRC64   data/train.courtlisteneropinions.6.jsonl.xz
    1       1    953.7 MiB  4,462.4 MiB  0.214  CRC64   data/train.courtlisteneropinions.7.jsonl.xz
    1       1    953.7 MiB  4,604.0 MiB  0.207  CRC64   data/train.courtlisteneropinions.8.jsonl.xz
    1       1    953.7 MiB  4,612.0 MiB  0.207  CRC64   data/train.courtlisteneropinions.9.jsonl.xz
  335     335  6,047.4 KiB     24.1 MiB  0.245  CRC64   data/train.doj_guidance.jsonl.xz
    1       1     41.1 MiB    305.6 MiB  0.135  CRC64   data/train.dol_ecab.jsonl.xz
    1       1     19.1 MiB    100.5 MiB  0.190  CRC64   data/train.echr.jsonl.xz
  508     507  1,502.0 KiB  4,716.7 KiB  0.318  CRC64   data/train.ed_policy_guidance.jsonl.xz
    1       1  1,372.0 MiB  9,032.6 MiB  0.152  CRC64   data/train.edgar.jsonl.xz
    1       1  3,896.6 KiB     18.6 MiB  0.205  CRC64   data/train.eoir.jsonl.xz
    1       1    140.3 MiB  1,154.7 MiB  0.121  CRC64   data/train.eurlex.jsonl.xz
    1       1     51.4 MiB    239.4 MiB  0.215  CRC64   data/train.euro_parl.jsonl.xz
    1       1    355.3 KiB  1,512.5 KiB  0.235  CRC64   data/train.examoutlines.jsonl.xz
    1       1     20.7 MiB    131.7 MiB  0.157  CRC64   data/train.federal_register.jsonl.xz
  396     396     43.9 MiB    175.7 MiB  0.250  CRC64   data/train.fmshrc.jsonl.xz
    1       1     73.4 MiB    341.7 MiB  0.215  CRC64   data/train.founding_docs.jsonl.xz
    1       1    324.2 KiB  1,459.4 KiB  0.222  CRC64   data/train.frcp.jsonl.xz
    1       1    116.1 KiB    484.9 KiB  0.239  CRC64   data/train.fre.jsonl.xz
    1       1    297.3 KiB  1,245.0 KiB  0.239  CRC64   data/train.ftc_advisory_opinions.jsonl.xz
2,084   2,083     13.4 MiB     42.2 MiB  0.318  CRC64   data/train.hhs_alj.jsonl.xz
    1       1     29.5 MiB    157.4 MiB  0.188  CRC64   data/train.ijc.jsonl.xz
  442     442  7,904.4 KiB     35.8 MiB  0.216  CRC64   data/train.irs_legal_advice_memos.jsonl.xz
  658     658  3,403.1 KiB     10.6 MiB  0.314  CRC64   data/train.medicaid_policy_guidance.jsonl.xz
    1       1    170.7 MiB    788.9 MiB  0.216  CRC64   data/train.nlrb_decisions.jsonl.xz
    1       1    218.4 MiB  1,580.3 MiB  0.138  CRC64   data/train.oig.jsonl.xz
    1       1  5,857.4 KiB     31.5 MiB  0.182  CRC64   data/train.olc_memos.jsonl.xz
    1       1     58.6 MiB    234.5 MiB  0.250  CRC64   data/train.r_legaldvice.jsonl.xz
1,639   1,639     43.7 MiB    188.1 MiB  0.232  CRC64   data/train.resource_contracts.jsonl.xz
    1       1    242.6 MiB  1,241.6 MiB  0.195  CRC64   data/train.scotus_docket_entries.jsonl.xz
    1       1     68.5 MiB    323.2 MiB  0.212  CRC64   data/train.scotus_oral.jsonl.xz
10,805  10,805     40.7 MiB    118.4 MiB  0.344  CRC64   data/train.sec.jsonl.xz
    1       1    705.0 MiB  5,019.9 MiB  0.140  CRC64   data/train.state_code.jsonl.xz
    1       1     75.2 MiB    540.8 MiB  0.139  CRC64   data/train.taxrulings.jsonl.xz
    1       1    273.6 KiB  1,318.5 KiB  0.207  CRC64   data/train.tos.jsonl.xz
    1       1     22.6 MiB    108.1 MiB  0.209  CRC64   data/train.undebates.jsonl.xz
    1       1    167.6 MiB  1,119.6 MiB  0.150  CRC64   data/train.us_bills.jsonl.xz
    1       1     25.3 MiB    196.1 MiB  0.129  CRC64   data/train.uscode.jsonl.xz
    1       1  1,713.2 MiB     33.7 GiB  0.050  CRC64   data/train.uspto_oab.jsonl.xz
   54      54  2,960.9 KiB     11.0 MiB  0.264  CRC64   data/validation.acus_reports.jsonl.xz
    1       1  1,024.1 MiB  6,797.1 MiB  0.151  CRC64   data/validation.atticus_contracts.0.jsonl.xz
    1       1    374.6 MiB  2,471.7 MiB  0.152  CRC64   data/validation.atticus_contracts.1.jsonl.xz
    1       1    523.0 MiB  4,258.9 MiB  0.123  CRC64   data/validation.bva.jsonl.xz
    1       1      9.8 MiB     50.5 MiB  0.195  CRC64   data/validation.canadian_decisions.jsonl.xz
    1       1  4,281.5 KiB     19.1 MiB  0.219  CRC64   data/validation.cc_casebooks.jsonl.xz
    1       1  1,532.6 KiB     19.6 MiB  0.077  CRC64   data/validation.cfpb_cc.jsonl.xz
    1       1     23.3 MiB    190.4 MiB  0.122  CRC64   data/validation.cfr.jsonl.xz
    1       1    347.4 MiB  1,620.7 MiB  0.214  CRC64   data/validation.congressional_hearings.jsonl.xz
    1       1  1,102.4 KiB  6,733.0 KiB  0.164  CRC64   data/validation.constitutions.jsonl.xz
    1       1  1,024.1 MiB     10.7 GiB  0.094  CRC64   data/validation.courtlistenerdocketentries.0.jsonl.xz
    1       1    473.7 MiB  5,225.2 MiB  0.091  CRC64   data/validation.courtlistenerdocketentries.1.jsonl.xz
    1       1    953.7 MiB  4,391.3 MiB  0.217  CRC64   data/validation.courtlisteneropinions.0.jsonl.xz
    1       1    953.7 MiB  4,406.9 MiB  0.216  CRC64   data/validation.courtlisteneropinions.1.jsonl.xz
    1       1    953.8 MiB  4,436.7 MiB  0.215  CRC64   data/validation.courtlisteneropinions.2.jsonl.xz
    1       1    953.7 MiB  4,476.9 MiB  0.213  CRC64   data/validation.courtlisteneropinions.3.jsonl.xz
    1       1    953.7 MiB  4,618.0 MiB  0.207  CRC64   data/validation.courtlisteneropinions.4.jsonl.xz
    1       1    238.5 MiB  1,147.4 MiB  0.208  CRC64   data/validation.courtlisteneropinions.5.jsonl.xz
  100     100  1,778.7 KiB  7,371.5 KiB  0.241  CRC64   data/validation.doj_guidance.jsonl.xz
    1       1     13.8 MiB    101.5 MiB  0.136  CRC64   data/validation.dol_ecab.jsonl.xz
    1       1  4,132.1 KiB     20.8 MiB  0.194  CRC64   data/validation.echr.jsonl.xz
  174     173    490.5 KiB  1,564.9 KiB  0.313  CRC64   data/validation.ed_policy_guidance.jsonl.xz
    1       1    453.6 MiB  2,978.9 MiB  0.152  CRC64   data/validation.edgar.jsonl.xz
    1       1  1,340.0 KiB  6,294.8 KiB  0.213  CRC64   data/validation.eoir.jsonl.xz
    1       1     49.1 MiB    393.7 MiB  0.125  CRC64   data/validation.eurlex.jsonl.xz
    1       1     17.0 MiB     79.0 MiB  0.215  CRC64   data/validation.euro_parl.jsonl.xz
    1       1    103.7 KiB    547.9 KiB  0.189  CRC64   data/validation.examoutlines.jsonl.xz
    1       1  7,419.0 KiB     45.7 MiB  0.158  CRC64   data/validation.federal_register.jsonl.xz
  120     120     13.5 MiB     53.9 MiB  0.250  CRC64   data/validation.fmshrc.jsonl.xz
    1       1     25.3 MiB    113.2 MiB  0.224  CRC64   data/validation.founding_docs.jsonl.xz
    1       1     63.5 KiB    248.8 KiB  0.255  CRC64   data/validation.frcp.jsonl.xz
    1       1     58.4 KiB    226.7 KiB  0.257  CRC64   data/validation.fre.jsonl.xz
    1       1    117.4 KiB    419.1 KiB  0.280  CRC64   data/validation.ftc_advisory_opinions.jsonl.xz
  722     721  4,900.2 KiB     15.1 MiB  0.318  CRC64   data/validation.hhs_alj.jsonl.xz
    1       1     10.0 MiB     52.3 MiB  0.191  CRC64   data/validation.ijc.jsonl.xz
  161     161  3,791.0 KiB     17.7 MiB  0.209  CRC64   data/validation.irs_legal_advice_memos.jsonl.xz
  214     214  1,101.1 KiB  3,411.1 KiB  0.323  CRC64   data/validation.medicaid_policy_guidance.jsonl.xz
    1       1     55.8 MiB    257.8 MiB  0.217  CRC64   data/validation.nlrb_decisions.jsonl.xz
    1       1     80.0 MiB    603.7 MiB  0.132  CRC64   data/validation.oig.jsonl.xz
    1       1  1,826.2 KiB  9,874.6 KiB  0.185  CRC64   data/validation.olc_memos.jsonl.xz
    1       1     19.7 MiB     78.7 MiB  0.251  CRC64   data/validation.r_legaldvice.jsonl.xz
  584     584     15.3 MiB     63.5 MiB  0.241  CRC64   data/validation.resource_contracts.jsonl.xz
    1       1     86.4 MiB    422.5 MiB  0.204  CRC64   data/validation.scotus_docket_entries.jsonl.xz
    1       1     23.1 MiB    109.0 MiB  0.212  CRC64   data/validation.scotus_oral.jsonl.xz
3,559   3,559     13.0 MiB     37.7 MiB  0.344  CRC64   data/validation.sec.jsonl.xz
    1       1    371.8 MiB  2,678.4 MiB  0.139  CRC64   data/validation.state_code.jsonl.xz
    1       1     24.8 MiB    177.4 MiB  0.140  CRC64   data/validation.taxrulings.jsonl.xz
    1       1     92.7 KiB    381.6 KiB  0.243  CRC64   data/validation.tos.jsonl.xz
    1       1  7,705.6 KiB     35.5 MiB  0.212  CRC64   data/validation.undebates.jsonl.xz
    1       1     53.8 MiB    356.3 MiB  0.151  CRC64   data/validation.us_bills.jsonl.xz
    1       1     15.2 MiB    117.5 MiB  0.129  CRC64   data/validation.uscode.jsonl.xz
    1       1    885.5 MiB     11.2 GiB  0.077  CRC64   data/validation.uspto_oab.jsonl.xz
-------------------------------------------------------------------------------
22,839  22,833     41.0 GiB    291.5 GiB  0.141  CRC64   119 files

```

### Data Fields

- text: the document text
- created_timestamp: If the original source provided a timestamp when the document was created we provide this as well. Note, these may be inaccurate. For example CourtListener case opinions provide the timestamp of when it was uploaded to CourtListener not when the opinion was published. We welcome pull requests to correct this field if such inaccuracies are discovered.
- downloaded_timestamp: When the document was scraped.
- url: the source url

### Data Splits

There is a train/validation split for each subset of the data. 75%/25%. Note, we do not use the validation set for any downstream tasks nor do we filter out any data from downstream tasks. Please filter as needed before training models or feel free to use a different dataset split.

## Dataset Creation

### Curation Rationale

We curate a large corpus of legal and administrative data. The utility of this data is twofold: (1) to aggregate legal and administrative data sources that demonstrate different norms and legal standards for data filtering; (2) to collect a dataset that can be used in the future for pretraining legal-domain language models, a key direction in access-to-justice initiatives. As such, data sources are curated to inform: (1) legal analysis, knowledge, or understanding; (2) argument formation; (3) privacy filtering standards. Sources like codes and laws tend to inform (1). Transcripts and court filings tend to inform (2). Opinions tend to inform (1) and (3).

### Source Data

#### Initial Data Collection and Normalization

We do not normalize the data, but we provide dataset creation code and relevant urls in https://github.com/Breakend/PileOfLaw

#### Who are the source language producers?

Varied (see sources above).

### Personal and Sensitive Information

This dataset may contain personal and sensitive information. However, this has been previously filtered by the relevant government and federal agencies that weigh the harms of revealing this information against the benefits of transparency. If you encounter something particularly harmful, please file a takedown request with the upstream source and notify us in the communities tab. We will then remove the content. We cannot enable more restrictive licensing because upstream sources may restrict using a more restrictive license. However, we ask that all users of this data respect the upstream licenses and restrictions. Per the standards of CourtListener, we do not allow indexing of this data by search engines and we ask that others do not also. Please do not turn on anything that allows the data to be easily indexed.

## Considerations for Using the Data

### Social Impact of Dataset

We hope that this dataset will provide more mechanisms for doing data work. As we describe in the paper, the internal variation allows contextual privacy rules to be learned. If robust mechanisms for this are developed they can applied more broadly. This dataset can also potentially be used for legal language model pretraining. As discussed in ``On the Opportunities and Risks of Foundation Models'', legal language models can help improve access to justice in various ways. But they can also be used in potentially harmful ways. While such models are not ready for most production environments and are the subject of significant research, we ask that model creators using this data, particularly when creating generative models, consider the impacts of their model and make a good faith effort to weigh the benefits against the harms of their method. Our license and many of the sub-licenses also restrict commercial usage.

### Discussion of Biases

The data reflects the biases of governments and courts. As we discuss in our work, these can be significant, though more recent text will likely be less overtly toxic. Please see the above statement and embark on any model uses responsibly.

### Other Known Limitations

We mainly focus on U.S. and English-speaking legal sources, though we include some European and Canadian resources.

## Additional Information

### Licensing Information

 CreativeCommons Attribution-NonCommercial-ShareAlike 4.0 International. But individual sources may have other licenses. See paper for details. Some upstream data sources request that indexing be disabled. As such please **do not re-host any data in a way that can be indexed by search engines.**

### No Representations

We do not make any representation that the legal information provided here is accurate. It is meant for research purposes only. For the authoritative and updated source of information please refer directly to the governing body which provides the latest laws, rules, and regulations relevant to you.

### DMCA Takedown Requests

Pile of Law follows the notice and takedown procedures in the Digital Millennium Copyright Act (DMCA), 17 U.S.C. Section 512.

If you believe content on Pile of Law violates your copyright, please immediately notify its operators by sending a message with the information described below. Please use the subject "Copyright" in your message. If Pile of Law's operators act in response to an infringement notice, they will make a good-faith attempt to contact the person who contributed the content using the most recent email address that person provided to Pile of Law.

Under the DMCA, you may be held liable for damages based on material misrepresentations in your infringement notice. You must also make a good-faith evaluation of whether the use of your content is a fair use, because fair uses are not infringing. See 17 U.S.C. Section 107 and Lenz v. Universal Music Corp., No. 13-16106 (9th Cir. Sep. 14, 2015). If you are not sure if the content you want to report infringes your copyright, you should first contact a lawyer.

The DMCA requires that all infringement notices must include all of the following:

+ A signature of the copyright owner or a person authorized to act on the copyright owner's behalf
+ An identification of the copyright claimed to have been infringed
+ A description of the nature and location of the material that you claim to infringe your copyright, in sufficient detail to allow Pile of Law to find and positively identify that material
+ Your name, address, telephone number, and email address
+ A statement that you believe in good faith that the use of the material that you claim to infringe your copyright is not authorized by law, or by the copyright owner or such owner's agent
+ A statement, under penalty of perjury, that all of the information contained in your infringement notice is accurate
+ A statement, under penalty of perjury, that you are either the copyright owner or a person authorized to act on their behalf.

Pile of Law will respond to all DMCA-compliant infringement notices, including, as required or appropriate, by removing the offending material or disabling all links to it.

All received infringement notices may be posted in full to the Lumen database (previously known as the Chilling Effects Clearinghouse). 

All takedown requests with the above information should be posted to the Communities tab.

This removal notice has been modified from the (CourtListener DMCA takedown notice)[https://www.courtlistener.com/terms/].

### Citation Information

For a citation to this work:

```
@misc{hendersonkrass2022pileoflaw,
  url = {https://arxiv.org/abs/2207.00220},
  author = {Henderson*, Peter and Krass*, Mark S. and Zheng, Lucia and Guha, Neel and Manning, Christopher D. and Jurafsky, Dan and Ho, Daniel E.},
  title = {Pile of Law: Learning Responsible Data Filtering from the Law and a 256GB Open-Source Legal Dataset},
  publisher = {arXiv},
  year = {2022}
}
```

Since this dataset also includes several other data sources with citations, please refer to our paper and cite the additional relevant work in addition to our own work.