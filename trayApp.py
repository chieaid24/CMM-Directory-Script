from pystray import Icon, Menu, MenuItem
from PIL import Image, ImageDraw
import tkinter as tk
from tkinter import messagebox
import threading
import sys
import script
import time
import os

#create threading event to control pausing
pause_event = threading.Event()
pause_event.set()

def update_tooltip(icon, text):
    icon.title = text

# Example functions for your menu
def pause(icon, item):
    print("Pausing main program..")
    pause_event.clear()
    update_tooltip(icon, "CMM Report Compiler, paused")

def unpause(icon, item):
    print("Unpausing main program..")
    pause_event.set()
    update_tooltip(icon, "CMM Report Compiler, running")

def on_quit(icon, item):
    icon.stop()
    os._exit(0)

def restart(icon, item):
    print("Restarting the program...")
    python = sys.executable  # Path to the Python interpreter
    script_path = f'"{sys.argv[0]}"'  # Quote the script path to handle spaces
    os.execl(python, python, script_path, *sys.argv[1:])


# Create an icon image (16x16)
def create_image():
    # Load the image 'logo.jpg' from the same folder as the script
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current script
    image_path = os.path.join(script_dir, "logo.jpg")  # Construct the full path to 'logo.jpg'
    return Image.open(image_path)  # Open and return the image



# Run the tray application
def run_tray():
    menu = Menu(
        # manually run, redefine folders, manual setup with part name and number of files, so when that # of files appears\
        # (it is being updated every 5 minutes) it compiles them
        MenuItem('Pause', pause),
        MenuItem('Unpause', unpause),
        MenuItem('Restart', restart),
        MenuItem('Quit', on_quit)
    )
    icon = Icon("MyApp", create_image(), "CMM Report Compiler, running", menu)
    icon.run()

# Optional: Run in a separate thread so it doesn’t block
if __name__ == "__main__":
    threading.Thread(target=run_tray, daemon=True).start()    # Your main script can continue running here
    print("Tray app running in background...")
    input_folder, output_folder, runs = script.initialize_program()
    while True:
        pause_event.wait()
        print("Running main program!")
        script.run_program(input_folder, output_folder, runs)
        print("Waiting for 5 minutes")
        time.sleep(300)