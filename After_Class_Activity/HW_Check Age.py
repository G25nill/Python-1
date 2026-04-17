# Check Age Program

age = int(input("Enter your age: "))

# Check if age is between 10 and 20
if age >= 10 and age <= 20:

    print("Age is between 10 and 20")

    # Nested condition suggesting activities for specific ages
    if age == 10:
        print("Sports: Football, Cricket, Cycling")
        print("Grade: Primary School")
        print("Activities: Playing, Drawing, Basic Learning")
        print("Hobbies: Reading story books, Playing games")

    elif age == 20:
        print("Sports: Gym, Football, Running")
        print("Grade: University/College")
        print("Activities: Studying, Skill Development, Part-time work")
        print("Hobbies: Traveling, Fitness, Learning new skills")

    else:
        print("General Activities: Study, Sports, Personal development")

else:
    print("Age is NOT between 10 and 20")