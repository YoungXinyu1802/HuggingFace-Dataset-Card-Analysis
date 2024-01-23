---
annotations_creators:
- expert-generated
language:
- en
language_creators:
- other
license:
- apache-2.0
multilinguality:
- monolingual
pretty_name: 'ASRS Aviation Incident Reports '
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- summarization
---

# Dataset Card for ASRS Aviation Incident Reports
## Table of Contents
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
- **Homepage:** [https://huggingface.co/datasets/elihoole/asrs-aviation-reports]
- **Repository:** [ASRS Incident Reports Summarisation code repo](https://github.com/elihoole/asrs-incident-reports)
- **Point of Contact:** [Elijah Hoole](mailto:E.J.Hoole@sms.ed.ac.uk)
### Dataset Summary
This dataset collects 47,723 aviation incident reports published in the Aviation Safety Reporting System (ASRS) database maintained by NASA. 

### Supported Tasks and Leaderboards
- 'summarization': Dataset can be used to train a model for abstractive and extractive summarization. The model performance is measured by how high the output summary's [ROUGE](https://huggingface.co/metrics/rouge) score for a given narrative account of an aviation incident is when compared to the synopsis as written by a NASA expert. Models and scores to follow. 

### Languages
The BCP-47 code for English as generally spoken in the United States is en-US and the BCP-47 code for English as generally spoken in the United Kingdom is en-GB. It is unknown if other varieties of English are represented in the data.

## Dataset Structure


### Data Instances
For each instance, there is a string for the narrative account (Report 1_Narrative), a string for the synopsis (Report 1.2_Synopsis), and a string for the document id (acn_num_ACN). Some instances may have two narratives (Report 1_Narrative & Report 2_Narrative) and extended analyses produced by experts (Report 1.1_Callback & Report 2.1_Callback). Other fields contain metadata such as time, location, flight conditions, aircraft model name, etc. associated with the incident. See the [ASRS Incident Reports dataset viewer](https://huggingface.co/datasets/elihoole/asrs-aviation-reports/viewer/elihoole--asrs-aviation-reports/train) to explore more examples.

```
{'acn_num_ACN': '1206196',
 'Report 1_Narrative': 'While taxiing company B757 aircraft from gate to Hangar line; we were cleared by Ground Control to proceed via A-T-join runway XX. After receiving subsequent clearance to T1 [then associated taxiways] to the hangar; we caught up to a dark; apparently unpowered company livery RJ (ERJ-145) near the T1 intersection.  The RJ was being towed dark with absolutely no external lighting on; a completely dark aircraft.  This situation only presented itself as we drew close to the aircraft in tow.  The towbarless tractor (supertug) was lit externally; but minimally visible from our vantage point; with a completely dark aircraft between us and the tractor.  Once the towing operation completed a turn onto taxiway T; a single green light came in view which is somehow mounted on supertug; presented a similar appearance to a green wing navigation light common on all aircraft.  To say this presented a confusing situation is an understatement. [Aircraft] operation in Noncompliance with FARs; Policy and Procedures.  This is a situation never before observed in [my] 30 plus years as a taxi mechanic at our location.  There are long established standards in place regarding external light usage and requirements; both in gate areas; as well as movement in active controlled taxiways; most with an eye on safety regarding aircraft position (nav lights) and anti-collision lights signaling running engines and/or aircraft movement.',
 'Report 1.1_Callback': '',
 'Report 2_Narrative': '',
 'Report 2.1_Callback': '',
 'Report 1.2_Synopsis': 'A Line Aircraft Maintenance Technician (AMT) taxiing a company B757 aircraft reports coming up on a dark; unpowered ERJ-145 aircraft with no external lighting on. Light on the towbarless Supertug tractor only minimally visible; with completely dark aircraft between their B757 and Tow tractor. Technician notes long established standards requiring Anti-Collision and Nav lights not enforced during aircraft tow.'}
```

The average token count for the articles and the highlights are provided below. 

| Feature             | Number of Instances | Mean Token Count |
| ------------------- | ------------------  | ---------------- |
| Report 1_Narrative  | 47,723              | 281              |
| Report 1.1_Callback | 1,435               | 103              |
| Report 2_Narrative  | 11,228              | 169              |
| Report 2.1 Callback | 85                  | 110              |
|​ Report 1.2_Synopsis | 47,723              | 27               |

### Data fields

More data explanation. 
