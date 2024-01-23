---
license: mit
---
# Disclaimer
*This is a hate speech dataset (in Arabic, French, and English).*

*Offensive content that does not reflect the opinions of the authors.* 

# Dataset of our EMNLP 2019 Paper (Multilingual and Multi-Aspect Hate Speech Analysis)
For more details about our dataset, please check our paper:

	@inproceedings{ousidhoum-etal-multilingual-hate-speech-2019,
    		title = "Multilingual and Multi-Aspect Hate Speech Analysis",
    		author = "Ousidhoum, Nedjma
             		and Lin, Zizheng
             		and Zhang, Hongming
            		and Song, Yangqiu
            		and Yeung, Dit-Yan",
    			booktitle = "Proceedings of EMNLP",
    		year = "2019",
    		publisher =	"Association for Computational Linguistics",
	}	

(You can preview our paper on https://arxiv.org/pdf/1908.11049.pdf)

## Clarification
The multi-labelled tasks are *the hostility type of the tweet* and the *annotator's sentiment*. (We kept labels on which at least two annotators agreed.)

## Taxonomy
In further experiments that involved binary classification tasks of the hostility/hate/abuse type, we considered single-labelled *normal* instances to be *non-hate/non-toxic* and all the other instances to be *toxic*.

## Dataset
Our dataset is composed of three csv files sorted by language. They contain the tweets and the annotations described in our paper:

the hostility type *(column: tweet sentiment)* 

hostility directness *(column: directness)* 

target attribute *(column: target)*

target group *(column: group)* 

annotator's sentiment *(column: annotator sentiment)*.

## Experiments

To replicate our experiments, please see https://github.com/HKUST-KnowComp/MLMA_hate_speech/blob/master/README.md 

