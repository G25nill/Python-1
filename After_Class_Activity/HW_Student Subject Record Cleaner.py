
# Create the student record dictionary
student_data = {"id1": {"name": "Sara","class": "V","subject": "english, math, science"},
    "id2": {"name": "David","class": "V","subject": "english, math, science"},
    "id3": {"name": "Sara","class": "V","subject": "english, math, science"},
    "id4": {"name": "Surya", "class": "V","subject": "english, coding, math"}}

# Show the records before making any changes
print("Original Student Records:")
print(student_data)

# Safely look up student records
print()
print("Details of id1:")
print(student_data.get("id1", "Not Found"))

print()
print("Details of id5:")
print(student_data.get("id5", "Not Found"))

# Add a new student to the dictionary
student_data["id5"] = {"name": "Anaya","class": "V","subject": "english, art, science"}

print()
print("After adding id5:")
print(student_data)

# Change the subject information for id2
student_data["id2"]["subject"] = "english, math, coding"

print()
print("After updating id2 subject:")
print(student_data["id2"])

# Find and remove duplicate records
cleaned_data = {}
seen_records = []

for student_id, record in student_data.items():
    record_key = (
        record["name"],
        record["class"],
        record["subject"])

    if record_key not in seen_records:
        seen_records.append(record_key)
        cleaned_data[student_id] = record

student_data = cleaned_data

print()
print("After removing duplicate records:")
print(student_data)

# Remove id4 using pop()
removed_student = student_data.pop("id4", "Student not found")

print()
print("Removed student:")
print(removed_student)

# Find the number of remaining records
remaining_students = len(student_data)

print()
print("Total student records left:", remaining_students)

# Display every remaining student record
print()
print("===== FINAL STUDENT SUBJECT RECORDS =====")

for student_id, details in student_data.items():
    print(student_id, ":", details)

print("==========================================")

