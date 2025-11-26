from entity import Entity

class Enemy(Entity):
    def __init__(self, x, y, platforms, sprite_sheet, animation_ranges):
        #Llama al constructor de la superclase
        super().__init__(x, y, platforms, sprite_sheet, animation_ranges)

        self.hp = 10
        self.damage = 5

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.die()

    def die(self):
        #logica de muerte, por ejemplo eliminar de la lista de sprites y liberar memoria
        pass

    #Sobreescribir el update_state para la IA básica
    def update_state(self):
        #lógica de IA, perseguir al jugador
        if self.is_in_air:
            new_state = "jump"
        elif abs(self.vel_x) > 0:
            new_state = "walk"
        else:
            new_state = "idle"

        if new_state != self.state:
            self.state = new_state
            self.anim.play(new_state)

    def update(self):
        #Lógica de movimiento del enemigo IA
        self.update_state()
        super().update() #llama al update de entity para físicas y animaciones