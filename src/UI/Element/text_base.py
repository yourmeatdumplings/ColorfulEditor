from src import default_font
from src.UI.Element.base import Base
from src.UI.Element.box import Box
from src.UI.Element.text import Text
from src.Style import TextStyle
from pygame.color import Color

class TextBase(Base, Text):
    def __init__(self, text: str = '', text_style: TextStyle = TextStyle.Center, text_x: int = 0, text_y: int = 0, text_size: int = 20, x: int = 0, y: int = 0, width: int = 100, height: int = 100, color: str | tuple[int, int, int] | Color = 'white', text_color: str | tuple[int, int, int] | Color = 'black', outline_size: int = 0, outline_color: str | tuple[int, int, int] = 'green', font: str = default_font, state: bool = True, text_state: bool = True):
        super().__init__(x, y, width, height, color, outline_size, outline_color, state)
        super(Box, self).__init__(text, text_x + x, text_y + y, text_size, text_color, font, state)

        self.__text_x = text_x
        self.__text_y = text_y

        self.text_style = text_style

        self.text_state = text_state

    def __style(self):
        match self.text_style:
            case TextStyle.Center:
                self.text_x = self.x + self.width / 2 - self.text_rect.width / 2
                self.text_y = self.y + self.height / 2- self.text_rect.height / 2
            case TextStyle.CenterTop:
                self.text_x = self.x + self.width / 2 - self.text_rect.width / 2
                self.text_y = self.y
            case TextStyle.CenterBottom:
                self.text_x = self.x + self.width / 2 - self.text_rect.width / 2
                self.text_y = self.y + self.text_rect.height
            case TextStyle.CenterLeft:
                self.text_x = self.x
                self.text_y = self.y + self.height / 2- self.text_rect.height / 2
            case TextStyle.CenterRight:
                self.text_x = self.x + self.text_rect.width
                self.text_y = self.y + self.height / 2- self.text_rect.height / 2
            case TextStyle.LeftTop:
                self.text_x = self.x
                self.text_y = self.y
            case TextStyle.LeftBottom:
                self.text_x = self.x
                self.text_y = self.y + self.text_rect.height
            case TextStyle.RightTop:
                self.text_x = self.x + self.text_rect.width
                self.text_y = self.y
            case TextStyle.RightBottom:
                self.text_x = self.x + self.text_rect.width
                self.text_y = self.y + self.text_rect.height
            case TextStyle.No:
                self.text_x = self.x + self.__text_x
                self.text_y = self.y + self.__text_y

    def on_draw(self, ui):
        self.__style()
        super().on_draw(ui)
        if self.text_state:
            super(Box, self).on_draw(ui)