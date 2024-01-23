---
license: mit
---
## Problem and Opportunity
In the United States, voting is largely a private matter. A registered voter is given a randomized ballot form or machine to prevent linkage between their voting choices and their identity. This disconnect supports confidence in the election process, but it provides obstacles to an election's analysis. A common solution is to field exit polls, interviewing voters immediately after leaving their polling location. This method is rife with bias, however, and functionally limited in direct demographics data collected. 

For the 2020 general election, though, most states published their election results for each voting location. These publications were additionally supported by the geographical areas assigned to each location, the voting precincts. As a result, geographic processing can now be applied to project precinct election results onto Census block groups. While precinct have few demographic traits directly, their geographies have characteristics that make them projectable onto U.S. Census geographies. Both state voting precincts and U.S. Census block groups:
* are exclusive, and do not overlap
* are adjacent, fully covering their corresponding state and potentially county
* have roughly the same size in area, population and voter presence

Analytically, a projection of local demographics does not allow conclusions about voters themselves. However, the dataset does allow statements related to the geographies that yield voting behavior. One could say, for example, that an area dominated by a particular voting pattern would have mean traits of age, race, income or household structure.

The dataset that results from this programming provides voting results allocated by Census block groups.  The block group identifier can be joined to Census Decennial and American Community Survey demographic estimates. 

