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
# 2--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
pressures = [101.3, 105.4, 98.2, 110.1, 103.5]
print(min(pressures))
print(max(pressures))
average_pressure = sum(pressures) / len(pressures)
print(average_pressure)
# 3--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Wrong way
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

# correct way
equipments = ["pump", "valve", "reactor"]
steps = 1
for equipment in equipments[
    :
]:  # can remove [:] from equipments[:] because we are reading only not deleting
    # print(f"{steps}. Install {equipment.title()}") this is correct because here equipment is a string (str) not a list
    print(f"{steps}. Install {equipment.title()}")
    steps = steps + 1
print("Installation check is complete")
# 4--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# hard way
flow_rates = [12.5, 14.2, 11.8, 15.0]
hour = 1
recorded_flows = []  # list not a value
for flow_rate in flow_rates:
    recorded_flows.append(flow_rate)
    running_total = sum(recorded_flows)
    print(f"Total volume after hour {hour}: {running_total} liters")
    hour = hour + 1

# easy way
flow_rates = [12.5, 14.2, 11.8, 15.0]
hour = 1
total_volume = 0.0  # empty piggy bank (value not a list)

for flow_rate in flow_rates:
    total_volume = total_volume + flow_rate
    print(f"Total volume after hour {hour}: {total_volume} liters")
    hour = hour + 1
# 5--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
temps = [55.2, 56.4, 58.1, 54.3, 55.0, 57.2, 59.3, 56.1, 55.8, 54.9]
mid_day_temps = []
# mid_day_temps = temps[3:7] (this is the correct answer)
for index in temps[3:7]:
    mid_day_temps.append(index)
print(mid_day_temps)
average_value = sum(mid_day_temps) / len(mid_day_temps)
print(f"The average mid-day temperature is: {average_value}")
# 6--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
