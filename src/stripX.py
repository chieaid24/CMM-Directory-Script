import tkinter as tk
from tkinter import filedialog
import os

def select_folder1(io):
    # Create a hidden root window
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Open the folder selection dialog
    folder_path = filedialog.askdirectory(title=f"Select the {io} Folder")

    # Return the selected folder path
    return folder_path

def deleteX(input_folder):
    # Loop through all files in the input folder
    for file_name in os.listdir(input_folder):
        # Check if the file is a .TXT file and ends with "-x"
        if file_name.endswith("-x.TXT"):
            # Construct the full file path
            file_path = os.path.join(input_folder, file_name)
            
            # Create the new file name by removing "-x"
            new_file_name = file_name.replace("-x", "")
            new_file_path = os.path.join(input_folder, new_file_name)
            
            # Rename the file
            os.rename(file_path, new_file_path)
            print(f"Renamed {file_path} to {new_file_path}")


def run_prog():
    input_folder = select_folder1("Input")
    print("Input folder", input_folder)
    deleteX(input_folder)

run_prog()