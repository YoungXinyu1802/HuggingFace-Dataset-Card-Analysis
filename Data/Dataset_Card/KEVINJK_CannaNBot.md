tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
model = RobertaForQuestionAnswering.from_pretrained('roberta-base')
import torch
from transformers import RobertaTokenizer, RobertaForQuestionAnswering
from sklearn.model_selection import train_test_split
import pandas as pd

# Load the pre-trained RoBERTa tokenizer and model
tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
model = RobertaForQuestionAnswering.from_pretrained('roberta-base')

# Define the preprocessed data as a list of tuples, where the first element is the question and the second element is the answer
data = [("What types of products do you sell?", "We offer a wide range of cannabis products, including dried flowers, pre-rolls, oils, capsules, and accessories."), 
        ("How do I place an order?", "You can place an order on our website or by calling our customer service line."), 
        ("How long will it take to receive my order?", "Orders are typically processed and shipped within 1-2 business days. Shipping times vary depending on your location and the shipping method you choose."),
        ("What payment methods do you accept?", "We accept Visa, Mastercard, and American Express credit cards, as well as Visa Debit and Mastercard Debit cards. You can also pay with an electronic funds transfer (EFT) from your bank account."),
        ("Do you offer free shipping?", "We offer free shipping on orders over $99 (before taxes and shipping fees) to most locations in Canada."),
        ("Can I track my order?", "Yes, you will receive a confirmation email with a tracking number once your order has shipped. You can use the tracking number to check the status of your order on the carrier's website."),
        ("What are your store hours?", "Our stores are open Monday to Sunday from 10:00am to 9:00pm."),
        ("Where are your store locations?", "We have several retail locations across New Brunswick. You can find a list of our stores and their addresses on our website."),
        ("What is your return policy?", "We do not accept returns on cannabis products due to health and safety regulations. However, if you receive a damaged or defective product, please contact our customer service team for assistance."),
        ("What are the legal regulations for buying and using cannabis in New Brunswick?", "In New Brunswick, you must be 19 years or older to purchase and use cannabis. It is illegal to drive under the influence of cannabis, and you can face fines and penalties for doing so. You can possess up to 30 grams of dried cannabis or the equivalent in public, and up to 150 grams in your home. It is also illegal to buy or sell cannabis from anyone other than an authorized retailer. For more information, please visit the Government of New Brunswick's website.")]

# Convert the data into a pandas dataframe
df = pd.DataFrame(data, columns=["Question", "Answer"])

# Split the data into training, validation, and testing datasets
train_data, test_data = train_test_split(df, test_size=0.2, random_state=42)
train_data, val_data = train_test_split(train_data, test_size=0.2, random_state=42)

# Tokenize the input sequences and convert them to tensors
train_input_ids = tokenizer.batch_encode_plus(train_data.Question.tolist(), padding=True, truncation=True, max_length=512, return_tensors="pt")
val_input_ids = tokenizer.batch_encode_plus(val_data.Question.tolist(), padding=True, truncation=True, max_length=512, return_tensors="pt")
test_input_ids = tokenizer.batch_encode_plus(test_data.Question.tolist
