import pygame

class AnimatedSprite:
    def __init__(self, sprite_sheet, animation_ranges, frame_duration):
        """
        sprite_sheet: tu objeto SpriteSheet con todos los frames
        animation_ranges: dict con nombre de animación -> (inicio, fin) en índices de frames
        frame_duration: cuántos ticks de update se mantienen en cada frame de animación
        """
        self.sprite_sheet = sprite_sheet
        self.animation_ranges = animation_ranges
        self.frame_duration = frame_duration

        self.current_animation = None
        self.frame_index = 0
        self.frame_timer = 0

        # Por defecto, arrancar con la primera animación del dict (opcional)
        # self.play(next(iter(animation_ranges)))

    def play(self, animation_name):
        """Cambiar de animación."""
        if animation_name not in self.animation_ranges:
            raise ValueError(f"Animación desconocida: {animation_name}")
        if animation_name != self.current_animation:
            self.current_animation = animation_name
            start, end = self.animation_ranges[animation_name]
            self.frame_index = start
            self.frame_timer = 0

    def update(self):
        """Actualizar el frame de animación según el frame_duration."""
        if self.current_animation is None:
            return

        self.frame_timer += 1
        if self.frame_timer >= self.frame_duration:
            self.frame_timer = 0
            start, end = self.animation_ranges[self.current_animation]
            # Avanzar el índice dentro del rango
            self.frame_index += 1
            if self.frame_index >= end:
                self.frame_index = start

    def get_current_frame(self):
        """Devuelve la Surface del frame actual."""
        return self.sprite_sheet.get_frame(self.frame_index)
