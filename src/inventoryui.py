import pygame


class InventoryUI:
    def __init__(self, inventory):
        self.inventory = inventory
        self.open = False

        self.slot_size = 32
        self.margin = 1

        self.columns = 3
        self.rows = 3

        # crear superficie oscura semitransparente
        self.bg = pygame.Surface((102, 102))
        self.bg.fill((30, 30, 30))
        self.bg.set_alpha(200)

    def draw(self, screen):
        if not self.open:
            return

        sw, sh = screen.get_size()
        screen.blit(self.bg, (sw//2 - 102, sh//2 - 102))

        font = pygame.font.SysFont(None, 18)

        # Dibujar slots
        x_start = sw//2 - 102
        y_start = sh//2 - 102

        slot_index = 0

        for row in range(self.rows):
            for col in range(self.columns):
                x = x_start + col * (self.slot_size + self.margin)
                y = y_start + row * (self.slot_size + self.margin)

                pygame.draw.rect(screen, (200,200,200), (x,y,self.slot_size,self.slot_size), 2)

                item = self.inventory.slots[slot_index]

                if item:
                    screen.blit(item.icon, (x+8, y+8))
                    qty = font.render(str(item.quantity), True, (255,255,255))
                    screen.blit(qty, (x+30, y+30))

                slot_index += 1

    def toggle(self):
        self.open = not self.open
