import tkinter as tk
import time
from datetime import datetime
import json
import os

# with open('timers,json') as f:
#     data = json.load(f)


    

# with open('new_timers.json', 'w') as f:
#     json.dump(data, f, indent=2)





# ============================================================================================ #

# # Function to save the timer data in JSON format
# def save_to_json(duration):
#     timer_data = {
#         "start_time": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
#         "duration": duration,
#         "end_time": (datetime.now() + timedelta(seconds=duration)).strftime('%Y-%m-%d %H:%M:%S')
#     }

#     # If the file exists, load the existing data, otherwise create a new list
#     if os.path.exists("timers.json"):
#         with open("timers.json", "r") as file:
#             data = json.load(file)
#     else:
#         data = []

#     # Add the new timer data to the list
#     data.append(timer_data)

#     # Save the updated data back to the JSON file
#     with open("timers.json", "w") as file:
#         json.dump(data, file, indent=4)


# ============================================================================================ #

# Function to start the timer
def start_timer():
    try:
        duration = int(entry.get())
        # # Save timer data to JSON
        # save_to_json(duration)
        for remaining in range(duration, 0, -1):
            label.config(text=f"Time remaining: {remaining} seconds")
            window.update()
            time.sleep(1)
        label.config(text="Timer finished!")
    except ValueError:
        label.config(text="Please enter a valid number.")

# Create a window
window = tk.Tk()
window.title("Simple Timer with Save Feature")

# Create a label
label = tk.Label(window, text="Enter the time in seconds:", font=("Helvetica", 14))
label.pack(pady=20)

# Create an entry field for duration
entry = tk.Entry(window, font=("Helvetica", 14))
entry.pack(pady=10)

# Create a button to start the timer
start_button = tk.Button(window, text="Start Timer", command=start_timer, font=("Helvetica", 14))
start_button.pack(pady=20)

# Start the tkinter loop
window.mainloop()
