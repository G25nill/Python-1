
import tkinter as tk
from tkinter import ttk, messagebox


class StationeryApp:

    def __init__(self, window):
        self.window = window
        self.window.title("Stationery Order Management App")

        # Names of items and their prices in dollars
        self.items = {
            "NOTEBOOK": 3,
            "PENCIL PACK": 2,
            "PEN SET": 4,
            "ERASER": 1,
            "GEOMETRY BOX": 6,
            "COLOUR PENCILS": 5
        }

        self.rate = 82

        self.add_background()

        # Main frame for the application
        main_frame = ttk.Frame(self.window)
        main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        heading = ttk.Label(
            main_frame,
            text="Stationery Order Management",
            font=("Arial", 20, "bold")
        )
        heading.grid(row=0, columnspan=3, padx=10, pady=10)

        self.labels = {}
        self.entries = {}

        # Display the stationery items and quantity boxes
        for row, (name, price) in enumerate(self.items.items(), start=1):

            label = ttk.Label(
                main_frame,
                text=f"{name} (${price}):",
                font=("Arial", 12)
            )
            label.grid(row=row, column=0, padx=10, pady=5)

            self.labels[name] = label

            entry = ttk.Entry(main_frame, width=5)
            entry.grid(row=row, column=1, padx=10, pady=5)

            self.entries[name] = entry

        # Currency selection
        currency_row = len(self.items) + 1

        ttk.Label(
            main_frame,
            text="Currency:",
            font=("Arial", 12)
        ).grid(row=currency_row, column=0, padx=10, pady=5)

        self.currency = tk.StringVar(value="USD")

        currency_box = ttk.Combobox(
            main_frame,
            textvariable=self.currency,
            values=("USD", "INR"),
            state="readonly",
            width=18
        )
        currency_box.grid(row=currency_row, column=1, padx=10, pady=5)
        currency_box.current(0)

        self.currency.trace_add("write", self.change_prices)

        # Button to confirm the order
        ttk.Button(
            main_frame,
            text="Place Order",
            command=self.calculate_order
        ).grid(
            row=currency_row + 1,
            columnspan=3,
            padx=10,
            pady=10
        )

    # Add the background image
    def add_background(self):
        canvas = tk.Canvas(self.window, width=800, height=600)
        canvas.pack()

        image = tk.PhotoImage(file="background.png")

        # Resize the image to fit the window
        image = image.subsample(
            max(1, image.width() // 800),
            max(1, image.height() // 600)
        )

        canvas.create_image(0, 0, anchor=tk.NW, image=image)
        canvas.image = image

    # Change prices when the currency is changed
    def change_prices(self, *args):
        selected_currency = self.currency.get()

        if selected_currency == "INR":
            symbol = "₹"
            exchange = self.rate
        else:
            symbol = "$"
            exchange = 1

        for name, label in self.labels.items():
            new_price = self.items[name] * exchange
            label.config(text=f"{name} ({symbol}{new_price}):")

    # Calculate the order total
    def calculate_order(self):
        total = 0
        summary = "Stationery Order Summary:\n"

        if self.currency.get() == "INR":
            symbol = "₹"
            exchange = self.rate
        else:
            symbol = "$"
            exchange = 1

        for name, entry in self.entries.items():
            amount = entry.get()

            if amount.isdigit():
                amount = int(amount)
                price = self.items[name] * exchange
                cost = amount * price
                total += cost

                if amount > 0:
                    summary += (
                        f"{name}: {amount} x {symbol}{price} "
                        f"= {symbol}{cost}\n"
                    )

        if total > 0:
            summary += f"\nTotal Cost: {symbol}{total}"

            messagebox.showinfo("Order Placed", summary)
        else:
            messagebox.showerror(
                "Error",
                "Please order at least one stationery item."
            )


# Run the program
if __name__ == "__main__":
    window = tk.Tk()
    window.geometry("800x600")

    app = StationeryApp(window)

    window.mainloop()
