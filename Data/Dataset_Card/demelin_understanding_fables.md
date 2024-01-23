---
annotations_creators:
- no-annotation
language:
- en
language_creators:
- expert-generated
license:
- mit
multilinguality:
- monolingual
pretty_name: Understanding Fables
size_categories:
- n<1K
source_datasets:
- original
task_categories:
- multiple-choice
- text-generation
- text-understanding
- text-comprehension
- natural-language-understanding
- natural-language-generation
task_ids:
- multiple-choice-qa
- language-modeling
---

# Dataset Card for Understanding Fables

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-instances)
  - [Data Splits](#data-instances)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)

## Dataset Description

- **Homepage:** [Understanding Fables BIG-Bench entry](https://github.com/google/BIG-bench/tree/main/bigbench/benchmark_tasks/understanding_fables)
- **Repository:** [Understanding Fables BIG-Bench entry](https://github.com/google/BIG-bench/tree/main/bigbench/benchmark_tasks/understanding_fables)
- **Paper:** [Beyond the Imitation Game: Quantifying and extrapolating the capabilities of language models](https://arxiv.org/abs/2206.04615)
- **Leaderboard:** [N/A]
- **Point of Contact:** [Denis Emelin](demelin.github.io)

### Dataset Summary

Fables are short narratives that aim to communicate a specific lesson or wisdom, referred to as the moral. Morals can be idiomatic or provide a succinct summary of the fable. Importantly, they make explicit the communicative intent of the fable and, thus, are highly relevant to its content. A computational model capable of natural language understanding should, when presented with a fable and a set of potentially relevant morals, rank the moral that accurately captures the message communicated by the fable above the rest. Additionally, fables represent a highly unusual narrative domain, where animals and inanimate objects are anthropomorphized and referred to with gendered pronouns, i.e., a rabbit may be a she, rather than an it. Thus, to understand fables, models must abstract away from patterns commonly encountered in their training data by applying human-like characteristics to non-human actors. Overall, for a computational model to perform well on this task, it must be capable of (1) successfully identifying the core message of a short narrative, (2) identifying a moral that expresses this message among a set of distractor morals, and (3) doing so within a narrative domain that is unlike the majority of pre-training data. Thus, the evaluated large language models would need to demonstrate cross-domain generalization capability in addition to narrative comprehension.

The dataset evaluates models' ability to comprehend written narratives by asking them to select the most appropriate moral for each fable, from a set of five alternatives. In addition to the correct answer, this set contains four distractor morals, which were selected semi-automatically. To identify challenging distractor morals for each fable, sentence similarity was computed between the embeddings of each sentence in the fable and all morals found in the entire dataset, keeping ten morals that were found to be most similar to any of the fable's sentences. From this set, four distractors were selected manually, so that neither of the final distractors represents a valid moral of the fable. By construction, such distractor items are likely to pose a challenge for models that disproportionally rely on shallow heuristics as opposed to more sophisticated language-understanding strategies.

### Supported Tasks and Leaderboards

- multiple-choice: The dataset can be used to evaluate models on their ability to rank a moral that is relevant to a specified fable above distractor morals, e.g. by assigning the correct choice a lower model perplexity. A [RoBERTa-based model](https://huggingface.co/roberta-base) can be used for this purpose.
- text-generation: The dataset can also be used to train models to generate appropriate morals conditioned on the fable text. A [GPT-based model](https://huggingface.co/EleutherAI/gpt-neo-2.7B) can be used for this purpose.


### Languages

The text in the dataset is in contemporary American English.

## Dataset Structure

### Data Instances

A typical data point consists of a single fable, five morals - four distractors and one that correctly captures the lesson imparted by the fable, and an integer label denoting the ID of the correct answer option. An example dataset entry looks as follows:  

{"story": "On a warm winter's day, the ants were busy drying corn that they had collected during summer. While they were engaged in their work, a starving grasshopper passed by and begged them for a single grain to stop his hunger. The ants, in turn, asked him why he had not collected food during the summer to prepare for the harsh winter, to which the grasshopper replied that he spent the warm days singing. Mockingly, the ants said to him in unison:  "Since you spent your summer singing, then you must dance hungrily to bed in winter." What is the moral of this story?",  
"answer0": "Fine clothes may disguise, but silly words will disclose a fool.",  
"answer1": "Better starve free than be a fat slave.",  
"answer2": "Evil wishes, like chickens, come home to roost.",  
"answer3": "Grasp at the shadow and you will lose the substance.",  
"answer4": "It is thrifty to prepare today for the wants of tomorrow.",  
"label": 4}
 

### Data Fields

- "story': The fable for which the appropriate moral has to be identified
- "answerN": Moral candidates to be evaluated by the model 
- "label": The ID of the moral belonging to the fable

### Data Splits

*Understanding Fables* was designed as an evaluation-only benchmark and therefore is intended to be used for zero-shot testing only. However, users are very welcome to split the data as they wish :) .

## Dataset Creation

### Curation Rationale

To comply with the requirements for inclusion in BIG-bench, each fable was manually paraphrased, to ensure that the task cannot be solved by memorising web data. Following sources were used for fable collection:  
- [https://www.aesopfables.com/aesop1.html](https://www.aesopfables.com/aesop1.html)
- [https://www.aesopfables.com/aesop2.html](https://www.aesopfables.com/aesop2.html)
- [https://www.aesopfables.com/aesop3.html](https://www.aesopfables.com/aesop3.html)
- [https://www.aesopfables.com/aesop4.html](https://www.aesopfables.com/aesop4.html)


### Source Data

#### Initial Data Collection and Normalization

Paraphrasing was done by an English speaker with native-like language proficiency and an academic background in literature. The created paraphrases differ from the originals in the identity of their participants (lion was replaced with tiger, wolf with coyote etc.), their sentence and narrative structure, and their register (archaic terms such as thou have been replaced with their modern counterparts). The phrasing of the morals has also been updated in cases where the original language was noticeably archaic (e.g., o'er reach -> overreach), with changes kept to a minimum. The mean string similarity between original fables and their paraphrases is consequently low at 0.26, according to the word-level DamerauLevenshtein distance. At the same time, great care was taken not to alter the content of the fables and preserve the relevance of their respective morals. This is evidenced by the high semantic similarity between the originals and their paraphrases, with a mean of 0.78, computed as the cosine similarity between the embeddings of the originals and their paraphrases, obtained using the Sentence-Transformers library. Moreover, duplicate and near-duplicate fables were removed from the final collection, as were several thematically problematic stories, e.g., ones with sexist undertones. In total, the dataset includes 189 paraphrased, unique fables.

#### Who are the source language producers?

Original authors and transcribers of the fables (unknown), the [dataset author](demelin.github.io). 

### Annotations

#### Annotation process

[N/A]

#### Who are the annotators?

[N/A]

### Personal and Sensitive Information

[N/A]

## Considerations for Using the Data

### Social Impact of Dataset

[N/A]

### Discussion of Biases

Several thematically problematic fables, e.g., ones with sexist undertones, were removed by the author during the dataset creation process. However, it can  be that the author overlooked other problematic or harmful biases present within the dataset.

### Other Known Limitations

The dataset is very limited in size due to the small number of thematically distinct fables available online. Similarly, the focus on English fables alone is a limiting factor to be addressed in future dataset iterations.

## Additional Information

### Dataset Curators

[Denis Emelin](demelin.github.io)

### Licensing Information

MIT

### Citation Information

@article{Srivastava2022BeyondTI,
  title={Beyond the Imitation Game: Quantifying and extrapolating the capabilities of language models},
  author={Aarohi Srivastava and Abhinav Rastogi and Abhishek B Rao and Abu Awal Md Shoeb and Abubakar Abid and Adam Fisch and Adam R. Brown and Adam Santoro and Aditya Gupta and Adri{\`a} Garriga-Alonso and Agnieszka Kluska and Aitor Lewkowycz and Akshat Agarwal and Alethea Power and Alex Ray and Alex Warstadt and Alexander W. Kocurek and Ali Safaya and Ali Tazarv and Alice Xiang and Alicia Parrish and Allen Nie and Aman Hussain and Amanda Askell and Amanda Dsouza and Ameet Annasaheb Rahane and Anantharaman S. Iyer and Anders Johan Andreassen and Andrea Santilli and Andreas Stuhlmuller and Andrew M. Dai and Andrew D. La and Andrew Kyle Lampinen and Andy Zou and Angela Jiang and Angelica Chen and Anh Vuong and Animesh Gupta and Anna Gottardi and Antonio Norelli and Anu Venkatesh and Arash Gholamidavoodi and Arfa Tabassum and Arul Menezes and Arun Kirubarajan and Asher Mullokandov and Ashish Sabharwal and Austin Herrick and Avia Efrat and Aykut Erdem and Ayla Karakacs and Bridget R. Roberts and Bao Sheng Loe and Barret Zoph and Bartlomiej Bojanowski and Batuhan Ozyurt and Behnam Hedayatnia and Behnam Neyshabur and Benjamin Inden and Benno Stein and Berk Ekmekci and Bill Yuchen Lin and Blake Stephen Howald and Cameron Diao and Cameron Dour and Catherine Stinson and Cedrick Argueta and C'esar Ferri Ram'irez and Chandan Singh and Charles Rathkopf and Chenlin Meng and Chitta Baral and Chiyu Wu and Chris Callison-Burch and Chris Waites and Christian Voigt and Christopher D. Manning and Christopher Potts and Cindy Tatiana Ramirez and Clara Rivera and Clemencia Siro and Colin Raffel and Courtney Ashcraft and Cristina Garbacea and Damien Sileo and Daniel H Garrette and Dan Hendrycks and Dan Kilman and Dan Roth and Daniel Freeman and Daniel Khashabi and Daniel Levy and Daniel Gonz'alez and Danny Hernandez and Danqi Chen and Daphne Ippolito and Dar Gilboa and David Dohan and D. Drakard and David Jurgens and Debajyoti Datta and Deep Ganguli and Denis Emelin and Denis Kleyko and Deniz Yuret and Derek Chen and Derek Tam and Dieuwke Hupkes and Diganta Misra and Dilyar Buzan and Dimitri Coelho Mollo and Diyi Yang and Dong-Ho Lee and Ekaterina Shutova and Ekin Dogus Cubuk and Elad Segal and Eleanor Hagerman and Elizabeth Barnes and Elizabeth P. Donoway and Ellie Pavlick and Emanuele Rodol{\`a} and Emma FC Lam and Eric Chu and Eric Tang and Erkut Erdem and Ernie Chang and Ethan A. Chi and Ethan Dyer and Ethan Jerzak and Ethan Kim and Eunice Engefu Manyasi and Evgenii Zheltonozhskii and Fan Xia and Fatemeh Siar and Fernando Mart'inez-Plumed and Francesca Happ'e and François Chollet and Frieda Rong and Gaurav Mishra and Genta Indra Winata and Gerard de Melo and Germ{\'a}n Kruszewski and Giambattista Parascandolo and Giorgio Mariani and Gloria Wang and Gonzalo Jaimovitch-L'opez and Gregor Betz and Guy Gur-Ari and Hana Galijasevic and Han Sol Kim and Hannah Rashkin and Hanna Hajishirzi and Harsh Mehta and Hayden Bogar and Henry Shevlin and Hinrich Sch{\"u}tze and Hiromu Yakura and Hongming Zhang and Hubert Wong and Ian Aik-Soon Ng and Isaac Noble and Jaap Jumelet and Jack Geissinger and John Kernion and Jacob Hilton and Jaehoon Lee and Jaime Fern{\'a}ndez Fisac and J. Brooker Simon and James Koppel and James Zheng and James Zou and Jan Koco'n and Jana Thompson and Jared Kaplan and Jarema Radom and Jascha Narain Sohl-Dickstein and Jason Phang and Jason Wei and Jason Yosinski and Jekaterina Novikova and Jelle Bosscher and Jenni Marsh and Jeremy Kim and Jeroen Taal and Jesse Engel and Jesujoba Oluwadara Alabi and Jiacheng Xu and Jiaming Song and Jillian Tang and Jane W Waweru and John Burden and John Miller and John U. Balis and Jonathan Berant and Jorg Frohberg and Jos Rozen and Jos{\'e} Hern{\'a}ndez-Orallo and Joseph Boudeman and Joseph Jones and Joshua B. Tenenbaum and Joshua S. Rule and Joyce Chua and Kamil Kanclerz and Karen Livescu and Karl Krauth and Karthik Gopalakrishnan and Katerina Ignatyeva and Katja Markert and Kaustubh D. Dhole and Kevin Gimpel and Kevin Ochieng’ Omondi and Kory Wallace Mathewson and Kristen Chiafullo and Ksenia Shkaruta and Kumar Shridhar and Kyle McDonell and Kyle Richardson and Laria Reynolds and Leo Gao and Li Zhang and Liam Dugan and Lianhui Qin and Lidia Contreras-Ochando and Louis-Philippe Morency and Luca Moschella and Luca Lam and Lucy Noble and Ludwig Schmidt and Luheng He and Luis Oliveros Col'on and Luke Metz and Lutfi Kerem cSenel and Maarten Bosma and Maarten Sap and Maartje ter Hoeve and Madotto Andrea and Maheen Saleem Farooqi and Manaal Faruqui and Mantas Mazeika and Marco Baturan and Marco Marelli and Marco Maru and M Quintana and Marie Tolkiehn and Mario Giulianelli and Martha Lewis and Martin Potthast and Matthew Leavitt and Matthias Hagen and M'aty'as Schubert and Medina Baitemirova and Melissa Arnaud and Melvin Andrew McElrath and Michael A. Yee and Michael Cohen and Mi Gu and Michael I. Ivanitskiy and Michael Starritt and Michael Strube and Michal Swkedrowski and Michele Bevilacqua and Michihiro Yasunaga and Mihir Kale and Mike Cain and Mimee Xu and Mirac Suzgun and Monica Tiwari and Mohit Bansal and Moin Aminnaseri and Mor Geva and Mozhdeh Gheini and T MukundVarma and Nanyun Peng and Nathan Chi and Nayeon Lee and Neta Gur-Ari Krakover and Nicholas Cameron and Nicholas S. Roberts and Nicholas Doiron and Nikita Nangia and Niklas Deckers and Niklas Muennighoff and Nitish Shirish Keskar and Niveditha Iyer and Noah Constant and Noah Fiedel and Nuan Wen and Oliver Zhang and Omar Agha and Omar Elbaghdadi and Omer Levy and Owain Evans and Pablo Antonio Moreno Casares and Parth Doshi and Pascale Fung and Paul Pu Liang and Paul Vicol and Pegah Alipoormolabashi and Peiyuan Liao and Percy Liang and Peter W. Chang and Peter Eckersley and Phu Mon Htut and Pi-Bei Hwang and P. Milkowski and Piyush S. Patil and Pouya Pezeshkpour and Priti Oli and Qiaozhu Mei and QING LYU and Qinlang Chen and Rabin Banjade and Rachel Etta Rudolph and Raefer Gabriel and Rahel Habacker and Ram'on Risco Delgado and Rapha{\"e}l Milli{\`e}re and Rhythm Garg and Richard Barnes and Rif A. Saurous and Riku Arakawa and Robbe Raymaekers and Robert Frank and Rohan Sikand and Roman Novak and Roman Sitelew and Ronan Le Bras and Rosanne Liu and Rowan Jacobs and Rui Zhang and Ruslan Salakhutdinov and Ryan Chi and Ryan Lee and Ryan Stovall and Ryan Teehan and Rylan Yang and Sahib J. Singh and Saif M. Mohammad and Sajant Anand and Sam Dillavou and Sam Shleifer and Sam Wiseman and Samuel Gruetter and Sam Bowman and Samuel S. Schoenholz and Sanghyun Han and Sanjeev Kwatra and Sarah A. Rous and Sarik Ghazarian and Sayan Ghosh and Sean Casey and Sebastian Bischoff and Sebastian Gehrmann and Sebastian Schuster and Sepideh Sadeghi and Shadi Sameh Hamdan and Sharon Zhou and Shashank Srivastava and Sherry Shi and Shikhar Singh and Shima Asaadi and Shixiang Shane Gu and Shubh Pachchigar and Shubham Toshniwal and Shyam Upadhyay and Shyamolima Debnath and Siamak Shakeri and Simon Thormeyer and Simone Melzi and Siva Reddy and Sneha Priscilla Makini and Soo-hwan Lee and Spencer Bradley Torene and Sriharsha Hatwar and Stanislas Dehaene and Stefan Divic and Stefano Ermon and Stella Rose Biderman and Stephanie C. Lin and Stephen Prasad and Steven T. Piantadosi and Stuart M. Shieber and Summer Misherghi and Svetlana Kiritchenko and Swaroop Mishra and Tal Linzen and Tal Schuster and Tao Li and Tao Yu and Tariq A. Ali and Tatsuo Hashimoto and Te-Lin Wu and Theo Desbordes and Theodore Rothschild and Thomas Phan and Tianle Wang and Tiberius Nkinyili and Timo Schick and T. N. Kornev and Timothy Telleen-Lawton and Titus Tunduny and Tobias Gerstenberg and Trenton Chang and Trishala Neeraj and Tushar Khot and Tyler O. Shultz and Uri Shaham and Vedant Misra and Vera Demberg and Victoria Nyamai and Vikas Raunak and Vinay V. Ramasesh and Vinay Uday Prabhu and Vishakh Padmakumar and Vivek Srikumar and William Fedus and William Saunders and William Zhang and W Vossen and Xiang Ren and Xiaoyu F Tong and Xinyi Wu and Xudong Shen and Yadollah Yaghoobzadeh and Yair Lakretz and Yang Song and Yasaman Bahri and Ye Ji Choi and Yichi Yang and Yiding Hao and Yifu Chen and Yonatan Belinkov and Yu Hou and Yu Hou and Yushi Bai and Zachary Seid and Zhao Xinran and Zhuoye Zhao and Zi Fu Wang and Zijie J. Wang and Zirui Wang and Ziyi Wu and Sahib Singh and Uri Shaham},
  journal={ArXiv},
  year={2022},
  volume={abs/2206.04615}
}