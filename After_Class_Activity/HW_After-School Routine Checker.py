
# After-School Routine Checker

# Import tkinter modules
from tkinter import *
from tkinter import messagebox

# Create the application window
root = Tk()
root.title("After-School Routine Checker")
root.geometry("400x320")

# Display the title
title_label = Label(
    root,
    text="My After-School Routine",
    font=("Arial", 16, "bold")
)
title_label.pack(pady=10)

# Ask the user to enter a task
task_label = Label(
    root,
    text="Enter your next after-school task:"
)
task_label.pack()

# Input box for the task
task_input = Entry(root, width=35)
task_input.pack(pady=8)

# Show the most recently pressed key
key_display = Label(root, text="Last key pressed: None")
key_display.pack(pady=5)

# Function to handle keyboard events
def show_key(event):
    key_display.config(
        text="Last key pressed: " + event.char
    )

# Detect key presses inside the input box
task_input.bind("<Key>", show_key)

# Create the routine display area
routine_label = Label(
    root,
    text="Click here to check your routine",
    bg="#d0efff",
    width=32,
    height=3
)
routine_label.pack(pady=10)

# Function to handle mouse clicks
def select_routine(event):
    routine_label.config(text="Routine area selected!")

# Detect left mouse clicks
routine_label.bind("<Button-1>", select_routine)

# Check whether the user entered a task
def display_task():
    next_task = task_input.get()

    if next_task == "":
        messagebox.showwarning(
            "Missing Task",
            "Please enter an after-school task."
        )
    else:
        routine_label.config(
            text="Next task: " + next_task
        )

# Add a button to check the task
check_btn = Button(
    root,
    text="Check My Routine",
    command=display_task
)
check_btn.pack(pady=10)

# Run the application
root.mainloop()
