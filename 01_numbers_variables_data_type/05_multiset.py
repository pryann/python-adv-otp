from collections import Counter


inventory = Counter()
loot = {"xp": 1000, "gold": 500, "gem": 3}
inventory.update(loot)
print(inventory)

inventory.update({"gold": 300, "gem": -2})
print(inventory)

print(inventory["gold"])
print(inventory.elements)

print(inventory.keys())
print(inventory.values())
print(inventory.items())
print(len(inventory))
