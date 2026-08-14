# Store the habit details in a tuple
habit_info = ("Reading", True, 7, 20.5)
print(habit_info)

# Store the completion record for each day
# 1 = completed, 0 = missed
weekly_habits = (1, 0, 1, 1, 0, 1, 1)
print(weekly_habits)

# Display the number of days in the tuple
total_days = len(weekly_habits)
print("Total days tracked:", total_days)

# Read specific days using their index numbers
print("Day 1 status:", weekly_habits[0])
print("Day 4 status:", weekly_habits[3])

# Select groups of days using slicing
first_three = weekly_habits[:3]
print("First three days:", first_three)

weekend = weekly_habits[5:]
print("Weekend days:", weekend)

# A tuple cannot be changed directly.
# Instead, make a new tuple by adding another value.
weekly_habits = weekly_habits + (1,)
print("After adding one more day:", weekly_habits)

# Count completed and missed days
completed = weekly_habits.count(1)
missed = weekly_habits.count(0)

print("Completed days:", completed)
print("Missed days:", missed)

# Check the record day by day using a loop
done = 0
not_done = 0

for status in weekly_habits:
    if status == 1:
        done += 1
    else:
        not_done += 1

# Compare completed days with missed days
if done > not_done:
    print("Great habit progress!")
else:
    print("Try to be more consistent!")

# Display the final tracker
print()
print("===== WEEKLY HABIT TRACKER =====")
print("Habit Name:", habit_info[0])
print("Weekly Record:", weekly_habits)
print("Completed:", done)
print("Missed:", not_done)
print("================================")

