---
license: mit
task_categories:
- text-generation
language:
- en
tags:
- writingPrompt
dataset_info:
- config_name: 0.0.1
  features:
  - name: splitLineIndex
    dtype: int64
  - name: text
    dtype: string
  splits:
  - name: train
    num_examples: 13232
  - name: valid
    num_examples: 5168
  - name: train
    num_examples: 5700    
---
# Dataset Card for Writing Prompt Augmentation Dataset

## Dataset Description

- **Homepage:** 
- **Repository:** 
- **Paper:**  Writing Prompt Augmentation Dataset was built to expand samples of [FAIR Writing Prompt Dataset](https://www.kaggle.com/datasets/ratthachat/writing-prompts)
- **Leaderboard:**
- **Point of Contact:** [Fabricio Braz](mailto:fabraz@unb.br) 

### Dataset Summary

Writing Prompt Augmentation Dataset was built to expand samples of [FAIR Writing Prompt Dataset](https://www.kaggle.com/datasets/ratthachat/writing-prompts), for feeding [Open Assistant](https://github.com/LAION-AI/Open-Assistant).

### Languages

English

## Dataset Structure

### Data Instances

```javascript
{"splitLineIndex":36888,
 "text":"User: write me a story about: Most responses on here have a twist , and all of them are fictional . Show us a piece of your actual life ; let the reader experience you ., where the middle of the story is about: The boss sits on my wall and asks me where a urgent report is up. I stare at the screen, confused. -> Rosey: Sure, here\'s a story about: Most responses on here have a twist , and all of them are fictional . Show us a piece of your actual life ; let the reader experience you ., where the middle of the story is about: The boss sits on my wall and asks me where a urgent report is up. I stare at the screen, confused.:\\nMy bedroom was dark , but the chatter of distant birds outside of the heavily curtained window suggested a new day was dawning . I stayed in bed , one with the shadows , and stared at the indistinct blackness that filled the ceiling . A trickle of sickly grey light would soon spring from the edges of curtain - the heavy fabric could only do so much to dam the brightness of day . \\n \\n But , for a few more minutes , it was still dark . \\n \\n And I was staring at it - staring at the darkness . Examining it . \\n \\n What was I looking for ? Why , answers of course . Why does anyone stare into the darkness of a bedroom ceiling ? I was seeking answers . \\n \\n Why do it ? I asked myself . Why go to work ? You \'re good at your job when you can be bothered to do it , but how often does that happen ? How often do you really put the effort in ? \\n \\n Can you even remember enjoying it ? \\n \\n Can you remember when you were happy ? \\n \\n I had been too deep in my hunt for answers to notice that the homogenous darkness had given way to a bluish grey world of shapes and objects . My feet swung out of bed and I sat up in the early morning coldness . \\n \\n When *was* I happy last ? \\n \\n I stood up and started my day . \\n \\n * * * \\n \\n The kitchen was filling with light , the muted greys and blues of morning had arrived first , but each minute that passed promised the arrival of the full colours of day . \\n \\n The spoon clinked in the bowl as I scooped up some cereal . I wore only what I had to bed : boxer shirts and a t-shirt . The winter cold does n\'t bother you when you \'ve stopped caring . \\n \\n *When* was I happy ? \\n \\n The question was echoing in my head . A great puzzle . A mystery of the ages . \\n \\n I gulped the last of my morning coffee and went to the bathroom . \\n \\n * * * \\n \\n The plug hole held no answers , no matter how long I stared . \\n \\n How long had I been staring ? \\n \\n I turned the shower off and stepped out into the sterile tiled whiteness . A lifetime of habits drew me to the basin and , without thought , I started to brush my teeth . My mind was still locked , frozen , on the question . \\n \\n When was I happy ? \\n \\n As I wondered , day continued it \'s steady march outside . \\n \\n The bathroom was clean and white , morning light filtered in through a frosted window . The birds were loud now , but I could hardly hear them over the whir of the steam sucking fan above me . \\n \\n Day had officially arrived . \\n \\n Perhaps I am asking myself the wrong question , I thought . \\n \\n The man in the mirror bared his teeth and scrubbed some more , white foam dripped in blobs about the basin . \\n \\n *What* makes me happy ? \\n \\n * * * \\n \\n I had slipped into my work clothes : business shirt , dress pants , leather shoes . My prisoners garb . As I pulled the items on they weighed me down , each a colossal burden . At least I did n\'t wear a tie any more . \\n \\n I had given up on ties , and the rest of my uniform wore the scars of neglect : the shirt was unironed , the pants were thin at the knees and the stitching had come loose at the bottoms , the shoes were beaten , scratched , the soles and tops barely held their bond . \\n \\n This is the business attire of a man who has stopped caring . \\n \\n No one at work seemed to mind . \\n \\n I walked to the front door of my house , shuffling without enthusiasm , without joy for the new day that lay on the other side . \\n \\n I grabbed the handle . \\n \\n What makes me happy ? \\n \\n * * * \\n \\n Another request , another complaint , and my list of work grew longer . It only ever grew longer these days . I had important calls to make , issues to resolve , reports to write - but all I did , for the most part , was stare . \\n \\n Stare at my screen . At my hands . At nothing . \\n \\n The questions I had been asking in the darkness and through-out my house during my morning preparations were not new . I had been thinking on them for a while . I did not know for how long . \\n \\n Weeks ? No . Months . \\n \\n Still no answers . \\n \\n What I do know is : I am *not* happy . \\n \\n The boss leaned on my cubicle wall and asked me where an urgent report , a report that had been urgent for weeks , was up to . The bullshit I served sated his questions and as he walked away I sighed and stared at my screen . \\n \\n To my surprise the report was there . I had been working on it absent-mindedly . Try as I might I still did my job , at least to a degree . \\n \\n Manager for a division of one . Writer of reports and promiser of game changing applications . Mr IT . \\n \\n Well ... at one time I had been Mr IT . Once , when I had been passionate , had had a fire in my belly that churned the engine of my rising star . A career in IT . I had wanted this . \\n \\n Had n\'t I ? \\n \\n Then , why are n\'t I happy ? \\n \\n Because , you did n\'t want this . You never did . You stepped out of high school and fell into it . You \'re good with computers - at least , you were - but they never made you happy . You liked the challenge , sure , but you did it because you had to pay the bills and you had to leave your parents house at some point . \\n \\n Then it was a matter of you being lazy and gutless . Work is a hard habit to break , especially when people keep throwing money at you . You \'d just go in , day after day . Week after week . Month after ... \\n \\n School was almost a decade away and you have n\'t done half of what you wanted . Remember writing ? You were going to write , remember ? You \'ve done some shorts over the years , but you wanted more . You wanted to type those two words . After months and months , you \'d type those two words and you \'d have accomplished sonething . The End . And your book would be done - who cares if it got published . Who cares if no one but you ever saw it . \\n \\n You \'d have written something . You \'d have accomplished something . \\n \\n You \'d be ... \\n \\n And there it is . The answer . \\n \\n Ten years of wasted time - ten years of excuses and meeting other people \'s expectations . Ten years of syaing you \'ll get around to it . \\n \\n Ten years of regret . \\n \\n The report was done . So was I . \\n \\n How do I do this ? Do I walk in and hand in the report and a resignation . No . I ca n\'t do that . These people have been good to me . I need to finish up some of the jobs . Need to get them ready for my abscence . \\n \\n Or am I making excuses ? \\n \\n My screen and my work came into focus . I knew what I needed to do , could feel , almost by instinct , what job \'s were my biggest priorities . A spark lit in my gut and passion trickled through my veins . \\n \\n I was n\'t turning back into Mr IT - could in fact , never be that man again . \\n \\n But I knew what made me happy . Knew how to get there ... \\n \\n ... and could feel it there , just on my horizon ."}
```

### Data Fields

 * splitLineIndex: refers to the index line of the data source.
 * text: refers to the actual prompt/story text

### Data Splits

|split|samples|
|--|--
|train|  13232|
|valid|5168|
|test| 5700|

## Dataset Creation

### Source Data

#### Initial Data Collection and Normalization

As mentioned, this dataset is an extension of FAIR writing prompt dataset. The steps employed to create the dataset are in the jupyter notebook at files. 

#### Who are the source language producers?

FAIR

### Personal and Sensitive Information

The data comes with NSFW samples. Be aware!


## Additional Information


### Licensing Information

Writing Prompt Augmentation Dataset is licensed under MIT.

### Citation Information

Use to generate consistent stories by Hierarchical Neural Story Generation (Fan et al., 2018) https://arxiv.org/abs/1805.04833


### Contributions

Thanks to Huu Nguyen (gh:ontocord)!