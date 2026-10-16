# Reading Schedule Planner
# Import tkinter modules
from tkinter import *
from tkinter import messagebox

# Create the main window
window = Tk()
window.title("Reading Schedule Planner")
window.geometry("500x300")
window.config(bg="light blue")

# Display the heading
title_label = Label(
    window,
    text="Reading Schedule Planner",
    font=("Arial", 18, "bold"),
    bg="light blue"
)
title_label.pack(pady=50)

# Display instructions
info_label = Label(
    window,
    text="Create a simple plan to complete your book.",
    bg="light blue"
)
info_label.pack(pady=10)


# Function to open the reading plan window
def open_plan():
    plan_window = Toplevel(window)
    plan_window.title("Create Reading Plan")
    plan_window.geometry("500x350+50+50")
    plan_window.config(bg="light grey")

    # Input labels and entry boxes
    total_label = Label(
        plan_window,
        text="Enter total number of pages:",
        bg="light grey"
    )
    total_label.place(x=80, y=40)

    total_entry = Entry(plan_window)
    total_entry.place(x=280, y=40)

    daily_label = Label(
        plan_window,
        text="Enter pages you can read each day:",
        bg="light grey"
    )
    daily_label.place(x=80, y=90)

    daily_entry = Entry(plan_window)
    daily_entry.place(x=280, y=90)

    # Heading for the results
    output_heading = Label(
        plan_window,
        text="Your Reading Plan",
        font=("Arial", 14, "bold"),
        bg="light grey"
    )
    output_heading.place(x=175, y=185)

    # Result fields
    complete_label = Label(
        plan_window,
        text="Complete reading days:",
        bg="light grey"
    )
    complete_label.place(x=80, y=235)

    complete_entry = Entry(plan_window)
    complete_entry.place(x=280, y=235)

    left_label = Label(
        plan_window,
        text="Pages remaining:",
        bg="light grey"
    )
    left_label.place(x=80, y=275)

    left_entry = Entry(plan_window)
    left_entry.place(x=280, y=275)

    # Calculate the reading schedule
    def make_plan():
        try:
            pages = int(total_entry.get())
            daily_pages = int(daily_entry.get())

            if pages <= 0 or daily_pages <= 0:
                messagebox.showerror(
                    "Invalid Input",
                    "Please enter numbers greater than zero."
                )
                return

            # Calculate full days and leftover pages
            days = pages // daily_pages
            leftover = pages % daily_pages

            # Remove old results
            complete_entry.delete(0, END)
            left_entry.delete(0, END)

            # Show the new results
            complete_entry.insert(0, str(days))
            left_entry.insert(0, str(leftover))

        except ValueError:
            messagebox.showerror(
                "Invalid Input",
                "Please enter valid whole numbers."
            )

    # Button to calculate the plan
    make_button = Button(
        plan_window,
        text="Create Plan",
        command=make_plan,
        bg="#1261A0",
        fg="white"
    )
    make_button.place(x=205, y=135)


# Button to open the second window
open_button = Button(
    window,
    text="Create My Reading Plan",
    command=open_plan,
    bg="#1261A0",
    fg="white"
)
open_button.pack(pady=15)

# Keep the application running
window.mainloop()
