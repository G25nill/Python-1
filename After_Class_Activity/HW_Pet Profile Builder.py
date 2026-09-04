# Pet Profile Builder

# Step 1: Make a basic Pet class
class Pet:
    print("The Pet class has been created!")

# Step 2: Make an object using the Pet class
pet_object = Pet()


# Step 3: Create the PetProfile class
class PetProfile:

    # Class attribute shared by every pet
    category = "pet"

    # Set the information for each individual pet
    def __init__(self, name, animal_type, age, favourite_food):
        self.name = name
        self.animal_type = animal_type
        self.age = age
        self.favourite_food = favourite_food


# Step 4: Create two PetProfile objects
pet1 = PetProfile("Charlie", "Dog", 5, "Chicken")
pet2 = PetProfile("Luna", "Cat", 2, "Tuna")


# Step 5: Display the shared class attribute
print("{} is a {}".format(pet1.name, pet1.category))
print("{} is also a {}".format(pet2.name, pet2.category))


# Step 6: Display the details of the first pet
print("{} is a {} and is {} years old.".format(
    pet1.name, pet1.animal_type, pet1.age))
print("{} enjoys eating {}.".format(
    pet1.name, pet1.favourite_food))


# Display the details of the second pet
print("{} is a {} and is {} years old.".format(
    pet2.name, pet2.animal_type, pet2.age))
print("{} enjoys eating {}.".format(
    pet2.name, pet2.favourite_food))

