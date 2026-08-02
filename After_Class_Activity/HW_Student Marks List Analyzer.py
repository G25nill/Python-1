
# STUDENT MARKS LIST ANALYZER

# Step 1: Create and display an empty list
blank_marks = []
print("Empty List:", blank_marks)

# Create a list containing five student marks
student_marks = [85, 72, 90, 66, 78]
print("Student Marks List:", student_marks)


# Step 2: Repeat a sample list using the * operator
practice_marks = [10, 20, 30]
repeated_marks = practice_marks * 2

print("Repeated Sample List:", repeated_marks)


# Step 3: Find the number of marks in the list
number_of_students = len(student_marks)

print("Total Number of Marks:", number_of_students)


# Step 4: Access the first and last items using indexing
first_student_mark = student_marks[0]
last_student_mark = student_marks[-1]

print("Mark at the First Position:", first_student_mark)
print("Mark at the Last Position:", last_student_mark)


# Step 5: Use slicing to access the first three marks
first_three = student_marks[0:3]

print("First Three Marks:", first_three)

# Reverse the list using slicing
marks_in_reverse = student_marks[::-1]

print("Marks in Reverse Order:", marks_in_reverse)


# Step 6: Create a function to find marks
# whose first and last digits are the same
def count_same_digit_marks(mark_values):
    matching_values = []
    matching_count = 0

    for value in mark_values:
        value_as_text = str(value)

        if value_as_text[0] == value_as_text[-1]:
            matching_values.append(value)
            matching_count += 1

    print("Marks with Matching First and Last Digits:",
          matching_values)

    return matching_count


# Check the marks in the main student marks list
total_matching_marks = count_same_digit_marks(student_marks)

print("Number of Matching Marks:", total_matching_marks)


# Step 7: Calculate the total using a for loop
sum_of_marks = 0

for value in student_marks:
    sum_of_marks = sum_of_marks + value


# Calculate the average mark
average_mark = sum_of_marks / len(student_marks)

print("Sum of All Marks:", sum_of_marks)
print("Average Mark:", average_mark)


# Sort the list to find the lowest and highest marks
student_marks.sort()

lowest_mark = student_marks[0]
highest_mark = student_marks[-1]

print("Lowest Mark:", lowest_mark)
print("Highest Mark:", highest_mark)


# Final summary
print()
print("========================================")
print("     STUDENT MARKS LIST ANALYZER")
print("========================================")
print("Sorted Student Marks:", student_marks)
print("Number of Marks:", number_of_students)
print("Total Marks:", sum_of_marks)
print("Average Marks:", average_mark)
print("Smallest Mark:", lowest_mark)
print("Largest Mark:", highest_mark)
print("========================================")
