# Example 1: A simple lambda function
add = lambda x, y: x + y
result = add(5, 3)
print(result)  # Output: 8

# Example 2: Sorting a list of tuples using a lambda function
students = [
    ("Alice", 25),
    ("Bob", 18),
    ("Charlie", 22),
    ("David", 30)
]

# Sort the list of students based on their age
students.sort(key=lambda student: student[1])
print(students)
# Output: [('Bob', 18), ('Charlie', 22), ('Alice', 25), ('David', 30)]

# Example 3: Using lambda with built-in functions like map
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]
