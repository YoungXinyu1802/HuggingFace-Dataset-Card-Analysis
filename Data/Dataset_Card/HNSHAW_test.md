from transformers import BertTokenizer, BertModel
import numpy as np

# Load the pre-trained BERT model and tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# Define the search query
query = "deep learning"

# Tokenize the query and convert to input IDs and attention mask
tokenized_query = tokenizer.encode_plus(query, add_special_tokens=True, 
                                         return_token_type_ids=False, 
                                         padding='max_length', truncation=True, 
                                         max_length=64, return_attention_mask=True)

# Convert the input IDs and attention mask to PyTorch tensors
query_ids = torch.tensor(tokenized_query['input_ids']).unsqueeze(0)
query_mask = torch.tensor(tokenized_query['attention_mask']).unsqueeze(0)

# Pass the query through the BERT model to get the embeddings
with torch.no_grad():
    query_embedding = model(query_ids, attention_mask=query_mask)[0][:, 0, :].numpy()

# Define a list of documents to search
documents = ["Machine learning is the future of computing", 
             "Deep learning is a subset of machine learning",
             "Artificial intelligence is the science of making intelligent machines",
             "Neural networks are used in deep learning"]

# Tokenize and embed the documents
document_embeddings = []
for document in documents:
    # Tokenize the document and convert to input IDs and attention mask
    tokenized_document = tokenizer.encode_plus(document, add_special_tokens=True, 
                                                return_token_type_ids=False, 
                                                padding='max_length', truncation=True, 
                                                max_length=64, return_attention_mask=True)
    # Convert the input IDs and attention mask to PyTorch tensors
    document_ids = torch.tensor(tokenized_document['input_ids']).unsqueeze(0)
    document_mask = torch.tensor(tokenized_document['attention_mask']).unsqueeze(0)
    
    # Pass the document through the BERT model to get the embeddings
    with torch.no_grad():
        document_embedding = model(document_ids, attention_mask=document_mask)[0][:, 0, :].numpy()
        
    # Add the document embedding to the list of document embeddings
    document_embeddings.append(document_embedding)

# Compute the cosine similarity between the query and each document
similarities = []
for document_embedding in document_embeddings:
    similarity = np.dot(query_embedding, document_embedding.T) / (np.linalg.norm(query_embedding) * np.linalg.norm(document_embedding))
    similarities.append(similarity)

# Sort the documents by similarity score
sorted_documents = [x for _, x in sorted(zip(similarities, documents), reverse=True)]

# Print the top 3 most similar documents
print(sorted_documents[:3])
