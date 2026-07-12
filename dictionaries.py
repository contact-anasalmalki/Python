alien_0 = {"color": "green", "points": 5}
alien_color = alien_0["color"]
new_points = alien_0["points"]
print(f"The alien is {alien_color}\n")
print(f"You just earned {new_points}")
alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)
alien_0["color"] = "yellow"
alien_0["x_position"] = 10
print(alien_0)
del alien_0["points"]
print(alien_0)
# single quotes for internal dictionary keys, and double quotes for printed user messages.
favorite_foods = {
    "jen": "pizza",
    "sarah": "sushi",
    "edward": "tacos",
    "phil": "pizza",
}
sarah_foods = favorite_foods["sarah"]
print(f"Sarah's favorite food is {sarah_foods.title()}")

# We use '.items()' and define TWO temporary loop variables: 'name' and 'food'
# for name, food in favorite_foods.items():
for name, food in favorite_foods.items():
    print(f"[{name.title()}'s] favorite food is [{food.title()}]")

# This only retrieves the keys ('jen', 'sarah', etc.)
for name in favorite_foods.keys():
    print(name)

# for food in favorite_foods.values(): This only retrieves the values ('pizza', 'sushi', etc.)
# Wrapping .values() in set() automatically filters out duplicates
for food in set(favorite_foods.values()):
    print(food)
# unique foods printed in this order: tacos, pizza, sushi. This is different from the order they were defined in your dictionary.
# Sets are completely unordered collections. When you convert data into a set()

# Nesting (A dictionary in a List)
alien_0 = {"color": "green", "points": 5}
alien_1 = {"color": "yellow", "points": 10}
alien_2 = {"color": "red", "points": 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    alien_color = alien["color"]
    alien_points = alien["points"]
    print(f'"This alien is {alien_color} and is worth {alien_points} points."')

# Nesting (A List in a dictionary)
favorite_places = {
    "jen": ["paris", "london"],
    "sarah": ["tokyo"],
    "edward": ["new york", "rome"],
}
for name, places in favorite_places.items():
    print(f"\n{name.title()} favorite places are:")
    for place in places:
        print(f"\t{place.title()}")

# Nesting (A Dictionary in a dictionary)
users = {
    "aeinstein": {
        "first": "albert",
        "last": "einstein",
        "location": "princeton",
    },
    "mcurie": {
        "first": "marie",
        "last": "curie",
        "location": "paris",
    },
}
for username, user_info in users.items():
    print(f"Username: {username}")
    print(f"\tFull name:{user_info["first"].title()} {user_info["last"].title()}")
    print(f"\tLocation:{user_info["location"].title()}")
