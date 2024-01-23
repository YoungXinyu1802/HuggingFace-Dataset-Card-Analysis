---
annotations_creators:
- crowdsourced
language:
- en
language_creators:
- found
license:
- cc-by-4.0
multilinguality:
- monolingual
paperswithcode_id: winogavil
pretty_name: WinoGAViL
size_categories:
- 10K<n<100K
source_datasets:
- original
tags:
- commonsense-reasoning
- visual-reasoning
task_ids: []
extra_gated_prompt: "By clicking on “Access repository” below, you also agree that you are using it solely for research purposes. The full license agreement is available in the dataset files."
---

# Dataset Card for WinoGAViL

- [Dataset Description](#dataset-description)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Colab notebook code for Winogavil evaluation with CLIP](#colab-notebook-code-for-winogavil-evaluation-with-clip)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)

## Dataset Description

WinoGAViL is a challenging dataset for evaluating vision-and-language commonsense reasoning abilities. Given a set of images, a cue, and a number K, the task is to select the K images that best fits the association. This dataset was collected via the WinoGAViL online game to collect vision-and-language associations, (e.g., werewolves to a full moon). Inspired by the popular card game Codenames, a spymaster gives a textual cue related to several visual candidates, and another player has to identify them. Human players are rewarded for creating associations that are challenging for a rival AI model but still solvable by other human players.   We evaluate several state-of-the-art vision-and-language models, finding that they are intuitive for humans (>90% Jaccard index) but challenging for state-of-the-art AI models, where the best model (ViLT) achieves a score of 52%, succeeding mostly where the cue is visually salient. Our analysis as well as the feedback we collect from players indicate that the collected associations require diverse reasoning skills, including general knowledge, common sense, abstraction, and more. 

- **Homepage:** 
https://winogavil.github.io/
- **Colab**
https://colab.research.google.com/drive/19qcPovniLj2PiLlP75oFgsK-uhTr6SSi
- **Repository:**
https://github.com/WinoGAViL/WinoGAViL-experiments/
- **Paper:**
https://arxiv.org/abs/2207.12576
- **Leaderboard:**
https://winogavil.github.io/leaderboard
- **Point of Contact:**
winogavil@gmail.com; yonatanbitton1@gmail.com 

### Supported Tasks and Leaderboards

https://winogavil.github.io/leaderboard. 
https://paperswithcode.com/dataset/winogavil. 

## Colab notebook code for Winogavil evaluation with CLIP
https://colab.research.google.com/drive/19qcPovniLj2PiLlP75oFgsK-uhTr6SSi

### Languages

English. 

## Dataset Structure

### Data Fields

candidates (list): ["bison", "shelter", "beard", "flea", "cattle", "shave"] - list of image candidates.  
cue (string): pogonophile - the generated cue.  
associations (string): ["bison", "beard", "shave"] - the images associated with the cue selected by the user.  
score_fool_the_ai (int64): 80 - the spymaster score (100 - model score) for fooling the AI, with CLIP RN50 model. 
num_associations (int64): 3 - The number of images selected as associative with the cue.  
num_candidates (int64): 6 - the number of total candidates.  
solvers_jaccard_mean (float64): 1.0 - three solvers scores average on the generated association instance.  
solvers_jaccard_std (float64): 1.0 - three solvers scores standard deviation on the generated association instance
ID (int64): 367 - association ID. 

### Data Splits
There is a single TEST split. In the accompanied paper and code we sample it to create different training sets, but the intended use is to use winogavil as a test set.
There are different number of candidates, which creates different difficulty levels:   
  -- With 5 candidates, random model expected score is 38%.  
  -- With 6 candidates, random model expected score is 34%.  
  -- With 10 candidates, random model expected score is 24%.  
  -- With 12 candidates, random model expected score is 19%.  

<details>
  <summary>Why random chance for success with 5 candidates is 38%?</summary>
  
  It is a binomial distribution probability calculation. 
  
  Assuming N=5 candidates, and K=2 associations, there could be three events:   
  (1) The probability for a random guess is correct in 0 associations is 0.3 (elaborate below), and the Jaccard index is 0 (there is no intersection between the correct labels and the wrong guesses). Therefore the expected random score is 0.  
  (2) The probability for a random guess is correct in 1 associations is 0.6, and the Jaccard index is 0.33 (intersection=1, union=3, one of the correct guesses, and one of the wrong guesses). Therefore the expected random score is 0.6*0.33 = 0.198.  
  (3) The probability for a random guess is correct in 2 associations is 0.1, and the Jaccard index is 1 (intersection=2, union=2). Therefore the expected random score is 0.1*1 = 0.1.  
  * Together, when K=2, the expected score is 0+0.198+0.1 = 0.298.   
  
  To calculate (1), the first guess needs to be wrong. There are 3 "wrong" guesses and 5 candidates, so the probability for it is 3/5. The next guess should also be wrong. Now there are only 2 "wrong" guesses, and 4 candidates, so the probability for it is 2/4. Multiplying 3/5 * 2/4 = 0.3. 
  Same goes for (2) and (3). 
  
  Now we can perform the same calculation with K=3 associations. 
    Assuming N=5 candidates, and K=3 associations, there could be four events:   
  (4) The probability for a random guess is correct in 0 associations is 0, and the Jaccard index is 0. Therefore the expected random score is 0.  
  (5) The probability for a random guess is correct in 1 associations is 0.3, and the Jaccard index is 0.2 (intersection=1, union=4). Therefore the expected random score is 0.3*0.2 = 0.06.  
  (6) The probability for a random guess is correct in 2 associations is 0.6, and the Jaccard index is 0.5 (intersection=2, union=4). Therefore the expected random score is 0.6*5 = 0.3.    
  (7) The probability for a random guess is correct in 3 associations is 0.1, and the Jaccard index is 1 (intersection=3, union=3). Therefore the expected random score is 0.1*1 = 0.1.    
  * Together, when K=3, the expected score is 0+0.06+0.3+0.1 = 0.46. 
  
Taking the average of 0.298 and 0.46 we reach 0.379. 

Same process can be recalculated with 6 candidates (and K=2,3,4), 10 candidates (and K=2,3,4,5) and 123 candidates (and K=2,3,4,5,6). 

</details>


## Dataset Creation

Inspired by the popular card game Codenames, a “spymaster” gives a textual cue related to several visual candidates, and another player has to identify them. Human players are rewarded for creating
associations that are challenging for a rival AI model but still solvable by other
human players.

### Annotations

#### Annotation process

We paid Amazon Mechanical Turk Workers to play our game.  

## Considerations for Using the Data

All associations were obtained with human annotators. 

### Licensing Information

CC-By 4.0 

### Citation Information

 @article{bitton2022winogavil,
  title={WinoGAViL: Gamified Association Benchmark to Challenge Vision-and-Language Models},
  author={Bitton, Yonatan and Guetta, Nitzan Bitton and Yosef, Ron and Elovici, Yuval and Bansal, Mohit and Stanovsky, Gabriel and Schwartz, Roy},
  journal={arXiv preprint arXiv:2207.12576},
  year={2022}
