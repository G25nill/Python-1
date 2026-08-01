L = [4, 5, 1, 2, 9, 7, 10, 8]
print("Original List :", L)

# variable to store the sum of
# the list
count = 0

# Finsing the sum
for i in L:
    count += i

# divide the total elements by
# number of elements 
avg = count/len(L)

print("sum = ", count)
print("average = ", avg)

#sorting the elements of the list
L.sort()

# Sorting the elements of the list
print("Smallest element is:", L[0])

# printing the last element
print("Large element is:", L[-1])
