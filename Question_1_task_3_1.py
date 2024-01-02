# https://github.com/Ahamed-Fahim29/HIT137-Assignment-02_Group-125-SYD
import os
import pandas as pd
from collections import Counter
import time

# Check if the current working directory is "CDU_Python_Assignment-2"
expected_directory = "CDU_Python_Assignment-2"
if os.path.basename(os.getcwd()) != expected_directory:
    print(f"Error: Please make sure you are in the '{expected_directory}' directory.")
else:
    # Load the text file
    output_txt_file = os.path.join(os.getcwd(), "output_text_file.txt")

    # Measure execution time
    start_time = time.time()

    # Read the text file in chunks to handle large files
    chunk_size = 100000  # Adjust the chunk size based on the available memory
    word_counts = Counter()

    with open(output_txt_file, 'r', encoding='utf-8') as file:
        for chunk in iter(lambda: file.read(chunk_size), ''):
            words = chunk.split()
            word_counts.update(words)

    # Get the top 30 most common words
    top_30_words = word_counts.most_common(30)

    # Convert to DataFrame for better handling
    top_30_df = pd.DataFrame(top_30_words, columns=['Word', 'Count'])

    # Save to CSV file
    csv_file_path = os.path.join(os.getcwd(), 'top_30_words.csv')
    top_30_df.to_csv(csv_file_path, index=False)

    # Print execution time
    print("Execution Time:", time.time() - start_time)
    print(f"Top 30 common words and their counts saved to CSV file:")
    print(f"CSV File Name: {os.path.basename(csv_file_path)}")
    print(f"CSV File Location: {csv_file_path}")

