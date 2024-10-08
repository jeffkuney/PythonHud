import tkinter as tk
from tkinter import messagebox
import json

def save_input_to_json():
    user_input = input_entry.get()

    if not user_input.strip():
        messagebox.showwarning("User Error", "Truly apply thyself")
        return

    # Create a dictionary with the input
    data = {"user_input": user_input}

    # Save to a JSON file
    with open("user_input.json", "w") as json_file:
        json.dump(data, json_file, indent=4)

    messagebox.showinfo("Joy", "Thine words have been immortalized in 'user_input.json'.")


#========================================================================#

# Create the main window
root = tk.Tk()
root.title("Giveth thine info")
root.geometry("400x200")

# Create a label and an entry for user input
label = tk.Label(root, text="What is thy name?")
label.pack(pady=10)

input_entry = tk.Entry(root, width=40)
input_entry.pack(pady=5)

# Create a button to save the input
save_button = tk.Button(root, text="Enter", command=save_input_to_json)
save_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()