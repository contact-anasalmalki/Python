temps_fahrenheit = [32, 68, 104, 122, 212]
# need to start a new list before the for loop to store the converted values
temps_celsius = []
for y in temps_fahrenheit[:]:
    temp_celsius = (y - 32) * 5 / 9
    temps_celsius.append(temp_celsius)
print(temps_celsius)

# in list comprehension, the new list is created in one line of code
# no need to create a new list before the for loop, and no need to use the append() method
temps_fahrenheit = [1, 2, 3, 4, 5]
# lists are iterable, so we can use a for loop to iterate through the list and perform the conversion in one line of code without the need for a new list or the append() method or []
temps_celsius = [(temp - 32) * 5 / 9 for temp in temps_fahrenheit]

pressures = [101.3, 105.4, 98.2, 110.1, 103.5]
print(min(pressures))
print(max(pressures))
average_pressure = sum(pressures) / len(pressures)
print(average_pressure)

# Wrong_way
equipments = ["pump", "valve", "reactor"]
steps = 1
instructions = []
for equipment in equipments[:]:
    instructions.append(equipment)
    #     print(f"{steps}. Install {instructions.title()}") this is wrong because .title() .lower() .upper() only applies to strings (str) while instruction is Lists (list)
    print(f"{steps}. Install {instructions}")
    instructions.pop(0)
    steps = steps + 1
print("Installation check is complete")

# correct_way
equipments = ["pump", "valve", "reactor"]
steps = 1
for equipment in equipments[
    :
]:  # can remove [:] from equipments[:] because we are reading only not deleting
    # print(f"{steps}. Install {equipment.title()}") this is correct because here equipment is a string (str) not a list
    print(f"{steps}. Install {equipment.title()}")
    steps = steps + 1
print("Installation check is complete")

# best way
equipments = ["pump", "valve", "reactor"]

# 'enumerate' automatically tracks the count and the item at the same time
for step, equipment in enumerate(equipments, start=1):
    print(f"{step}. Install {equipment.title()}.")

print("Installation check is complete.")
