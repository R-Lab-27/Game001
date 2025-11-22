import pygame
from constants import ALLOWED_ITEMS, ITEM_SPRITESHEET

class Item:
    def __init__(self, name, quantity=1):

        data = ALLOWED_ITEMS[name]

        self.name = name
        self.description = data["description"]
        self.quantity = quantity
        self.max_stack = data["max_stack"]
        
        # Indice del sprite dentro del spritesheet
        index = data["index"]

        # Obtener el frame desde el spritesheet de items
        self.icon = ITEM_SPRITESHEET.get_frame(index)

        # Escalar icono
        self.icon = pygame.transform.scale(self.icon, (32, 32)) # tamaño estandar

    def __repr__(self):
        return f"{self.name} x{self.quantity}"