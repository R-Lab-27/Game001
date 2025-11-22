import pygame


class InventoryUI:
    def __init__(self, inventory):
        self.inventory = inventory
        self.open = False

        self.slot_size = 32
        self.margin = 1

        self.columns = 3
        self.rows = 3


        self.titulo = "Inventory"
        # crear superficie oscura semitransparente para inventario

        self.bg = pygame.Surface((98, 98))
        self.bg.fill((170, 170, 170))
        self.bg.set_alpha(200)

    def draw(self, screen):
        if not self.open:
            return

        sw, sh = screen.get_size()
         # Dibujar slots
        x_start = sw//2 - 300
        y_start = sh//2 - 150
        screen.blit(self.bg, (x_start, y_start))

        font = pygame.font.SysFont(None, 20)
        #Imprimir titulo del Inventario
        inventory_title = font.render(self.titulo, True, (0,0,0))
        screen.blit(inventory_title, (x_start, y_start - 14))

        font = pygame.font.SysFont(None, 16)

        slot_index = 0

        for row in range(self.rows):
            for col in range(self.columns):
                x = x_start + col * (self.slot_size + self.margin)
                y = y_start + row * (self.slot_size + self.margin)

                pygame.draw.rect(screen, (200,200,200), (x,y,self.slot_size,self.slot_size), 1)

                item = self.inventory.slots[slot_index]

                if item:

                    # icon_x = x + (self.slot_size - item.icon.get_width()) // 2                    
                    # icon_y = y + (self.slot_size - item.icon.get_height()) // 2
                    #Muestra el icono en el slot
                    offset_x = 1
                    offset_y = 1
                    screen.blit(item.icon, (x, y))

                    #muestra el la cantidad del objeto sobre la imagen del icono
                    qty = font.render(str(item.quantity), True, (0,0,0))
                    qty_rect = qty.get_rect()
                    qty_rect.bottomright = (x + self.slot_size, y + self.slot_size)

                    screen.blit(qty, qty_rect)

                slot_index += 1

    def toggle(self):
        self.open = not self.open
