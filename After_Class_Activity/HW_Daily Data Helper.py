# Daily Data Helper

# PART 1: DailyMessage class
class DailyMessage:

    def __init__(self):
        self.message = ""

    def get_message(self):
        self.message = input("Enter today's message: ")

    def print_message(self):
        uppercase_message = self.message.upper()
        print("Message in uppercase:", uppercase_message)


# Create DailyMessage object
daily_text = DailyMessage()
daily_text.get_message()
daily_text.print_message()


# PART 2: HelperSession class
class HelperSession:

    def __init__(self):
        print("Daily Data Helper session created")

    def __del__(self):
        print("Daily Data Helper session ended")


# Function to create a HelperSession object
def create_session():
    print("Making helper session...")
    new_session = HelperSession()
    print("Session is ready...")
    return new_session


print()
print("Calling create_session() function...")

session_obj = create_session()

print("Program is still running...")


# PART 3: PairFinder class
class PairFinder:

    def find_pair(self, numbers, target):
        previous_numbers = {}

        # enumerate() provides the index and value
        for position, value in enumerate(numbers):

            required = target - value

            if required in previous_numbers:
                return (previous_numbers[required], position)

            previous_numbers[value] = position

        return None


# Numbers to search through
numbers = (10, 20, 30, 40, 50, 60, 70)

target_value = int(input("Enter target sum to search: "))

finder = PairFinder()
result = finder.find_pair(numbers, target_value)


if result:
    print("index1=%d, index2=%d" % result)
else:
    print("No matching pair found.")


# Remove the session object
del session_obj

print("Program End")

