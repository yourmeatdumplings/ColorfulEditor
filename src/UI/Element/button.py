import pygame
from typing import Any
from src import default_font
from src.UI.Element.text_base import TextBase
from src.Style import TextStyle
from pygame.color import Color

class Button(TextBase):
    def __init__(self, text: str = 'Button', text_style: TextStyle = TextStyle.Center, text_x: int = 0, text_y: int = 0, text_size: int = 20, x: int = 0, y: int = 0, width: int = 100, height: int = 100, color: str | tuple[int, int, int] | Color = 'white', text_color: str | tuple[int, int, int] | Color = 'black', outline_size: int = 0, outline_color: str | tuple[int, int, int] | Color = 'green', mouse_color: str | tuple[int, int, int] | Color |None = None, button_color: str | tuple[int, int, int] | Color | None = None, font: str = default_font, state: bool = True, text_state: bool = True):
        super().__init__(text, text_style, text_x, text_y, text_size, x, y, width, height, color, text_color, outline_size, outline_color, font, state, text_state)

        self.mouse_color = mouse_color
        self.button_color = button_color

        self.func = print
        self.args: list[Any] = ['Button down!']
        self.kwargs: dict[str, Any] = {}

    def set_func(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def on_input(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.func(*self.args, **self.kwargs)