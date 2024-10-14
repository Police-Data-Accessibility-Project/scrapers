from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import pandas as pd
import argparse

# Load the tokenizer and model
model_name = "PDAP/fine-url-classifier"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
model.eval()

# Load the dataset from command line argument
parser = argparse.ArgumentParser(description="Load CSV file into a pandas DataFrame.")
parser.add_argument('--csv_file', type=str, required=True, help="Path to the CSV file")
args = parser.parse_args()
df = pd.read_csv(args.csv_file)

# Combine multiple columns (e.g., 'url', 'html_title', 'h1') into a single text field for each row
columns_to_combine = ['url_path', 'html_title', 'h1']  # Add other columns here as needed
df['combined_text'] = df[columns_to_combine].apply(lambda row: ' '.join(row.values.astype(str)), axis=1)

# Convert the combined text into a list
texts = df['combined_text'].tolist()

# Tokenize the inputs
inputs = tokenizer(texts, padding=True, truncation=True, return_tensors="pt")

# Perform inference
with torch.no_grad():
    outputs = model(**inputs)

# Get the predicted labels
predictions = torch.argmax(outputs.logits, dim=-1)

# Map predictions to labels
labels = model.config.id2label
predicted_labels = [labels[int(pred)] for pred in predictions]

# Add the predicted labels to the dataframe and save
df['predicted_label'] = predicted_labels
df.to_csv("labeled_muckrock_dataset.csv", index=False)
