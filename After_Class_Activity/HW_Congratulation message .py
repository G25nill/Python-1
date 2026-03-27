# Name: Congratulation message

# Step 1: Take user input
sentence = input("Enter your congratulation message: ")

# Step 2: Length
print("Length of the sentence:", len(sentence))

# Step 3: Indexing (first character)
if len(sentence) > 0:
    print("First character:", sentence[0])

# Step 4: Slicing
print("Sliced part:", sentence[:5])

# Step 5: Split sentence
words = sentence.split()
if len(words) > 0:
    part = words[0]
else:
    part = ""
print("First word after splitting:", part)

# Step 6: Case conversion 
if sentence.islower():
    converted = sentence.upper()
elif sentence.isupper():
    converted = sentence.lower()
else:
    converted = sentence.swapcase()

print("Converted sentence:", converted)

# Step 7: Concatenation
new_string = " You did it!"
final_string = converted + new_string
print("Concatenated string:", final_string)

# Step 8: Reverse
reversed_string = final_string[::-1]
print("Reversed string:", reversed_string)