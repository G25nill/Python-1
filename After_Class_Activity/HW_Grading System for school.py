# Input marks
s1 = int(input("Enter marks for Subject 1: "))
s2 = int(input("Enter marks for Subject 2: "))
s3 = int(input("Enter marks for Subject 3: "))

# Subject 1 grade
if s1 >= 80:
    print("Subject 1 Grade: A+")
elif s1 >= 70:
    print("Subject 1 Grade: A")
elif s1 >= 60:
    print("Subject 1 Grade: B")
elif s1 >= 50:
    print("Subject 1 Grade: C")
elif s1 >= 40:
    print("Subject 1 Grade: D")
else:
    print("Subject 1 Grade: F")

# Subject 2 grade
if s2 >= 80:
    print("Subject 2 Grade: A+")
elif s2 >= 70:
    print("Subject 2 Grade: A")
elif s2 >= 60:
    print("Subject 2 Grade: B")
elif s2 >= 50:
    print("Subject 2 Grade: C")
elif s2 >= 40:
    print("Subject 2 Grade: D")
else:
    print("Subject 2 Grade: F")

# Subject 3 grade
if s3 >= 80:
    print("Subject 3 Grade: A+")
elif s3 >= 70:
    print("Subject 3 Grade: A")
elif s3 >= 60:
    print("Subject 3 Grade: B")
elif s3 >= 50:
    print("Subject 3 Grade: C")
elif s3 >= 40:
    print("Subject 3 Grade: D")
else:
    print("Subject 3 Grade: F")

# Total and average
total = s1 + s2 + s3
average = total / 3

print("Total:", total)
print("Average:", average)

# Overall grade
if average >= 80:
    print("Overall Grade: A+")
elif average >= 70:
    print("Overall Grade: A")
elif average >= 60:
    print("Overall Grade: B")
elif average >= 50:
    print("Overall Grade: C")
elif average >= 40:
    print("Overall Grade: D")
else:
    print("Overall Grade: F")