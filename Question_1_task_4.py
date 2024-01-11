import spacy
import time
from transformers import BertTokenizer, BertForTokenClassification
import torch
import pandas as pd

def extract_entities_spacy(text, nlp_model, max_tokens=2000):
    start_time = time.time()
    # Process text with spaCy NER model
    doc = nlp_model(text[:max_tokens])

    entities = []
    for ent in doc.ents:
        entities.append((ent.text, ent.label_))

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution Time (spaCy): {execution_time:.2f} seconds")
    
    return entities

def extract_entities_biobert(text, tokenizer, model, max_tokens=2000):
    start_time = time.time()
    
    # Tokenize input text
    tokens = tokenizer.tokenize(tokenizer.decode(tokenizer.encode(text[:max_tokens])))
    
    # Split tokens into chunks of size 512 (maximum supported by BioBERT)
    chunk_size = 512
    token_chunks = [tokens[i:i + chunk_size] for i in range(0, len(tokens), chunk_size)]

    entities = []
    for chunk in token_chunks:
        # Run tokenized chunk through BioBERT model
        inputs = tokenizer.encode_plus(" ".join(chunk), return_tensors="pt", truncation=True)
        outputs = model(inputs["input_ids"]).logits
        predictions = torch.argmax(outputs, dim=2)

        current_entity = []
        for token, prediction in zip(chunk, predictions[0].numpy()):
            if prediction != 0:  # Ignore tokens labeled as 'O'
                current_entity.append(token)
            elif current_entity:
                entities.append((" ".join(current_entity), str(prediction)))
                current_entity = []

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution Time (BioBERT): {execution_time:.2f} seconds")
    
    return entities

def analyze_entities(entities_sci_sm, entities_biobert):
    common_entities = set(entities_sci_sm) & set(entities_biobert)
    entities_difference_sci_sm = set(entities_sci_sm) - common_entities
    entities_difference_biobert = set(entities_biobert) - common_entities

    analysis_results = {
        'Total Entities Detected by en_core_sci_sm': len(entities_sci_sm),
        'Total Entities Detected by BioBERT': len(entities_biobert),
        'Entities Detected by Both Models': len(common_entities),
        'Entities Detected only by en_core_sci_sm': len(entities_difference_sci_sm),
        'Entities Detected only by BioBERT': len(entities_difference_biobert),
        'Common Entities': common_entities
    }

    return analysis_results

if __name__ == "__main__":
    # Load the spaCy models
    nlp_sci_sm = spacy.load("en_core_sci_sm")

    # Load BioBERT tokenizer and model
    tokenizer = BertTokenizer.from_pretrained("monologg/biobert_v1.1_pubmed")
    model = BertForTokenClassification.from_pretrained("monologg/biobert_v1.1_pubmed")

    # Load the text from the output file
    output_txt_file_path = "output_text_file.txt"

    try:
        with open(output_txt_file_path, 'r', encoding='utf-8') as txt_file:
            text_content = txt_file.read()
    except FileNotFoundError:
        print(f"Error: File not found - {output_txt_file_path}")
        exit()

    # Extract entities using spaCy
    entities_sci_sm = extract_entities_spacy(text_content, nlp_sci_sm)

    # Extract entities using BioBERT
    entities_biobert = extract_entities_biobert(text_content, tokenizer, model)

    # Save the results to files
    output_spacy_file = "output_entities_spacy.txt"
    output_biobert_file = "output_entities_biobert.txt"

    with open(output_spacy_file, 'w', encoding='utf-8') as spacy_file:
        spacy_file.write('\n'.join(map(str, entities_sci_sm)))

    with open(output_biobert_file, 'w', encoding='utf-8') as biobert_file:
        biobert_file.write('\n'.join(map(str, entities_biobert)))

    # Perform analysis
    analysis_results = analyze_entities(entities_sci_sm, entities_biobert)

    # Print the analysis results
    print("\nAnalysis Results:")
    for key, value in analysis_results.items():
        print(f"{key}: {value}")

    # Save the analysis results to a CSV file
    output_analysis_file = "entity_analysis_results.csv"
    pd.DataFrame(analysis_results.items(), columns=['Criteria', 'Values']).to_csv(output_analysis_file, index=False)

    print(f"\nAnalysis results saved to: {output_analysis_file}")
