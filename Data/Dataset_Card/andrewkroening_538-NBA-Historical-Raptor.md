---
license: cc
---
## Dataset Overview

### Intro

This dataset was downloaded from the good folks at fivethirtyeight. You can find the original (or in the future, updated) versions of this and several similar datasets at [this GitHub link.](https://github.com/fivethirtyeight/data/tree/master/nba-raptor)


### Data layout

Here are the columns in this dataset, which contains data on every NBA player, broken out by season, since the 1976 NBA-ABA merger:

Column | Description
-------|---------------
`player_name` |	Player name
`player_id` |	Basketball-Reference.com player ID
`season` |	Season
`season_type` |	Regular season (RS) or playoff (PO)
`team` |	Basketball-Reference ID of team
`poss` |	Possessions played
`mp` |	Minutes played
`raptor_box_offense` |	Points above average per 100 possessions added by player on offense, based only on box score estimate
`raptor_box_defense` |	Points above average per 100 possessions added by player on defense, based only on box score estimate
`raptor_box_total` |	Points above average per 100 possessions added by player, based only on box score estimate
`raptor_onoff_offense` |	Points above average per 100 possessions added by player on offense, based only on plus-minus data
`raptor_onoff_defense` |	Points above average per 100 possessions added by player on defense, based only on plus-minus data
`raptor_onoff_total` |	Points above average per 100 possessions added by player, based only on plus-minus data
`raptor_offense` |	Points above average per 100 possessions added by player on offense, using both box and on-off components
`raptor_defense` |	Points above average per 100 possessions added by player on defense, using both box and on-off components
`raptor_total` |	Points above average per 100 possessions added by player on both offense and defense, using both box and on-off components
`war_total` |	Wins Above Replacement between regular season and playoffs
`war_reg_season` |	Wins Above Replacement for regular season
`war_playoffs` |	Wins Above Replacement for playoffs
`predator_offense` |	Predictive points above average per 100 possessions added by player on offense
`predator_defense` |	Predictive points above average per 100 possessions added by player on defense
`predator_total` |	Predictive points above average per 100 possessions added by player on both offense and defense
`pace_impact` |	Player impact on team possessions per 48 minutes


### More information

This dataset was put together for Hugging Face by this guy: [Andrew Kroening](https://github.com/andrewkroening)

He was building some kind of a silly tool using this dataset. It's an NBA WAR Predictor tool, and you can find the Gradio interface [here.](https://huggingface.co/spaces/andrewkroening/nba-war-predictor) The GitHub repo can be found [here.](https://github.com/andrewkroening/nba-war-predictor-tool)