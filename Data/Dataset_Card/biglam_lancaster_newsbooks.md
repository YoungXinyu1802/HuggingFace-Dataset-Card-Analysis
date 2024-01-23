---
annotations_creators:
- no-annotation
paperswithcode_id: null
language:
- en
language_creators:
- expert-generated
license:
- cc-by-sa-3.0
multilinguality:
- monolingual
pretty_name: Lancaster Newsbooks
size_categories:
- n<1K
source_datasets:
- original
tags:
- newsbooks
- '1654'
- lancaster
- oxford text
task_categories: []
task_ids: []
---
# Dataset Card for lancaster_newsbooks

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

- **Homepage:** https://ota.bodleian.ox.ac.uk/repository/xmlui/handle/20.500.12024/2531
- **Repository:** [Needs More Information]
- **Paper:** [Needs More Information]
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** Tony McEnery

### Dataset Summary

This corpus consists of two collections of seventeenth-century English "newsbooks". Both were drawn from the Thomason Tracts collection, which is held at the British Library and available in graphical form via Early English Books Online (EEBO). The construction of these keyboarded versions were in both cases funded by the British Academy.

The FIRST collection (1654_newsbooks) consists of every newsbook published in London and still surviving in the Thomason Tracts from the first half of 1654 (to be precise, for the second half of December 1653 to the end of May 1654, with one or two additions from the first week in June, 1654). This was constructed for the project "Looking at text re-use in a corpus of seventeenth-century news reportage", funded by the British Academy, grant reference SG-33825. 

The SECOND collection (mercurius_fumigosus) consists of every surviving issue published of the highly idiosyncratic newsbook "Mercurius Fumigosus", written by John Crouch between summer 1654 and early autumn 1655. This was constructed for the project "Decoding the news - Mercurius Fumigosus as a source of news in the interregnum, 1654-1655", funded by the British Academy, grant reference LRG-35423. 

This is version 1.0 of the corpus, released April 2007; it supercedes earlier versions circulated informally.

For more information about the corpus, see www.ling.lancs.ac.uk/newsbooks

### Supported Tasks and Leaderboards

`text-classification`: This dataset can be used to augent existing datasets to find stylistic differences between texts from different time periods

### Languages

The language in this dataset is English from 1654. The associated BCP-47 code is `en:GB`

## Dataset Structure

### Data Instances

```
{
'id': 'PerfAcc170', 
'text': "Another late fight in Scotland, betwixt Col. Morgan and the Highlanders; with the number that were slain and taken Prisoners. The removing of Lieut. Col. John Lilburn from the Tower of London. The readiness of our Fleet for new action, though Peace be agreed on with Holland and Denmark. The taking of several more Prizes at sea. An Order of the Commissioners for the Trial and Approbation of public Preachers. Several proceedings of His Highness the Lord Protector and his Council, and another Ordinance touching 
the adjourning of the Term. Together with variety of choice Intelligence from several Foreign parts. From Wednesday APRIL 5 TO Wednesday April 12. 1654. Many Addresses were made to his Highness the Lord Protector, in the name of the City and County of York, and other places, wherein they acknowledge the great blessing of God to this Nation, that they have so great, so good and able a Protector. This day the Sessions began in the Old Bailey, and one of those that committed the late Robbery on Black-Heath, being called to his Trial, he refused to plead; but more  hereafter. This evening about 9 of the Clock, the Dutch Ambassadors signed and sealed the Ratification of the Articles of Peace so long spoken of; so did likewise the Commissioners appointed to treat with them by his Highness the Lord Protector. Paris April 11, 1654. The Cardinal de Retz being removed from Vincennes by the Marshal de la Mesteray, is now safe arrived at Nantes, and put into the Castle. The Court Emissaries give out that he is not to be long there, but in a few days to be set at liberty, only that his Majesty desireth satisfaction upon some certain points, although the main drift is to make him surrender his place of Archbishop of this City. The Commissioners of Languedoc cannot yet prevail in anything upon their Complaints, but are like the Commissioners of Catalonia, who hitherto have prevailed no further than to receive many fair words, but nothing effectual, the main work now in hand, is to find monies speedily for the setting forth of the Army, that they may be in the field as soon as may be, and to that end the Partisans are not wanting to find out new ways for exacting of monies, preferring large sums to be put into the King's Coffers, the difficulty lieth only in the effecting of it, by reason that the Country is in most places so exhausted of monies, that they are scarce able to live: The design for the King's Coronation is now on foot again, and if I am rightly informed, it will be done about the middle of May next, which being done, his Majesty shall go upon the borders and down to Picardy to forward his Army in their Action, so much the rather, by reason 
that the Prince of Conde, whom we hear was last week at Valenciennes, and then taking a view of his Army, is returned to Bruxels, there to confer with the Archduke Leopoldus for to obtain money and other necessaries for the march of his Army, that so they may fall to action as soon as the weather and season will give them leave, his Lady and son are still at Rocroy, where they are expecting some alteration to their present condition. The Earl of Harcourt hath not yet received any answer from the Court upon those proposals which he lately 
sent to the Court. We have news, that the Duke Francis hath at last accepted the command of his Brother the Duke of Lorrain's Army, and is expected there in a few days, which our Cardinal doth very well relish. The forces that were in the Country of Liege are now marching homewards, and are to be quartered in Lorrain. The great preparation for an Armado to go from Marseilles and Touloon, is much at a stand, only there are lately 5 men of War gone to Sea, and 3 more are to follow, but upon no design than to rob and plunder upon the sea, sparing scarce any they encounter, whether they be friends or foes. This day his Highness the Lord Protector and his Council, passed an Ordinance for adjourning of Easter Term, from and after the first Return thereof, called Quindena Pasch, until the first Return of Trinity Term, called Crastino Trinatatis. Dalkieth, April 3. Cap. Sherwin Commander of the Primrose, and Cap. Smith Commander of the Duchess, in their return from Orkney, took a Dutch vessel laden with French and Spanish Wines, linen Cloth, and other good commodities, bound for 
the West Indies; they sent her into Aberdeen. Some young Lairds and others purposing to glean a party of horse in Lothian, and repair to the enemy, are taken, and brought hither prisoners. Aberdeen, April 1. The Earl of Athol is come to Glencarn with about 700 horse and foot, Seaford and some new raised forces are daily expected to join with them. Glencarn with his whole force, consisting of 2000 horse and foot, is at Dingwel, two miles from Brahan, not undeserving the name of an Island, so that we hope to engage them there. In order whereunto Lieut. Col. Mitchell is marched towards Inverness with 9 companies of Foot, and Col. Morgan hath followed him with 5 troops of Col Rich his Regiment, and 4 troops of Dragoons; he intends to take Col. Tomlinson's Regiment, which is in his way, and to draw 5 companies of Foot out of Inverness. From Cows in the Isle of Wight, April 6. A private man of War hath, about two days since, taken and brought in hither two French vessels, one of which is laden with Salt, the other hath but little except ballast; Our Fleet is for the most part near St. Helens point and the rest as the Spits head, being in all near 100 sail, gallant ships, and bravely accommodated. One of our Frigates hath taken a Holland ship, and carried her to Portsmouth; she hath in her 8 Bales of Paper, and some small quantity of Indico. Many ships that were here, went away yesterday morning towards the Downs; and several Merchants' ships are at present here in this road, being detained by contrary winds; they expect some favourable Easterly gales, that so they may proceed on their intended voyages. Deal, April 7. A man of War of ours is this morning gone for Holland, to get the Ratification of the Peace made with them, and an Express from the Dutch Ambassador, touching the Agreement. Most part of the ships which remained in this Road, are gone up into the River of Thames; here is only some few left that are bound to the Southward. A Fleet consisting of about 40 or 50 sail of ships, great and small, passed by this place, which we suppose to be the Dunkirk fleet bound for London. Because many will not give credit to the Agreement of Peace between the Commonwealths of England and Holland, (though their Unbelief proceeds from several causes, some prejudicately fearing the worst, and others wishing and desiring rather than the Fountain of Blood may still be open) We can, and do assure you, That the Articles (as 
we said before) were signed and sealed by the Commissioners on both sides, on Wednesday night last, and within 14 days are to be signed and sealed by the Lord Protector, and the States of Holland, and then to publicly proclaimed and published, both in England and Holland 
in one day. The Agreement with Denmark is also taken in upon the Articles: And for satisfaction of the loss which our English Merchants sustained by that King's command, whose demands amount to about 150000l. it is referred to four Merchants, two whereof to be English, and the other two Dutch; which four Merchants shall have absolute power to determine those demands within the space of twenty days; the place where they are to sit, is Guildhall. As touching the business of Amboyna, it is referred to eight Commissioners, who have six months time to agree thereon, and in case they agree not, then Umpires are nominated to determine that business. Let those that delight themselves in blood, have blood to drink, for they are worthy. From Legorn, March 23. thus. This week in the sight of this City was a sore fight between two ships at Sea, the one Dutchman of War of 32 guns, and the other an English ship called the Expedition, who came from Zant with Currans; the fight lasted 6 hours, but night having parted them, both ships sunk; most of the men were saved, but nothing else, though the fight was near the shore. It is advertised from Cullen, That the Treaty between that Elector and the Spanish Commissioners, is brought to perfection, and signed, which is, That both French and Spanish shall have free passage through the Country of Liege, not committing any acts of hostility upon each other; and the Spaniards in point of satisfaction for the losses received from them and the Lorrainers, shall pay to the said Elector 200000 Rixdollars out of the Duke of Lorrain's estate, and for security of performance, the Lordship of Kerpen, and another in Gulick shall be put into his hands until full payment. From Poland thus. The General of the Cossacks hath delivered up three very considerable places to the Muscovite, and caused himself to be re baptized after the Muscovia manner, which is so 
ill resented by all sorts of people in that Country, that the Commanders sent to the King of Poland, That if he pleased to send them a general pardon for what they had done, and the rest of the Army, they will return with the major part of the Army into his Majesty's service; which hath so incensed the General, that having caused them to be apprehended he hath made each of them shorter by the head, which hath caused much heart burning among the people. Whereas many abuses and corruptions are crept into the ordinary course and administration of Justice, both in Law and Equity, the reformation whereof hath not yet been attained; Out of a tender care and desire that so necessary and good a work may at length be brought to effect, it is held convenient that so necessary and good a work may at length be brought to effect, it is held convenient that so necessary and good a work may at length be brought to effect, it is held convenient and necessary to adjourn part of the next Term of Easter; be if therefore Ordained by his Highness the Lord Protector, by and with the consent of his Council, That part of the said Term of Easter now next coming be adjourned, that is to say, from and after the first Return, called Quindena Pasch, unto the last Return of the said Easter Term, called Crastino Ascensionis; And all and every person or persons, which have cause, or commandment to appear in any of the Courts at Westminster, in or at any day or time, from and after the said Return, called Quindena Pasch, may tarry at their dwellings, or where their business shall lie, without resorting to any of the said Courts for that 
Cause, until the said last Return, called Crastino Ascensionis, without danger or forfeiture, penalty or contempt to be in that behalf. And be it also ordained by the Authority aforesaid, That Writs of Adjournment shall be directed to the Justices of the said Courts, and 
Barons of the Exchequer, giving them authority to adjourn the said part of the said Term of Easter, as aforesaid, that is to say, from and after the said first Return called Quindena Pasch, until the said last Return of the said Term, called Crastino Ascensionis, as before is said, and the said adjournment shall be made, as aforesaid. And be it further Ordained, That all Matters, Causes and Suits, depending in any of the said Courts, shall have continuance, and the parties shall have day, from the day of the said Adjournment, until the said Return of Crastino Ascensionis, as is aforesaid; and the Lord's Commissioners of the Great Seal are required to issue forth Writs accordingly. And be it further Ordained, That a former Ordinance of the sixth day of this instant April, for the Adjourning of part of the 
said Term, until the first Return of Trinity Term next, called Crastino Trinitatis, be from henceforth Repealed and void. And it is lastly Ordained by the Authority aforesaid, That the Sheriffs of London and Middlesex, and all other Sheriffs both in England and Wales, do 
forthwith proclaim and publish this Ordinance in the chief Market Towns and usual places within their several and respective Counties. Lieutenant Colonel John Lilburn being said to have again attempted something against the State, is removed from the Tower to be prisoner 
in some more remote place. The titular King of Scots is still at Paris, and of late something more merry than ordinary. The Deputies for Languedoc telling him, that if there were a Peace concluded with England, it would be well for all the Protestants in France; He made answer that he was glad of it, for it would then be the better for himself. This day was the Gaol delivery; three were hanged, one whereof died most desperately, and going up the Cart, drank a health to the Devil's Majesty: One was pressed last Saturday, and being afterwards heard to groan, was carried down to the Press-yard again to have the execution dispatched. The Commissioners for Approbation of public Ministers, sate at Whitehall, and divers Certificates were presented unto them in behalf of several particular persons, for approbation; and in regard that none hereafter should out of carelessness of partiality set their hands to a Certificate for any person that hereafter should out of carelessness or partiality let their hands to a Certificate for any person that hereafter may be found unworthy to be admitted, and so become prejudicial to the Church of Christ, and frustrate the intentions of our Governors which made this Ordinance; the said Commissioners do earnestly beseech all whom it may concern (in the bowels of Christ) as they tender the honour of the great God 
himself, whose servants we all are, the prejudice of the souls of his people purchased by the blood of his Son, the advancement and propagation of his Gospel, through all the parts of this Land and Nation, whereunto we belong, so to lend assistance both of their fervent prayers, and due informations, that thereby the work may be carried on more prosperously, and the Commissioners more encouraged to attend it. Signed in the name, and at the request of the Commissioners for Approbation of public Preachers. By Francis Rouse, Io. Arrowsmith. 
William Goss. Stephen Marshall. The last Letters from Edinburgh speak of another Engagement betwixt Col. Morgan, and the Enemy; but they tell us not the particulars, only they say, that the Enemy is once more dispersed, and driven further up into the mountains, with the loss of about 200 men. The peace with Holland being concluded (as you heard before) our Merchants are lading of goods on shipboard, as fast as Lighters can be gotten to carry them where the ships ride at anchor. We likewise hear of the like preparations in Holland for transporting of goods of several sorts hither. And now all the rest of Europe are at a stand, or at leastwise stand gazing upon us, and begin to cast about with themselves, what action may be great and considerable enough for to be undertaken next by those great Fleets, which are as ready for action as any opportunity can be to offer itself. How they will be disposed of Time will discover. London, Printed by E. Alsop 1654.", 
'title': 'A Perfect Account, Issue 170'}
```

### Data Fields

```
{
"id": Unique identifier for that data point("string"),
"text": Text in that datapoint("string"),
"title": The title of the news article("string")
}
```

### Data Splits

Train: 303

## Dataset Creation

### Curation Rationale

The FIRST collection (1654_newsbooks) consists of every newsbook published in London and still surviving in the Thomason Tracts from the first half of 1654 (to be precise, for the second half of December 1653 to the end of May 1654, with one or two additions from the first week in June, 1654) and was constructed for the project "Looking at text re-use in a corpus of seventeenth-century news reportage", funded by the British Academy, grant reference SG-33825. 
The SECOND collection (mercurius_fumigosus) consists of every surviving issue published of the highly idiosyncratic newsbook "Mercurius Fumigosus", written by John Crouch between summer 1654 and early autumn 1655. This was constructed for the project "Decoding the news - Mercurius Fumigosus as a source of news in the interregnum, 1654-1655", funded by the British Academy, grant reference LRG-35423. 


### Source Data

#### Initial Data Collection and Normalization

This corpus was created by the Department of Linguistics and English Language, Lancaster University.

#### Who are the source language producers?

The original data was humna-generated from existing newsbooks

### Annotations

#### Annotation process

[N/A]

#### Who are the annotators?

[N/A]

### Personal and Sensitive Information

None, since this dataset is from 1654

## Considerations for Using the Data

### Social Impact of Dataset

This dataset provides an insight into the news and social systems from 17th century England

### Discussion of Biases

The dataset is from the 17th century and some articles might reflect social biases of the time in terms of sexuality, gender, race, etc.

### Other Known Limitations

[N/A]

## Additional Information

### Dataset Curators

This corpus was created by the Department of Linguistics and English Language, Lancaster University.

Project leader: Tony McEnery
Corpus editor:  Andrew Hardie

### Licensing Information

Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License

### Citation Information

 @misc{20.500.12024/2531,
 title = {The Lancaster Newsbooks Corpus},
 author = {Thomason, George, d. 1666},
 url = {http://hdl.handle.net/20.500.12024/2531},
 note = {Oxford Text Archive},
 copyright = {Distributed by the University of Oxford under a Creative Commons Attribution-{NonCommercial}-{ShareAlike} 3.0 Unported License.},
 year = {2005} }