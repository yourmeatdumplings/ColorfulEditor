from pygame.transform import scale

from src.UI.Element import Element
from src.Libs.display import get_global_size
import pygame

class Box(Element):
    def __init__(self, x: int = 0, y: int = 0, width: int = 100, height: int = 100, state: bool = True):
        super().__init__(state)

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.box = pygame.Surface((self.width, self.height))
        self.box.set_alpha(0)
        self.rect = self.box.get_rect()

    def set_width(self, __width):
        self.width = __width
    def set_height(self, __height):
        self.height = __height
    def set_x(self, __x):
        self.x = __x
    def set_y(self, __y):
        self.y = __y

    def add_width(self, __width):
        self.width += __width
    def add_height(self, __height):
        self.height += __height
    def add_x(self, __x):
        self.x += __x
    def add_y(self, __y):
        self.y += __y
    def on_draw(self, ui):
        super().on_draw(ui)
        self.box = scale(self.box, get_global_size(self.width, self.height))
        self.rect = self.box.get_rect()
        self.rect.topleft = get_global_size(self.world_x, self.world_y)
        ui.surface_display.blit(self.box, self.rect)