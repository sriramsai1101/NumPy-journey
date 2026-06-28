import numpy as np

marks = np.array([
    [85, 78, 92],
    [65, 70, 60],
    [95, 88, 91],
    [45, 50, 40]
])

print("Marks Matrix:")
print(marks)

# Total marks of each student
print("Student Totals:")
print(marks.sum(axis=1))

# Average marks of each student
print("Student Averages:")
print(np.mean(marks, axis=1))

# Highest mark in entire class
print("Highest Mark:")
print(np.max(marks))

# Lowest mark in entire class
print("Lowest Mark:")
print(np.min(marks))

# Students scoring above 80
print("Marks Above 80:")
print(marks[marks > 80])
#students marks above 75
print("Marks above 75:")
print(np.sum(marks>75))
#student with highest marks
totals=marks.sum(axis=1)
print("Student with highest marks: ")
print(np.argmax(totals))
print("marks with student:  ")
print(np.argmin(totals))
