import json
import tkinter as tk
from tkinter import messagebox
import os

#======================================================================== Functions #

#====================================== Save Inputs #
def save_input_to_json():
    name = name_entry.get().strip()
    age = age_entry.get().strip()
    favorite_color = color_entry.get().strip()


    # Validation
    if not name or not age or not favorite_color:
        messagebox.showwarning("User Error", "Truly apply thyself.")
        return

    if not age.isdigit():
        messagebox.showwarning("User Error", "Falsehood Detected. Report to solitary confinement or try again.")
        return

    # Create or load the JSON file
    if os.path.exists("user_data.json"):
        with open("user_data.json", "r") as json_file:
            data = json.load(json_file)
    else:
        data = {"users": []}

    # Append new user to list
    user_data = {
        "name": name,
        "age": int(age),
        "favorite_color": favorite_color
    }
    data["users"].append(user_data)

    # Save the updated data back to the JSON file
    with open("user_data.json", "w") as json_file:
        json.dump(data, json_file, indent=4)

    # Success
    messagebox.showinfo("Joy", f"{name}'s data has been immortalized in 'user_data.json'.")

    # Clear inputs
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    color_entry.delete(0, tk.END)

#====================================== Load Inputs #
def update_previous_entries():
    if os.path.exists("user_data.json"):
        with open("user_data.json", "r") as json_file:
            data = json.load(json_file)
        
        # Clear the listbox
        listbox.delete(0, tk.END)

        # Add each user entry to the listbox
        for user in data["users"]:
            display_text = f"{user['name']}, {user['age']} years old, likes {user['favorite_color']}"
            listbox.insert(tk.END, display_text)

#======================================================================== Window/Frame #

# Create the main window
root = tk.Tk()
root.title("Giveth thine info")
root.geometry("600x300")

# Create a frame for the form inputs (left side)
left_frame = tk.Frame(root)
left_frame.pack(side=tk.LEFT, padx=10, pady=10)

# Create a frame for displaying previous entries (right side)
right_frame = tk.Frame(root)
right_frame.pack(side=tk.RIGHT, padx=10, pady=10)

# Create a listbox to display previous JSON entries
listbox = tk.Listbox(right_frame, width=50, height=10)
listbox.pack(pady=5)




#======================================================================== Labels #
# Create labels and entries for user input in the left frame
name_label = tk.Label(left_frame, text="Enter name:")
name_label.pack(pady=5)
name_entry = tk.Entry(left_frame, width=40)
name_entry.pack(pady=5)

age_label = tk.Label(left_frame, text="Enter age:")
age_label.pack(pady=5)
age_entry = tk.Entry(left_frame, width=40)
age_entry.pack(pady=5)

color_label = tk.Label(left_frame, text="Enter favorite color:")
color_label.pack(pady=5)
color_entry = tk.Entry(left_frame, width=40)
color_entry.pack(pady=5)

# Label for the list of previous entries
previous_entries_label = tk.Label(right_frame, text="Previous Entries:")
previous_entries_label.pack(pady=5)

#======================================================================== Buttons #
save_button = tk.Button(left_frame, text="Acceptance", command=save_input_to_json)
save_button.pack(pady=20)

#======================================================================== Run #
# Initially populate the listbox with previous entries
update_previous_entries()

root.mainloop()