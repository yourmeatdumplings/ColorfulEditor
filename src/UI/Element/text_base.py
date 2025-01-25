import pygame

from src import default_font, get_global_height
from src.Libs.display import get_global_size
from src.UI.Element.base import Base
from src.UI.Element.box import Box
from src.UI.Element.text import Text
from pygame.color import Color

class TextBase(Base, Text):
    def __init__(self, text: str = '', text_style: str = 'center', text_x: int = 0, text_y: int = 0, text_size: int = 20, x: int = 0, y: int = 0, width: int = 100, height: int = 100, color: str | tuple[int, int, int] | Color = 'white', text_color: str | tuple[int, int, int] | Color = 'black', outline_size: int = 0, outline_color: str | tuple[int, int, int] = 'green', font: str = default_font, state: bool = True, text_state: bool = True):
        super().__init__(x, y, width, height, color, outline_size, outline_color, state)
        super(Box, self).__init__(text, text_x + x, text_y + y, text_size, text_color, font, state)

        self.__text_x = text_x
        self.__text_y = text_y

        self.text_x = text_x
        self.text_y = text_y
        self.world_text_x = text_x
        self.world_text_y = text_x

        self.text_style = text_style

        self.text_state = text_state

    def __style(self):
        match self.text_style:
            case 'center':
                self.text_x = self.x + self.width / 2 - self.text_rect.width / 2
                self.text_y = self.y + self.height / 2- self.text_rect.height / 2
            case 'center-top':
                self.text_x = self.x + self.width / 2 - self.text_rect.width / 2
                self.text_y = self.y
            case 'center-bottom':
                self.text_x = self.x + self.width / 2 - self.text_rect.width / 2
                self.text_y = self.y + self.text_rect.height
            case 'center-left':
                self.text_x = self.x
                self.text_y = self.y + self.height / 2- self.text_rect.height / 2
            case 'center-right':
                self.text_x = self.x + self.text_rect.width
                self.text_y = self.y + self.height / 2- self.text_rect.height / 2
            case 'left-top':
                self.text_x = self.x
                self.text_y = self.y
            case 'left-bottom':
                self.text_x = self.x
                self.text_y = self.y + self.text_rect.height
            case 'right-top':
                self.text_x = self.x + self.text_rect.width
                self.text_y = self.y
            case 'left-bottom':
                self.text_x = self.x + self.text_rect.width
                self.text_y = self.y + self.text_rect.height
            case '':
                self.text_x = self.x + self.__text_x
                self.text_y = self.y + self.__text_y

    def on_draw(self, ui):
        self.__style()
        super().on_draw(ui)
        if self.text_state:
            if self.parent:
                self.world_text_x, self.world_text_y =  (self.text_x + self.out_x + self.parent.world_x, self.text_y + self.out_y + self.parent.world_y)
            else:
                self.world_text_x, self.world_text_y = self.x, self.y

            font_surf = pygame.font.Font(self.font, get_global_height(self.text_size))
            self.text_surface = font_surf.render(str(self.text), True, self.color)
            self.text_rect = self.text_surface.get_rect(topleft=get_global_size(self.world_text_x, self.world_text_y))
            ui.surface_display.blit(self.text_surface, self.text_rect)