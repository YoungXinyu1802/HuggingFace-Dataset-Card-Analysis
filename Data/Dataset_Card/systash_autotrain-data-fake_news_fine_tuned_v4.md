---
task_categories:
- text-classification

---
# AutoTrain Dataset for project: fake_news_fine_tuned_v4

## Dataset Description

This dataset has been automatically processed by AutoTrain for project fake_news_fine_tuned_v4.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "text": "Many of us do not share Donald Trump s past values  but we do love America  In my opinion  it is not about him  It is about     Who will preserve and a protect the constitution     Who will protect the second amendment     Who will not send your son or daughter into harms way unless there is a good reason     Who does not support partial birth abortion     Who wants to fix our inner cities and our infrastructure     Who will improve our economy and bring jobs back to the USA     Who is a nationalist and not a globalist     Who will protect our vets from dying in the streets and on park benches and get them help when they need it     Who supports our police  firemen  military men and women      Who will protect our borders from criminal elements and terrorist      Who will not leave Americans to die in foreign countries under the hands of terrorist      Who is now a professed Christian and changed man according to many Christian leaders and pastors  These are just a few reasons to vote for Donald Trump ",
    "target": 1
  },
  {
    "text": "Good morning   Here   s what you need to know      President Trump is expected to order the construction of a Mexican border wall today and slash immigration of refugees from    terror prone    nations  White House officials said  He pressed automakers to increase jobs in the U  S  but a new forecast of a federal budget deficit that could expand to almost     trillion over    years could complicate his agenda to cut taxes and ramp up spending  Mr  Trump also revived two pipelines blocked under President Obama  the Keystone XL pipeline  the focus of years of debate over energy needs and climate change and the Dakota Access pipeline  the target of Native American protests            And tensions are rising between the U  S  and China  Beijing  after a challenge from a Trump spokesman  insisted it had    irrefutable    sovereignty over disputed islands in the South China Sea  China sees opportunities to extend its global reach with Mr  Trump in power  but it also sees a threat to its prized goal  stability            Israel  discarding diplomatic restraint just a few days into the Trump administration  approved the construction of        housing units for Jews in West Bank settlements  A month ago  the Obama administration declined to veto a Security Council resolution condemning the settlements  and last week  a gathering of world leaders warned Israel to stop expanding them            The office of Prime Minister Theresa May pledged to stay on its timetable for taking Britain out of the European Union despite a top court ruling requiring the approval of Parliament before the process can begin  Political observers said it was unlikely that legislators  despite being largely opposed to Brexit  would try to block the will of the voters            Three months after Prime Minister Narendra Modi abruptly banned    percent of India   s currency in a bid to fight    black money           hidden reserves that feed corruption        unemployment is spreading  and some people are going without fruit  vegetables and milk     This has actually hurt the poor enormously     one business leader said  Above  a protest over cash shortages last week            And this year   s Oscar nominations are out  Voters gave    La La Land       nominations  a tie for the most in Academy Award history  The academy also honored six black actors        a record  Here is the full list of nominees            The Alibaba Group beat estimates with strong   earnings  The results showed how much the   giant        despite a growing global profile and its record I  P  O  on Wall Street        is still dependent on China      Silver Lake  an investment firm  is leading a       billion investment in Koubei  an   business that is part of what is increasingly known as the    sector  or O O      President Trump   s pick for the Federal Communications Commission  Ajit Pai  an   from Kansas  is expected to roll back rules that ban internet service providers from favoring certain websites and apps      Nearly     million Chinese citizens used their mobile phones to make payments last year  an increase of    percent from       new government data shows      Japan releases data on its imports and exports for December  The country   s   economy has been struggling despite government efforts at stimulus      South Korea and Taiwan release G  D  P  figures      Wall Street was up  Here   s a snapshot of global markets      China   s     nuclear plant  begun in the     s  was one of the country   s most ambitious military projects  Today  the   mountain has been reborn as a tourist attraction   The New York Times      Peter Thiel  the American billionaire  has taken New Zealand citizenship and quietly acquired a sprawling estate on Lake Wanaka   New Zealand Herald      Afghanistan ordered the arrest of nine bodyguards of Gen  Abdul Rashid Dostum  the more senior of the country   s two vice presidents  on accusations of the rape and torture of an Uzbek elder   The New York Times      A wave of smog is forecast to engulf four northern Chinese provinces as the Lunar New Year approaches   Reuters      Talks in Astana  Kazakhstan  may have done more to to firm up Russia   s growing role in diplomacy over Syria than to create any progress toward peace   The New York Times      A proposal to ban the display of Vietnam   s flag on city poles has divided the Vietnamese community of San Jose  Calif   The Mercury News      Gambia   s former president  Yahya Jammeh  didn   t go into exile in Equatorial Guinea    He left with two   a   and a plane full of luxury items   The New York Times      China   s government has shut down     of the country   s     golf courses since       citing illegal land or water use   Xinhua      Scientists found the fossils of a huge  nearly    otter that roamed rivers and lakes in southwestern China about      million years ago   Reuters      Doing just    minutes of yoga can improve your bone health      Vacations don   t have to be all about relaxing  Here   s how to plan one with some good deeds along the way      Recipe of the day  Try this grilled cheese sandwich featuring mayonnaise for some midweek comfort food      In China  members of the Tanka people have survived on southern coastal waterways  and on the margins of society  since ancient times  As big cities spread  their floating way of life is disappearing      Genetic research is taking some truly   turns  Ant researchers have identified the molecular and neural cues that help explain social behaviors  including caring for young  breeding        even capturing and   upstarts  like tiny police officers      And a pioneering scientist  Maria Sibylla Merian  captivated Europeans     years ago with her studies of insects  Now  her findings are being celebrated again  Grandstands filled with cheering fans  perfectly plated vegetables  and your country   s name on the line        this isn   t your typical cooking competition  This is the Bocuse d   Or  or the culinary version of the Olympics  The competition  which takes place this week in Lyon  France  was founded by the master French chef Paul Bocuse  He was influential in establishing nouvelle cuisine  which emphasizes ingredients and presentation  At     Mr  Bocuse remains a king among chefs  Long before          became a trendy concept  a    Bocuse was learning how to butcher a cow for his first restaurant job  He eventually joined his father at their family restaurant  L   Auberge du Pont de Collonges  One year after he took over  the restaurant won a Michelin star  He recalled how early in his career he wowed a prominent food critic with fresh ingredients  Mr  Bocuse served haricots verts picked that morning  lightly boiled and served with olive oil  shallots and salt  In       The Times   s Craig Claiborne described the restaurant outside of Lyon as    one of the most elegant and proudest restaurants outside of Paris      Mr  Bocuse  though  once offered a less refined assessment of his skills     Some men have mistresses     Mr  Bocuse once said     I run a luxury restaurant      Remy Tumin contributed reporting        Your Morning Briefing is published weekday mornings  What would you like to see here  Contact us at asiabriefing nytimes  com ",
    "target": 0
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "text": "Value(dtype='string', id=None)",
  "target": "ClassLabel(names=['0', '1'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 7998 |
| valid        | 2000 |
