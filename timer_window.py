import tkinter as tk
import time
from datetime import datetime

# Function to write the timer data to a file
def save_to_file(duration):
    with open("timer_log.txt", "a") as file:
        start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        file.write(f"Timer started at {start_time} for {duration} seconds.\n")
        file.write(f"Timer ended at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write("----\n")

def start_timer():
    try:
        duration = int(entry.get())
        # Save the start time to file
        save_to_file(duration)
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
