---
annotations_creators:
- none
language_creators:
- unknown
language:
- en
license:
- other
multilinguality:
- unknown
size_categories:
- unknown
source_datasets:
- original
task_categories:
- table-to-text
task_ids: []
pretty_name: mlb_data_to_text
tags:
- data-to-text
---

# Dataset Card for GEM/mlb_data_to_text

## Dataset Description

- **Homepage:** https://github.com/ratishsp/mlb-data-scripts
- **Repository:** https://github.com/ratishsp/mlb-data-scripts
- **Paper:** https://aclanthology.org/P19-1195
- **Leaderboard:** N/A
- **Point of Contact:** Ratish Puduppully

### Link to Main Data Card

You can find the main data card on the [GEM Website](https://gem-benchmark.com/data_cards/mlb_data_to_text).

### Dataset Summary 

The MLB dataset is an English sport-related data-to-text dataset in the baseball domain. The input is a large table with results of a game and the output is a description of the game.

You can load the dataset via:
```
import datasets
data = datasets.load_dataset('GEM/mlb_data_to_text')
```
The data loader can be found [here](https://huggingface.co/datasets/GEM/mlb_data_to_text).

#### website
[Github](https://github.com/ratishsp/mlb-data-scripts)

#### paper
[ACL Anthology](https://aclanthology.org/P19-1195)

#### authors
Ratish Puduppully, Li Dong, Mirella Lapata

## Dataset Overview

### Where to find the Data and its Documentation

#### Webpage

<!-- info: What is the webpage for the dataset (if it exists)? -->
<!-- scope: telescope -->
[Github](https://github.com/ratishsp/mlb-data-scripts)

#### Download

<!-- info: What is the link to where the original dataset is hosted? -->
<!-- scope: telescope -->
[Github](https://github.com/ratishsp/mlb-data-scripts)

#### Paper

<!-- info: What is the link to the paper describing the dataset (open access preferred)? -->
<!-- scope: telescope -->
[ACL Anthology](https://aclanthology.org/P19-1195)

#### BibTex

<!-- info: Provide the BibTex-formatted reference for the dataset. Please use the correct published version (ACL anthology, etc.) instead of google scholar created Bibtex. -->
<!-- scope: microscope -->
```
@inproceedings{puduppully-etal-2019-data,
    title = "Data-to-text Generation with Entity Modeling",
    author = "Puduppully, Ratish  and
      Dong, Li  and
      Lapata, Mirella",
    booktitle = "Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics",
    month = jul,
    year = "2019",
    address = "Florence, Italy",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/P19-1195",
    doi = "10.18653/v1/P19-1195",
    pages = "2023--2035",
}
```

#### Contact Name

<!-- quick -->
<!-- info: If known, provide the name of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
Ratish Puduppully

#### Contact Email

<!-- info: If known, provide the email of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
ratishpuduppully@gmail.com

#### Has a Leaderboard?

<!-- info: Does the dataset have an active leaderboard? -->
<!-- scope: telescope -->
no


### Languages and Intended Use

#### Multilingual?

<!-- quick -->
<!-- info: Is the dataset multilingual? -->
<!-- scope: telescope -->
no

#### Covered Languages

<!-- quick -->
<!-- info: What languages/dialects are covered in the dataset? -->
<!-- scope: telescope -->
`English`

#### License

<!-- quick -->
<!-- info: What is the license of the dataset? -->
<!-- scope: telescope -->
other: Other license

#### Intended Use

<!-- info: What is the intended use of the dataset? -->
<!-- scope: microscope -->
The dataset can be used to study data-to-text generation. The dataset is in sports domain. It pairs statistics of Major League Baseball (MLB) game with its summary. The summary is in the form of a document containing an average of 540 tokens. Thus it is useful to study long document generation.

#### Add. License Info

<!-- info: What is the 'other' license of the dataset? -->
<!-- scope: periscope -->
Restricted to non-commercial research purposes.

#### Primary Task

<!-- info: What primary task does the dataset support? -->
<!-- scope: telescope -->
Data-to-Text

#### Communicative Goal

<!-- quick -->
<!-- info: Provide a short description of the communicative goal of a model trained for this task on this dataset. -->
<!-- scope: periscope -->
Produce a summary of MLB game from its statistics. 


### Credit

#### Curation Organization Type(s)

<!-- info: In what kind of organization did the dataset curation happen? -->
<!-- scope: telescope -->
`academic`

#### Curation Organization(s)

<!-- info: Name the organization(s). -->
<!-- scope: periscope -->
University of Edinburgh

#### Dataset Creators

<!-- info: Who created the original dataset? List the people involved in collecting the dataset and their affiliation(s). -->
<!-- scope: microscope -->
Ratish Puduppully, Li Dong, Mirella Lapata


### Dataset Structure

#### Data Fields

<!-- info: List and describe the fields present in the dataset. -->
<!-- scope: telescope -->
```
        features = datasets.Features(
            {
                "home_name": datasets.Value("string"),
                "box_score": [
                    {
                        "p_l": datasets.Value("string"),
                        "last_name": datasets.Value("string"),
                        "p_h": datasets.Value("string"),
                        "sac": datasets.Value("string"),
                        "p_bb": datasets.Value("string"),
                        "pos": datasets.Value("string"),
                        "ao": datasets.Value("string"),
                        "p_bf": datasets.Value("string"),
                        "cs": datasets.Value("string"),
                        "hbp": datasets.Value("string"),
                        "ab": datasets.Value("string"),
                        "full_name": datasets.Value("string"),
                        "p_w": datasets.Value("string"),
                        "go": datasets.Value("string"),
                        "fldg": datasets.Value("string"),
                        "p_bs": datasets.Value("string"),
                        "avg": datasets.Value("string"),
                        "p_r": datasets.Value("string"),
                        "p_s": datasets.Value("string"),
                        "lob": datasets.Value("string"),
                        "first_name": datasets.Value("string"),
                        "p_sv": datasets.Value("string"),
                        "p_so": datasets.Value("string"),
                        "p_save": datasets.Value("string"),
                        "p_hr": datasets.Value("string"),
                        "po": datasets.Value("string"),
                        "p_ip1": datasets.Value("string"),
                        "p_ip2": datasets.Value("string"),
                        "bb": datasets.Value("string"),
                        "ops": datasets.Value("string"),
                        "p_hld": datasets.Value("string"),
                        "bo": datasets.Value("string"),
                        "p_loss": datasets.Value("string"),
                        "e": datasets.Value("string"),
                        "p_game_score": datasets.Value("string"),
                        "p_win": datasets.Value("string"),
                        "a": datasets.Value("string"),
                        "p_era": datasets.Value("string"),
                        "d": datasets.Value("string"),
                        "p_out": datasets.Value("string"),
                        "h": datasets.Value("string"),
                        "p_er": datasets.Value("string"),
                        "p_np": datasets.Value("string"),
                        "hr": datasets.Value("string"),
                        "r": datasets.Value("string"),
                        "so": datasets.Value("string"),
                        "t": datasets.Value("string"),
                        "rbi": datasets.Value("string"),
                        "team": datasets.Value("string"),
                        "sb": datasets.Value("string"),
                        "slg": datasets.Value("string"),
                        "sf": datasets.Value("string"),
                        "obp": datasets.Value("string"),
                    }
                ],
                "home_city": datasets.Value("string"),
                "vis_name": datasets.Value("string"),
                "play_by_play": [{
                    "top": [{
                        "runs": datasets.Value("string"),
                        "scorers": [
                            datasets.Value("string")
                        ],
                        "pitcher": datasets.Value("string"),
                        "o": datasets.Value("string"),
                        "b": datasets.Value("string"),
                        "s": datasets.Value("string"),
                        "batter": datasets.Value("string"),
                        "b1": [
                            datasets.Value("string")
                        ],
                        "b2": [
                            datasets.Value("string")
                        ],
                        "b3": [
                            datasets.Value("string")
                        ],
                        "event": datasets.Value("string"),
                        "event2": datasets.Value("string"),
                        "home_team_runs": datasets.Value("string"),
                        "away_team_runs": datasets.Value("string"),
                        "rbi": datasets.Value("string"),
                        "error_runs": datasets.Value("string"),
                        "fielder_error": datasets.Value("string")
                    }
                    ],
                    "bottom": [{
                        "runs": datasets.Value("string"),
                        "scorers": [
                            datasets.Value("string")
                        ],
                        "pitcher": datasets.Value("string"),
                        "o": datasets.Value("string"),
                        "b": datasets.Value("string"),
                        "s": datasets.Value("string"),
                        "batter": datasets.Value("string"),
                        "b1": [
                            datasets.Value("string")
                        ],
                        "b2": [
                            datasets.Value("string")
                        ],
                        "b3": [
                            datasets.Value("string")
                        ],
                        "event": datasets.Value("string"),
                        "event2": datasets.Value("string"),
                        "home_team_runs": datasets.Value("string"),
                        "away_team_runs": datasets.Value("string"),
                        "rbi": datasets.Value("string"),
                        "error_runs": datasets.Value("string"),
                        "fielder_error": datasets.Value("string")
                    }
                    ],
                    "inning": datasets.Value("string")
                }
                ],
                "vis_line": {
                    "innings": [{
                     "inn": datasets.Value("string"),
                     "runs": datasets.Value("string")
                    }
                    ],
                    "result": datasets.Value("string"),
                    "team_runs": datasets.Value("string"),
                    "team_hits": datasets.Value("string"),
                    "team_errors": datasets.Value("string"),
                    "team_name": datasets.Value("string"),
                    "team_city": datasets.Value("string")
                },
                "home_line": {
                    "innings": [{
                        "inn": datasets.Value("string"),
                        "runs": datasets.Value("string")
                    }
                    ],
                    "result": datasets.Value("string"),
                    "team_runs": datasets.Value("string"),
                    "team_hits": datasets.Value("string"),
                    "team_errors": datasets.Value("string"),
                    "team_name": datasets.Value("string"),
                    "team_city": datasets.Value("string")
                },
                "vis_city": datasets.Value("string"),
                "day": datasets.Value("string"),
                "summary": [
                    datasets.Value("string"),
                ],
                "gem_id": datasets.Value("string")
            }
```

#### Reason for Structure

<!-- info: How was the dataset structure determined? -->
<!-- scope: microscope -->
The high level structure contains the following attributes: home_name, vis_name, home_city, vis_city, summary, summary_eval, day, gem_id, box_score, play_by_play, home_line, vis_line.
The attributes home_name, vis_name, home_city, vis_city and day are string values.
The attribute "summary" contains the summary in the form of a list of tokens.
The attribute "summary_eval" contains the summary in the form of a string of tokens. The difference from "summary" field is that "summary_eval" doesn't contain "*NEWPARAGRAPH*" delimiters to separate the paragraphs. "summary_eval" field should be used to evaluate model outputs. "summary" field may be used during the training process.
box_score contains the box score statistics of the players in the game. It is in the form of a list (of average size 90), with each element describing the statistics of a player. The box score statistics contain 53 attributes. 
The description of the attributes is given below. The descriptions of most of the attributes is obtained from [mlb.com](https://www.mlb.com/glossary/standard-stats). 

- r :       Runs scored by a player in the game.                                                                                                                                                                                                                                                                                                                                                                                                                       
- rbi           Runs Batted In (RBI): action of a batter results in a run scored by other players in the team.                                                                                                                                                                                                                                                                                                                                                             
- pos           Position of the player.                                                                                                                                                                                                                                                                                                                                                                                                                                    
- avg           Batting Average. It is an indicator of the hits in the players' career.                                                                                                                                                                                                                                                                                                                                                                                    
- bb            A walk occurs when a pitcher throws four pitches out of the strike zone, none of which are swung at by the hitter.                                                                                                                                                                                                                                                                                                                                         
- hr            Batter hits the ball in the air over the outfield fence.                                                                                                                                                                                                                                                                                                                                                                                                   
- p_r           Runs given by a pitcher in the game.                                                                                                                                                                                                                                                                                                                                                                                                                       
- p_bb          Walks allowed by pitcher in a game.                                                                                                                                                                                                                                                                                                                                                                                                                        
- p_h           Hits allowed by pitcher in a game.                                                                                                                                                                                                                                                                                                                                                                                                                         
- p_hr          Home runs allowed by pitcher in a game.                                                                                                                                                                                                                                                                                                                                                                                                                    
- p_er          Earned Run (ER): An earned run is any run that scores against a pitcher.                                                                                                                                                                                                                                                                                                                                                                                   
- p_era         Earned Run Average (ERA): Earned run average represents the number of earned runs a pitcher allows per nine innings.                                                                                                                                                                                                                                                                                                                                       
- p_np          Number of Pitches: A pitcher's total number of pitches is determined by all the pitches he throws in game.                                                                                                                                                                                                                                                                                                                                                 
- p_ip1         Innings Pitched (IP1): Innings pitched measures the number of innings a pitcher remains in a game. Because there are three outs in an inning, each out recorded represents one-third of an inning pitched.                                                                                                                                                                                                                                                 
- p_ip2         Innings Pitched (IP2): Innings pitched measures the number of innings a pitcher remains in a game. Because there are three outs in an inning, each out recorded represents one-third of an inning pitched.                                                                                                                                                                                                                                                 
- p_w           A pitcher receives a win when he is the pitcher of record when his team takes the lead for good.                                                                                                                                                                                                                                                                                                                                                           
- p_l           A pitcher receives a loss when a run that is charged to him proves to be the go-ahead run in the game, giving the opposing team a lead it never gives up.                                                                                                                                                                                                                                                                                                  
- p_so          A strikeout occurs when a pitcher throws any combination of three swinging or looking strikes to a hitter.                                                                                                                                                                                                                                                                                                                                                 
- p_save        Save: A save is awarded to the relief pitcher who finishes a game for the winning team. A pitcher cannot receive a save and a win in the same game.                                                                                                                                                                                                                                                                                                        
- p_sv          Saves: The count of saves recorded by a pitcher in his career.                                                                                                                                                                                                                                                                                                                                                                                             
- sac           A sacrifice fly occurs when a batter hits a fly-ball out to the outfield or foul territory that allows a runner to score.                                                                                                                                                                                                                                                                                                                                  
- p_bf          Batters faced is simply a count of the number of total plate appearances against a certain pitcher or team. In a perfect game -- with 27 outs -- a pitcher will record 27 batters faced.                                                                                                                                                                                                                                                                   
- cs            A caught stealing occurs when a runner attempts to steal but is tagged out before reaching second base, third base or home plate.                                                                                                                                                                                                                                                                                                                          
- hbp           A hit-by-pitch occurs when a batter is struck by a pitched ball without swinging at it. He is awarded first base as a result.                                                                                                                                                                                                                                                                                                                              
- ab            An official at-bat comes when a batter reaches base via a fielder's choice, hit or an error (not including catcher's interference) or when a batter is put out on a non-sacrifice.                                                                                                                                                                                                                                                                         
- p_bs          A blown save occurs when a relief pitcher enters a game in a save situation, but allows the tying run to score.                                                                                                                                                                                                                                                                                                                                            
- p_s           The count of strikes thrown by a pitcher                                                                                                                                                                                                                                                                                                                                                                                                                   
- lob           Left on base can be viewed as both an individual statistic or as a team statistic. In an individual batter's case, it refers to how many men remain on base after that batter makes an out at the plate, as the batter has failed to do his job to score those runners -- or at least put himself in a position to score. In a team's case or in an individual pitcher's case, it refers to the number of men who remain on base at the end of an inning.  
- po            A fielder is credited with a putout when he is the fielder who physically records the act of completing an out -- whether it be by stepping on the base for a forceout, tagging a runner, catching a batted ball, or catching a third strike                                                                                                                                                                                                               
- ops           OPS adds on-base percentage and slugging percentage to get one number that unites the two. It's meant to combine how well a hitter can reach base, with how well he can hit for average and for power.                                                                                                                                                                                                                                                     
- p_hld         A hold occurs when a relief pitcher enters the game in a save situation and maintains his team's lead for the next relief pitcher, while recording at least one out.                                                                                                                                                                                                                                                                                       
- p_loss        True/False- Indicates losing pitcher                                                                                                                                                                                                                                                                                                                                                                                                                       
- e             A fielder is given an error if, in the judgment of the official scorer, he fails to convert an out on a play that an average fielder should have made.                                                                                                                                                                                                                                                                                                     
- p_win         True/False- Indicates winning pitcher                                                                                                                                                                                                                                                                                                                                                                                                                      
- a             An assist is awarded to a fielder who touches the ball before a putout is recorded by another fielder.                                                                                                                                                                                                                                                                                                                                                     
- h             A hit occurs when a batter strikes the baseball into fair territory and reaches base without doing so via an error or a fielder's choice.                                                                                                                                                                                                                                                                                                                  
- so            A strikeout of a batter                                                                                                                                                                                                                                                                                                                                                                                                                                    
- team          Team of the player                                                                                                                                                                                                                                                                                                                                                                                                                                         
- sb            A stolen base occurs when a baserunner advances by taking a base to which he isn't entitled.                                                                                                                                                                                                                                                                                                                                                               
- slg           Slugging percentage represents the total number of bases a player records per at-bat. Unlike on-base percentage, slugging percentage deals only with hits and does not include walks and hit-by-pitches in its equation.                                                                                                                                                                                                                                   
- sf            A sacrifice fly occurs when a batter hits a fly-ball out to the outfield or foul territory that allows a runner to score.                                                                                                                                                                                                                                                                                                                                  
- obp           OBP refers to how frequently a batter reaches base per plate appearance. Times on base include hits, walks and hit-by-pitches, but do not include errors, times reached on a fielder's choice or a dropped third strike.       

The description of attributes in play-by-play is below:

- batter             Batter in the play.                                                          
- pitcher            Pitcher in play.                                                             
- b1                 Player/s at first base position.                                             
- b2                 Player/s at second base position.                                            
- b3                 Player/s at third base position.                                             
- scorers            Player/s scored in the play.                                                 
- fielder_error      Player committed field error.                                                
- event              Event of the play such as single, double, home run etc.                      
- event2             Second event of the play such as wild pitch, error etc.                      
- inning             Inning of the play.                                                          
- top/ bottom        If home team is batting it is bottom and if away team is batting it is top.  
- o                  Count of outs                                                                
- b                  Count of balls                                                               
- s                  Count of strikes                                                             
- r                  Count of runs                                                                
- rbi                Count of runs batted in (rbi)                                                
- error_runs         Runs due to error                                                            
- home_team_runs     Score of home team                                                           
- vis_team_runs      Score of visiting team                                                       

`home_line` and `vis_line` contain string value pairs for `team_name`, `team_city`, `team_runs`, `team_hits`, `team_error`, `result`, and a list of runs scored in each inning.

#### Data Splits

<!-- info: Describe and name the splits in the dataset if there are more than one. -->
<!-- scope: periscope -->
There are three splits in the dataset: train, validation and test

#### Splitting Criteria

<!-- info: Describe any criteria for splitting the data, if used. If there are differences between the splits (e.g., if the training annotations are machine-generated and the dev and test ones are created by humans, or if different numbers of annotators contributed to each example), describe them here. -->
<!-- scope: microscope -->
The splits are random.



## Dataset in GEM

### Rationale for Inclusion in GEM

#### Why is the Dataset in GEM?

<!-- info: What does this dataset contribute toward better generation evaluation and why is it part of GEM? -->
<!-- scope: microscope -->
This dataset can verify if models are capable of long document generation. The challenges in long document generation conditioned on input tables include ensuring coherent output, staying faithful to the input, ensuring fluent output and avoiding repetition of text. Such aspects can be verified on models trained on this dataset

#### Similar Datasets

<!-- info: Do other datasets for the high level task exist? -->
<!-- scope: telescope -->
yes

#### Unique Language Coverage

<!-- info: Does this dataset cover other languages than other datasets for the same task? -->
<!-- scope: periscope -->
no

#### Difference from other GEM datasets

<!-- info: What else sets this dataset apart from other similar datasets in GEM? -->
<!-- scope: microscope -->
Compared to the existing RotoWire (Wiseman et al. 2017) dataset, MLB summaries are longer (approximately by 50%) and the input records are richer and more structured (with the addition of play-by-play). Moreover, the MLB dataset is five times larger in terms of data size (i.e., pairs of tables and game summaries).

#### Ability that the Dataset measures

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: periscope -->
Long document generation, coherent ordering of information, faithfulness to the input statistics, fluency in generation and avoiding repetition of text.


### GEM-Specific Curation

#### Modificatied for GEM?

<!-- info: Has the GEM version of the dataset been modified in any way (data, processing, splits) from the original curated data? -->
<!-- scope: telescope -->
yes

#### GEM Modifications

<!-- info: What changes have been made to he original dataset? -->
<!-- scope: periscope -->
`data points removed`

#### Modification Details

<!-- info: For each of these changes, described them in more details and provided the intended purpose of the modification -->
<!-- scope: microscope -->
Some examples have been removed from training dataset which satisfied the below criteria:
1. The examples in training dataset which overlapped with validation/test.
2. Some examples which described washed out games. 



#### Additional Splits?

<!-- info: Does GEM provide additional splits to the dataset? -->
<!-- scope: telescope -->
no


### Getting Started with the Task

#### Pointers to Resources

<!-- info: Getting started with in-depth research on the task. Add relevant pointers to resources that researchers can consult when they want to get started digging deeper into the task. -->
<!-- scope: microscope -->
The [research paper](https://aclanthology.org/P19-1195) is a good resource



## Previous Results

### Previous Results

#### Measured Model Abilities

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: telescope -->
Automatic evaluation measure can evaluate the factuality, content selection, content ordering and the fluency of the model output. The factuality, content selection and content ordering  is measured using an Information Extraction based evaluation approach introduced by Wiseman et al (2017). The fluency is measured using BLEU.

#### Metrics

<!-- info: What metrics are typically used for this task? -->
<!-- scope: periscope -->
`Other: Other Metrics`

#### Other Metrics

<!-- info: Definitions of other metrics -->
<!-- scope: periscope -->
Wiseman et al. (2017) define three metrics induced from the outputs of an Information Extraction model which is run on the model/human-written game summaries . Let ŷ be the gold summary and y the model output.
• Relation Generation (RG) measures the precision and count of relations extracted from y that also appear in records r.
• Content Selection (CS) measures the precision and recall of relations extracted from y that are also extracted from ŷ.
• Content Ordering (CO) measures the complement of the normalized Damerau-Levenshtein distance (Brill and Moore, 2000) between the sequences of relations extracted from y and ŷ

#### Proposed Evaluation

<!-- info: List and describe the purpose of the metrics and evaluation methodology (including human evaluation) that the dataset creators used when introducing this task. -->
<!-- scope: microscope -->
We have reused the automatic metrics based on Information Extraction evaluation introduced by Wiseman et al (2017). For human evaluation, we conducted studies to evaluate the factuality, coherence, grammaticality and conciseness.

#### Previous results available?

<!-- info: Are previous results available? -->
<!-- scope: telescope -->
yes

#### Relevant Previous Results

<!-- info: What are the most relevant previous results for this task/dataset? -->
<!-- scope: microscope -->
The most relevant previous results for dataset are in the TACL 2021 paper on [Data-to-text Generation with Macro Planning](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00381/101876/Data-to-text-Generation-with-Macro-Planning)



## Dataset Curation

### Original Curation

#### Original Curation Rationale

<!-- info: Original curation rationale -->
<!-- scope: telescope -->
This dataset was curated to complement an existing data-to-text generation dataset (RotoWire by Wiseman et al. 2017) which focuses on long document generation. Compared to RotoWire , MLB summaries are longer (approximately by 50%) and the input records are richer and more structured (with the addition of play-by-play). Moreover, the MLB dataset is five times larger in terms of data size (i.e., pairs of tables and game summaries)

#### Communicative Goal

<!-- info: What was the communicative goal? -->
<!-- scope: periscope -->
The goal is to study automatic generation of long documents in a data-to-text setting. The generated summaries should exhibit coherent ordering of content, be faithful to the input statistics, be fluent and avoid repetition of text.

#### Sourced from Different Sources

<!-- info: Is the dataset aggregated from different data sources? -->
<!-- scope: telescope -->
no


### Language Data

#### How was Language Data Obtained?

<!-- info: How was the language data obtained? -->
<!-- scope: telescope -->
`Found`

#### Where was it found?

<!-- info: If found, where from? -->
<!-- scope: telescope -->
`Single website`

#### Language Producers

<!-- info: What further information do we have on the language producers? -->
<!-- scope: microscope -->
The game summaries are produced by professional writers.

#### Topics Covered

<!-- info: Does the language in the dataset focus on specific topics? How would you describe them? -->
<!-- scope: periscope -->
The language focuses on the sports domain.

#### Data Validation

<!-- info: Was the text validated by a different worker or a data curator? -->
<!-- scope: telescope -->
not validated

#### Data Preprocessing

<!-- info: How was the text data pre-processed? (Enter N/A if the text was not pre-processed) -->
<!-- scope: microscope -->
Game summaries were tokenized using NLTK (Bird et al., 2009) and hyphenated words were separated. Sentences containing quotes were removed as they included opinions and non-factual statements unrelated to the input tables. Sometimes MLB summaries contain a "Game notes" section with incidental information which was also removed.

#### Was Data Filtered?

<!-- info: Were text instances selected or filtered? -->
<!-- scope: telescope -->
not filtered


### Structured Annotations

#### Additional Annotations?

<!-- quick -->
<!-- info: Does the dataset have additional annotations for each instance? -->
<!-- scope: telescope -->
none

#### Annotation Service?

<!-- info: Was an annotation service used? -->
<!-- scope: telescope -->
no


### Consent

#### Any Consent Policy?

<!-- info: Was there a consent policy involved when gathering the data? -->
<!-- scope: telescope -->
no

#### Justification for Using the Data

<!-- info: If not, what is the justification for reusing the data? -->
<!-- scope: microscope -->
The copyright remains with the original data creators and the usage permission is restricted to non-commercial uses.


### Private Identifying Information (PII)

#### Contains PII?

<!-- quick -->
<!-- info: Does the source language data likely contain Personal Identifying Information about the data creators or subjects? -->
<!-- scope: telescope -->
yes/very likely

#### Categories of PII

<!-- info: What categories of PII are present or suspected in the data? -->
<!-- scope: periscope -->
`sensitive information`, `generic PII`

#### Any PII Identification?

<!-- info: Did the curators use any automatic/manual method to identify PII in the dataset? -->
<!-- scope: periscope -->
no identification


### Maintenance

#### Any Maintenance Plan?

<!-- info: Does the original dataset have a maintenance plan? -->
<!-- scope: telescope -->
no



## Broader Social Context

### Previous Work on the Social Impact of the Dataset

#### Usage of Models based on the Data

<!-- info: Are you aware of cases where models trained on the task featured in this dataset ore related tasks have been used in automated systems? -->
<!-- scope: telescope -->
no


### Impact on Under-Served Communities

#### Addresses needs of underserved Communities?

<!-- info: Does this dataset address the needs of communities that are traditionally underserved in language technology, and particularly language generation technology? Communities may be underserved for exemple because their language, language variety, or social or geographical context is underepresented in NLP and NLG resources (datasets and models). -->
<!-- scope: telescope -->
no


### Discussion of Biases

#### Any Documented Social Biases?

<!-- info: Are there documented social biases in the dataset? Biases in this context are variations in the ways members of different social categories are represented that can have harmful downstream consequences for members of the more disadvantaged group. -->
<!-- scope: telescope -->
unsure



## Considerations for Using the Data

### PII Risks and Liability



### Licenses

#### Copyright Restrictions on the Dataset

<!-- info: Based on your answers in the Intended Use part of the Data Overview Section, which of the following best describe the copyright and licensing status of the dataset? -->
<!-- scope: periscope -->
`research use only`

#### Copyright Restrictions on the Language Data

<!-- info: Based on your answers in the Language part of the Data Curation Section, which of the following best describe the copyright and licensing status of the underlying language data? -->
<!-- scope: periscope -->
`research use only`


### Known Technical Limitations



