---
annotations_creators:
- expert-generated
language:
- en
language_creators:
- expert-generated
- machine-generated
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: Old Bailey Proceedings
size_categories:
- 1K<n<10K
source_datasets:
- original
task_categories:
- text-classification
- text-generation
task_ids:
- multi-class-classification
- language-modeling
- masked-language-modeling
---
[Needs More Information]

# Dataset Card for Old Bailey Proceedings

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-instances)
  - [Data Splits](#data-instances)
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

## Dataset Description

- **Homepage:** https://www.dhi.ac.uk/projects/old-bailey/
- **Repository:** https://www.dhi.ac.uk/san/data/oldbailey/
- **Paper:** [Needs More Information]
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** The University of Sheffield
Digital Humanities Institute
34 Gell Street
Sheffield S3 7QY

### Dataset Summary

**Note** We are making this dataset available via the HuggingFace hub to open it up to more users and use cases. We have focused primarily on making an initial version of this dataset available, focusing on some potential use cases. If you think there are other configurations this dataset should support, please use the community tab to open an issue. 

The dataset consists of 2,163 transcriptions of the Proceedings and 475 Ordinary's Accounts marked up in TEI-XML, and contains some documentation covering the data structure and variables. Each Proceedings file represents one session of the court (1674-1913), and each Ordinary's Account file represents a single pamphlet (1676-1772).

### Supported Tasks and Leaderboards

- `language-modeling`: This dataset can be used to contribute to the training or evaluation of language models for historical texts. Since it represents transcription from court proceedings, the language in this dataset may better represent the variety of language used at the time.
- `text-classification`: This dataset can be used to classify what style of English some text is in
- `named-entity-recognition`: Some of the text contains names of people and places. We don't currently provide the token IDs for these entities but do provide the tokens themselves. This means this dataset has the potential to be used to evaluate the performance of other Named Entity Recognition models on this dataset. 


### Languages

`en`

## Dataset Structure

### Data Instances

An example of one instance from the dataset: 

```python
{
'id': 'OA16760517', 
'text': "THE CONFESSION AND EXECUTION Of the Prisoners at TYBURN On Wednesday the 17May1676. Viz. Henry Seabrook , Elizabeth Longman Robert Scot , Condemned the former Sessions. Edward Wall , and Edward Russell . Giving a full 
and satisfactory Account of their Crimes, Behaviours, Discourses in Prison, and last Words (as neer as could be taken) at the place of Execution. Published for a Warning, to all that read it, to avoid the like wicked Courses, which brought these poor people to this shameful End. THE CONFESSION AND EXECUTION Of the Prisoners at TYBURN On Wednesday the 17th of May, 1676. Viz. Henry Seabrook , Elizabeth Longman Robert Scot , Condemned the former Sessions. Edward Wall , and Edward Russell . Giving a full and satisfactory Account of their Crimes, Behaviours, Discourses in Prison, and last Words (as neer as could be taken) at the place of Execution. Published for a Warning, to all that read it, to avoid the like wicked Courses, which brought these poor people to this shameful End. However, Mercy so far interposed after the Sentence of Justice, that only Five of them actually suffered: Amongst whom was Elizabeth Longman , an old Offendor, having been above a Dozen several times in Newgate : Some time since she was convicted, and obtained the benefit and favour of Transportation, and was accordingly carried into Virginia : But Clum, non Animutant, qu: trans mare currunt. She had not been there above Fourteen Moneths, before she 
procured Monies remitted from some of the Brotherhood here, wherewith she bought off her Servitude, and ever she comes again into England , long before the term of her Sentence was expired. Nor was she content to violate the Law only in that point, bur returned to her old Trade (for so these people call stealing) as well as to her Countrey; and was soon after her Arrival conducted to Newgate , for mistaking several parcels of Silk, upon which being Convicted, and pleading her Belly, she was 
set by the last Sessions before this: But now it appearing that she was highly accessary (though all the while in Newgate ) to the Robbery of a Person of Quality, and that she was wholly incorrigible, not to be reclaimed by any Warnings, she was brought down again to the Bar, and demanded, what she could say for her self, why she should not suffer Death, according to Law, upon her old Judgment. To which she still pleaded, that she was quick with Child. But being searched by a Jury of Matrons, they found no such thing; so that she was carried with the rest into the Hole, and ordered for Execution. As for her behaviour, I am sorry no better account can be given of it; for truely she did not seem so sensible of her End, or to make that serious preparation for it, as night be expected from a Person in her condition: yet were not the charitable assistances and endeavours of the Ordinary and several other Ministers wanting towards her, though 'tis feared they did not make the wisht-for Impressions upon her Spirit. Two others viz. Edward Wall and Edward Russel that suffered, were brought to this untimely and ignominious End, by the means and seducements of this unhappy Woman. For they together with one A. M. going after the former Sessions to a Gentlemans House, to sollicite and engage his Interest, in order to the obtaining of a Reprieve for a Woman that past for one of their Wives, and was then under Condemnation, they chanced to spie the Maid a scowring a very considerable quantity of Plate, the glittering sight whereof so much affected them, that when they came back to Newgate , to give an account of their business, amongst other discourse, they mentioned what abundance of Plate they saw. And will you only see it? (says this Besse Longman , being by) then you deserve to starve indeed, when Fortune puts Booty, as it were, in your Mouths, and you are such Cowards, that you dare not take it: With these and many other words to that purpose, she animated them on so far, till by her Instigation and the Devils together, they resolved upon the Villany, and accordingly went the next Night, broke open the Gentlemans House, and took thence a great quantity of Plate: But upon description and search, A. M: was taken next Morning on saffron-hill , with a Silver Ladle, a Silver Porringer, and that famous Engine of Wickedness, called Betty. He was carried for the present to New prison , and there kept till he had discovered the othe. Parties; and upon his ingenu u Confession obtained the Mercy of a Repeve from that Execution, which his Fellow Criminals now suffer'd. The other person executed, was Henry Sea brooke : He was condemned the former Sessions for robbing the Merchant at Dukes Place ; but upon his pretending to discover the rest of the Cabal, and other great matters, was kept from the Gibbet all this, while; but now failing to verifie those pretentions, he was ordered by the Court to receive his punishment according to his former Sentence, with the resof the Prisoners condemned this Sessions. Of these poor wretches, two, viz Wall and Russell, as they ingenuously pleaded guilty to their Indictment at the Bar, so they behaved themselves very modestly at their Condemnation; and afterwards in Prison when Ministers' came to visit and discourse with them, in order to their Souls everlasting good, they received them with great expressions of joy and este, attending with much reverence and seeming heed to their Spiritual Instruction, who with most necessary and importunate Exhortations pressed them to a speedy and hearty Repentance, Since it stood them so much in hand, being upon the brink of Eternity, they told them, Their Condition was sad, as being justly sentenced by Men to a temporal Death; but that was infinitely short of being condemned by God, and suffering Eternal Death under the ury of his Wrath: that though it was vin for them to flatter themselves with hopes of onger life in this world, yet there were 
means est to secure them of Everlasting Life in the ext: and that to such vile sinners as they nd been, it was an unspeakable Mercy, that hey had yet a little space left them, wherein make their peace with Heaven; and what ould the damned Souls, weltring without pe in Eternal Flames, give or do for such a recious opportunity? With such and many her pious Admonitions and Prescriptions did ese Spiritual Physicians endeavour to cure e Ulcers of their Souls, and excite them to row off the peccant matter, and wash away i Iniquities with tears of a sincere Repennce, proceeding not from a sense of approa- ching Punishment, but of trouble for the Evil itself, and their provoking of God thereby. To all which they gave very great attention, promising to put that blessed Advice in practice; and so continued in a very serious and laudable frame till the time of Execution, which was the 17May, being then conducted to Tyburn with vest numbers of people following the Carts to behold the last 
sad Scene of their deplorable Tragedy. Being come to the Gallows, and the usual Prayers and Solemnities being performed, one of them spoke a pretty while to the Multitude, protesting, This was the first Face that he was ever actually guilty of, though he had been accessary to divers others, and had been all his days a very ill Liver; so that he could not but acknowledge that he suffer'd justly. He very much admonish'd all persons to consider their ways; especially warning Youth not to misspend their time in Idleness, or Disobedience to Parents or Masters; and to have a care of being seduced and drawn away by led women. affirming that such Courses and their Temptations, and to satisfie their Luxury, had been originally the cause of his destruction, and that shameful death he was now going to suffer. The rest said very few words, unless to some particular Acquaintance; but by their Gestures seemed to pray secretly, and so were all Executed according to Sentence.", 
'places': ['TYBURN', 'TYBURN', 'Newgate', 'Virginia', 'England', 'Newgate', 'Newgate', 'Newgate', 'saffron-hill', 'New prison', 'Dukes Place', 'Tyburn'], 
'type': 'OA', 
'persons': ['Henry Seabrook', 'Elizabeth Longman', 'Robert Scot', 'Edward Wall', 'Edward Russell', 'Henry Seabrook', 'Elizabeth Longman', 'Robert Scot', 'Edward Wall', 'Edward Russell', 'Elizabeth Longman', 'Edward Wall', 'Edward Russel', 'Besse Longman', 'Henry Sea brooke'], 
'date': '16760517'}
```

### Data Fields

- `id`: A unique identifier for the data point (in this case, a trial)
- `text`: The text of the proceeding
- `places`: The places mentioned in the text
- `type`: This can be either 'OA' or 'OBP'. OA is "Ordinary's Accounts" and OBP is "Sessions Proceedings"
- `persons`: The persons named in the text
- `date`: The date of the text

### Data Splits
This dataset only contains a single split:

Train: `2638` examples

## Dataset Creation

### Curation Rationale

Between 1674 and 1913 the Proceedings of the Central Criminal Court in London, the Old Bailey, were published eight times a year. These records detail 197,000 individual trials and contain 127 million words in 182,000 pages. They represent the largest single source of information about non-elite lives and behaviour ever published and provide a wealth of detail about everyday life, as well as valuable systematic evidence of the circumstances surrounding the crimes and lives of victims and the accused, and their trial outcomes. This project created a fully digitised and structured version of all surviving published trial accounts between 1674 and 1913, and made them available as a searchable online resource.

### Source Data

#### Initial Data Collection and Normalization

Starting with microfilms of the original Proceedings and Ordinary's Accounts, page images were scanned to create high definition, 400dpi TIFF files, from which GIF and JPEG files have been created for transmission over the internet. The uncompressed TIFF files will be preserved for archival purposes and should eventually be accessible over the web once data transmission speeds improve. A GIF format has been used to transmit image files for the Proceedings published between 1674 and 1834. 

#### Who are the source language producers?

The text of the 1674 to October 1834 Proceedings was manually typed by the process known as "double rekeying", whereby the text is typed in twice, by two different typists. Then the two transcriptions are compared by computer. Differences are identified and then resolved manually. This process was also used to create a transcription of the Ordinary's Accounts. This process means this text data contains fewer errors than many historical text corpora produced using Optical Character Recognition. 

### Annotations

#### Annotation process

The markup was done by a combination of automated and manual processes.

Most of the 1674 to October 1834 markup was done manually by a team of five data developers working at the Humanities Research Institute at the University of Sheffield (see project staff).

However, person names were tagged using an automated markup programme, GATE, developed by the Department of Computer Science at the University of Sheffield and specially customised to process the text of the Proceedings. Most of the 1674-1834 trial proceedings were run through GATE, which was able to identify approximately 80-90% of the names in the text. GATE was asked only to identify names where both a forename (not just an initial) and surname were given. The names not identified by this programme were not regularly marked up manually unless they were the names of defendants or victims.

The November 1834 to 1913 text was first run through an automated markup process. This process was carried out by the Digital Humanities Institute Sheffield.

Remaining markup, including checking of the results of the automated markup, was carried out by a team of eight data developers employed by the University of Hertfordshire (see project staff).

#### Who are the annotators?

- The directors of this project, and authors of all the historical background pages, are Professor Clive Emsley (Open University), Professor Tim Hitchcock (University of Sussex) and Professor Robert Shoemaker (University of Sheffield).
- The Project Manager is Dr Sharon Howard.
- The technical officer responsible for programming the search engines is Jamie McLaughlin.
- The Senior Data Developer, in charge of all the tagging procedures, was Dr Philippa Hardman.
- The other Data Developers were Anna Bayman, Eilidh Garrett, Carol Lewis-Roylance, Susan Parkinson, Anna Simmons, Gwen Smithson, Nicola Wilcox, and Catherine Wright.
- The London researcher was Mary Clayton.
- The technical officers responsible for the automated markup were Ed MacKenzie and Katherine Rogers.
- Project staff who worked on the 1674-1834 phase of the project include Dr Louise Henson (Senior Data Developer), Dr John Black, Dr Edwina Newman, Kay O'Flaherty, and Gwen Smithson.

### Personal and Sensitive Information

-This dataset contains personal information of people involved in criminal proceedings during the time period

## Considerations for Using the Data

### Social Impact of Dataset

[Needs More Information]

### Discussion of Biases

- "Virtually every aspect of English life between 1674 and 1913 was influenced by gender, and this includes behaviour documented in the Old Bailey Proceedings. Long-held views about the particular strengths, weaknesses, and appropriate responsibilities of each sex shaped everyday lives, patterns of crime, and responses to crime." This dataset contains text that adheres to those stereotypes.
- "The make-up of London's population changed and changed again during the course of the two and a half centuries after 1674. European Protestant refugees, blacks discharged from the armies of a growing empire, and Jews from Spain and Eastern Europe, Irish men and women, Lascars and political refugees from the revolutions of the nineteenth century contributed to the ragout of communities that made up this world city. Information about all these communities, and several more besides, can be found in the Proceedings"

### Other Known Limitations

 




## Additional Information

### Dataset Curators

- The directors of this project, and authors of all the historical background pages, are Professor Clive Emsley (Open University), Professor Tim Hitchcock (University of Sussex) and Professor Robert Shoemaker (University of Sheffield).
- The Project Manager is Dr Sharon Howard.
- The technical officer responsible for programming the search engines is Jamie McLaughlin.
- The Senior Data Developer, in charge of all the tagging procedures, was Dr Philippa Hardman.
- The other Data Developers were Anna Bayman, Eilidh Garrett, Carol Lewis-Roylance, Susan Parkinson, Anna Simmons, Gwen Smithson, - Nicola Wilcox, and Catherine Wright.

### Licensing Information

[CC-NY-04](https://creativecommons.org/licenses/by/4.0/)

### Citation Information

@article{Howard2017,
author = "Sharon Howard",
title = "{Old Bailey Online XML Data}",
year = "2017",
month = "4",
url = "https://figshare.shef.ac.uk/articles/dataset/Old_Bailey_Online_XML_Data/4775434",
doi = "10.15131/shef.data.4775434.v2"
}

Thanks to [@shamikbose](https://github.com/shamikbose) for adding this dataset.