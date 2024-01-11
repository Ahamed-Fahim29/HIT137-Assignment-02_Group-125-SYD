# https://github.com/Ahamed-Fahim29/HIT137-Assignment-02_Group-125-SYD
# question_1_task_2
import spacy
from transformers import AutoTokenizer, AutoModelForTokenClassification

def check_libraries():
    try:
        # Check SpaCy installation
        print("Checking SpaCy installation:")
        nlp_sci_sm = spacy.load("en_core_sci_sm")
        nlp_bc5cdr_md = spacy.load("en_ner_bc5cdr_md")
        print("SpaCy installation successful.\n")

        # Check Hugging Face Transformers installation
        print("Checking Hugging Face Transformers installation:")
        tokenizer = AutoTokenizer.from_pretrained("dmis-lab/biobert-v1.1")
        model = AutoModelForTokenClassification.from_pretrained("dmis-lab/biobert-v1.1")
        print("Hugging Face Transformers installation successful.\n")

        print("All libraries and models are installed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    check_libraries()
