import tkinter as tk
from tkinter import messagebox

def start_countdown():
    """Start the countdown timer."""
    try:
        time_left = int(entry_timer.get())
        countdown(time_left)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

def countdown(time_left):
    """Recursive countdown function."""
    if time_left > 0:
        label_timer.config(text=f"Time Left: {time_left} seconds")
        root.after(1000, countdown, time_left - 1)
    else:
        label_timer.config(text="Time's up!")
        messagebox.showinfo("Countdown Complete", "The countdown has finished!")

def submit_input():
    """Handle user input submission."""
    user_input = entry_input.get()
    if user_input:
        messagebox.showinfo("Input Received", f"You entered: {user_input}")
        entry_input.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Countdown Timer with Input")

# Countdown Timer Section
frame_timer = tk.Frame(root)
frame_timer.pack(pady=10)

label_timer = tk.Label(frame_timer, text="Enter countdown time (seconds):", font=("Arial", 14))
label_timer.pack()

entry_timer = tk.Entry(frame_timer, width=10, font=("Arial", 14))
entry_timer.pack()

button_start = tk.Button(frame_timer, text="Start Countdown", command=start_countdown, font=("Arial", 12))
button_start.pack(pady=5)

# User Input Section
frame_input = tk.Frame(root)
frame_input.pack(pady=20)

label_input = tk.Label(frame_input, text="Enter your input below:", font=("Arial", 14))
label_input.pack()

entry_input = tk.Entry(frame_input, width=30, font=("Arial", 14))
entry_input.pack()

button_submit = tk.Button(frame_input, text="Submit Input", command=submit_input, font=("Arial", 12))
button_submit.pack(pady=5)

# Run the application
root.mainloop()
