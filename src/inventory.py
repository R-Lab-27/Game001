from item import Item

class Inventory:
    def __init__(self):
        self.items = {}   #{"potion": Item, "sword": Item}

    def add_item(self, item_name, quantity=1, description=""):
        if item_name in self.items:
            self.items[item_name].quantity += quantity
        else:
            self.items[item_name] = Item(item_name, description, quantity)

    def remove_item(self, item_name, quantity=1):
        if item_name not in self.items:
            return False
        
        self.items[item_name].quantity -= quantity

        if self.items[item_name].quantity <= 0:
            del self.items[item_name]

        return True
    
    def has_item(self, item_name):
        return item_name in self.items
    
    def get_quantity(self, item_name):
        return self.items.get(item_name, 0)
    
    def show(self):
        for item in self.items.values():
            print(item)