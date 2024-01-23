---
language:
- en
multilinguality:
- monolingual
annotations_creators:
- crowdsourced
language_creators:
- crowdsourced
license:
- other
pretty_name: NTRS
size_categories:
- 1M<n<10M
source_datasets:
- original
task_categories:
- text-generation
- fill-mask
task_ids:
- language-modeling
- masked-language-modeling
---

# Dataset Card for NASA technical report server metadata

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
 - [Considerations for Using the Data](#considerations-for-using-the-data)
- [Additional Information](#additional-information)
  - [Licensing Information](#licensing-information)
  - [Contributions](#contributions)

## Dataset Description

**Homepage: https://ntrs.nasa.gov/**

### Dataset Summary
The NTRS collects scientific and technical information funded or created by NASA and provides metadata but also access to abstracts and full texts.
The dataset contains all abstracts, titles, and associated metadata indexed on the NTRS.
The most recent bulk download can be aquired via the NTRS directly at:
https://sti.nasa.gov/harvesting-data-from-ntrs/

This repository does not claim any ownership on the provided data, it only is supposed to provide an easily accesible gateway to the data, through the Huggingface API. 
The original author and source should always be credited.

## Dataset Structure

### Data Instances

The dataset contain over 508000 objects (abstracts) and associated metadata from NASA funded projects in time range of 1917 to today (18.06.2022). 
It therefore is a rich data source for language modeling in the domain of spacecraft design and space science.

### Data Fields
```yaml
"copyright": {"licenseType":"NO,"determinationType":"GOV_PUBLIC_USE_PERMITTED", "thirdPartyContentCondition":"NOT_SET",...},
 "subjectCategories": ["Space Transportation and Safety"],
 "exportControl": {"isExportControl":"NO","ear":"NO","itar":"NO",...},
 "created": "2022-01-28T15:19:38.8948330+00:00",
 "distributionDate": "2019-07-12T00:00:00.0000000+00:00",
 "otherReportNumbers": ["NACA-AR-1"],
 "center": {"code":"CDMS","name":"Legacy CDMS","id":"092d6e0881874968859b972d39a888dc"},
 "onlyAbstract": False,
 "sensitiveInformation": 2,
 "abstract": "Report includes the National Advisory Committe...",
 "title": "Annual Report of the National Advisory Committ...",
 "stiType": "CONTRACTOR_OR_GRANTEE_REPORT",
 "distribution": "PUBLIC",
 "submittedDate": "2013-09-06T18:26:00.0000000+00:00",
 "isLessonsLearned": 0.0,
 "disseminated": "DOCUMENT_AND_METADATA",
 "stiTypeDetails": "Contractor or Grantee Report",
 "technicalReviewType": "TECHNICAL_REVIEW_TYPE_NONE",
 "modified": "2013-08-29 00:00:00.000000",
 "id": 19930091025,
 "publications": [{"submissionId":19930091025,"publicationDate":1916-01-01T00:00:00.0000000+00:00,"issn":"https://doi.org/10.1109/BigData52589.2021.9671853",...},...]
 "status": "CURATED",
 "authorAffiliations": [{"sequence":0,"meta":{"author":{"name":"Author_name_1","orcidId":"ID"},"organization":{"name":"NASA",...}},"id":ID},{"sequence":1,...,}]
 "keywords": [Web scraping, data mining, epidemiology],
 "meetings": [{"country":"US","name":"2021 IEEE",...},...]
 "fundingNumbers": [{"number":"920121",	"type":"CONTRACT_GRANT"},...]
 "redactedDate": "2022-04-20T14:36:15.0925240",
 "sourceIdentifiers": []}
```

## Dataset Creation

### Curation Rationale

The last bulk download was done on 18.06.2022. The dataset was cleaned from abstracts that occur multiple times. 

## Considerations for Using the Data

Main field that probably interest people:

"abstract", "subjectCategory", "keywords", "center"

## Additional Information

### Licensing Information
"Generally, United States government works (works prepared by officers and employees of the U.S. Government as part of their official duties) are not protected by copyright in the U.S. (17 U.S.C. §105) and may be used without obtaining permission from NASA. However, U.S. government works may contain privately created, copyrighted works (e.g., quote, photograph, chart, drawing, etc.) used under license or with permission of the copyright owner. Incorporation in a U.S. government work does not place the private work in the public domain.
place the private work in the public domain.

Moreover, not all materials on or available through download from this Web site are U.S. government works. Some materials available from this Web site may be protected by copyrights owned by private individuals or organizations and may be subject to restrictions on use. For example, contractors and grantees are not considered Government employees; generally, they hold copyright to works they produce for the Government. Other materials may be the result of joint authorship due to collaboration between a Government employee and a private individual wherein the private individual will hold a copyright to the work jointly with U.S. Government. The Government is granted a worldwide license to use, modify, reproduce, release, perform, display, or disclose these works by or on behalf of the Government.

While NASA may publicly release copyrighted works in which it has government purpose licenses or specific permission to release, such licenses or permission do not necessarily transfer to others. Thus, such works are still protected by copyright, and recipients of the works must comply with the copyright law (Title 17 United States Code). Such copyrighted works may not be modified, reproduced, or redistributed without permission of the copyright owner."

Taken from https://sti.nasa.gov/disclaimers/, please visit for more information. 
### Contributions

For any any inquiries about this data set please contact [@pauldrm](https://github.com/<github-username>) 
