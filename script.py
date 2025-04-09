import tkinter as tk
from tkinter import filedialog
import os

def select_folder(io):
    # Create a hidden root window
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Open the folder selection dialog
    folder_path = filedialog.askdirectory(title=f"Select the {io} Folder")

    # Return the selected folder path
    return folder_path

def isolate_part_no(input_str):
    # Find the substring starting with "Part"
    part_index = input_str.find("Part")
    if part_index != -1:
        return input_str[part_index:]
    return None  # Return None if "Part" is not found

def copy_files(file_list, output_folder):
    s1_file = None
    for file_path in file_list:
        if "[S1]" in os.path.basename(file_path):
            s1_file = file_path
            break
    if not s1_file:
        raise FileNotFoundError("No file containing '[S1]' found. Aborted program")
    
    # create new file and copy s1 to that
    s1_file_name = os.path.basename(s1_file)
    combined_file_name = os.path.splitext(s1_file_name)[0] + " Combined" + os.path.splitext(s1_file_name)[1]
    new_file_path = os.path.join(output_folder, combined_file_name)

    with open(s1_file, "r") as s1:
        s1_contents = s1.readlines()
    with open(new_file_path, "w") as new_file:
        new_file.writelines(s1_contents)

    for file_path in file_list:
        if file_path != s1_file:
            with open(file_path, "r") as file:
                all_lines = file.readlines()
            
            # copy all of the lines after line 5
            lines_to_copy = all_lines[5:]

            with open(new_file_path, "a") as new_file:
                new_file.writelines(lines_to_copy)
                print(f"Copied lines for {new_file}")

def rename_files(file_list):
    for file_path in file_list:
        # Get the directory, file name, and extension
        directory = os.path.dirname(file_path)
        file_name, file_extension = os.path.splitext(os.path.basename(file_path))
        
        # Create the new file name with '-x' appended
        new_file_name = f"{file_name}-x{file_extension}"
        new_file_path = os.path.join(directory, new_file_name)
        
        # Rename the file
        os.rename(file_path, new_file_path)
        print(f"Renamed {file_path} to {new_file_path}")

    

# loop through all the files, disregard the ones with the - x (means it has already been scanned)
# isolate the part#000 part and match however many match (bc could be 2 or 3)
# copy the secondary parts into S1, save as new file, into the output file directory

def initialize_program():
    # Create a hidden root window
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Select input and output folders
    input_folder = select_folder("Input")
    print("Input folder", input_folder)
    output_folder = select_folder("Output")
    print("Output folder", output_folder)

    # Prompt the user to enter the number of runs
    runs = tk.simpledialog.askinteger(
        "Input Required",
        "Enter the number of Runs each part requires:",
        minvalue=1
    )
    print("Number of Runs:", runs)
    return input_folder, output_folder, runs



def run_program(input_folder, output_folder, runs):
    totalMatchFound = True
    completed_parts = []
    while totalMatchFound:
        #list containing the to be processed files
        file_list = []
        #loop through all of the text documents
        for index, file_name in enumerate(os.listdir(input_folder)):
            if (file_name.endswith(".TXT") or file_name.endswith(".txt")) and isolate_part_no(file_name) not in completed_parts:
                file_path = os.path.join(input_folder, file_name)
                file_list = [file_path]
                print(f"Processing file {index + 1}: {file_path}")

                #nested loop starting at index + 1
                for sub_index, sub_file_name in enumerate(os.listdir(input_folder)[index + 1:], start=index + 1):
                    if sub_file_name.endswith(".TXT") or sub_file_name.endswith('.txt'):
                        sub_file_path = os.path.join(input_folder, sub_file_name)
                        print(f"Comparing with file {sub_index + 1}: {sub_file_path}")

                        #check if matching parts
                        if isolate_part_no(file_name) == isolate_part_no(sub_file_name):
                            print("Found matching file!")
                            file_list.append(sub_file_path)
                #once the inner loop finishes, check if a match exists, else continue looping
                if len(file_list) == runs:
                    completed_parts.append(isolate_part_no(file_name))
                    break
        # for each outer loop ran, add that part to the completed parts
            completed_parts.append(isolate_part_no(file_name))
            print("Completed parts:", completed_parts)

        # after the outer loop finishes, if matching, then excecute the program
        if len(file_list) == runs:
            copy_files(file_list, output_folder)
            file_list = []
        else:
            # if no match at all is found, then exit the program
            totalMatchFound = False
