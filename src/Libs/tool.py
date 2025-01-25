from src.Libs.display import get_global_height
from src.Path import default_font
from src.Port import *
from pygame.color import Color
import sys
import pygame

def draw_text(text, font: str = default_font, size: int = 30, color: str | tuple[int, int, int] | Color = 'white', x: int = 0, y: int = 0) -> None:
    pygame.init()
    surface_display = pygame.display.get_surface()
    font_surface = pygame.font.Font(font, get_global_height(size))
    surface = font_surface.render(str(text), True, color)
    rect = surface.get_rect(topleft=(x, y))
    surface_display.blit(surface, rect)

def exit_game() -> None:
    print(f'{Client}: 退出游戏!')
    pygame.quit()
    sys.exit()