---
annotations_creators:
- expert-generated
language_creators:
- found
- expert-generated
language:
- en
license:
- cc-by-nc-4.0
multilinguality:
- monolingual
paperswithcode_id: phrase-in-context
pretty_name: 'PiC: Phrase Retrieval'
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- text-retrieval
task_ids: []
---

# Dataset Card for "PiC: Phrase Retrieval"

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

- **Homepage:** [https://phrase-in-context.github.io/](https://phrase-in-context.github.io/)
- **Repository:** [https://github.com/phrase-in-context](https://github.com/phrase-in-context)
- **Paper:**
- **Leaderboard:**
- **Point of Contact:** [Thang Pham](<thangpham@auburn.edu>)

### Dataset Summary

PR is a phrase retrieval task with the goal of finding a phrase **t** in a given document **d** such that **t** is semantically similar to the query phrase, which is the paraphrase **q**<sub>1</sub> provided by annotators.
We release two versions of PR: **PR-pass** and **PR-page**, i.e., datasets of 3-tuples (query **q**<sub>1</sub>, target phrase **t**, document **d**) where **d** is a random 11-sentence passage that contains **t** or an entire Wikipedia page.
While PR-pass contains 28,147 examples, PR-page contains slightly fewer examples (28,098) as we remove those trivial examples whose Wikipedia pages contain exactly the query phrase (in addition to the target phrase).
Both datasets are split into 5K/3K/~20K for test/dev/train, respectively.

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

English.

## Dataset Structure

### Data Instances

**PR-pass**
* Size of downloaded dataset files: 43.61 MB
* Size of the generated dataset: 36.98 MB
* Total amount of disk used: 80.59 MB

An example of 'train' looks as follows.

```
{
  "id": "3478-1",
  "title": "https://en.wikipedia.org/wiki?curid=181261",
  "context": "The 425t was a 'pizza box' design with a single network expansion slot. The 433s was a desk-side server systems with multiple expansion slots. Compatibility. PC compatibility was possible either through software emulation, using the optional product DPCE, or through a plug-in card carrying an Intel 80286 processor. A third-party plug-in card with a 386 was also available. An Apollo Token Ring network card could also be placed in a standard PC and network drivers allowed it to connect to a server running a PC SMB (Server Message Block) file server. Usage. Although Apollo systems were easy to use and administer, they became less cost-effective because the proprietary operating system made software more expensive than Unix software. The 68K processors were slower than the new RISC chips from Sun and Hewlett-Packard. Apollo addressed both problems by introducing the RISC-based DN10000 and Unix-friendly Domain/OS operating system. However, the DN10000, though fast, was extremely expensive, and a reliable version of Domain/OS came too late to make a difference.",
  "query": "dependable adaptation",
  "answers": {
    "text": ["reliable version"], 
    "answer_start": [1006] 
  }
}
```

**PR-page**
* Size of downloaded dataset files: 421.56 MB
* Size of the generated dataset: 412.17 MB
* Total amount of disk used: 833.73 MB

An example of 'train' looks as follows.

```
{
  "id": "5961-2",
  "title": "https://en.wikipedia.org/wiki?curid=354711",
  "context": "Joseph Locke FRSA (9 August 1805 – 18 September 1860) was a notable English civil engineer of the nineteenth century, particularly associated with railway projects. Locke ranked alongside Robert Stephenson and Isambard Kingdom Brunel as one of the major pioneers of railway development. Early life and career. Locke was born in Attercliffe, Sheffield in Yorkshire, moving to nearby Barnsley when he was five. By the age of 17, Joseph had already served an apprenticeship under William Stobart at Pelaw, on the south bank of the Tyne, and under his own father, William. He was an experienced mining engineer, able to survey, sink shafts, to construct railways, tunnels and stationary engines. Joseph's father had been a manager at Wallbottle colliery on Tyneside when George Stephenson was a fireman there. In 1823, when Joseph was 17, Stephenson was involved with planning the Stockton and Darlington Railway. He and his son Robert Stephenson visited William Locke and his son at Barnsley and it was arranged that Joseph would go to work for the Stephensons. The Stephensons established a locomotive works near Forth Street, Newcastle upon Tyne, to manufacture locomotives for the new railway. Joseph Locke, despite his youth, soon established a position of authority. He and Robert Stephenson became close friends, but their friendship was interrupted, in 1824, by Robert leaving to work in Colombia for three years. Liverpool and Manchester Railway. George Stephenson carried out the original survey of the line of the Liverpool and Manchester Railway, but this was found to be flawed, and the line was re-surveyed by a talented young engineer, Charles Vignoles. Joseph Locke was asked by the directors to carry out another survey of the proposed tunnel works and produce a report. The report was highly critical of the work already done, which reflected badly on Stephenson. Stephenson was furious and henceforth relations between the two men were strained, although Locke continued to be employed by Stephenson, probably because the latter recognised his worth. Despite the many criticisms of Stephenson's work, when the bill for the new line was finally passed, in 1826, Stephenson was appointed as engineer and he appointed Joseph Locke as his assistant to work alongside Vignoles, who was the other assistant. However, a clash of personalities between Stephenson and Vignoles led to the latter resigning, leaving Locke as the sole assistant engineer. Locke took over responsibility for the western half of the line. One of the major obstacles to be overcome was Chat Moss, a large bog that had to be crossed. Although, Stephenson usually gets the credit for this feat, it is believed that it was Locke who suggested the correct method for crossing the bog. Whilst the line was being built, the directors were trying to decide whether to use standing engines or locomotives to propel the trains. Robert Stephenson and Joseph Locke were convinced that locomotives were vastly superior, and in March 1829 the two men wrote a report demonstrating the superiority of locomotives when used on a busy railway. The report led to the decision by the directors to hold an open trial to find the best locomotive. This was the Rainhill Trials, which were run in October 1829, and were won by \"Rocket\". When the line was finally opened in 1830, it was planned for a procession of eight trains to travel from Liverpool to Manchester and back. George Stephenson drove the leading locomotive \"Northumbrian\" and Joseph Locke drove \"Rocket\". The day was marred by the death of William Huskisson, the Member of Parliament for Liverpool, who was struck and killed by \"Rocket\". Grand Junction Railway. In 1829 Locke was George Stephenson's assistant, given the job of surveying the route for the Grand Junction Railway. This new railway was to join Newton-le-Willows on the Liverpool and Manchester Railway with Warrington and then on to Birmingham via Crewe, Stafford and Wolverhampton, a total of 80 miles. Locke is credited with choosing the location for Crewe and recommending the establishment there of shops required for the building and repairs of carriages and wagons as well as engines. During the construction of the Liverpool and Manchester Railway, Stephenson had shown a lack of ability in organising major civil engineering projects. On the other hand, Locke's ability to manage complex projects was well known. The directors of the new railway decided on a compromise whereby Locke was made responsible for the northern half of the line and Stephenson was made responsible for the southern half. However Stephenson's administrative inefficiency soon became apparent, whereas Locke estimated the costs for his section of the line so meticulously and speedily, that he had all of the contracts signed for his section of the line before a single one had been signed for Stephenson's section. The railway company lost patience with Stephenson, but tried to compromise by making both men joint-engineers. Stephenson's pride would not let him accept this, and so he resigned from the project. By autumn of 1835 Locke had become chief engineer for the whole of the line. This caused a rift between the two men, and strained relations between Locke and Robert Stephenson. Up to this point, Locke had always been under George Stephenson's shadow. From then on, he would be his own man, and stand or fall by his own achievements. The line was opened on 4 July 1837. New methods. Locke's route avoided as far as possible major civil engineering works. The main one was the Dutton Viaduct which crosses the River Weaver and the Weaver Navigation between the villages of Dutton and Acton Bridge in Cheshire. The viaduct consists of 20 arches with spans of 20 yards. An important feature of the new railway was the use of double-headed (dumb-bell) wrought-iron rail supported on timber sleepers at 2 ft 6 in intervals. It was intended that when the rails became worn they could be turned over to use the other surface, but in practice it was found that the chairs into which the rails were keyed caused wear to the bottom surface so that it became uneven. However this was still an improvement on the fish-bellied, wrought-iron rails still being used by Robert Stephenson on the London and Birmingham Railway. Locke was more careful than Stephenson to get value for his employers' money. For the Penkridge Viaduct Stephenson had obtained a tender of £26,000. After Locke took over, he gave the potential contractor better information and agreed a price of only £6,000. Locke also tried to avoid tunnels because in those days tunnels often took longer and cost more than planned. The Stephensons regarded 1 in 330 as the maximum slope that an engine could manage and Robert Stephenson achieved this on the London and Birmingham Railway by using seven tunnels which added both cost and delay. Locke avoided tunnels almost completely on the Grand Junction but exceeded the slope limit for six miles south of Crewe. Proof of Locke's ability to estimate costs accurately is given by the fact that the construction of the Grand Junction line cost £18,846 per mile as against Locke's estimate of £17,000. This is amazingly accurate compared with the estimated costs for the London and Birmingham Railway (Robert Stephenson) and the Great Western Railway (Brunel). Locke also divided the project into a few large sections rather than many small ones. This allowed him to work closely with his contractors to develop the best methods, overcome problems and personally gain practical experience of the building process and of the contractors themselves. He used the contractors who worked well with him, especially Thomas Brassey and William Mackenzie, on many other projects. Everyone gained from this cooperative approach whereas Brunel's more adversarial approach eventually made it hard for him to get anyone to work for him. Marriage. In 1834 Locke married Phoebe McCreery, with whom he adopted a child. He was elected to the Royal Society in 1838. Lancaster and Carlisle Railway. A significant difference in philosophy between George Stephenson and Joseph Locke and the surveying methods they employed was more than a mere difference of opinion. Stephenson had started his career at a time when locomotives had little power to overcome excessive gradients. Both George and Robert Stephenson were prepared to go to great lengths to avoid steep gradients that would tax the locomotives of the day, even if this meant choosing a circuitous path that added on extra miles to the line of the route. Locke had more confidence in the ability of modern locomotives to climb these gradients. An example of this was the Lancaster and Carlisle Railway, which had to cope with the barrier of the Lake District mountains. In 1839 Stephenson proposed a circuitous route that avoided the Lake District altogether by going all the way round Morecambe Bay and West Cumberland, claiming: 'This is the only practicable line from Liverpool to Carlisle. The making of a railway across Shap Fell is out of the question.' The directors rejected his route and chose the one proposed by Joseph Locke, one that used steep gradients and passed over Shap Fell. The line was completed by Locke and was a success. Locke's reasoned that by avoiding long routes and tunnelling, the line could be finished more quickly, with less capital costs, and could start earning revenue sooner. This became known as the 'up and over' school of engineering (referred to by Rolt as 'Up and Down,' or Rollercoaster). Locke took a similar approach in planning the Caledonian Railway, from Carlisle to Glasgow. In both railways he introduced gradients of 1 in 75, which severely taxed fully laden locomotives, for even as more powerful locomotives were introduced, the trains that they pulled became heavier. It may therefore be argued that Locke, although his philosophy carried the day, was not entirely correct in his reasoning. Even today, Shap Fell is a severe test of any locomotive. Manchester and Sheffield Railway. Locke was subsequently appointed to build a railway line from Manchester to Sheffield, replacing Charles Vignoles as chief engineer, after the latter had been beset by misfortunes and financial difficulties. The project included the three-mile Woodhead Tunnel, and the line opened, after many delays, on 23 December 1845. The building of the line required over a thousand navvies and cost the lives of thirty-two of them, seriously injuring 140 others. The Woodhead Tunnel was such a difficult undertaking that George Stephenson claimed that it could not be done, declaring that he would eat the first locomotive that got through the tunnel. Subsequent commissions. In the north, Locke also designed the Lancaster and Preston Junction Railway; the Glasgow, Paisley and Greenock Railway; and the Caledonian Railway from Carlisle to Glasgow and Edinburgh. In the south, he worked on the London and Southampton Railway, later called the London and South Western Railway, designing, among other structures, Nine Elms to Waterloo Viaduct, Richmond Railway Bridge (1848, since replaced), and Barnes Bridge (1849), both across the River Thames, tunnels at Micheldever, and the 12-arch Quay Street viaduct and the 16-arch Cams Hill viaduct, both in Fareham (1848). He was actively involved in planning and building many railways in Europe (assisted by John Milroy), including the Le Havre, Rouen, Paris rail link, the Barcelona to Mataró line and the Dutch Rhenish Railway. He was present in Paris when the Versailles train crash occurred in 1842, and produced a statement concerning the facts for General Charles Pasley of the Railway Inspectorate. He also experienced a catastrophic failure of one of his viaducts built on the new Paris-Le Havre link. . The viaduct was of stone and brick at Barentin near Rouen, and was the longest and highest on the line. It was 108 feet high, and consisted of 27 arches, each 50 feet wide, with a total length of over 1600 feet. A boy hauling ballast for the line up an adjoining hillside early that morning (about 6.00 am) saw one arch (the fifth on the Rouen side) collapse, and the rest followed suit. Fortunately, no one was killed, although several workmen were injured in a mill below the structure. Locke attributed the catastrophic failure to frost action on the new lime cement, and premature off-centre loading of the viaduct with ballast. It was rebuilt at Thomas Brassey's cost, and survives to the present. Having pioneered many new lines in France, Locke also helped establish the first locomotive works in the country. Distinctive features of Locke's railway works were economy, the use of masonry bridges wherever possible and the absence of tunnels. An illustration of this is that there is no tunnel between Birmingham and Glasgow. Relationship with Robert Stephenson. Locke and Robert Stephenson had been good friends at the beginning of their careers, but their friendship had been marred by Locke's falling out with Robert's father. It seems that Robert felt loyalty to his father required that he should take his side. It is significant that after the death of George Stephenson in August 1848, the friendship of the two men was revived. When Robert Stephenson died in October 1859, Joseph Locke was a pallbearer at his funeral. Locke is reported to have referred to Robert as 'the friend of my youth, the companion of my ripening years, and a competitor in the race of life'. Locke was also on friendly terms with his other engineering rival, Isambard Kingdom Brunel. In 1845, Locke and Stephenson were both called to give evidence before two committees. In April a House of Commons Select Committee was investigating the atmospheric railway system proposed by Brunel. Brunel and Vignoles spoke in support of the system, whilst Locke and Stephenson spoke against it. The latter two were to be proved right in the long run. In August the two gave evidence before the Gauge Commissioners who were trying to arrive at a standard gauge for the whole country. Brunel spoke in favour of the 7 ft gauge he was using on the Great Western Railway. Locke and Stephenson spoke in favour of the 4 ft 8½in gauge that they had used on several lines. The latter two won the day and their gauge was adopted as the standard. Later life and legacy. Locke served as President of the Institution of Civil Engineers in between December 1857 and December 1859. He also served as Member of Parliament for Honiton in Devon from 1847 until his death. Joseph Locke died on 18 September 1860, apparently from appendicitis, whilst on a shooting holiday. He is buried in London's Kensal Green Cemetery. He outlived his friends/rivals Robert Stephenson and Isambard Brunel by less than a year; all three engineers died between 53 and 56 years of age, a circumstance attributed by Rolt to sheer overwork, accomplishing more in their brief lives than many achieve in a full three score and ten. Locke Park in Barnsley was dedicated to his memory by his widow Phoebe in 1862. It features a statue of Locke plus a folly, 'Locke Tower'. Locke's greatest legacy is the modern day West Coast Main Line (WCML), which was formed by the joining of the Caledonian, Lancaster &amp; Carlisle, Grand Junction railways to Robert Stephenson's London &amp; Birmingham Railway. As a result, around three-quarters of the WCML's route was planned and engineered by Locke.",
  "query": "accurate approach",
  "answers": {
    "text": ["correct method"], 
    "answer_start": [2727] 
  }
}
```

### Data Fields

The data fields are the same among all subsets and splits.

* id: a string feature.
* title: a string feature.
* context: a string feature.
* question: a string feature.
* answers: a dictionary feature containing:
  * text: a list of string features.
  * answer_start: a list of int32 features.

### Data Splits

|        name        |train|validation|test|
|--------------------|----:|---------:|---:|
|PR-pass             |20147|      3000|5000|
|PR-page             |20098|      3000|5000|

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

The source passages + answers are from Wikipedia and the source of queries were produced by our hired linguistic experts from [Upwork.com](https://upwork.com).

#### Who are the source language producers?

We hired 13 linguistic experts from [Upwork.com](https://upwork.com) for annotation and more than 1000 human annotators on Mechanical Turk along with another set of 5 Upwork experts for 2-round verification.

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

13 linguistic experts from [Upwork.com](https://upwork.com).

### Personal and Sensitive Information

No annotator identifying details are provided.

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

This dataset is a joint work between Adobe Research and Auburn University.
Creators: [Thang M. Pham](https://scholar.google.com/citations?user=eNrX3mYAAAAJ), [David Seunghyun Yoon](https://david-yoon.github.io/), [Trung Bui](https://sites.google.com/site/trungbuistanford/), and [Anh Nguyen](https://anhnguyen.me).

[@PMThangXAI](https://twitter.com/pmthangxai) added this dataset to HuggingFace.

### Licensing Information

This dataset is distributed under [Creative Commons Attribution-NonCommercial 4.0 International (CC-BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/)

### Citation Information

```
@article{pham2022PiC,
  title={PiC: A Phrase-in-Context Dataset for Phrase Understanding and Semantic Search},
  author={Pham, Thang M and Yoon, Seunghyun and Bui, Trung and Nguyen, Anh},
  journal={arXiv preprint arXiv:2207.09068},
  year={2022}
}
```