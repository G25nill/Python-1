# Account PIN Safety Checker

# Create the Account class
class Account:

    def __init__(self, name, starting_pin):
        self.owner = name
        self.__pin = starting_pin

    # Display information about the private PIN
    def show_pin_status(self):
        print("Account Owner:", self.owner)
        print("PIN is safely stored inside the class.")

    # Change the PIN only if it is valid
    def set_pin(self, pin_value):
        if len(pin_value) == 4 and pin_value.isdigit():
            self.__pin = pin_value
            print("PIN updated successfully.")
        else:
            print("Invalid PIN. PIN must be exactly 4 digits.")

    # Compare an entered PIN with the private PIN
    def check_pin(self, entered):
        if entered == self.__pin:
            print("Access granted.")
        else:
            print("Access denied.")

    # Controls what is shown when the object is printed
    def __str__(self):
        return "Account holder: " + self.owner


# Make an Account object
account = Account("Riya", "1234")

# Print the object
print(account)

# Display the PIN status
account.show_pin_status()

# Attempt to change the private PIN directly
account.__pin = "9999"
print("Tried changing PIN directly from outside.")

# Test whether the original PIN was changed
account.check_pin("9999")
account.check_pin("1234")

# Change the PIN using the setter method
account.set_pin("9999")

# Test the newly updated PIN
account.check_pin("9999")

