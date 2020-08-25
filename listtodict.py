def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total+= v
    print("Total number of items: " + str(item_total))


def addToInventory(inventory, addedItems):
    for sum in addedItems: # sum created here - starts at 0 anyway
        inventory.setdefault(sum, 0) # This adds a defaulted zero value key to the inventory dict if it's not already there
        inventory[sum] += 1
    return inventory


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
