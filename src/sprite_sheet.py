import pygame

class SpriteSheet:
    def __init__(self, filename, cols, rows):
        self.sheet = pygame.image.load(filename).convert_alpha()
        self.cols = cols
        self.rows = rows
        self.sheet_width = self.sheet.get_width()
        self.sheet_height = self.sheet.get_height()
        self.frame_width = self.sheet_width // cols
        self.frame_height = self.sheet_height // rows
        self.frames = []
        self.load_frames()

    def load_frames(self):
        for row in range(self.rows):
            for col in range(self.cols):
                x = col * self.frame_width
                y = row * self.frame_height
                rect = pygame.Rect(x, y, self.frame_width, self.frame_height)
                frame = self.sheet.subsurface(rect)
                self.frames.append(frame)
    
    def get_frame(self, index):
        return self.frames[index]
             
