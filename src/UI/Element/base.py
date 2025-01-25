from pygame import Surface
from pygame.transform import scale
from pygame.color import Color
from src.Libs.display import get_global_size
from src.UI.Element.box import Box

class Base(Box):
    def __init__(self, x: int = 0, y: int = 0, width: int = 100, height: int = 100, color: str | tuple[int, int, int] | Color = 'white', outline_size: int = 0, outline_color: str | tuple[int, int, int] | Color = 'green',state: bool = True):
        super().__init__(x, y, width, height, state)
        self.color = color
        self.outline_size = outline_size
        self.outline_color = outline_color

        self.outline_base: Surface = self.box.copy()
        self.outline_base.fill(self.outline_color)
        self.outline_base_rect = self.outline_base.get_rect()

        self.base = Surface((self.width - 2 * self.outline_size, self.height - 2 * self.outline_size))
        self.base.fill(self.color)
        self.base_rect = self.base.get_rect()

    def set_color(self, __color):
        self.color = __color
    def set_outline_color(self, __color):
        self.outline_color = __color
    def set_outline_size(self, __size):
        self.outline_size = __size

    def on_draw(self, ui):
        super().on_draw(ui)
        self.outline_base = scale(self.outline_base, get_global_size(self.width, self.height))
        self.outline_base_rect = self.outline_base.get_rect(topleft = get_global_size(self.world_x, self.world_y))
        ui.surface_display.blit(self.outline_base, self.outline_base_rect)

        self.base = scale(self.base, get_global_size(self.width - 2 * self.outline_size, self.height - 2 * self.outline_size))
        self.base_rect = self.base.get_rect(topleft = get_global_size(self.world_x + self.outline_size, self.world_y + self.outline_size))
        ui.surface_display.blit(self.base, self.base_rect)