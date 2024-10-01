import pygame as pg
import os
from Const import *
from Text import Text
current_dir = os.path.dirname(os.path.abspath(__file__))

class MainMenu(object):
    def __init__(self):
        self.mainImage = pg.image.load(f'{current_dir}/images\super_mario_bros.png').convert_alpha()

        self.toStartText = Text('ENTER DABAIYE', 16, (WINDOW_W - WINDOW_W * 0.72, WINDOW_H - WINDOW_H * 0.3))

    def render(self, core):
        core.screen.blit(self.mainImage, (50, 50))
        self.toStartText.render(core)
