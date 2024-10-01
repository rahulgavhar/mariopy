import pygame as pg
import os


class Tube(pg.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, 'images', 'tube.png')
        self.image = pg.image.load(file_path).convert_alpha()
        length = (12 - y_pos) * 32
        self.image = self.image.subsurface(0, 0, 64, length)
        self.rect = pg.Rect(x_pos * 32, y_pos * 32, 64, length)

    def render(self, core):
        core.screen.blit(self.image, core.get_map().get_camera().apply(self))
