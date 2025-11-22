import pygame

class SpriteSheet:
    def __init__(self, filename, anim_cols, anim_rows):
        self.sheet = pygame.image.load(filename).convert_alpha() #if pygame.display.get_surface() else pygame.image.load(filename)
        self.cols = anim_cols
        self.rows = anim_rows
        self.sheet_width = self.sheet.get_width()
        self.sheet_height = self.sheet.get_height()
        self.frame_width = self.sheet_width // anim_cols
        self.frame_height = self.sheet_height // anim_rows
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
             
