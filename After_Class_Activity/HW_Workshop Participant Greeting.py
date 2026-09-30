
from tkinter import *
from datetime import date

# Make the main window
window = Tk()
window.title("Workshop Participant Greeting")
window.geometry("400x300")

# Heading
title_label = Label(
    text="Workshop Welcome Desk",
    fg="white",
    bg="#072F5F",
    height=1,
    width=300
)
title_label.pack()

# Participant name
participant_label = Label(
    text="Participant Name",
    bg="#3895D3"
)
participant_label.pack(pady=10)

participant_entry = Entry()
participant_entry.pack()

# Text area
output = Text(
    height=4,
    width=40
)
output.pack()

# Function for checking in
def check_in():
    participant = participant_entry.get()

    output.delete(1.0, END)

    output.insert(END, "Hello " + participant + "!\n")
    output.insert(END, "Welcome to the workshop.\n")
    output.insert(END, "Date: " + str(date.today()))

# Check-in button
check_button = Button(
    text="Check In",
    command=check_in,
    height=1,
    bg="#1261A0",
    fg="white"
)
check_button.pack(pady=10)

# Start the program
window.mainloop()

