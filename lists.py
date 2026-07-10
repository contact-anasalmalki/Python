# lists are used to store multiple items in a single variable
components = ["valve", "pump", "reactor", "piping"]

# indexing starts from 0, so the first item in the list is at index 0
# negative indexing starts from -1, so the last item in the list is at index -1
print(components[0])
print(components[-1])
print(f"the {components[0]} needs maintenance.".title())
components[0] = "control_valve"

# append() method adds an item to the end of the list
components.append("compressor")

# insert() method adds an item at a specific index
components.insert(1, "heat_exchanger")
print(components)

# deleting items from a list can be done using the del statement, pop() method, or remove() method()
# difference between del statement and pop() method is that del statement does not return the removed item, while pop() method does.
# difference between pop() method and remove() method is that pop() method removes an item at a specific index, while remove() method removes the first (in case of duplicates) item with a specific value.

# del statement removes an item at a specific index
del components[0]

# pop() method removes the last item from the list
components.pop()

# pop() method can also remove an item at a specific index
last_removed = components.pop(1)
print(f"successfully popped: {last_removed}".capitalize())

# remove() method removes the first item (in case of duplicates) with a specific value
components.remove("reactor")
print(components)

cities = ["Dammam", "Khobar", "Riyadh", "Jeddah", "Jubail"]

# length of a list can be found using len() function
print(len(cities))

# sorting a list can be done using the sort() method or sorted() function (alphabetically sorts the list in ascending order by default, but can also sort in descending order by passing reverse=True as an argument)

# sorted() does not change the original list
print(sorted(cities))
print(cities)

# sort() method changes the original list
cities.sort()
print(cities)

# pop() method removes the last item from the list and returns it (can be used to store the removed item in a variable)
popped_city = cities.pop()
print(popped_city)
