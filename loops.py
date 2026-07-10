# for loop is used to iterate over a sequence (list, tuple, dictionary, set, or string).
materials = ["nitrogen", "oxygen", "argon"]
for material in materials:
    print(f"Analyzing sample: {material.title()}")
print("Analysis is complete.")

# range() function generates a sequence of numbers, starting from 0 by default, and increases by 1 (by default), and stops before a specified number.
squares = []
for y in range(1, 11):
    x = y**2
    squares.append(x)
print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))

# list comprehension (shortcut) to create a list of squares
squares_shortcut = [x**2 for x in range(1, 11)]
print(squares_shortcut)
print(squares_shortcut[:4])
print(squares_shortcut[3:7])
print(squares_shortcut[-3:])
squares_copy = squares_shortcut[:]
squares_copy.append(999)
print(f"{squares_shortcut}{squares_copy}")

# List (tuples) can not be changed, but they can be reassigned to a new value.
standard_conditions = (273.15, 101.325)
print(standard_conditions[0:2])
# standard_conditions[0] = 298.15
standard_conditions = (298.15, 101.325)
print(standard_conditions)
