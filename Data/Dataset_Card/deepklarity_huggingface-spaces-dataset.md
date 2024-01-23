---
license: cc
---

This dataset provides information of all the spaces (~6,200 at time of snapshot) created on [HuggingFace Spaces](https://huggingface.co/spaces) 🤗. Most of the data comes from a public API endpoint while some of the data is enriched by web scraping. The dataset is intended to provide a snapshot of the spaces and was last updated in first week of *July-2022*. 

Along with the name of the space, the dataset consists of following columns:
- likes (number of likes on the space)
- sdk (streamlit,gradio or other)
- status (was running successfully or had error when snapshot was taken)
- total_commits (number of commits in the space)
- last_commit (when did last commit happen)
- community_interactions (number of interactions in the newly introduced Community tab)

Apart from these, we have also added some post-processing columns (where space was using gradio):
- inputs (Image/Text/Slider etc)
- outputs (Image/Audio/Textbox etc)
- ai_ml_reqs (If the requirements.txt contain a popular ML repo dependency like: torch, tensorflow, pandas, sklearn, scipy etc) 


Contributors:
- [Abdullah Meda](https://www.linkedin.com/in/abdmeda/)
- [Ayush Ranwa](https://twitter.com/Ayushranwa6)
- [Deepak Rawat](https://twitter.com/dsr_ai)
- [Kartik Godawat](https://twitter.com/kartik_godawat)

Please reach out to us for any queries or discussions.

