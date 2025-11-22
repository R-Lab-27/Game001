import pygame
import item_constants
from sprite_sheet import SpriteSheet

class Item:
    def __init__(self, name, quantity=1):

        data = item_constants.ALLOWED_ITEMS[name]
        

        self.name = name
        self.description = data["description"]
        self.quantity = quantity
        self.max_stack = data["max_stack"]
        
        # Indice del sprite dentro del spritesheet
        index = data["index"]

        # Obtener el frame desde el spritesheet de items
        self.icon = item_constants.ITEM_SPRITESHEET.get_frame(index)
        print(f"icon: {index} -> x: {self.icon.get_width()} y: {self.icon.get_height()}")

        # Escalar icono
        self.icon = pygame.transform.scale(self.icon, (32, 32)) # tamaño estandar

    def __repr__(self):
        return f"{self.name} x{self.quantity}"