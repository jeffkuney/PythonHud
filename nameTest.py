import json
import tkinter as tk
from tkinter import messagebox
import os


def save_input_to_json():
    name = name_entry.get().strip()
    age = age_entry.get().strip()
    favorite_color = color_entry.get().strip()


    #Validation
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


#========================================================================#

# Create the main window
root = tk.Tk()
root.title("Giveth thine info")
root.geometry("400x300")


# Create labels and entries for user input
name_label = tk.Label(root, text="Enter name:")
name_label.pack(pady=5)
name_entry = tk.Entry(root, width=40)
name_entry.pack(pady=5)

age_label = tk.Label(root, text="Enter age:")
age_label.pack(pady=5)
age_entry = tk.Entry(root, width=40)
age_entry.pack(pady=5)

color_label = tk.Label(root, text="Enter favorite color:")
color_label.pack(pady=5)
color_entry = tk.Entry(root, width=40)
color_entry.pack(pady=5)

# Create a button to save the input
save_button = tk.Button(root, text="Acceptance", command=save_input_to_json)
save_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()