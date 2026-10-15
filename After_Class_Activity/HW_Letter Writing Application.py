
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Create the main window
root = Tk()
root.title("Letter Writing Application")
root.geometry("600x500")

root.rowconfigure(0, weight=1)
root.columnconfigure(1, weight=1)


# Function to open a letter
def open_letter():
    file_path = askopenfilename(
        filetypes=[
            ("Text Files", "*.txt"),
            ("All Files", "*.*")
        ]
    )

    if not file_path:
        return

    text_area.delete("1.0", END)

    with open(file_path, "r") as file:
        content = file.read()
        text_area.insert(END, content)

    root.title(file_path)


# Function to save a letter with a new name
def save_letter():
    file_path = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[
            ("Text Files", "*.txt"),
            ("All Files", "*.*")
        ]
    )

    if not file_path:
        return

    with open(file_path, "w") as file:
        content = text_area.get("1.0", END)
        file.write(content)

    root.title(file_path)


# Create the text editor
text_area = Text(root)

# Create a frame for the buttons
button_frame = Frame(root, relief=RAISED, bd=2)

# Add the buttons
open_button = Button(
    button_frame,
    text="Open Letter",
    command=open_letter
)

save_button = Button(
    button_frame,
    text="Save Letter As...",
    command=save_letter
)


# Arrange the buttons inside the frame
open_button.grid(row=0, column=0, sticky="ew")
save_button.grid(row=1, column=0, sticky="ew")

# Place the frame and editor in the window
button_frame.grid(row=0, column=0, sticky="ns")
text_area.grid(row=0, column=1, sticky="nsew")

# Run the application
root.mainloop()
