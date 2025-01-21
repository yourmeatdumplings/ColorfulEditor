from pygame import Surface
from src.Libs.display import get_global_size
from pygame.transform import scale

class Texture2D:
    def __init__(self, surface: Surface):
        self.image = surface
        self.rect = self.image.get_rect()

        self.__width, self.__height = self.rect.size

    def draw(self, x :int, y: int, surface: Surface):
        self.image = scale(self.image, get_global_size(self.__width, self.__height))
        self.rect = self.image.get_rect()
        self.rect.topleft = get_global_size(x, y)
        surface.blit(self.image, self.rect)