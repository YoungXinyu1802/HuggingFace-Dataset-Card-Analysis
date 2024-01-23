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
paperswithcode_id: vasr
pretty_name: VASR
size_categories:
- 1K<n<10K
source_datasets:
- original
tags:
- commonsense-reasoning
- visual-reasoning
task_ids: []
extra_gated_prompt: "By clicking on “Access repository” below, you also agree that you are using it solely for research purposes. The full license agreement is available in the dataset files."
---
# Dataset Card for VASR
- [Dataset Description](#dataset-description)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [How to Submit Predictions?](#how-to-submit-predictions?)
  - [Colab notebook code for VASR evaluation with ViT](#colab-notebook-code-for-vasr-evaluation-with-clip)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
## Dataset Description
VASR is a challenging dataset for evaluating computer vision commonsense reasoning abilities. Given a triplet of images, the task is to select an image candidate B' that completes the analogy (A to A' is like B to what?). Unlike previous work on visual analogy that focused on simple image transformations, we tackle complex analogies requiring understanding of scenes. Our experiments demonstrate that state-of-the-art models struggle with carefully chosen distractors (±53%, compared to 90% human accuracy).
- **Homepage:** 
https://vasr-dataset.github.io/
- **Colab**
https://colab.research.google.com/drive/1HUg0aHonFDK3hVFrIRYdSEfpUJeY-4dI
- **Repository:**
https://github.com/vasr-dataset/vasr/tree/main/experiments
- **Paper:** https://arxiv.org/abs/2212.04542    
- **Leaderboard:**
https://vasr-dataset.github.io/
- **Point of Contact:**
yonatan.bitton@mail.huji.ac.il

## Supported Tasks and Leaderboards
https://vasr.github.io/leaderboard. 
https://paperswithcode.com/dataset/vasr. 

## How to Submit Predictions?
To submit predictions, please send a prediction CSV file to vasr.benchmark@gmail.com / yonatan.bitton@mail.huji.ac.il.   
The prediction file should include a "B'" column with the predicted candidate name that best solves the analogy, and an index from 1 to 4 indicating the location of the predicted candidate in the given candidate list.   
An example prediction file is available [HERE](https://drive.google.com/file/d/1NvBNdvlWmEOYjIVi2xdmQ_tUm-TXo42u/view?usp=share_link).  
A submission is allowed once a week, and you will receive a response within a week.   

## Colab notebook code for VASR evaluation with ViT
https://colab.research.google.com/drive/1HUg0aHonFDK3hVFrIRYdSEfpUJeY-4dI

### Languages
English. 

## Dataset Structure
### Data Fields
A: datasets.Image() - the first input image, **A**:A'.     
A': datasets.Image() - the second input image, different from A in a single key, A:**A'**.  
B: datasets.Image() - the third input image, has the same different item as A, **B**:B'.  
B': datasets.Image() - the forth image, which is the analogy solution. Different from B in a single key (the same different one as in A:A'),  B:**B'**. Hidden in the test set.  
candidates_images: [datasets.Image()] - a list of candidate images solutions to the analogy.  
label: datasets.Value("int64") - the index of the ground-truth solution. Hidden in the test set.  
candidates: [datasets.Value("string")] - a list of candidate string solutions to the analogy.  

### Data Splits
There are three splits, TRAIN, VALIDATION, and TEST.  
Since there are four candidates and one solution, random chance is 25%. 

## Dataset Creation

We leverage situation recognition annotations and the CLIP model to generate a large set of 500k candidate analogies.
There are two types of labels: 
- Silver labels, obtained from the automatic generation.
- Gold labels, obtained from human annotations over the silver annotations.

In the huggingface version we provide only the gold labeled dataset. Please refer to the project website download page if you want to download the silver labels version. 

### Annotations

#### Annotation process

We paid Amazon Mechanical Turk Workers to solve analogies, five annotators for each analogy.
Workers were asked to select the image that best solves the analogy. 
The resulting dataset is composed of the 3,820 instances agreed upon with a majority vote of at least 3 annotators, which was obtained in 93% of the cases.

## Considerations for Using the Data

All associations were obtained with human annotators. 
All used images are from the imSitu dataset (http://imsitu.org/)  
Using this data is allowed for academic research alone.

### Licensing Information

CC-By 4.0 

### Citation Information

NA

