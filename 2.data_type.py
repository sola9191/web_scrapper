# String
name = "nico"
# print(name.replace("i", "d"))
# print(name.endswith("x"))

# Lists 
day_of_week=["Mon", "Tue", "Wed", "Thur", "Fri"]
print(day_of_week.count("Wed"))
# day_of_week.clear()
# day_of_week.reverse()
# day_of_week.append("Sat")
# day_of_week.append("Sun")
# day_of_week.remove("Fri")
# print(day_of_week[2])
# print(day_of_week)

# Tuples
"""
days = ("Mon", "Tue", "Wed")
print(days[0])
days=list(days)
print(days)
days=tuple(days)
print(days)
"""

# Dictionary
player = {
#    key : value
    'name' : 'nico',
    'age' : 12,
    'alive' : True,
    'fav_food' : ['burger', 'pizza']
}
print(player)
print(player['name'])
print(player.get('age'))
print(player.get('fav_food'))
player.pop("age")
player["xp"] = 1500
print(player)
player["fav_food"].append("noddles")
print(player["fav_food"])
player["name"] = "sola"
print(player["name"])