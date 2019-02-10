inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
print(list(inventory.values()))
print(list(inventory.items()))

for (k,v) in inventory.items():
    print("Got", k, "that maps to", v)

for k in inventory:
    print("Got", k, "that maps to", inventory[k])

print('apples' in inventory)
print('cherries' in inventory)

if 'bananas' in inventory:
    print(inventory['bananas'])
else:
    print("we have no bananas")

print(inventory.get("apples"))
print(inventory.get("cherries"))

print(inventory.get("cherries", 0))

if inventory.get("cherries"):
    print(inventory['cherries'])
else:
    print("we have no cherries")
