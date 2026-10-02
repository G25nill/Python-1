from tkinter import *

# Main window
window = Tk()
window.title("ATM PIN Setup Interface")
window.geometry("400x500")

# Account information section
account_frame = Frame(
    window,
    height=150,
    width=360,
    bg="#d0efff"
)

# Account name label
account_name_label = Label(
    account_frame,
    text="Account Name",
    bg="#3895D3",
    fg="white",
    width=14
)

# PIN label
create_pin_label = Label(
    account_frame,
    text="Create PIN",
    bg="#3895D3",
    fg="white",
    width=14
)

# Input fields
account_input = Entry(account_frame)
pin_input = Entry(account_frame, show="*")


# Check the entered information
def set_pin():
    username = account_input.get()
    user_pin = pin_input.get()

    result_box.delete(1.0, END)

    if username == "" or user_pin == "":
        result_box.insert(
            END,
            "Please enter the account name and PIN."
        )
    else:
        result_box.insert(
            END,
            "Hello " + username +
            "\nYour ATM PIN has been set successfully."
        )


# Keypad
button_frame = Frame(
    window,
    relief=SUNKEN,
    borderwidth=2
)

keys = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    ["Clear", 0, "Enter"]
]

# Create keypad
for row in range(4):
    button_frame.rowconfigure(row, weight=1, minsize=40)

    for column in range(3):
        button_frame.columnconfigure(
            column,
            weight=1,
            minsize=70
        )

        key_frame = Frame(
            button_frame,
            relief=RAISED,
            borderwidth=1
        )

        key_frame.grid(
            row=row,
            column=column,
            sticky="nsew"
        )

        key_text = Label(
            key_frame,
            text=keys[row][column],
            bg="#d0efff"
        )

        key_text.pack(
            padx=8,
            pady=8
        )


# Set PIN button
set_button = Button(
    window,
    text="Set ATM PIN",
    command=set_pin,
    bg="red",
    fg="white"
)

# Result display
result_box = Text(
    window,
    height=5,
    width=42,
    bg="#BEBEBE",
    fg="black"
)

# Place everything
account_frame.place(x=20, y=10)

account_name_label.place(x=15, y=25)
account_input.place(x=155, y=25)

create_pin_label.place(x=15, y=85)
pin_input.place(x=155, y=85)

button_frame.place(x=85, y=180)

set_button.place(x=145, y=370)

result_box.place(x=25, y=410)

# Run the program
window.mainloop()

