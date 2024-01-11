# https://github.com/Ahamed-Fahim29/HIT137-Assignment-02_Group-125-SYD
# question_2_chapter_1
import os
import shutil
import zipfile
from PIL import Image
import time
import sys  # Import sys module for error handling

# Step 1: Check if the current working directory is HIT137-Assignment-02_Group-125-SYD
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

        # Step 4: Load the original image from the extracted folder
        original_image_path = os.path.join(extracted_folder_path, "chapter1.jpg")  # Correct file extension
        try:
            original_image = Image.open(original_image_path)
        except FileNotFoundError:
            print(f"Error: Original image file not found - {original_image_path}")
            sys.exit(1)

        # Step 5: Generate a number
        current_time = int(time.time())
        generated_number = (current_time % 100) + 50
        if generated_number % 2 == 0:
            generated_number += 10
        print("Generated Number:", generated_number)

        # Step 6: Create a new image with modified pixel values
        new_image = Image.new('RGB', original_image.size)
        for x in range(original_image.width):
            for y in range(original_image.height):
                r, g, b = original_image.getpixel((x, y))
                new_r = (r + generated_number) % 256
                new_g = (g + generated_number) % 256
                new_b = (b + generated_number) % 256
                new_image.putpixel((x, y), (new_r, new_g, new_b))

        # Step 7: Save the new image in the current directory
        new_image_path = os.path.join(current_directory, "chapter1out.png")
        new_image.save(new_image_path)
        print("New image saved successfully:", new_image_path)

        # Step 8: Calculate the sum of red pixel values in the new image
        red_pixel_sum = sum([new_image.getpixel((x, y))[0] for x in range(new_image.width) for y in range(new_image.height)])
        print("Sum of Red Pixel Values:", red_pixel_sum)

    except FileNotFoundError:
        print(f"Error: File not found - {zipped_folder_path}")
