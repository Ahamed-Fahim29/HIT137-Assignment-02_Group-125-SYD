# https://github.com/Ahamed-Fahim29/HIT137-Assignment-02_Group-125-SYD
# question_1_task_1
import pandas as pd
import os
import zipfile
import shutil

# Check if the current working directory is HIT137-Assignment-02_Group-125-SYD
current_directory = os.getcwd()
expected_directory = "HIT137-Assignment-02_Group-125-SYD"

if os.path.basename(current_directory) != expected_directory:
    print(f"Error: Please make sure you are in the '{expected_directory}' directory.")
else:
    # Define the relative path to the zipped folder within the assignment folder
    zipped_folder_relative_path = "Assignment 2.zip"
    zipped_folder_path = os.path.join(current_directory, zipped_folder_relative_path)

    print("Base Path:", current_directory)
    print("Zipped Folder Path:", zipped_folder_path)  # Print the path for debugging purposes

    # Print the contents of the directory for additional debugging
    print("Contents of the Directory:")
    print(os.listdir(current_directory))

    # Step 2: Check if the extracted folder already exists, delete it if it does
    extracted_folder_path = os.path.join(current_directory, "Assignment 2_Extracted")
    if os.path.exists(extracted_folder_path):
        print("Deleting existing extracted folder...")
        shutil.rmtree(extracted_folder_path)

    # Step 3: Create the extracted folder
    os.makedirs(extracted_folder_path, exist_ok=True)

    # Unzipping the folder
    try:
        with zipfile.ZipFile(zipped_folder_path, 'r') as zip_ref:
            zip_ref.extractall(extracted_folder_path)
        print("Zip file extracted successfully.")
    except FileNotFoundError:
        print(f"Error: File not found - {zipped_folder_path}")

    # Step 4: Loop through each CSV file in the extracted folder
    all_texts = []

    for file_name in os.listdir(extracted_folder_path):
        if file_name.endswith('.csv'):
            # Step 5: Read the CSV file using pandas
            file_path = os.path.join(extracted_folder_path, file_name)
            df = pd.read_csv(file_path)

            # Step 6: Identify the cell with the largest text in each row
            texts_per_row = []
            for _, row in df.iterrows():
                largest_text_in_row = max(row.astype(str), key=len)
                texts_per_row.append(largest_text_in_row)

            # Step 7: Extend the list with the largest texts in each row
            all_texts.extend(texts_per_row)

    # Step 8: Write the largest texts to the output text file
    output_txt_file = os.path.join(current_directory, "output_text_file.txt")
    with open(output_txt_file, 'w', encoding='utf-8') as txt_file:
        txt_file.write('\n'.join(all_texts))

    # Success message
    print(f"All large texts extracted from the CSVs are combined into the text file:")
    print(f"Text File Name: {os.path.basename(output_txt_file)}")
    print(f"Text File Location: {output_txt_file}")
