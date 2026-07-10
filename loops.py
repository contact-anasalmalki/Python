materials = ["nitrogen", "oxygen", "argon"]
for material in materials:
    print(f"Analyzing sample: {material.title()}")
print("Analysis is complete.")

squares = []
for y in range(1, 11):
    x = y**2
    squares.append(x)
print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))

squares_shortcut = [x**2 for x in range(1, 11)]
print(squares_shortcut)
print(squares_shortcut[:4])
print(squares_shortcut[3:7])
print(squares_shortcut[-3:])
squares_copy = squares_shortcut[:]
squares_copy.append(999)
print(f"{squares_shortcut}{squares_copy}")

standard_conditions = (273.15, 101.325)
print(standard_conditions[0:2])
# standard_conditions[0] = 298.15
standard_conditions = (298.15, 101.325)
print(standard_conditions)
