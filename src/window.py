# define window full size, you can set it
import pygame
from src.console import Display

windows_title = 'ColorfulEditor' if not Display.Title else Display.Title

windows_state = pygame.FULLSCREEN if Display.IsFullScreenState else 0

windows_size = Display.FullSize if Display.IsDefaultSize else Display.Size