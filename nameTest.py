import json
import tkinter as tk
from tkinter import messagebox
import os


def save_input_to_json():
    user_input = input_entry.get().strip()

    if not user_input.strip():
        messagebox.showwarning("User Error", "Truly apply thyself")
        return

    # Create or load the JSON file
    if os.path.exists("user_names.json"):
        with open("user_names.json", "r") as json_file:
            data = json.load(json_file)
    else:
        data = {"names": []}

    # Append the new name to the list
    data["names"].append(user_input)

    # Save the updated data back to the JSON file
    with open("user_names.json", "w") as json_file:
        json.dump(data, json_file, indent=4)

    messagebox.showinfo("Joy", f"'{user_input}' has been immortalized in 'user_names.json'.")
    input_entry.delete(0, tk.END)  # Clear the input field after saving


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