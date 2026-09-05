# Vehicle Type Builder

class Vehicle:
    
    def __init__(self, brand, max_speed):
        self.brand = brand
        self.max_speed = max_speed

    def show_details(self):
        print("Brand:", self.brand)
        print("Max Speed:", self.max_speed, "km/h")


class Car(Vehicle):

    def __init__(self, model, seats, brand, max_speed):
        super().__init__(brand, max_speed)
        self.model = model
        self.seats = seats

    def show_details(self):
        print("Model:", self.model)
        print("Seats:", self.seats)
        super().show_details()

    def fuel_type(self, fuel):
        print(self.model, "uses", fuel)


# Create an object from the Car class
car1 = Car("City Rider", 5, "Honda", 180)

# Display vehicle and car information
car1.show_details()

# Display the fuel type
car1.fuel_type("petrol")

# Test the inheritance relationship
result = issubclass(Car, Vehicle)
print("Is Car a subclass of Vehicle?", result)

