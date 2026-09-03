# Student Grade Book

grades = {"Rahim": 85, "Nadia": 92, "Arif": 76, "Sadia": 88, "Tanvir": 71}

print("=" * 38)
print("STUDENT GRADE BOOK")
print("=" * 38)

# Calculate class average
total_score = 0

for score in grades.values():
    total_score += score

class_average = total_score / len(grades)

print("Class Average:", f"{class_average:.1f}")

# Find highest and lowest scorers
highest_student = max(grades, key=grades.get)
lowest_student = min(grades, key=grades.get)

print("Highest Scorer:", highest_student, "-", grades[highest_student])
print("Lowest Scorer:", lowest_student, "-", grades[lowest_student])

# Student score lookup
student_name = input("Enter a student's name: ")

student_score = grades.get(student_name, None)

if student_score is not None:
    print(student_name, "scored", student_score)
else:
    print("Sorry, student not found.")