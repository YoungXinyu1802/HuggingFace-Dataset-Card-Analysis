# Playlist Generator Dataset

This dataset contains three files, used in the [Playlist Generator](https://huggingface.co/spaces/NimaBoscarino/playlist-generator) space. Visit the blog post to learn more about the project: https://huggingface.co/blog/your-first-ml-project

1. `verse-embeddings.pkl` contains Sentence Transformer embeddings for each verse for each song in a private (unreleased) dataset of song lyrics. The embeddings were generated using this model: https://huggingface.co/sentence-transformers/msmarco-MiniLM-L-6-v3
2. `verses.csv` maps each verse to a song ID. The indices in `verse-embeddings.pkl` correspond with the indices in this CSV file.
3. `songs_new.csv` contains information about each song, such as the title, artist, and a link to the album art (if available)