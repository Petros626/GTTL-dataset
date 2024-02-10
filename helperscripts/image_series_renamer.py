import os
import shutil

def rename_images(number, directory):
    if not os.path.exists(directory):
        print(f"The directory {directory} does not exist.")
        return

    # search for images in directory and create a list with the following requirements:
    # 1. check if path is regular file or not
    # 2. filename is lowercase and starts with 'images_' and ends with '.jpg' | '.png' | 'jpeg'
    image_files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f.lower().startswith("images_") and f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    for i, file_name in enumerate(image_files, start=number):
        new_name = f"images_{i}.jpg"  # Create new filename
        shutil.move(os.path.join(directory, file_name), os.path.join(directory, new_name))  # rename all the files

    print("Images were succesfully renamed.")

# Get ongoing number and directory from user
user_input = input("Please enter an ongoing number: ")
try:
    start_number = int(user_input)
    directory_input = input("Please enter the directory with the images: ")
    rename_images(start_number, directory_input)
except ValueError:
    print("Unvalid input. Please enter a number.")
