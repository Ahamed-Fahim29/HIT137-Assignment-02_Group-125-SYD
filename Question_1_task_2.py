# https://github.com/Ahamed-Fahim29/HIT137-Assignment-02_Group-125-SYD
import os
import spacy
from transformers import AutoTokenizer, AutoModelForTokenClassification

# Check if the current working directory is "CDU_Python_Assignment-2"
expected_directory = "CDU_Python_Assignment-2"
if os.path.basename(os.getcwd()) != expected_directory:
    print(f"Error: Please make sure you are in the '{expected_directory}' directory.")
else:
    # Load spaCy model
    nlp = spacy.load('en_core_sci_sm')  # or 'en_ner_bc5cdr_md'

    # Load Hugging Face model (BioBert)
    tokenizer = AutoTokenizer.from_pretrained("dmis-lab/biobert-v1.1")
    model = AutoModelForTokenClassification.from_pretrained("dmis-lab/biobert-v1.1")

    # Check spaCy model with a sample text
    sample_text_spacy = "Sample text to test spaCy model installation."
    doc_spacy = nlp(sample_text_spacy)
    for ent in doc_spacy.ents:
        print(f"spaCy Entity: {ent.text}, Label: {ent.label_}")

    # Check Hugging Face model with a sample text
    sample_text_transformers = "Sample text to test Hugging Face model installation."
    inputs = tokenizer(sample_text_transformers, return_tensors="pt")
    outputs = model(**inputs)
    print("Hugging Face Model Outputs:", outputs)

    # Print success messages
    print("Library installations and models loaded successfully.")
