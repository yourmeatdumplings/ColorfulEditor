from src import default_font
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
            super(Box, self).on_draw(ui)