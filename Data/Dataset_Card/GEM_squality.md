---
annotations_creators:
- crowd-sourced
language_creators:
- unknown
language:
- en
license:
- cc-by-4.0
multilinguality:
- unknown
size_categories:
- unknown
source_datasets:
- original
task_categories:
- summarization
task_ids: []
pretty_name: squality
---

# Dataset Card for GEM/squality

## Dataset Description

- **Homepage:** https://github.com/nyu-mll/SQuALITY
- **Repository:** https://github.com/nyu-mll/SQuALITY/data
- **Paper:** https://arxiv.org/abs/2205.11465
- **Leaderboard:** N/A
- **Point of Contact:** Alex Wang

### Link to Main Data Card

You can find the main data card on the [GEM Website](https://gem-benchmark.com/data_cards/squality).

### Dataset Summary 

SQuALITY (Summarization-format QUestion Answering with Long Input Texts, Yes!) is a summarization dataset that is:
* Abstractive
* Long-input: The input document are short stories between 3000--6000 words.
* Question-focused: Each story is associated with multiple question-summary pairs.
* Multi-reference: Each question is paired with 4 summaries.
* High-quality: The summaries are crowdsourced from skilled and trained writers.

You can load the dataset via:
```
import datasets
data = datasets.load_dataset('GEM/squality')
```
The data loader can be found [here](https://huggingface.co/datasets/GEM/squality).

#### website
[Github](https://github.com/nyu-mll/SQuALITY)

#### paper
[ArXiv](https://arxiv.org/abs/2205.11465)

#### authors
Alex Wang (NYU); Angelica Chen (NYU); Richard Yuanzhe Pang (NYU); Nitish Joshi (NYU); Samuel R. Bowman (NYU)

## Dataset Overview

### Where to find the Data and its Documentation

#### Webpage

<!-- info: What is the webpage for the dataset (if it exists)? -->
<!-- scope: telescope -->
[Github](https://github.com/nyu-mll/SQuALITY)

#### Download

<!-- info: What is the link to where the original dataset is hosted? -->
<!-- scope: telescope -->
[Github](https://github.com/nyu-mll/SQuALITY/data)

#### Paper

<!-- info: What is the link to the paper describing the dataset (open access preferred)? -->
<!-- scope: telescope -->
[ArXiv](https://arxiv.org/abs/2205.11465)

#### BibTex

<!-- info: Provide the BibTex-formatted reference for the dataset. Please use the correct published version (ACL anthology, etc.) instead of google scholar created Bibtex. -->
<!-- scope: microscope -->
```
@article{wang2022squality,
  title={S{Q}u{ALITY}: Building a Long-Document Summarization Dataset the Hard Way},
  author={Wang, Alex and Pang, Richard Yuanzhe and Chen, Angelica and Phang, Jason and Bowman, Samuel R.},
  journal={arXiv preprint 2205.11465},
  year={2022}
}
```

#### Contact Name

<!-- quick -->
<!-- info: If known, provide the name of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
Alex Wang

#### Contact Email

<!-- info: If known, provide the email of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
wangalexc@gmail.com

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

#### Covered Dialects

<!-- info: What dialects are covered? Are there multiple dialects per language? -->
<!-- scope: periscope -->
stories: 1930--1970 American English
summaries: modern American English

#### Covered Languages

<!-- quick -->
<!-- info: What languages/dialects are covered in the dataset? -->
<!-- scope: telescope -->
`English`

#### Whose Language?

<!-- info: Whose language is in the dataset? -->
<!-- scope: periscope -->
stories: 1930--1970 American science fiction writers (predominantly American men)
summaries: Upwork writers (college-educated, native-English) and NYU undergraduates (English-fluent college students)

#### License

<!-- quick -->
<!-- info: What is the license of the dataset? -->
<!-- scope: telescope -->
cc-by-4.0: Creative Commons Attribution 4.0 International

#### Intended Use

<!-- info: What is the intended use of the dataset? -->
<!-- scope: microscope -->
summarization research

#### Primary Task

<!-- info: What primary task does the dataset support? -->
<!-- scope: telescope -->
Summarization

#### Communicative Goal

<!-- quick -->
<!-- info: Provide a short description of the communicative goal of a model trained for this task on this dataset. -->
<!-- scope: periscope -->
Given a question about a particular high-level aspect of a short story, provide a summary about that aspect in the story (e.g., plot, character relationships, setting, theme, etc.).


### Credit

#### Curation Organization Type(s)

<!-- info: In what kind of organization did the dataset curation happen? -->
<!-- scope: telescope -->
`academic`

#### Curation Organization(s)

<!-- info: Name the organization(s). -->
<!-- scope: periscope -->
New York University

#### Dataset Creators

<!-- info: Who created the original dataset? List the people involved in collecting the dataset and their affiliation(s). -->
<!-- scope: microscope -->
Alex Wang (NYU); Angelica Chen (NYU); Richard Yuanzhe Pang (NYU); Nitish Joshi (NYU); Samuel R. Bowman (NYU)

#### Funding

<!-- info: Who funded the data creation? -->
<!-- scope: microscope -->
Eric and Wendy Schmidt; Apple; NSF

#### Who added the Dataset to GEM?

<!-- info: Who contributed to the data card and adding the dataset to GEM? List the people+affiliations involved in creating this data card and who helped integrate this dataset into GEM. -->
<!-- scope: microscope -->
Alex Wang (NYU)


### Dataset Structure

#### Data Fields

<!-- info: List and describe the fields present in the dataset. -->
<!-- scope: telescope -->
* metadata: Project Gutenberg ID, internal UID, Project Gutenberg license
* document: the story
* questions: a list where each element contains
    * question text: the question
    * question number: the order in which workers answered the question
    * responses: a list where each element contains
        * worker ID: anonymous
        * internal UID
        * response text: the response

#### Reason for Structure

<!-- info: How was the dataset structure determined? -->
<!-- scope: microscope -->
The dataset is arranged with responses grouped by question (for ease of multi-reference training and evaluation) and questions grouped by story (to avoid duplicating the story in the dataset)

#### Example Instance

<!-- info: Provide a JSON formatted example of a typical instance in the dataset. -->
<!-- scope: periscope -->
```
{"metadata": {"passage_id": "63833", "uid": "ea0017c487a245668698cf527019b2b6", "license": ""}, "document": "Story omitted for readability", "questions": [{"question_text": "What is the plot of the story?", "question_number": 1, "responses": [{"worker_id": "6", "uid": "0c27bef1b7b644ffba735fdb005f9529", "response_text": "Brevet Lieutenant Commander David Farragut Stryakalski III, AKA Strike, is charged with commanding a run-down and faulty vessel, the Aphrodite. Aphrodite was the brain-child of Harlan Hendricks, an engineer who ushered in new technology ten years back. All three of his creations failed spectacularly, resulting in death and a failed career. The Aphrodite was the only ship to survive, and she is now used for hauling mail back and forth between Venus and Mars.\nStrike and Cob, the Aphrodite\u2019s only executive to last more than six months, recount Strike\u2019s great failures and how he ended up here. He used to fly the Ganymede, but was removed after he left his position to rescue colonists who didn\u2019t need rescuing. Strike was no longer trustworthy in Admiral Gorman\u2019s eyes, so he banished him to the Aphrodite. \nThe circuit that caused the initial demise of Aphrodite was sealed off. After meeting some members of his crew, Strike orders a conference for all personnel and calls in an Engineering Officer, one I.V. Hendricks. \nAfter Lieutenant Ivy Hendricks arrives--not I.V.--Strike immediately insults her by degrading the ship\u2019s designer, Harlan Hendricks. As it turns out, Hendricks is his daughter, and she vows to prove him wrong and all those who doubted her father. \nDespite their initial conflict, Strike and Hendricks\u2019 relationship soon evolves from resentment to respect. During this time, Strike\u2019s confidence in the Aphrodite plummets as she suffers from mechanical issues. \nThe Aphrodite starts to heat up as they get closer to the sun. The refrigeration units could not handle the heat, causing discomfort among the crew. As they get closer, a radar contact reveals that two dreadnaughts, the Lachesis and the Atropos, are doing routine patrolling. Nothing to worry about, except the Atropos had Admiral Gorman on board, hated by Strike and Hendricks.\nStrike and Hendricks make a joke about Gorman falling into the sun. As the temperature steadily climbs, the crew members overheat and begin fighting, resulting in a black eye. A distress signal came through from the Lachesis: the Atropos, with Gorman on board, was tumbling into the sun. The Lachesis was attempting to rescue them with an unbreakable cord, but they too were being pulled in. \nHendricks had fixed the surge-circuit rheostat, the one her father designed, and claimed it could help them rescue the ships. After some tension, Strike agrees and they race down to the sun to pick up the drifting dreadnaughts. \nStrike puts Hendricks in charge, but soon the heat overtakes her, and she is unable to continue. Strike takes over, attaches the Aphrodite to the Lachesis with a cord, and turns on the surge-circuit. They blast themselves out of there, rescuing the two ships and Admiral Gorman at the same time. \nCob and Strike are awarded Spatial Cross awards, while Hendricks is promoted to an engineering position at the Bureau of Ships. The story ends with Cob and Strike flipping through the pages of an address book until they land on Canalopolis, Mars. \n"}, {"worker_id": "1", "uid": "04e79312dede4a0da5993101e55a796a", "response_text": "Strike joins the crew of the Aphrodite after he has made several poor decisions while he was the captain of another spaceship. He is essentially being punished by his boss, Gorman, and put somewhere where he can do little harm. His job is to deliver the mail from Venus to Mars, so it\u2019s pretty straightforward. \n\nWhen he meets the Officer of the Deck, Celia Graham, he immediately becomes uncomfortable. He does not like to work with women in space, although it\u2019s a pretty common occurrence. He holds a captain\u2019s meeting the first day on the job, and he waits to meet his Engineering Officer, I.V. Hendricks. He makes a rude comment about how the man is late for his first meeting, but actually, the female Ivy has already shown up. \n\nAfter meeting Ivy formally, he makes a comment about how the ship Aphrodite was built by an imbecile. Ivy immediately tells him that he\u2019s wrong, and she knows this because the designer of the ship was none other than her own father. \n\nHis first week as captain on the new ship goes very poorly. Several repairs need to be done to Aphrodite, they run  behind schedule, and the new crew members have a tough time getting a handle on Aphrodite\u2019s intricacies. \n\nThe heat index in the ship begins to rise, and the crew members can no longer wear their uniforms without fainting. Suddenly a distress call comes in, and it\u2019s coming from the Atropos, a ship Captained by Gorman, and the Lachesis. The crew members hesitate to take the oldest and most outdated machinery on a rescue trip. Strike has been in trouble for refusing to follow commands before, and he knows it\u2019s a risky move. However, Ivy insists that she knows how to pilot the Aphrodite, and she can save the crew members on the Atropos and the Lachesis from death. They are quickly tumbling towards the sun, and they will perish if someone doesn\u2019t do something quickly. \n\nIvy takes control of the ship, and the heat on the Aphrodite continues to rise steadily. Eventually, she faints from pure heat exhaustion, and she tells Strike that he must take over. He does, and he manages to essentially lasso the other two ships, and with just the right amount of power, he pulls them back into orbit. \n\nAt a bar, after the whole ordeal, Cob pokes fun at Strike for staying on the Aphrodite. He then admits that he actually respects Strike\u2019s loyalty to the ship that saved his reputation. Cob asks about Strike\u2019s relationship with Ivy, but Strike tells him that she has taken her dad\u2019s former job, so she no longer works with him. Strike takes the moment to look up her info, presumably to restart the relationship. \n"}, {"worker_id": "5", "uid": "71efb8636b504f42a6989bb90e360186", "response_text": "The narrative follows commander Strike as he begins his command of the spaceship Aphrodite. Strike comes from a long line of military greats but himself is prone to poor professional decision making.\n\nAs he takes command, the mission is a simple mail run. However, in the course of their journey, they receive word of two ships in dire need of rescue. Strike and his engineering officer, Ivy Hendricks, decide to use the ships extremely risky surge-circuit to aid the ships.\n\nThe rescue is a success and the crew is hailed for its bravery in saving the doomed vessels. "}, {"worker_id": "3", "uid": "8aa46ba8bd2945c98babd7dd2d9ecc38", "response_text": "The story starts in a muddy swamp on Venus, where Strike, a Brevet Lieutenant Commander, is encountering his new ship, the Aphrodite, for the first time. Here on Venusport Base, he is introduced to the executive officer of the ship, a man who goes by Cob. Strike comes from a line of servicemen who were all well respected, but he himself has more of a reputation for causing trouble by saying the wrong things or deviating from mission plans. His reputation preceded him, as Cob had specific questions about some of these events. The Aphrodite was incredibly impressive when it was designed, but did not live up to its expectations. It had been refitted, and the new mission that Strike was to lead was a mail run between Venus and Mars. As he entered the ship, Strike began to meet his new crew, including Celia Graham, his Radar Officer. Strike is not used to women being on ships and is decidedly uncomfortable with the idea. As he is briefing the officers who were already present, Strike is surprised when he meets his new engineering officer, Ivy Hendricks. Ivy is the daughter of the man who designed the ship, and she is cold to Strike at first, as he is to her. However, her expertise in engineering generally, the ship specifically, and other skills as well as piloting, meant that Strike warmed up to her as their mission went on. As the ship was flying towards Mars on their route, the crew picked up a distress signal from the Lachesis, which was trying to pull the Atropos away from the gravitational pull of the sun after it was damaged in an equipment malfunction. The Admiral who had put Strike in charge of the Aphrodite was on the Atropos, and Ivy dislikes him even more than Strike does, but they know they have to try to save the crews. Strike is hesitant, but Ivy has a plan and insists that they try. She has spent all of her free time tinkering with the circuits, and takes charge. She turned the Aphrodite towards the ships in danger, and sends out a cable to connect the Aphrodite to those ships. After they are all connected, the ships continue to spin towards the sun, which causes Ivy to pass out, leaving Strike in charge. He manages to pull the ships into line and send the Aphrodite in the right direction before passing out himself. The Aphrodite has the power to pull everyone away from the Sun\u2019s gravity, but the acceleration knocks everyone out on all three ships. In the end, it was a successful rescue mission of multiple crews. Strike and Cob find themselves in an officer\u2019s club at the end of the story, discussing Ivy\u2019s new job, and Strike acknowledges that Cob is right about the Aphrodite having grown on him, and plans to stay its captain."}]}, {"question_text": "Who is Ivy Hendricks and what happens to her throughout the story?", "question_number": 2, "responses": [{"worker_id": "6", "uid": "0c27bef1b7b644ffba735fdb005f9529", "response_text": "Lieutenant Ivy Hendricks is the daughter of Harlan Hendricks, a formerly respected engineer. He created the surge-circuit, an innovation in interstellar astrogation, and he was awarded a Legion of Merit. He designed three famous ships: the Artemis, the Andromeda, and the Aphrodite, the prototype. Despite being hailed as the latest and greatest in technology, all three ships either exploded or failed. \nAccording to Lieutenant Ivy Hendricks, their failures were due to the lack of education on board. She claimed that her father asked for the crew members to be trained in surge-circuit technology, so they could use it properly and correctly. That wish was not granted and after all three ships failed, his reputation and career were doomed. Admiral Gorman pulled the plug on his career and therefore became the target of all Lieutenant Hendricks\u2019 hate. \nWith a bone to pick, Lieutenant Hendricks, a knowledgeable engineer herself, comes aboard the Aphrodite to serve as her engineer and occasional pilot. She wants to prove to the world that her father\u2019s creation was genius and deserving of praise. \nAlthough they started off on the wrong foot, Lieutenant Hendricks and Strike, her commander, develop a friendship and appreciation for each other. They bond over their deep hatred of Admiral Gorman and the joy of piloting a ship. She soon proves herself to Strike, and he begins to trust her. Their relationship walks the fine line between friendship and romance. \nAs the Aphrodite is attempting to rescue the fallen dreadnaughts, Lieutenant Hendricks comes up with the solution. Due to her constant tinkering on the ship, she had fixed the surge-circuit rheostat and made it ready to use. Initially, no one trusts her, seeing as the last time it was used people died. But Strike\u2019s trust in her is strong and true, so he approves the use of the surge-circuit. Hendricks pilots the ship, but soon becomes too overheated and comes close to fainting. Strike takes over piloting and eventually activates the surge-circuit. It works and they are able to rescue the two ships, one of which had Admiral Gorman, her sworn enemy, onboard. \nLieutenant Hendricks receives a major promotion; she is now an engineer at the Bureau of Ships. She proved them wrong, and restored her father\u2019s legacy and good name. The story ends with their romance left in the air, but Hendricks has much to be proud of. \n"}, {"worker_id": "1", "uid": "04e79312dede4a0da5993101e55a796a", "response_text": "\nLieutenant Ivy Hendricks is the new Engineering Officer on Aphrodite. Strike and Cob assume that Ivy is a man before she arrives because they are sexist and because her name is listed as I.V. in the orders. Ivy is actually the daughter of the man who designed the award-winning craft.\n\nShe is cold and unfriendly towards Strike after she meets him, and that\u2019s probably because he makes a rude comment about the ship which her father created. After a couple weeks of working together, the two begin to get along very well. Strike admires Ivy\u2019s piloting skills and her depth of knowledge about the Aphrodite. \n\nThe two also bond over their shared hatred of Strike\u2019s former boss, Gorman. Strike feels as though he has ruined his career, and Ivy thinks that Gorman torpedoed her father\u2019s career. Ivy wants nothing more than to prove that Gorman is an idiot. \n\nHowever, when Gorman\u2019s ship is hurtling towards the sun and he and his crew members are about to die, Ivy sees that it\u2019s the perfect opportunity to show Gorman just how wrong he was about the ship her father designed. It\u2019s a very dangerous mission, but Ivy is steadfast in her decision and she\u2019s deeply courageous. She pilots the ship for most of the rescue mission, but eventually faints from the extreme heat. She tells Strike that he needs to take over, and he does a great job. \n\nIvy is then promoted, and she moves to Canalopolis, Mars. She now outranks her former Captain, Strike. \n"}, {"worker_id": "5", "uid": "71efb8636b504f42a6989bb90e360186", "response_text": "Ivy Hendricks is the engineering officer assigned to the Aphrodite. She is the daughter of Harlan Hendricks, the ship's original designer. She is fiercely protective of her father's legacy and resents Admiral Gorman for the way he treated him.\n\nHendricks and Strike, form an alliance of sorts after his initial surprise of seeing a woman assigned to this officer's role. When news arrives that two ships are in danger of falling into the sun, Ivy lobbies to use her father's technology to save the ship. Strike agrees to her plan although the risks are high. The Aphrodite eventually saves the ships although Ivy faints in the process from the heat and command has to be taken over by Strike.\n\nThe successful mission results in a promotion for Ivy as she works as a designer in the Bureau of Ships like her father."}, {"worker_id": "3", "uid": "8aa46ba8bd2945c98babd7dd2d9ecc38", "response_text": "Ivy Hendricks is the new engineering officer on the Aphrodite, having been transferred from the Antigone. She is a tall woman with dark hair and contrasting pale blue eyes, who has a very wide range of experience in ship operations and engineering. Her father, Harlan Hendricks, was the man who designed the Aphrodite, so she knows the ship needs a lot of specific training. At first, the captain did not expect her to be a woman, and managed to imply that many people found her father incompetent. Although she seemed cold at first, as she reacted to the situation, she and the captain eventually got along fairly well, as he learned to appreciate her wide skill set that ranged from engineering to piloting. Ivy and Strike also had a common enemy in the higher ranks: Space Admiral Gorman. Once Spike trusted her he appreciated that Ivy spent a lot of spare time working on the old circuits, so she knew the ship like the back of her hand. When the Aphrodite found the Lachesis and the Atropos when following up on a distress signal, Ivy new the ship well enough to be able to formulate a plan to save everyone. She piloted the Aphrodite carefully, using cables shot with a rocket to connect the three ships together, but the spinning of the ships in the heat inside meant that she passed out and had to leave Strike to take over for her. Her plan was successful; she was promoted, and instead of returning to the Aphrodite she started a design job with the Bureau of Ships."}]}, {"question_text": "What is the relationship between Strike and Aphrodite?", "question_number": 3, "responses": [{"worker_id": "6", "uid": "0c27bef1b7b644ffba735fdb005f9529", "response_text": "Strike is a member of a famous, well-behaved, and well-trained service family. His father and grandfather served in World War II and the Atomic War, respectively. Both earned medals for their heroic service. Strike, however, did not follow in his family\u2019s footsteps. \n\tWith a tendency to say the wrong thing at the wrong time, Strike often offended those around him and garnered a negative reputation. After being put in charge of the Ganymede, he soon lost his position after abandoning his station to rescue colonists who were not in danger. As well, he accused a Martian Ambassador of being a spy at a respectable ball. Admiral Gorman soon demoted him, and he became the commander of the Aphrodite. \n\tAt first, Strike was not a fan. He sees her as ugly, fat, and cantankerous. He misses the Ganymede, a shiny and new rocketship, and views the Aphrodite as less-than. \n\tWithin the first week of flying her, the Aphrodite had a burned steering tube, which made it necessary to go into free-fall as the damage control party made repairs. Strike\u2019s faith in Lover-Girl continued to plummet. \n\tHowever, after Lieutenant Hendricks, the resident engineer, got her hands on the Aphrodite, Strike\u2019s opinion started to change. Her knowledge of the ship, engineering, and piloting helped him gain confidence in both her abilities and those of Aphrodite.\nNear the end of the story, the Aphrodite is tasked with rescuing two ships that are falling into the sun. Previously Lieutenant Hendricks had fixed up the surge-circuit rheostat, and so she offered it up as the only solution. Strike agrees to try it, which shows his faith and trust in the Aphrodite. Luckily, all things go to plan, and the Aphrodite, with Strike piloting, is able to save the two ships and Admiral Gorman. \nAfter Strike won a medal himself, finally following in the family footsteps, he is offered his old position back on the Ganymede. He refuses, and instead returns to old Lover-Girl. He has grown fond of her over the course of their adventure, and they develop a partnership. "}, {"worker_id": "1", "uid": "04e79312dede4a0da5993101e55a796a", "response_text": "Strike is completely unimpressed by the rocket ship Aphrodite. He comments that she looks like a pregnant carp, and he knows that he\u2019s been assigned captain of the ship because he messed up terribly on his other missions. \n\nAphrodite was built 10 years ago, and now she is completely outdated and a laughing stock compared to the other spaceships in the fleet.  She was designed by Harlan Hendricks, and the engineer received a Legion of Merit award for her design. \n\nStrike\u2019s mission is to fly Aphrodite to take the mail from Venusport to Canalopolis, Mars. It\u2019s boring and straightforward.\n\nWhen a disaster occurs and two other ships, the Atropos and the Lachesis, are in serious danger of getting too close to the sun, Strike agrees to take the old girl on a rescue mission. He is convinced by Ivy, since she knows the ship better than anyone else and she believes in her. \n\nAlthough Ivy takes Aphrodite most of the way there, its Strike who finishes the mission and saves his former boss, Gorman, and many other people from certain death. Aphrodite is the entire reason that Strike is able to mend his terrible reputation and he wins back respect from Gorman. Although they got off to a rocky start, Strike finds it impossible to leave his best girl, even when he is offered a job on another ship. He is loyal to the ship that made him a hero. \n"}, {"worker_id": "5", "uid": "71efb8636b504f42a6989bb90e360186", "response_text": "Strike is assigned to be commander of the spaceship Aphrodite. The ship is assigned as a mail carrier for the inner part of the solar system. The Aphrodite is a dilapidated design with an awful reputation. Strike ended up with the Aphrodite as a result of a series of poor professional decisions that resulted in him getting command of the more prestigious ship Ganymede taken away from him.\n\nHis initial impression of the Aphrodite softens to a grudging respect after the successful mission to save the Atropos and Lachesis. Although he presumably is in line to command the Ganymede again, another faux pas resulting in Strike continuing to command the Aphrodite.   "}, {"worker_id": "3", "uid": "8aa46ba8bd2945c98babd7dd2d9ecc38", "response_text": "At the beginning of the story, Strike is very reluctant to accept Aphrodite, because being in charge of the ship means a demotion for him. His perception of the ship at the beginning of the story is colored by this history, and his first impression of the ship is not a positive one, even from the outside. Besides the actual construction of the ship, the technology that ran it was not something he showed much faith in. The first week that he was in charge after leaving Venus, it seemed things were going drastically wrong. When one important piece of equipment burnt out, the ship went into freefall, requiring a lot of repair work from the engineers, and anyone in charge of navigation was handed more work because of this as well. The ship was really put to the test when the Aphrodite responded to the distress call from the Lachesis, whose crew was trying to keep the Atropos from falling into the sun. Because Ivy knew the Aphrodite so well, and had been working on the circuits, it turned out the Aphrodite was the perfect ship to save the day. She could not see the rescue all the way through to the end, because she passed out early, but Strike was conscious a little bit longer and took over until he also passed out. After this unexpected rescue mission, Cob, the Executive Officer, noted that Strike has a newfound appreciation for the ship, and has no intention of leaving. Strike is dedicated to his new mission, even though at the beginning of the story he wanted nothing more than to pilot something the same rank as his old ship."}]}, {"question_text": "Describe the setting of the story.", "question_number": 4, "responses": [{"worker_id": "6", "uid": "0c27bef1b7b644ffba735fdb005f9529", "response_text": "Jinx Ship to the Rescue by Alfred Coppel, Jr. takes place in space, but more specifically in the Aphrodite. \n\tIt starts in the muddy Venusport Base on Venus. Venusport is famous for its warm, slimy, and green rain that falls for 480 hours of every day. A fog rolls in and degrades visibility. \n\tDespite starting on Venusport Base, the characters actually spend most of their time onboard the Aphrodite, a Tellurian Rocket Ship. The Aphrodite had a surge-circuit monitor of twenty guns built into her frame. She was bulky, fat, and ugly, and occasionally had some technical and mechanical struggles as well. \n\tAlthough her frame may not be appealing, she soon becomes victorious as she gains the trust of Strike and other members of his crew and saves two fallen dreadnaughts. With her surge-circuit rheostat rebuilt, the Aphrodite is finally able to accomplish what she was always meant to. "}, {"worker_id": "1", "uid": "04e79312dede4a0da5993101e55a796a", "response_text": "The story starts on the planet of Venus. Venus has days that are 720 hours long, and rain is common. The rain is hot, slimy, and green, and it makes the already wet swamplands even more mushy. Fog is common on Venus.\n\nThe middle of the story takes place on the old and outdated ship, Aphrodite. She gives the crew members a lot of trouble on their first mission. She is in dire need of repairs, she\u2019s slow, and it\u2019s impossible to control her temperature. The crew members are unable to wear their uniforms because the temperature is over 100 degrees. \n\nAphrodite\u2019s mission is simple. She needs to take the mail from Venus to Mars, and it\u2019s the only thing she can be trusted to do successfully. So it\u2019s very impressive when she ends up being the hero of the day and manages to rescue two other ships that are headed towards the sun. \n"}, {"worker_id": "5", "uid": "71efb8636b504f42a6989bb90e360186", "response_text": "The narrative is set in the early 21st century primarily aboard the spaceship Aphrodite. The ship's mission is to deliver mail in the inner part of the solar system.\n\nThe ships route takes them around the sun and as a result the ambient temperature inside the ship begins to rise to intolerable levels due to proximity to the sun. Because of the heat, the coed crew is allowed to operate with very little clothing. Aphrodite is a ship of an outdated design that gives it a lack of comfort and subjects it to numerous small problems that make its operation frustrating."}, {"worker_id": "3", "uid": "8aa46ba8bd2945c98babd7dd2d9ecc38", "response_text": "The story starts at a spaceport on Venus, where it has been raining for hundreds of hours straight. The rain has stopped by the time the story starts, but it is left a lot of mud in the swampy marshes. It was nearing the end of the day, and the fog was enveloping the surroundings as it grew darker outside. It was hot and sticky at Venusport Base, but after Strike left the service on his mission in the Aphrodite, it would only grow hotter on board. The ship itself, where most of the story takes place, is an older, refitted, bulky type of ship. There were only two others like it, and their designer had been awarded a Legion of Merit for the three. However, this is the only one still in use, as the others were destroyed in a much earlier mission. Strike\u2019s disappointment in the ship seems to mirror the sentiment. Inside the ship, there are many systems of pipes connected the control panels, and the captain had to navigate carefully so that he didn\u2019t hit his head on the bulkhead. While in space, as the ship flew closer and closer to the sun, the interior of the ship grew hotter and hotter. The crew opted to wear as little clothing as possible in an attempt to handle the heat. When the Aphrodite received the distress call from the Lachesis, the ships were close enough to the sun to be affected by its gravitational pull. After the close call near the sun, once everyone regained consciousness, the story ends at an officer\u2019s club on Mars. It was a formal environment, and the Aphrodite\u2019s captain and executive officer planned the rest of their route from there."}]}, {"question_text": "Who is Strike and what happens to him throughout the story?", "question_number": 5, "responses": [{"worker_id": "6", "uid": "0c27bef1b7b644ffba735fdb005f9529", "response_text": "Strike is a member of an esteemed service family on Venus; seven generations of well-behaved and well-trained operators. Unfortunately, Strike struggles to carry on the family tradition, and is known for misspeaking and offending those around him. By trusting his gut, he wound up failing his higher-ups and crew several times. All this culminated in an eventual mistrust of Strike, which led to him being charged with the Aphrodite. \n\tHis deep hatred of Space Admiral Gordon is passionate, but not without reason. Gordon is the one who demoted him to the Aphrodite. At the start, Strike is checking out his new vessel and notes how ugly the ship is. After examining the ship and it\u2019s crew, it is revealed that Strike is uncomfortable around women and believes they don\u2019t belong on a spaceship. \n\tIn order to start flying, he calls in an expert engineer to come aboard and travel with them. Thinking I.V. Hendricks is a man, he is excited to have them onboard. But when Ivy Hendricks shows up, a female engineer and the daughter of the Aphrodite\u2019s creator, his world is soon turned upside down. \n\tHis initial negative reaction to her is soon displaced by begrudging appreciation and eventually trust and friendship. Hendricks proves his previous theories about women wrong, and Strike is forced to accept that perhaps women do belong on a spaceship. She especially impresses him with her total knowledge of spaceship engineering and the Aphrodite in general. And it helped that she hated Admiral Gorman just as much as Strike, if not more. \n\tWhile flying by the sun to deliver mail, the Aphrodite receives a distress call from two ships: the Lachesis and the Atropos, the latter of which carried Admiral Gorman onboard. After the Aphrodite reached orbit, the Lachesis reached out and reported the Atropos was falling into the sun, due to a burst chamber. They couldn\u2019t move those onboard over thanks to all the radiation, so the Lachesis was attempting to pull the Atropos back using an unbreakable cord. But it wasn\u2019t enough. \n\tSince Ivy Hendricks had fixed the surge-circuit rheostat--the feature that crashed the original Aphrodite--, they were able to save the Lachesis and the Atropos and regain some of their dignity and former glory. \n\tStrike is awarded the Spatial Cross, as well as Cob, his friend and longtime executive of the Aphrodite. Strike was asked to return to the Ganymede, a beautiful sleek ship, but allegedly said the wrong thing to Gorman, and was instead sent back to the Aphrodite. Cob believes he did it on purpose, as Strike had grown quite fond of Lover-Girl. \n\tIvy has gone to the Bureau of Ships to engineer vessels, a great upgrade from her previous job. Cob pressures Strike to reach out to her, but he refuses. However, it ends on a hopeful note, with the potential for romance between Strike and Hendricks, and even more adventures on the clunky Aphrodite. "}, {"worker_id": "1", "uid": "04e79312dede4a0da5993101e55a796a", "response_text": "Strike\u2019s real name is Brevet Lieutenant Commander David Farragut Strykalski III. After serving on the Ganymede, he is put in charge of the Aphrodite. He comes from many generations of officers. However, he doesn\u2019t feel like he fits the mold of his grandfather and great-grandfather and so on. His boss, Gorman, disagreed with several decisions he made in the past and sent him to work on the Aphrodite, the unimpressive spaceship.\n\nStrike does not like working with women in space, so he is disappointed when two of his crew members are powerful and successful females. He learns his lesson after working with Ivy Hendricks for a few weeks. She impresses him with her piloting skills and her knowledge of the ship that her father designed. \n\nStrike is skeptical at first when Ivy wants to take Aphrodite to rescue two ships whose crew members are in grave danger. He knows that the mistakes he made before got him on the Aphrodite, and there\u2019s a big chance that he\u2019ll be fired for trying to save the day, or worse, the mission could end in death for him and all of his crew members. He has feelings for Ivy, and her intense passion convinces him that she\u2019s right, Aphrodite can handle the mission and they can save those peoples\u2019 lives.\n\nIvy pilots the ship almost the entire route, but she is unable to finish the job when she passes out from the intense heat. Captain Strike takes over and saves the crews on the Atropos and the Lachesis. He is hailed as a hero, and he repairs his terrible reputation with the selfless act. He decides not to leave the Aphrodite. He wants to be loyal to the ship that worked so hard for him. He does decide to give Ivy a call. Even though she outranks him, he has to admit that he has a crush on her. "}, {"worker_id": "5", "uid": "71efb8636b504f42a6989bb90e360186", "response_text": "Strike is the commander of the Aphrodite. He was originally the commander of the prestigious Ganymede. However a number of decisions made out of bravado as well as some unprofessional comments lost him that command.\n\nNow in command of a dilapidated ship, Strike comes to terms with his job. He commands a crew including a large number of women which makes him somewhat uncomfortable. His engineering officer Ivy Hendricks in particular seems to be of romantic interest to Strike.\n\nStrike ends up teaming with Ivy to save two ships from falling into the sun earning him a small promotion but an ill-advised comment prevents him from leaving the Aphrodite, perhaps to the satisfaction of Strike himself."}, {"worker_id": "3", "uid": "8aa46ba8bd2945c98babd7dd2d9ecc38", "response_text": "Strike is a highly decorated lieutenant commander in the Navy, who comes from a long line of ship operators. Although he has run many successful missions, he has a reputation of causing trouble\u2014his new Executive Officer, Cob, has heard a number of stories that he asks Strike for details about. Strike has lost command of the ship that he had been captaining, and is sent by Admiral Gorman to captain a mail route on the Aphrodite. He is extremely hesitant to have any positive feelings about the experience, from the ship itself, to the inclusion of women on its crew. Not only is this not the type of ship he is used to, he is never served with women on board. He has to navigate adapting to the new situation while adapting to the new job. Through the first week of his assignment, the ship and its crew grow on him. He comes to trust Ivy Hendricks, the Engineering Officer, and he lets her take charge to try to save the other ships when they respond to a distress call. Eventually, she passes out, and has to leave Strike in charge of getting the ships to safety. Eventually,  Strike passes out just like everyone else, from the ship\u2019s acceleration to break the sun\u2019s gravity. At the end of the story, it is clear that his increased appreciation for the ship means he plans on staying, to the delight of his Executive Officer. Cob alludes to Strike having feelings for Ivy, but he says that although she is nice, he has no interest in being with a woman with a higher ranked title than he has. "}]}]}
```

#### Data Splits

<!-- info: Describe and name the splits in the dataset if there are more than one. -->
<!-- scope: periscope -->
train, dev, test

#### Splitting Criteria

<!-- info: Describe any criteria for splitting the data, if used. If there are differences between the splits (e.g., if the training annotations are machine-generated and the dev and test ones are created by humans, or if different numbers of annotators contributed to each example), describe them here. -->
<!-- scope: microscope -->
Stories that appear in both SQuALITY and [QuALITY](https://github.com/nyu-mll/quality) are assigned to the same split in both datasets.



## Dataset in GEM

### Rationale for Inclusion in GEM

#### Why is the Dataset in GEM?

<!-- info: What does this dataset contribute toward better generation evaluation and why is it part of GEM? -->
<!-- scope: microscope -->
The summaries in the dataset were crowdsourced, allowing us to use input documents that are easily understood by crowdworkers (as opposed to technical domains, such as scientific papers). Additionally, there is no lede bias in stories, as is typically in news articles used in benchmark summarization datasets like CNN/DM and XSum.

Additionally, the dataset is multi-reference and the references for each task are highly diverse. Having a diverse set of references better represents the set of acceptable summaries for an input, and opens the door for creative evaluation methodologies using these multiple references.

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
The inputs (story-question pairs) are multi-reference. The questions are high-level and are written to draw from multiple parts of the story, instead of a single section of the story.


### GEM-Specific Curation

#### Modificatied for GEM?

<!-- info: Has the GEM version of the dataset been modified in any way (data, processing, splits) from the original curated data? -->
<!-- scope: telescope -->
no

#### Additional Splits?

<!-- info: Does GEM provide additional splits to the dataset? -->
<!-- scope: telescope -->
no


### Getting Started with the Task

#### Pointers to Resources

<!-- info: Getting started with in-depth research on the task. Add relevant pointers to resources that researchers can consult when they want to get started digging deeper into the task. -->
<!-- scope: microscope -->
* [original paper](https://arxiv.org/abs/2205.11465)
* [modeling question-focused summarization](https://arxiv.org/abs/2112.07637)
* [similar task format but different domain](https://arxiv.org/abs/2104.05938)




## Previous Results

### Previous Results

#### Metrics

<!-- info: What metrics are typically used for this task? -->
<!-- scope: periscope -->
`ROUGE`, `BERT-Score`

#### Proposed Evaluation

<!-- info: List and describe the purpose of the metrics and evaluation methodology (including human evaluation) that the dataset creators used when introducing this task. -->
<!-- scope: microscope -->
Following norms in summarization, we have evaluated with automatic evaluation metrics like ROUGE and BERTScore, but these metrics do not correlate with human judgments of summary quality when comparing model summaries (see paper for details). 

We highly recommend users of the benchmark use human evaluation as the primary method for evaluating systems. We present one example of such in the paper in which we ask Upwork workers to read the short story and then rate sets of three responses to each question. While this is close to the gold standard in how we would want to evaluate systems on this task, we recognize that finding workers who will read the whole story (~30m) is difficult and expensive, and doing efficient human evaluation for long document tasks is an open problem.

#### Previous results available?

<!-- info: Are previous results available? -->
<!-- scope: telescope -->
yes

#### Other Evaluation Approaches

<!-- info: What evaluation approaches have others used? -->
<!-- scope: periscope -->
Human evaluation

#### Relevant Previous Results

<!-- info: What are the most relevant previous results for this task/dataset? -->
<!-- scope: microscope -->
See paper (https://arxiv.org/abs/2205.11465)



## Dataset Curation

### Original Curation

#### Sourced from Different Sources

<!-- info: Is the dataset aggregated from different data sources? -->
<!-- scope: telescope -->
no


### Language Data

#### How was Language Data Obtained?

<!-- info: How was the language data obtained? -->
<!-- scope: telescope -->
`Crowdsourced`

#### Where was it crowdsourced?

<!-- info: If crowdsourced, where from? -->
<!-- scope: periscope -->
`Other crowdworker platform`

#### Language Producers

<!-- info: What further information do we have on the language producers? -->
<!-- scope: microscope -->
Upwork: US-born, native English speakers with backgrounds in the humanities and copywriting

NYU undergraduates: English-fluent undergraduates from a diverse set of nationalities and majors



#### Topics Covered

<!-- info: Does the language in the dataset focus on specific topics? How would you describe them? -->
<!-- scope: periscope -->
The short stories are primarily science fiction and from the 1930s -- 1970s.

#### Data Validation

<!-- info: Was the text validated by a different worker or a data curator? -->
<!-- scope: telescope -->
validated by crowdworker

#### Was Data Filtered?

<!-- info: Were text instances selected or filtered? -->
<!-- scope: telescope -->
not filtered


### Structured Annotations

#### Additional Annotations?

<!-- quick -->
<!-- info: Does the dataset have additional annotations for each instance? -->
<!-- scope: telescope -->
crowd-sourced

#### Number of Raters

<!-- info: What is the number of raters -->
<!-- scope: telescope -->
11<n<50

#### Rater Qualifications

<!-- info: Describe the qualifications required of an annotator. -->
<!-- scope: periscope -->
English-fluent, with experience reading and writing about literature

#### Raters per Training Example

<!-- info: How many annotators saw each training example? -->
<!-- scope: periscope -->
4

#### Raters per Test Example

<!-- info: How many annotators saw each test example? -->
<!-- scope: periscope -->
4

#### Annotation Service?

<!-- info: Was an annotation service used? -->
<!-- scope: telescope -->
no

#### Any Quality Control?

<!-- info: Quality control measures? -->
<!-- scope: telescope -->
validated by another rater

#### Quality Control Details

<!-- info: Describe the quality control measures that were taken. -->
<!-- scope: microscope -->
Each response was reviewed by three reviewers, who ranked the response (against two other responses), highlighted errors in the response, and provided feedback to the original response writer.


### Consent

#### Any Consent Policy?

<!-- info: Was there a consent policy involved when gathering the data? -->
<!-- scope: telescope -->
yes

#### Consent Policy Details

<!-- info: What was the consent policy? -->
<!-- scope: microscope -->
Writers were informed that their writing and reviewing would be used in the development of AI.


### Private Identifying Information (PII)

#### Contains PII?

<!-- quick -->
<!-- info: Does the source language data likely contain Personal Identifying Information about the data creators or subjects? -->
<!-- scope: telescope -->
unlikely

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
yes



## Considerations for Using the Data

### PII Risks and Liability



### Licenses

#### Copyright Restrictions on the Dataset

<!-- info: Based on your answers in the Intended Use part of the Data Overview Section, which of the following best describe the copyright and licensing status of the dataset? -->
<!-- scope: periscope -->
`open license - commercial use allowed`

#### Copyright Restrictions on the Language Data

<!-- info: Based on your answers in the Language part of the Data Curation Section, which of the following best describe the copyright and licensing status of the underlying language data? -->
<!-- scope: periscope -->
`public domain`


### Known Technical Limitations

#### Unsuited Applications

<!-- info: When using a model trained on this dataset in a setting where users or the public may interact with its predictions, what are some pitfalls to look out for? In particular, describe some applications of the general task featured in this dataset that its curation or properties make it less suitable for. -->
<!-- scope: microscope -->
The stories in the dataset are from the 1930--1970s and may contain harmful stances on topics like race and gender. Models trained on the stories may reproduce these stances in their outputs.

#### Discouraged Use Cases

<!-- info: What are some discouraged use cases of a model trained to maximize the proposed metrics on this dataset? In particular, think about settings where decisions made by a model that performs reasonably well on the metric my still have strong negative consequences for user or members of the public. -->
<!-- scope: microscope -->
The proposed automatic metrics for this dataset (ROUGE, BERTScore) are not sensitive to factual errors in summaries, and have been shown to not correlate well with human judgments of summary quality along a number of axes.


