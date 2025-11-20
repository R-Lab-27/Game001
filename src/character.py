import pygame
from animated_sprite import AnimatedSprite
from sprite_sheet import SpriteSheet

class Player:
    def __init__(self, x, y):
        #Carga el mapa de animaciones del personaje
        self.sprite_sheet = SpriteSheet("/home/r/Training/Proyectos/Game001/src/assets/adventurer-1.3-Sheet.png", 8, 12)
        # Usar AnimatedSprite
        # Definir los rangos para idle, walk y run
        animation_ranges = {
            "idle": (0, 4),
            "agachar": (5, 8),
            "run": (9, 16),
            "jump": (17, 25)
        }
        self.anim = AnimatedSprite(self.sprite_sheet, animation_ranges=animation_ranges, frame_duration=5)

        self.rect = pygame.Rect(x, y,
                                self.sprite_sheet.frame_width,
                                self.sprite_sheet.frame_height)
        
        # Velocidad física
        self.vel_x = 0.0
        self.acceleration = 0.3   # cuánto acelera al apretar tecla
        self.max_walk_speed = 2.0
        self.max_run_speed = 5.0
        self.friction = 0.3       # desacelera cuando no se presiona

        #nuestro vector de dirección
        self.facing_right = True # suposición inicial
        
        # Estado de animación actual
        self.state = "idle"
        self.anim.play(self.state)

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            # acelerar hacia la derecha
            self.vel_x += self.acceleration
            self.facing_right = True
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            # acelerar hacia la izquierda
            self.vel_x -= self.acceleration
            self.facing_right = False
        else:
            # no presionás, que frene
            if self.vel_x > 0:
                self.vel_x -= self.friction
                if self.vel_x < 0:
                    self.vel_x = 0
            elif self.vel_x < 0:
                self.vel_x += self.friction
                if self.vel_x > 0:
                    self.vel_x = 0

        # limitar la velocidad
        # si querés que "run" sea cuando vas rápido
        # podés hacer algo como:
        if abs(self.vel_x) > self.max_run_speed:
            self.vel_x = self.max_run_speed * (1 if self.vel_x > 0 else -1)

    def update_state(self):
        # decís cuál estado usar según la velocidad
        speed = abs(self.vel_x)
        if speed < 0.1:
            new_state = "idle"
        elif speed < self.max_walk_speed:
            new_state = "run"
        else:
            new_state = "run"

        if new_state != self.state:
            self.state = new_state
            self.anim.play(new_state)

    def update(self):
        self.handle_input()
        self.update_state()

        # actualizás animación
        self.anim.update()

        # actualizás posición según velocidad
        self.rect.x += self.vel_x

    def draw(self, screen):
        frame = self.anim.get_current_frame()
        #voltear la imagen si va en dirección izquierda
        if not self.facing_right:
            frame = pygame.transform.flip(frame, True, False)
        screen.blit(frame, self.rect.topleft)
