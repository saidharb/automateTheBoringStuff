def addToInventory(inventory, addedItems)->dict:
    for i in range (len(addedItems)):
        #print(addedItems[i])
        inventory.setdefault(addedItems[i],0)
        inventory[addedItems[i]]=inventory[addedItems[i]]+1
        #print(inventory[addedItems[i]])
    return inventory

def displayInventory(inventory)->None:
    print("Inventory:")
    item_total=0
    for k, v in inventory.items():
        print(str(v)+' '+k)
        item_total=item_total+v
    print("Total number of items: " + str(item_total))

        
lol={'rope':1,'torch':6,'gold coin':42,'dagger':1,'arrow':12}
displayInventory(lol)
dragonLoot=['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby','spell book', 'spell book']
inv=addToInventory(lol, dragonLoot)
displayInventory(inv)