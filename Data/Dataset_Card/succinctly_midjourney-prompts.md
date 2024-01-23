---
license: apache-2.0
---
[Midjourney](https://midjourney.com) is an independent research lab whose broad mission is to "explore new mediums of thought". In 2022, they launched a text-to-image service that, given a natural language prompt, produces visual depictions that are faithful to the description. Their service is accessible via a public [Discord server](https://discord.com/invite/midjourney): users issue a query in natural language, and the Midjourney bot returns AI-generated images that follow the given description. The raw dataset (with Discord messages) can be found on Kaggle: [Midjourney User Prompts & Generated Images (250k)](https://www.kaggle.com/datasets/succinctlyai/midjourney-texttoimage). The authors of the scraped dataset have no affiliation to Midjourney.

This HuggingFace dataset was [processed](https://www.kaggle.com/code/succinctlyai/midjourney-text-prompts-huggingface) from the raw Discord messages to solely include the text prompts issued by the user (thus excluding the generated images and any other metadata). It could be used, for instance, to fine-tune a large language model to produce or auto-complete creative prompts for image generation.

Check out [succinctly/text2image-prompt-generator](https://huggingface.co/succinctly/text2image-prompt-generator), a GPT-2 model fine-tuned on this dataset.