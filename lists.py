components=["valve","pump","reactor","piping"]
print(components[0])
print(components[-1])
print(f"the {components[0]} needs maintenance.".title())
components[0]="control_valve"
components.append("compressor")
components.insert(1,"heat_exchanger")
print(components)
del components[0]
components.pop()
last_removed = components.pop()
print(f"successfully popped: {last_removed}".capitalize())
components.remove("reactor")
print(components)
cities=["Dammam","Khobar","Riyadh","Jeddah","Jubail"]
print(len(cities))
print(sorted(cities))
print(cities)
cities.sort()
print(cities)
popped_city = cities.pop()
print(popped_city)