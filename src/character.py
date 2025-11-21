import pygame
from animated_sprite import AnimatedSprite
from sprite_sheet import SpriteSheet


class Player:
    def __init__(self, x, y, platforms):
        #Carga el mapa de animaciones del personaje
        self.sprite_sheet = SpriteSheet("/home/r/Training/Proyectos/Game001/src/assets/adventurer-1.3-Sheet.png", 8, 12)
        # Usar AnimatedSprite
        # Definir los rangos para idle, walk y run
        
        animation_ranges = {
            "idle": (0, 3),
            "agachar": (4, 7),
            "run": (8, 15),
            "jump": (16, 23),
            "attack_1":(40, 47),
            "attack_2": (48, 52),
            "attack_3": (53, 58)
        }


        self.anim = AnimatedSprite(self.sprite_sheet, animation_ranges=animation_ranges, frame_duration=4)

        # Rectangulo de colisión del personaje
        self.rect = pygame.Rect(x, y,
                                self.sprite_sheet.frame_width * 0.7,
                                self.sprite_sheet.frame_height)
        
        # Velocidad física
        self.vel_x = 0.0
        self.vel_y = 0.0
        self.acceleration = 0.1   # cuánto acelera al apretar tecla
        self.max_walk_speed = 2.0
        self.max_run_speed = 3.0
        self.friction = 0.3       # desacelera cuando no se presiona

        # Gravedad y salto
        self.gravity = 0.5
        self.jump_strength = -8 #velocidad inicial cuando salta
        self.falling_terminal_vel = 10
        self.jump_release = True

        # Plataformas (listas o groupo de objetos con los cuales podemos colicionar)
        self.platforms = platforms

        #nuestro vector de dirección
        self.facing_right = True # suposición inicial

        #Esta atacando
        self.attack = False

        #Variables para el combo de ataque
        self.combo_step = 0  # 0 = sin combo, 1 ,2,3 para ataques
        self.combo_buffer = False
        
        # Estado de animación actual
        self.state = "idle"
        self.anim.play(self.state)
        self.is_in_air = False

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            # acelerar hacia la derecha
            if self.is_in_air:
                # Si actualmente esta en el aire, que ya no aumente la aceleración en el eje x, si no que por fricción la reduzca
                pass
            else:
                #Cuando la velocidad en dirección derecha o izquierda es muy alta, al cambiar abruptamente de dirección se produce un desliz hacia la
                #dirección contraría de donde se apreta el botón, para solucionarlo, en cuanto se aprete el botón si la velocidad es muy alta en -x o x se establece en cero
                if self.vel_x < 0:
                    self.vel_x = 0
                    self.vel_x += self.acceleration
                else:
                    self.vel_x += self.acceleration
            self.facing_right = True
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            # acelerar hacia la izquierda
            if self.is_in_air:
                 # Si actualmente esta en el aire, que ya no aumente la aceleración en el eje x, si no que por fricción la reduzca
                pass
            else:
                if self.vel_x > 0:
                    self.vel_x = 0
                    self.vel_x -= self.acceleration
                else:
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

        #Saltar
        if keys[pygame.K_SPACE]:
            #solo saltar si no esta ya en el aire
            if self.jump_release and not self.is_in_air:
                self.vel_y = self.jump_strength
                self.is_in_air = True
                self.jump_release = False
        else:
            #La dejo de presionar la tecla
            self.jump_release = True

        #Atacar
        if keys[pygame.K_r]:
            #Solo atacar si no estamos en el aire, en este caso activamos el buffer para rastrear el combo de ataque
            if self.combo_step > 0: #Si ya esta en un ataque
                self.combo_buffer = True #permitir combo
            elif not self.is_in_air:
                self.combo_buffer = True
            
        # limitar la velocidad
        if abs(self.vel_x) > self.max_run_speed:
            self.vel_x = self.max_run_speed * (1 if self.vel_x > 0 else -1)

    def apply_gravity(self):
        # Aplicar la gravedad
        self.vel_y += self.gravity
        # Limitar la velocidad de caida
        # Velocidad de caida terminal 10.0 (Si alcanza esa velocidad de caida, no se salva)
        self.vel_y = min(self.vel_y, self.falling_terminal_vel)

    def update_state(self):
        # Decidir animaciones según estado
        if self.is_in_air:
            new_state = "jump"

        #Si presionas R y el combo aún no inicio, inicia el combo
        elif self.combo_buffer and self.combo_step == 0:
            self.combo_buffer = False
            self.combo_step = 1
            new_state = "attack_1"
        #Si ya estas en medio de un combo, continuar con la animación actual
        elif self.combo_buffer and self.combo_step > 0:
            new_state = f"attack_{self.combo_step}"
            #self.combo_step += 1
        #Movimiento del personaje
        else:
            speed = abs(self.vel_x)
            if speed < 0.1:
                new_state = "idle"
            elif speed < self.max_walk_speed:
                new_state = "run"
            else:
                new_state = "run"

        #Si el estado cambió, reproducir animación
        if new_state != self.state:
            self.state = new_state

            if "attack" in new_state:
            # if new_state.startswith("attack"):
                self.anim.play(new_state, lock=True, on_end=lambda: self._finish_attack())
            else:
                self.anim.play(new_state)

    def _finish_attack(self):
        #Método para avanzar el combo de ataque
        if self.combo_buffer:
            self.combo_buffer = False
            self.combo_step += 1
            if self.combo_step > 3:
                self.combo_step = 0
            return

        # En este caso no hubo input entonces es el fin del combo
        self.combo_step = 0
        self.state = "idle"
        self.anim.play("idle")

    def resolve_collisions(self):
        """ Resolver colisiones verticales y horizontales con plataformas"""
        # Primero mover en x y verificar coliciones horizontales
        self.rect.x += self.vel_x
        hits = [p for p in self.platforms if self.rect.colliderect(p.rect)]
        for plat in hits:
            if self.vel_x > 0: # Nos movemos hacia la derecha
                self.rect.right = plat.rect.left
            elif self.vel_x < 0: # Nos movemos hacia la izquierda
                self.rect.left = plat.rect.right
            self.vel_x = 0

        # Ahora mover y verificar en el eje y
        self.rect.y += self.vel_y
        hits = [p for p in self.platforms if self.rect.colliderect(p.rect)]
        # Si coliciona verticalmente, ajustar y frenar la caida o salto
        for plat in hits:
            if self.vel_y > 0: #Estamos cayendo
                self.rect.bottom = plat.rect.top
                self.vel_y = 0
                self.is_in_air = False
            elif self.vel_y < 0: #Subiendo (saltando y choca con el techo)
                self.rect.top = plat.rect.bottom
                self.vel_y = 0


    def update(self):
        self.handle_input()
        self.apply_gravity()
        self.resolve_collisions()
        self.update_state()

        # actualiza animación
        self.anim.update()

        # actualiza posición según velocidad
        self.rect.x += self.vel_x

    def draw(self, screen):
        frame = self.anim.get_current_frame()
        #voltear la imagen si va en dirección izquierda
        if not self.facing_right:
            frame = pygame.transform.flip(frame, True, False)
        screen.blit(frame, (self.rect.x, self.rect.y))
