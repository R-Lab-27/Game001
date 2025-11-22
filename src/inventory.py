from item import Item
import constants

class Inventory:
    def __init__(self, max_slots=9):
        self.max_slots = max_slots
        self.slots = [None] * max_slots   # cada slot es un Item o None

    def add_item(self, item_name, quantity=1):
        #Agregar items teniendo en cuenta los límites de stack y slots disponibles

        if item_name not in constants.ALLOWED_ITEMS:
            print(f"Error: {item_name} no está en la lista de objetos permitidos.")
            return False
        # 1 Intentar agregar a un stack de objeto existente
        for slot in self.slots:
            if slot and slot.name == item_name and slot.quantity < slot.max_stack:
                espacio = slot.max_stack - slot.quantity
                agregar = min(espacio, quantity)
                slot.quantity += agregar
                quantity -= agregar

                if quantity <= 0:
                    return True
            
        # 2 Si sobran unidades, intentar crear nuevos stacks
        for i in range(self.max_slots):
            if self.slots[i] is None:
                agregar = min(constants.ALLOWED_ITEMS[item_name]["max_stack"], quantity)
                self.slots[i] = Item(item_name, agregar)
                quantity -= agregar

                if quantity <= 0:
                    return True
                
        #En el caso de que ya no hay espacio
        print("Inventario lleno, no se pudieron agregar todos los objetos")
        return False


    def remove_item(self, item_name, quantity=1):
        """ Eliminar cantidad de un objeto sin permitir negativos"""
        total = 0

        # Contamos total disponible
        for slot in self.slots:
            if slot and slot.name == item_name:
                total += slot.quantity

        
        if total < quantity:
            print("No hay cantidad suficiente para eliminar")
            return False
        
        # Eliminamos hasta cumplir la cantidad
        for i in range(self.max_slots):
            slot = self.slots[i]
            if slot and slot.name == item_name:
                eliminar = min(slot.quantity, quantity)
                slot.quantity -= eliminar
                quantity -= eliminar

                if slot.quantity == 0:
                    self.slots[i] == None

                if quantity <= 0:
                    return True
        
    
    def has_item(self, item_name):
        return item_name in self.slots
    
    def get_quantity(self, item_name):
        if item_name in self.items:
            return self.slots[item_name].quantity
        
        return 0
    
    def show(self):
        for item in self.slots:
            print(item)