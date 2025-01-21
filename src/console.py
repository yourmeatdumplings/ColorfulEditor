from pygame.math import Vector2 as vec2

'''
Console module for Rooms & Doors.
You can use this module to interact with the Rooms & Doors console.
'''


# navigation
'''
Hold down the 'Ctrl' key and click Reach.
'''

#display

class Editor:
    Version: float = 0.1

class Display:
    # if True, it will define the size of the window.
    IsDefaultSize: bool = False
    # if True, it will display the window in your settings. else it will be in windowed mode.
    IsFullScreenState: bool = False
    # if default size is False, it will be the size of the window.
    Size: vec2 = vec2(1280, 720)
    # it's full windows size.
    FullSize: vec2 = vec2(1920, 1080)
    # display fill color.
    FillColor: str | tuple[int,int,int] = 'black'
    # display's title.
    Title: str = ''

class Page:
    Start: str = 'REPL'