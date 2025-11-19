import pygame

class SpriteSheet:
    def __init__(self, image, frame_width, frame_height):
        self.sheet = image
        self.frame_width = frame_width
        self.frame_height = frame_height

    def get_frame(self, col, row):
        """Devuelve un subsurface para el frame en la columna col y fila row."""
        rect = pygame.Rect(
            col * self.frame_width,
            row * self.frame_height,
            self.frame_width,
            self.frame_height
        )
        # sub superficie
        image = pygame.Surface((self.frame_width, self.frame_height), pygame.SRCALPHA)
        image.blit(self.sheet, (0, 0), rect)
        return image

    def get_animation_frames(self, row, num_frames):
        """Devuelve una lista de frames de una misma fila (animación)."""
        frames = []
        for col in range(num_frames):
            frames.append(self.get_frame(col, row))
        return frames
