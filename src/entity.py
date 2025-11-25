#Clase entity para utilizarlo como superclase para las demas clases
import pygame
from animated_sprite import AnimatedSprite

class Entity():
    def __init__(self, pos_x, pos_y, platforms, sprite_sheet, animation_ranges, frame_duration=6):
        #Propiedades de animación y apariencia
        self.sprite_sheet = sprite_sheet
        self.anim = AnimatedSprite(sprite_sheet, animation_ranges=animation_ranges, frame_duration=frame_duration)
        self.facing_right = True

        #Estado de animacón actual
        self.state = "idle"
        self.anim_play(self.state)

        #Propiedades del Rectángulo (Rect y Hitbox)
        #Asumiendo que calculamos hitbox y offset en la clase hija
        self.rect = pygame.Rect(pos_x, pos_y, 32, 32) #Ajustar en clase hija según sea necesario
        self.platforms = platforms

        #Propiedades físicas
        self.vel_x = 0
        self.vel_y = 0
        self.gravity = 0.5
        self.falling_terminal_vel = 10
        self.is_in_air = False

    def apply_gravity(self):
        # (El mismo código que tienes en Player.apply_gravity)
        self.vel_y += self.gravity
        self.vel_y = min(self.vel_y, self.falling_terminal_vel)

    def resolve_collisions(self):
        # (El mismo código que tienes en Player.resolve_collisions)
        self.rect.x += self.vel_x
        # ... (lógica de colisión X)
        self.rect.y += self.vel_y
        # ... (lógica de colisión Y y chequeo de is_in_air)
    # Definir en subclase
    def update_state(self):
        pass # La lógica de estado (idle, run, jump) es específica del Player/Enemy

    def update(self):
        # Esto contiene la lógica que TODOS los personajes necesitan
        self.apply_gravity()
        self.resolve_collisions()
        self.anim.update()

    def draw(self, screen):
        # (El mismo código que tienes en Player.draw para dibujar el frame volteado)
        frame = self.anim.get_current_frame()
        if not self.facing_right:
            frame = pygame.transform.flip(frame, True, False)
        
        # Necesitarás definir offset_x/y en las clases hijas si se usan aquí
        screen.blit(frame, (self.rect.x, self.rect.y)) # Simplificado, usar offset real

