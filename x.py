import os
import tkinter as tk
from tkinter import filedialog

def filter_lines():
    # Open file dialog to select the input file
    input_file = filedialog.askopenfilename(title="Select Input File", filetypes=[("Text Files", "*.txt")])
    if not input_file:
        print("No input file selected.")
        return

    # Automatically name the output file based on the input file
    input_file_name, input_file_ext = os.path.splitext(input_file)
    

    # Prompt user for the search text
    search_text = input("Enter the text to search for: ")
    output_file = f"{search_text}_filtered{input_file_ext}"
    try:
        # Open the input file and read lines
        with open(input_file, 'r') as file:
            lines = file.readlines()

        # Filter lines that contain the search text
        matched_lines = [line for line in lines if search_text in line]

        # Save matched lines to the output file
        with open(output_file, 'w') as file:
            file.writelines(matched_lines)

        print(f"Filtered lines containing '{search_text}' have been saved to {output_file}.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Initialize Tkinter and hide the root window
    root = tk.Tk()
    root.withdraw()

    print("Select the input file...")
    filter_lines()
