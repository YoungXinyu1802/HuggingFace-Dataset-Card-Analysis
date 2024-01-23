---
task_categories:
- text-classification

---
# AutoTrain Dataset for project: real-vs-fake-news

## Dataset Description

This dataset has been automatically processed by AutoTrain for project real-vs-fake-news.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "feat_title": "FBI Russia probe helped by Australian diplomat tip-off: NYT",
    "text": "WASHINGTON (Reuters) - Trump campaign adviser George Papadopoulos told an Australian diplomat in May 2016 that Russia had political dirt on Democratic presidential candidate Hillary Clinton, the New York Times reported on Saturday. The conversation between Papadopoulos and the diplomat, Alexander Downer, in London was a driving factor behind the FBI\u2019s decision to open a counter-intelligence investigation of Moscow\u2019s contacts with the Trump campaign, the Times reported. Two months after the meeting, Australian officials passed the information that came from Papadopoulos to their American counterparts when leaked Democratic emails began appearing online, according to the newspaper, which cited four current and former U.S. and foreign officials. Besides the information from the Australians, the probe by the Federal Bureau of Investigation was also propelled by intelligence from other friendly governments, including the British and Dutch, the Times said. Papadopoulos, a Chicago-based international energy lawyer, pleaded guilty on Oct. 30 to lying to FBI agents about contacts with people who claimed to have ties to top Russian officials. It was the first criminal charge alleging links between the Trump campaign and Russia. The White House has played down the former aide\u2019s campaign role, saying it was \u201cextremely limited\u201d and that any actions he took would have been on his own. The New York Times, however, reported that Papadopoulos helped set up a meeting between then-candidate Donald Trump and Egyptian President Abdel Fattah al-Sisi and edited the outline of Trump\u2019s first major foreign policy speech in April 2016. The federal investigation, which is now being led by Special Counsel Robert Mueller, has hung over Trump\u2019s White House since he took office almost a year ago. Some Trump allies have recently accused Mueller\u2019s team of being biased against the Republican president. Lawyers for Papadopoulos did not immediately respond to requests by Reuters for comment. Mueller\u2019s office declined to comment. Trump\u2019s White House attorney, Ty Cobb, declined to comment on the New York Times report. \u201cOut of respect for the special counsel and his process, we are not commenting on matters such as this,\u201d he said in a statement. Mueller has charged four Trump associates, including Papadopoulos, in his investigation. Russia has denied interfering in the U.S. election and Trump has said there was no collusion between his campaign and Moscow. ",
    "feat_subject": "politicsNews",
    "feat_date": "December 30, 2017 ",
    "target": 1
  },
  {
    "feat_title": "Democrats ride grassroots wave to major statehouse gains",
    "text": "(Reuters) - Democrats claimed historic gains in Virginia\u2019s statehouse and booted Republicans from state and local office across the United States on Tuesday, in the party\u2019s first big wave of victories since Republican Donald Trump\u2019s won the White House a year ago. Democrats must figure out how to turn that momentum to their  advantage in November 2018 elections, when control of the U.S. Congress and scores of statehouses will be at stake. From coast to coast, Democratic victories showed grassroots resistance to Trump rallying the party\u2019s base, while independent and conservative voters appeared frustrated with the unpopular Republican leadership in Washington.  Democrats won this year\u2019s races for governor in Virginia and New Jersey, but successes in legislative and local races nationwide may have revealed more about where the party stands a year into Trump\u2019s administration. Unexpectedly massive Democratic gains in Virginia\u2019s statehouse surprised even the most optimistic party loyalists in a state that has trended Democratic in recent years but remains a top target for both parties in national elections.  \u201cThis is beyond our wildest expectations, to be honest,\u201d said Catherine Vaughan, co-founder of Flippable, one of several new startup progressive groups rebuilding the party at the grassroots level. With several races still too close to call, Democrats were close to flipping, or splitting, control of the Virginia House of Delegates, erasing overnight a two-to-one Republican majority. Democratic Lieutenant Governor Ralph Northam also defeated Republican Ed Gillespie by nearly nine percentage points in what had seemed a closer contest for Virginia\u2019s governor\u2019s mansion, a year after Democrat Hillary Clinton carried the state by five points in the presidential election. The losing candidate had employed Trump-style campaign tactics that highlighted divisive issues such as immigration, although the president did not join him on the campaign trail. In New Jersey, a Democratic presidential stronghold, voters replaced a two-term Republican governor with a Democrat and increased the party\u2019s majorities in the state legislature. Democrats notched additional wins in a Washington state Senate race that gave the party full control of the state government and in Republican-controlled Georgia, where Democrats picked up three seats in special state legislative elections. \u201cThis was the first chance that the voters got to send a message to Donald Trump and they took advantage of it,\u201d John Feehery, a Republican strategist in Washington, said by phone. The gains suggested to some election analysts that Democrats could retake the U.S. House of Representatives next year. Republicans control both the House and Senate along with the White House. Dave Wasserman, who analyzes U.S. House and statehouse races for the nonpartisan Cook Political Report, called the Virginia results a \u201ctidal wave.\u201d Even after Tuesday\u2019s gains, however, Democrats are completely locked out of power in 26 state governments. Republicans control two-thirds of U.S. legislative chambers. Desperate to rebuild, national Democrats this year showed newfound interest in legislative contests and races even farther down the ballot. The Democratic National Committee successfully invested in mayoral races from St. Petersburg, Florida, to Manchester, New Hampshire. \u201cIf there is a lesson to be taken from yesterday, it is that we need to make sure that we are competing everywhere, because Democrats can win,\u201d DNC Chairman Tom Perez said on a media call. Democratic Legislative Campaign Committee executive director Jessica Post said national party leaders must remain focused on local races, even in a congressional year. \u201cWe don\u2019t focus enough on the state level, and that is why we are in the place we are,\u201d she said. \u201cBut when we do, we win.\u201d ",
    "feat_subject": "politicsNews",
    "feat_date": "November 8, 2017 ",
    "target": 1
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "feat_title": "Value(dtype='string', id=None)",
  "text": "Value(dtype='string', id=None)",
  "feat_subject": "Value(dtype='string', id=None)",
  "feat_date": "Value(dtype='string', id=None)",
  "target": "ClassLabel(names=['Fake', 'True'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 1598 |
| valid        | 400 |
