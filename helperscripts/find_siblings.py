import os
import json

def find_duplicate_labels(input_dir):
    label_counts = {}  # here we save the number of occurrences of each label name
    duplicates = {}    # here we save the file names in which the duplicates were found

    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                with open(file_path, "r") as label_file:
                    try:
                        labels = json.load(label_file)
                        for label in labels:
                            label_name = label.get("name")
                            if label_name:
                                if label_name in label_counts:
                                    label_counts[label_name] += 1
                                    if label_name not in duplicates:
                                        duplicates[label_name] = []
                                    duplicates[label_name].append(file_path)
                                else:
                                    label_counts[label_name] = 1
                    except json.JSONDecodeError:
                        print(f"Error decoding JSON in file: {file_path}")

    return duplicates

input_directory = input("Enter the directory containing label text files: ")

if os.path.isdir(input_directory):
    duplicate_labels = find_duplicate_labels(input_directory)
    if duplicate_labels:
        print("Duplicate labels found in the following files:")
        for label_name, files_with_duplicates in duplicate_labels.items():
            print(f"Label: {label_name}")
            for file_path in files_with_duplicates:
                print(f"  - {file_path}")
    else:
        print("No duplicate labels found.")
else:
    print(f"The specified directory '{input_directory}' does not exist.")
