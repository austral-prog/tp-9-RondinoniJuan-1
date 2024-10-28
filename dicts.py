def create_inventory(items):
    inventario = {}

    for item in items:
        inventario[item] = inventario.get(item, 0) + 1

    return inventario

def add_items(inventory, items):
    for item in items:
        inventory[item] = inventory.get(item, 0) + 1

    return inventory

def decrement_items(inventory, items):
    for item in items:
        if item in inventory:
            inventory[item] = max(inventory[item] - 1, 0)

    return inventory

def remove_item(inventory, item):
    if item in inventory:
        del inventory[item]

    return inventory

def list_inventory(inventory):

    return [(item, cantidad) for item, cantidad in inventory.items() if cantidad > 0]
