inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

del inventory['pears']
inventory['bananas'] = inventory['bananas'] + 200

numItems = len(inventory)
print(numItems)
print(inventory)

for akey in inventory.keys(): # The order of which we get the keys is undefined
    print "Got key", akey, "which maps value to", inventory[akey]

ks = list(inventory.keys())
print(ks)

for k in inventory:
   print "Got key", k 
