
# Part 1: Make two snack boxes using sets
box_one = {"chips", "juice", "cookies", "chips", "apple"}
box_two = {"cookies", "sandwich", "juice", "sandwich"}

print("First snack box:", box_one)
print("Second snack box:", box_two)

# Part 2: Add banana to the first snack box
box_one.add("banana")
print("First box after adding banana:", box_one)

# Part 3: Find the snacks that are in both boxes
shared_items = box_one.intersection(box_two)
print("Common snacks:", shared_items)

# Part 4: Create an integer array for the snack counts
from array import array

counts = array('i', [4, 6, 3, 5])
print("Original snack counts:", counts)

# Part 5: Add a value at the start and another at the end
counts.insert(0, 2)
counts.append(7)
print("Snack counts after adding values:", counts)

# Part 6: Find how many times 5 occurs
number_of_fives = counts.count(5)
print("Number of 5s:", number_of_fives)

# Part 7: Reverse the snack counts
counts.reverse()
print("Snack counts in reverse:", counts)

# Part 8: Display the final summary
print()
print("===== SCHOOL SNACK COUNTER =====")
print("First snack box:", box_one)
print("Second snack box:", box_two)
print("Shared snacks:", shared_items)
print("Final snack counts:", counts)
print("================================")