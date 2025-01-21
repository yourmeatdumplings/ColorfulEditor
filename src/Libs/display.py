from src.console import Display
from pygame.display import get_window_size

def get_size() -> tuple[int, int]:
    return get_window_size()

def get_global_width(width) -> int:
    return int(get_size()[0] / Display.Size.x * width)

def get_global_height(height) -> int:
    return int(get_size()[1] / Display.Size.y * height)

def get_global_size(width, height) -> tuple[int, int]:
    return (
        get_global_width(width),
        get_global_height(height)
    )