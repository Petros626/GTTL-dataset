import json
import os

def parse_label(line, id_counter, color):
    name = line.strip() # free label entry from space and line breaks
    type = "rectangle" # fixed type for the labels
    
    label = {
        "name": name,
        "id": id_counter,
        "color": color,
        "type": type,
        "attributes": []
    }
    return label
    
example_label = {
    "name": "car",
    "id": 1,
    "color": "#33ddff",
    "type": "rectangle",
    "attributes": []
}

script_directory = os.path.dirname(os.path.abspath(__file__))

print("This program creates labels in the desired raw format to use with the annotation tool CVAT.")
print("Example label:")
print(json.dumps(example_label, indent=2))
print("\n")

input_filename = input("Enter the file name of the input file (e.g. labels.txt): ")
input_file = os.path.join(script_directory, input_filename)

if not os.path.isfile(input_file):
    print(f"The specified file '{input_file}' was not found.")
else:
    color = input("Enter the desired color for the labels (e.g. #33ddff): ")
    start_id = int(input("Enter the desired start id for the labels (e.g. 1): "))
    output_filename = input("Enter the file name of the output file (e.g. output.txt): ")
    output_file = os.path.join(script_directory, output_filename)

    labels = [] # list
    id_counter = start_id

    # read process
    with open(input_file, "r") as file: # open input file
        for line in file: # loop through all lines
            label = parse_label(line, id_counter, color)
            labels.append(label) # create one full label
            id_counter += 1
            
    # check process
    with open(input_file, "r") as file:
        lines = file.readlines()
        if not lines[-1].strip():
            print("Warning: The last line in the input file is empty. Please delete it to avoid assigning empty IDs.")
            
    # write process
    with open(output_file, "w") as file:
        if output_filename.lower().endswith(".txt"):
            json.dump(labels, file, indent=2) # convert dict. to json
            file.write("\n")
    print(f"\nThe labels were stored in {output_filename}.")
