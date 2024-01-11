# https://github.com/Ahamed-Fahim29/HIT137-Assignment-02_Group-125-SYD
# question_1_task_3_2
import os
import pandas as pd
from collections import Counter
from transformers import AutoTokenizer
import time
from concurrent.futures import ThreadPoolExecutor
import itertools  # Add this import

def tokenize_chunk(chunk, tokenizer):
    encoding = tokenizer.batch_encode_plus([chunk], return_tensors="pt", max_length=512, truncation=True)
    tokens = tokenizer.convert_ids_to_tokens(encoding['input_ids'][0])
    return tokens

def count_unique_tokens(text_file_path, top_n=30, max_chunks=None):
    # Check if the current working directory is "HIT137-Assignment-02_Group-125-SYD"
    expected_directory = "HIT137-Assignment-02_Group-125-SYD"
    if os.path.basename(os.getcwd()) != expected_directory:
        print(f"Error: Please make sure you are in the '{expected_directory}' directory.")
        return

    # Load the AutoTokenizer
    tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

    # Measure execution time
    start_time = time.time()

    # Initialize a Counter for unique tokens
    unique_token_counts = Counter()

    # Read the text file in chunks to handle large files
    chunk_size = 50000  # Adjust the chunk size based on the available memory

    with open(text_file_path, 'r', encoding='utf-8') as file:
        chunks = iter(lambda: file.read(chunk_size), '')
        
        # Limit the number of chunks for testing purposes
        if max_chunks:
            chunks = itertools.islice(chunks, max_chunks)

        with ThreadPoolExecutor() as executor:
            for i, tokens in enumerate(executor.map(lambda chunk: tokenize_chunk(chunk, tokenizer), chunks)):
                unique_token_counts.update(set(tokens))
                # Log progress every 100 chunks
                if i % 100 == 0:
                    print(f"Processed {i} chunks")

    # Get the top N unique tokens
    top_n_tokens = unique_token_counts.most_common(top_n)

    # Convert to DataFrame for better handling
    top_n_df = pd.DataFrame(top_n_tokens, columns=['Token', 'Count'])

    # Save to CSV file
    csv_file_path = os.path.join(os.getcwd(), 'top_30_tokens.csv')
    top_n_df.to_csv(csv_file_path, index=False)

    # Print execution time and success messages
    print("Execution Time:", time.time() - start_time)
    print(f"Top 30 unique tokens and their counts saved to CSV file:")
    print(f"CSV File Name: {os.path.basename(csv_file_path)}")
    print(f"CSV File Location: {csv_file_path}")

# Example usage
output_txt_file_path = os.path.join(os.getcwd(), "output_text_file.txt")
count_unique_tokens(output_txt_file_path, max_chunks=10)  # Adjust max_chunks for testing
