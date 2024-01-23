
# Introduction

Modern image captaining relies heavily on extracting knowledge, from images such as objects,
to capture the concept of static story in the image. In this paper, we propose a textual visual context dataset 
for captioning, where the publicly available dataset COCO caption (Lin et al., 2014) has been extended with information 
about the scene (such as objects in the image). Since this information has textual form, it can be used to leverage any NLP task,
such as text similarity or semantic relation methods, into captioning systems, either as an end-to-end training strategy or a post-processing based approach. 

Please refer to  [project page](https://sabirdvd.github.io/project_page/Dataset_2022/index.html) and [Github](https://github.com/ahmedssabir/Visual-Semantic-Relatedness-Dataset-for-Image-Captioning) for more information. [![arXiv](https://img.shields.io/badge/arXiv-2301.08784-b31b1b.svg)](https://arxiv.org/abs/2301.08784)  [![Website shields.io](https://img.shields.io/website-up-down-green-red/http/shields.io.svg)](https://ahmed.jp/project_page/Dataset_2022/index.html)



 

# Overview

 We enrich COCO-Caption with textual Visual Context information. We use ResNet152, CLIP, 
          and Faster R-CNN to extract object information for each  image. We use three filter approaches 
          to ensure the quality of the dataset (1) Threshold: to filter out predictions where the object classifier 
          is not confident enough,  and (2) semantic alignment with semantic similarity to remove duplicated objects. 
          (3) semantic relatedness score as soft-label: to guarantee the visual context and caption have a strong 
          relation. In particular, we use Sentence-RoBERTa via cosine similarity to give a soft score, and then 
          we use a threshold to annotate the final label (if th ≥ 0.2, 0.3, 0.4 then 1,0). Finally, to take advantage 
          of the visual overlap  between caption and visual context, and to extract global information, we use BERT followed by a shallow CNN (<a href="https://arxiv.org/abs/1408.5882">Kim, 2014</a>)
          to estimate the visual relatedness score. 
 
 For quick start please have a look this [demo](https://github.com/ahmedssabir/Textual-Visual-Semantic-Dataset/blob/main/BERT_CNN_Visual_re_ranker_demo.ipynb) and [pre-trained model with th 0.2, 0.3, 0.4](https://huggingface.co/AhmedSSabir/BERT-CNN-Visual-Semantic)  
 
<!-- 
## Dataset 

### Sample 
 
 ```
|---------------+--------------+---------+---------------------------------------------------|
| VC1           | VC2          | VC3     | human annoated caption                            |
| ------------- | -----------  | --------| ------------------------------------------------- |
| cheeseburger  | plate        | hotdog  | a plate with a hamburger fries and tomatoes       |
| bakery        | dining table | website | a table having tea and a cake on it               |
| gown          | groom        | apron   | its time to cut the cake at this couples wedding  |
|---------------+--------------+---------+---------------------------------------------------|
``` 
-->

### Download 

0. [Dowload Raw data with ID and Visual context](https://www.dropbox.com/s/xuov24on8477zg8/All_Caption_ID.csv?dl=0) -> original dataset with related ID caption [train2014](https://cocodataset.org/#download)
1. [Downlod Data with cosine score](https://www.dropbox.com/s/u1n2r2ign8v7gvh/visual_caption_cosine_score.zip?dl=0)-> soft cosine lable with **th** 0.2, 0.3, 0.4 and 0.5
2. [Dowload Overlaping visual with caption](https://www.dropbox.com/s/br8nhnlf4k2czo8/COCO_overlaping_dataset.txt?dl=0)-> Overlap visual context and the human annotated caption 
3. [Download Dataset (tsv file)](https://www.dropbox.com/s/dh38xibtjpohbeg/train_all.zip?dl=0) 0.0-> raw data with hard lable without cosine similairty and with **th**reshold  cosine sim degree of the relation beteween the visual and caption = 0.2, 0.3, 0.4
4. [Download Dataset GenderBias](https://www.dropbox.com/s/1wki0b0d21078mj/gender%20natural.zip?dl=0)-> man/woman replaced with person class label



For unsupervised learning
  
 1. [Download CC](https://www.dropbox.com/s/pc1uv2rf6nqdp57/CC_caption_40.txt.zip) -> Caption dataset from Conceptinal Caption (CC) 2M (2255927 captions)
 2. [Download CC+wiki](https://www.dropbox.com/s/xuov24on8477zg8/All_Caption_ID.csv?dl=0) -> CC+1M-wiki 3M (3255928) 
 3. [Download CC+wiki+COCO](https://www.dropbox.com/s/k7oqwr9a1a0h8x1/CC_caption_40%2Bwiki%2BCOCO.txt.zip) -> CC+wiki+COCO-Caption 3.5M (366984)
 4. [Download COCO-caption+wiki](https://www.dropbox.com/s/wc4k677wp24kzhh/COCO%2Bwiki.txt.zip) -> COCO-caption +wiki 1.4M (1413915)
 5. [Download COCO-caption+wiki+CC+8Mwiki](https://www.dropbox.com/s/xhfx32sjy2z5bpa/11M_wiki_7M%2BCC%2BCOCO.txt.zip) -> COCO-caption+wiki+CC+8Mwiki 11M (11541667) 

## Citation

The details of this repo are described in the following paper. If you find this repo useful, please kindly cite it:

```bibtex
@article{sabir2023visual,
  title={Visual Semantic Relatedness Dataset for Image Captioning},
  author={Sabir, Ahmed and Moreno-Noguer, Francesc and Padr{\'o}, Llu{\'\i}s},
  journal={arXiv preprint arXiv:2301.08784},
  year={2023}
}
```

