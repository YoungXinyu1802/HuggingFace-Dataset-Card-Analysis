---
license: apache-2.0
task_categories:
- question-answering
- summarization
- conversational
- sentence-similarity
language:
- en
pretty_name: Embeddings for George Orwell's 1984
tags:
- faiss
- langchain
- instructor embeddings
- vector stores
- books
- LLM
---
# Vector store of embeddings for the book "1984" by George Orwell

This is a [faiss](https://github.com/facebookresearch/faiss) vector store created with [instructor embeddings](https://github.com/HKUNLP/instructor-embedding) using [LangChain](https://langchain.readthedocs.io/en/latest/modules/indexes/examples/embeddings.html#instructembeddings) . Use it for similarity search, question answering or anything else that leverages embeddings! 😃

Creating these embeddings can take a while so here's a convenient, downloadable one 🤗


## How to use

1. Download data
2. Load to use with LangChain

pip install -qqq langchain InstructorEmbedding sentence_transformers faiss-cpu huggingface_hub

```python
import os
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.vectorstores.faiss import FAISS
from huggingface_hub import snapshot_download

# download the `vectorstore` folder
cache_dir="orwell_faiss"
vectorstore = snapshot_download(repo_id="calmgoose/orwell-1984_faiss-instructembeddings",
                                repo_type="dataset",
                                revision="main",
                                allow_patterns="vectorstore/*",
                                cache_dir=cache_dir,
                                )

# get path to the `vectorstore` folder that you just downloaded
# we'll look inside the `cache_dir` for the folder we want
target_dir = "vectorstore"

# Walk through the directory tree recursively
for root, dirs, files in os.walk(cache_dir):
    # Check if the target directory is in the list of directories
    if target_dir in dirs:
        # Get the full path of the target directory
        target_path = os.path.join(root, target_dir)

# load embeddings
# this is what was used to create embeddings for the book
embeddings = HuggingFaceInstructEmbeddings(
    embed_instruction="Represent the book passage for retrieval: ",
    query_instruction="Represent the question for retrieving supporting texts from the book passage: "
    )

# load vector store to use with langchain
docsearch = FAISS.load_local(folder_path=target_path, embeddings=embeddings)

# similarity search
question = "Who is big brother?"
search = docsearch.similarity_search(question, k=4)

for item in search:
    print(item.page_content)
    print(f"From page: {item.metadata['page']}")
    print("---")
```