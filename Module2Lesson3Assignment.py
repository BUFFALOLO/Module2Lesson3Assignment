"""
1. Python List Transformation
Objective: The aim of this assignment is to practice list operations & transformations.
Problem Statement: You've been given a list of grades from an exam. You need to process and analyze these grades.

Task 1: Given the list of grades, sort the grades in descending order & print the sorted list
Task 2: Calculate the average grade & print it.
"""

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort()
print(grades)
grades.reverse()
print(grades)

count = len(grades)
print(count)

total = sum(grades)
print(total)

avg = total / count
print(avg)

"""
2. Advanced List Methods & Indentity Operators 
Problem Statement: You have two lists of student names. 
1 list contains the names of students who have submitted their assignments, & the other list contains the names of students who attended the last class.

Task 1: Given the 2 lists, Find out if Alice submitted their assignment and attended class. 
HINT: How might the in keyword be of use here? And how can you check to see if Alice is in both submitted and attended in one if statement?
"""

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

student_alice = "True" if "Alice" in submitted and attended else "False"
print(student_alice )

"""
3. Advanced Slicing Techniques
Objective: The aim of this assignment is to use Python list slicing.
Problem Statement: You have a list of daily temperatures for one month, & you'd like to extract specific data from it.

Task 1: Given the list of temperatures, Extract the temperatures for the second week (7 days) of the month (index 7 to index 14). 
Expected Outcome: 83, 85, 86, 87, 88, 89, 90,

Task 2: Extract all the temperatures above 100. 
HINT: add the temperatures over 100 to a new list, or use list slicing to get the temperatures.
"""

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
second_week_temps = temperatures[7:14]
print(second_week_temps)

over_100 = temperatures.copy()
over_100 = over_100[23:]
print(over_100)
