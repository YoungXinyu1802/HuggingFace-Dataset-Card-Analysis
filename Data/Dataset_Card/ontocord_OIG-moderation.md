---
license: apache-2.0
---
# This is the Open Instruction Generalist - Moderation Dataset
This is our attempt to create a diverse dataset of dialogue that may be related to NSFW subject matters, abuse eliciting text, privacy violation eliciting instructions, depression or related content, hate speech, and other similar topics. We use the [prosocial], [anthropic redteam], subsets of [English wikipedia] datasets along with other public datasets and data created or contributed by volunteers. To regularize the dataset we also have "regular" OIG instructions, which includes Q/A instructions, coding instructions, and similar types of queries. Currently there are two versions of the datasets, but more will be created.

- OIG_safety_v0.1.jsonl (66200)
- OIG_safety_v0.2.jsonl (134530)
  
OIG-moderation includes data from:
Public datasets such as anthropic-redteam and anthropic-harmless, prosocial, and contributed datasets from community members
Augmented toxic data such as civil comments data converted into instructions, (c) anthropic-redteam data augmented with prosocial tags
Data provided by the LAION community that might include NSFW prompt
Synthetic depression data generated from a public depression bag of words dataset using https://huggingface.co/pszemraj/flan-t5-large-grammar-synthesis. 
A model trained on the OIG-moderation dataset can be used to provide moderation labels, and the bot providers can choose to then block responses from their chatbots based on these labels. If a bot provider's policy for example permits sexual content, but prohibits PII eliciting text, they can hopefully do so with the output of a model trained on this data.
The tags consist of (a) Base prosocial tags: casual, possibly needs caution, probably needs caution, needs caution, needs intervention and (b) Additional tags: abuse related, personal information related, sexual content, hate.
An utterance can have more than one tag. For example, a wikipedia article about pornography content might be tagged: needs caution | sexual content.
## Acknowledgement
We would like to thank all the following people for their amazing contirbutions: @Rallio, @Summer, @Iamiakk @Jue, @yp_yurilee, @Jjmachan, @Coco.han, @Pszemraj, and many others.
We would like to thank Together.xyz for testing the v0.1 data for effectiveness and their dedication to the open source community.
We would like to thank AI Horde and user @Db0 for their incredible contribution of filtered data that were flagged as unethical.
## Disclaimer
These datasets contain synthetic data and in some cases data that includes NSFW subject matter and triggering text such as toxic/offensive/trolling things. If you are concerned about the presence of this type of material in the dataset please make sure you carefully inspect each of the entries and filter appropriately. Our goal is for the model to be as helpful and non-toxic as possible and we are actively evaluating ways to help create models that can detect potentially unwanted or problematic instructions or content.
## Risk Factors
While we acknowledge that this dataset can be modified to train a model to generate unsafe text, it is important to release this publicly as a resource for both researchers and those building production agents to train detection models. 
