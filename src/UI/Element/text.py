import pygame
from src import default_font, get_global_height
from src.Libs.display import get_global_size
from src.UI import Element
from pygame.color import Color

class Text(Element):
    def __init__(self, text: str = '', x: int = 0, y: int = 0, size: int = 20, color: str | tuple[int,int,int] | Color = 'white', font: str = default_font, state: bool = True):
        pygame.init()

        super().__init__(state)

        self.text_x = x
        self.text_y = y
        self.text = text
        self.font = font
        self.color = color
        self.text_size = size

        font_surf = pygame.font.Font(self.font, get_global_height(self.text_size))
        self.text_surface = font_surf.render(str(self.text), True, self.color)
        self.text_rect = self.text_surface.get_rect()

    def set_text(self, __text):
        self.text = __text
    def set_text_x(self, __x):
        self.text_x = __x
    def set_text_y(self, __y):
        self.text_y = __y
    def add_text_x(self, __x):
        self.text_x += __x
    def add_text_y(self, __y):
        self.text_y += __y

    def on_draw(self, ui):
        super().on_draw(ui)
        font_surf = pygame.font.Font(self.font, get_global_height(self.text_size))
        self.text_surface = font_surf.render(str(self.text), True, self.color)
        self.text_rect = self.text_surface.get_rect(topleft=get_global_size(self.text_x, self.text_y))
        ui.surface_display.blit(self.text_surface, self.text_rect)